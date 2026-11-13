"""Verify changed headings, retained objects, and explicit fold markup."""
from pathlib import Path
from datetime import datetime
from collections import Counter
from urllib.parse import urlsplit,unquote
import hashlib,json,re
from bs4 import BeautifulSoup

OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[1]
read=lambda p:p.read_text(encoding='utf-8')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
expected=json.loads(read(OUT/'render-expectations.json'))
integration=json.loads(read(OUT/'integration.json'))
rows=[]
for page in expected['pages']:
    path=ROOT/'site'/page['url']
    soup=BeautifulSoup(read(path),'html.parser')
    main=soup.select_one('main')
    source=next(r for r in integration['records'] if r['headings'][0]['id']==page['chapter'])
    old_source=read(OUT/'baseline'/source['path'])
    before_links=Counter(re.findall(r'\]\(([^)]+)\)',old_source))
    actual_links=Counter(a['href'] for a in soup.select('a[href]'))
    expected_heading_ids=[h['id'].lower().replace(':','-') for h in source['headings'][1:]]
    missing_ids=[key for key in expected_heading_ids if not main.find(id=key)]
    anchors_missing=[link for link in before_links if not actual_links[link] and not link.startswith('#')]
    # Quarto may add cross-reference link markup; original explicit links retain href.
    folds=main.select('.publisher-clarification-note.publisher-fold-always')
    notes=[]
    for n in folds:
        notes.append({'title':n.find('p').get_text(' ',strip=True),
                      'first_definitions':len(n.select('.definition-term')),
                      'figures':len(n.select('figure img')),
                      'headings':len(n.select('h1,h2,h3,h4,h5,h6'))})
    images=[]
    for img in main.select('figure img'):
        target=(path.parent/unquote(urlsplit(img['src']).path)).resolve()
        images.append({'src':img['src'],'exists':target.is_file(),
                       'alt_nonempty':bool(img.get('alt','').strip())})
    row={'chapter':page['chapter'],'missing_stable_section_ids':missing_ids,
         'missing_original_links':anchors_missing,'folds':notes,'figures':images,
         'expected_folds':page['folds'],'expected_figures':page['figures'],
         'tables':len(main.select('table')),'expected_tables':page['tables'],
         'unresolved_block':'{{block:' in main.get_text(),
         'source_bytes_match_reviewed_proposal':sha(ROOT/source['path'])==source['after_sha256'],
         'source_text_matches_reviewed_proposal':read(ROOT/source['path'])==read(OUT/'proposed'/source['path']),
         'source_format_note':'Integration normalizes Windows CRLF to LF; reader text must remain exactly equal after newline decoding.'}
    row['status']='pass' if (not missing_ids and not anchors_missing
       and [n['title'] for n in notes]==page['folds']
       and all(not n['first_definitions'] and not n['figures'] and not n['headings'] for n in notes)
       and len(images)==page['figures'] and all(i['exists'] and i['alt_nonempty'] for i in images)
       and row['tables']==page['tables'] and not row['unresolved_block']
       and row['source_text_matches_reviewed_proposal']) else 'fail'
    rows.append(row)
baseline=json.loads(read(OUT/'baseline/hashes.json'))
assets_preserved=all(sha(ROOT/p)==h for p,h in baseline['approved_assets'].items())
report={'at':datetime.now().astimezone().isoformat(),'pages':rows,'approved_assets_unchanged':assets_preserved,
        'approved_asset_count':len(baseline['approved_assets']),
        'status':'pass' if assets_preserved and all(r['status']=='pass' for r in rows) else 'fail'}
(OUT/'post-build-check.json').write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding='utf-8')
print(json.dumps({'status':report['status'],'pages':len(rows),'folds':sum(len(r['folds']) for r in rows),
                  'figures':sum(len(r['figures']) for r in rows),'failures':[r for r in rows if r['status']!='pass']},indent=2))
raise SystemExit(0 if report['status']=='pass' else 1)
