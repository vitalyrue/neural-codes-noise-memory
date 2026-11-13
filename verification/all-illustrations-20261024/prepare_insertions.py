"""Prepare reversible image additions for a connected-source review."""
from pathlib import Path
from datetime import datetime
import json, yaml

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
PACKETS = ['foundation-information-integration.json', 'eye-place-integration.json', 'synthesis-integration.json']
LABELS = {
 'A01': 'Poisson count likelihood, SI Eq. S43, p. 9',
 'A02': 'Gaussian displacement density, SI Eq. S30, p. 7',
 'A03': 'Internal Fisher information, Eq. 3, p. 2',
 'A04': 'Diffusion bound, Eq. 4, p. 3',
 'A05': 'Shared and private variability, Eqs. 11–15, p. 10',
 'A06': 'Measurement noise correction, Eqs. 18–19, p. 10',
 'A07': 'Gaussian input and firing rate, STAR Methods Eqs. 2–3, p. e1',
 'A08': 'Field-size laws, Eq. 1, p. 1111',
}
rows = []
for name in PACKETS:
    rows.extend(json.loads((OUT / name).read_text(encoding='utf-8')))
assert len(rows) == 9 and len({r['visual_id'] for r in rows}) == 9
drafts, metas, changes = {}, {}, []
for r in rows:
    r['chapter'] = r.get('chapter', r.get('chapter_path'))
    r['placement'] = r.get('placement', r.get('placement_section'))
    r['candidate'] = r.get('candidate', f"candidate-content/visuals/candidates/20261024-all/{r['id']}")
    r['asset'] = 'assets/approved/visuals/' + r['visual_id'][4:].lower() + '.png'
    cp = r['chapter']
    if cp not in drafts:
        drafts[cp] = (OUT / 'baseline' / cp).read_text(encoding='utf-8')
        metas[cp] = yaml.safe_load((OUT / 'baseline' / Path(cp).with_suffix('.yaml')).read_text(encoding='utf-8'))
    after = r['interpretation']
    if r.get('source_link'):
        # Published chapter pages resolve their local paper copies in ../papers/.
        r['html_source_link'] = r['source_link'].replace('../../assets/papers/', '../papers/')
        r['source_link_label'] = LABELS[r['id']]
        after += f" See [{r['source_link_label']}]({r['html_source_link']})."
    addition = r['intro'] + '\n\n<div class="figure-scroll">\n\n{{block:' + r['visual_id'] + '}}\n\n</div>\n\n' + after
    before = r['insert_after']
    assert drafts[cp].count(before) == 1, (r['id'], 'anchor missing or ambiguous')
    replacement = before + '\n\n' + addition
    drafts[cp] = drafts[cp].replace(before, replacement)
    changes.append({'id': r['id'], 'chapter': cp, 'before': before, 'after': replacement})
    metas[cp]['blocks'].append({'id': r['visual_id'], 'kind': 'figure', 'placement': r['placement'],
        'asset': r['asset'], 'caption': r['caption'], 'alt': r['alt'], 'width_inches': 7.29167, 'html_fold': 'never'})
    r['chapter_id'] = metas[cp]['chapter_id']
for cp, text in drafts.items():
    reverse = text
    for change in reversed([x for x in changes if x['chapter'] == cp]):
        assert reverse.count(change['after']) == 1
        reverse = reverse.replace(change['after'], change['before'])
    assert reverse == (OUT / 'baseline' / cp).read_text(encoding='utf-8')
    target = OUT / 'proposed' / cp
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding='utf-8', newline='\n')
    target.with_suffix('.yaml').write_text(yaml.safe_dump(metas[cp], allow_unicode=True, sort_keys=False, width=84), encoding='utf-8')
(OUT / 'integration.json').write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding='utf-8')
(OUT / 'insertions.json').write_text(json.dumps(changes, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps({'at': datetime.now().astimezone().isoformat(), 'figures': len(rows), 'chapters': len(drafts), 'original_recovers_exactly': True}))
