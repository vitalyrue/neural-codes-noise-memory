"""Snapshot current review inputs without making an approval judgment."""
from pathlib import Path
import datetime,json,sys,yaml
ROOT=Path(__file__).resolve().parents[2]
SCRIPTS=Path('C:/Users/vital/.codex/skills/course-diagram-builder/scripts')
sys.path.insert(0,str(SCRIPTS))
from visual_review import policy_hash,context_hash,file_hash,review_input_paths
from book_runtime.release_audit import load_book

ledger=yaml.safe_load((ROOT/'source-maps/visual-ledger.yaml').read_text(encoding='utf-8'))
book=load_book(ROOT/'guide-project.yaml')
chapters=[*book.front_matter,*[c for p in book.parts for c in p.chapters],*book.appendices]
hashes={c.chapter_id:c.content_hash for c in chapters}
rows=[v for v in ledger['visuals'] if 'review_contract' in v]
bindings={}
for v in rows:
    stem=Path(v['caption_and_alt']).stem
    side=yaml.safe_load((ROOT/v['caption_and_alt']).read_text(encoding='utf-8'))
    cid=side['chapter_id']
    bindings[v['visual_id']]={
        'policy_sha256':policy_hash(),'context_sha256':context_hash(v),
        'reviewed_sha256':file_hash(ROOT/v['asset']),
        'input_sha256':{name:file_hash(ROOT/name) for name in review_input_paths(v['review_contract'])},
        'source_scope_sha256':{cid:hashes[cid]},
        'review_contract':v['review_contract'],
    }
packet={'status':'bindings-only, not approval','at':datetime.datetime.now().astimezone().isoformat(),
        'book_model_hash':book.content_hash(),'figures':bindings}
(ROOT/'verification/illustrations/current-bindings.json').write_text(json.dumps(packet,indent=2),encoding='utf-8')
(ROOT/'verification/illustrations/new-visual-ledger.yaml').write_text(yaml.safe_dump({'schema_version':1,'visual_ledger_version':3,'visuals':rows},sort_keys=False,allow_unicode=True),encoding='utf-8')
print(json.dumps({'snapshotted':len(rows),'book_model_hash':book.content_hash(),'at':packet['at']},indent=2))
