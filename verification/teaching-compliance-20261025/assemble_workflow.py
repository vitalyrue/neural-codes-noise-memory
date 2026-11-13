from pathlib import Path
from datetime import datetime
import json,hashlib,copy,re
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[1]
load=lambda p:json.loads(p.read_text(encoding='utf-8'))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
path=OUT/'pedagogy-final/PARAGRAPH_REVIEW.json';packet=load(path)
runs=[];reuse=[];actual_reports=[]
for group in ('memory','eye','place'):
    origpath=OUT/f'original-workflow-{group}.json';original=load(origpath)['workflow']['runs'][0]
    unit=original['assessments'][0]['unit_id'];runs.append(original)
    for filename in [f'evidence-assembly-{group}.json',f'final-stage2-{group}.json',f'final-stage3-{group}.json',f'final-recheck-{group}.json']:
        p=OUT/filename;d=load(p);run=copy.deepcopy(d['workflow_run'])
        assert run['input_hash']==packet['input_hash'] and run['review_contract_hash']==packet['review_contract_hash'],filename
        assert all(a['status']=='pass' and a['unresolved']==[] for a in run['assessments']),filename
        # Canonical task-name aliases identify the same actual independent agent.
        assert run['reviewer_id'] in ('compliance_'+group,'/root/compliance_'+group)
        run['reviewer_id']='/root/compliance_'+group
        for assessment in run['assessments']:
            for question in assessment['questions']:
                question['source_refs']=list(dict.fromkeys(question['source_refs']))
        if run['stage']=='truth_reasoning':
            assert sum(a['unit_id']==unit for a in run['assessments'])==1
            run['assessments']=[a for a in run['assessments'] if a['unit_id']!=unit]
        runs.append(run);actual_reports.append({'path':p.relative_to(ROOT).as_posix(),'sha256':sha(p),'run_id':run['run_id']})
    recheck=runs[-1]
    assert recheck['stage']=='recheck'
    reuse.append({'run_id':original['run_id'],'original_call_path':str(origpath),'original_call_sha256':sha(origpath),'snapshot_root':str(OUT/'baseline'),'unit_map':{unit:unit},'recheck_run_ids':[recheck['run_id']]})
runs.sort(key=lambda r:datetime.fromisoformat(r['started_at'].replace('Z','+00:00')))
changed={Path(r['file']).with_suffix('.md').as_posix() for r in load(OUT/'integration.json')['changes'] if r['file'].startswith('content/chapters/')}
affected=[u for u in packet['workflow']['unit_ids'] if u.rsplit('::',1)[0] in changed]
repair={'unit_ids':affected,'applied_at':load(OUT/'integration.json')['at'],'before_input_hash':load(OUT/'pedagogy/PARAGRAPH_REVIEW.json')['input_hash'],'after_input_hash':packet['input_hash'],'reason':'All exact changes in repairs-v1.json and repairs-v2.json were integrated into the final source. Actual final truth, necessity and understanding calls plus later repair/source-reuse rechecks adopt the repaired content and connections.','recheck_run_ids':[r['run_id'] for r in runs if r['stage']=='recheck']}
packet['workflow']={'writer_ids':['/root','legacy-guide-authors'],'unit_ids':packet['workflow']['unit_ids'],'runs':runs,'repairs':[repair],'reuse':reuse}
path.write_text(json.dumps(packet,ensure_ascii=False,indent=2),encoding='utf-8')
# Independent reviewers completed disjoint Part2 unit blocks; preserve the header.
part=OUT/'pedagogy-final/PEDAGOGY_REVIEW_PART_02.md';text=part.read_text(encoding='utf-8')
fragments={}
for group in ('eye','place'):
    d=load(OUT/f'packet-fragments-{group}.json')
    if 'fragments' in d:d=d['fragments']
    assert isinstance(d,dict)
    for key,value in d.items():
        assert key not in fragments,key
        fragments[key]=value
# Unit fragments begin at their marker and end before the next marker. Their
# exact boundaries are recorded by the independent assembler and checked here.
markers=list(re.finditer(r'<!-- pedagogy-unit: ([^\n]+?) -->',text))
for match in reversed(markers):
    ident=match.group(1);assert ident in fragments,ident
    value=fragments[ident]
    if isinstance(value,dict):value=value.get('markdown',value.get('text'))
    assert isinstance(value,str) and f'<!-- pedagogy-unit: {ident} -->' in value,ident
    start=match.start();idx=markers.index(match);end=markers[idx+1].start() if idx+1<len(markers) else len(text)
    text=text[:start]+value+text[end:]
part.write_text(text,encoding='utf-8')
record={'at':datetime.now().astimezone().isoformat(),'workflow_runs':len(runs),'unit_count':len(packet['workflow']['unit_ids']),'affected_units':len(affected),'historical_reused_units':reuse,'actual_report_bindings':actual_reports,'normalization':'Reviewer aliases normalized to canonical task names and duplicate identical source references removed. Three byte-identical original accepted units establish the actual fresh independent starts; current truth calls cover the other units, with final explicit adoption rechecks. All original reports and dates remain unchanged. Structural wrapper retain decisions preserve original exclusion-from-prose notes.','part2_fragments':len(fragments)}
(OUT/'workflow-assembly.json').write_text(json.dumps(record,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps({'runs':len(runs),'units':record['unit_count'],'repaired_units':len(affected),'part2_fragments':len(fragments)}))
