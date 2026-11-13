"""Scoped post-build HTML/source-preservation checks for the nine additions.

Run after root rebuilds the local guide. This writes only post-build-check.json.
No browser runs, book edits, semantic acceptance, or whole-book checks occur.
"""
from pathlib import Path
from datetime import datetime
from urllib.parse import unquote, urlsplit, parse_qs
import copy
import hashlib
import json
import re

from bs4 import BeautifulSoup
import fitz
import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
ROOT_START = datetime.fromisoformat('2026-10-24T18:31:14.999410+03:00')
EXPECTED_COUNTS = {'ch:FOUNDATIONS':4, 'ch:MEMORY-INFORMATION':4,
                   'ch:EYE-DRIFT':4, 'ch:PLACE-FIELDS':5, 'ch:SYNTHESIS':1}
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
normalize = lambda text: ' '.join(text.replace('\xa0', ' ').split())


def check():
    started = datetime.now().astimezone()
    rows = json.loads((HERE/'integration.json').read_text(encoding='utf-8'))
    insertions = json.loads((HERE/'insertions.json').read_text(encoding='utf-8'))
    if len(rows) != 9 or len({r['id'] for r in rows}) != 9:
        raise ValueError('Expected nine distinct rows in integration.json.')
    chapters = sorted({r['chapter'] for r in rows})
    if len(chapters) != 5:
        raise ValueError('Expected five changed chapters.')
    new_ids = {r['visual_id'] for r in rows}
    pages, figures, pdf_links, preservation = [], [], [], []
    for chapter in chapters:
        group = [r for r in rows if r['chapter'] == chapter]
        meta = yaml.safe_load((ROOT/Path(chapter).with_suffix('.yaml')).read_text(encoding='utf-8'))
        chapter_id = meta['chapter_id']
        html = ROOT/'site/chapters'/(chapter_id.replace(':','-').lower()+'.html')
        text = html.read_text(encoding='utf-8')
        soup = BeautifulSoup(text, 'html.parser')
        main = soup.select_one('main')
        if main is None:
            raise ValueError('Missing main element: '+str(html))
        main_text = main.get_text(' ', strip=True)
        page = {'chapter':chapter, 'html':str(html.relative_to(ROOT)).replace('\\','/'),
                'main_figure_count':len(main.select('figure img')),
                'expected_main_figures':EXPECTED_COUNTS[chapter_id],
                'literal_markdown_image':'![' in main_text,
                'unresolved_block':'{{block:' in main_text or '{{block:' in str(main),
                'static_math_errors':len(main.select('mjx-merror,.MathJax_Error'))}
        page['status'] = 'pass' if page['main_figure_count'] == page['expected_main_figures'] and not (
            page['literal_markdown_image'] or page['unresolved_block'] or page['static_math_errors']) else 'fail'
        pages.append(page)
        for row in group:
            stem = Path(row['asset']).stem
            hits = [img for img in main.select('figure img')
                    if Path(unquote(urlsplit(img.get('src','')).path)).name in {stem+'.png','fig-'+stem+'.png'}]
            img = hits[0] if hits else None
            caption = img.find_parent('figure').find('figcaption') if img else None
            asset_path = (html.parent/unquote(urlsplit(img['src']).path)).resolve() if img else None
            blocks = [b for b in meta.get('blocks',[]) if b.get('id') == row['visual_id']]
            figure = {'id':row['id'], 'matches':len(hits), 'alt_matches':img is not None and img.get('alt') == row['alt'],
                      'caption_present':caption is not None and bool(caption.get_text(strip=True)),
                      'asset_exists':asset_path is not None and asset_path.exists(),
                      'built_asset_matches_approved':asset_path is not None and asset_path.exists() and sha(asset_path) == sha(ROOT/row['asset']),
                      'sidecar_caption_alt_match':len(blocks)==1 and blocks[0].get('caption') == row['caption'] and blocks[0].get('alt') == row['alt']}
            figure['status'] = 'pass' if figure['matches']==1 and all(figure[k] for k in [
                'alt_matches','caption_present','asset_exists','built_asset_matches_approved','sidecar_caption_alt_match']) else 'fail'
            figures.append(figure)

            if row.get('html_source_link'):
                expected = urlsplit(row['html_source_link'])
                expected_page = int(parse_qs(expected.fragment)['page'][0])
                label = normalize(row['source_link_label'])
                matches = [a for a in main.select('a[href]') if normalize(a.get_text(' ',strip=True)) == label]
                link = {'id':row['id'],'label':row['source_link_label'],'label_matches':len(matches),
                        'expected_page':expected_page,'status':'fail'}
                if len(matches)==1:
                    actual = urlsplit(matches[0]['href'])
                    actual_pages = parse_qs(actual.fragment).get('page',[])
                    pdf_path = (html.parent/unquote(actual.path)).resolve()
                    link.update(href=matches[0]['href'],target=str(pdf_path),
                                path_matches=unquote(actual.path)==unquote(expected.path),
                                page_matches=actual_pages==[str(expected_page)],exists=pdf_path.exists())
                    if pdf_path.exists():
                        link['pdf_signature_valid'] = pdf_path.read_bytes()[:5] == b'%PDF-'
                        try:
                            with fitz.open(pdf_path) as document:
                                link['pdf_pages'] = len(document)
                                link['page_in_range'] = 1 <= expected_page <= len(document)
                                link['page_readable'] = bool(document[expected_page-1].get_text().strip()) if link['page_in_range'] else False
                        except Exception as error:
                            link['pdf_error'] = str(error)
                        link['status'] = 'pass' if all(link.get(k,False) for k in [
                            'path_matches','page_matches','exists','pdf_signature_valid','page_in_range','page_readable']) else 'fail'
                pdf_links.append(link)

        current = (ROOT/chapter).read_text(encoding='utf-8')
        baseline = (HERE/'baseline'/chapter).read_text(encoding='utf-8')
        restored = current
        replacements = []
        for addition in reversed([x for x in insertions if x['chapter']==chapter]):
            count = restored.count(addition['after'])
            replacements.append({'id':addition['id'],'replacement_occurrences':count})
            if count==1:
                restored = restored.replace(addition['after'],addition['before'],1)
        old_meta = yaml.safe_load((HERE/'baseline'/Path(chapter).with_suffix('.yaml')).read_text(encoding='utf-8'))
        restored_meta = copy.deepcopy(meta)
        restored_meta['blocks'] = [b for b in restored_meta.get('blocks',[]) if b.get('id') not in new_ids]
        heading = lambda source: re.findall(r'^#{1,6}\s+.*$',source,re.MULTILINE)
        preserve = {'chapter':chapter,'replacements':replacements,
                    'exact_original_text_recovers':restored == baseline,
                    'original_headings_unchanged':heading(current)==heading(baseline),
                    'old_sidecar_content_unchanged':restored_meta == old_meta,
                    'old_sidecar_blocks_unchanged':restored_meta.get('blocks',[])==old_meta.get('blocks',[])}
        preserve['status'] = 'pass' if all(preserve[k] for k in ['exact_original_text_recovers','original_headings_unchanged',
            'old_sidecar_content_unchanged','old_sidecar_blocks_unchanged']) and all(x['replacement_occurrences']==1 for x in replacements) else 'fail'
        preservation.append(preserve)

    untouched = 'content/chapters/02-memory-dynamics'
    chapter2 = {'chapter':'ch:MEMORY-DYNAMICS',
                'markdown_unchanged':sha(ROOT/(untouched+'.md'))==sha(HERE/'baseline'/(untouched+'.md')),
                'sidecar_unchanged':sha(ROOT/(untouched+'.yaml'))==sha(HERE/'baseline'/(untouched+'.yaml'))}
    chapter2_soup = BeautifulSoup((ROOT/'site/chapters/ch-memory-dynamics.html').read_text(encoding='utf-8'),'html.parser')
    chapter2['main_figures'] = len(chapter2_soup.select('main figure img'))
    chapter2['status'] = 'pass' if chapter2['markdown_unchanged'] and chapter2['sidecar_unchanged'] and chapter2['main_figures']==4 else 'fail'
    finished = datetime.now().astimezone()
    report = {'started_at':started.isoformat(),'finished_at':finished.isoformat(),'root_start':ROOT_START.isoformat(),
              'root_wall_elapsed_seconds':(finished-ROOT_START).total_seconds(),'awake_execution_time':'unverified',
              'scope':'Five changed chapter HTML files, nine new images, eight new PDF source links, exact text/sidecar preservation, unchanged Chapter 2 count. No semantic or whole-book audit.',
              'pages':pages,'figures':figures,'pdf_links':pdf_links,'preservation':preservation,'chapter2':chapter2}
    report['status'] = 'pass' if len(figures)==9 and len(pdf_links)==8 and all(
        x['status']=='pass' for x in pages+figures+pdf_links+preservation+[chapter2]) else 'fail'
    (HERE/'post-build-check.json').write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding='utf-8')
    print(json.dumps({'status':report['status'],'pages':len(pages),'figures':len(figures),'pdf_links':len(pdf_links),
                      'failures':[x for x in pages+figures+pdf_links+preservation+[chapter2] if x['status']!='pass']},indent=2,ensure_ascii=False))
    return 0 if report['status']=='pass' else 1


if __name__ == '__main__':
    raise SystemExit(check())
