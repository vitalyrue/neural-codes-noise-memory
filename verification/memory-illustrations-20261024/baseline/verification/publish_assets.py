"""Copy registered papers and apply authored local presentation additions.

The PDF links are part of the authored reading-path chapter. Publisher handles
the book prose and figure assets; this small project helper supplies the paper
downloads and records their exact hashes. Scientific-figure CSS is authored in
assets/styles/illustrations.css, then copied into the built stylesheet. This
does not modify rendered teaching prose.
"""
from pathlib import Path
import hashlib,json,shutil,datetime,re
import yaml
ROOT=Path(__file__).resolve().parents[1]
manifest=yaml.safe_load((ROOT/"sources/source-manifest.yaml").read_text())
target=ROOT/"site/papers";target.mkdir(parents=True,exist_ok=True)
copied=[]
for source in manifest["sources"]:
    src=ROOT/source["path"]
    digest=hashlib.sha256(src.read_bytes()).hexdigest()
    if digest!=source["sha256"]:raise ValueError(f"Source changed: {src}")
    dest=target/src.name
    shutil.copy2(src,dest)
    copied.append({"source":source["path"],"output":str(dest.relative_to(ROOT)).replace("\\","/"),"sha256":digest})
index=ROOT/'site/index.html'
before=hashlib.sha256(index.read_bytes()).hexdigest()
html=index.read_text(encoding='utf-8')
# Build identifiers are evidence for the project records, not a study concept.
html,count=re.subn(r'<dl class="publisher-build-meta"[^>]*>.*?</dl>\s*','',html,flags=re.S)
if count>1:raise ValueError('Unexpected repeated build metadata block')
index.write_text(html,encoding='utf-8',newline='\n')
record={"checked_at":datetime.datetime.now().astimezone().isoformat(),"assets":copied,"index_presentation":{"removed_build_metadata_blocks":count,"before_sha256":before,"after_sha256":hashlib.sha256(index.read_bytes()).hexdigest(),"reason":"Keep publication tooling details in the saved build records rather than the reader introduction."}}
figure_css=ROOT/'assets/styles/illustrations.css'
if figure_css.exists():
    stylesheet=ROOT/'site/styles.css'
    marker='/* BEGIN book illustration styles */'
    original_css=stylesheet.read_text(encoding='utf-8').split(marker)[0].rstrip()
    stylesheet.write_text(original_css+'\n\n'+marker+'\n'+figure_css.read_text(encoding='utf-8')+'\n/* END book illustration styles */\n',encoding='utf-8')
    record['illustration_styles']={'source':'assets/styles/illustrations.css','source_sha256':hashlib.sha256(figure_css.read_bytes()).hexdigest(),'output':'site/styles.css','output_sha256':hashlib.sha256(stylesheet.read_bytes()).hexdigest()}
(ROOT/"verification/publication/paper-assets.json").write_text(json.dumps(record,indent=2),encoding="utf-8")
print(f"Published {len(copied)} paper assets with checked hashes.")
