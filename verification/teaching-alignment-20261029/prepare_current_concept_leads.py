"""Locate historical concept leads in current text without adopting judgments."""
from pathlib import Path
import collections
import difflib
import json
import re

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[1]
old = json.loads((ROOT / 'verification/teaching-compliance-20261025/concept-index-reviewed.json').read_text())
current = json.loads((OUT / 'concept-index-current-unreviewed.json').read_text())
prior = {p['id']: p for p in old['passages']}
by_chapter = collections.defaultdict(list)
for passage in current['passages']:
    by_chapter[passage['chapter_id']].append(passage)


def clean(text):
    text = re.sub(r'<!--.*?-->', ' ', text, flags=re.S)
    return ' '.join(text.split()).casefold()


def owner(chapter):
    if chapter in {'ch:FOUNDATIONS', 'ch:PERSISTENCE', 'ch:MEMORY-DYNAMICS',
                   'ch:MEMORY-LONG-DELAYS', 'ch:MEMORY-INFORMATION', 'ch:MEMORY-READOUT'}:
        return 'memory'
    if chapter.startswith('ch:EYE-') or chapter == 'ch:READING-GUIDE':
        return 'eye'
    return 'place'


leads = []
for relation in old['relations']:
    earlier = prior[relation['passage_id']]
    ranked = sorted([(difflib.SequenceMatcher(None, clean(earlier['text']), clean(p['text']),
                                              autojunk=False).ratio(), p)
                     for p in by_chapter[earlier['chapter_id']] if clean(p['text'])],
                    key=lambda value: value[0], reverse=True)[:2]
    leads.append({'concept_id': relation['concept_id'], 'suggested_role': relation['role'],
                  'old_passage_id': relation['passage_id'], 'old_text': earlier['text'],
                  'owning_group': owner(earlier['chapter_id']), 'status': 'unreviewed lead',
                  'current_candidates': [{'similarity': round(score, 4), 'passage_id': p['id'],
                                           'text': p['text']} for score, p in ranked if score >= .35]})
for group in ('memory', 'eye', 'place'):
    related = {lead['concept_id'] for lead in leads if lead['owning_group'] == group}
    data = {'status': 'Candidates only. These are locations to inspect, not current teaching judgments.',
            'current_index': 'concept-index-current-unreviewed.json',
            'scope': group, 'candidate_concepts': [c for c in old['concepts'] if c['id'] in related],
            'leads': [lead for lead in leads if lead['concept_id'] in related],
            'instruction': 'Judge actual current meaning, adequacy, required uses and reading order. Add missing concepts and relations. Do not adopt an old role solely from this lead. Cross-group earlier teaching is included when a concept appears in your scope.'}
    (OUT / f'final-{group}-concept-leads.json').write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
    print(group, len(data['candidate_concepts']), 'candidate concepts;', len(data['leads']), 'location leads')
