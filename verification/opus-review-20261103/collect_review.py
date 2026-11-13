from pathlib import Path
from datetime import datetime, timezone
import json, sys
sys.stdout.reconfigure(encoding='utf-8')

root=Path(__file__).resolve().parent
stage=int(sys.argv[1])
call=root/'calls'/f'stage{stage}'
body=(call/'ANSWER.md').read_text(encoding='utf-8').strip()
raw=body.split('\n',1)[1].split('\n```',1)[0] if body.startswith('```') else body
parsed=json.loads(raw)
(call/'BODY.json').write_text(json.dumps(parsed,ensure_ascii=False,indent=2),encoding='utf-8')
models=set(); init=set(); tool_names={}
for line in (call/'STDOUT.jsonl').read_text(encoding='utf-8-sig').splitlines():
    try: e=json.loads(line)
    except ValueError: continue
    if e.get('type')=='assistant':
        msg=e.get('message',{})
        if msg.get('model'): models.add(msg['model'])
        for c in msg.get('content',[]):
            if c.get('type')=='tool_use': tool_names[c['name']]=tool_names.get(c['name'],0)+1
    if e.get('type')=='system' and e.get('subtype')=='init': init.add(e.get('model'))
r=json.loads((call/'PROVIDER_RESULT.json').read_text(encoding='utf-8'))
check={'checked_utc':datetime.now(timezone.utc).isoformat(),'original_result_preserved':True,'main_assistant_models':sorted(models),'initial_model':sorted(init),'auxiliary_models':sorted(set(r.get('modelUsage',{}))-models),'provider_is_error':r.get('is_error'),'review_completed':not r.get('is_error') and models=={'claude-opus-5-5'},'coverage_records':len(parsed.get('coverage',[])),'findings':len(parsed.get('findings',[])),'tools':tool_names,'note':'The initial stage1 wrapper rejected any auxiliary model. Main assistant and web-tool helper usage are now distinguished; no provider review was repeated. JSON extracted from its first code fence without altering the answer.'}
(call/'RESULT_CHECK.json').write_text(json.dumps(check,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(check,ensure_ascii=False,indent=2))
for f in parsed.get('findings',[]):
    print('\n'+f.get('id','')+' | '+f.get('severity','')+' | '+f.get('kind','')+' | '+f.get('file','')+' '+f.get('line_or_section',''))
    for field in ['claim_or_gap','source_evidence','suggested_action','confidence']:
        if field in f: print(field+': '+(json.dumps(f[field],ensure_ascii=False) if isinstance(f[field],list) else f[field]))
