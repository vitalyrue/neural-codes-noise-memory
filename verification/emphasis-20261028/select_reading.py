from pathlib import Path
import re,json,hashlib,datetime
r=Path(__file__).resolve().parents[2];o=Path(__file__).resolve().parent
p=r/'content/chapters/00-reading-guide.md';text=p.read_text(encoding='utf-8')
items=[]
def add(kind,selected,reason):
 assert text.count(selected)==1,(selected,text.count(selected))
 before=text[:text.index(selected)];matches=re.findall(r'\{#((?:ch|sec):[^}]+)\}',before)
 items.append({'kind':kind,'text':selected,'section':matches[-1],'reason':reason})
keys=[
'They ask how activity can retain a value, how an internal fluctuation can move the eyes, and why a cell can respond at several separate locations.',
'Yet the remembered value can change while the activity persists.',
'Their central result is a lower bound: the uncertainty in reading the network\'s current value limits how slowly that value can wander.',
'Ben-Shushan and colleagues (2022) ask whether the motion begins mainly in muscles or in neural commands sent to them.',
'Mainali, Azeredo da Silveira, and Burak (2025) ask whether one statistical account can explain this variety across species and spatial dimensions.',
'how interacting neurons can retain a value while random spike timing changes it.',
'An equation that specifies how a cell responds belongs to the model. A derivation works out what follows from that choice.',
'A successful numerical check of a probability identity is different from an independent reproduction of a paper\'s empirical result.'
]
for s in keys:add('key',s,'Central scientific question, contribution, or local distinction; wording unchanged.')
defs=[
'[**neuron**]{.definition-term custom-style="Definition Term"}s, the brain\'s signaling cells',
'Even while gaze is held on a stationary target, the eyes move smoothly and irregularly between brief, rapid movements. This smooth motion is called [**fixational drift**]{.definition-term custom-style="Definition Term"}.',
'[**retina**]{.definition-term custom-style="Definition Term"}, the light-sensitive tissue at the back of the eye',
'A [**place cell**]{.definition-term custom-style="Definition Term"} in the [**hippocampus**]{.definition-term custom-style="Definition Term"}, a brain region involved in memory and navigation, becomes more active in particular locations.',
'Each connected region of elevated activity is a [**place field**]{.definition-term custom-style="Definition Term"}.',
'[**diffusion coefficient**]{.definition-term custom-style="Definition Term"}, which sets how quickly uncertainty spreads',
'[**mean squared displacement**]{.definition-term custom-style="Definition Term"} (MSD), the average squared change in the represented coordinate after elapsed time $t$'
]
for s in defs:add('definition',s,'Existing term plus the phrase giving its meaning; no new definition or wording.')
covered=[]
for s in defs:
 for term in re.findall(r'\[\*\*([^*]+)\*\*\]\{\.definition-term',s):covered.append({'term':term,'status':'covered','reason':'Defining clause included.'})
files=[{'file':p.name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'selections':items,'definitionCoverage':covered}]
# Glossary entries are already short definition units; highlight their existing
# wording as a unit instead of treating a term name as the whole definition.
p=r/'content/chapters/glossary.md';text=p.read_text(encoding='utf-8');items=[]
for line in text.splitlines():
 if line.startswith('- ') and '.definition-term' in line:
  selected=line[2:];assert text.count(selected)==1
  items.append({'kind':'definition','text':selected,'section':'ch:GLOSSARY','reason':'The existing glossary entry is a definition unit.'})
files.append({'file':p.name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'selections':items,'definitionCoverage':[{'term':re.search(r'\[\*\*([^*]+)\*\*\]',x['text'])[1],'status':'covered','reason':'Whole existing glossary definition.'} for x in items]})
(o/'selections-reading.json').write_text(json.dumps({'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'files':files},indent=2,ensure_ascii=False),encoding='utf-8')
print('Reading guide:',len(keys),'key passages,',len(defs),'definition passages; glossary:',len(items),'definitions.')
