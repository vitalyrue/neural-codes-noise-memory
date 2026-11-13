"""One-time conversion of the three remaining raw pipe tables."""
from pathlib import Path
from datetime import datetime
import hashlib,json,re,yaml
ROOT=Path(__file__).resolve().parents[1]
assignments={
 '04-eye-drift.md':[('tbl:EYE-FIGURE-GUIDE','sec:EYE-FIGURES','Reading the figures as an argument.')],
 '05-place-fields.md':[('tbl:PLACE-SIZE-LAWS','sec:PLACE-SIZE-LAW','Field-size laws in one, two, and three dimensions.'),('tbl:PLACE-DATA-COMPARISONS','sec:PLACE-DATA','Fitted quantities and additional comparisons.')],
}
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
report={'task_started_at':'2026-10-23T21:23:47.9951655+03:00','applied_at':datetime.now().astimezone().isoformat(),'scope':'All remaining reader-source pipe tables; exact cell/prose preservation, no new semantic review.','files':[]}
pattern=re.compile(r'(?m)^\|[^\n]+\n\|[- :|]+\|\s*\n(?:\|[^\n]+\n)+')
for name,items in assignments.items():
 p=ROOT/'content/chapters'/name; side=p.with_suffix('.yaml'); old=p.read_text(encoding='utf-8'); matches=list(pattern.finditer(old)); assert len(matches)==len(items),(name,len(matches))
 metadata=yaml.safe_load(side.read_text(encoding='utf-8')); before={'source':sha(p),'sidecar':sha(side)}; replacements=[]; tables=[]
 for m,(tid,placement,caption) in zip(matches,items):
  lines=m[0].strip().splitlines(); cells=lambda line:[s.strip() for s in line.strip().strip('|').split('|')]
  headers=cells(lines[0]); rows=[cells(s) for s in lines[2:]]; assert rows and all(len(r)==len(headers) for r in rows)
  assert not any(b['id']==tid for b in metadata.get('blocks',[]))
  metadata.setdefault('blocks',[]).append({'id':tid,'kind':'table','placement':placement,'headers':headers,'rows':rows,'caption':caption,'first_column_role':'row-labels','html_fold':'never'})
  replacement='<div class="table-responsive">\n\n{{block:'+tid+'}}\n\n</div>\n'; replacements.append((m[0],replacement));tables.append({'id':tid,'placement':placement,'original_markdown':m[0],'headers':headers,'rows':rows})
 new=old
 for original,replacement in replacements: assert new.count(original)==1;new=new.replace(original,replacement)
 restored=new
 for original,replacement in replacements:restored=restored.replace(replacement,original)
 assert restored==old,'Outside-table source changed'
 p.write_text(new,encoding='utf-8',newline='\n');side.write_text(yaml.safe_dump(metadata,sort_keys=False,allow_unicode=True),encoding='utf-8')
 report['files'].append({'source':p.relative_to(ROOT).as_posix(),'before_sha256':before,'after_sha256':{'source':sha(p),'sidecar':sha(side)},'outside_table_source_identical':True,'tables':tables})
assert not any(pattern.search(p.read_text(encoding='utf-8')) for p in (ROOT/'content/chapters').glob('*.md'))
(ROOT/'verification/publication/table-repair-20261023.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'files':len(report['files']),'tables_converted':sum(len(f['tables']) for f in report['files']),'remaining_raw_reader_tables':0,'all_cells_preserved':True}))
