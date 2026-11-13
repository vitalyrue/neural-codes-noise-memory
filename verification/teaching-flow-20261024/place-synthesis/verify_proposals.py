from make_proposals import BASE,OUT,HERE,changes,sha
from pathlib import Path
from collections import Counter
import re,json,yaml
from datetime import datetime

checks=[]
for stem in ['05-place-fields','06-synthesis']:
    fn=stem+'.md'; old=(BASE/fn).read_text(encoding='utf-8'); new=(OUT/fn).read_text(encoding='utf-8')
    # A proof move can leave extra blank separators; no source unit changes.
    new=re.sub(r'\n{3,}','\n\n',new)
    (OUT/fn).write_text(new,encoding='utf-8',newline='\n')
    ids=lambda t:re.findall(r'\{#([^}]+)\}',t)
    assert ids(old)==ids(new),fn+' IDs or order'
    blocks=lambda t:re.findall(r'\{\{block:([^}]+)\}\}',t)
    assert blocks(old)==blocks(new),fn+' blocks or order'
    links=lambda t:re.findall(r'\]\(([^)]+)\)',t)
    assert Counter(links(old))==Counter(links(new)),fn+' links'
    assert re.findall(r'\[\*\*.*?definition-term[^\n]+',old)==re.findall(r'\[\*\*.*?definition-term[^\n]+',new),fn+' definitions'
    # Revert connection repairs and discard heading/fold markers before comparing
    # exact paragraph units as a multiset. This detects deleted or added prose/math.
    restored=new
    for c in reversed(changes):
        if c['file']==fn and c['kind']=='connection':
            assert restored.count(c['after'])==1
            restored=restored.replace(c['after'],c['before'],1)
    def units(t):
        t=re.sub(r'^#{1,6} .+\n?','',t,flags=re.M)
        t=re.sub(r'^:::[^\n]*\n?','',t,flags=re.M)
        return Counter(p.strip() for p in re.split(r'\n\s*\n',t) if p.strip())
    assert units(old)==units(restored),(fn,'source paragraph or math lost',list((units(old)-units(restored)).elements())[:2],list((units(restored)-units(old)).elements())[:2])
    fold_bodies=re.findall(r'^::: \{[^\n]+\}\n\n(.*?)\n\n:::',new,re.M|re.S)
    for body in fold_bodies:
        assert '{{block:' not in body and 'definition-term' not in body
        assert not re.search(r'^#{1,6} |^:::',body,re.M)
    yd=yaml.safe_load((OUT/(stem+'.yaml')).read_text(encoding='utf-8'))
    yo=yaml.safe_load((BASE/(stem+'.yaml')).read_text(encoding='utf-8'))
    assert yd['blocks']==yo['blocks']
    headings=dict((ident,title) for title,ident in re.findall(r'^#{1,6} (.+) \{#([^}]+)\}$',new,re.M))
    assert headings[yd['chapter_id']]==yd['title']
    for sec in yd['section_list']: assert headings[sec['id']]==sec['title']
    checks.append(dict(file=fn,before_sha256=sha(old),after_sha256=sha(new),section_ids='identical and in original order',block_references='identical and in original order',all_links='identical multiset',all_source_paragraphs_and_math='exactly retained after the individually logged connection repairs are reversed',definitions='identical and outside folds',yaml_blocks='identical',yaml_titles='match source',folds=len(fold_bodies)))

report=dict(timestamp=datetime.now().astimezone().isoformat(),checks=checks,limits=['No new empirical or mathematical claim was added. Existing findings are preserved, not independently reverified from every primary paper here.','This is an author preservation check; independent correctness, wording and reader-flow review remain pending.','No build or pixel sweep was run by this author.'])
(HERE/'preservation-checks.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(report,ensure_ascii=False,indent=2))
