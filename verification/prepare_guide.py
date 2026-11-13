"""Prepare Publisher metadata from the authored chapter files and saved papers.

This does not rewrite teaching prose or certify its coverage or correctness.
Run after chapter writers have frozen their files. Page-coverage decisions are
integrated separately from their evidence records.
"""
from pathlib import Path
import csv
import datetime
import hashlib
import json
import re
import shutil
import yaml
from pypdf import PdfReader

ROOT=Path(__file__).resolve().parents[1]
PARENT=ROOT.parent

CHAPTERS=[
    ("00-reading-guide","ch:READING-GUIDE","part:MECHANISMS","frontmatter",[]),
    ("01-foundations","ch:FOUNDATIONS","part:MECHANISMS","chapter",[]),
    ("02-memory-dynamics","ch:MEMORY-DYNAMICS","part:MECHANISMS","chapter",["ch:FOUNDATIONS"]),
    ("03-memory-information","ch:MEMORY-INFORMATION","part:MECHANISMS","chapter",["ch:FOUNDATIONS","ch:MEMORY-DYNAMICS"]),
    ("04-eye-drift","ch:EYE-DRIFT","part:OBSERVATIONS","chapter",["ch:FOUNDATIONS","ch:MEMORY-DYNAMICS","ch:MEMORY-INFORMATION"]),
    ("05-place-fields","ch:PLACE-FIELDS","part:OBSERVATIONS","chapter",["ch:FOUNDATIONS"]),
    ("06-synthesis","ch:SYNTHESIS","part:OBSERVATIONS","chapter",["ch:EYE-DRIFT","ch:PLACE-FIELDS"]),
    ("glossary","ch:GLOSSARY","part:OBSERVATIONS","appendix",[]),
    ("references","ch:REFERENCES","part:OBSERVATIONS","appendix",[]),
]

SOURCES=[
    ("P1","burak-fiete-2012-persistent-activity.pdf","Published paper, Early Edition layout"),
    ("P1SI","burak-fiete-2012-persistent-activity-si.pdf","Supporting text"),
    ("P2","ben-shushan-2022-fixational-drift.pdf","Published paper"),
    ("P2SI","ben-shushan-2022-supplement-1.pdf","Supplementary notes and figures"),
    ("P2REV","ben-shushan-2022-supplement-2.pdf","Open peer review"),
    ("P2FORM","ben-shushan-2022-supplement-5.pdf","Reporting summary; XFA contents unavailable"),
    ("P3","mainali-2025-universal-statistics.pdf","Published paper with cover and STAR Methods"),
    ("P3SI","mainali-2025-supplement.pdf","Supplementary figures and Methods S1-S4"),
]

def dump(path,obj):
    path.write_text(yaml.safe_dump(obj,sort_keys=False,allow_unicode=True),encoding="utf-8")

def paragraph_after(lines,start):
    acc=[]
    for line in lines[start:]:
        if not line.strip():
            if acc:break
            continue
        if line.startswith(("#","$$","|","{{","[^")):break
        acc.append(line.strip())
    return " ".join(acc)

def prepare():
    for stem,cid,pid,role,prereqs in CHAPTERS:
        path=ROOT/"content/chapters"/(stem+".md")
        if not path.exists():
            raise FileNotFoundError(f"Authored chapter not yet available: {path}")
        lines=path.read_text(encoding="utf-8").splitlines()
        h1=re.match(r"^# (.*?)\s*\{#[^}]+\}\s*$",lines[0])
        if not h1:raise ValueError(f"Missing explicit chapter heading: {stem}")
        sections=[]
        for idx,line in enumerate(lines):
            match=re.match(r"^(#{2,6}) (.*?)\s*\{#([^}]+)\}\s*$",line)
            if not match:continue
            level,title,sid=len(match[1]),match[2],match[3]
            if not re.fullmatch(r"sec:[A-Z0-9-]+",sid):raise ValueError(f"Invalid section id {sid}")
            sections.append({"id":sid,"title":title,"summary":paragraph_after(lines,idx+1),"level":level})
        # Generated navigation summaries have no footnote-definition context.
        # Keep citations in the authored paragraph, not unresolved in the index.
        purpose=re.sub(r"\[\^[^\]]+\]", "", paragraph_after(lines,1))
        sidecar_path=path.with_suffix(".yaml")
        existing_blocks=(yaml.safe_load(sidecar_path.read_text(encoding="utf-8")) or {}).get("blocks",[]) if sidecar_path.exists() else []
        packet={"chapter_id":cid,"part_id":pid,"title":h1[1],
                "purpose":purpose,"role":role,"page_break_before":True,
                "pedagogical_prerequisites":prereqs,"explicit_render_dependencies":[],
                "discovered_references":[],"navigation_dependencies":[] if role!="chapter" else [pid],
                "section_list":sections,"blocks":existing_blocks,"source_loci":[]}
        if cid=="ch:FOUNDATIONS":
            original_attractor={"id":"fig:FOUNDATIONS-ATTRACTOR","kind":"figure",
                "placement":"sec:FOUNDATIONS-ATTRACTOR",
                "asset":"assets/approved/visuals/attractor-directions.svg",
                "caption":"A common activity disturbance returns to the initial angle, while an along-line disturbance persists as a changed angle. The solid arrow is deterministic recovery; the dashed arrow is an imposed disturbance. This is the guide's two-activity construction, not experimental data.",
                "alt":"Two activity axes in hertz, a diagonal fixed-point line, initial state at 50 and 30, common disturbance at 53 and 33 with a solid arrow back, and along-line disturbance at 53 and 27 corresponding to 6.5 degrees.",
                "width_inches":6.4,"html_fold":"never"}
            # Seed the original only when absent. Later figure additions and
            # their independently reviewed text remain authored sidecar blocks.
            if not any(block.get("id")==original_attractor["id"] for block in packet["blocks"]):
                packet["blocks"].insert(0,original_attractor)
        dump(path.with_suffix(".yaml"),packet)

    # These two files were created by publisher init for its empty starter only.
    for name in ["introduction.md","introduction.yaml"]:
        starter=ROOT/"content/chapters"/name
        if starter.exists():starter.unlink()

    plan={"schema_version":3,"book":{"title":"Neural Codes, Noise, and Memory: A Guide to Three Papers",
        "contributors":[],"front_matter":["ch:READING-GUIDE"],"parts":[
            {"part_id":"part:MECHANISMS","title":"Noise and persistent activity",
             "purpose":"A stable population pattern can retain a continuous value while fluctuations move that value along its family of persistent states. These chapters establish the neural and probability background, derive the surviving motion, and connect it to limits on information and readout.",
             "chapters":["ch:FOUNDATIONS","ch:MEMORY-DYNAMICS","ch:MEMORY-INFORMATION"]},
            {"part_id":"part:OBSERVATIONS","title":"Eye drift and spatial representations",
             "purpose":"Neural fluctuations reach behavior through a motor pathway, while spatial tuning describes how a position is expressed across cells. The eye and place-field studies constrain these different relationships. The final chapter connects their results without treating a static map as a complete dynamical model.",
             "chapters":["ch:EYE-DRIFT","ch:PLACE-FIELDS","ch:SYNTHESIS"]}],
        "appendices":["ch:GLOSSARY","ch:REFERENCES"]}}
    dump(ROOT/"plan/chapter-plan.yaml",plan)

    config=yaml.safe_load((ROOT/"guide-project.yaml").read_text(encoding="utf-8"))
    config["guide"]["description"]="This guide teaches the neural background and central derivations of Burak and Fiete (2012), Ben-Shushan and colleagues (2022), and Mainali and colleagues (2025). Begin with the reading path for paper copies, assumed knowledge, and the route through the mathematics."
    config["publication"]["required_outputs"]=["html"]
    config["publication"]["reproducibility"]["source_date_epoch"]=int(datetime.datetime.fromisoformat("2026-10-22T19:06:07.534112+03:00").timestamp())
    config["publication"]["renderers"]["quarto"]["html_folding"]={"enabled":False}
    dump(ROOT/"guide-project.yaml",config)

    inventory=[];manifest=[];order=0
    old_inventory={}
    inventory_path=ROOT/"source-maps/source-inventory.csv"
    if inventory_path.exists():
        with inventory_path.open(encoding="utf-8-sig",newline="") as f:
            old_inventory={row.get("source_unit_id"):row for row in csv.DictReader(f)}
    assetroot=ROOT/"assets/papers";assetroot.mkdir(parents=True,exist_ok=True)
    for sid,name,kind in SOURCES:
        original=PARENT/"papers"/name
        if not original.exists():raise FileNotFoundError(original)
        target=assetroot/name
        digest=hashlib.sha256(original.read_bytes()).hexdigest()
        if not target.exists():shutil.copy2(original,target)
        elif hashlib.sha256(target.read_bytes()).hexdigest()!=digest:
            raise ValueError(f"Existing source copy differs: {target}")
        reader=PdfReader(str(target));pages=len(reader.pages)
        manifest.append({"source_id":sid,"path":str(target.relative_to(ROOT)).replace("\\","/"),"sha256":digest,"page_count":pages,"kind":kind})
        for index,page in enumerate(reader.pages,1):
            key=f"{sid}-p{index:02d}"
            old=old_inventory.get(key,{})
            text=old["text_preview"] if old.get("source_sha256")==digest else " ".join((page.extract_text() or "").split())[:220]
            order+=1
            inventory.append({"source_unit_id":key,"source_id":sid,
                "source_path":str(target.relative_to(ROOT)).replace("\\","/"),"source_sha256":digest,
                "unit_locator":f"PDF page {index}","presentation_order":order,
                "unit_type":"pdf-page","title":kind,"text_preview":text[:220]})
    with (ROOT/"source-maps/source-inventory.csv").open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=list(inventory[0]));w.writeheader();w.writerows(inventory)
    dump(ROOT/"sources/source-manifest.yaml",{"schema_version":1,"sources":manifest})
    print(json.dumps({"chapters":len(CHAPTERS),"source_files":len(manifest),"source_pages":len(inventory)},indent=2))

if __name__=="__main__":prepare()
