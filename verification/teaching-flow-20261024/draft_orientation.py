"""Prepare the coordinator-owned reading guide and shared title proposals."""
from pathlib import Path
from datetime import datetime
import hashlib, json, re, yaml

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
DEST = OUT / 'proposed'
source = ROOT / 'content/chapters/00-reading-guide.md'
text = source.read_text(encoding='utf-8')
before = text
decisions = [
 ('ch:READING-GUIDE', 'Research questions and reading guide', 'What the three papers establish',
  'The page distinguishes a model bound, an inference from recordings, and a statistical explanation before giving reading paths.'),
 ('sec:READING-FIELD', 'The field and the shared problem', 'Variable neural signals must support reliable behavior',
  'The opening identifies the common problem that gives the three studies their purpose.'),
 ('sec:READING-MEMORY', 'How can a noisy circuit retain a value?', 'Persistent activity can still lose memory accuracy',
  'The model keeps activity going while the represented value wanders; the lower bound constrains that loss.'),
 ('sec:READING-EYE', 'What makes the eyes drift during fixation?', 'Eye drift points to a shared neural source',
  'The recordings support an upstream contribution under explicit assumptions, without locating one circuit uniquely.'),
 ('sec:READING-PLACE', 'Why do place fields have different sizes and shapes?', 'Smooth random maps explain the variety of place fields',
  'The model accounts for size and shape statistics across the examined settings, with wiring treated as an interpretation.'),
 ('sec:READING-START', 'Starting knowledge and reading paths', 'Starting knowledge and reading paths',
  'This is navigation rather than a scientific result; the current title tells the reader how to use it.'),
 ('sec:READING-PAPERS', 'The original papers', 'The original papers',
  'A direct lookup title is appropriate for the copies and supporting information.'),
 ('sec:READING-SCOPE', 'Scope and notation', 'How to interpret the calculations and evidence',
  'The section distinguishes teaching checks from empirical reproduction and sets the diffusion convention used later.'),
]
edits=[]
for key, old, new, reason in decisions:
    if old == new: continue
    a=f'{old} {{#{key}}}'
    b=f'{new} {{#{key}}}'
    assert text.count(a)==1, key
    text=text.replace(a,b)
    edits.append(dict(kind='heading',id=key,before=a,after=b,reason=reason))

anchor='After the foundations, the [guide map](../chapters/ch-foundations.html#fig-foundations-paper-map) shows the three paper questions together.'
addition='On a first reading, follow the main text, figures, assumptions, and results. The expandable notes preserve longer calculations and extensions; open one when you want to check the steps behind a result. The explanations needed for the next section remain in the main text.'
assert text.count(anchor)==1
text=text.replace(anchor, anchor+'\n\n'+addition)
edits.append(dict(kind='insert',id='sec:READING-START',before=anchor,after=anchor+'\n\n'+addition,reason='Explain how the selected folds support the two reading depths without suggesting that every equation is optional.'))

# The reading path is followed by evidence conventions; paper-copy access closes
# the orientation as a separate reference task. Keep every original paragraph.
papers=text.index('## The original papers')
scope=text.index('## How to interpret the calculations and evidence')
notes=text.index('[^orientation-memory]:')
oldspan=text[papers:notes]
newspan=text[scope:notes]+text[papers:scope]
text=text[:papers]+newspan+text[notes:]
edits.append(dict(kind='move',id='sec:READING-SCOPE',before=oldspan,after=newspan,reason='Keep reading paths and interpretation conventions together before switching to the original-paper lookup list. Stable section IDs and all paragraphs stay intact.'))

packet=yaml.safe_load(source.with_suffix('.yaml').read_text(encoding='utf-8'))
titles={r[0]:r[2] for r in decisions}
packet['title']=titles['ch:READING-GUIDE']
sections={s['id']:s for s in packet['section_list']}
order=[]
for m in re.finditer(r'^## (.+) \{#([^}]+)\}\n\n',text,re.M):
    key=m.group(2); row=sections[key]
    row['title']=m.group(1)
    row['summary']=text[m.end():].split('\n\n',1)[0]
    order.append(row)
packet['section_list']=order
dest=DEST/'content/chapters'
dest.mkdir(parents=True,exist_ok=True)
(dest/source.name).write_text(text,encoding='utf-8')
(dest/source.with_suffix('.yaml').name).write_text(yaml.safe_dump(packet,allow_unicode=True,sort_keys=False,width=84),encoding='utf-8')

plan=yaml.safe_load((ROOT/'plan/chapter-plan.yaml').read_text(encoding='utf-8'))
partdecisions=[
 ('part:MECHANISMS','Noise and persistent activity','Persistent activity has a limit on memory accuracy',
  'Chapters 1 to 3 establish the mechanism and derive its accuracy and readout limits. The purpose paragraph supplies the continuous-state and noise assumptions.'),
 ('part:OBSERVATIONS','Eye drift and spatial representations','Eye motion and place fields constrain different parts of a neural code',
  'Chapters 4 and 5 constrain the origin of motion and spatial tuning separately; Chapter 6 explains the added assumptions needed to combine them.'),
]
for key,old,new,reason in partdecisions:
    part=next(p for p in plan['book']['parts'] if p['part_id']==key)
    assert part['title']==old
    part['title']=new
(DEST/'plan').mkdir(exist_ok=True)
(DEST/'plan/chapter-plan.yaml').write_text(yaml.safe_dump(plan,allow_unicode=True,sort_keys=False,width=84),encoding='utf-8')

paragraph_groups=[
 ('opening and READING-FIELD','Concrete memory, gaze, and navigation tasks establish the problem before the field name and methods. Retain this order.'),
 ('READING-MEMORY paragraphs 1-3','Problem: activity can persist while the value changes. Method: a continuous family of patterns and random spikes. Result: lower bound, time dependence and scope. Retain so the bound answers an already understood question.'),
 ('READING-EYE paragraphs 1-3','Define fixation drift and why it matters, explain calibration and paired recordings, then give the 82 percent inference and its assumptions. Retain; moving the percentage earlier would detach it from what was measured.'),
 ('READING-PLACE paragraphs 1-4','Teach place cells and the varied fields first, then the thresholded-map model and comparisons, then results and wiring limit. The final comparison states why the three contributions differ. Retain.'),
 ('READING-START paragraphs 1-4','Audience and chapter progression precede alternative routes, map access, then the added instructions for expandable depth. Each paragraph answers how to start or choose a route.'),
 ('READING-SCOPE paragraphs 1-3','Guide calculations and their purpose precede empirical reproduction limits, then the shared notation. Move this complete section after reading paths so interpretation remains part of the orientation.'),
 ('READING-PAPERS','Copy/version sentence precedes the list, and the formula caveat follows the original supporting-information links. Move only as a complete section to keep that dependency.'),
]
record=dict(at=datetime.now().astimezone().isoformat(), source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
 book_order={'decision':'retain', 'benefit':'The foundations support both branches; mechanism precedes information limits and experimental use; synthesis follows both temporal and spatial models.',
 'alternative':'Move the place-field chapter immediately after foundations.', 'alternative_benefit':'Readers interested only in spatial codes reach their paper earlier.',
 'alternative_cost':'It interrupts the memory-to-information-to-eye argument. The existing explicit 1-to-5 reading path supplies the shorter route without changing the main progression.'},
 title_decisions=[dict(id=i,old=o,new=n,reason=r,decision='retain' if o==n else 'change') for i,o,n,r in decisions+partdecisions],
 paragraph_decisions=[dict(locus=l,reason=r) for l,r in paragraph_groups],fold_decisions=[],edits=edits,
 unchanged_lookup_titles=['Glossary','References'],
 limits='This is an author proposal; independent truth, wording and reading-flow review are still required.')
(OUT/'orientation-decisions.json').write_text(json.dumps(record,indent=2,ensure_ascii=False),encoding='utf-8')
print(json.dumps({'at':record['at'],'headings_changed':sum(r['decision']=='change' for r in record['title_decisions']),'sections_moved':1,'folds':0}))
