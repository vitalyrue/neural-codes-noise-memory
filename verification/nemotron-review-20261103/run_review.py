from pathlib import Path
from datetime import datetime,timezone
import subprocess,json,uuid,hashlib,time,sys
root=Path(__file__).resolve().parent
exe=r'C:/nvm4w/nodejs/node_modules/@opencode/cli/bin/opencode.exe'
model='opencode/nemotron-3.5-super-vl-free#high'
def now():return datetime.now(timezone.utc).isoformat()
def save(p,value):p.write_text(json.dumps(value,ensure_ascii=False,indent=2),encoding='utf-8')
stage=int(sys.argv[1]);call=root/'calls'/f'stage{stage}';call.mkdir(parents=True,exist_ok=True)
assert not (call/'RESULT.json').exists(),'Original attempt retained; use a distinct scoped follow-up if needed.'
prompt=(root/f'STAGE{stage}_PROMPT.txt').read_text(encoding='utf-8')
prompt+='\nReturn your complete review in your final answer. No file writes, code execution, subagents or questions. You may read supplied source files and primary web pages to resolve ambiguity. Do not read historical reviews or writer rationales. State what you actually inspected. Keep final answer under about12000tokens; do not spend the answer budget on execution-status messages.\n'
if stage==1:prompt+='\nBEGIN FROZEN CURRENT GUIDE AND SOURCE PACKET\n'+(root/'inputs/REVIEW_PACKET.txt').read_text(encoding='utf-8')+'\nEND FROZEN PACKET\n'
(call/'PROMPT.txt').write_text(prompt,encoding='utf-8')
args=[exe,'run','--standalone','--model',model,'--agent','neuro-review','--format','json']
if stage==1:args+=['--title','Nemotron independent Burak guide review 2026-11-03']
else:args+=['--session',json.loads((root/'SESSION.json').read_text(encoding='utf-8'))['session_id']]
request={'local_request_id':str(uuid.uuid4()),'stage':stage,'started_utc':now(),'requested_model':model,'agent':'neuro-review','prompt_sha256':hashlib.sha256(prompt.encode()).hexdigest(),'prompt_bytes':len(prompt.encode()),'status':'running','input_manifest_sha256':hashlib.sha256((root/'MANIFEST.json').read_bytes()).hexdigest()}
save(call/'REQUEST.json',request)
with (call/'STDOUT.jsonl').open('w',encoding='utf-8') as out,(call/'STDERR.txt').open('w',encoding='utf-8') as err:
    p=subprocess.Popen(args,cwd=root/'inputs',stdin=subprocess.PIPE,stdout=out,stderr=err,text=True,encoding='utf-8',creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0));request['pid']=p.pid;save(call/'REQUEST.json',request)
    p.stdin.write(prompt);p.stdin.close()
    while p.poll() is None:
        save(root/'RUNNING.json',{'stage':stage,'started_utc':request['started_utc'],'checkpoint_utc':now(),'pid':p.pid,'stdout_bytes':(call/'STDOUT.jsonl').stat().st_size});time.sleep(5)
    code=p.wait()
events=[]
for line in (call/'STDOUT.jsonl').read_text(encoding='utf-8-sig').splitlines():
    try:events.append(json.loads(line))
    except ValueError:pass
sid=next((e.get('sessionID') for e in events if e.get('sessionID')),None)
request.update(completed_utc=now(),returncode=code,session_id=sid)
if sid:
    exported=subprocess.run([exe,'session','export',sid],cwd=root/'inputs',capture_output=True,text=True,encoding='utf-8')
    (call/'SESSION_EXPORT.json').write_text(exported.stdout,encoding='utf-8')
    try:
        session=json.loads(exported.stdout);info=session['info'];request.update(recorded_model=info.get('model'),session_usage_cumulative=info.get('tokens'),session_cost_cumulative=info.get('cost'),session_outcome=info.get('outcome'))
    except (ValueError,KeyError):request['export_limit']='Session export did not parse.'
    if stage==1:save(root/'SESSION.json',{'session_id':sid,'model':request.get('recorded_model'),'created_utc':request['started_utc']})
stops=[e for e in events if e.get('type')=='step_finish' and e.get('part',{}).get('reason')=='stop']
mid=stops[-1]['part'].get('messageID') if stops else None
if 'session' in globals():
    final_messages=[x for x in session.get('messages',[]) if x.get('type')=='assistant' and x.get('agent')=='neuro-review']
    if final_messages:mid=final_messages[-1]['id']
texts={}
for e in events:
    if e.get('type')=='text' and (not mid or e.get('part',{}).get('messageID')==mid):texts[e['part'].get('id',str(len(texts)))]=e['part'].get('text','')
body='\n\n'.join(texts.values());(call/'ANSWER.md').write_text(body,encoding='utf-8')
request['errors']=[e for e in events if e.get('type')=='error']
turn_usage=[e['part'].get('tokens',{}) for e in events if e.get('type')=='step_finish'];request['turn_usage_steps']=turn_usage
recorded=request.get('recorded_model',{})
request['status']='completed' if code==0 and body and not request['errors'] and request.get('session_outcome')=='succeeded' and recorded.get('providerID')=='opencode' and recorded.get('id')=='nemotron-3.5-super-vl-free' else 'incomplete'
try:
    raw=body.strip();raw=raw.split('\n',1)[1].split('\n```',1)[0] if raw.startswith('```') else raw
    save(call/'BODY.json',json.loads(raw))
except ValueError:request['structured_json']='Not parsed; exact original answer retained.'
save(call/'RESULT.json',request);save(root/'RUNNING.json',{'stage':stage,'status':request['status'],'completed_utc':now()})
print(json.dumps({k:request.get(k) for k in ['stage','status','recorded_model','session_id','session_outcome','session_usage_cumulative','errors']}))
