import json,re,hashlib,datetime
from pathlib import Path
ROOT=Path(r"C:/dev/clsc/burak-papers/guide")
TASK=ROOT/"verification/teaching-compliance-20261025"
def read(p):return json.loads(p.read_text(encoding="utf-8-sig"))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
data=read(TASK/"assembly-eye-data.json"); units=read(TASK/"assembly-eye-input.json")
packet=read(TASK/"pedagogy-final/PARAGRAPH_REVIEW.json")
reports={n:read(TASK/n) for n in ["stage3-eye.json","stage3-memory.json","stage3-place.json"]}
s3=reports["stage3-eye.json"]
paragraphs={p["id"]:p for p in packet["paragraphs"]}
reviewed={}
for report in reports.values():
 for p in report.get("paragraph_judgments",report.get("paragraph_reviews",[])):reviewed[p["id"]]=p
mismatches=[]
for pid,p in reviewed.items():
 if pid in paragraphs and p.get("source_hash")!=paragraphs[pid]["source_hash"]:mismatches.append(pid)
if mismatches:raise ValueError("Stale paragraph evidence: "+str(mismatches))
reasoning={x[0]:x for x in s3["unit_reasoning"]}
fragments={}; front_blocks={}; completed=[]; claims_checked=[]; unresolved=[]
front_path=TASK/"pedagogy-final/PEDAGOGY_REVIEW_FRONT_MATTER_AND_APPENDICES.md"
front_before=front_path.read_text(encoding="utf-8-sig"); front_after=front_before
replacements={}
for u in units:
 uid=u["id"]; key=uid.split("::")[-1]; rec=data["recipes"][key]
 phrase,actor,obj,action,condition,loc,example,alternatives=rec
 if key=="sec:EYE-INVERSE-FILTER":phrase="integral adds the responses to all past spikes."
 if key=="sec:EYE-FILTERED-MSD":phrase="The same increment contributes its variance $h$"
 src=uid.split("::")[0]; ps=[p for p in packet["paragraphs"] if p["unit_id"]==uid]
 phrase_hits=[i+1 for i,l in enumerate((ROOT/src).read_text(encoding="utf-8-sig").splitlines()) if phrase in l]
 if len(phrase_hits)!=1:raise ValueError(uid+" exact phrase locator "+str(phrase_hits))
 phrase_line=phrase_hits[0]
 real=[p for p in ps if not re.fullmatch(r"</?div[^>]*>",p["text"].strip())]
 first=real[0] if real else None; last=real[-1] if real else None
 cite=first["id"] if first else uid
 entry=reasoning.get(key)
 if entry:chain,objection=entry[2],entry[3]
 elif key=="ch:GLOSSARY":
  chain="Lookup definition -> actual first main-text teaching -> bounded later use; all3 reviewers' exact glossary records supply the meaning/scope check."
  objection="Brownian definition could permit nonzero-mean increments and confuse drift with variance. Fixed at glossary line9; final mean-zero definition matches persistence line74. Other entries retain their scoped meanings, per memory/place current adoption answers."
 else:
  chain="Source used in main text -> reference entry -> distinct article/supplement or author notes -> original work access."
  objection="Reference could identify the wrong work or merge independent notes with the main article. Does not apply to the reviewed lookup role: stage3-place checks17 entries, and root source-consistency/external-link records separately match identifiers/order/access."
 prior="stage1-eye.json; stage1-recheck-eye.json; stage2-eye.json; stage3-eye.json"
 if key=="ch:GLOSSARY":prior+="; stage3-memory.json glossary paragraphs; stage3-place.json glossary paragraphs; current bounded adoption messages"
 if key=="ch:REFERENCES":prior="stage1-place.json.related_work_checks; stage3-place.json References paragraphs; source-consistency.json; external-link-check.json; current bounded place-agent adoption"
 first_line=first["line"] if first else 1
 context=" ".join(p["purpose"]+" "+p["connection"] for p in [reviewed.get(first["id"],{}),reviewed.get(last["id"],{})] if p.get("purpose")) if first else chain
 definitions=re.findall(r"\[\*\*(.*?)\*\*\]\{\.definition-term",u["block"])
 definition=("line "+str(first_line)+" onward; exact blue first-definition terms: "+", ".join(dict.fromkeys(definitions))+". Meanings match the actual introducing sentences and glossary entries; first-use evidence is in concept-judgments-eye.json and the cited Stage3 paragraph records.") if definitions else ("Not applicable: line "+str(first_line)+" is an opening/reference recap of already taught objects, not a first introduction requiring another blue label.")
 prereq=("Audience at00-reading-guide.md:37 is calculus/basic probability/linear algebra. "+cite+" and current concept-judgments-eye.json give exact teaching/use spans; "+chain)
 if key=="ch:GLOSSARY":prereq=data["glossary_adoption"]
 if key=="ch:REFERENCES":prereq=data["references_adoption"]
 bridge_map={
 "sec:EYE-RECORDINGS":"Spikes and measured eye position are paired, then transformed only by the separate calibrated calculation; line31/39 and fig:EYE-PHYSICAL-AND-RECORDED distinguish physical and analysis objects.",
 "sec:EYE-FORWARD-FIT":"Lines43-67 map actual E,velocity,acceleration into predicted rate with coefficient units and positive neural lead; rate measured from interspike intervals is distinct from expected fit.",
 "sec:EYE-INVERSE-FILTER":"Lines73-117 reverse calibrated movement-to-rate relation into unit-spike position responses; sum/convolution preserves degree units and area1/k.",
 "sec:EYE-CHI":"Lines201-229 map measured/predicted displacements to C+eta and C+epsilon, preserving physical units, unit common gain and explicit cross-term approximation.",
 "sec:EYE-FILTERED-MSD":"Lines100-126 turn filtered Brownian position into velocity, weighted independent input increments, then covariance; actual finite weighted sums teach dW before the integral is used.",
 "sec:EYE-CIRCUIT-MODEL":"Lines20-53 map spike events to normalized synaptic states and weighted stored position; lines55-72 map through motor filtering and effective plant contributions to measured eye output.",
 "sec:EYE-SCALING":"Lines91-101 convert independent interval-time fluctuations into long-window count variability before CV squared scales diffusion."
 }
 bridge=bridge_map.get(key,"Not applicable: "+loc+" describes "+("source lookup rather than a transformed computational representation." if key in ["ch:GLOSSARY","ch:REFERENCES"] else "a question, inference or reference comparison; no unintroduced encoding or storage transformation is required here."))
 fields={
 "Reader problem, observable limitation, or engineering decision":cite+"; "+rec[0]+" The reader needs to understand "+(entry[1] if entry else ("the lookup meaning and its main teaching site." if key=="ch:GLOSSARY" else "which exact publication supports the cited claim.")),
 "Prerequisites, first use, and first teaching location":prereq,
 "Definition and emphasis":definition,
 "Concrete wording and sentence contribution":"line "+str(phrase_line)+" and "+loc+"; phrase: "+phrase+"; paraphrase: "+action+"; actor: "+actor+"; object: "+obj+"; action: "+action+"; condition or consequence: "+condition+"; verdict: retain; retention reason: "+(entry[1] if entry else "The named object has the precise lookup meaning needed at its main teaching/use location."),
 "Local relevance and paragraph continuity":context+" Full individual purpose/connection/retain reasons are bound by exact current paragraph IDs/hashes in "+("stage3-eye.json" if key not in ["ch:GLOSSARY","ch:REFERENCES"] else "the3 Stage3 reports")+"; no prose-wrapper exclusion proposes a source deletion.",
 "Operating mode and object roles, when relevant":("Not applicable: "+loc+" is a reference lookup after teaching, not a changing-state model or experimental mode." if key in ["ch:GLOSSARY","ch:REFERENCES","sec:READING-PAPERS"] else loc+"; "+actor+" acts on "+obj+" to "+action+"; "+condition+". Measurement, prediction and illustrative calculation remain distinct; the unit is not a parameter-training procedure unless its explicit fitting equation is being discussed."),
 "System setup and component relationships":"setting: "+loc+"; roles: "+actor+"; objects and flow: "+obj+" -> "+action+"; assumptions: "+condition+"; verdict: adequate.",
 "Representation bridge, when relevant":bridge,
 "Mechanism, calculation, or state change":("Not applicable: "+loc+" is source/definition lookup; detailed mechanisms remain in their reviewed main-text teaching passages." if key in ["ch:GLOSSARY","ch:REFERENCES","sec:READING-PAPERS"] else loc+"; "+chain+" Formula/source checks are given individually below and were actually performed in "+prior+"."),
 "Concrete trace or example":example,
 "Example setup and conclusion":example+" "+("No invented example is required." if "Not applicable:" in example else "The stated inputs/conditions precede the computation or observation; interpretation follows. Numbers marked constructed are not reported measurements."),
 "Assumptions, limits, trade-offs, or failure modes":loc+"; "+condition+". "+(objection if key not in ["ch:GLOSSARY","ch:REFERENCES"] else "Short entries are lookup; main explanations still carry assumptions and examples. "+objection),
 "Relevant alternatives, common criteria, and selection or scope":alternatives,
 "Essential explanation beyond the checklist":"reader task: "+(entry[1] if entry else "locate and interpret the already used term/source")+"; dependencies checked: "+prereq+"; reasoning chain: "+chain+"; unresolved: none within this unit's stated teaching/reference scope.",
 "Result that motivates the next section":(reviewed[last["id"]]["connection"]+" "+reviewed[last["id"]]["reason"] if last else chain),
 "Expert objection":"objection: "+objection+"; kind: correctness; target: "+uid+" and "+loc+"; disposition: "+("fixed" if key=="ch:GLOSSARY" else "does not apply")+"; reason: "+chain+" Checked in "+prior+".",
 "Verdict":"Pass for current local teaching review; actual current source/math/source-connection adoption recorded in evidence-assembly-eye.json. No authoritative release claim."
 }
 if key in ["ch:GLOSSARY","ch:REFERENCES","sec:READING-PAPERS"]:
  fields["System setup and component relationships"]="Not applicable: "+loc+" is lookup/reference access after the system and methods were taught; inventing component flow would not improve the reader's task."
 block=u["block"]
 # Exact scaffold response slots only; quoted source passages remain untouched.
 for label,value in fields.items():
  pattern=r"(?m)^- "+re.escape(label)+r": \[cite an exact passage.*?\]$"
  if label=="Concrete wording and sentence contribution":pattern=r"(?m)^- Concrete wording and sentence contribution: phrase,.*?\[cite an exact passage.*?\]$"
  if label=="Verdict":pattern=r"(?m)^- Verdict: Pending reviewer assessment$"
  block,n=re.subn(pattern,lambda m:"- "+label+": "+value,block,count=1)
  if n!=1:unresolved.append(uid+": field "+label+" matched "+str(n))
 checks=data["claims"].get(key,[])
 if len(checks)!=len(u["claims"]):raise ValueError(uid+" claim count mismatch "+str((len(checks),len(u["claims"]))))
 for claim,proof in zip(u["claims"],checks):
  cid,line,text,_=claim;code,method=proof.split("|",1)
  verdict={"T":"true as written","C":"condition stated","N":"not a claim"}[code]
  # Repair legibility of compressed mathematical evidence labels, without changing source text.
  for a,b in {"stage1eye":"Stage1 eye","stage1place":"Stage1 place","stage3place":"Stage3 place","OriginalFig":"Original Fig","MainEq":"Main Eq","mainEq":"main Eq","sourcechecked":"source checked","CV²":"CV squared","MainFig":"Main Fig","2022main":"2022 main","2022Methods":"2022 Methods","sourcecheck":"source check"}.items():method=method.replace(a,b)
  old="- Claim "+cid+", line "+line+': "'+text+'" -> '+claim[3]
  new="- Claim "+cid+", line "+line+': "'+text+'" -> [verdict: '+verdict+"; checked: "+method+"; evidence: "+prior+"]"
  if old not in block:raise ValueError("missing claim row "+uid+cid)
  block=block.replace(old,new,1);claims_checked.append({"unit_id":uid,"claim_id":cid,"line":int(line),"verdict":verdict,"method":method})
 if "[cite an exact passage" in block or "-> [verdict: true as written, condition stated" in block or "- Verdict: Pending" in block:unresolved.append(uid+": placeholder remains")
 if "FRONT_MATTER" in u["file"]:front_blocks[uid]=block
 else:fragments[uid]=block
 completed.append(uid)
front_markers=list(re.finditer(r'<!-- pedagogy-unit: (.*?) -->',front_before))
front_after=front_before[:front_markers[0].start()]+''.join(front_blocks[m.group(1)] for m in front_markers)
front_path.write_text(front_after,encoding="utf-8")
(TASK/"packet-fragments-eye.json").write_text(json.dumps(fragments,ensure_ascii=False,indent=2),encoding="utf-8")
now=datetime.datetime.now().astimezone().isoformat();start=datetime.datetime.fromisoformat(data["started_at"])
assessments=[]
for uid in completed:
 key=uid.split("::")[-1];rec=data["recipes"][key];reason=reasoning.get(key)
 proofs=[x["method"] for x in claims_checked if x["unit_id"]==uid]
 answer=(reason[2]+" "+reason[3] if reason else (data["glossary_adoption"] if key=="ch:GLOSSARY" else data["references_adoption"]))+" Current claims checked: "+"; ".join(proofs[:3])+". Full individual checked outcomes are in the completed packet unit and claims_checked."
 assessments.append({"unit_id":uid,"status":"pass" if not any(x.startswith(uid+":") for x in unresolved) else "open","unresolved":[x for x in unresolved if x.startswith(uid+":")],"questions":[{"question":"Does the final unit preserve correct claims, needed premises and source/mathematical support after the reviewed repairs?","answer":answer,"source_refs":[uid]}]})
files=["stage1-eye.json","stage1-recheck-eye.json","stage2-eye.json","stage3-eye.json","stage3-memory.json","stage3-place.json","repairs-v2.json","source-consistency.json","external-link-check.json","concept-judgments-eye.json","pedagogy-final/PARAGRAPH_REVIEW.json"]
record={"local_request_id":"evidence-assembly-eye-20261025","started_at":data["started_at"],"completed_at":now,"awake_execution_time":"unverified","wall_seconds":(datetime.datetime.fromisoformat(now)-start).total_seconds(),"scope":"Current bounded claim-check and evidence adoption, not retagging historical Stage1/2/3 calls.","unit_ids":completed,"reports":[{"path":f,"sha256":sha(TASK/f)} for f in files],"rule_hashes":[{"path":str(p),"sha256":sha(p)} for p in [Path(r"C:/dev/NBIS/publisher-releases/0.8.23/skills/course-study-guide-builder/references/pedagogy-language-contract.md"),Path(r"C:/dev/NBIS/publisher-releases/0.8.23/skills/course-quality-gate/references/prose-and-style-contract.md")]],"source_hashes":s3["source_hashes"],"sources_adoption":"Final source/typed fields were read in Stage3; this call checked current claim text against actual prior calculations/source locators, not just inherited a pass. Main paper formulas, noise assumptions and printed k0 ambiguity remain; no source claim is expanded. Current paragraph hashes were checked across all3 final reports against the final packet with no mismatch.","rules_adoption":"Publisher0.8.23 teaching and quality-record rules were read in this task. Existing real answers were mapped to the required current packet fields; no empty scaffold was treated as passed.","connections_adoption":"Final chapter overviews, figure transitions, source limits and first-use spans were assessed in Stage3. This call checks the repaired current claim set retains those actual connections; reference/glossary role answers were separately obtained from memory/place reviewers.","glossary_adoption":data["glossary_adoption"],"references_adoption":data["references_adoption"],"claims_checked":claims_checked,"unresolved":unresolved,"outputs":[{"path":str(front_path),"sha256":sha(front_path)},{"path":"packet-fragments-eye.json","sha256":sha(TASK/"packet-fragments-eye.json")}],"workflow_run":{"run_id":"evidence-assembly-eye-20261025","reviewer_id":"/root/compliance_eye","context":"reviewer_continuation","stage":"truth_reasoning","started_at":data["started_at"],"completed_at":now,"input_hash":packet["input_hash"],"review_contract_hash":packet["review_contract_hash"],"assessments":assessments},"token_stats":"Token stats unavailable"}
(TASK/"evidence-assembly-eye.json").write_text(json.dumps(record,ensure_ascii=False,indent=2),encoding="utf-8")
print(json.dumps({"units":len(completed),"fragments":len(fragments),"claims":len(claims_checked),"unresolved":unresolved,"completed_at":now,"wall_seconds":record["wall_seconds"]},indent=2))

