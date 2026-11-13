from pathlib import Path
from datetime import datetime
import hashlib,json,shutil,re,yaml
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
paths=list((ROOT/'content/chapters').glob('*.md'))+list((ROOT/'content/chapters').glob('*.yaml'))
paths +=[ROOT/p for p in ['guide-project.yaml','plan/chapter-plan.yaml','publisher-lock.yaml','skill-lock.yaml','source-maps/terminology-ledger.yaml','source-maps/visual-ledger.yaml','source-maps/source-coverage.csv','source-maps/research-ledger.csv','references/bibliography/reference-register.json','verification/semantic-review-ledger.yaml','assets/styles/reading.css','assets/styles/illustrations.css']]
records={}
for p in paths:
 rel=p.relative_to(ROOT);target=OUT/'baseline'/rel
 assert not target.exists(),target
 target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,target);records[rel.as_posix()]=sha(p)
assets={p.relative_to(ROOT).as_posix():sha(p) for folder in ['assets/approved/visuals','assets/papers','assets/styles'] for p in (ROOT/folder).rglob('*') if p.is_file()}
rulesroot=Path('C:/dev/NBIS/publisher-releases/0.8.23/skills/course-study-guide-builder')
rules={p.relative_to(rulesroot).as_posix():sha(p) for p in rulesroot.rglob('*.md')}
(OUT/'baseline/hashes.json').write_text(json.dumps({'at':datetime.now().astimezone().isoformat(),'sources':records,'assets':assets,'rules':rules},indent=2),encoding='utf-8')
frame=[]
for p in sorted((ROOT/'content/chapters').glob('*.md')):
 text=p.read_text(encoding='utf-8');meta=yaml.safe_load(p.with_suffix('.yaml').read_text(encoding='utf-8'))
 heads=re.findall(r'^#{1,6} .+$',text,re.M)
 before=text.split('\n## ',1)[0]
 body=text.split('\n[^',1)[0]
 frame.append({'file':p.name,'chapter':meta['chapter_id'],'opening':before,'headings':heads,'ending':'\n\n'.join(body.strip().split('\n\n')[-3:]),'blocks':[{k:b.get(k) for k in ['id','kind','caption','alt_text','path']} for b in meta.get('blocks',[])]})
(OUT/'book-frame.json').write_text(json.dumps(frame,indent=2,ensure_ascii=False),encoding='utf-8')
print(json.dumps({'source_files':len(records),'assets':len(assets),'reader_files':len(frame),'at':datetime.now().astimezone().isoformat()}))
