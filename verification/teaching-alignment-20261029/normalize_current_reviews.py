"""Serialize actual reviewer fields without manufacturing acceptance.

This preparatory report is not the official packet. Original calls stay intact.
Final assembly requires all stages, paragraph judgments and later recheck calls.
"""
from pathlib import Path
import datetime
import json
import re
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, r'C:/dev/NBIS/publisher-releases/0.8.23/skills/course-quality-gate/scripts')
import orchestrate_pedagogy_reviews as gate

def read(name):
    return json.loads((HERE / name).read_text(encoding='utf-8'))

prepared = read('pedagogy-final/PARAGRAPH_REVIEW.json')
paragraphs = {p['id']: p for p in prepared['paragraphs']}
units = set(prepared['workflow']['unit_ids'])

def flattened(value):
    if isinstance(value, list):
        return ', '.join(flattened(x) for x in value)
    if isinstance(value, dict):
        return '. '.join(f'{k}: {flattened(v)}' for k, v in value.items())
    return str(value).replace('\n', ' ').strip()

def reference_ids(value):
    if isinstance(value, str): return [value]
    found = []
    if isinstance(value, list):
        for item in value: found.extend(reference_ids(item))
    elif isinstance(value, dict):
        for key in ('unit_id', 'paragraph_id', 'paragraph_refs'):
            if key in value: found.extend(reference_ids(value[key]))
    return list(dict.fromkeys(found))

def location(unit, refs):
    found = []
    for ref in refs:
        if ref in paragraphs:
            p = paragraphs[ref]
            found.append(f"{p['source']} line {p['line']} ({ref})")
    if found:
        return ', '.join(dict.fromkeys(found))
    if unit == 'part:MECHANISMS::part-opening':
        return 'plan/chapter-plan.yaml line 10 (part:MECHANISMS purpose)'
    if unit == 'part:OBSERVATIONS::part-opening':
        return 'plan/chapter-plan.yaml line 20 (part:OBSERVATIONS purpose)'
    raise ValueError(f'No actual passage location: {unit} {refs}')

def field_text(label, value, unit, assessment, group):
    if isinstance(value, str):
        if (label in gate.STRUCTURED_TEACHING_FIELDS
                and value.startswith('Not applicable:') and ';' in value
                and not re.search(r'\breason:', value, re.I)):
            # Label the already supplied reason, without adding a new judgment.
            lead, reason = value.split(';', 1)
            return lead + '; reason:' + reason
        return value
    refs = reference_ids(value.get('source_refs', value.get('source_ref', [])))
    if not refs:
        refs = reference_ids(value.get('target', []))
    if not any(r in paragraphs for r in refs) and not unit.startswith('part:'):
        refs = list(dict.fromkeys(refs + [r for q in assessment.get('questions',assessment.get('reader_questions',[])) for r in reference_ids(q.get('source_refs',q.get('evidence_refs',[])))]))
    if not any(r in paragraphs for r in refs) and not unit.startswith('part:'):
        refs = reference_ids(assessment.get('source_refs',assessment.get('paragraph_refs',[])))
    loc = location(unit, refs)
    def component(*keys):
        for key in keys:
            if key in value:return value[key]
        raise KeyError((label,unit,keys))
    if label == 'System setup and component relationships':
        # Reviewers explicitly confirmed retain means adequate in a later message.
        verdict = value['verdict']
        if verdict in ('retain', 'adequate for the unit'):
            verdict = 'adequate'
        fields = [('setting', value['setting']), ('roles', value['roles']),
                  ('objects and flow', value.get('objects_and_flow', value.get('flow'))),
                  ('assumptions', value['assumptions']), ('verdict', verdict)]
    elif label == 'Expert objection':
        disposition = value['disposition']
        if disposition in ('retain', 'retained', 'not sustained on complete reading'):
            disposition = 'does not apply'
        if group == 'eye-pending' and unit.endswith('::sec:READING-START'):
            disposition = 'pending cross-group check'
        fields = [('objection', value['objection']), ('kind', value['kind']),
                  ('target', value['target']), ('disposition', disposition), ('reason', value['reason'])]
    elif label.startswith('Concrete wording and sentence contribution:'):
        fields = [('phrase', component('phrase')), ('paraphrase', component('paraphrase','plain_language_paraphrase')),
                  ('actor',component('actor')),('object',component('object')),
                  ('action',component('action','action_or_state_change')),
                  ('condition or consequence',component('condition or consequence','condition_or_consequence')),
                  ('verdict',component('verdict')),
                  ('replacement or retention reason',component('replacement or retention reason','replacement_or_retention_reason','retention_reason'))]
    elif label in gate.STRUCTURED_TEACHING_FIELDS:
        fields = [(key,component(key,key.replace(' ','_'))) for key in gate.STRUCTURED_TEACHING_FIELDS[label]]
        # The reports record zero unresolved items as []; the Markdown contract
        # spells that same saved judgment "none". Do not infer it from status.
        fields = [(key, 'none' if key == 'unresolved' and item == [] else item)
                  for key, item in fields]
    else:
        body = value.get('answer', value.get('evidence',value.get('check',value.get('assessment'))))
        if body is None:
            body = '. '.join(f'{k}: {flattened(v)}' for k, v in value.items() if k not in ('source_refs', 'verdict'))
        return f'{loc}; {flattened(body)}'
    # Inner semicolons are ordinary reviewer sentence punctuation, not field separators.
    return loc + '; ' + '; '.join(k + ': ' + flattened(v).replace(';', '.') for k, v in fields)

def main():
    results = {}
    checks = []
    for group in ('memory', 'eye', 'place'):
        report = read(f'final-{group}-stage1.json')
        source = read(f'final-{group}-input.json')
        assert report['completed_at'], group
        assert report['input_hash'] == prepared['input_hash']
        assert report['review_contract_hash'] == prepared['review_contract_hash']
        assert {a['unit_id'] for a in report['assessments']} == set(source['units'])
        expected_claims = {(u, c[0], c[1]) for u, v in source['units'].items() for c in v['claims']}
        claims = report.get('claims', report.get('claim_checks'))
        actual_claims = {(c['unit_id'], c['claim_id'].split('::')[-1], c.get('line', c.get('source_line'))) for c in claims}
        assert actual_claims == expected_claims, (group, expected_claims ^ actual_claims)
        for a in report['assessments']:
            unit = a['unit_id']
            results[unit] = {}
            for label, value in a['fields'].items():
                rendered = field_text(label, value, unit, a, 'eye-pending' if group == 'eye' else group)
                results[unit][label] = {'text': rendered, 'run_id': report['run_id']}
                valid = gate._structured_teaching_is_complete(label, rendered) if label in gate.STRUCTURED_TEACHING_FIELDS else gate._evidence_is_complete(rendered)
                if not valid:
                    checks.append({'unit_id': unit, 'field': label, 'reason': 'Incomplete formal field; preserve pending judgment or request a record clarification.'})
    output = {'prepared_at': datetime.datetime.now().astimezone().isoformat(),
              'status': 'preparatory_serialization_not_acceptance', 'input_hash': prepared['input_hash'],
              'fields': results, 'format_findings': checks,
              'limits': ['Only saved Stage 1 fields serialized.', 'Eye READING-START cross-group promise remains pending.',
                         'Final acceptance requires the remaining actual stages and rechecks.', 'Figure acceptance deferred.']}
    (HERE / 'stage1-fields-normalized.json').write_text(json.dumps(output, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
    print(json.dumps({'units': len(results), 'format_findings': checks}, ensure_ascii=False))

if __name__ == '__main__':
    main()
