from pathlib import Path
from html.parser import HTMLParser
import re,json,datetime,hashlib
from bs4 import BeautifulSoup
O=Path(__file__).resolve().parent;R=O.parents[1]
class MainText(HTMLParser):
    def __init__(self):super().__init__();self.active=False;self.text=[]
    def handle_starttag(self,tag,attrs):
        if tag=='main':self.active=True
    def handle_endtag(self,tag):
        if tag=='main':self.active=False
    def handle_data(self,data):
        if self.active:self.text.append(data)
    def normalized(self):return re.sub(r'\s+',' ',''.join(self.text)).strip()
prior=json.loads((O/'baseline/rendered-main-text.json').read_text(encoding='utf-8'))
rows=[];counts={'key':0,'definition':0,'term':0};problems=[]
for name,old in prior.items():
    html=(R/'site'/name).read_text(encoding='utf-8');parser=MainText();parser.feed(html)
    same=parser.normalized()==old
    if not same: problems.append(dict(page=name,issue='Rendered text changed'))
    soup=BeautifulSoup(html,'html.parser'); main=soup.find('main')
    c={'key':len(soup.select('main .key-statement')),'definition':len(soup.select('main .definition-explanation')),'term':len(soup.select('main .definition-term'))}
    for k in counts:counts[k]+=c[k]
    if main and ('{.key-statement}' in main.get_text() or '{.definition-explanation}' in main.get_text()):problems.append(dict(page=name,issue='Leaked Markdown'))
    rows.append(dict(page=name,rendered_text_unchanged=same,**c))
assert counts=={'key':76,'definition':187,'term':194},counts
assert not problems,problems
ledger=json.loads((O/'edit-ledger.json').read_text(encoding='utf-8'))
for f in ledger['files']:
    raw=(R/'content/chapters'/f['file']).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==f['after_sha256'],f['file']
    restored=raw.decode('utf-8')
    for e in f['edits']:restored=restored.replace(e['new'],e['old'],1)
    assert hashlib.sha256(restored.encode('utf-8')).hexdigest()==f['before_sha256'],f['file']
result=dict(at=datetime.datetime.now().astimezone().isoformat(),passed=True,counts=counts,all_original_source_and_rendered_words_preserved=True,pages=rows)
(O/'render-checks.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(dict(passed=True,counts=counts,pages=len(rows))))
