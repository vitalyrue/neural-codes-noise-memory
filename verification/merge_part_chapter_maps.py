"""Use an authored, linked contribution map as the Part's single chapter list.

The pinned renderer appends a second list from chapter-purpose metadata. Preserve
its heading/bookmark while replacing that repeat with the authored map. Keep all
unrelated HTML bytes intact. This runs from the project's normal asset publisher.
"""
import re
from html.parser import HTMLParser

AUTHORED = re.compile(r'<div class="part-chapter-map">\s*(<ul>.*?</ul>)\s*</div>', re.S)
GENERATED = re.compile(r'<section id="chapters-in-this-part" class="level2 unnumbered">\s*(<h2\b[^>]*>.*?</h2>)\s*(<ul>.*?</ul>)\s*</section>', re.S)
MERGED = re.compile(r'<section id="chapters-in-this-part" class="level2 unnumbered part-chapter-map-merged">\s*<h2\b[^>]*>.*?</h2>\s*(<ul>.*?</ul>)\s*</section>', re.S)

class ChapterLinks(HTMLParser):
    def __init__(self):
        super().__init__(); self.links=[]; self.items=0
    def handle_starttag(self,tag,attrs):
        if tag=='li':self.items+=1
        if tag=='a':
            href=dict(attrs).get('href','')
            if href.startswith('../chapters/') and href.endswith('.html'):
                self.links.append(href)

def check_links(markup,expected):
    parser=ChapterLinks();parser.feed(markup)
    if parser.links != list(expected) or parser.items != len(expected):
        raise ValueError('Part chapter map has missing, repeated, or out-of-order chapter links')

def merge_part_chapter_map(markup,expected):
    authored=list(AUTHORED.finditer(markup));generated=list(GENERATED.finditer(markup))
    merged=list(MERGED.finditer(markup))
    if len(merged)==1 and not authored and not generated:
        check_links(merged[0][1],expected)
        return markup,False
    if len(authored)!=1 or len(generated)!=1 or merged:
        raise ValueError('Expected one authored map and one generated chapter list')
    a,g=authored[0],generated[0]
    check_links(a[1],expected);check_links(g[2],expected)
    replacement='<section id="chapters-in-this-part" class="level2 unnumbered part-chapter-map-merged">\n'+g[1]+'\n'+a[1]+'\n</section>'
    for start,end,text in sorted([(a.start(),a.end(),replacement),(g.start(),g.end(),'')],reverse=True):
        markup=markup[:start]+text+markup[end:]
    return markup,True
