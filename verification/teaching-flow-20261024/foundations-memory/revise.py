from pathlib import Path
import datetime, hashlib, json, re, difflib
import yaml

ROOT=Path('C:/dev/clsc/burak-papers/guide')
TASK=ROOT/'verification/teaching-flow-20261024'
GROUP=TASK/'foundations-memory'
OUT=TASK/'proposed/content/chapters'
OUT.mkdir(parents=True,exist_ok=True)
H=lambda s:hashlib.sha256(s.encode('utf-8')).hexdigest()
now=lambda:datetime.datetime.now().astimezone().isoformat()

# Every heading was read separately. These are exact local decisions, not word substitutions.
titles={
'01-foundations':[
('ch:FOUNDATIONS','Neural activity, stored values, and random motion','Persistent neural activity can still accumulate memory error','The opening and two-activity example distinguish a coherent neural pattern from retaining the correct coordinate.'),
('sec:FOUNDATIONS-SPIKES','Spikes, rates, and population patterns','Patterns of firing rates represent a value','Single-cell tuning is combined into a population vector and extended to spatial tuning. The title describes that learned relationship.'),
('sec:FOUNDATIONS-POISSON','A variable spike count at a fixed rate','A variable spike count at a fixed rate','Already expresses the key distinction: fixed expected rate does not fix the observed count.'),
('sec:FOUNDATIONS-COVARIANCE','Variance, covariance, and displacement','Mean squared displacement combines random spread with mean motion','Covariance identities prepare the displacement identity and prevent treating MSD or correlation as a source fraction.'),
('sec:FOUNDATIONS-ATTRACTOR','Stable activity with a vulnerable stored value','Stable activity with a vulnerable stored value','Already states the learned contrast; the two disturbances demonstrate why stability can coexist with coordinate error.'),
('sec:FOUNDATIONS-DIFFUSION','Repeated perturbations become diffusion','Independent, unbiased changes give linear variance growth','The independent zero-mean increment calculation establishes the result under its assumptions; boundaries remain explicitly limited in the body.'),
('sec:FOUNDATIONS-RANDOMNESS','Randomness across time and across space','A fixed spatial map differs from a value that wanders over time','The section distinguishes one random spatial function from accumulating temporal fluctuations, with the three-paper map.'),
],
'02-memory-dynamics':[
('ch:MEMORY-DYNAMICS','How spiking noise moves a stored memory','Spiking noise produces diffusion along the memory attractor','The chapter derives leading local diffusion from projected spike noise. Naming diffusion and the attractor states the knowledge gained more precisely than how noise moves memory; the body retains the weak-noise, continuous-family and drift qualifications.'),
('sec:MEMORY-SPIKES','From individual spikes to a slowly changing network state','Recurrent spikes renew decaying synaptic activity','The model cycle links activation decay, transfer rates and new spikes; the weak-noise approximation follows that cycle.'),
('sec:MEMORY-LINEARIZATION','Which part of a perturbation survives?',"The network's return flow determines the lasting memory change",'The left vector extracts the endpoint shift after stable modes decay. The tilted example proves why following the return flow, rather than taking a perpendicular projection, gives the surviving change.'),
('sec:MEMORY-DIFFUSION','Projecting spike fluctuations gives the diffusion coefficient','Projecting spike fluctuations gives the diffusion coefficient','Already states the calculation and result. The body preserves locality and leading weak-noise scope.'),
('sec:MEMORY-SYMMETRIC','Symmetric weights make the projection measurable','Symmetric weights express diffusion through tuning curves','The derivation supplies a tuning-curve formula but does not establish experimental access to every required transfer quantity. The new title makes the mathematical contribution explicit.'),
('sec:MEMORY-LONG-TIME','From local spreading to long delay errors','Long delay errors depend on boundaries and local diffusion','The line/ring comparison and variable-D calculation show why local D alone does not imply indefinitely linear reported error.'),
('sec:MEMORY-DRIFT-SCOPE','Random drift, systematic drift, and a mistuned network','A diffusion calculation does not determine systematic drift','The section gives this specific limit, then separates drift tuning from random increments and qualifies correlated-noise extensions.'),
('sec:MEMORY-FIGURES','Reading the first two figures','Figures distinguish memory motion from readout error and test diffusion','Figure 1 separates motion of the stored value from uncertainty reading it. Figure 2 tests the projection calculation in two simulated designs.'),
]}

changes=[]
folds=[]
sources={}
for stem, decisions in titles.items():
    p=ROOT/'content/chapters'/f'{stem}.md'
    source=p.read_text(encoding='utf-8')
    sources[stem]=source
    text=source
    for anchor,old,new,reason in decisions:
        oldline=next(l for l in text.splitlines() if l.endswith('{#'+anchor+'}'))
        assert re.sub(r'^#+ ','',oldline).rsplit(' {#',1)[0]==old
        newline=oldline.replace(old,new,1)
        if old!=new:
            text=text.replace(oldline,newline,1)
            changes.append(dict(file=p.name,locus=anchor,kind='heading',before=oldline,after=newline,reason=reason))
    if stem=='01-foundations':
        start=text.index('The variance follows directly from the first two factorial moments.')
        end=text.index('\n\nThe count variance grows with rate',start)
        span=text[start:end]
        wrapped='::: {.publisher-clarification-note .publisher-fold-always title="Derivation: why a Poisson count has variance equal to its mean"}\n\n'+span+'\n\n:::'
        text=text[:start]+wrapped+text[end:]
        changes.append(dict(file=p.name,locus='sec:FOUNDATIONS-POISSON / original lines 44-50',kind='fold',before=span,after=wrapped,reason='Mean and variance are already visible. This proof checks those identities without supplying a later prerequisite.'))
        folds.append(dict(file=p.name,section='sec:FOUNDATIONS-POISSON',title='Derivation: why a Poisson count has variance equal to its mean',visible_premise='Constant-rate Poisson law and lambda=r*Delta t, with dimensionless expected count.',visible_result='E[K]=lambda and Var(K)=lambda, immediately before the fold.',visible_conditions='Constant rate, stated count interval and distribution.',hidden_exact_span=span,hidden_sha256=H(span),later_uses='Relative standard deviation, silent-cell example and pooled population counts; Chapter 2 uses conditional Poisson covariance.',closed_path='All uses need the visible distribution and moments, not the factorial-moment proof. No definitions, figures, IDs or typed blocks enter the fold.'))
    else:
        # Separate first definitions and the density result from its optional proof.
        start=text.index('Let $p(\\theta,t)$ be the density')
        eqstart=text.index('$$\n\\frac{\\partial p}{\\partial t}',start)
        oldintro=text[start:eqstart]
        split='To pass from random increments to a density equation, choose any smooth function'
        premise,proof=oldintro.split(split,1)
        proof=split+proof
        oldending='Because the resulting identity holds for every such smooth $F$, the density obeys the [**Fokker Planck equation**]{.definition-term custom-style="Definition Term"}:\n\n'
        newending='Because the resulting identity holds for every such smooth $F$, it gives the Fokker Planck equation shown above.'
        assert proof.endswith(oldending)
        proof=proof[:-len(oldending)]+newending
        newintro=premise.strip()+' In the zero-drift diffusion approximation, this density evolves according to the [**Fokker Planck equation**]{.definition-term custom-style="Definition Term"}:\n\n'
        text=text[:start]+newintro+text[eqstart:]
        insert=text.index('\n\nWhen $D$ varies with state,')
        wrapped='::: {.publisher-clarification-note .publisher-fold-always title="Derivation: from random increments to the memory density equation"}\n\n'+proof+'\n\n:::'
        text=text[:insert]+'\n\n'+wrapped+text[insert:]
        changes.append(dict(file=p.name,locus='sec:MEMORY-LONG-TIME / original lines 271-289',kind='move-proof-with-bridge',before=oldintro,after_visible=newintro,after_moved=wrapped,destination='After the line/ring figure interpretation, before the variable-D moments.',reason='The visible path teaches the density and its equation before the optional proof. Itô, Fokker Planck and Dirac delta first definitions stay visible. The proof remains complete, with only its final reference changed for the new position.'))
        folds.append(dict(file=p.name,section='sec:MEMORY-LONG-TIME',title='Derivation: from random increments to the memory density equation',visible_premise='p(theta,t) is a trial density initialized at Theta; Itô evaluates the noise coefficient at the beginning of each increment.',visible_result='The zero-drift Fokker Planck equation and point-mass initial condition precede the proof, followed by Gaussian line and wrapped-ring interpretations.',visible_conditions='Zero-drift diffusion approximation, constant D and unbounded line for the Gaussian; the ring wrapping and error convention remain visible. The variable-D moment paragraph separately retains its vanishing-boundary-term condition.',hidden_exact_span=proof,hidden_sha256=H(proof),later_uses='Gaussian spreading and wrapped-ring error, then dE[theta]/dt and dVar(theta)/dt identities. Chapter 3 uses the constant-D Brownian model taught in Chapter 1.',closed_path='All needed equations, meanings, limits and figures are visible. The optional smooth-test-function/Taylor/integration-by-parts calculation only verifies the density equation. Its local compact-support or boundary-term premise remains inside its own proof. No main heading, first-definition span, typed block or image is hidden.'))
    out=OUT/p.name
    out.write_text(text,encoding='utf-8')
    yp=p.with_suffix('.yaml')
    original_yaml=yp.read_text(encoding='utf-8')
    y=yaml.safe_load(original_yaml)
    original_blocks=json.dumps(y['blocks'],sort_keys=True,ensure_ascii=False)
    byid={a:(old,new,reason) for a,old,new,reason in decisions}
    y['title']=byid[y['chapter_id']][1]
    for sec in y['section_list']:
        sec['title']=byid[sec['id']][1]
        # Existing summaries remain accurate because section openings remain intact.
    proposed_yaml=yaml.safe_dump(y,allow_unicode=True,sort_keys=False,width=100)
    assert json.dumps(yaml.safe_load(proposed_yaml)['blocks'],sort_keys=True,ensure_ascii=False)==original_blocks
    (OUT/yp.name).write_text(proposed_yaml,encoding='utf-8')
    changes.append(dict(file=yp.name,locus='title and section_list titles',kind='sidecar',before=original_yaml,after=proposed_yaml,reason='Match the Markdown heading decisions. Existing section summaries still describe unchanged openings. All typed block objects preserved exactly.'))

checks=[]
for stem,source in sources.items():
    proposed=(OUT/(stem+'.md')).read_text(encoding='utf-8')
    assert re.findall(r'\{#([^}]+)\}',source)==re.findall(r'\{#([^}]+)\}',proposed)
    assert re.findall(r'\{\{block:.*?\}\}',source)==re.findall(r'\{\{block:.*?\}\}',proposed)
    assert re.findall(r'\]\((.*?)\)',source)==re.findall(r'\]\((.*?)\)',proposed)
    assert sorted(re.findall(r'\$\$.*?\$\$',source,re.S))==sorted(re.findall(r'\$\$.*?\$\$',proposed,re.S))
    assert sorted(re.findall(r'\[\*\*.*?\*\*\]\{\.definition-term.*?\}',source))==sorted(re.findall(r'\[\*\*.*?\*\*\]\{\.definition-term.*?\}',proposed))
    for inside in re.findall(r'::: \{[^\n]*publisher-fold-always[^\n]*\}\n(.*?)\n:::',proposed,re.S):
        assert not re.search(r'^#|\{\{block:|\.definition-term|<img|!\[|publisher-fold-always',inside,re.M)
    checks.append(dict(file=stem,source_sha256=H(source),proposed_sha256=H(proposed),headings_ids='same order',blocks='same order',links='same order',display_math='same exact expressions, order changed only by recorded proof move',definition_spans='same exact set, all visible',original_prose='preserved except individually recorded proof-ending bridge',folds=proposed.count('.publisher-fold-always')))
    diff=''.join(difflib.unified_diff(source.splitlines(True),proposed.splitlines(True),fromfile='baseline/'+stem+'.md',tofile='proposed/'+stem+'.md'))
    (GROUP/(stem+'.diff')).write_text(diff,encoding='utf-8')

(GROUP/'changes.json').write_text(json.dumps(dict(timestamp=now(),status='author draft; independent review pending',changes=changes),ensure_ascii=False,indent=2),encoding='utf-8')
(GROUP/'title-decisions.json').write_text(json.dumps({stem:[dict(id=a,old=old,new=new,decision='retain' if old==new else 'change',contribution=support,support=reason) for a,old,new,reason in decisions for support in [reason]] for stem,decisions in titles.items()},ensure_ascii=False,indent=2),encoding='utf-8')
(GROUP/'fold-decisions.json').write_text(json.dumps(dict(accepted_candidates=folds,retained_visible=[dict(section='sec:FOUNDATIONS-DIFFUSION',span='Brownian covariance proof and 2D min(s,t) result',reason='Chapter 3 needs the path-covariance reasoning for observation error. Keep the short proof connected to its result.'),dict(section='sec:MEMORY-DIFFUSION',span='Multiple-coordinate diffusion tensor',reason='The first definition must remain visible; its matrix formula also teaches why independent cell noise can couple represented coordinates.'),dict(section='sec:MEMORY-LINEARIZATION',span='Left/right vector construction and tilted-flow example',reason='This is the chapter mechanism and needed for Chapter 3 information-bound reasoning.'),dict(section='sec:MEMORY-SYMMETRIC',span='Symmetric-weight derivation and inhibition example',reason='The normalization and squared numerator prepare the next chapter and make the source discrepancy checkable.'),dict(section='sec:MEMORY-LONG-TIME',span='Variable-D moment calculation and mutual-excitation example',reason='This shows that varying D need not curve variance; hiding it would leave the section title and long-time claim less well explained.')]),ensure_ascii=False,indent=2),encoding='utf-8')
(GROUP/'preservation-checks.json').write_text(json.dumps(dict(timestamp=now(),checks=checks,limits='Source checks do not establish teaching quality or rendered fidelity. No new arithmetic or scientific findings were introduced.'),ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(dict(timestamp=now(),outputs=4,changed_headings=sum(old!=new for ds in titles.values() for _,old,new,_ in ds),folds=len(folds),checks='passed'),indent=2))
