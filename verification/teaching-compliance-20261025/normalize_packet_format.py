from pathlib import Path
from datetime import datetime
import sys,json,re,hashlib
OUT=Path(__file__).resolve().parent
sys.path.insert(0,'C:/dev/NBIS/publisher-releases/0.8.23/skills/course-quality-gate/scripts')
from orchestrate_pedagogy_reviews import REVIEW_FIELDS
changes=[]
for p in (OUT/'pedagogy-final').glob('PEDAGOGY_REVIEW_*.md'):
    old=p.read_text(encoding='utf-8');rows=[]
    for n,line in enumerate(old.splitlines(),1):
        original=line
        for label in sorted(REVIEW_FIELDS,key=len,reverse=True):
            prefix='- '+label+': '
            if line.startswith(prefix):
                value=line[len(prefix):]
                if not (value.startswith('[') and value.endswith(']')):
                    value='['+value+']'
                value=re.sub(r'\b(lines?|paragraphs?)(?=\d)',r'\1 ',value)
                line=prefix+value;break
        if line!=original:changes.append({'file':p.name,'line':n,'before':original,'after':line})
        rows.append(line)
    if old!='\n'.join(rows)+'\n':p.write_text('\n'.join(rows)+'\n',encoding='utf-8')
record={'at':datetime.now().astimezone().isoformat(),'scope':'Mechanical bracket/line-locator syntax required by Publisher packet parser; independent answer wording is preserved. Original completed packets/fragments remain evidenced by independent reports.','changes':changes}
(OUT/'packet-format-normalization.json').write_text(json.dumps(record,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'formatted_fields':len(changes)}))
