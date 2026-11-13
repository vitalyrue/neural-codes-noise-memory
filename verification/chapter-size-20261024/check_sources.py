from pathlib import Path
from datetime import datetime
from collections import Counter
import hashlib,json,re,yaml
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[1]
read=lambda p:p.read_text(encoding='utf-8')
load=lambda p:json.loads(read(p))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
integration=load(OUT/'integration.json');edits=load(OUT/'reference-edits.json')
def units(text):
 body=re.split(r'(?m)^\[\^[^\]]+\]:',text)[0]
 starts=list(re.finditer(r'(?m)^## .+? \{#([^}]+)\}\s*$',body))
 return {m.group(1):body[m.start():starts[i+1].start() if i+1<len(starts) else len(body)].strip() for i,m in enumerate(starts)}
def canonical_links(text):
 for old,anchors in load(ROOT/'source-maps/chapter-redirects.json').items():
  for anchor,new in anchors.items():text=text.replace(old+'#'+anchor,new+'#'+anchor)
 return text
rows=[];oldblocks=[];newblocks=[];source_hashes={}
for row in integration['chapters']:
 source=ROOT/row['file'];text=read(source);old=read(OUT/'baseline'/row['original']);original=units(old)
 for before,after in edits.get(Path(row['original']).name,[]):
  original={k:v.replace(before,after) for k,v in original.items()}
 current=units(text)
 expected={k:canonical_links(original[k]) for k in row['sections']}
 differences=[k for k in expected if current.get(k)!=expected[k]]
 display_math=lambda s:re.findall(r'(?ms)^\$\$\s*\n(.*?)^\$\$',s)
 body='\n\n'.join(current.values());expectedbody='\n\n'.join(expected.values())
 meta=yaml.safe_load(read(source.with_suffix('.yaml')));newblocks+=meta.get('blocks',[])
 rows.append({'chapter':row['chapter'],'section_count':len(current),'body_words':len(body.split()),'unexpected_section_changes':differences,'display_math_preserved':display_math(body)==display_math(expectedbody),'intro_before_first_section':len(text.split('\n## ',1)[0].split('\n\n'))>=3,'folds':body.count('.publisher-fold-always'),'status':'pass' if not differences and display_math(body)==display_math(expectedbody) else 'fail'})
 source_hashes[row['file']]=sha(source);source_hashes[str(Path(row['file']).with_suffix('.yaml')).replace('\\','/')]=sha(source.with_suffix('.yaml'))
for original in sorted({r['original'] for r in integration['chapters']}):oldblocks+=yaml.safe_load(read((OUT/'baseline'/original).with_suffix('.yaml'))).get('blocks',[])
block_key=lambda b:b['id']
blocks_preserved=sorted(oldblocks,key=block_key)==sorted(newblocks,key=block_key)
assets_preserved=all(sha(ROOT/p)==h for p,h in integration['approved_assets'].items())
report={'at':datetime.now().astimezone().isoformat(),'rows':rows,'blocks_preserved':blocks_preserved,'assets_preserved':assets_preserved,'source_hashes':source_hashes,'status':'pass' if all(r['status']=='pass' for r in rows) and blocks_preserved and assets_preserved else 'fail'}
(OUT/'source-check.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps({k:report[k] for k in ['status','blocks_preserved','assets_preserved']}));print(json.dumps(rows,indent=2))
raise SystemExit(0 if report['status']=='pass' else 1)
