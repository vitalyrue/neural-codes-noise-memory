"""Prepare diagnostic candidates only. No candidate is an accepted judgment."""
from pathlib import Path
import collections
import difflib
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent

def group(chapter_or_path):
    name = chapter_or_path.rsplit('/', 1)[-1]
    if name.startswith(('01', '02', '03')) or chapter_or_path in {
        'ch:FOUNDATIONS', 'ch:PERSISTENCE', 'ch:MEMORY-DYNAMICS',
        'ch:MEMORY-LONG-DELAYS', 'ch:MEMORY-INFORMATION', 'ch:MEMORY-READOUT'}:
        return 'memory'
    if name.startswith(('00', '04')) or chapter_or_path.startswith('ch:EYE-') or chapter_or_path == 'ch:READING-GUIDE':
        return 'eye'
    return 'place'

vale = json.loads((ROOT / 'verification/vale-report-guide.json').read_text())
alerts = {key: [] for key in ('memory', 'eye', 'place')}
for raw_path, items in vale['raw'].items():
    path = Path(raw_path)
    relative = path.relative_to(ROOT).as_posix()
    lines = path.read_text(encoding='utf-8').splitlines()
    for item in items:
        line = item['Line']
        identity = json.dumps([relative, line, item['Span'], item['Check'], item['Match']], ensure_ascii=False)
        alerts[group(relative)].append({
            'id': hashlib.sha256(identity.encode()).hexdigest()[:16],
            'source': relative, 'line': line, 'rule': item['Check'],
            'severity': item['Severity'], 'match': item['Match'],
            'message': item['Message'], 'span': item['Span'],
            'source_line': lines[line-1] if line <= len(lines) else '',
            'decision': 'pending', 'reason': ''
        })
for key, rows in alerts.items():
    (OUT / f'{key}-vale-input.json').write_text(json.dumps(rows, indent=2, ensure_ascii=False), encoding='utf-8')
    print(key, 'Vale', len(rows), dict(collections.Counter(r['severity'] for r in rows)))

old = json.loads((ROOT / 'verification/teaching-compliance-20261025/concept-index-reviewed.json').read_text())
current = json.loads((OUT / 'concept-index-initial.json').read_text())
old_passages = {p['id']: p for p in old['passages']}
current_by_chapter = collections.defaultdict(list)
for passage in current['passages']:
    current_by_chapter[passage['chapter_id']].append(passage)

def normalized(text):
    text = re.sub(r'\{[^\n{}]*\}', '', text)
    return re.sub(r'\s+', ' ', text.replace('**', '').replace('[', '').replace(']', '')).strip()

mapped = {}
relations = {key: [] for key in ('memory', 'eye', 'place')}
for relation in old['relations']:
    previous = old_passages[relation['passage_id']]
    candidates = current_by_chapter[previous['chapter_id']]
    ranked = sorted(((difflib.SequenceMatcher(None, normalized(previous['text']), normalized(p['text'])).ratio(), p) for p in candidates), key=lambda x: x[0], reverse=True)
    score, candidate = ranked[0]
    unique = len(ranked) == 1 or score - ranked[1][0] > 0.04
    located = candidate if score >= 0.80 and unique else None
    if located:
        mapped[previous['id']] = located['id']
    row = {
        'concept_id': relation['concept_id'], 'role': relation['role'],
        'old_passage_id': previous['id'], 'old_text': previous['text'],
        'old_span': relation.get('span'), 'prior_evidence': relation.get('evidence'),
        'candidate_passage_id': located['id'] if located else None,
        'candidate_text': located['text'] if located else None,
        'candidate_score': round(score, 4),
        'status': 'candidate',
        'instruction': 'Read current passage and its earlier teaching; choose exact current span and record a new judgment. Similarity is only a locator.'
    }
    for name in ('need', 'adequacy'):
        if name in relation:
            row[name] = relation[name]
    relations[group(previous['chapter_id'])].append(row)
for key, rows in relations.items():
    sections = [s for s in current['sections'] if group(s['chapter_id']) == key]
    payload = {'status': 'candidate-only', 'audience': old['audience'],
               'catalog': old['concepts'], 'sections': sections,
               'relations_to_review': rows, 'old_to_candidate_passages': mapped,
               'old_teaching_sets': old['teaching_sets']}
    (OUT / f'{key}-concept-candidates.json').write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding='utf-8')
    print(key, 'concept relations', len(rows), 'unlocated', sum(r['candidate_passage_id'] is None for r in rows))
