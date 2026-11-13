from pathlib import Path
import json,datetime,hashlib,re
from bs4 import BeautifulSoup
O=Path(__file__).resolve().parent; R=O.parents[1]
O.mkdir(exist_ok=True); (O/'baseline').mkdir(exist_ok=True)
cases=[
('01-foundations.md','[**Example: an apparently silent cell','For changing rates,'),
('01b-persistence.md','[**Example: two disturbances','## Independent steps'),
('01b-persistence.md','[**Example: why the noise','Two times along a Brownian path'),
('02-memory-dynamics.md','**Example: a disturbance','## Projecting spike'),
('02-memory-dynamics.md','**Example: opposite firing','[^p1-model]:'),
('03-memory-information.md','**Example: the same diffusion','**Neural mechanism.** When a circuit stores several coordinates'),
('03b-memory-readout.md','**Example: limited spike','## Time scales and noise laws'),
('04-eye-drift.md','**Example: correlation 0.17','In the experiment, each cell gives'),
('06-synthesis.md','### Example: opposite rate','[Irregular single-cell responses can therefore')]
open_tag='<div class="publisher-worked-calculation publisher-fold-never">\n\n'
close_tag='</div>\n\n'
ledger=[]
for filename in dict.fromkeys(c[0] for c in cases):
    p=R/'content/chapters'/filename;raw=p.read_bytes();old=raw.decode('utf-8')
    (O/'baseline'/filename).write_bytes(raw)
    newline='\r\n' if '\r\n' in old else '\n'
    opening=open_tag.replace('\n',newline);closing=close_tag.replace('\n',newline)
    edits=[]
    for _,start,end in [c for c in cases if c[0]==filename]:
        assert old.count(start)==old.count(end)==1,(filename,start,end)
        a=old.index(start);b=old.index(end);assert a<b
        block=old[a:b]
        assert block.endswith(newline+newline)
        edits.append(dict(start=a,end=b,old=block,new=opening+block+closing))
    new=old
    for e in sorted(edits,key=lambda e:e['start'],reverse=True):new=new[:e['start']]+e['new']+new[e['end']:]
    restored=new
    for e in edits:restored=restored.replace(e['new'],e['old'],1)
    assert restored==old
    p.write_bytes(new.encode('utf-8'))
    ledger.append(dict(file=filename,before=hashlib.sha256(raw).hexdigest(),after=hashlib.sha256(new.encode()).hexdigest(),examples=len(edits),edits=edits))
# Baseline rendered content for only the affected pages, for text / link checks.
names=['ch-foundations','ch-persistence','ch-memory-dynamics','ch-memory-information','ch-memory-readout','ch-eye-drift','ch-synthesis']
baseline={}
for name in names:
    p=R/'site/chapters'/f'{name}.html';s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser').find('main')
    baseline[name]=dict(text=re.sub(r'\s+',' ',s.get_text()),headings=[x.get_text() for x in s.select('h1,h2,h3')],ids=sorted(x['id'] for x in s.select('[id]')),images=[x.get('src') for x in s.select('img')],links=[x.get('href') for x in s.select('a')])
(O/'baseline/rendered.json').write_text(json.dumps(baseline,ensure_ascii=False,indent=2),encoding='utf-8')
now=datetime.datetime.now().astimezone().isoformat()
(O/'edits.json').write_text(json.dumps(dict(at=now,files=ledger),ensure_ascii=False,indent=2),encoding='utf-8')
(O/'STATE.json').write_text(json.dumps(dict(startedAt='2026-10-28T17:57:32.6432061+02:00',checkpointAt=now,status='Nine complete examples wrapped; build next',scope='Presentation only; exact source text preserved; existing shared panel style; examples remain open',awakeExecution='unverified'),indent=2),encoding='utf-8')
print('Wrapped 9 examples in 7 chapters; exact source reversal passed.')
