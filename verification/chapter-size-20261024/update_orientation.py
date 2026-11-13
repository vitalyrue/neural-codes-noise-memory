from pathlib import Path
import json,re,yaml
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[1]
p=ROOT/'content/chapters/00-reading-guide.md'
t=p.read_text(encoding='utf-8')
edits=[
 ('Chapters 2 and 3 derive the result and its limits.','Chapters 3–6 develop the [diffusion calculation](../chapters/ch-memory-dynamics.html), its long-delay behavior, the [information bound](../chapters/ch-memory-information.html), and the limits of [readout](../chapters/ch-memory-readout.html).'),
 ('Chapter 4 separates the measured relationships, the statistical inference and the proposed mechanism.','Chapters 7–9 separate the [shared-drive inference](../chapters/ch-eye-drift.html), the [timing of drift](../chapters/ch-eye-timing.html), and the [proposed circuit mechanism](../chapters/ch-eye-circuit.html).'),
 ('Chapter 5 develops the model and distinguishes exact predictions, limiting approximations and empirical tests.','Chapters 10–12 develop the [spatial model](../chapters/ch-place-fields.html), its [size and shape predictions](../chapters/ch-place-sizes.html), and the [tests and circuit interpretation](../chapters/ch-place-tests.html). They distinguish exact predictions, limiting approximations and empirical comparisons.'),
 ('developed in Chapter 6.','developed in [Chapter 13](../chapters/ch-synthesis.html).'),
 ('The first chapter establishes spikes, population activity, fixed points, covariance, and diffusion. Chapters 2 and 3 derive the persistent-activity model and its information bound. Chapter 4 applies the dynamical ideas to eye drift. Chapter 5 develops spatial Gaussian processes and place-field geometry. Chapter 6 brings the results together and compares related work.','The first two chapters establish [neural signals and variability](../chapters/ch-foundations.html), then [persistence and accumulated error](../chapters/ch-persistence.html). Chapters 3–6 derive memory diffusion, its long-delay behavior, the information bound, and readout. Chapters 7–9 follow the eye study from shared-drive evidence through timing to a circuit model. Chapters 10–12 develop spatial maps, their size predictions, and tests of their shapes and possible origins. Chapter 13 connects the results and compares related work. Each chapter opens with its question and the reason for its path through the material.'),
 ('For the memory and eye papers, follow chapters 1 through 4 in order. For place fields, the relevant starting path is chapter 1 followed by chapter 5; its Gaussian-process calculation does not require every readout result in chapter 3.','For the memory and eye papers, follow chapters 1 through 9 in order. For place fields, read the two foundations chapters and then chapters 10–12; the spatial calculation does not require the readout derivation in chapter 6.'),
 ('Chapter 1 explains this model and its assumptions.','[Chapter 2](../chapters/ch-persistence.html#sec-foundations-diffusion) explains this model and its assumptions.'),
 ('The place-field chapter uses $q$','The place-field chapters use $q$')]
for before,after in edits:
 assert t.count(before)==1,before
 t=t.replace(before,after)
p.write_text(t,encoding='utf-8',newline='\n')
# Refresh summaries from their real paragraphs for changed and retained chapter sources.
for p in (ROOT/'content/chapters').glob('*.md'):
 if p.name in ['glossary.md','references.md']:continue
 y=p.with_suffix('.yaml');meta=yaml.safe_load(y.read_text(encoding='utf-8'));text=p.read_text(encoding='utf-8')
 for s in meta.get('section_list',[]):
  m=re.search(r'(?m)^#{2,6} .+? \{#'+re.escape(s['id'])+r'\}\s*\n',text)
  if m:s['summary']=text[m.end():].strip().split('\n\n')[0]
 y.write_text(yaml.safe_dump(meta,allow_unicode=True,sort_keys=False,width=88),encoding='utf-8',newline='\n')
(OUT/'orientation-edits.json').write_text(json.dumps([{'before':a,'after':b} for a,b in edits],indent=2),encoding='utf-8')
print('Reading paths now match the thirteen chapters.')
