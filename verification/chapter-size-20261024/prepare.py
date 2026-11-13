from pathlib import Path
from datetime import datetime
import hashlib,json,shutil,re,yaml
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[1]
paths=[*sorted((ROOT/'content/chapters').glob('*')),
 ROOT/'guide-project.yaml',ROOT/'plan/chapter-plan.yaml',ROOT/'plan/structural-locks/current.yaml',
 *sorted((ROOT/'source-maps').glob('*')),
 ROOT/'verification/publish_assets.py',ROOT/'verification/manifests/build-manifest.json',
 ROOT/'assets/styles/illustrations.css']
hashes={}
for p in paths:
 if not p.is_file():continue
 rel=p.relative_to(ROOT);dest=OUT/'baseline'/rel;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,dest)
 hashes[rel.as_posix()]=hashlib.sha256(p.read_bytes()).hexdigest()
(OUT/'baseline/hashes.json').write_text(json.dumps(hashes,indent=2),encoding='utf-8')
rows=[]
for p in sorted((ROOT/'content/chapters').glob('0[1-6]*.md')):
 text=p.read_text(encoding='utf-8');parts=re.split(r'(?m)(?=^## )',text.split('\n[^',1)[0])
 rows.append({'file':p.name,'sections':[{'heading':s.split('\n')[0],'words':len(s.split())} for s in parts[1:]],'words':len(text.split())})
(OUT/'inventory.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
(OUT/'RUN.md').write_text('# Chapter size and overview revision\n\nStart 2026-10-24T20:17:28.7375959+03:00. Plan: inspect natural boundaries; parallel read-only chapter proposals; preserve source and add motivated openings; reduce screen fonts once by30percent and save future default; review split boundaries/openings; rebuild local HTML and sample three pages. Estimate20–30minutes. Model GPT-6 lead, exact variant not exposed; GPT-6.1-sol/high structural reviewers. Awake time unverified.\n',encoding='utf-8')
print(json.dumps({'at':datetime.now().astimezone().isoformat(),'snapshot_files':len(hashes),'chapters':rows},indent=2))
