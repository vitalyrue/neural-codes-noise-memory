from pathlib import Path
import yaml,json,hashlib,datetime,collections
p=Path('C:/dev/clsc/burak-papers/guide'); out=p/'verification/teaching-alignment-20261029'; h=lambda f:hashlib.sha256(f.read_bytes()).hexdigest()
d=yaml.safe_load((p/'source-maps/visual-ledger.yaml').read_text(encoding='utf-8')); rows=[]
audit=json.loads((out/'visual-audit.json').read_text(encoding='utf-8-sig'))
for v in d['visuals']:
 r=v.get('diagram_review',{}); c=v.get('review_contract',{}); asset=p/v['asset']; changed=[]; same=[]
 for name,old in r.get('input_sha256',{}).items():
  f=p/name; (same if f.exists() and h(f)==old else changed).append(name)
 row={'visual_id':v['visual_id'],'class':'paper-excerpt' if v.get('source_pdf') else 'guide-original','asset':v['asset'],'asset_sha256':h(asset),'ledger_asset_matches':h(asset)==v['sha256'],'review_asset_matches':h(asset)==r.get('reviewed_sha256') if r else None,'review_record_present':bool(r),'changed_inputs':changed,'unchanged_inputs':same,'findings':[x for x in audit['findings'] if x.get('location')==v['visual_id']]}
 if v.get('source_pdf'): row['source_pdf_matches']=h(p/v['source_pdf'])==v['source_pdf_sha256']
 rows.append(row)
summary={'started_at':'2026-10-29T10:26:45+00:00','checkpoint_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'awake_seconds':None,'awake_status':'unverified','counts':dict(collections.Counter(r['class'] for r in rows)),'ledger_asset_mismatches':[r['visual_id'] for r in rows if not r['ledger_asset_matches']],'review_asset_mismatches':[r['visual_id'] for r in rows if r['review_asset_matches'] is False],'rule_counts':dict(collections.Counter(x['rule'] for x in audit['findings'])),'rows':rows}
(out/'visual-current-inventory.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
paths=['source-maps/visual-ledger.yaml','source-maps/book-style-lock.yaml','skill-lock.yaml','content/chapters/01b-persistence.md','content/chapters/01b-persistence.yaml','content/chapters/06-synthesis.md','content/chapters/06-synthesis.yaml','content/chapters/05-place-fields.md','content/chapters/05-place-fields.yaml','assets/approved/visuals/attractor-directions.svg','assets/approved/visuals/synthesis-shared-position.png','assets/approved/visuals/paper-excerpts/place-fig-1.png','assets/papers/mainali-2025-universal-statistics.pdf']
(out/'visual-sample-source-hashes.json').write_text(json.dumps({f:h(p/f) for f in paths},indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in summary.items() if k!='rows'},indent=2)); print('input issue groups',collections.Counter(tuple(x['changed_inputs']) for x in rows if x['review_record_present']))
for name in ['01b-persistence.yaml','06-synthesis.yaml','05-place-fields.yaml']:
 y=yaml.safe_load((p/'content/chapters'/name).read_text(encoding='utf-8'))
 print(name,[(b['id'],b.get('width_inches')) for b in y.get('blocks',[]) if b.get('kind')=='figure'])
