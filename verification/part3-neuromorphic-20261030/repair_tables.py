from pathlib import Path
import re,json,yaml,hashlib,shutil
from datetime import datetime,timezone
root=Path(__file__).resolve().parents[2]; task=Path(__file__).resolve().parent
records=[]
for name,tid,sid,caption in [
 ('07-hardware-memory','tbl:HARDWARE-STORAGE','sec:HARDWARE-MEMORY-STORAGE','Physical states and the information they can represent.'),
 ('09-neuromorphic-systems','tbl:NEUROMORPHIC-ARCHITECTURES','sec:NEUROMORPHIC-SYSTEMS-ARCHITECTURES','Where selected neuromorphic systems store and update their variables.'),
 ('10-hardware-tests','tbl:HARDWARE-TEST-PARAMETERS','sec:HARDWARE-TESTS-PARAMETERS','Controlled changes and the memory measurements they motivate.'),
]:
 p=root/'content/chapters'/(name+'.md'); before=p.read_bytes(); text=before.decode('utf-8').replace('\r\n','\n')
 m=re.search(r'^\|[^\n]+\|\n\|[-| ]+\|\n(?:\|[^\n]+\|\n)+',text,re.M)
 assert m,name
 cells=[[v.strip() for v in line.strip().strip('|').split('|')] for line in m[0].strip().splitlines()]
 headers=cells[0];rows=cells[2:];assert all(len(row)==len(headers) for row in rows)
 replacement='<div class="table-responsive">\n\n{{block:'+tid+'}}\n\n</div>\n'
 text=text[:m.start()]+replacement+text[m.end():]
 side=p.with_suffix('.yaml'); meta=yaml.safe_load(side.read_text(encoding='utf-8'))
 assert not any(b['id']==tid for b in meta['blocks'])
 table=dict(id=tid,kind='table',placement=sid,headers=headers,rows=rows,caption=caption,first_column_role='row-labels',html_fold='never')
 meta['blocks'].append(table)
 p.write_text(text,encoding='utf-8');side.write_text(yaml.safe_dump(meta,sort_keys=False,allow_unicode=True,width=105),encoding='utf-8')
 check=yaml.safe_load(side.read_text(encoding='utf-8'))['blocks'][-1]
 assert check['headers']==headers and check['rows']==rows
 records.append(dict(file=str(p.relative_to(root)),before_sha256=hashlib.sha256(before).hexdigest(),after_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),table_id=tid,cells_sha256=hashlib.sha256(json.dumps([headers,rows],ensure_ascii=False).encode()).hexdigest(),all_cell_text_unchanged=True,caption=caption))
shutil.copy2(task/'concept-index-final.json',task/'concept-index-before-table-format.json')
(task/'table-format-reuse.json').write_text(json.dumps({'at':datetime.now(timezone.utc).isoformat(),'reason':'Raw pipe paragraphs did not render as tables. Move identical reviewed cells into native typed table blocks; no scientific claim changed. Captions describe the existing comparisons.','records':records},indent=2),encoding='utf-8')
p=task/'footnote-spacing-reuse.json';d=json.loads(p.read_text(encoding='utf-8'))
for r in d['records']:
 r['before_lf_normalized_sha256']=r.pop('before_sha256');r['after_lf_normalized_sha256']=r.pop('after_sha256')
d['hash_note']='These hashes identify decoded text normalized to LF, not Windows file bytes. Equality check normalized whitespace and proved no word/markup change. Final raw-byte hashes are recorded in scoped acceptance and review records.'
p.write_text(json.dumps(d,indent=2),encoding='utf-8')
print('Converted three tables; every reviewed header and cell preserved.')
