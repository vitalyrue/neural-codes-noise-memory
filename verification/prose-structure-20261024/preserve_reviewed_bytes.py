from pathlib import Path
import hashlib,json
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
record=json.loads((OUT/'integration.json').read_text(encoding='utf-8'));changed=[]
for r in record['records']:
 canonical=ROOT/r['file'];proposed=OUT/'proposed/content/chapters'/canonical.name
 assert canonical.read_text(encoding='utf-8')==proposed.read_text(encoding='utf-8')
 if sha(canonical)!=sha(proposed):
  canonical.write_bytes(proposed.read_bytes());changed.append(r['file'])
 r['after_sha256']=sha(canonical)
record['reviewed_line_endings_preserved']=changed
(OUT/'integration.json').write_text(json.dumps(record,indent=2),encoding='utf-8')
print(json.dumps({'reviewed_bytes_preserved':changed}))
