"""Record this local illustration delivery after scoped reviews and rendering checks."""
from pathlib import Path
from datetime import datetime
import hashlib, json, sys, yaml
ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
sys.path.insert(0, 'C:/Users/vital/.codex/skills/course-diagram-builder/scripts')
from visual_review import audit_ledger, validate_visual_review
from book_runtime.release_audit import audit_release, write_structure_lock
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
read = lambda p: json.loads(p.read_text(encoding='utf-8'))
packet = read(OUT / 'integration.json')
ids = {r['visual_id'] for r in packet}
reviews = {}
for name in ['diagram-review-A01-A04.json', 'diagram-review-A05-A09.json']:
    group = read(OUT / name)
    assert not (set(reviews) & set(group))
    reviews.update(group)
assert set(reviews) == ids
(OUT / 'diagram-review.json').write_text(json.dumps(reviews, indent=2), encoding='utf-8')
lp = ROOT / 'source-maps/visual-ledger.yaml'
ledger = yaml.safe_load(lp.read_text(encoding='utf-8'))
new = []
for row in ledger['visuals']:
    if row['visual_id'] not in ids: continue
    row['diagram_review'] = reviews[row['visual_id']]
    errors = validate_visual_review(row, ROOT)
    assert not errors, (row['visual_id'], errors)
    new.append(row)
checked = audit_ledger({'visuals': new}, ROOT)
assert checked['status'] == 'pass' and checked['reviewed_figures'] == 9
baseline = yaml.safe_load((OUT / 'baseline/source-maps/visual-ledger.yaml').read_text(encoding='utf-8'))
assert [v for v in ledger['visuals'] if v['visual_id'] not in ids] == baseline['visuals']
for name in ['browser-check.json', 'post-build-check.json', 'browser-pixel-review.json']:
    assert read(OUT / name)['status'] == 'pass', name
assert (OUT / 'stage2-review.json').exists() and (OUT / 'stage3-review.json').exists()
lp.write_text(yaml.safe_dump(ledger, allow_unicode=True, sort_keys=False, width=84), encoding='utf-8')
(OUT / 'new-visual-ledger.yaml').write_text(yaml.safe_dump({'schema_version': 1, 'visuals': new}, allow_unicode=True, sort_keys=False, width=84), encoding='utf-8')
(OUT / 'new-figures-review-audit.json').write_text(json.dumps(checked, indent=2), encoding='utf-8')
bindings = read(OUT / 'current-bindings.json')
raw = OUT / 'raw-build-manifest.json'
manifest = read(raw)
assert manifest['book_model_hash'] == bindings['book_model_hash']
write_structure_lock(ROOT / 'guide-project.yaml', 'plan/structural-locks/current.yaml')
observed = audit_release(ROOT / 'guide-project.yaml')
assert observed['book_model_hash'] == bindings['book_model_hash']
html = observed['artifacts']['html']
manifest['artifacts'] = {'html': {k: html[k] for k in ['path', 'kind', 'bytes', 'file_count', 'sha256']}}
manifest['finalized_at'] = datetime.now().astimezone().isoformat()
manifest['quarto_build_manifest'] = {'path': raw.relative_to(ROOT).as_posix(), 'sha256': sha(raw)}
manifest['postprocess_evidence'] = ['verification/publication/paper-assets.json']
manifest['checks'] = [(OUT / n).relative_to(ROOT).as_posix() for n in ['post-build-check.json', 'browser-check.json', 'browser-pixel-review.json', 'new-figures-review-audit.json']]
manifest['review_scope'] = 'Nine new images and connected insertions across Chapters 1, 3, 4, 5 and 6; existing Chapter 2 unchanged. No whole-book review renewal.'
(ROOT / 'verification/manifests/build-manifest.json').write_text(json.dumps(manifest, indent=2), encoding='utf-8')
audit = audit_release(ROOT / 'guide-project.yaml')
(OUT / 'release-audit.json').write_text(json.dumps(audit, indent=2), encoding='utf-8')
assert audit['status'] == 'passed', audit.get('findings')
now = datetime.now().astimezone()
start = datetime.fromisoformat('2026-10-24T18:31:14.999410+03:00')
delivery = {'completed_at': now.isoformat(), 'task_started_at': start.isoformat(),
 'wall_elapsed_seconds': round((now-start).total_seconds(), 1),
 'awake_execution_time': 'unverified', 'token_stats': 'unavailable',
 'new_figures': 9, 'teaching_chapters_with_figures': 6, 'total_teaching_figures': 22,
 'new_source_pdf_links': 8, 'original_content_recovers_exactly': True,
 'old_figure_metadata_and_records_preserved': True,
 'book_model_hash': manifest['book_model_hash'], 'html': manifest['artifacts']['html'],
 'checks': manifest['checks'],
 'independent_review': ['stage1-A01-A04.json', 'stage1-A05-A08.json', 'stage1-A09.json', 'stage2-review.json', 'focused-W1-W4-recheck.json', 'stage3-review.json', 'diagram-review.json'],
 'browser_scope': 'Nine figures at 878 and 390 px, actual local horizontal scrolling; three page contexts visually sampled.',
 'review_scope': manifest['review_scope'], 'standard_release_audit': 'pass',
 'limit': 'Local HTML delivery. Historical whole-chapter and earlier visual records and development tool locks remain; no public or authoritative release claim.'}
for target in [OUT / 'DELIVERY.json', ROOT / 'verification/DELIVERY.json']:
    target.write_text(json.dumps(delivery, indent=2), encoding='utf-8')
print(json.dumps({k:delivery[k] for k in ['completed_at','wall_elapsed_seconds','new_figures','book_model_hash','standard_release_audit']}, indent=2))
