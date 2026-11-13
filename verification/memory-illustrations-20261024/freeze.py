"""Record actual review inputs; does not approve any figure."""
from pathlib import Path
from datetime import datetime
import json, sys, yaml
ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
sys.path.insert(0, 'C:/Users/vital/.codex/skills/course-diagram-builder/scripts')
from visual_review import policy_hash, context_hash, file_hash, review_input_paths
from book_runtime.release_audit import load_book
book = load_book(ROOT / 'guide-project.yaml')
chapters = [*book.front_matter, *[c for p in book.parts for c in p.chapters], *book.appendices]
chapter = next(c for c in chapters if c.chapter_id == 'ch:MEMORY-DYNAMICS')
ledger = yaml.safe_load((ROOT / 'source-maps/visual-ledger.yaml').read_text(encoding='utf-8'))
ids = {'fig:MEMORY-SPIKE-TRACE', 'fig:MEMORY-INHIBITION-RATES', 'fig:MEMORY-LINE-RING'}
rows = [v for v in ledger['visuals'] if v['visual_id'] in ids]
bindings = {}
for row in rows:
    bindings[row['visual_id']] = {
        'policy_sha256': policy_hash(), 'context_sha256': context_hash(row),
        'reviewed_sha256': file_hash(ROOT / row['asset']),
        'input_sha256': {name: file_hash(ROOT / name) for name in review_input_paths(row['review_contract'])},
        'source_scope_sha256': {chapter.chapter_id: chapter.content_hash},
        'review_contract': row['review_contract']}
packet = {'status': 'bindings only, not approval', 'at': datetime.now().astimezone().isoformat(),
          'book_model_hash': book.content_hash(), 'figures': bindings}
(OUT / 'current-bindings.json').write_text(json.dumps(packet, indent=2), encoding='utf-8')
print(json.dumps({'snapshotted': len(rows), 'book_model_hash': packet['book_model_hash']}))
