from pathlib import Path
from datetime import datetime
import hashlib,json
from book_runtime.release_audit import load_book,audit_release
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[1]
read=lambda p:json.loads(p.read_text(encoding='utf-8'))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for name in ['source-check.json','rendered-check.json','browser-check.json','pixel-review.json']:assert read(OUT/name)['status']=='pass',name
accept=read(OUT/'acceptance.json')
for rel,digest in accept['source_bindings'].items():assert sha(ROOT/rel)==digest,rel
review_bindings=[]
for group,key in [('foundations-memory','source_snapshots'),('information-eye','sources'),('place-synthesis','source_observations')]:
 review=read(OUT/f'stage3-{group}.json')
 for s in review[key]:
  rel=s.get('path',s.get('file'));rel=rel if '/' in rel else 'content/chapters/'+rel
  assert sha(ROOT/rel)==s['sha256'].lower(),(group,rel)
  review_bindings.append({'review':f'stage3-{group}.json','path':rel,'sha256':s['sha256'].lower(),'matches_current':True})
(OUT/'review-bindings.json').write_text(json.dumps(review_bindings,indent=2),encoding='utf-8')
book=load_book(ROOT/'guide-project.yaml');manifest=read(OUT/'raw-build-manifest.json')
assert book.content_hash()==manifest['book_model_hash']
html=audit_release(ROOT/'guide-project.yaml')['artifacts']['html']
manifest['artifacts']={'html':{k:html[k] for k in ['path','kind','bytes','file_count','sha256']}}
manifest['finalized_at']=datetime.now().astimezone().isoformat()
manifest['quarto_build_manifest']={'path':(OUT/'raw-build-manifest.json').relative_to(ROOT).as_posix(),'sha256':sha(OUT/'raw-build-manifest.json')}
manifest['postprocess_evidence']=['verification/publication/paper-assets.json']
manifest['checks']=[(OUT/name).relative_to(ROOT).as_posix() for name in ['acceptance.json','review-bindings.json','source-check.json','rendered-check.json','browser-check.json','pixel-review.json']]
manifest['review_scope']=accept['scope']
(ROOT/'verification/manifests/build-manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
audit=audit_release(ROOT/'guide-project.yaml');(OUT/'release-audit.json').write_text(json.dumps(audit,indent=2),encoding='utf-8');assert audit['status']=='passed',audit.get('findings')
now=datetime.now().astimezone();start=datetime.fromisoformat('2026-10-24T20:17:28.7375959+03:00')
delivery={'completed_at':now.isoformat(),'started_at':start.isoformat(),'wall_elapsed_seconds':round((now-start).total_seconds(),1),'awake_execution_time':'unverified','token_stats':'unavailable','chapters_before':6,'chapters_after':13,'motivated_openings':13,'section_bodies':'49 complete main sections plus one nested example, retained in order except recorded cross-reference repairs','figures_preserved':22,'tables_preserved':4,'optional_notes_preserved':10,'screen_body_font_before_px':17,'screen_body_font_after_px':11.9,'screen_font_reduction_percent':30,'print_type_sizes':'unchanged in representative desktop/mobile browser checks','default_saved':['C:/Users/vital/.codex/AGENTS.md','C:/Users/vital/.codex/memories/extensions/ad_hoc/notes/20261024-document-font-default.md'],'old_bookmarks':'41 moved stable anchors mapped; actual old foundations-map bookmark exercised in browser','preview':'http://127.0.0.1:8765/guide/site/','book_model_hash':book.content_hash(),'html':manifest['artifacts']['html'],'standard_release_audit':'pass','browser_scope':'Three screenshots inspected, exact font checks at878px and390px, example interaction and moved bookmark tested;19HTML pages checked mechanically for local links.','limits':accept['limits']}
for p in [OUT/'DELIVERY.json',ROOT/'verification/DELIVERY.json']:p.write_text(json.dumps(delivery,indent=2),encoding='utf-8')
print(json.dumps(delivery,indent=2))
