from pathlib import Path
from urllib.parse import urlsplit,unquote
from bs4 import BeautifulSoup
import json,yaml,datetime
root=Path(__file__).resolve().parents[2]; out=Path(__file__).resolve().parent
source=json.loads((out/'source-checks.json').read_text())
report={'checked_at':datetime.datetime.now().astimezone().isoformat(),'pages':{},'errors':[]}
cache={}
for name in source['chapters']:
    y=yaml.safe_load((root/'content/chapters'/name.replace('.md','.yaml')).read_text(encoding='utf-8'))
    page=root/'site/chapters'/(y['chapter_id'].replace(':','-').lower()+'.html')
    markup=page.read_text(encoding='utf-8'); soup=BeautifulSoup(markup,'html.parser'); main=soup.select_one('main')
    assert main is not None,page
    errors=[]; ids=[x['id'] for x in soup.select('[id]')]
    if len(ids)!=len(set(ids)): errors.append('duplicate ids')
    if main.select('.katex-error, merror'): errors.append('math error')
    if '{{block:' in main.get_text(): errors.append('unexpanded block')
    if '::: For' in main.get_text(): errors.append('malformed closing fence')
    for a in main.select('a[href]'):
        u=urlsplit(a['href'])
        if u.scheme or u.netloc: continue
        target=(page.parent/unquote(u.path)).resolve() if u.path else page
        if not target.exists(): errors.append('missing file '+a['href']); continue
        if u.fragment and target.suffix=='.html':
            if target not in cache: cache[target]=BeautifulSoup(target.read_text(encoding='utf-8'),'html.parser')
            if not cache[target].find(id=unquote(u.fragment)):errors.append('missing anchor '+a['href'])
    for img in main.select('img[src]'):
        u=urlsplit(img['src'])
        if not u.scheme and not (page.parent/unquote(u.path)).resolve().exists():errors.append('missing image '+img['src'])
    report['pages'][page.name]={'internal_links':len(main.select('a[href]')),'figures':len(main.select('figure')),'formal_fold_sources':len(main.select('.publisher-clarification-note.publisher-fold-always')),'errors':errors}
    report['errors'].extend([page.name+': '+e for e in errors])
report['status']='passed' if not report['errors'] else 'failed'
(out/'html-checks.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps({'status':report['status'],'pages':len(report['pages']),'errors':report['errors']},indent=2))
assert not report['errors']
