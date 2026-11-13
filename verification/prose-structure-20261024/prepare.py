from pathlib import Path
from datetime import datetime
import hashlib,json,shutil
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[1]
paths=[*sorted((ROOT/'content/chapters').glob('*')),ROOT/'plan/chapter-plan.yaml',ROOT/'plan/structural-locks/current.yaml',ROOT/'guide-project.yaml',ROOT/'source-maps/terminology-ledger.yaml',ROOT/'source-maps/visual-ledger.yaml',ROOT/'source-maps/chapter-redirects.json',ROOT/'assets/styles/reading.css',ROOT/'assets/styles/illustrations.css',ROOT/'verification/manifests/build-manifest.json',ROOT/'verification/publish_assets.py']
hashes={}
for p in paths:
 if p.is_file():
  rel=p.relative_to(ROOT);target=OUT/'baseline'/rel;target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,target);hashes[rel.as_posix()]=hashlib.sha256(p.read_bytes()).hexdigest()
assets={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in (ROOT/'assets/approved/visuals').iterdir() if p.is_file()}
(OUT/'baseline/hashes.json').write_text(json.dumps({'sources':hashes,'assets':assets},indent=2),encoding='utf-8')
(OUT/'proposed/content/chapters').mkdir(parents=True,exist_ok=True)
(OUT/'RUN.md').write_text('# Paragraph structure revision\n\nStart2026-10-24T21:32:54.8366363+03:00. Plan: read synthesis and guide flow; parallel chapter proposals; independent truth, wording and flow review; integrate with preserved science; rebuild local HTML; inspect three browser samples. ETA20–30minutes. GPT-6 lead exactvariantunexposed; GPT-6.1-sol/high paragraph reviewers. Awake time unverified.\n',encoding='utf-8')
print(json.dumps({'at':datetime.now().astimezone().isoformat(),'snapshots':len(hashes),'assets':len(assets)}))
