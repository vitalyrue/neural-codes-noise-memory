"""Recorded, exact context edits. Does not regenerate the chapter plan."""
from pathlib import Path
import json, hashlib, datetime, re
import yaml

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
changes = []
def replace(rel, old, new, reason):
    path = ROOT / rel
    text = path.read_text(encoding='utf-8')
    assert text.count(old) == 1, (rel, text.count(old), old[:80])
    changes.append(dict(file=rel, old=old, new=new, reason=reason,
                        before_sha256=hashlib.sha256(path.read_bytes()).hexdigest()))
def scalar(rel, key, value, reason):
    path = ROOT / rel
    text = path.read_text(encoding='utf-8')
    match = re.search(r'^' + re.escape(key) + r':[^\n]*(?:\n +[^\n]*)*', text, re.M)
    assert match, (rel, key)
    old = match.group(0)
    # All replacements are plain single-line strings, quoted as JSON/YAML.
    replace(rel, old, key + ': ' + json.dumps(value, ensure_ascii=False), reason)

description = ('These three neuroscience papers study how groups of nerve cells represent information used in memory, eye control, and navigation. The guide connects mathematical models of stored values with eye-movement recordings from monkeys and recordings of spatial activity in rodents and bats. Begin with the reading path for the setting, contribution, and limits of each study, followed by the background and step-by-step calculations.')
scalar('guide-project.yaml', '  description', description, 'Establish the scientific field, biological subjects and relation between theory and recordings on the landing page.')

rel = 'content/chapters/00-reading-guide.md'
old = 'A remembered direction must remain useful after its cue disappears. The eyes must maintain a position while we look at a target. An animal moving through an environment must represent where it is. How do groups of nerve cells perform these tasks when their electrical signals are brief and variable?'
new = ('The subject is neuroscience: how groups of nerve cells represent information used in memory, eye control, and navigation. The three papers examine mathematical models that store a quantity such as an angle, eye movements and neural activity recorded in macaque monkeys, and location-dependent neural activity recorded in rodents and bats. They ask how activity can retain a value, how an internal fluctuation can move the eyes, and why a cell can respond at several separate locations.')
replace(rel, old, new, 'Identify the realm, species, tasks and different kinds of evidence before the reader encounters abstract representations.')
replace(rel, 'These questions belong to computational and systems neuroscience: explaining how groups of [**neuron**]{.definition-term custom-style="Definition Term"}s, the brain\'s signaling cells, represent information and support behavior.', 'A remembered direction must remain useful after its cue disappears; the eyes must hold an angle while an animal looks at a target; a moving animal must keep track of where it is. These tasks depend on groups of [**neuron**]{.definition-term custom-style="Definition Term"}s, the brain\'s signaling cells, whose electrical signals are brief and variable. Computational and systems neuroscience studies how these cells and their interactions support such behavior.', 'Connect observable tasks to cells and methods while preserving the first blue definition.')

replace('content/index.md', 'Neural circuits represent quantities such as location and eye position while individual spikes fluctuate. This guide develops the background and central calculations of Burak and Fiete (2012), Ben-Shushan and colleagues (2022), and Mainali and colleagues (2025).', description, 'Keep the source index consistent with the rendered landing description.')

parts = [
('A stable population pattern can retain a continuous value while fluctuations\n      move that value along its family of persistent states. These chapters establish the\n      neural and probability background, derive the surviving motion, and connect it to limits\n      on information and readout.',
'In a model neural circuit, the pattern of firing rates across many nerve cells can represent a remembered angle. Random spike timing can change that angle even while the circuit sustains its activity. Chapters 1–2 explain neural signals and how activity stores a value. Chapters 3–4 derive how that value wanders over time. Chapters 5–6 connect its stability to how accurately it can be estimated from the cells’ spikes.'),
('Neural fluctuations reach behavior through a motor pathway, while spatial tuning\n      describes how a position is expressed across cells. The eye and place-field studies\n      constrain these different relationships. The final chapter connects their results without\n      treating a static map as a complete dynamical model.',
'The next studies connect neural activity to eye control in monkeys and to location in rodents and bats. Chapters 7–9 follow the path from a neural command through eye muscles to measured movement, and test a possible source of drift. Chapters 10–12 explain where hippocampal nerve cells fire as an animal moves and compare a spatial model with recordings. Chapter 13 asks what these findings establish together and which connections remain untested.')]
for old, new in parts:
    replace('plan/chapter-plan.yaml', old, json.dumps(new, ensure_ascii=False), 'Make the Part introduction identify the cells, behavior, evidence and purpose of the chapter sequence.')

purposes = {
'00-reading-guide': new if False else 'These neuroscience papers study memory, eye control, and navigation. Their settings are mathematical models of stored values, eye-movement and neural recordings from macaque monkeys, and recordings of location-dependent neural activity in rodents and bats. This reading guide explains each study’s question, methods, findings, and limits.',
'01-foundations': 'Nerve cells communicate with brief electrical spikes. This chapter explains how firing rates across a group of cells can represent an eye angle or an animal’s location, and how variable spike timing affects that representation. These ideas supply the biological and probability background for the three papers.',
'01b-persistence': 'A neural circuit can sustain its firing while the value represented by that firing changes. Using eye angle as an example, this chapter separates changes in the activity of the cells from changes in the stored value. That distinction explains how persistent activity can still accumulate memory error.',
'02-memory-dynamics': 'Burak and Fiete model a group of interacting neurons that retains a continuous value after an input ends. This chapter follows spikes through their effects at synapses and back into firing, then derives how random spike timing displaces the stored value.',
'02b-memory-long-delays': 'In the memory-network model, random changes in a stored angle accumulate over time. This chapter extends the local spreading calculation to longer delays, where boundaries, angular wraparound, and systematic drift can change the size of the memory error.',
'03-memory-information': 'A neuron receiving spikes from a memory circuit has access to information about the stored value. This chapter measures the best accuracy available from those spikes and derives the constraint that this information places on the circuit’s memory stability.',
'03b-memory-readout': 'Reading spikes from a memory circuit takes time, during which its stored value can keep changing. This chapter calculates how much longer observation can help recover the value present at a recall cue, and explains why it cannot recover every earlier random displacement.',
'04-eye-drift': 'Even when a monkey looks at a stationary spot, its eyes drift slightly. This chapter explains how paired measurements of eye angle and the firing of neurons that command eye muscles support a shared neural source of that drift, before considering a particular circuit mechanism.',
'04b-eye-timing': 'Eye movements recorded during steady gaze in monkeys look different over short and long time intervals. This chapter uses their timing to distinguish fluctuations around a fixed command from accumulated changes in the command, while accounting for eye-position measurement error.',
'04c-eye-circuit': 'A circuit that stores the intended eye angle is one possible source of fixational drift. This chapter follows the proposed model from interacting neurons through motor neurons and muscles to eye motion, and explains how delayed visual feedback can limit that motion.',
'05-place-fields': 'Hippocampal place cells fire more at particular locations as an animal moves. This chapter introduces the rodent and bat recordings, then shows how a smooth random input that exceeds a firing threshold can produce several separate active regions for one cell.',
'05b-place-sizes': 'A place cell’s active regions can have different sizes on a route, across a floor, or in a flight volume. This chapter derives why the spatial model predicts different field-size distributions in one, two, and three dimensions, and identifies the high-threshold approximation used in that derivation.',
'05c-place-tests': 'Recordings show where a hippocampal cell is active as an animal moves through an environment. This chapter tests the spatial model against the shapes and arrangement of those regions, then asks what agreement can reveal about the inputs and connections that produce them.',
'06-synthesis': 'The three papers address different links between nerve-cell activity and behavior: retaining a value, producing eye movement, and representing location. This chapter compares what the models and recordings establish, and separates supported connections from further questions about how a complete neural circuit would work.'}
for stem, value in purposes.items():
    scalar('content/chapters/' + stem + '.yaml', 'purpose', value, 'Give the navigation excerpt enough setting to be understood without the surrounding chapter; keep citations in chapter text.')

journal = OUT / 'edits-root.json'
journal.write_text(json.dumps({'created': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'edits': changes}, indent=2, ensure_ascii=False), encoding='utf-8')
for change in changes:
    path = ROOT / change['file']
    text = path.read_text(encoding='utf-8')
    assert text.count(change['old']) == 1
    path.write_text(text.replace(change['old'], change['new']), encoding='utf-8')
for rel in {change['file'] for change in changes}:
    if rel.endswith('.yaml'):
        yaml.safe_load((ROOT / rel).read_text(encoding='utf-8'))
print(f'Applied {len(changes)} exact edits; journal: {journal}')
