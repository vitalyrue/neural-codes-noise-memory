from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, urllib.request
from bs4 import BeautifulSoup

root=Path(__file__).resolve().parents[2]
task=Path(__file__).resolve().parent
results=[]
for chapter in ['ch-foundations','ch-memory-dynamics']:
    path=root/'site/chapters'/f'{chapter}.html'
    content=path.read_bytes()
    soup=BeautifulSoup(content,'html.parser')
    if chapter=='ch-foundations':
        section=soup.find(id='sec-memory-spikes')
        assert section and 'Equation 7' in section.get_text(' ',strip=True)
        assert 'Eq. 8' in section.get_text(' ',strip=True) and 'Eq. 9' in section.get_text(' ',strip=True)
        assert section.find(id='fig-memory-spike-trace')
        assert section.find('span',class_='definition-explanation')
        assert section.find('span',class_='key-statement')
    else:
        assert soup.find(id='sec-memory-weak-noise')
        assert soup.find(id='sec-memory-spikes') is None
        assert soup.find('a',href='ch-foundations.html#sec-memory-spikes')
    url=f'https://vrdell15.tail8b993e.ts.net/burak/chapters/{chapter}.html?foundationDynamics=20261101'
    with urllib.request.urlopen(url,timeout=20) as response:
        live=response.read()
        assert response.status==200
    assert live==content,chapter+' live bytes differ'
    results.append({'chapter':chapter,'url':url,'live_matches_built_html':True,'sha256':hashlib.sha256(content).hexdigest()})

script=(root/'site/scripts/chapter-redirects.js').read_text(encoding='utf-8')
assert '"sec-memory-spikes": "ch-foundations.html"' in script
assert '"fig-memory-spike-trace": "ch-foundations.html"' in script
report={'checked_at_utc':datetime.now(timezone.utc).isoformat(),'pages':results,
        'source_and_figure_bookmark_routes_present':True,'scope':'Two changed pages and relocated model/figure links only.'}
(task/'html-checks.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print('Both live chapters match built HTML; model, figure, definitions and bookmark routes are present.')
