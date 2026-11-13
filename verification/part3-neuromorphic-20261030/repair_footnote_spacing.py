from pathlib import Path
import re,json,hashlib
from datetime import datetime,timezone
root=Path(__file__).resolve().parents[2]; records=[]
for filename in ['07-hardware-memory.md','08-hardware-dynamics.md','09-neuromorphic-systems.md']:
 p=root/'content/chapters'/filename; before=p.read_text(encoding='utf-8'); lines=before.splitlines()
 starts=[]
 for i,line in enumerate(lines):
  if re.match(r'^\[\^[^]]+\]:',line):
   j=i
   while j>0 and re.match(r'<!-- vale .+ = NO -->$',lines[j-1]):j-=1
   if j>0 and lines[j-1].strip():starts.append(j)
 for j in reversed(starts):lines.insert(j,'')
 after='\n'.join(lines)+'\n'
 assert re.sub(r'\s+',' ',before)==re.sub(r'\s+',' ',after)
 p.write_text(after,encoding='utf-8')
 records.append(dict(file=str(p.relative_to(root)),before_sha256=hashlib.sha256(before.encode()).hexdigest(),after_sha256=hashlib.sha256(after.encode()).hexdigest(),inserted_blank_lines=len(starts),words_and_markup_unchanged=True))
out=dict(at=datetime.now(timezone.utc).isoformat(),reason='New footnote blocks separated by adjacent lint comments were parsed as one block. Match the existing working footnote paragraph spacing.',records=records)
(Path(__file__).parent/'footnote-spacing-reuse.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out))
