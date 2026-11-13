"""Apply reviewed, exact inline selections and prove all original text survives."""
from pathlib import Path
import datetime, hashlib, json, re
from html.parser import HTMLParser

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[1]
def digest(b): return hashlib.sha256(b).hexdigest()
def now(): return datetime.datetime.now(datetime.timezone.utc).isoformat()

class MainText(HTMLParser):
    def __init__(self):
        super().__init__(); self.active=False; self.text=[]
    def handle_starttag(self, tag, attrs):
        if tag == 'main': self.active=True
    def handle_endtag(self, tag):
        if tag == 'main': self.active=False
    def handle_data(self, data):
        if self.active: self.text.append(data)
    def normalized(self): return re.sub(r'\s+', ' ', ''.join(self.text)).strip()

files=[]
for name in ['selections-memory.json','selections-eye-place.json','selections-reading.json']:
    files.extend(json.loads((OUT/name).read_text(encoding='utf-8'))['files'])
assert len({f['file'] for f in files}) == len(files) == 15
ledger=[]; prepared=[]
for f in files:
    path=ROOT/'content/chapters'/f['file']
    raw=path.read_bytes(); assert digest(raw)==f['sha256'], f['file']
    assert raw==(OUT/'baseline/chapters'/f['file']).read_bytes()
    old=raw.decode('utf-8'); spans=[]
    for item in f['selections']:
        selected=item['text']; assert old.count(selected)==1,(f['file'],selected)
        assert '\n' not in selected, (f['file'],'multiline selection')
        start=old.index(selected); end=start+len(selected)
        css={'key':'key-statement','definition':'definition-explanation'}[item['kind']]
        replacement='['+selected+']{.'+css+'}'
        spans.append(dict(start=start,end=end,old=selected,new=replacement,kind=item['kind']))
    spans.sort(key=lambda x:x['start'])
    assert all(a['end']<=b['start'] for a,b in zip(spans,spans[1:])),f['file']
    new=old
    for s in reversed(spans): new=new[:s['start']]+s['new']+new[s['end']:]
    restored=new
    for s in spans:
        assert restored.count(s['new'])==1
        restored=restored.replace(s['new'],s['old'],1)
    assert restored.encode('utf-8')==raw, f['file']
    ledger.append(dict(file=f['file'],before_sha256=digest(raw),after_sha256=digest(new.encode('utf-8')),edits=spans,exact_reversal=True))
    prepared.append((path,new))

# Save the prior rendered words independently of markup and style.
rendered={}
for path in (ROOT/'site').rglob('*.html'):
    if 'site_libs' in path.parts: continue
    parser=MainText();parser.feed(path.read_text(encoding='utf-8'))
    rendered[path.relative_to(ROOT/'site').as_posix()]=parser.normalized()
(OUT/'baseline/rendered-main-text.json').write_text(json.dumps(rendered,ensure_ascii=False,indent=2),encoding='utf-8')
(OUT/'edit-ledger.json').write_text(json.dumps(dict(at=now(),files=ledger),ensure_ascii=False,indent=2),encoding='utf-8')
for path,new in prepared: path.write_bytes(new.encode('utf-8'))
counts={k:sum(s['kind']==k for f in ledger for s in f['edits']) for k in ['key','definition']}
state=json.loads((OUT/'STATE.json').read_text());state.update(checkpointUtc=now(),status='Inline markup applied; exact original text recoverable',counts=counts)
(OUT/'STATE.json').write_text(json.dumps(state,indent=2),encoding='utf-8')
print(json.dumps(dict(files=len(files),counts=counts,all_original_text_preserved=True)))
