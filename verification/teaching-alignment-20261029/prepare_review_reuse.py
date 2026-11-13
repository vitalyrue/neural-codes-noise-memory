"""Bind saved calls to saved inputs; report eligibility, never acceptance."""
from pathlib import Path
import datetime
import hashlib
import json
import re
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
SNAPSHOT = HERE / 'final-snapshot'
sys.path.insert(0, r'C:/dev/NBIS/publisher-releases/0.8.23/skills/course-quality-gate/scripts')
import orchestrate_pedagogy_reviews as gate

WRITERS = ['/root', 'unknown legacy guide writers', '/root/alignment_global',
           '/root/alignment_eye_truth', '/root/alignment_place_truth']

def load_records(root):
    discovered = gate.discover_source_files(root)
    scopes = gate._expected_review_scopes(root, discovered)
    records = {u: r for scope in scopes.values() for u, r in scope['unit_records'].items()}
    return gate._input_hash(root, discovered), records

def actual_run(report):
    """Map recorded key names to the validator schema without changing judgments."""
    def refs(value):
        found = []
        if isinstance(value, str): found.append(value)
        elif isinstance(value, list):
            for x in value: found.extend(refs(x))
        elif isinstance(value, dict):
            for key in ('unit_id', 'paragraph_id', 'paragraph_refs'):
                if key in value: found.extend(refs(value[key]))
        return list(dict.fromkeys((x.split('::',1)[1]+'::part-opening')
                                 if x.startswith('plan/chapter-plan.yaml::part:') else x for x in found))
    result = {'run_id': report.get('run_id', report.get('local_request_id')),
              'reviewer_id': report.get('reviewer_id', '/root/accept_eye'),
              'stage': report['stage'], 'context': report.get('context', report.get('context_mode')),
              'started_at': report['started_at'], 'completed_at': report.get('completed_at', report.get('ended_at')),
              'input_hash': report['input_hash'], 'review_contract_hash': report['review_contract_hash']}
    assessments = []
    for a in report.get('assessments', report.get('unit_assessments', [report])):
        questions = [{'question':q['question'], 'answer':q['answer'],
                      **{k:q[k] for k in ('kind','original_run_ids') if k in q},
                      'source_refs':refs(q.get('source_refs', q.get('evidence_refs'))) or [a['unit_id']]}
                     for q in a.get('questions', a.get('reader_questions'))]
        assessments.append({'unit_id':a['unit_id'], 'status':a['status'],
                            'unresolved':a['unresolved'], 'questions':questions})
    result['assessments'] = assessments
    return result

def main():
    old_hash, old = load_records(SNAPSHOT)
    new_hash, new = load_records(ROOT)
    # Input hashing includes relative paths, so identical snapshot bytes bind identically.
    freeze = json.loads((HERE/'final-source-freeze.json').read_text(encoding='utf-8'))
    assert old_hash == freeze['input_hash'], (old_hash, freeze['input_hash'])
    assert set(old) == set(new)
    equal = {}
    for unit in old:
        equal[unit] = gate._review_input_signature(SNAPSHOT, old[unit]) == gate._review_input_signature(ROOT, new[unit])
    calls = []
    for group in ('memory', 'eye', 'place'):
        for stage in (1, 2):
            source = HERE/f'final-{group}-stage{stage}.json'
            if not source.exists():
                continue
            report = json.loads(source.read_text(encoding='utf-8'))
            run = actual_run(report)
            if not run.get('completed_at'):
                continue
            assert run['input_hash'] == old_hash
            wrapped = {'prepared_at': datetime.datetime.now().astimezone().isoformat(),
                       'purpose': 'Lossless call wrapper for source-bound reuse; no new review occurred.',
                       'source_artifact': str(source), 'source_artifact_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
                       'input_hash': run['input_hash'], 'review_contract_hash': run['review_contract_hash'],
                       'writer_ids': WRITERS, 'runs': [run]}
            output = HERE/f'final-{group}-stage{stage}-call.json'
            if output.exists():
                previous = json.loads(output.read_text(encoding='utf-8'))
                if previous['runs'] != [run]:
                    # Preserve the first serialization and explicitly record a canonical ID repair.
                    output = HERE/f'final-{group}-stage{stage}-call-v2.json'
                    wrapped['serialization_note']='Resolve the recorded plan Part reference to its generated Part-opening unit ID. No reviewer judgment, question or answer changed.'
                    if output.exists():assert json.loads(output.read_text(encoding='utf-8'))['runs']==[run]
            if not output.exists():
                output.write_text(json.dumps(wrapped, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
            selected, changed, references = [], [], set()
            for a in run['assessments']:
                refs = {re.sub(r'::p\d+$','',r) for q in a['questions'] for r in q['source_refs']}
                if equal[a['unit_id']] and all(equal.get(r, False) for r in refs):
                    selected.append(a['unit_id']); references.update(refs)
                else:
                    changed.append(a['unit_id'])
            mapped = sorted(set(selected) | references)
            calls.append({'run_id': run['run_id'], 'original_call_path': str(output),
                          'original_call_sha256': hashlib.sha256(output.read_bytes()).hexdigest(),
                          'snapshot_root': str(SNAPSHOT), 'eligible_assessments': selected,
                          'requires_current_call': changed,
                          'unit_map': {u:u for u in mapped},
                          'recheck_run_ids': []})
    result = {'prepared_at': datetime.datetime.now().astimezone().isoformat(),
              'status': 'source_equality_only_current_adoption_pending',
              'before_input_hash': old_hash, 'current_input_hash': new_hash,
              'unit_equality': equal, 'calls': calls,
              'limits': 'Later actual reviewer answers must establish source/rule binding and current connections. Equality and wrappers are not acceptance.'}
    (HERE/'review-reuse-preparation.json').write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'changed_units':[u for u,v in equal.items() if not v],
                      'saved_calls':len(calls),'current_hash':new_hash},ensure_ascii=False))

if __name__ == '__main__':
    main()
