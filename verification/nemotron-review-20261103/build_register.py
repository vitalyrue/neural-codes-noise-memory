from pathlib import Path
from datetime import datetime, timezone
import json

root=Path(__file__).resolve().parent
out=['# Nemotron review: original findings and recommendations','',
     'These are the model\'s final-answer fields, not accepted edits. See REVIEW.md for the coordinator\'s checks and priorities. Original answers, including later-corrected claims, remain unchanged.','']
coverage=[]
for n in [1,2,3]:
    call=root/'calls'/f'stage{n}'
    body=json.loads((call/'BODY.json').read_text(encoding='utf-8'))
    result=json.loads((call/'RESULT.json').read_text(encoding='utf-8'))
    out.extend([f'## Stage {n}','',body['summary'],''])
    fields=['findings','useful_additions'] if n<3 else ['structural_recommendations','clarifications_and_additions','reconsidered_findings','top_actions_in_order']
    for field in fields:
        if not body.get(field):continue
        out.extend(['### '+field.replace('_',' ').capitalize(),''])
        for row in body[field]:
            label=row.get('id',row.get('original_id',row.get('rank','')))
            out.extend(['#### '+str(label),''])
            for k,v in row.items():
                if k in ['id','original_id','rank'] or v in ['',None,[]]:continue
                name=k.replace('_',' ').capitalize()
                if isinstance(v,list):
                    out.extend(['**'+name+':**',''])
                    for item in v:
                        out.append('- '+('; '.join(str(a).replace('_',' ')+': '+str(b) for a,b in item.items()) if isinstance(item,dict) else str(item)))
                    out.append('')
                else:out.extend(['**'+name+':** '+str(v),''])
    for field in ['remaining_checks','coverage_and_limits','what_to_keep']:
        if not body.get(field):continue
        out.extend(['### '+field.replace('_',' ').capitalize(),''])
        v=body[field]
        if isinstance(v,list):out.extend('- '+str(x) for x in v)
        else:out.append(str(v))
        out.append('')
    coverage.append({'stage':n,'recorded_model':result.get('recorded_model'),'local_request_id':result['local_request_id'],'started_utc':result['started_utc'],'completed_utc':result['completed_utc'],'session_id':result.get('session_id'),'coverage':body.get('coverage',body.get('part_and_chapter_path',[]))})
(root/'FINDINGS_REGISTER.md').write_text('\n'.join(out)+'\n',encoding='utf-8')
last=json.loads((root/'calls/stage3/RESULT.json').read_text(encoding='utf-8'))
(root/'COVERAGE_AND_USAGE.json').write_text(json.dumps({'recorded_utc':datetime.now(timezone.utc).isoformat(),'note':'Final session totals counted once; access smoke test excluded. Input, cache, output and reasoning are the separate fields reported by OpenCode.','model':last['recorded_model'],'session_usage_cumulative':last['session_usage_cumulative'],'recorded_session_cost':last.get('session_cost_cumulative'),'stages':coverage},ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'stages':len(coverage),'stage1_units':len(coverage[0]['coverage']),'stage2_units':len(coverage[1]['coverage']),'stage3_path_records':len(coverage[2]['coverage']),'register_chars':len('\n'.join(out))}))
