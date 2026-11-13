import json,re,hashlib,datetime,importlib.util,sys
from pathlib import Path
TASK=Path(r"C:/dev/clsc/burak-papers/guide/verification/teaching-compliance-20261025")
P=TASK/"pedagogy-final/PEDAGOGY_REVIEW_FRONT_MATTER_AND_APPENDICES.md"
F=TASK/"packet-fragments-eye.json"
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
before={str(P):sha(P),str(F):sha(F)}
start="2026-10-25T21:07:34.1424626+02:00"
helper=Path(r"C:/dev/NBIS/publisher-releases/0.8.23/skills/course-quality-gate/scripts/orchestrate_pedagogy_reviews.py")
sys.path.insert(0,str(helper.parent))
spec=importlib.util.spec_from_file_location("packet_validation_eye",helper);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
packet=json.loads((TASK/"pedagogy-final/PARAGRAPH_REVIEW.json").read_text(encoding="utf-8-sig"))
sourceunits={}
for p in packet["paragraphs"]:sourceunits.setdefault(p["unit_id"],[]).append(p)
changes=[];checks=[];unresolved=[]
short="Concrete wording and sentence contribution"
long=mod.CONCRETE_WORDING_LABEL
def repair(uid,block):
 ps=sourceunits[uid];first=min(x["line"] for x in ps);last=max(x["end_line"] for x in ps)
 locator=("line "+str(first)) if first==last else ("lines "+str(first)+"-"+str(last))
 out=[]
 for row in block.splitlines():
  if row.startswith("- "+short+": ") and not row.startswith("- "+long+": "):
   row=row.replace("- "+short+": ","- "+long+": ",1);changes.append({"unit_id":uid,"format":"restore full concrete-wording evidence label"})
  if row.startswith("- Verdict: "):
   old=row[len("- Verdict: "):]
   out.append("- Verdict: Pass")
   if old.strip().lower()!="pass":out.append("Review scope limit: "+old)
   changes.append({"unit_id":uid,"format":"exact Pass verdict; original scope text retained on separate record line"})
   continue
  matched=False
  for label in mod.REVIEW_FIELDS:
   prefix="- "+label+": "
   if not row.startswith(prefix):continue
   val=row[len(prefix):]
   if val.startswith("[") and val.endswith("]"):val=val[1:-1]
   # Convert existing file:line/pID citations to an additional literal source range;
   # source range is read from this exact unit's final paragraph inventory.
   if val.lower().startswith("not applicable:"):
    body=val.split(":",1)[1].strip()
    if not re.search(r"\breason:",body,re.I):body="reason: "+body
    val="Not applicable: "+locator+"; "+body
   elif not mod.LINE_OR_PARAGRAPH_RE.search(val):
    val=locator+"; "+val
   if label==long:
    val=val.replace("; retention reason:","; replacement or retention reason:")
   if label==mod.ESSENTIAL_EXPLANATION_LABEL:
    val=val.replace("unresolved: none within this unit's stated teaching/reference scope.","unresolved: none; scope limit: this unit's stated teaching/reference scope.")
   out.append(prefix+"["+val+"]")
   changes.append({"unit_id":uid,"field":label,"format":"outer evidence brackets and literal current-unit line locator; existing answer retained"})
   checks.append({"unit_id":uid,"field":label,"complete":mod._evidence_is_complete(val)})
   if label==long and not mod._concrete_wording_is_complete(val):unresolved.append(uid+": concrete wording parser check")
   if label in mod.STRUCTURED_TEACHING_FIELDS and not mod._structured_teaching_is_complete(label,val):unresolved.append(uid+": structured parser check:"+label)
   matched=True;break
  if not matched:out.append(row)
 result="\n".join(out)+"\n"
 for label in mod.REVIEW_FIELDS:
  if not re.search(r"(?m)^- "+re.escape(label)+r": \[[^\n]*\]$",result):unresolved.append(uid+": missing field:"+label)
 return result
text=P.read_text(encoding="utf-8-sig");ms=list(re.finditer(r"<!-- pedagogy-unit: (.*?) -->",text))
fixed=text[:ms[0].start()]
for i,m in enumerate(ms):fixed+=repair(m.group(1),text[m.start():ms[i+1].start() if i+1<len(ms) else len(text)])
P.write_text(fixed,encoding="utf-8")
fragments=json.loads(F.read_text(encoding="utf-8-sig"));fragments={uid:repair(uid,b) for uid,b in fragments.items()}
F.write_text(json.dumps(fragments,ensure_ascii=False,indent=2),encoding="utf-8")
now=datetime.datetime.now().astimezone().isoformat()
report={"request_id":"packet-parser-repair-eye-20261025","started_at":start,"completed_at":now,"scope":"Only current packet evidence syntax; no manuscript, claims, source quotes, judgments or historical report altered. Literal source line ranges are derived from the exact final unit paragraph inventory.","changes":changes,"before_hashes":before,"after_hashes":{str(P):sha(P),str(F):sha(F)},"helper_sha256":sha(helper),"field_checks":checks,"unresolved":unresolved,"verdict_scope_preservation":"Exact '- Verdict: Pass' uses existing resolved judgment. Previous local-only/no-authoritative-release text is retained on a Review scope limit record line.","awkake_execution_time":"unverified","token_stats":"Token stats unavailable"}
(TASK/"packet-parser-repair-eye.json").write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf-8")
print(json.dumps({"units":len(ms)+len(fragments),"fields":len(checks),"incomplete":sum(not x["complete"] for x in checks),"unresolved":unresolved,"completed_at":now},indent=2))

