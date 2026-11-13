from pathlib import Path
from datetime import datetime
import hashlib, json, shutil
OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[1]
paths=[*sorted((ROOT/'content/chapters').glob('*.md')),*sorted((ROOT/'content/chapters').glob('*.yaml'))]
paths += [ROOT/n for n in ['guide-project.yaml','plan/chapter-plan.yaml','plan/structural-locks/current.yaml','source-maps/terminology-ledger.yaml','source-maps/visual-ledger.yaml','verification/manifests/build-manifest.json','publisher-lock.yaml','skill-lock.yaml']]
hashes={}
for path in paths:
    rel=path.relative_to(ROOT)
    dest=OUT/'baseline'/rel
    assert not dest.exists(),str(dest)
    dest.parent.mkdir(parents=True,exist_ok=True)
    shutil.copy2(path,dest)
    hashes[rel.as_posix()]=hashlib.sha256(path.read_bytes()).hexdigest()
assets={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in (ROOT/'assets/approved').rglob('*') if p.is_file()}
(OUT/'baseline/hashes.json').write_text(json.dumps({'at':datetime.now().astimezone().isoformat(),'sources':hashes,'approved_assets':assets},indent=2),encoding='utf-8')
print(json.dumps({'files_snapshotted':len(paths),'assets_hashed':len(assets)}))
