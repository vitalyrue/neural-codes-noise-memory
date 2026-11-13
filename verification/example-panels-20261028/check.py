from pathlib import Path
import json,re,datetime
from bs4 import BeautifulSoup
O=Path(__file__).resolve().parent;R=O.parents[1]
old=json.loads((O/'baseline/rendered.json').read_text(encoding='utf-8'))
expected={'ch-foundations':1,'ch-persistence':2,'ch-memory-dynamics':2,'ch-memory-information':1,'ch-memory-readout':1,'ch-eye-drift':1,'ch-synthesis':1}
rows=[]
for name,prior in old.items():
    s=BeautifulSoup((R/'site/chapters'/f'{name}.html').read_text(encoding='utf-8'),'html.parser').find('main')
    panels=s.select('.publisher-worked-calculation')
    assert len(panels)==expected[name],(name,len(panels))
    assert re.sub(r'\s+',' ',s.get_text())==prior['text'],(name,'rendered text')
    assert [x.get_text() for x in s.select('h1,h2,h3')]==prior['headings'],(name,'headings')
    assert [x.get('src') for x in s.select('img')]==prior['images'],(name,'images')
    assert [x.get('href') for x in s.select('a')]==prior['links'],(name,'links')
    descriptions=[]
    for panel in panels:
        first=panel.find(['p','h3']);assert first and first.get_text().lstrip().startswith(('Example:','13.2.1')),(name,'title',first)
        assert 'publisher-fold-never' in panel['class']
        descriptions.append(dict(title=first.get_text(),paragraphs=len(panel.find_all('p')),figures=len(panel.select('figure')),ending=panel.get_text().strip()[-180:]))
    rows.append(dict(page=name,panels=descriptions,text_headings_images_links_unchanged=True))
result=dict(at=datetime.datetime.now().astimezone().isoformat(),passed=True,examples=sum(expected.values()),pages=rows)
(O/'checks.json').write_text(json.dumps(result,indent=2,ensure_ascii=False),encoding='utf-8')
print('9 panels rendered in 7 chapters; text, headings, images and links unchanged.')
