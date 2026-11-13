from pathlib import Path
from datetime import datetime
import json,hashlib,shutil
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
rows=[]
for p in sorted((OUT/'proposed').rglob('*')):
    if not p.is_file() or '__pycache__' in p.parts:continue
    rel=p.relative_to(OUT/'proposed');target=ROOT/rel
    assert target.is_file(),str(rel)
    backup=OUT/'baseline'/rel
    if not backup.exists():
        backup.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(target,backup)
    before=sha(backup);after=sha(p)
    if before==after:continue
    target.write_bytes(p.read_bytes())
    rows.append({'file':rel.as_posix(),'before_sha256':before,'after_sha256':after})
(OUT/'integration.json').write_text(json.dumps({'at':datetime.now().astimezone().isoformat(),'changes':rows},indent=2),encoding='utf-8')
print(json.dumps({'changed_files':len(rows),'files':[r['file'] for r in rows]}))
