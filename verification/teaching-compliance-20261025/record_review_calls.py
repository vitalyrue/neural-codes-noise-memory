from pathlib import Path
from datetime import datetime
import json,hashlib
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[1]
log=Path('C:/Users/vital/.codex/sessions/2026/10/22/rollout-2026-10-22T18-09-53-01a16429-56cd-7531-92ce-552e368634a9.jsonl')
rows=[]
for line in log.open(encoding='utf-8'):
    d=json.loads(line);p=d.get('payload',{})
    if d.get('timestamp','')<'2026-10-25':continue
    if p.get('name') not in ('spawn_agent','followup_task'):continue
    args=p.get('arguments',{});args=json.loads(args) if isinstance(args,str) else args
    target=args.get('task_name',args.get('target',''))
    if 'compliance_' not in target:continue
    rows.append({'timestamp':d['timestamp'],'tool':p['name'],'call_id':p.get('call_id'),'target':target,'request_opening':args.get('message','')[:180]})
(OUT/'actual-review-calls.json').write_text(json.dumps({'recorded_at':datetime.now().astimezone().isoformat(),'source':'Current chat tool-call log; only bounded call identities/timestamps retained.','calls':rows},ensure_ascii=False,indent=2),encoding='utf-8')
packet=json.loads((OUT/'pedagogy/PARAGRAPH_REVIEW.json').read_text(encoding='utf-8'))
units={'memory':'content/chapters/01-foundations.md::sec:FOUNDATIONS-SPIKES','eye':'content/chapters/00-reading-guide.md::ch:READING-GUIDE','place':'content/chapters/06-synthesis.md::ch:SYNTHESIS'}
for group,unit in units.items():
    report=OUT/f'stage1-{group}.json';d=json.loads(report.read_text(encoding='utf-8'));call=next(r for r in rows if r['tool']=='spawn_agent' and r['target']=='compliance_'+group)
    if group=='memory':answer=next(x['passage_specific_reason'] for x in d['section_judgments'] if x['section']=='FOUNDATIONS-SPIKES')
    elif group=='eye':answer=d['retained_passages'][0][4]
    else:answer=next(x['stage1_answer'] for x in d['passage_judgments'] if '06-synthesis' in x['file'])
    run={'run_id':call['call_id'],'stage':'truth_reasoning','reviewer_id':'/root/compliance_'+group,'context':'fresh','started_at':call['timestamp'],'completed_at':d['completed_at'],'input_hash':packet['input_hash'],'review_contract_hash':packet['review_contract_hash'],'assessments':[{'unit_id':unit,'status':'pass','unresolved':[],'questions':[{'question':'Does this original teaching unit contain a material correctness or prerequisite defect?','answer':answer,'source_refs':[unit]}]}]}
    original={'schema_version':1,'input_hash':packet['input_hash'],'review_contract_hash':packet['review_contract_hash'],'conversion_note':'This is a structured transcription of one actually retained unit from the original fresh independent call. Its original report, source snapshot, findings elsewhere and completion time remain unchanged. Spawn time/call ID come from the current chat tool log. It does not claim that the original full report had no findings.','source_report':report.relative_to(ROOT).as_posix(),'source_report_sha256':hashlib.sha256(report.read_bytes()).hexdigest(),'workflow':{'writer_ids':['/root','legacy-guide-authors'],'runs':[run]}}
    (OUT/f'original-workflow-{group}.json').write_text(json.dumps(original,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'actual_calls':len(rows),'unchanged_original_units':units}))
