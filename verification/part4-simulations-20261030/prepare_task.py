from pathlib import Path
from datetime import datetime, timezone
import shutil, json, hashlib

root=Path(__file__).resolve().parents[2]
task=Path(__file__).resolve().parent
paths=[root/'plan/chapter-plan.yaml',root/'plan/structural-locks/current.yaml',root/'guide-project.yaml',root/'content/index.md',root/'CURRENT_STATE.md',root/'verification/semantic-review-ledger.yaml']
paths+=list((root/'content/chapters').glob('*.md'))+list((root/'content/chapters').glob('*.yaml'))+list((root/'source-maps').glob('*.csv'))
manifest={}
for path in paths:
    rel=path.relative_to(root)
    dest=task/'baseline'/rel
    assert not dest.exists(), f'Baseline already exists: {dest}'
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(path,dest)
    manifest[rel.as_posix()]=hashlib.sha256(path.read_bytes()).hexdigest()
(task/'baseline-hashes.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
p=task/'STATE.json'; state=json.loads(p.read_text(encoding='utf-8'))
state['checkpoint_at']=datetime.now(timezone.utc).isoformat()
state['baseline_files']=len(manifest)
state['doctor']='matched locks; attention: 8 reusable, 12 required; prior review/figure holds retained'
p.write_text(json.dumps(state,indent=2),encoding='utf-8')
print({'baseline_files':len(manifest),'checkpoint_at':state['checkpoint_at']})
