"""Copy registered papers and apply authored local presentation additions.

The PDF links are part of the authored reading-path chapter. Publisher handles
the book prose and figure assets; this small project helper supplies the paper
downloads and records their exact hashes. Figure and reading CSS are authored in
assets/styles and copied into the built stylesheet. The chapter redirect map
preserves bookmarks after chapter division. These additions do not rewrite prose.
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
reading_css=ROOT/'assets/styles/reading.css'
if reading_css.exists():
    stylesheet=ROOT/'site/styles.css'
    marker='/* BEGIN book reading styles */'
    original_css=stylesheet.read_text(encoding='utf-8').split(marker)[0].rstrip()
    stylesheet.write_text(original_css+'\n\n'+marker+'\n'+reading_css.read_text(encoding='utf-8')+'\n/* END book reading styles */\n',encoding='utf-8',newline='\n')
    record['reading_styles']={'source':'assets/styles/reading.css','source_sha256':hashlib.sha256(reading_css.read_bytes()).hexdigest(),'output':'site/styles.css','output_sha256':hashlib.sha256(stylesheet.read_bytes()).hexdigest(),'scope':'Screen typography; original print rules retained.'}
redirects=ROOT/'source-maps/chapter-redirects.json'
if redirects.exists():
    mapping=json.loads(redirects.read_text(encoding='utf-8'))
    script=ROOT/'site/scripts/chapter-redirects.js';script.parent.mkdir(exist_ok=True)
    script.write_text('/* Preserve section bookmarks after chapter division. */\n(()=>{const routes='+json.dumps(mapping)+';const page=location.pathname.split("/").pop();const target=routes[page]?.[decodeURIComponent(location.hash.slice(1))];if(target){const url=new URL(target,location.href);url.search=location.search;url.hash=location.hash;location.replace(url.href);}})();\n',encoding='utf-8',newline='\n')
    for page in (ROOT/'site').rglob('*.html'):
        if 'site_libs' in page.parts:continue
        markup=page.read_text(encoding='utf-8')
        markup=re.sub(r'<script[^>]+data-chapter-redirects[^>]*></script>\s*','',markup)
        relative=__import__('os').path.relpath(script,page.parent).replace('\\','/')
        markup=markup.replace('</head>',f'<script src="{relative}" data-chapter-redirects defer></script>\n</head>')
        page.write_text(markup,encoding='utf-8',newline='\n')
    record['chapter_bookmarks']={'source':'source-maps/chapter-redirects.json','sha256':hashlib.sha256(redirects.read_bytes()).hexdigest(),'moved_anchors':sum(len(x) for x in mapping.values())}
for style_record in ['illustration_styles','reading_styles']:
    if style_record in record:record[style_record]['output_sha256']=hashlib.sha256((ROOT/'site/styles.css').read_bytes()).hexdigest()
# Give changed shared styles a new URL so existing VPN browser tabs load them.
style_version=hashlib.sha256((ROOT/'site/styles.css').read_bytes()).hexdigest()[:12]
style_pages=0
for page in (ROOT/'site').rglob('*.html'):
    markup=page.read_text(encoding='utf-8')
    markup,n=re.subn(r'href="((?:\.\./)*styles\.css)(?:\?v=[a-f0-9]+)?"',
                    lambda m: f'href="{m.group(1)}?v={style_version}"',markup)
    if n:
        page.write_text(markup,encoding='utf-8',newline='\n')
        style_pages+=1
record['style_cache_version']={'sha256_prefix':style_version,'pages':style_pages}
record['final_index_sha256']=hashlib.sha256(index.read_bytes()).hexdigest()
(ROOT/"verification/publication/paper-assets.json").write_text(json.dumps(record,indent=2),encoding="utf-8")
print(f"Published {len(copied)} paper assets with checked hashes.")
