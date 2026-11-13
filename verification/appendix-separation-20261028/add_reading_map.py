from pathlib import Path
import json, datetime, hashlib
import yaml
ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
path=ROOT/'content/chapters/00-reading-guide.md'
old='## How to interpret the calculations and evidence {#sec:READING-SCOPE}'
addition='''## Neural mechanisms and mathematical derivations answer different questions {#sec:READING-MECHANISM-MATH}

Chapters 3–6 explain how interacting neurons can retain a value while random spike timing changes it. Their treatment of the Burak and Fiete appendix separates three parts of each substantial topic:

1. **Neural mechanism:** which cells and signals interact, what changes, and which features are assumptions of the model. For readout, this part also states what an observer can measure and which value it must estimate.
2. **Mathematical derivation:** the general tool, its conditions, and the calculation after neural quantities are assigned to the symbols.
3. **Interpretation:** what the result predicts about memory or readout, and what its assumptions leave unresolved.

For example, a spike can disturb several cells' activity. The circuit's interactions remove some changes, while others leave the represented angle displaced. Linear algebra calculates which part survives; probability gives the spread of that displacement. The result then predicts how quickly memory errors accumulate in this model. The mathematical tools also apply to other systems, but this neural prediction depends on the circuit and spike statistics used in the calculation.

The same distinction matters for readout. A calculation of the best possible estimate sets a benchmark under specified access to neural signals. Establishing that an animal's neurons implement the assumed computation requires separate evidence.

For a first conceptual pass, read the mechanism, inspect the displayed result and its variables, then read the interpretation. Follow the mathematical derivation when you want to understand why the result holds or calculate with it. Assumptions remain part of both readings.

The [PNAS appendix](https://www.pnas.org/action/downloadSupplement?doi=10.1073%2Fpnas.1117386109&file=Appendix.pdf) supplies both neural-model choices and mathematical arguments. This map links its seven sections to the guide's explanations. Page links open the local copy; the guide sometimes uses an equivalent teaching derivation and identifies source inconsistencies beside the affected calculation.

{{block:tbl:READING-APPENDIX}}

'''
rows=[
['[I: large-network limit, p. 1](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=1)', 'How can many variable spike inputs produce small fluctuations in total input?', '[Mean and variance scaling; Gaussian approximation](../chapters/ch-memory-dynamics.html#sec-memory-spikes)'],
['[II: diffusion coefficient, p. 3](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=3)', 'Which changes in neural activity leave the stored value displaced?', '[Linearization and projection](../chapters/ch-memory-dynamics.html#sec-memory-linearization), [diffusion](../chapters/ch-memory-dynamics.html#sec-memory-diffusion), and [systematic drift](../chapters/ch-memory-long-delays.html#sec-memory-drift-scope)'],
['[III: motion along the attractor, p. 6](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=6)', 'How do memory errors grow over long delays or around an angular range?', '[Probability-density evolution and boundary conditions](../chapters/ch-memory-long-delays.html#sec-memory-long-time)'],
['[IV: internal Fisher information, p. 9](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=9)', 'How well can nearby stored values be distinguished from their spikes?', '[Spike likelihood and information per unit time](../chapters/ch-memory-information.html#sec-memory-fi)'],
['[V: information–diffusion inequality, p. 10](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=10)', 'How does uncertainty in the circuit’s own spikes constrain memory stability?', '[Scalar and matrix bounds, with equality conditions](../chapters/ch-memory-information.html#sec-memory-bound)'],
['[VI: readout, p. 12](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=12)', 'How much does longer observation help when the stored value keeps moving?', '[Storage and readout error](../chapters/ch-memory-readout.html#sec-memory-readout-setup), [equal weighting](../chapters/ch-memory-readout.html#sec-memory-naive), [ideal readout](../chapters/ch-memory-readout.html#sec-memory-ideal), and [partial access](../chapters/ch-memory-readout.html#sec-memory-partial)'],
['[VII: model extensions, p. 17](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=17)', 'What changes when firing rates respond gradually or the noise law changes?', '[Two time scales and alternative noise statistics](../chapters/ch-memory-readout.html#sec-memory-extensions)']]
block={'id':'tbl:READING-APPENDIX','kind':'table','placement':'sec:READING-MECHANISM-MATH','headers':['Appendix section','Neural question','Mathematical explanation in the guide'],'rows':rows,'caption':'Reading map for the Burak and Fiete supporting text. Page numbers refer to the appendix PDF.','first_column_role':'row-labels','html_fold':'never'}
text=path.read_text(encoding='utf-8'); assert text.count(old)==1
side=path.with_suffix('.yaml');data=yaml.safe_load(side.read_text(encoding='utf-8'))
assert not any(x['id']==block['id'] for x in data['blocks'])
journal={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'file':'content/chapters/00-reading-guide.md','old':old,'new':addition+old,'reason':'Reader path and exact SI-to-guide map for the user-selected mechanism/derivation/interpretation separation.','before_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'new_block':block,'unchanged_existing_content':True}
(OUT/'edits-reading-map.json').write_text(json.dumps(journal,indent=2,ensure_ascii=False),encoding='utf-8')
path.write_text(text.replace(old,addition+old),encoding='utf-8')
data['blocks'].append(block)
data['section_list'].insert(next(i for i,s in enumerate(data['section_list']) if s['id']=='sec:READING-SCOPE'),{'id':'sec:READING-MECHANISM-MATH','title':'Neural mechanisms and mathematical derivations answer different questions','summary':addition.split('\n\n')[1],'level':2})
side.write_text(yaml.safe_dump(data,sort_keys=False,allow_unicode=True,width=100),encoding='utf-8')
print('Added reading path and typed seven-row appendix map; existing content retained.')
