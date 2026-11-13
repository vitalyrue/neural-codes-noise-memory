"""Build a readable index of actual reviewer findings, without changing sources."""
from pathlib import Path
from datetime import datetime, timezone
import json

root=Path(__file__).resolve().parent
out=['# Opus 5.5 review: complete findings register','',
     'These are the reviewer\'s original findings on the unchanged guide. They are proposals, not accepted edits. Later qualifications and withdrawn concerns are recorded separately below and in REVIEW.md. Exact provider answers remain in calls/stageN/ANSWER.md.','']
usage={}; stages=[]
for n,title in [(1,'Source and mathematics review'),(2,'Explanations and terminology'),(3,'Structure and learning path')]:
    call=root/'calls'/f'stage{n}'
    if not (call/'BODY.json').exists(): continue
    body=json.loads((call/'BODY.json').read_text(encoding='utf-8'))
    result=json.loads((call/'RESULT.json').read_text(encoding='utf-8'))
    usage=result.get('modelUsage',{}) # Provider modelUsage is cumulative across resumed session.
    stages.append({'stage':n,'start':result.get('started_utc'),'end':result.get('completed_utc'),'duration_ms':result.get('duration_ms'),'provider_uuid':result.get('provider_uuid'),'coverage_count':len(body.get('coverage',body.get('part_and_chapter_path',[]))),'usage_for_this_turn':result.get('usage')})
    out.extend([f'## Stage {n}: {title}','',body.get('summary',''),''])
    collections=['findings','useful_additions'] if n<3 else ['part_and_chapter_path','structural_recommendations','clarifications_and_additions','reconsidered_findings','top_actions_in_order']
    for collection in collections:
        values=body.get(collection,[])
        if not values: continue
        out.extend(['### '+collection.replace('_',' ').capitalize(),''])
        for item in values:
            label=str(item.get('id',item.get('original_id',item.get('rank',''))))
            out.extend(['#### '+label,''])
            for k,v in item.items():
                if k in ['id','original_id','rank'] or v in [None,'',[]]:continue
                label=k.replace('_',' ').capitalize()
                if isinstance(v,list):
                    out.extend(['**'+label+':**',''])
                    for entry in v:
                        if isinstance(entry,dict): out.append('- '+'; '.join(str(x).replace('_',' ')+': '+str(y) for x,y in entry.items()))
                        else:out.append('- '+str(entry))
                    out.append('')
                else:out.extend(['**'+label+':** '+str(v),''])
    for key in ['retained_strengths','retained_choices','what_to_keep','remaining_checks','coverage_and_limits']:
        v=body.get(key)
        if v:
            out.extend(['### '+key.replace('_',' ').capitalize(),''])
            if isinstance(v,list):out.extend('- '+str(x) for x in v)
            elif isinstance(v,dict):out.extend('- '+str(k)+': '+str(x) for k,x in v.items())
            else:out.append(str(v))
            out.append('')
out.extend(['## Coordinator checks after the original replies','',
            'These distinguish supported improvements, unresolved questions and objections resolved by checking the sources. No manuscript changes were made.',''])
checks=json.loads((root/'coordinator-checks.json').read_text(encoding='utf-8'))
for k,v in checks.items():
    if not isinstance(v,dict):continue
    out.extend(['### '+k,'',v.get('disposition',''),''])
    for field in ['primary_url','abstract_url','primary_urls','source','supporting_check','limits']:
        if field in v:
            value=v[field]
            if isinstance(value,list):out.extend('- '+str(x) for x in value)
            else:out.append(field.replace('_',' ').capitalize()+': '+str(value))
            out.append('')
(root/'FINDINGS_REGISTER.md').write_text('\n'.join(out)+'\n',encoding='utf-8')
totals={'recorded_utc':datetime.now(timezone.utc).isoformat(),'note':'modelUsage is cumulative across this resumed reviewer session, so only the final stage is used for totals. Per-turn usage is preserved in stage records. Output includes reasoning tokens. Cache creation and cache read are separate input categories. CLI smoke test excluded. Root and supporting-agent token statistics unavailable.','model_usage_cumulative':usage,'stages':stages}
(root/'USAGE_AND_STAGES.json').write_text(json.dumps(totals,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'stages':len(stages),'register':str(root/'FINDINGS_REGISTER.md'),'chars':len('\n'.join(out))}))
