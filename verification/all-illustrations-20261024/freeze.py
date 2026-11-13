"""Record final source and image inputs without granting approval."""
from pathlib import Path
from datetime import datetime
import json, sys, yaml
ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
sys.path.insert(0, 'C:/Users/vital/.codex/skills/course-diagram-builder/scripts')
from visual_review import policy_hash, context_hash, file_hash, review_input_paths
from book_runtime.release_audit import load_book
book = load_book(ROOT / 'guide-project.yaml')
chapters = {c.chapter_id:c for c in [*book.front_matter, *[c for p in book.parts for c in p.chapters], *book.appendices]}
packet = json.loads((OUT / 'integration.json').read_text(encoding='utf-8'))
id_chapter = {r['visual_id']:r['chapter_id'] for r in packet}
ledger = yaml.safe_load((ROOT / 'source-maps/visual-ledger.yaml').read_text(encoding='utf-8'))
bindings = {}
for row in ledger['visuals']:
    if row['visual_id'] not in id_chapter: continue
    chapter = chapters[id_chapter[row['visual_id']]]
    bindings[row['visual_id']] = {'policy_sha256': policy_hash(), 'context_sha256': context_hash(row),
      'reviewed_sha256': file_hash(ROOT / row['asset']),
      'input_sha256': {name:file_hash(ROOT / name) for name in review_input_paths(row['review_contract'])},
      'source_scope_sha256': {chapter.chapter_id:chapter.content_hash}, 'review_contract': row['review_contract']}
assert len(bindings) == 9
result = {'status': 'bindings only, not approval', 'at': datetime.now().astimezone().isoformat(), 'book_model_hash': book.content_hash(), 'figures': bindings}
(OUT / 'current-bindings.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
print(json.dumps({'snapshotted': len(bindings), 'book_model_hash': result['book_model_hash']}))
