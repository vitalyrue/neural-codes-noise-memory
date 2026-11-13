"""Integrate the writers' page decisions; do not create semantic acceptance.

Every page must have a disposition. Reviewer reports separately judge whether
the actual passages teach what the map claims.
"""
from pathlib import Path
import csv,re,json,datetime
ROOT=Path(__file__).resolve().parents[1]
inventory=list(csv.DictReader((ROOT/"source-maps/source-inventory.csv").open(encoding="utf-8-sig",newline="")))
decisions={}
for writer in ["memory","eye","place"]:
    path=ROOT/f"verification/writers/{writer}-evidence.md"
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| P"):continue
        cells=[x.strip() for x in line.strip().strip("|").split("|")]
        key=cells[0]
        if not re.fullmatch(r"P[123](?:SI)?-p\d{2}",key):continue
        raw=" | ".join(cells[1:])
        status=re.search(r"\b(covered|intentional-consolidation|intentional-omission|duplicate)\b",raw)
        if not status:raise ValueError(f"No disposition: {line}")
        locations=list(dict.fromkeys(re.findall(r"(?:sec|ch):[A-Z0-9-]+",raw)))
        default={"memory":"ch:MEMORY-DYNAMICS","eye":"ch:EYE-DRIFT","place":"ch:PLACE-FIELDS"}[writer]
        decisions[key]={"disposition":status[1],"guide_locus":"; ".join(locations or [default]),"rationale":raw,"writer_evidence":str(path.relative_to(ROOT)).replace("\\","/")}

review_pages={12:("sec:EYE-LIMITS","Alternative upstream inputs and source versus mechanism"),13:("sec:EYE-LIMITS","Alternative upstream inputs and source versus mechanism"),19:("sec:EYE-RECORDINGS; sec:EYE-SHARED-VARIANCE","Motor neurons were recorded individually"),20:("sec:EYE-MEASUREMENT-NOISE","Noise-floor uncertainty and raw trajectory treatment"),21:("sec:EYE-MEASUREMENT-NOISE","Noise-floor uncertainty and raw trajectory treatment"),23:("sec:EYE-SCALING","Parameter tuning and the normalization ambiguity"),34:("sec:EYE-SHARED-VARIANCE; sec:EYE-LIMITS","Single-motor-neuron readout versus behavior, not simultaneous neuron pairs")}
for index in range(1,36):
    key=f"P2REV-p{index:02d}"
    if index in review_pages:
        locus,rationale=review_pages[index]
        decisions[key]={"disposition":"covered","guide_locus":locus,"rationale":rationale+". Selected reviewed passages only; no claim that every reply on the page is taught.","writer_evidence":"verification/writers/eye-evidence.md"}
    else:
        decisions[key]={"disposition":"intentional-omission","guide_locus":"sec:EYE-LIMITS","rationale":"Reviewer/reply history, repeated or secondary analyses, formatting exchanges, or acceptance reply not required for the guide's derivations. Only selected review passages are used; the final article and supplement govern the taught results.","writer_evidence":"verification/writers/eye-evidence.md"}
decisions["P2FORM-p01"]={"disposition":"intentional-omission","guide_locus":"sec:READING-SCOPE","rationale":"Reporting-summary form is nonteaching reporting metadata. XFA contents are unavailable to the local reader; no guide claim depends on them.","writer_evidence":"verification/writers/eye-evidence.md"}
decisions["P3SI-p16"]["rationale"]="Supplemental bibliography consolidated into the article/supplement citations and accessible Taylor source. Adler is cited in the SI; Nosko is main-article reference 32. The full Adler/Nosko theorem proofs were not independently read or claimed as reproduced."

rows=[]
for inv in inventory:
    key=inv["source_unit_id"]
    if key not in decisions:raise ValueError(f"Missing writer decision: {key}")
    d=decisions[key]
    rows.append({"source_unit_id":key,"source_id":inv["source_id"],"source_path":inv["source_path"],"source_sha256":inv["source_sha256"],"unit_locator":inv["unit_locator"],"presentation_order":inv["presentation_order"],**d,"duplicate_of":"","review_status":"pending-independent-guide-review"})
unknown=set(decisions)-{r['source_unit_id'] for r in inventory}
if unknown:raise ValueError(f"Unknown units: {unknown}")
with (ROOT/"source-maps/source-coverage.csv").open("w",encoding="utf-8",newline="") as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
counts={}
for r in rows:counts[r['disposition']]=counts.get(r['disposition'],0)+1
report={"prepared_at":datetime.datetime.now().astimezone().isoformat(),"inventory_pages":len(inventory),"coverage_rows":len(rows),"dispositions":counts,"semantic_acceptance":"pending; these are writer decisions, not reviewer verdicts"}
(ROOT/"verification/checks/source-coverage-integration.json").write_text(json.dumps(report,indent=2),encoding="utf-8")
print(json.dumps(report,indent=2))
