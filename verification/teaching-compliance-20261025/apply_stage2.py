from pathlib import Path
from datetime import datetime
import hashlib,json
OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[1]
P=OUT/'proposed'
sha=lambda b:hashlib.sha256(b).hexdigest()
changes=[]
for group in ('memory','eye','place'):
    d=json.loads((OUT/f'stage2-{group}.json').read_text(encoding='utf-8'))
    for edit in d.get('proposed_repairs',d.get('findings',[])):
        name=edit.get('file',edit.get('passage',{}).get('file'))
        path=P/'content/chapters'/Path(name).name
        old=path.read_bytes(); text=old.decode('utf-8')
        before,after=edit['before'],edit['after']
        assert text.count(before)==1,(edit['id'],path,text.count(before))
        new=text.replace(before,after).encode('utf-8')
        path.write_bytes(new)
        changes.append({'id':edit['id'],'file':path.relative_to(P).as_posix(),'before':before,'after':after,'old_sha256':sha(old),'new_sha256':sha(new),'decision':'accept','reason':edit.get('reason',edit.get('deletion_test'))})
    if group=='memory':
        path=P/'content/chapters/02-memory-dynamics.yaml'
        old=path.read_bytes();text=old.decode('utf-8')
        before='can we write it using tuning curves and the input to rate rule?'
        after='can we express it through the tuning curves and neural transfer function?'
        if before in text:
            assert text.count(before)==1
            new=text.replace(before,after).encode('utf-8');path.write_bytes(new)
            changes.append({'id':'M-S2-07-sidecar','file':path.relative_to(P).as_posix(),'before':before,'after':after,'old_sha256':sha(old),'new_sha256':sha(new),'decision':'accept','reason':'Match the accepted section opening while retaining the same question and symmetric-weight condition.'})
(OUT/'repairs-v2.json').write_text(json.dumps({'at':datetime.now().astimezone().isoformat(),'edits':changes},ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'accepted_repairs':len(changes),'files':sorted({x['file'] for x in changes})}))
