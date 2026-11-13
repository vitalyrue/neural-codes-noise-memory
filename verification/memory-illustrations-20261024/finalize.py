"""Record the local Chapter 2 delivery after scoped independent and browser checks."""
from pathlib import Path
from datetime import datetime
import hashlib, json, re, sys, yaml
ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
sys.path.insert(0, 'C:/Users/vital/.codex/skills/course-diagram-builder/scripts')
from visual_review import audit_ledger, validate_visual_review
from book_runtime.release_audit import audit_release, write_structure_lock
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def read_json(p): return json.loads(p.read_text(encoding='utf-8'))

reviews = read_json(OUT / 'diagram-review.json')
ids = {'fig:MEMORY-SPIKE-TRACE', 'fig:MEMORY-INHIBITION-RATES', 'fig:MEMORY-LINE-RING'}
assert set(reviews) == ids
path = ROOT / 'source-maps/visual-ledger.yaml'
ledger = yaml.safe_load(path.read_text(encoding='utf-8'))
new = []
for row in ledger['visuals']:
    if row['visual_id'] not in ids: continue
    row['diagram_review'] = reviews[row['visual_id']]
    errors = validate_visual_review(row, ROOT)
    assert not errors, (row['visual_id'], errors)
    new.append(row)
new_audit = audit_ledger({'visuals': new}, ROOT)
assert new_audit['status'] == 'pass' and new_audit['reviewed_figures'] == 3
baseline_ledger = yaml.safe_load((OUT / 'baseline/source-maps/visual-ledger.yaml').read_text(encoding='utf-8'))
assert [r for r in ledger['visuals'] if r['visual_id'] not in ids] == baseline_ledger['visuals']
path.write_text(yaml.safe_dump(ledger, allow_unicode=True, sort_keys=False, width=84), encoding='utf-8')
(OUT / 'new-visual-ledger.yaml').write_text(yaml.safe_dump({'schema_version': 1, 'visuals': new}, allow_unicode=True, sort_keys=False, width=84), encoding='utf-8')
(OUT / 'new-figures-review-audit.json').write_text(json.dumps(new_audit, indent=2), encoding='utf-8')

for name in ['browser-check.json', 'post-build-link-check.json']:
    assert read_json(OUT / name)['status'] == 'pass', name
chapter = ROOT / 'content/chapters/02-memory-dynamics.md'
current = chapter.read_text(encoding='utf-8')
original = (OUT / 'baseline/content/chapters/02-memory-dynamics.md').read_text(encoding='utf-8')
assert re.findall(r'^#+ .*$', original, re.M) == re.findall(r'^#+ .*$', current, re.M)
reverse = current
for item in reversed(read_json(OUT / 'insertions.json')):
    assert reverse.count(item['after']) == 1
    reverse = reverse.replace(item['after'], item['before'])
assert reverse == original
old_blocks = yaml.safe_load((OUT / 'baseline/content/chapters/02-memory-dynamics.yaml').read_text(encoding='utf-8'))['blocks']
blocks = yaml.safe_load(chapter.with_suffix('.yaml').read_text(encoding='utf-8'))['blocks']
assert [b for b in blocks if b['id'] not in ids] == old_blocks

bindings = read_json(OUT / 'current-bindings.json')
raw = OUT / 'raw-build-manifest.json'
manifest = read_json(raw)
assert manifest['book_model_hash'] == bindings['book_model_hash']
write_structure_lock(ROOT / 'guide-project.yaml', 'plan/structural-locks/current.yaml')
observed = audit_release(ROOT / 'guide-project.yaml')
assert observed['book_model_hash'] == bindings['book_model_hash']
html = observed['artifacts']['html']
manifest['artifacts'] = {'html': {k: html[k] for k in ['path','kind','bytes','file_count','sha256']}}
manifest['finalized_at'] = datetime.now().astimezone().isoformat()
manifest['quarto_build_manifest'] = {'path': raw.relative_to(ROOT).as_posix(), 'sha256': sha(raw)}
manifest['postprocess_evidence'] = ['verification/publication/paper-assets.json']
manifest['checks'] = [(OUT / n).relative_to(ROOT).as_posix() for n in ['post-build-link-check.json','browser-check.json','new-figures-review-audit.json']]
manifest['review_scope'] = 'Three Chapter 2 figures, their connected inserted text, and exact paper links; no whole-book review renewal.'
(ROOT / 'verification/manifests/build-manifest.json').write_text(json.dumps(manifest, indent=2), encoding='utf-8')
final_audit = audit_release(ROOT / 'guide-project.yaml')
(OUT / 'release-audit.json').write_text(json.dumps(final_audit, indent=2), encoding='utf-8')
assert final_audit['status'] == 'passed', final_audit.get('findings')

now = datetime.now().astimezone()
start = datetime.fromisoformat('2026-10-24T18:06:16.763030+03:00')
delivery = {
 'completed_at': now.isoformat(), 'task_started_at': start.isoformat(),
 'wall_elapsed_seconds': round((now-start).total_seconds(),1),
 'awake_execution_time': 'unverified', 'token_stats': 'unavailable',
 'chapter': 'ch:MEMORY-DYNAMICS', 'new_figures': 3, 'chapter_figures': 4,
 'source_pdf_links': 48, 'unique_pdf_targets': 33, 'source_notes': 14,
 'html_pdf_links': 54, 'original_mathematical_expressions_preserved': 170,
 'original_content_recovers_exactly': True, 'old_figure_metadata_and_records_preserved': True,
 'book_model_hash': manifest['book_model_hash'], 'html': manifest['artifacts']['html'],
 'checks': manifest['checks'], 'independent_review': ['stage1-review.md','stage2-review.md','focused-W1-W4-recheck.md','stage3-review.md','diagram-review.json'],
 'browser_scope': 'Three new figures at 878 and 390px, actual local horizontal scrolling, two representative PDF-link clicks, four screenshot inspections.',
 'repair': 'The M03 interval is inline math in its caption so Markdown creates the image correctly; no change to the interval or plotted data.',
 'review_scope': manifest['review_scope'], 'standard_release_audit': 'pass',
 'limit': 'Local HTML delivery only. Historical whole-chapter/legacy visual records and development tool locks remain; no public or authoritative release claim.'
}
for p in [OUT / 'DELIVERY.json', ROOT / 'verification/DELIVERY.json']:
    p.write_text(json.dumps(delivery, indent=2), encoding='utf-8')
print(json.dumps({k:delivery[k] for k in ['completed_at','wall_elapsed_seconds','new_figures','source_pdf_links','book_model_hash','standard_release_audit']}, indent=2))
