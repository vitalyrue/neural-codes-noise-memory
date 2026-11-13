from pathlib import Path
from datetime import datetime,timezone
import subprocess,json,uuid,hashlib
root=Path(__file__).resolve().parent
call=root/'access-check';call.mkdir(exist_ok=True)
assert not (call/'RESULT.json').exists(),'Preserve existing attempt'
exe=r'C:/nvm4w/nodejs/node_modules/@opencode/cli/bin/opencode.exe'
model='opencode/nemotron-3.5-super-vl-free#high'
prompt='Access check only, not the book review. Read the supplied file '+str(root/'inputs/SMOKE.txt')+' and return its exact one-line content. No other tools or file writes. Do not plan or ask questions.'
request={'local_request_id':str(uuid.uuid4()),'started_utc':datetime.now(timezone.utc).isoformat(),'model':model,'agent':'neuro-review','prompt':prompt,'purpose':'Test exact Nemotron route, JSON event format, stdin input and allowed frozen-file read.'}
(call/'REQUEST.json').write_text(json.dumps(request,indent=2),encoding='utf-8')
with (call/'STDOUT.jsonl').open('w',encoding='utf-8') as out,(call/'STDERR.txt').open('w',encoding='utf-8') as err:
    p=subprocess.Popen([exe,'run','--standalone','--model',model,'--agent','neuro-review','--format','json','--title','Nemotron scientific review access test'],cwd=root/'inputs',stdin=subprocess.PIPE,stdout=out,stderr=err,text=True,encoding='utf-8',creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
    p.communicate(prompt)
request.update(completed_utc=datetime.now(timezone.utc).isoformat(),returncode=p.returncode)
(call/'RESULT.json').write_text(json.dumps(request,indent=2),encoding='utf-8')
print(json.dumps({'returncode':p.returncode,'stdout_bytes':(call/'STDOUT.jsonl').stat().st_size,'completed':request['completed_utc']}))
