"""Preserve footnote definitions as distinct Publisher Markdown blocks."""
from pathlib import Path
import hashlib,json,re,datetime
ROOT=Path(__file__).resolve().parents[1]
records=[]
for p in (ROOT/'content/chapters').glob('*.md'):
 old=p.read_text(encoding='utf-8')
 new=re.sub(r'(?m)(?<!\n)\n(?=\[\^[^\]]+\]:)', '\n\n', old)
 assert re.sub(r'\s+',' ',old)==re.sub(r'\s+',' ',new)
 if new!=old:
  records.append(dict(file=p.relative_to(ROOT).as_posix(),before_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),after_sha256=hashlib.sha256(new.encode('utf-8')).hexdigest(),normalized_text_identical=True))
  p.write_text(new,encoding='utf-8',newline='\n')
report=dict(applied_at=datetime.datetime.now().astimezone().isoformat(),reason='Publisher joined adjacent definition lines into one paragraph; blank blocks keep each footnote independently resolvable. Whitespace-only source repair.',files=records)
(ROOT/'verification/publication/footnote-format-repair.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))
