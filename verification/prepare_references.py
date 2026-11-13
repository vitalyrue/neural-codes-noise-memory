"""Resolve DOI metadata and write the book's deduplicated reference appendix.

Crossref supplies bibliographic metadata only. Source claim checks remain in
the research and reviewer records, rather than being inferred from this lookup.
"""
from pathlib import Path
import concurrent.futures,datetime,html,json,re,urllib.request,urllib.parse
ROOT=Path(__file__).resolve().parents[1]
cache=ROOT/"references/bibliography/crossref"
cache.mkdir(parents=True,exist_ok=True)
source_order=[]
notes_url="https://nischmainali.github.io/blog/gp-code-notes/"
doi_pattern=r"https?://(?:dx\.)?doi\.org/([^\s)<>\]]+)"
def add_urls(text):
    events=[]
    for match in re.finditer(doi_pattern,text):
        events.append((match.start(),urllib.parse.unquote(match[1]).rstrip(".,;\"'")))
    if notes_url in text:events.append((text.index(notes_url),notes_url))
    for _,key in sorted(events):
        if key.lower() not in [x.lower() for x in source_order]:source_order.append(key)
for p in sorted((ROOT/"content/chapters").glob("*.md")):
    if p.stem in ["references","introduction"]:continue
    text=p.read_text(encoding="utf-8")
    definitions=dict(re.findall(r"^\[\^([^]]+)\]:\s*(.*)$",text,re.M))
    body="\n".join(line for line in text.splitlines() if not re.match(r"^\[\^[^]]+\]:",line))
    token_pattern=r"\[\^([^]]+)\]|"+doi_pattern+"|"+re.escape(notes_url)
    for match in re.finditer(token_pattern,body):
        if match[1]:add_urls(definitions.get(match[1],""))
        else:add_urls(match[0])
dois=[key for key in source_order if key!=notes_url]

def fetch(doi):
    file=cache/(re.sub(r"[^a-zA-Z0-9.-]","_",doi)+".json")
    if file.exists():return doi,json.loads(file.read_text(encoding="utf-8"))
    url="https://api.crossref.org/works/"+urllib.parse.quote(doi,safe="")
    req=urllib.request.Request(url,headers={"User-Agent":"LocalTeachingGuide/1.0 (bibliographic metadata lookup)"})
    try:
        with urllib.request.urlopen(req,timeout=25) as r:data=json.load(r)["message"]
    except urllib.error.HTTPError as exc:
        if doi.lower()!="10.1073/pnas.1117386109" or exc.code!=429:raise
        # Bibliographic fields checked directly in the saved primary PDF.
        data={"DOI":doi,"author":[{"given":"Yoram","family":"Burak"},{"given":"Ila R.","family":"Fiete"}],
              "published":{"date-parts":[[2012,10,23]]},
              "title":["Fundamental limits on persistent activity in networks of noisy neurons"],
              "container-title":["Proceedings of the National Academy of Sciences"],
              "volume":"109","issue":"43","page":"17645-17650",
              "guide_metadata_source":"Saved primary paper PDF; Crossref endpoint returned429"}
    file.write_text(json.dumps(data,indent=2,ensure_ascii=False),encoding="utf-8")
    return doi,data

resolved={};failures=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    futures={pool.submit(fetch,d):d for d in dois}
    for future in concurrent.futures.as_completed(futures):
        d=futures[future]
        try:doi,data=future.result();resolved[doi]=data
        except Exception as exc:failures.append({"doi":d,"error":str(exc)})
if failures:
    (ROOT/"verification/checks/reference-lookup-errors.json").write_text(json.dumps(failures,indent=2),encoding="utf-8")
    raise RuntimeError(f"{len(failures)} DOI metadata lookups failed: {failures}")

def plain(x):return html.unescape(re.sub(r"<[^>]+>","",x))
def author(a):
    family=a.get("family") or a.get("name","")
    given=a.get("given","")
    initials=" ".join(word[0]+"." for word in re.split(r"[\s-]+",given) if word)
    return family+(", "+initials if initials else "")
lines=["# References {#ch:REFERENCES}","",
"Entries follow their first use in the reading path and chapters. The paper's supporting information shares its main article entry. The author's mathematical notes are listed separately because the guide also uses them for the excursion derivation.",""]
records=[]
for n,doi in enumerate(source_order,1):
    if doi==notes_url:
        lines.extend([f"{n}. Mainali, N. (2026, August 6). *Mathematical properties of Gaussian process neural code: Excursion geometry, spectral structure, and coding error*. [Author's mathematical notes]({notes_url}).",""])
        continue
    m=resolved[doi];authors=m.get("author",[])
    names="; ".join(author(a) for a in authors)
    if not names:names=m.get("publisher","")
    date=(m.get("published") or m.get("issued") or {}).get("date-parts",[[None]])[0]
    year=date[0] or "n.d."
    title=plain((m.get("title") or [doi])[0]).rstrip(".")
    venue=plain((m.get("container-title") or [m.get("publisher","")])[0])
    details=venue
    if m.get("volume"):details+=", "+str(m["volume"])
    if m.get("issue"):details+="("+str(m["issue"])+")"
    if m.get("page"):details+=", "+str(m["page"]).replace("-","–")
    elif m.get("article-number"):details+=", "+str(m["article-number"])
    lines.append(f"{n}. {names} ({year}). *{title}*. {details}. [DOI](https://doi.org/{doi}).")
    lines.append("")
    records.append({"number":n,"doi":doi,"title":title,"year":year,"authors":names,"metadata_source":m.get("guide_metadata_source","Crossref API"),"metadata_checked_at":datetime.datetime.now().astimezone().isoformat()})

(ROOT/"content/chapters/references.md").write_text("\n".join(lines),encoding="utf-8")
(ROOT/"references/bibliography/reference-register.json").write_text(json.dumps(records,indent=2,ensure_ascii=False),encoding="utf-8")
print(json.dumps({"unique_dois":len(dois),"additional_author_notes":1,"failures":failures},indent=2))
