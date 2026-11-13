"""Assemble saved independent judgments; missing evidence is an error.

Does not run a review or infer any passing judgment from file equality.
"""
from pathlib import Path
import argparse
import copy
import datetime
import hashlib
import json
import re
import shutil

import normalize_current_reviews as norm
from prepare_review_reuse import actual_run, WRITERS

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
PACKET = HERE/'pedagogy-current'
gate = norm.gate
READING_START = 'content/chapters/00-reading-guide.md::sec:READING-START'

def read(path):
    return json.loads(path.read_text(encoding='utf-8'))

def assessments(report):
    return report.get('assessments', report.get('unit_assessments', [report]))

def current_run_references(run, known_refs, corrections):
    # Current reports retain their complete original references. The workflow
    # schema accepts only current unit/paragraph IDs, not supplementary report
    # anchors or physical line citations. Keep those in the bound source report.
    if run['reviewer_id'] in ('accept_eye', 'accept_memory', 'accept_place'):
        original=run['reviewer_id']
        run['reviewer_id']='/root/'+original
        corrections.append({'run_id':run['run_id'],'reviewer_alias':original,'canonical_reviewer':run['reviewer_id']})
    for a in run['assessments']:
        for q in a['questions']:
            original=q['source_refs']
            refs=[r for r in original if r in known_refs]
            if a['unit_id'].startswith('part:') and any(r.startswith('plan/chapter-plan.yaml:') for r in original):
                refs.append(a['unit_id'])
            refs=list(dict.fromkeys(refs))
            assert refs,(run['run_id'],a['unit_id'],original)
            if refs!=original:
                corrections.append({'run_id':run['run_id'],'unit_id':a['unit_id'],'question':q['question'],'original_refs':original,'workflow_refs':refs,'note':'Full supplementary references remain in the unchanged bound report.'})
            q['source_refs']=refs
    return run

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--preflight',action='store_true')
    args=parser.parse_args()
    prepared=read(PACKET/'PARAGRAPH_REVIEW.json')
    current_hash=gate._input_hash(ROOT,gate.discover_source_files(ROOT))
    assert prepared['input_hash']==current_hash
    required_fields=gate.REVIEW_FIELDS
    norm.paragraphs={p['id']:p for p in prepared['paragraphs']}
    unit_ids=prepared['workflow']['unit_ids']
    norm.units=set(unit_ids)
    reuse=read(HERE/'review-reuse-preparation.json')
    assert reuse['current_input_hash']==current_hash
    selected={entry['run_id']:set(entry['eligible_assessments']) for entry in reuse['calls']}
    # Its original truth call was honestly open pending the whole-book reading.
    # Preserve that call, but use a later complete ordered sequence for this unit.
    for run_id in selected:
        selected[run_id].discard(READING_START)
    source_reports=[]
    for g in ('memory','eye','place'):
        for stage in (1,2):source_reports.append((g,HERE/f'final-{g}-stage{stage}.json','old'))
    for stage in (1,2):source_reports.append(('eye',HERE/f'current-eye-noise-stage{stage}.json','current'))
    for g in ('memory','eye','place'):source_reports.append((g,HERE/f'final-{g}-stage3.json','current'))
    for stage in (1,2,3):source_reports.append(('eye',HERE/f'current-eye-reading-start-stage{stage}.json','current'))
    recheck_paths=[HERE/f'final-{g}-recheck.json' for g in ('memory','eye','place')]
    recheck_paths.append(HERE/'current-eye-reading-start-recheck.json')
    needed=[str(p.name) for _,p,_ in source_reports if not p.exists()]+[p.name for p in recheck_paths if not p.exists()]
    if needed:
        raise ValueError('Actual review reports missing: '+', '.join(needed))
    fields={u:{} for u in unit_ids}
    claims={}
    runs=[]
    field_bindings={u:{} for u in unit_ids}
    paragraph_reviews={}
    report_bindings=[]
    serialization_corrections=[]
    known_refs=set(unit_ids)|set(norm.paragraphs)
    for group,path,kind in source_reports:
        report=read(path)
        run=actual_run(report)
        assert run['completed_at'],path
        assert run['review_contract_hash']==prepared['review_contract_hash']
        if kind=='current':
            assert run['input_hash']==current_hash,path
            run=current_run_references(run,known_refs,serialization_corrections)
        if path.name=='final-eye-stage3.json':
            run['assessments']=[a for a in run['assessments'] if a['unit_id']!=READING_START]
        runs.append(run)
        accepted_units=selected[run['run_id']] if kind=='old' else {a['unit_id'] for a in run['assessments']}
        for a in assessments(report):
            unit=a['unit_id']
            if unit not in accepted_units:continue
            assert a['status']=='pass' and a['unresolved']==[],(path,unit)
            canonical=next(x for x in run['assessments'] if x['unit_id']==unit)
            for label,value in a.get('fields',a.get('review',{})).items():
                if label not in required_fields:raise ValueError(('Unknown field',path,label))
                context='eye-pending' if group=='eye' and kind=='old' and run['stage']=='truth_reasoning' else group
                text=norm.field_text(label,value,unit,{**a,'questions':canonical['questions']},context)
                fields[unit][label]=text
                field_bindings[unit][label]={'report':path.name,'run_id':run['run_id']}
        for claim in report.get('claims',report.get('claim_checks',[])):
            unit=claim['unit_id']
            if unit not in accepted_units:continue
            if path.name=='current-eye-reading-start-stage1.json':
                clarification=read(HERE/'current-eye-reading-start-claim-clarification.json')
                assert clarification['source_run_id']==run['run_id']
                row=next(x for x in clarification['clarifications'] if x['claim_id']==claim['claim_id'])
                assert claim['verdict']==row['original_verdict']
                claim={**claim,'verdict':row['clarified_verdict'],
                       'check':claim['check']+' Reviewer clarification: '+row['reason']}
            key=(unit,claim['claim_id'].split('::')[-1],claim.get('line',claim.get('source_line')))
            assert claim['verdict'] in gate.CLAIM_VERDICTS,(path,key)
            claims[key]=claim
        if run['stage']=='understanding_flow':
            for row in report['paragraph_reviews']:
                ident=row.get('id',row.get('paragraph_id'))
                assert ident in norm.paragraphs,(path,ident)
                if path.name=='final-eye-stage3.json' and norm.paragraphs[ident]['unit_id']==READING_START:
                    continue
                assert ident not in paragraph_reviews,ident
                review=copy.deepcopy(row['review'])
                assert set(review)=={'purpose','connection','decision','reason'},(path,ident)
                if review['decision'] in ('retain_structure','retain_hidden_control'):
                    # Both are explicit retention judgments; the schema has one
                    # retain value. Their structural/control reasons stay exact.
                    review['decision']='retain'
                assert review['decision']=='retain',(path,ident,review)
                paragraph_reviews[ident]=review
        report_bindings.append({'path':path.name,'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'run_id':run['run_id']})
    for path in recheck_paths:
        report=read(path);run=actual_run(report)
        assert run['stage']=='recheck' and run['input_hash']==current_hash
        run=current_run_references(run,known_refs,serialization_corrections)
        if path.name=='final-eye-recheck.json':
            run['assessments']=[a for a in run['assessments'] if a['unit_id']!=READING_START]
        runs.append(run)
        report_bindings.append({'path':path.name,'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'run_id':run['run_id']})
    for unit,evidence in fields.items():
        assert set(evidence)==set(required_fields),(unit,'missing fields',set(required_fields)-set(evidence))
    assert set(paragraph_reviews)==set(norm.paragraphs),('missing paragraph review',set(norm.paragraphs)-set(paragraph_reviews))
    format_findings=[]
    for unit,evidence in fields.items():
        for label,value in evidence.items():
            valid=(gate._structured_teaching_is_complete(label,value) if label in gate.STRUCTURED_TEACHING_FIELDS else
                   gate._concrete_wording_is_complete(value) if label.startswith('Concrete wording and sentence contribution:') else
                   gate._evidence_is_complete(value))
            if not valid:format_findings.append({'unit_id':unit,'field':label,'value':value})
    if format_findings:
        (HERE/'assembly-format-findings.json').write_text(json.dumps(format_findings,ensure_ascii=False,indent=2),encoding='utf-8')
        raise ValueError(f'{len(format_findings)} incomplete serialized fields; see assembly-format-findings.json')
    recheck_by_group={g:actual_run(read(HERE/f'final-{g}-recheck.json'))['run_id'] for g in ('memory','eye','place')}
    reuse_entries=[]
    for entry in reuse['calls']:
        group=next(g for g in ('memory','eye','place') if entry['run_id'].startswith('final-'+g+'-'))
        reuse_entries.append({k:entry[k] for k in ('run_id','original_call_path','original_call_sha256','snapshot_root','unit_map')})
        reuse_entries[-1]['unit_map']={k:v for k,v in entry['unit_map'].items() if k!=READING_START}
        reuse_entries[-1]['recheck_run_ids']=[recheck_by_group[group]]
    repair=read(HERE/'final-local-repair.json')
    prepared['workflow']={'writer_ids':WRITERS,'unit_ids':unit_ids,
                         'runs':sorted(runs,key=lambda r:r['started_at']),
                         'repairs':[{'unit_ids':unit_ids,
                                     'before_input_hash':'81f7e2f3f75c1d85db5116fb870c668bdebcfc94c180926ad1673e33b6f06e76',
                                     'after_input_hash':current_hash,'applied_at':repair['applied_at'],
                                     'reason':'Completed text-repair batch:223 approved edits, glossary ordering, reviewed bounded Vale controls and one later deletion. Exact intermediate changes and times are preserved in integration.json, glossary-order-correction.json, vale-exceptions.json, vale-location-workaround.json and final-local-repair.json. All units are included for their affected reading connections.',
                                     'recheck_run_ids':list(recheck_by_group.values())+[actual_run(read(HERE/'current-eye-reading-start-recheck.json'))['run_id']]}],
                         'reuse':reuse_entries}
    for p in prepared['paragraphs']:p['review']=paragraph_reviews[p['id']]
    backup=HERE/'pedagogy-current-preassembly'
    if not backup.exists():
        backup.mkdir()
        for p in PACKET.iterdir():
            if p.is_file():shutil.copy2(p,backup/p.name)
    assert read(backup/'PARAGRAPH_REVIEW.json')['input_hash']==current_hash
    rendered={}
    seen_claims=set()
    unit_re=re.compile(r'<!-- pedagogy-unit: (.*?) -->')
    for path in backup.glob('PEDAGOGY_REVIEW_*.md'):
        if path.name.endswith('_INDEX.md'):continue
        source=path.read_text(encoding='utf-8');matches=list(unit_re.finditer(source));parts=[];last=0
        for i,match in enumerate(matches):
            end=matches[i+1].start() if i+1<len(matches) else len(source)
            unit=match.group(1);segment=source[match.start():end]
            for label,value in fields[unit].items():
                pat=re.compile(r'^- '+re.escape(label)+r': .*$',re.M)
                segment,n=pat.subn(lambda _: '- '+label+': ['+value+']',segment)
                assert n==1,(path,unit,label,n)
            def replace_claim(m):
                key=(unit,m.group('id'),int(m.group('line')))
                claim=claims[key];seen_claims.add(key)
                return m.group(0).rsplit(' -> [',1)[0]+' -> [verdict: '+claim['verdict']+'; checked: '+claim['check'].replace('\n',' ')+']'
            segment=gate.CLAIM_LINE_RE.sub(replace_claim,segment)
            segment,n=re.subn(r'^- Verdict: Pending reviewer assessment$', '- Verdict: Pass',segment,flags=re.M)
            assert n==1,(path,unit,n)
            parts.append(source[last:match.start()]);parts.append(segment);last=end
        parts.append(source[last:]);rendered[path.name]=''.join(parts)
    assert seen_claims==set(claims),('claim coverage difference',seen_claims^set(claims))
    result={'assembled_at':datetime.datetime.now().astimezone().isoformat(),'input_hash':current_hash,
            'review_contract_hash':prepared['review_contract_hash'],'reports':report_bindings,
            'field_bindings':field_bindings,'counts':{'units':len(fields),'paragraphs':len(paragraph_reviews),'claims':len(claims),'runs':len(runs)},
            'status':'serialized_actual_judgments_validator_pending','figure_acceptance':'deferred'}
    result['acceptance_scope_selection']={'unit':READING_START,'reason':'Original truth assessment was open. Original reports remain complete and unchanged; this unit is omitted from their accepted subsets and covered by later separate current truth, language, flow and recheck calls.','original_current_flow_and_recheck_reports_preserved':True}
    result['serialization_corrections']=serialization_corrections
    (HERE/'assembly-evidence.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    if args.preflight:
        print(json.dumps({'preflight':'pass','counts':result['counts']}));return
    (PACKET/'PARAGRAPH_REVIEW.json').write_text(json.dumps(prepared,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    for name,text in rendered.items():(PACKET/name).write_text(text,encoding='utf-8',newline='\n')
    print(json.dumps(result['counts']))

if __name__=='__main__':main()
