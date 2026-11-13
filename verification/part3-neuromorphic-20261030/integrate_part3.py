from pathlib import Path
import json, re
from datetime import datetime, timezone
import yaml

root = Path(__file__).resolve().parents[2]
task = Path(__file__).resolve().parent
chapters = root / 'content/chapters'
specs = [
    ('07-hardware-memory', 'ch:HARDWARE-MEMORY', ['ch:FOUNDATIONS', 'ch:PERSISTENCE']),
    ('08-hardware-dynamics', 'ch:HARDWARE-DYNAMICS', ['ch:HARDWARE-MEMORY', 'ch:MEMORY-DYNAMICS']),
    ('09-neuromorphic-systems', 'ch:NEUROMORPHIC-SYSTEMS', ['ch:HARDWARE-DYNAMICS']),
    ('10-hardware-tests', 'ch:HARDWARE-TESTS', ['ch:NEUROMORPHIC-SYSTEMS', 'ch:MEMORY-INFORMATION', 'ch:MEMORY-READOUT', 'ch:SYNTHESIS']),
]
for filename, cid, prereqs in specs:
    text = (chapters / (filename + '.md')).read_text(encoding='utf-8')
    title = re.search(r'^# (.+?) \{#', text).group(1)
    purpose = text.split('\n\n')[1]
    sections = []
    for match in re.finditer(r'^## (.+?) \{#(sec:[^}]+)\}\n\n', text, re.M):
        opening = text[match.end():].split('\n\n')[0]
        sections.append(dict(id=match[2], title=match[1], summary=opening, level=2))
    data = dict(chapter_id=cid, part_id='part:HARDWARE', title=title, purpose=purpose,
                role='chapter', page_break_before=True, pedagogical_prerequisites=prereqs,
                explicit_render_dependencies=[], discovered_references=[],
                navigation_dependencies=['part:HARDWARE'], section_list=sections, blocks=[], source_loci=[])
    (chapters / (filename + '.yaml')).write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=105), encoding='utf-8')

quote = 'Lastly, I would like to mention that systems of nerve cells, which stimulate each other in various possible cyclical ways, also constitute memories.'
assert len(quote.split()) <= 25, len(quote.split())
part = dict(
    part_id='part:HARDWARE', title='Neural memory in electronic hardware',
    purpose="Electronic circuits can store connection settings, changing neuron states, and values represented by a network. Part III starts with von Neumann's comparison of neural and electronic memory, then asks how these forms of storage differ physically. Chapters 14–15 explain storage and feedback; Chapter 16 examines selected neuromorphic results through 30 October 2026; Chapter 17 develops experiments that separate device errors from the loss of a remembered value.",
    content=[
        dict(type='paragraph', text='> “' + quote + '”'),
        dict(type='paragraph', text='John von Neumann, *The Computer and the Brain* (1958), [printed page 66, PDF page 78](https://vpb.smallyu.net/%5BAuthor%5D%20John.Von.Neumann/The%20Computer%20and%20The%20Brain.pdf#page=78).'),
        dict(type='paragraph', text="Von Neumann compares mutually stimulating nerve cells with electronic circuits that preserve a state through feedback. In the following pages he also questions whether active elements alone could provide the nervous system's main large-capacity store. His comparison invites us to distinguish a memory's physical mechanism from the information it keeps. It does not establish that every brain memory uses persistent activity, or that present hardware follows one historical line from his book."),
        dict(type='paragraph', text="The setting here is experimental and computational neuroscience joined with electronic engineering. We ask how a silicon circuit can retain a quantity such as an angle, and what physical processes limit its accuracy. [A durable connection weight, a lasting activity pattern, and an accurately remembered value are three different achievements.]{.key-statement}"),
        dict(type='paragraph', text="The path starts with what is stored and where, then explains what feedback preserves. With those distinctions in place, we compare digital spiking processors, analog neural circuits, and phase-change weight storage. The final chapter turns the comparison into measurements of drift, noise, decoding error, and energy. Parts I and II provide the neural models and experimental reasoning; this Part extends them to selected hardware research current to **30 October 2026**."),
        dict(type='paragraph', text="For a first pass, read the physical explanations, main results, and interpretations. Worked calculations and deeper derivations are folded. The comparison assumes the calculus, basic probability, and linear algebra used earlier; electronics terms are introduced as they become necessary."),
    ],
    chapters=[cid for _, cid, _ in specs],
)
plan_path = root / 'plan/chapter-plan.yaml'
plan = yaml.safe_load(plan_path.read_text(encoding='utf-8'))
assert not any(p['part_id']=='part:HARDWARE' for p in plan['book']['parts'])
plan['book']['parts'].append(part)
plan_path.write_text(yaml.safe_dump(plan, sort_keys=False, allow_unicode=True, width=110), encoding='utf-8')

intro = "Part III extends this reading into electronic implementations of neural memory. It begins with von Neumann's comparison, separates stored weights from changing neural states, and examines selected neuromorphic computing research through 30 October 2026. The final chapter proposes tests connecting device physics to the accuracy of a remembered value."
index = root / 'content/index.md'
index.write_text(index.read_text(encoding='utf-8').rstrip()+'\n\n'+intro+'\n', encoding='utf-8')
project = root / 'guide-project.yaml'
text = project.read_text(encoding='utf-8')
old = 'followed by the background and step-by-step calculations."'
assert old in text
text = text.replace(old, 'followed by the background and step-by-step calculations. Part III connects these neural memory questions to physical electronic storage and selected neuromorphic advances through 30 October 2026."')
project.write_text(text, encoding='utf-8')

reading_path = chapters/'00-reading-guide.md'
text = reading_path.read_text(encoding='utf-8')
heading = 'Electronic implementations make memory mechanisms testable'
section = "## "+heading+" {#sec:READING-HARDWARE}\n\n[Part III](../parts/part-hardware.html) asks how the neural memory mechanisms can be implemented in electronic circuits. Its setting is neuromorphic computing: engineered systems inspired by neural organization and dynamics. The chapters distinguish connection weights from changing neural states, explain how feedback affects retention, and examine selected hardware research through 30 October 2026. They end with a proposed experiment that separates systematic drift, random spreading, and readout error. This extension is a comparison of mechanisms and evidence; the three original papers remain the foundation of Parts I and II.\n\n"
text = text.replace('## Starting knowledge and reading paths', section+'## Starting knowledge and reading paths', 1)
reading_path.write_text(text, encoding='utf-8')
sidecar = chapters/'00-reading-guide.yaml'
data = yaml.safe_load(sidecar.read_text(encoding='utf-8'))
pos = next(i for i,s in enumerate(data['section_list']) if s['id']=='sec:READING-START')
data['section_list'].insert(pos, dict(id='sec:READING-HARDWARE', title=heading, summary=section.split('\n\n')[1], level=2))
sidecar.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=105), encoding='utf-8')

terms = [
 ('analog state', 'A physical magnitude, such as capacitor voltage, used to represent a model quantity.', 'ch-hardware-memory.html#sec-hardware-memory-storage'),
 ('bistability', 'Two locally stable states under the same ongoing conditions.', 'ch-hardware-dynamics.html#sec-hardware-dynamics-evidence'),
 ('device mismatch', 'Persistent differences between nominally identical circuit elements.', 'ch-hardware-memory.html#sec-hardware-memory-storage'),
 ('digital storage', 'Discrete symbols represented by distinguishable physical ranges.', 'ch-hardware-memory.html#sec-hardware-memory-storage'),
 ('in-memory computing', 'Performing operations where values are stored, reducing transfers to a separate arithmetic unit.', 'ch-hardware-memory.html#sec-hardware-memory-updates'),
 ('mixed-signal hardware', 'Hardware combining analog circuit variables with digital storage, communication, or calculation.', 'ch-hardware-memory.html#sec-hardware-memory-updates'),
 ('neuromorphic computing', 'Electronic computation inspired by neural organization or dynamics, with digital, analog, or combined implementations.', 'ch-hardware-memory.html#sec-hardware-memory-roles'),
 ('nonvolatile storage', 'Storage that can retain its state without continuous power, within its retention limits.', 'ch-hardware-memory.html#sec-hardware-memory-storage'),
 ('on-chip learning', 'Computing and applying some weight changes using circuitry on the chip.', 'ch-neuromorphic-systems.html#sec-neuromorphic-systems-architectures'),
 ('phase-change memory (PCM)', 'Storage in a material phase configuration read through its resistance or conductance.', 'ch-hardware-memory.html#sec-hardware-memory-storage'),
 ('pinning', 'Attraction of a nominally continuous memory toward preferred states.', 'ch-hardware-dynamics.html#sec-hardware-dynamics-errors'),
 ('static random-access memory (SRAM)', 'Digital storage whose powered transistor feedback maintains bits.', 'ch-hardware-memory.html#sec-hardware-memory-storage'),
 ('working memory', 'Keeping information about recent input available for a later task.', 'ch-hardware-memory.html#sec-hardware-memory-roles'),
]
glossary = chapters/'glossary.md'
text = glossary.read_text(encoding='utf-8').rstrip()+'\n\n## Physical implementation and neural memory {#sec:GLOSSARY-HARDWARE}\n\nThese terms are explained in the linked Part III passages.\n\n'
for term, definition, link in terms:
    text += '- [[**'+term+':**]{.definition-term custom-style="Definition Term"} '+definition+']{.definition-explanation} [Explanation](../chapters/'+link+').\n'
glossary.write_text(text, encoding='utf-8')
sidecar = chapters/'glossary.yaml'
data = yaml.safe_load(sidecar.read_text(encoding='utf-8'))
data['section_list'].append(dict(id='sec:GLOSSARY-HARDWARE', title='Physical implementation and neural memory', summary='These terms are explained in the linked Part III passages.', level=2))
sidecar.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=105), encoding='utf-8')

# Correct bibliography order to the actual first appearance in the new Part.
refpath = chapters/'references.md'
text = refpath.read_text(encoding='utf-8')
start = text.index('18. von Neumann')
entries = re.split(r'\n\n(?=\d+\. )', text[start:].strip())
by_number = {int(re.match(r'(\d+)\.',e)[1]):e for e in entries}
order = [18,20,19,21,22,24,25,26,27,28,29,23,30]
text = text[:start]+'\n\n'.join(re.sub(r'^\d+\.',str(i)+'.',by_number[n]) for i,n in enumerate(order,18))+'\n'
refpath.write_text(text, encoding='utf-8')

now = datetime.now(timezone.utc).isoformat()
state = json.loads((task/'STATE.json').read_text(encoding='utf-8'))
state.update(checkpoint_at=now, status='draft_integrated_for_independent_review', chapters=[x[1] for x in specs], quote_word_count=len(quote.split()))
(task/'STATE.json').write_text(json.dumps(state, indent=2), encoding='utf-8')
with (task/'checkpoints.jsonl').open('a',encoding='utf-8') as f:
    f.write(json.dumps(dict(at=now,status=state['status']))+'\n')
print(json.dumps(dict(status=state['status'],quote_words=len(quote.split()),chapters=state['chapters'])))
