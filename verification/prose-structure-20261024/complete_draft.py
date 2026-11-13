from pathlib import Path
from datetime import datetime
import hashlib,json,re
OUT=Path(__file__).resolve().parent;P=OUT/'proposed/content/chapters'
edits=[]
def edit(file,old,new,reason):
 p=P/file;text=p.read_text(encoding='utf-8');assert text.count(old)==1,(file,old[:60])
 edits.append({'file':'content/chapters/'+file,'before':old,'after':new,'kind':'definition','reason':reason})
 p.write_text(text.replace(old,new),encoding='utf-8',newline='\n')
def mark(t):return '[**'+t+'**]{.definition-term custom-style="Definition Term"}'
# These later passages remain as reminders; only their repeated first-definition color changes.
for file,start,terms in [
 ('01-foundations.md','Spatial tuning gives a second example.',['place cell','place field']),
 ('01b-persistence.md','The [**Brownian motion**]',['diffusion coefficient']),
 ('01b-persistence.md','The [**mean squared displacement**]',['mean squared displacement']),
 ('04-eye-drift.md','Looking steadily at a small spot',['fixational drift'])]:
 text=(P/file).read_text(encoding='utf-8');old=next(p for p in text.split('\n\n') if p.startswith(start));new=old
 for term in terms:new=new.replace(mark(term),term)
 edit(file,old,new,'The reading guide already teaches this meaning in blue. Retain the full later explanation while marking each first teaching occurrence only once.')

groups={
 'foundations-memory':{
  'encoding':'Establishing a population activity pattern from an input.',
  'excitatory input':"In the models used here, an input that increases a receiving neuron's tendency to fire.",
  'inhibitory input':"In the models used here, an input that reduces a receiving neuron's tendency to fire."},
 'information-eye':{
  'Translation invariance':'In the readout model, invariance under shifts of the represented value. It makes the readout variance independent of the cue state.',
  'hyperbolic tangent':r'The function $\tanh z=(e^z-e^{-z})/(e^z+e^{-z})$.',
  'inverse hyperbolic tangent':r'The inverse of $\tanh$ on $(-1,1)$, given by $\operatorname{artanh}z=\tfrac12\log[(1+z)/(1-z)]$.',
  'hyperbolic cotangent':r'The function $\coth z=1/\tanh z$, for real $z\ne0$.'},
 'place':{
  'upcrossing':'A point where a function crosses upward through a specified threshold.',
  'jointly Gaussian vector':'A random vector for which every linear combination of its entries is Gaussian.',
  'Smoothness':'The existence and regularity of derivatives of a function. The crossing and peak calculations require different derivative orders.',
  'gamma function':r'The function $\Gamma(t)=\int_0^\infty u^{t-1}e^{-u}\,du$ for $t>0$, extending factorials through $\Gamma(n+1)=n!$.',
  'critical point':"A point where a function's gradient is zero. The Euler calculation also requires invertible Hessians.",
  'Morse theory':"A theory relating the topology of a function's level-set regions to its critical points. The guide uses a signed critical-point count under its smoothness and nondegeneracy assumptions, including boundary contributions.",
  'Rayleigh distribution':'The distribution of a positive variable that is a scaled square root of an exponential variable.',
  'skew':r'The third centered moment divided by the variance to the power $3/2$, measuring asymmetry.',
  'excess kurtosis':r'The fourth centered moment divided by the squared variance, minus three. It is zero for a Gaussian population.',
  'lognormal distribution':'A distribution of positive values whose logarithms are Gaussian.',
  'mean curvature':'For a surface in three dimensions, the average of its two principal curvatures.',
  'Gaussian curvature':'For a surface in three dimensions, the product of its two principal curvatures.'}}
for group,entries in groups.items():
 for term,meaning in entries.items():
  text=(P/'glossary.md').read_text(encoding='utf-8');items=list(re.finditer(r'(?m)^- \[\*\*([^*]+):\*\*\].*$',text))
  assert term.casefold() not in [m.group(1).casefold() for m in items],term
  later=next((m for m in items if m.group(1).casefold()>term.casefold()),None)
  old=later.group(0) if later else items[-1].group(0);entry='- '+mark(term+':')+' '+meaning
  new=entry+'\n'+old if later else old+'\n'+entry
  edit('glossary.md',old,new,'Matching lookup entry for the first teaching occurrence in '+group+'.')
(OUT/'coordinator-edits.json').write_text(json.dumps({'at':datetime.now().astimezone().isoformat(),'edits':edits,'glossary_review_groups':groups},indent=2,ensure_ascii=False),encoding='utf-8')
files=[p for p in P.glob('*.md')]
frozen={'at':datetime.now().astimezone().isoformat(),'files':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in files},'rule':'C:/dev/NBIS/publisher-releases/0.8.23/skills/course-study-guide-builder/references/pedagogy-language-contract.md','status':'draft for independent review'}
(OUT/'frozen-v1.json').write_text(json.dumps(frozen,indent=2),encoding='utf-8')
print(json.dumps({'files':len(files),'coordinator_edits':len(edits),'new_glossary_entries':sum(len(d) for d in groups.values()),'at':frozen['at']}))
