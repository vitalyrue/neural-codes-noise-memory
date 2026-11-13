import json, re, hashlib
from pathlib import Path
from datetime import datetime
import yaml
base=Path(r'C:/dev/clsc/burak-papers/guide')
out=base/'verification/teaching-alignment-20261029'
p=json.loads((out/'memory-input.json').read_text(encoding='utf8'))
vale=json.loads((out/'memory-vale-input.json').read_text(encoding='utf8'))
errors=[x for x in vale if x['severity']=='error']
assert len(errors)==256
stage1=json.loads((out/'memory-stage1.json').read_text(encoding='utf8'))
edits=[]; edit_by_loc={}; extra=[]; units={}; decisions={}
def unit_id(stem,line):
    source='content/chapters/'+stem+'.md'
    candidates=[(min([z['line'] for z in v['paragraphs']] or [0]),k) for k,v in p['units'].items() if v['source']==source]
    return max((x for x in candidates if x[0]<=line),default=min(candidates))[1]
def edit(stem,line,changes,reason,category='sentence structure'):
    source='content/chapters/'+stem+'.md'; original=(base/source).read_text(encoding='utf8').splitlines()[line-1]
    new=original
    for old,replacement in changes:
        assert new.count(old)==1,(stem,line,old,new)
        new=new.replace(old,replacement,1)
    assert new!=original
    eid='ML-'+str(len(edits)+1).zfill(3)
    item={'id':eid,'source':source,'line':line,'original':original,'replacement':new,'reason':reason,'category':category,
          'affected_unit_ids':[unit_id(stem,line)],'status':'proposed; not applied'}
    edits.append(item);edit_by_loc[(stem,line)]=item
    return eid
def full(stem,line,replacement,reason,category='sentence contribution'):
    original=(base/'content/chapters'/f'{stem}.md').read_text(encoding='utf8').splitlines()[line-1]
    return edit(stem,line,[(original,replacement)],reason,category)

# Each edit is selected after reading that paragraph and its neighboring passage.
edit('01-foundations',88,[('evolving state','changing state')],'Changing says exactly what the rates depend on; evolving supplies no additional precision. The conditional-independence qualification is retained.','plain wording')
edit('01-foundations',93,[(']{.definition-explanation}; its value',']{.definition-explanation}. Its value')],'The definition and its dependence on interval length are separate statements. Keep both and use a full stop.')
edit('01-foundations',99,[('firing together; their spikes','firing together. Their spikes')],'Separate common changes in neural firing from the spikes acting on muscles. Both steps remain in causal order.')
full('01-foundations',101,'[Covariance asks which recorded changes occur together. Displacement statistics ask how far the eye moves and how that movement grows with elapsed time.]{.key-statement} Neither measurement by itself identifies the neural circuit responsible.','The count-first announcement adds no premise. State the two questions directly and retain the important limit on circuit identification.')
edit('01-foundations',103,[('private noise; it does not mean','private noise. It does not mean')],'The model-comparison role and the warning against a single-cell causal interpretation each deserve a sentence.')
edit('01-foundations',115,[('degrees squared; in general','degrees squared. In general')],'Keep the concrete units and the general units rule in separate sentences.')
edit('01-foundations',127,[('moments exist; zero covariance','moments exist. Zero covariance')],'Preserve both directions of the dependence distinction while separating them into sentences.')
edit('01-foundations',129,[('the dimensionless gains $g_X,g_Y$ convert its effect into each recording','the dimensionless [**gain**]{.definition-term custom-style="Definition Term"}s $g_X,g_Y$ multiply its contribution in each recording')],'This is the first teaching of gain in the reading path. Name its multiplication role and mark the singular base once. The later eye marker must be removed in coordination.','first-definition placement')
edit('01-foundations',136,[("assumptions; it is not the paper's full inference model.","assumptions. It is not the paper's full inference model.")],'The example explains calibration but must not be mistaken for the source inference model. Keep that qualification as its own sentence.')
edit('01-foundations',178,[('coding context; it is not evidence','coding context. It is not evidence')],'The later anatomy source and the source-date limit are distinct statements, not a citation-list separator.')

edit('01b-persistence',13,[('coordinate; a ring','coordinate. A ring')],'The line and ring are separate examples of coordinate shape; no semicolon is needed.')
edit('01b-persistence',15,[("unchanged; the model's feedback","unchanged. The model's feedback"),('explicit; it is not','explicit. It is not')],'Separate the invariant difference from the corrective feedback and keep the initial not-fitted qualification where the teaching model is introduced.')
edit('01b-persistence',49,[(r'$2k$; changing $k$',r'$2k$. Changing $k$')],'The controlled algebraic comparison and the possible effect of changing a real circuit are different claims; keep the caveat intact.')
edit('01b-persistence',62,[('This construction illustrates the geometry; it is not a fit to eye-neuron recordings. ',''),('the direction that survives','the lasting change')],'The first sentence repeats the explicit illustrative/not-fitted setup at lines15 and21. Deleting it preserves the novel general-network caveat. Lasting change states the object directly.','deletion and plain wording')
full('01b-persistence',74,'- Increments are independent.','These are independent assumptions rather than clauses of a single prose sentence. Use a complete bullet sentence.')
full('01b-persistence',75,'- Each increment has mean zero.','Give the zero-mean assumption a complete bullet sentence, retaining its distinct role.')
full('01b-persistence',76,r'- Each increment has variance $2D\Delta t$, where $D$ has units coordinate squared per time.','Capitalize the third complete assumption to match the repaired adjacent bullets; no mathematical change.')
edit('01b-persistence',114,[(' These are teaching values, not a new estimate from either monkey.','')],'The paragraph already says Take an illustrative coefficient, and the figure caption also identifies chosen teaching values. The final denial adds no needed distinction and refers ahead to monkeys.','deletion')
edit('01b-persistence',124,[('must therefore account for systematic drift separately','must account separately for [**systematic drift**]{.definition-term custom-style="Definition Term"}, a nonzero mean velocity')],'The preceding constant-bias example already teaches the concept here. Mark and briefly name its exact meaning now; remove the later first-definition marker in the drift chapter.','first-definition placement')
edit('01b-persistence',126,[('motion; exact displacement scales','motion. Exact displacement scales')],'A path shows realized motion, while the scale shows trial spread. Keep both purposes in separate sentences.')
edit('01b-persistence',134,[('A single path can turn back toward zero even while the root mean squared displacement grows. ', '')],'The first sentence repeats line106 and the caption warning that RMS is not a path boundary. Keep the bias-versus-square-root comparison that interprets this figure.','deletion')
edit('01b-persistence',171,[('questions; they do not establish a single circuit','questions. They do not establish one circuit')],'Keep the limit on combining the three schematics, using two sentences and one in its literal counting sense.')

edit('02-memory-dynamics',3,[('The important question is whether the activity pattern stays in the right place, not just whether activity continues. ','')],'The immediately preceding key sentence already says continued firing can lose the stored value. The removed sentence restates it with an undefined right place. The following continuous-set model now directly answers the problem.','deletion')
edit('02-memory-dynamics',5,[('The following chapter asks how this local prediction extends to longer delays.','The following chapter extends this local prediction to longer delays.')],'The chapter transition is useful, but its function can be stated directly without attributing a question to a chapter.','plain wording')
edit('02-memory-dynamics',7,[('find the passage; the PDFs','find the passage. The PDFs')],'Keep the locator instruction and the absence of numbered lines as separate reference statements.')
edit('02-memory-dynamics',13,[('new firing rates; the resulting spikes','new firing rates. The resulting spikes')],'The recurrent cycle has two physical steps, rates determining new spikes and spikes renewing activation. A sentence break makes the steps easier to follow.')
edit('02-memory-dynamics',50,[("input units; it is not specified", "input units. It is not specified")],'Preserve the important distinction between a model input and a measured membrane voltage; a full stop separates it from the units statement.')
edit('02-memory-dynamics',95,[('the one change that survives:','the lasting change:')],'Lasting change is the concrete retained coordinate shift; the phrase does not need a survival metaphor. The spectral and small-perturbation assumptions remain.','plain wording')
full('02-memory-dynamics',178,'As $y$ decays, $x$ changes by one. The left vector extracts that lasting shift.','Use mathematical formatting for the variables and separate the observed example result from the vector interpretation.')
edit('02-memory-dynamics',184,[("outgoing synaptic activation; the circuit's", "outgoing synaptic activation. The circuit's")],'Separate the spike disturbance from the return-flow calculation, preserving which object each mechanism acts on.')
edit('02-memory-dynamics',222,[('individual coordinates; its other entries','individual coordinates. Its other entries')],'Diagonal and off-diagonal entries have different meanings. Keep each as a sentence with the same exact tensor terminology.')
edit('02-memory-dynamics',259,[('in the numerator; the projection calculation','in the numerator. The projection calculation')],'The printed omission and the two checks supporting the correction should be separate sentences. The source qualification remains.')
full('02-memory-dynamics',261,'- Symmetric weights.','A listed mathematical assumption should be a separate capitalized item with a full stop.')
full('02-memory-dynamics',262,'- A stable continuous family.','Keep the attractor assumption separate from connectivity and noise assumptions.')
full('02-memory-dynamics',263,'- The noise assumptions already introduced.','Match the repaired assumption-list punctuation without changing its scope.')
edit('02-memory-dynamics',284,[('would be impossible; a physical implementation','would be impossible. A physical implementation')],'The impossible negative rate and the required boundary modification are a reason and consequence. Sentence separation keeps both.')

edit('02b-memory-long-delays',13,[(r'state-dependent $D$; constant $D$',r'state-dependent $D$. Constant $D$')],'The general density calculation precedes its constant-D specialization. Keep this sequence without a semicolon.')
full('02b-memory-long-delays',70,r'As the wrapped density approaches uniform, its mean squared error approaches $\pi^2/3$. The unbounded line error keeps growing.','Identify the mathematical objects rather than relying on upper/below layout, and separate the two error laws.')
edit('02b-memory-long-delays',98,[('a curved variance versus time graph','a nonlinear increase of variance with time')],'The result concerns whether variance is linear in time, not a visual graph feature. Nonlinear is the exact familiar mathematical alternative to linear.','plain wording')
edit('02b-memory-long-delays',113,[('[**systematic drift**]{.definition-term custom-style="Definition Term"}','systematic drift')],'Systematic drift is already taught through the constant-bias example; its blue first-teaching mark moves to Persistence line124. Retain this model-specific definition of mean velocity along the attractor.','first-definition placement')
edit('02b-memory-long-delays',119,[('cancel the mean drift; they cannot','cancel the mean drift. They cannot')],'Preserve the essential mean-versus-random-increment distinction in two sentences.')
edit('02b-memory-long-delays',121,[(')); it does not prove',')). It does not prove')],'The source discusses an extension but does not prove a universal result. The citation ends the first sentence; the qualification starts the next.')
edit('02b-memory-long-delays',132,[('relates it to diffusion; the [readout chapter]','relates it to diffusion. The [readout chapter]')],'Keep the useful two-chapter handoff while making each chapter contribution a sentence.')
edit('02b-memory-long-delays',143,[('The curve describes rates; the marks are particular random spike events.','The curve describes rates. The marks show individual spikes.')],'The visual distinction is expected rate versus realized spikes. Individual spikes is sufficient and removes an unnecessary modifier and semicolon.')
edit('02b-memory-long-delays',148,[('longer intervals; its flattening','longer intervals. Its flattening')],'The observation interval and the reason for flattening are separate claims. Keep the wrapping/noise distinction.')
edit('02b-memory-long-delays',150,[('opposite directions; their difference','opposite directions. Their difference')],'Separate opposing rate changes from what the difference represents; preserve the simulation-versus-animal limit.')
edit('02b-memory-long-delays',167,[('in the supplied PDF; no author correction','in the supplied PDF. No author correction')],'This is a prose qualification after the bibliographic locators, not a citation-list separator. Preserve it as a new sentence.')
edit('02b-memory-long-delays',171,[("linear algebra extension; the paper's", "linear algebra extension. The paper's")],'Keep the distinction between a direct covariance projection and an unproved general conjecture in separate sentences.')

edit('03-memory-information',64,[('efficient estimation can approach the bound','a suitable estimator can approach the bound')],'Efficient is an unexplained technical estimator property here. The direct statement preserves the weak-noise/local-Gaussian limit without requiring that additional term.','plain wording')
edit('03-memory-information',113,[('$D$ and $J$; it is not','$D$ and $J$. It is not')],'Keep the exact assumptions and the limit of universality as separate sentences.')
edit('03-memory-information',139,[('supplies a counterexample to the unrestricted converse','shows why equality does not require an exponential transfer rule')],'The exact claim at issue can be stated directly without asking the reader to interpret unrestricted converse. The counterexample calculations remain unchanged.','plain wording')
edit('03-memory-information',147,[('A converse that forces an exponential rule needs additional restrictions linking the participating input values across cells and states.','To conclude that equality forces an exponential rule, we need additional restrictions linking the participating input values across cells and states.'),("This qualification concerns the source's claimed converse, while leaving the information–diffusion inequality intact.","This qualification concerns the source's claim that equality requires an exponential rule. The information–diffusion inequality remains unchanged.")],'Name the disputed implication in ordinary words, while retaining its quantifier and the distinction from the unchanged inequality.','plain wording')

edit('03b-memory-readout',5,[('why simply waiting can become harmful','why waiting can become harmful')],'Simply contributes no condition or comparison; equal weighting is the actual cause already stated.','plain wording')
edit('03b-memory-readout',7,[('at the recall cue; the observation interval','at the recall cue. The observation interval')],'The two intervals have different roles and are easiest to identify in separate sentences.')
edit('03b-memory-readout',11,[('The observer now wants the original value','The observer must estimate the original value'),(' Even perfect knowledge of the state $\\theta(T)$ cannot recover its particular earlier random displacements.','')],'State the estimation task directly. The final sentence repeats the chapter opening at line3; removing it keeps the target, access restriction and stored motion.','deletion and plain wording')
edit('03b-memory-readout',25,[("bin's population spikes; it is not", "bin's population spikes. It is not")],'The statistical summary and the warning against treating it as another physical coordinate are both needed, but do not need a semicolon.')
edit('03b-memory-readout',35,[(r'at every $x$; denote it by',r'at every $x$. Denote it by')],'The equality of conditional variances is a conclusion; introducing its notation is a separate step.')
edit('03b-memory-readout',46,[('readout model; state dependence','readout model. State dependence')],'Keep the model assumptions separate from the cases requiring a changed calculation.')
full('03b-memory-readout',56,'','This paragraph repeats the opening and the setup conclusion without adding a condition or a step. The timeline and preceding variance decomposition already separate storage from cue-state readout. The next equal-weight section states its own task.','deletion')
edit('03b-memory-readout',113,[('for an observer; the readout calculation','for an observer. The readout calculation')],'Retain the distinction between an ideal inference benchmark and an implemented neural circuit, with a full stop.')
full('03b-memory-readout',142,'With no observations, precision starts at zero. The term $J$ adds information from new observations. The term $2DP^2$ reduces that gain because later observations are separated from the cue state by diffusion.','Name which observations add information and why diffusion weakens it. This preserves the Riccati interpretation without an unexplained image of carrying information backward.','plain mechanism wording')
edit('03b-memory-readout',220,[('fraction of the information; a fraction of neurons','fraction of the information. A fraction of neurons')],'Keep the distinction between information fraction and arbitrary selection in separate sentences.')
edit('03b-memory-readout',228,[('Longer observation can reduce the readout cost; it cannot undo the random displacement during the delay.','Limited access leaves the storage error unchanged but increases the time and uncertainty involved in reading the cue state.')],'The old last sentence repeats the chapter opening. The replacement interprets this example’s full-versus-partial comparison while keeping the same stored variance.','example conclusion')
full('03b-memory-readout',270,'**Interpretation.** The sum of the two time constants replaces $\\tau$. When one time constant is much larger, it supplies most of that sum. This result belongs to the two stage model and noise placement just described. The paper does not prove that arbitrary collections of biological time constants can always be added.[^p1-two-times]','Replace very different with the concrete relation that makes one term dominate the sum, and preserve the model-specific limitation in a separate sentence.')
edit('03b-memory-readout',320,[(r'$2D(T+\tau)$; SI Eq. S83 likewise',r'$2D(T+\tau)$. SI Eq. S83')],'The main and supplement each make a source claim. State them separately and remove likewise, which adds no step before the algebra.')
edit('03b-memory-readout',341,[('long observation; it does not','long observation. It does not')],'The variance limit and absence of a deterministic restoring term are distinct necessary conclusions. Preserve both as sentences.')
edit('03b-memory-readout',347,[('cross time covariance terms','covariances between different times')],'The latter names the paired observations directly; no mathematical detail is lost.','plain wording')
edit('03b-memory-readout',349,[('solution S73; the recursion','solution S73. The recursion')],'Separate the source sign mismatch from the independently obtained final result.')
edit('03b-memory-readout',355,[('directly from S84; its rate decay','directly from S84. Its rate decay')],'Keep the equation source and its required negative decay sign as separate statements.')
edit('03b-memory-readout',359,[('supplied supplement; the corresponding results','supplied supplement. The corresponding results')],'This prose explains a stale locator rather than separating citations. Preserve both facts with a sentence break.')

def meta(stem,kind,ident,field,changes,reason):
    source='content/chapters/'+stem+'.yaml';d=yaml.safe_load((base/source).read_text(encoding='utf8'))
    obj=next(z for z in d[kind] if z['id']==ident);original=obj[field];new=original
    for a,b in changes:
        assert new.count(a)==1,(ident,field,a);new=new.replace(a,b,1)
    affected=next(k for k in p['units'] if k.endswith('::'+(ident if kind=='section_list' else obj['placement'])))
    eid='ML-'+str(len(edits)+1).zfill(3)
    edits.append({'id':eid,'source':source,'location':kind+'[id='+ident+'].'+field,
      'original':original,'replacement':new,'reason':reason,'category':'reader-facing metadata wording',
      'affected_unit_ids':[affected],'status':'proposed; not applied'})
    return eid

meta('01-foundations','blocks','fig:FOUNDATIONS-POISSON-POPULATION','caption',[('20 Hz; their standard deviations','20 Hz. Their standard deviations')],'The matching means and unequal standard deviations are separate comparison facts.')
meta('01b-persistence','blocks','fig:FOUNDATIONS-ATTRACTOR','caption',[('deterministic recovery; the dashed arrow','deterministic recovery. The dashed arrow')],'Separate the meanings of the two arrow styles.')
meta('01b-persistence','blocks','fig:FOUNDATIONS-PAPER-MAP','caption',[('over time; place-field statistics','over time. Place-field statistics')],'The temporal and spatial problems are distinct; a full stop makes the comparison direct.')
meta('01b-persistence','blocks','fig:FOUNDATIONS-DIFFUSION-BIAS','caption',[('at zero; the dashed envelope','at zero. The dashed envelope')],'Separate path initialization from the meaning of the RMS envelope.')
meta('01b-persistence','blocks','fig:FOUNDATIONS-DIFFUSION-BIAS','alt',[('time; some paths','time. Some paths')],'The scale and the fact that paths may cross it are separate statements.')
meta('02-memory-dynamics','section_list','sec:MEMORY-SPIKES','summary',[('new firing rates; the resulting spikes','new firing rates. The resulting spikes')],'Keep the navigation summary aligned with the repaired two-step recurrent explanation.')
meta('02-memory-dynamics','section_list','sec:MEMORY-LINEARIZATION','summary',[('the one change that survives:','the lasting change:')],'Mirror the main text’s direct name for the retained coordinate change.')
meta('02-memory-dynamics','section_list','sec:MEMORY-DIFFUSION','summary',[("outgoing synaptic activation; the circuit's", "outgoing synaptic activation. The circuit's")],'Separate spike disturbance and return-flow effect in the navigation text too.')
meta('02-memory-dynamics','blocks','fig:MEMORY-TILTED-DECAY','caption',[('$(1,0)$; successive','$(1,0)$. Successive'),('S10–S16; it is not','S10–S16. It is not')],'Separate endpoint, time-mark behavior and distinction from a paper simulation while preserving the citation range.')
meta('02-memory-dynamics','blocks','fig:MEMORY-TILTED-DECAY','alt',[('one zero; the left vector','one zero. The left vector')],'Give the tangent and extraction vector separate descriptions.')
meta('02-memory-dynamics','blocks','fig:MEMORY-INHIBITION-RATES','caption',[('excluded boundaries; the linear interior','excluded boundaries. The linear interior')],'Retain the positive-rate limit and the unmodeled boundary behavior in separate sentences.')
meta('02b-memory-long-delays','blocks','fig:MEMORY-LINE-RING','caption',[('error 2Dt; reporting angular error','error 2Dt. Reporting angular error')],'The line and wrapped-error results are separate comparisons at the same D.')
meta('02b-memory-long-delays','blocks','fig:PAPER-MEMORY-1','caption',[('memory coordinate; the second panel','memory coordinate. The second panel'),('(2012); exact artwork excerpt.','(2012), reproduced as an exact artwork excerpt.')],'Separate the two panel roles and use a complete source-identity phrase. Exact artwork acceptance remains deferred.')
meta('02b-memory-long-delays','blocks','fig:PAPER-MEMORY-2','caption',[('(2012); exact artwork excerpt.','(2012), reproduced as an exact artwork excerpt.')],'Use a complete source-identity phrase, retaining the same unverified artwork-fidelity assertion for later acceptance.')
meta('02b-memory-long-delays','blocks','fig:PAPER-MEMORY-S1','caption',[('(2012); exact artwork excerpt.','(2012), reproduced as an exact artwork excerpt.')],'Use a complete source-identity phrase; do not change its source claim.')
meta('02b-memory-long-delays','blocks','fig:PAPER-MEMORY-S1','alt',[('state trajectory; panel B','state trajectory. Panel B')],'Separate the trajectory panel from the variance comparison panel.')
meta('03-memory-information','blocks','fig:MEMORY-TUNING-INFORMATION','alt',[('the flanks; the higher baseline','the flanks. The higher baseline')],'Separate the shared shape property and the effect of a larger denominator.')
meta('03b-memory-readout','section_list','sec:MEMORY-READOUT-SETUP','summary',[('The observer now wants the original value','The observer must estimate the original value'),(' Even perfect knowledge of the state $\\theta(T)$ cannot recover its particular earlier random displacements.','')],'Keep the summary aligned with the direct estimation task; the introductory text already states the lost-past-increments limit.')
meta('03b-memory-readout','section_list','sec:MEMORY-IDEAL','summary',[('for an observer; the readout calculation','for an observer. The readout calculation')],'Keep the ideal-observer/neural-implementation distinction in separate sentences.')
meta('03b-memory-readout','blocks','fig:MEMORY-READOUT-TIMELINE','alt',[('x minus Theta; readout error','x minus Theta. Readout error')],'Define the two error terms separately while retaining their distinct targets.')
meta('03b-memory-readout','blocks','fig:MEMORY-READOUT-CURVES','caption',[('variance of one; simple averaging','variance of one. Simple averaging')],'Separate ideal saturation from the equal-weight optimum.')
meta('03b-memory-readout','blocks','fig:PAPER-MEMORY-3','caption',[('(2012); exact artwork excerpt.','(2012), reproduced as an exact artwork excerpt.')],'Retain the source identity in a complete phrase; exact artwork matching remains deferred.')
meta('03b-memory-readout','blocks','fig:PAPER-MEMORY-3','alt',[('toward one; a dashed curve','toward one. A dashed curve'),('then rises; a vertical','then rises. A vertical')],'Describe the ideal curve, equal-weight curve and optimum marker as separate objects.')
meta('03b-memory-readout','blocks','fig:PAPER-MEMORY-S2','caption',[('(2012); exact artwork excerpt.','(2012), reproduced as an exact artwork excerpt.')],'Retain the source identity in a complete phrase with no new graphical assertion.')

def retain(indices,reason):
    for i in indices:
        x=errors[i]; assert x['id'] not in decisions,i
        decisions[x['id']]={'id':x['id'],'decision':'retain_exception','reason':reason,
          'source':x['source'],'line':x['line'],'rule':x['rule'],'match':x['match']}
def revise(indices):
    for i in indices:
        x=errors[i];stem=Path(x['source']).stem; e=edit_by_loc[(stem,x['line'])]
        assert x['id'] not in decisions,i
        decisions[x['id']]={'id':x['id'],'decision':'revise','reason':e['reason'],'edit_id':e['id'],
          'source':x['source'],'line':x['line'],'rule':x['rule'],'match':x['match']}

# Every index names one frozen Vale error, in the input's stable order. Grouped
# indices share the stated local passage, not a rule-wide automatic exemption.
revise([11,13,14,15,17,19,21,22,30,36,37,38,40,43,44,48,49,50,51,52,57,58,
 62,63,64,65,71,75,83,84,86,89,114,116,123,127,128,130,131,132,135,141,146,
 157,203,204,207,209,210,213,216,217,223,224,228,229,232,236,240,243,251])
retain([0,1],'The opening names exactly the three actual papers and their distinct scientific questions. Removing or changing the count/list merely to avoid a tricolon would hide the book scope without simplifying its meaning.')
retain([2],'20 Hz is an expectation, not periodic firing. The explicit 50ms contrast corrects the immediate and likely rate-versus-clock misunderstanding before the Poisson example.')
retain([3],'Carries information is the established meaning of population code, and the sentence names the concrete rate vector and represented θ. Replacing it with contains would not clarify that relationship.')
retain([4],'The immediately displayed vector could be mistaken for cells arranged in physical space. The neuron-identity contrast is needed here because physical spatial maps follow.')
retain([5],'Therefore connects finite sampling, smoothing and thresholds to the estimated rate map. It is a consequence of the just-defined count/time estimator, not a topic change.')
retain([6],'Likewise identifies the repeated summation method for the second factorial moment. It prevents λ² from looking like an unsupported additional moment identity.')
retain([7],'This is why connects the inverse-square-root relative SD to the gain from independent observations. The causal link is the lesson of the calculation.')
retain([8],'Therefore ties the .368 zero-count probability to the otherwise surprising silent interval at a positive rate.')
retain([9],'The two count distributions refers to the explicitly computed one-cell and twenty-cell distributions and announces their common per-cell axis, not a decorative numbered list.')
retain([10],'Therefore explains why independence in a recurrent network must be conditional on its changing state. That restriction is essential to the result.')
retain([12],'The two measurements are CV and Fano factor, genuinely different statistics needed later. The short list preserves their contrast and does not introduce an arbitrary rhetorical count.')
retain([16],'Neither measurement identifies the circuit is a necessary limit on inference from covariance or displacement. The adjacent rewrite retains that negative claim because it prevents a causal overreading.')
retain([18],'The predicted displacement is computed from a recording rather than delivered to a muscle. That difference is essential to understanding the eye study’s observation model.')
retain([20],'Zero covariance is the exact statistical quantity. The rule mistakes zero for a gratuitous negation; changing it would change the mathematics.')
retain([23],'Stronger random movement, directional bias, or both enumerates the complete possibilities in MSD=variance+mean². Varying the count would weaken the interpretation.')
retain([24],'The bold list label identifies the physical cause for this bullet, and the following sentence explains its effect on mean and squared bias. It is a useful parallel comparison, not a detached label.')
retain([25],'Thus derives why added measurement variance can raise the observed MSD without physical movement. The measured/physical distinction requires that connection.')
retain([26,27],'The en dashes in the eye-paper footnote mark source ranges Figs1–2 and Methods Eqs2–7. They are precise locators, not prose em dashes.')
retain([28],'1110–1120 is the published page range of the place-field article. The en dash belongs to the citation.')
retain([29],'Figs1–2 identifies the anatomical source range. Retain the exact locator while the separate prose semicolon is repaired.')
retain([31,32],'The bibliography page range17645–17650 and equation range7–10 are source locators. They do not function as sentence punctuation.')
retain([33],'Stays fixed describes the assumed spatial function remaining unchanged within a cell/environment. It is a literal model condition, contrasted with temporal noise.')
retain([34,35],'Keeping the pattern stable is the actual dynamical property under discussion. Therefore links the preceding wrong-angle disturbance to the difference between stable activity and accurate memory.')
retain([39],'Teaching model describes the author’s purpose for the constructed example. It does not attribute cognition to the model.')
retain([41],'The two changes are the specific(+3,+3) and(+3,−3) perturbations just computed. The count is needed to connect the figure’s two directions to the examples.')
retain([42],'The dashed arrow is imposed noise, whereas the solid arrow is deterministic return flow. This contrast prevents confusing the essential two physical operations.')
retain([45],'Independent retained increments are not independent full spike trains. This is a real modeling distinction already motivated by recurrence in Foundations.')
retain([46],'A single memory trajectory distinguishes an individual realization from the distribution across trials. Single changes the object being described and is not an intensifier.')
retain([47],'Angular diffusion coefficient is the exact physical quantity with its units. Splitting or replacing that phrase would obscure which coefficient the numerical example sets.')
retain([53],'Therefore connects shared earlier increments to the non-independence of two observations of the same stored value. This is the premise needed for later readout covariance.')
retain([54],'For example introduces a concrete ring counterexample to unrestricted linear growth. The ring is immediately explained, so the connector has a specific purpose.')
retain([55],'Conversely switches from spatial maps failing to determine temporal drift to temporal drift failing to determine field shape. Both directions are scientifically different claims.')
retain([56],'The three questions refer to memory, eye drift and spatial map statistics already distinguished; the following schematic compares precisely those rows.')
retain([59,60],'The PNAS page range17645–17650 and SI section range I–III are citation locators in the memory footnote.')
retain([61],'The en dash1110–1120 is the published article page range, not prose punctuation.')
retain([66],'For example gives two concrete possible rate-input functions after the general transfer-function definition. It prevents the general function from remaining an unexplained symbol.')
retain([67],'Eqs7–9 is the source model range; keep that exact locator.')
retain([68],'Therefore connects the unit jump in s_j to the immediate W_ij input change. This is the explicit spike-to-recipient mechanism.')
retain([69],'In turn describes the recurrent sequence: the recipient’s new spikes then affect other cells. It is a causal stage rather than filler.')
retain([70],'Thus gathers the just-derived separate roles of weights, transfer function and τ. This one sentence explains how changing each parameter acts on the system.')
retain([72],'Thus introduces the conditional mean/covariance equations that follow from the stated Poisson increment law.')
retain([73],'S2–S5 is the supporting-information range for the weak-fluctuation construction. Preserve the locator.')
retain([74],'Therefore links the n/n mean and n/n² variance calculation to reducing fluctuations without changing mean dynamics.')
retain([76],'Therefore connects cancellation at a fixed point to the resulting linear stochastic equation. Without it the equation could read as a new model assumption.')
retain([77],'Thus identifies Ku=0 as the reason u is a right zero eigenvector. This is the definition at first use, not an ornamental transition.')
retain([78],'Left zero eigenvector is the exact linear-algebra term, explicitly defined by vᵀK=0 and normalized against u. Zero must not be removed.')
retain([79],'S12–S13 locates the source normalization and projection equations. The en dash is a mathematical source range.')
retain([80],'Consequently connects annihilation of decaying modes to the surviving projection u(vᵀδs). This is the inference being taught.')
retain([81,82],'The tilted two-variable example is the guide’s construction and does not claim to be an extra simulation in the source paper. Teaching example correctly attributes purpose to the author; the scope distinction is useful.')
retain([85],'S14–S15 identifies the projected diffusion equations in the source. Keep the range.')
retain([87],'The listed commonτ, stable family, weak-noise and independence conditions are actual assumptions. A three-part grammatical list is not grounds to alter them.')
retain([88],'Therefore states why Kᵀg′=0 determines the left-vector direction before its normalization. It links proof to formula.')
retain([90],'The guide’s independent check is not an author-confirmed correction. This source-status distinction is necessary when departing from the printed main formula.')
retain([91],'Although contrasts changing individual rates with their constant summed variability. That is the mathematical reason this example has constant D, not a defensive hedge.')
retain([92],'Therefore links constant summed Poisson variance to constant local diffusion. The conclusion does not follow from a rate changing alone.')
retain([93],'Fig2E–G is an exact panel range for the mutual-inhibition example, not sentence punctuation.')
retain([94],'The rate sum stays fixed literally describes the constant200/s curve and the algebra r1+r2=b/τ. It is not a figurative use of stays.')
retain([95,96],'The main-model footnote contains the article page range17645–17650 and model equation range7–9. Retain both locators.')
retain([97],'This semicolon separates main-paper and SI locator links in a bibliographic list. It is not an ordinary prose sentence join.')
retain([98,99],'10–11 and S2–S5 are equation ranges identifying the weak-fluctuation source passages.')
retain([100],'Teaching rewrite tells the reader that Brownian notation is the guide’s equivalent presentation of white-noise notation. It attributes no cognition to noise or a model.')
retain([101],'The semicolon separates distinct supporting-information locator links within a reference list, not two prose claims.')
retain([102],'S2–S5 is a precise source equation range for the replicated-population limit.')
retain([103,104,105],'S7–S10, S12–S13 and S14–S15 are the cited linearization/projection equation ranges. Preserve their source identity.')
retain([106],'The semicolon separates the SI S21 locator from the S22–S27 locator in a reference list. It is bibliographic punctuation.')
retain([107],'S22–S27 is the supporting-information range for multiple stored coordinates.')
retain([108,109],'17645–17650 and S16–S18 are the article and symmetric-formula source ranges.')
retain([110,111],'17645–17650 and Fig2E–G are the article and panel ranges for the mutual-inhibition source.')
retain([112],'The title’s nouns are the concrete mathematical objects: boundaries and drift alter memory error over long delays. The grammar is a complete causal statement, not an unexplained noun string.')
retain([113],'A boundary, angular wraparound and a region with a different D are three different ways local spreading stops determining long-time error. They are all used in the chapter; the list is necessary.')
retain([115],'Therefore connects the wrapped-Gaussian uniform limit to flattening despite unchanged local noise. It prevents misreading the plateau as reduced stochastic drive.')
retain([117],'θ changes from an angle to an activation coordinate in this example. The explicit contrast prevents unit and parameter misinterpretation.')
retain([118],'Firing rates is the literal neural quantity defined earlier. The detector mistakes the word firing for a metaphor.')
retain([119],'Hence connects increasing rates to increasing Poisson count variances. This depends on the specific noise law and is a real implication.')
retain([120],'Projection weights stay fixed means v=(1/2,1/2) is independent ofθ in this example. It states a checked mathematical condition.')
retain([121],'Giving the two identities names the result of taking second derivatives zero and two. The participle has a concrete mathematical antecedent and conclusion.')
retain([122],'Therefore links the generator identity dE[D]/dt=E[DD″] to the short-time variance expansion. It is an inference step.')
retain([124],'Meaning a nonzero mean velocity supplies the physical definition of systematic drift. The marker will move earlier, but this model-specific reminder remains useful.')
retain([125],'In addition distinguishes drift from deterministic weight mismatch from drift caused by state-dependent noise/nonlinear return flow. Those are different mechanisms.')
retain([126],'pp4–5 identifies the source section on systematic drift. The en dash is bibliographic.')
retain([129],'1B is a figure-panel identifier, not one byte or a numeric quantity with a unit. Do not insert a space.')
retain([133],'The dashed line is a lower bound rather than another fitted trajectory. That concrete figure-reading distinction is essential to understanding why a simulation can lie above it.')
retain([134],'The two rates are the explicitly displayed pair in the mutual-inhibition model. Counting the pair is not an artificial forecast.')
retain([136],'S28–S29 locates the source density equation and its assumptions.')
retain([137],'Teaching reconstruction describes the guide’s uniform-variance derivation, not a thinking mathematical object.')
retain([138],'S33–S37 locates the state-dependent diffusion calculation.')
retain([139],'The semicolon separates an equation locator from a figure locator in a bibliographic list. It is not joining prose sentences.')
retain([140],'S38–S41 is the exact source range in which the factor-two inconsistency is discussed.')
retain([142],'The semicolon separates two supporting-information links in the citation, not ordinary explanatory clauses.')
retain([143],'S19–S20 is the source equation range for the stochastic-convention comparison.')
retain([144],'The quoted words Our spiking model identify the exact beginning of a source paragraph. Moving the sentence period inside that quoted locator could imply it belongs to the source excerpt.')
retain([145],'17645–17650 is the published article page range.')
retain([147],'17645–17650 is the article page range in the Fig1 reference.')
retain([148],'17645–17650 is the article page range in the Fig2 reference.')
retain([149],'Spike information limits memory stability is the chapter’s actual directional relationship. Both quantities are established and the title states a consequence, not stacked labels.')
retain([150,152],'Particular network and particular circuit restrict the bound to the same model whose D and J were calculated. The qualifier prevents an invalid universal comparison across changed networks.')
retain([151],'What stays fixed is the literal controlled-variable condition in a parameter comparison. It has a precise mathematical role.')
retain([153],'The adjacent sentences give a formula’s per-cell contribution and its zero-slope consequence. Combining them only to vary rhythm would hide the inference; they do not repeat the same content.')
retain([154],'Two positive tuning curves is the actual pair differing only by a constant baseline. Their matched slopes are the controlled comparison, not a rhetorical list.')
retain([155],'Therefore applies Cauchy–Schwarz to the displayed vector norms and fixed dot product. This is the key proof step.')
retain([156],'Teaching reconstruction tells the reader the shorter proof is the guide’s equivalent derivation. It does not attribute cognition to the proof.')
retain([158],'Therefore connects v∝g′ and r′=φ′g′ to the equality condition across participating cells. It is the necessary algebraic implication.')
retain([159],'Therefore introduces the direct computed D and J of the linear counterexample. The selected prose rewrite preserves the mathematical connector.')
retain([160],'Information–diffusion inequality is the name of the relation between these two quantities. The en dash is neither an em dash nor a sentence interruption.')
retain([161],'The example’s coordinate is an activation difference rather than an angle. This distinction is needed for all following units and numeric values.')
retain([162],'Thus connects the displayed rates and slopes to the evaluated J and D. The numerical computation immediately follows.')
retain([163],'Therefore motivates matrices after explaining that one spike can affect several coordinates. Scalar bounds alone would miss shared directions.')
retain([164,165,166],'What a comparison holds fixed names controlled variables, the section’s central subject. It is a useful contribution heading and a literal mathematical comparison, not a vague capability or metaphor.')
retain([167],'Stays fixed refers to the explicit controlled quantities of a network comparison. Replacing the phrase is unnecessary.')
retain([168],'At the same time means changing a confounding property simultaneously with the parameter of interest. It is a real condition, not a hedge.')
retain([169],'Consequently connects numerator N and denominator N² to D∝1/N. The word marks a derived scaling rather than an assumed result.')
retain([170],'The controlled density/replication construction differs from adding arbitrary neurons with arbitrary weights. This limit is necessary to avoid a false biological scaling claim.')
retain([171],'Therefore connects a larger distance between fixed activation states to smaller coordinate displacement from one unit spike. It explains theτ^−2 scaling physically.')
retain([172],'Spike variance stays fixed is the controlled rate assumption; it is a literal condition required for the subsequentτ scaling.')
retain([173],'In contrast introduces a different fixed-activation comparison whose exponent isτ^−1. It prevents mistaking the two controlled calculations for a contradiction.')
retain([174],'Teaching reconstruction labels the guide’s expanded width calculation relative to the paper’s shorter discussion. No nonhuman intention is implied.')
retain([175],'The text cannot treat one tuning family’s power law as a universal result. The explicit qualification matters before the dimension-dependent conclusions.')
retain([176],'The two factors are exactly the integration-volume powerw^d and squared-slope powerw^−2. The list exposes the mechanism behind the exponent.')
retain([177],'Therefore combines those two powers into J∝w^(d−2), the result the next dimensional comparison needs.')
retain([178],'Reaches the diffusion lower bound is the usual exact meaning of attaining equality. The nearby sentence gives the bound’s quantities and distinguishes equality from optimizing over architectures.')
retain([179,180],'This is why links the matching sensory/internal tuning and simultaneous information optimum to the paper’s proposed combined circuit role. Removing it could make the biological suggestion look independent of those premises.')
retain([181],'The source suggestion and the empirical limit are distinct statements. Both are needed to prevent mathematical compatibility from being mistaken for localization of animal memory.')
retain([182],'Particular animal distinguishes a model’s compatible functions from a biological localization claim about an observed animal. It preserves the level of evidence.')
retain([183,184],'17645–17650 and2–4 are the article and main-result page ranges in the information footnote.')
retain([185],'9–10 is the SI page range for the information derivation.')
retain([186],'Teaching reconstruction identifies the guide’s proof of a source-invoked Cramér–Rao bound; it is an authorship/presentation statement.')
retain([187,188],'10–11 and S45–S49 are exact SI page and equation ranges for the scalar bound.')
retain([189],'S47–S51 is the equality-condition equation range; keep the source locator.')
retain([190,191],'10–12 and S52–S56 are the SI page/equation ranges for the multidimensional bound.')
retain([192],'Teaching reconstruction identifies the equivalent residual-matrix proof supplied here. It does not say the matrix thinks or teaches.')
retain([193],'17645–17650 is the article page range in the scaling reference.')
retain([194],'17645–17650 is the article page range in the width reference.')
retain([195],'Teaching derivations distinguishes the guide’s integral/resource calculations from an independent check of Zhang and Sejnowski. That source limit is needed.')
retain([196],'The semicolon separates source-location items in the colocation footnote, not prose claims. Preserve bibliographic punctuation.')
retain([197,198],'17645–17650 and4–5 identify the article and source discussion page ranges.')
retain([199],'The title names the real relationship: accuracy depends on observing a state that moves. How is followed by the concrete process being studied, not an empty heading template.')
retain([200],'Particular random displacements means the realized past increments, rather than their known distribution or mean. The modifier preserves the limitation’s exact meaning.')
retain([201],'θ,Θ and2Dt are the recurring coordinate, initial value and variance law. The parallel sentence is a compact notation recap needed before introducing T and L.')
retain([202],'The actual prose semicolon at this location is included in the proposed sentence repair; this row is handled by that edit.')
retain([205],'The Gaussian-fit sentence states a limit on taking short physical bins, distinct from the next sentence’s exactness within the mathematical model. The apparent staccato match is not redundant content.')
retain([206],'Therefore links translation invariance to equal readout variance at each x. This is the condition needed for the decomposition to use one function Vread(L).')
retain([208],'The two terms are precisely2DT andVread(L), whose different physical meanings the list explains. This is not an arbitrary numbered forecast.')
retain([211],'Therefore introduces the double integral after identifying its triangle and integrand. The conclusion is derived from the domain split.')
retain([212],'The two contributions are process error increasing with L and observation noise decreasing with L. Their opposing signs motivate the derivative and optimum.')
retain([214],'Therefore links adding transition variance to the reduced precision about an earlier state. That is the inference the backward recursion needs.')
retain([215],'Thus links new earliest-observation precision to the finite-bin recursion. This connects the physical observation step to its formula.')
retain([218],'Teaching reconstruction identifies the guide’s backward-precision derivation as equivalent to the source covariance calculation. The mathematical procedure is not attributed human cognition.')
retain([219],'S58–S75 is the source covariance derivation range. Keep the equation locator.')
retain([220],'Therefore states why matching small-L expansions makes the naive and ideal estimates agree through the written terms, not at all orders.')
retain([221],'Thus connects the inequality L*≤τ to the correct interpretation of the source’s cellular-time claim. The immediately following caveat preserves the asymptotic nature.')
retain([222],'Hence introduces the observed time and variance scales after substituting Jo=αJ while keeping D fixed. It marks the actual derivation.')
retain([225],'Dynamics carry a fluctuation into a lasting change refers to the explicit spike/return-flow transformation already derived. The sentence asks which time constant controls that transformation; no physical transport claim is implied.')
retain([226],'Left zero vector is the exact algebraic term for the normalized null direction of the block dynamics. Zero is essential.')
retain([227],'Consequently connects the s-block noise and normalized a vector to theτ+τm formula. It identifies the equation as derived, not assumed.')
retain([230],'Teaching reconstruction identifies the explicit-q formulation supplied by the guide to make units visible. It attributes the explanatory choice to the writer, not the equation.')
retain([231],'S94–S95 is the precise source equation range whose normalization is discussed.')
retain([233],'Thus draws the crucial at-most conclusion from the displayed inequality chain. Deleting its logical connection would make the source correction harder to follow.')
retain([234],'The first sentence defines the accumulated quantity and the next distinguishes readout duration from its lifetime. They are separate premises, not repeated short prose.')
retain([235],'Particular value names the fixed reference toward which a deterministic leak would pull. That differs from zero-mean diffusion and is needed to distinguish the mechanisms.')
retain([237],'S58–S63 is the SI range for the Gaussian readout model.')
retain([238,239],'15–16 and S76–S81 are page and equation ranges locating the naive-reader derivation.')
retain([241,242],'13–15 and S58–S75 are page and equation ranges locating the ideal-reader derivation.')
retain([244,245],'17645–17650 and S80–S81 are article and equation ranges in the readout-time reference.')
retain([246,247],'17–18 and S84–S92 locate the two-time-constant extension.')
retain([248,249],'S93–S95 and3–4 locate the Gaussian-noise subsection and related main discussion.')
retain([250],'17645–17650 is the article page range in the figure reference.')
retain([252],'S79–S81 is the corrected source equation range for the naive curve; preserve the exact locator.')
retain([253,254],'17645–17650 and4–6 are the article and main-equation ranges in the printed-bound reference.')
retain([255],'17645–17650 is the article page range in the integration-time reference.')

# The row at readout line7 is a real sentence join, not a retained exception.
x=errors[202];decisions.pop(x['id']);revise([202])
assert len(decisions)==256,sorted(set(range(256))-{i for i,x in enumerate(errors) if x['id'] in decisions})

# Two further term-placement checks arise from the connected read, not from Vale.
e=edit_by_loc[('02b-memory-long-delays',121)]
old='Calculating the corresponding Fisher information would require the matching joint likelihood.'
new='A matching calculation of information would need the probabilities of joint spike patterns.'
assert old in e['replacement'];e['replacement']=e['replacement'].replace(old,new,1)
e['reason']+=' Fisher information and likelihood are taught in the next chapter. This preview can state the needed joint-probability model directly without requiring those names yet.'
edit('02-memory-dynamics',265,[('translation symmetry,','[**translation symmetry**]{.definition-term custom-style="Definition Term"},')],'This sentence already gives the first teaching meaning of translation symmetry. Mark that occurrence and add its matching glossary entry. The later readout meaning of translation invariance remains distinct.','first-definition placement')
gsource='content/chapters/glossary.md';glines=(base/gsource).read_text(encoding='utf8').splitlines()
goriginal=next(x for x in glines if '**Translation invariance:**' in x)
edits.append({'id':'ML-'+str(len(edits)+1).zfill(3),'source':gsource,'line':glines.index(goriginal)+1,
 'original':goriginal,'replacement':'- [[**translation symmetry:**]{.definition-term custom-style="Definition Term"} Shifting an activity pattern along the represented coordinate leaves the network dynamics unchanged in form.]{.definition-explanation}\n'+goriginal,
 'reason':'The newly marked first teaching of translation symmetry needs a matching lookup entry. Keep it distinct from the model-specific readout translation invariance entry.',
 'category':'linked glossary definition','affected_unit_ids':['content/chapters/02-memory-dynamics.md::sec:MEMORY-SYMMETRIC'],'status':'proposed; not applied'})

def review(suffix,refs,deletion,terms,order,contribution,phrase,paraphrase,actor,obj,action,condition,verdict,reason):
    k=next(k for k in p['units'] if k.endswith(suffix))
    f=p['review_fields']
    wording=f'Phrase: {phrase} Paraphrase: {paraphrase} Actor: {actor} Object: {obj} Action: {action} Condition or consequence: {condition} Verdict: {verdict}. Replacement or retention reason: {reason}'
    unit_edits=[e['id'] for e in edits if k in e['affected_unit_ids']]
    sources=[k+'/'+r for r in refs.split()] if refs else [k]
    findings=[{'id':eid,'failed_check':next(e['category'] for e in edits if e['id']==eid),
       'proposed_edit_id':eid,'status':'open','passage_and_repair':'See proposed_edits for exact original, replacement, source and reason.'} for eid in unit_edits]
    units[k]={'status':'open' if unit_edits else 'pass','findings':findings,
      'questions':[{'question':'What would deleting this material lose, and which exact terminology does the reader need here?',
          'answer':deletion+' '+terms,'source_refs':sources}],
      'fields':{f[1]:order,f[2]:terms,f[3]:wording,f[4]:contribution},
      'deletion_test':deletion,'proposed_edit_ids':unit_edits}

review('::ch:FOUNDATIONS','p3 p5',
 'Deleting p3 would remove the biological tasks that make rate representation relevant. P5 connects representation, variable observations and shared movement statistics rather than listing unrelated topics.',
 'Value and activity pattern are familiar descriptions here. Neuron/place-cell definitions were supplied in the Reading Guide; rate and spike meanings are introduced next.',
 'Reading Guide sec:READING-START records calculus, probability and linear algebra. No specialist count or covariance machinery is presumed by this opening.',
 'The title gives the chapter result; p3 supplies the biological pressure and p5 states why the signal and probability foundations come before memory calculations.',
 'The three papers study different parts of this problem','The papers address storage loss, eye motion and spatial rate arrangements.','The three papers','Different aspects of neural representation','Study different questions','Their questions share background without being one circuit model','retain','The literal count and list distinguish the three source purposes. They are necessary scope, not a rhetorical tricolon.')
review('::sec:FOUNDATIONS-SPIKES','p9 p16 p20 p26 p28 p35',
 'Deleting the 20Hz timing contrast would permit a regular-clock interpretation; deleting the anatomy paragraph would blur CA1 output maps with recurrent storage. Both are needed before later papers.',
 'Spike, synapse, excitation/inhibition, recurrent connectivity, tuning curve, population code, decoding/encoding and rate map are explained at use. Place cell/field and hippocampus were already marked in Reading Guide p27, so repeat marking here is unnecessary.',
 'Cells and signals precede the rate vector. The vector is introduced before its neuron-index/physical-location distinction and before spatial examples.',
 'The section heading states the representation relationship. The eye curve provides one quantitative mapping; place and grid examples broaden the biological setting without claiming a shared mechanism.',
 'the pattern across N neurons carries information about θ','The rates together let an observer distinguish represented values.','The population rate pattern','The represented value θ','Varies with θ and supports decoding','A finite spike observation is still noisy','retain','Carries information is exact coding language with an explicit vector and variable. Contains would be no clearer; the later count section explains uncertainty.')
review('::sec:FOUNDATIONS-POISSON','p39 p66 p72 p88 p93',
 'The factorial-moment fold supplies a checkable derivation without obstructing the main count example. The conditional-recurrence paragraph and CV/Fano distinction prevent invalid later inferences and should remain.',
 'Poisson process, CV and Fano factor are technical names worth retaining. Changing state is sufficient in place of evolving state. The Fano definition needs a sentence break, not a different statistic.',
 'Mean/variance from basic probability are the baseline. The Poisson count law comes before its relative SD, pooling example and conditional-noise qualification.',
 'One uncertain cell motivates pooling. The final qualifications connect the useful model to recurrent activity and the eye paper’s more regular spike timing.',
 'Averaging over the evolving state','Average over the state as it changes.','The statistical average','Counts conditioned on a changing neural state','Can produce time and cross-cell correlations','Conditional independence does not imply independent full histories','revise','Changing is sufficient and more direct. Keep the exact conditional-independence distinction and repair the Fano sentence separately.')
review('::sec:FOUNDATIONS-COVARIANCE','p99 p101 p103 p129 p167',
 'Deleting the prediction-versus-command distinction would confuse an analysis with an intervention. Deleting the gain or measurement-error examples would obscure why recorded covariance/MSD does not directly locate a source. Remove only the redundant count-first sentence opening.',
 'Covariance, correlation and displacement have explicit meanings and blue first teaching. MSD is already taught in Reading Guide p82. Gain is taught at p129 but unmarked, so mark that first occurrence; its glossary entry already exists.',
 'The physical command→neurons→muscles path precedes the statistics. The shared/private equations explain gain before its effect on variance at p167. Later eye marking must become plain text.',
 'The heading distinguishes shared signals and bias. The parameter bullets name which part of the physical pathway changes; they are useful parallel comparisons, not prose to flatten.',
 'the dimensionless gains g_X,g_Y convert its effect into each recording','Each gain multiplies the shared signal’s contribution to a recording.','The gains g_X and g_Y','The shared signal S','Multiply its contribution','Covariance changes even if the source does not','revise','Use the direct multiplication description and mark gain at this first teaching location. Keep separate the causal muscle gain and fitted rate-angle slope.')
review('::ch:PERSISTENCE','p3 p5',
 'The opening introduces two perturbations with different effects on the represented value. Its roadmap connects repeated retained shifts to error growth and then separates temporal from spatial randomness.',
 'Coherent pattern is immediately grounded in changed activities versus changed value; no additional invented term is needed. State and attractor definitions follow.',
 'Representation and rate patterns from Foundations precede this distinction. The opening does not rely on eigenvectors or Brownian notation.',
 'The title states the surprising outcome and p3 raises its mechanism. P5 explains why geometry must precede accumulated random motion.',
 'a disturbance can change those activities without changing the represented value','Cells can change together while the decoded angle remains the same.','A disturbance','The population’s activities and represented angle','Changes one while preserving the other','A different disturbance can instead alter the stored value','retain','This is the concrete distinction proved by the next example. Deleting it would leave the geometry without a reader question.')
review('::sec:FOUNDATIONS-ATTRACTOR','p9 p13 p15 p49 p62',
 'Keep the model setup, rate coordinates and both perturbations because they isolate recovery from memory error. Delete p62’s repeated not-fitted sentence; p15 and the example label already establish the model’s status.',
 'State, fixed point, continuous attractor and attractor manifold are taught before calculation. Neutral is explained as absent restoring force. Lasting change is sufficient instead of the direction that survives.',
 'Rate patterns precede fixed-point geometry, which precedes the x/θ coordinate change and ODEs. The general projection is only previewed here and taught in the next chapter.',
 'The example answers the opening with two computed disturbances. The final paragraph should retain the general-network caveat and link, rather than repeat its status as an illustration.',
 'This construction illustrates the geometry; it is not a fit to eye-neuron recordings.','This is an illustrative model.','The guide’s construction','The two-rate example','Illustrates geometry','Its status was already stated before the example','delete','Deleting this repeated sentence loses no condition because p15 explicitly says not fitted. Preserve the following warning that general recovery need not be perpendicular.')
review('::sec:FOUNDATIONS-DIFFUSION','p68 p88 p106 p114 p124 p142',
 'The independent-step assumptions, D convention, bias comparison and shared-history covariance all support later calculations. Delete the repeated not-an-estimate sentence and the second warning about one path turning back; each already has an earlier sufficient explanation.',
 'Brownian motion is defined in the mathematical note before W appears in the example. Diffusion coefficient and MSD were first marked in the Reading Guide. Systematic drift’s first meaningful use is the constant-bias conclusion at p124; mark it there and retain the later reminder without a second blue mark.',
 'Independent variances are taught before2Dt. Covariance from Foundations supports the min(s,t) proof. Whether the optional first-read route adequately exposes Brownian notation remains a focused Stage3 flow question, not a missing source definition.',
 'The heading states the actual equal-increment premise and result. The example separates RMS from squared bias. The final covariance explanation motivates why later observations are not independent copies.',
 'A theory of random diffusion must therefore account for systematic drift separately','The mean motion must be tracked separately from random spread.','The diffusion model','Mean velocity and trial variance','Separates their contributions','A fixed bias contributes v²t² while variance contributes2Dt','revise','Mark systematic drift here and briefly name its nonzero mean velocity meaning. The example already supplies the mechanism and numerical contrast.')
review('::sec:FOUNDATIONS-RANDOMNESS','p159 p161 p163 p171',
 'The fixed-map comparison is needed for the book’s later Part III and the alternate place-field reading path. The schematic limit should remain because three aligned rows could otherwise look like one model.',
 'Random function of position is a sufficient plain description here. Gaussian process is not needed until its actual spatial-model teaching. Stays fixed names the model’s within-environment condition.',
 'Rate maps were introduced in Foundations before temporal diffusion. This section compares the two indexing variables after both are available.',
 'The heading directly states the distinction. The final source-map paragraph prepares the memory calculation without requiring the spatial mathematics early.',
 'Once drawn for a cell and an environment, that function is fixed','The same expected-rate function is used on repeat visits.','The modeled spatial function','Position-dependent expected rate','Remains unchanged during movement','Realized spikes can still differ on each visit','retain','This explicit condition prevents conflating a random map with temporal spike noise. The qualifier is needed; it does not claim biological maps never change.')
review('::ch:MEMORY-DYNAMICS','p3 p5 p7 p9',
 'The first sentence states continued firing with lost value. Its following right-place sentence adds no distinct point and can go. Keep the notation recap and precise source locator note because they support the equation-heavy chapter.',
 'Right place is vague for a nonspatial activation manifold. Remove that duplicate rather than define a new metaphor. The time and coordinate notation are exact and useful.',
 'The preceding chapter taught the represented coordinate and persistence/error distinction. The opening’s synaptic cycle leads to its detailed model before linearization.',
 'The title and first sentence name the scientific problem. P5 explains the calculation’s progression. The chapter transition is useful when stated as an extension to longer delays.',
 'The important question is whether the activity pattern stays in the right place','The pattern should keep representing the original value.','The activity pattern','The stored value','May shift despite continued firing','This is already stated immediately before','delete','The first sentence supplies the whole contrast more concretely. Deleting the inflated restatement also removes right place without losing a premise.')
review('::sec:MEMORY-SPIKES','p13 p17 p48 p50 p70 p80',
 'The explicit spike→activation→input→rate cycle is essential. The spike plot distinguishes events from their lingering effect; the replication argument justifies the approximation rather than merely naming weak noise.',
 'Neural transfer function and weak fluctuation approximation are taught at use. Counts, Brownian increments and preferred angle have preceding or local meanings. Gaussian process in the warning is a nonrequired contrast; no later calculation depends on that name here.',
 'The actor relationships and fixed-weight/Poisson assumptions precede the stochastic equations. The large-population construction precedes the leading-order qualification.',
 'The section heading states the renewal mechanism. Formula/trace/interpretation are connected by the actual state variable s, which is kept distinct from rate and voltage.',
 'Incoming activations determine new firing rates; the resulting spikes renew those activations','Synaptic input changes firing; new spikes add fresh activation.','Incoming activation and the resulting spikes','Firing rates and synaptic state','Form a recurrent renewal cycle','This feedback can sustain activity after input ends','revise','Keep both physical steps but use a full stop between them. The mathematics and causal order do not change.')
review('::sec:MEMORY-LINEARIZATION','p95 p97 p115 p130 p139 p178',
 'The K terms, left/right distinction and tilted example are all needed. A simple perpendicular projection would give the wrong retained coordinate, so the example cannot be replaced by the earlier symmetric one.',
 'Linearization and both zero eigenvectors are defined, with purpose and normalization. Mode is used in the baseline linear-algebra setting and tied to Kz=λz before its elimination. Lasting change is sufficient in the opening instead of survives.',
 'Taylor expansion from calculus gives K. The family derivative gives u before v is introduced to extract the coordinate. The tilted example comes after the proof and tests the geometric distinction.',
 'The heading identifies why return flow matters. The final example sentence should name x,y as variables and state the extraction result, with separate sentences.',
 'the one change that survives: the displacement to a different fixed point','The lasting disturbance is a shift to another fixed point.','The circuit’s return flow','The original activity disturbance','Removes stable components and retains a coordinate shift','Small disturbances and one neutral memory direction are assumed','revise','Lasting change states the required result in direct language. Preserve the exact eigenvector terminology in the derivation.')
review('::sec:MEMORY-DIFFUSION','p184 p186 p201 p213 p222',
 'Removing the projection variance expansion would hide why rate enters weighted by v². The local-scale limits and multiple-coordinate caveat are needed to apply the result correctly.',
 'Diffusion tensor is defined by covariance per twice elapsed time. The earlier v definition supplies projection meaning; coupled motion is explained as shared coordinate displacement.',
 'The scalar covariance sum precedes the multiple-coordinate formula and interpretation. No new noise assumption is introduced silently.',
 'The heading states the calculation result. The opening links cell spikes to return flow, and the close separates the next drift problem from local spreading.',
 'Each cell’s random spikes disturb its outgoing synaptic activation; the circuit’s return flow determines the lasting shift','Spikes perturb activation, and recovery decides which coordinate change remains.','The cell’s spikes and the circuit’s return flow','Synaptic activation and memory coordinate','Perturb then project the state','Weak local noise and conditional independence are required','revise','Separate the two actions into sentences. Their different actors and objects are already explicit and must stay so.')
review('::sec:MEMORY-SYMMETRIC','p226 p235 p259 p265 p284',
 'The symmetry specialization is useful because it replaces an unknown left vector with tuning/input slopes. The source square correction and excluded-boundary warning are essential, not editorial digressions.',
 'Symmetric weights are explained as reciprocal input weights before the derivation. Translation symmetry receives its first sufficient meaning at p265 but lacks its required blue mark and glossary entry. Keep it distinct from readout translation invariance.',
 'General K and projection come first. Symmetry then makes g′ a left zero direction. The inhibition example uses the earlier rate/state meanings and explicitly changes the coordinate units.',
 'The heading states the computational simplification. The example shows why opposing rate changes can coexist with constant D, and the excluded endpoints prevent overreading.',
 'translation symmetry, in which shifting an activity pattern along the represented coordinate leaves the network dynamics unchanged in form','A shift of the whole pattern preserves the dynamics’ form.','A shift along the represented coordinate','Activity pattern and network dynamics','Leaves the governing relation unchanged in form','This extra symmetry is not required for the symmetric-weight formula','revise','The explanation is sufficient and useful at this point. Mark its first teaching and add the matching glossary entry; do not add a longer geometry lesson.')
review('::ch:MEMORY-LONG-DELAYS','p3 p5 p7',
 'The opening names boundaries, periodic error and changing D, the actual mechanisms that limit a local2Dt prediction. Removing the average-motion sentence would hide a separate source of error handled later.',
 'Boundary, angular range and average value are plain descriptions before Fokker–Planck language. The three mechanisms are not an artificial tricolon.',
 'Local D and stable relaxation are available from the previous chapter. Density evolution is introduced only in the next section.',
 'The heading and first sentence raise the long-delay limitation. The roadmap tells why boundary calculations and drift separation precede the source-figure interpretation.',
 'the value may approach a boundary, wrap around an angular range, or reach a region where the spreading rate differs','Long delays can expose limits or changes that one local diffusion number misses.','The stored coordinate','Its range and local diffusion law','Moves into different global conditions','Each condition changes how error grows','retain','All three alternatives are used by the chapter. Removing one to avoid a three-item list would remove a real explanatory case.')
review('::sec:MEMORY-LONG-TIME','p11 p13 p47 p70 p74 p98',
 'The density derivation is a useful optional check, while the line/circle result and activation-coordinate distinction are required for interpretation. The excitation example isolates state-dependentD without adding a new decoder.',
 'Itô, Fokker Planck and Dirac delta are explained and marked at their first substantive uses. The delta notation is explicitly distinguished from δij. Replace curved variance versus time graph with the actual nonlinear-time relation.',
 'Density and increment moments precede the PDE. The Gaussian solution and wrapping precede the plateau. The zero-drift moment identities precede the linear-D conclusion.',
 'The heading identifies long-delay dependence. Replace upper/below in the figure conclusion with wrapped density and unbounded line so the mathematical objects remain clear in other layouts.',
 'a state dependent D need not produce a curved variance versus time graph','Changing D with state does not necessarily make variance nonlinear in time.','The state-dependent diffusion law','Variance over time','Can still yield linear variance growth','For linearD and the stated interior zero-drift conditions','revise','Name the mathematical relation directly. The following expectation calculation supplies the reason and all its qualifications remain.')
review('::sec:MEMORY-DRIFT-SCOPE','p111 p113 p115 p119 p121',
 'The drift-convention discussion is needed to prevent D from being mistaken for a full prediction of mean motion. The covariance extension marks an important limit, but its preview does not need still-untaught likelihood terminology.',
 'Systematic drift is taught earlier by the constant-bias example; this location keeps its model-specific reminder but loses the duplicate blue mark. Stratonovich is introduced with midpoint meaning. Fisher information and joint likelihood are not yet taught, so the preview can say joint spike probabilities.',
 'Itô was introduced in the density section before Stratonovich is compared. Mean and variance were taught in Foundations. The actual information/likelihood definitions come in the next chapter.',
 'The heading states whatD does not settle. The close appropriately warns about correlated noise, provided it does not require the next chapter’s terms to explain that warning.',
 'Calculating the corresponding Fisher information would require the matching joint likelihood','A matching information calculation needs joint probabilities for the spikes.','An information calculation','Joint spike patterns','Uses their probabilities under a correlated model','Independent-cell likelihoods no longer suffice','revise','Use the plain prerequisite now: probabilities of joint spike patterns. Retain the precise technical definitions where the next chapter derives them.')
review('::sec:MEMORY-FIGURES','p125 p127 p132 p143 p148 p150',
 'The panel guides identify rates versus spike events, internal displacement versus reading error, and model tests versus animal observations. These distinctions are needed to interpret the figures and cannot be inferred from their labels alone.',
 'Activity bump is defined as a localized rate peak across preferred angles; preferred angle was taught in the network model. Rotational symmetry is explained inline. Panel1B is a locator, not a numerical unit.',
 'All panel interpretations use prior flow, diffusion and wrapping explanations. Information is previewed descriptively before its formal derivation.',
 'The heading tells what the figures test. The end namesD and motivates deriving the next statistical quantity from the same tuning curves.',
 'The curve describes rates; the marks are particular random spike events','The curve is expected firing rate, while each mark is a realized spike.','The plotted curve and marks','Rates and spike events','Represent different objects','The angular trace tracks memory, not overall amplitude','revise','Use The curve describes rates. The marks show individual spikes. This preserves the required distinction with less wording and a sentence break.')
review('::ch:MEMORY-INFORMATION','p3 p5 p7',
 'The opening connects the same spike noise to internal movement and external reading. The bound-versus-guarantee caution is necessary before comparisons; the notation recap prevents J from floating free of the previous D calculation.',
 'The short-sample distinguishability description supplies the purpose before Fisher information is named. Particular network restricts the bound to matchedD,J and should remain.',
 'The physical spike model and projection come first; this chapter then defines and derives the statistical measure.',
 'The heading gives the relation. The first paragraph identifies who receives spikes and why the same variability affects both memory and readout.',
 'More information can permit better stability without ensuring that a particular circuit achieves it','A smaller lower bound need not reduce the actual error of this network.','The information constraint','A network’s possible diffusion','Allows but does not ensure smaller diffusion','The inequality is one-sided','retain','This is the needed distinction later demonstrated numerically. Dropping it would encourage a false optimization conclusion.')
review('::sec:MEMORY-FI','p15 p34 p42 p48 p64 p68',
 'The likelihood-to-score-to-bound steps are necessary for a reader without information theory. The baseline illustration shows why firing magnitude alone is misleading. The Gaussian approximation and prior limits must remain.',
 'Likelihood, score, Fisher information/rate, unbiased and prior all receive definitions before their main use. Efficient estimation is an unnecessary additional technical phrase; suitable estimator states the needed limit directly.',
 'The Poisson model and log differentiation from basic probability/calculus precede the score variance. The error bound is derived before its name and interpretation.',
 'The heading states the slope/noise relationship. The zero-slope and baseline examples interpret the formula rather than merely restating it.',
 'efficient estimation can approach the bound','A suitable estimator can get close to the lower error limit in the stated regime.','An estimator','The memory value inferred from spikes','Approaches the variance bound','Weak noise and informative local Gaussian likelihoods are assumed','revise','Efficient has a specialist estimator meaning not needed here. The replacement preserves the claim’s limiting conditions without adding another definition.')
review('::sec:MEMORY-BOUND','p82 p113 p127 p139 p147 p193',
 'Keep the equality condition, linear counterexample and strict inhibition example: each distinguishes a different quantifier. The matrix proof is a useful optional extension and its invertibility condition remains necessary.',
 'Cauchy Schwarz is recalled by its geometric inequality. Converse can be replaced by the exact implication being challenged, because logic terminology is not the subject. Do not alter the information–diffusion relation or its symbol names.',
 'D andJ were derived separately before their shared vector proof. Equality follows the inequality, and the multidimensional extension comes after the scalar example.',
 'The heading states the bound’s direction. The examples explain permitted versus actualD and sufficient versus necessary transfer classes.',
 'supplies a counterexample to the unrestricted converse','Shows that equality can hold without an exponential transfer rule.','The linear equal-input example','The alleged necessity of an exponential transfer','Refutes the unrestricted implication','The actual information–diffusion inequality remains valid','revise','State the disputed implication directly in the opening and conclusion. Preserve the full conditions on participating inputs and across-state ratios.')
review('::sec:MEMORY-COMPARISONS','p214 p216 p222 p224 p249 p262',
 'All four comparisons name what is held fixed. Removing the alternate fixed-activation or fixed-total-rate case would leave the main power law looking universal. The colocation limit prevents a mathematical relation becoming a biological localization claim.',
 'Holds fixed and stays fixed are literal controlled-variable conditions, not metaphors. Tuning width, rate, slope and matrix entries already have meanings. Exact powers and dimensional distinctions must remain.',
 'The scalar/matrix bound precedes parameter comparisons. The change of variables precedes the dimension list, and the alternative resource constraint follows so its different exponent can be understood.',
 'The heading states the key criterion. The two-factor list makes the opposite dimensional effects readable; it should not be turned into varied prose merely to avoid a count.',
 'Two factors determine how information changes with tuning width','The volume and slope terms contribute different powers of width.','The width change','Population integral and rate derivatives','Produces w^d and w^−2 factors','Peak rate, density and profile are fixed','retain','The number two is mathematical, not decorative. The list exposes the mechanism behindw^(d−2), which the next result needs.')
review('::ch:MEMORY-READOUT','p3 p5 p7',
 'Keep the future-only cue problem and the difference between target value and moving observations. Remove simply from the roadmap and split the storage/observation interval sentence; these changes lose no content.',
 'Cue state, storage delay and observation interval are assigned to x,T,L in the next setup. Particular random displacements distinguishes one realized history from the known distribution, so it is not padding.',
 'D,J andτ are recalled from previous chapters; the new timing roles are introduced before the decoder formulas.',
 'The heading identifies the observation problem. The roadmap contrasts equal weights and diffusion-aware reading for a moving target, then flags the source error claim to be checked.',
 'they cannot reveal the particular random displacements that occurred before it','Future spikes do not identify the actual sequence of earlier random increments.','Later spikes','The storage history','Constrain the cue state but not its unique earlier path','The observer starts observing only at the cue','retain','Particular is required to avoid falsely suggesting that the distribution or expected storage error is unknowable. Keep this first explanation and remove later redundant restatements.')
review('::sec:MEMORY-READOUT-SETUP','p11 p25 p35 p46 p56',
 'Keep the Gaussian observation interpretation and covariance proof, because the sum of error variances otherwise lacks its premise. Remove repeated lost-history sentences at p11 and p56; the opening already states the limitation and the setup gives the formal roles.',
 'The observer’s role can be stated as must estimate rather than wants. Translation invariance is explicitly readout-specific, so it should not be merged with network translation symmetry.',
 'Θ,x,xhat,T,L are assigned before the error split. Local unbiasedness was defined with the information bound, and the conditional-expectation step states how it is used.',
 'The heading states a conditional result. The timeline reinforces the target roles; its closing prose does not need to repeat the chapter-opening limitation yet again.',
 'The observer now wants the original value Θ','The task is to estimate the original value from future spikes.','The observer','The encoded value Θ','Estimates it using later spikes','Only observations after the cue are available','revise','Must estimate states the mathematical objective directly. Remove the final repeated past-increment sentence while preserving the access restriction and stored diffusion.')
review('::sec:MEMORY-NAIVE','p60 p68 p74 p80 p94 p109',
 'The shared Brownian history is essential because independent-sample averaging would give the wrong process term. The triangle integral makes2DL/3 checkable; the optimum follows from opposing terms.',
 'Naive denotes the explicitly defined equal-weight stationary-state reader. It is a source method label, not a judgment about the reader. Covariance and continuous averaging were already taught.',
 'The cue targetx is fixed before y(t) is averaged. Shared-increment covariance precedes the double integral, which precedes optimization.',
 'The heading names the failure at long observation times. The conclusion correctly locates the cause in equal weights rather than in obtaining extra data.',
 'The problem is their equal weighting for a moving state','Later data hurt only when the reader keeps giving all samples equal weight.','The equal-weight estimator','Observations of the drifting state','Treats distant observations as equally direct evidence aboutx','After the finite optimum the process-error term dominates','retain','The sentence supplies the decision-relevant cause and motivates the next ideal reader. Removing it would leave only a formula and the wrong lesson that more data are inherently harmful.')
review('::sec:MEMORY-IDEAL','p113 p117 p129 p142 p165 p199',
 'The backward precision construction avoids requiring an unexplained Kalman filter. Keep its transition-variance reasoning and limiting interpretation. Replace only the opaque carrying-information phrase and sentence joins.',
 'Precision is defined as reciprocal Gaussian variance. Hyperbolic functions are defined in the solution note; exact names remain because the formula uses them. Ideal observer is a benchmark, explicitly not a demonstrated circuit.',
 'Independent Gaussian precision addition precedes backward transition variance, recurrence, ODE and solution. The source-equivalence note is useful because the derivation differs from the SI method.',
 'The heading states improvement toward a limit. The numerical multiples ofL* distinguish practical saturation from an abrupt stopping time.',
 'uncertainty when carrying that information backward through diffusion','Later observations are less direct evidence about the cue because the state has diffused in between.','Diffusion between the cue and later samples','The precision gained about the cue state','Reduces the gain from new observations','The term is2DP² in the derived precision equation','revise','Name the observation times and the intervening motion. Keep the mathematical backward recursion but do not rely on a transport metaphor to explain it.')
review('::sec:MEMORY-PARTIAL','p203 p211 p220 p224 p228',
 'Independent thinning is necessary to justifyJo=αJ; do not collapse it into arbitrary neuron sampling. The example must interpret how partial access changes readout while leaving storage unchanged.',
 'Information fraction differs from cell/spike fraction under biased selection. Both are explained in place. Readout cost is replaced in the example conclusion by time and uncertainty to name the actual outputs.',
 'The full-observer scales precedeα substitution. The example keepsD,T fixed before comparingJo and the derived numbers.',
 'The heading states a possible longer observation time. The new final sentence summarizes the comparison actually calculated instead of repeating the chapter’s lost-history warning.',
 'Longer observation can reduce the readout cost; it cannot undo the random displacement during the delay','Limited access changes the readout term while storage error remains the same.','Limited spike access','Observation time and cue-state uncertainty','Increases both in this comparison','The full networkD and storage timeT are unchanged','revise','Replace the repeated general warning with the numerical example’s own conclusion. The storage/readout distinction remains intact.')
review('::sec:MEMORY-EXTENSIONS','p234 p244 p255 p270 p278 p282',
 'The two-stage block derivation is needed to explain why these time constants add. The matched additive-noise calculation is needed to prevent carrying the Poisson equality condition into another noise law.',
 'Left zero vector and tangent retain exact earlier meanings. Constant additiveq is defined by its equation and observation variance. Very different can be replaced by the actual much-larger relation that makes one term dominate.',
 'The newr dynamics and noise placement precede the block matrix. The Gaussian noise law precedes its information and diffusion weights, so no hidden change of model is required.',
 'The heading names changes to both bound and equality. The conclusion restricts the sum-of-times rule to this model; it is necessary rather than defensive.',
 'The larger one dominates when they are very different','When one time constant is much larger, it supplies most of their sum.','The larger time constant','The sumτ+τm','Contributes most of the effective time','The constants must be well separated','revise','Name the relevant magnitude relation directly. Keep the exact two-stage and noise-placement limits in separate sentences.')
review('::sec:MEMORY-FIG3-AND-CAUTION','p286 p312 p320 p330 p341',
 'The normalized curves identify the readout object before the source-bound challenge. The inequality direction and strict example are indispensable. The closing leak distinction prevents confusing finite useful readout with a deterministic memory lifetime.',
 'Saturation and asymptotic are tied to explicit limit formulas; retaining them preserves finite-versus-infinite observation meaning. Citation ranges and exact source equation numbers must not be changed for lint.',
 'All quantities and reader models are established earlier in the chapter. The source claim is stated before its algebraic challenge and numerical strict case.',
 'The heading signals both the result and a source qualification. The last paragraph connects uncertainty growth to use as an integrator without claiming a neural implementation.',
 'Diffusion limits the accuracy of the integral and the usefulness of long observation; it does not by itself introduce that restoring pull','Noise spreads the accumulated value without adding a deterministic leak.','Diffusion','The stored integral and its trial distribution','Increases uncertainty','No restoring mean force follows from diffusion alone','revise','Preserve the critical distinction but separate its positive result and negative limit into sentences. The analogy of pull was already made concrete by a leak toward a reference value.')
review('part:MECHANISMS::part-opening','',
 'The Part opening tells why continuing activity can still lose memory accuracy and maps the six chapters to representation, spreading and readout. Deleting it would remove the purpose of this multi-chapter sequence.',
 'The opening uses activity pattern, cells, angle and random spikes rather than assuming attractor or Fisher-information knowledge. Its technical title includes the model scope without demanding the later derivation.',
 'The Part places the two foundation chapters before detailed memory calculations. Later Parts retain separate eye-evidence and spatial-statistics purposes.',
 'The title and purpose state the physical problem; the chapter groups explain why the reader needs each step before the next.',
 'Random spikes can change that angle even while the activity continues','Persistent firing does not guarantee that the represented angle stays correct.','Random spikes','The represented angle','Can change it while activity continues','The Part concerns continuous-attractor models','retain','The sentence is the concrete problem organizing all six chapters. It adds purpose rather than reciting a table of contents.')

# Exact source phrase and diagnostic-location qualification.
pk='part:MECHANISMS::part-opening';field=p['review_fields'][3]
units[pk]['fields'][field]=units[pk]['fields'][field].replace('Random spikes can change that angle even while the activity continues','Random spike timing can change that angle even while the circuit sustains its activity')
decisions[errors[196]['id']]['reason']='The frozen diagnostic reports ; pp. at line282, but the current line282 contains no semicolon. The actual ; pp. separator is in the scaling reference at line278 and separates source locations, not prose clauses. Retain the source locator and record this diagnostic-position mismatch; do not invent a prose repair at line282.'
decisions[errors[185]['id']]['reason']='The SI information reference contains page range9–10 and equation rangeS42–S44. Both en dashes are precise source locators, not prose em dashes.'
decisions[errors[193]['id']]['reason']='The scaling reference contains article page range17645–17650 and discussion range5–6. Both are bibliographic locators.'

fold_purposes={
 'Derivation: why a Poisson count has variance equal to its mean':'The title tells the reader which stated moment identity the optional calculation checks; retain its exact Poisson term.',
 'Mathematical definitions: covariance, variance and correlation':'The title separates formal moment definitions from the preceding physical interpretation, and names the three distinct statistics.',
 'Derivation: separating spread from mean displacement':'The title names the two components whose algebra is being checked, so a reader can choose the relevant optional proof.',
 'Mathematical model: independent steps and Brownian motion':'The title identifies the modeling assumptions and the continuous process, not an unrelated advanced detour. Its optional placement remains a Stage3 route check.',
 'Mathematical detail: why two times share accumulated noise':'The title states the concrete question answered by the min(s,t) proof and connects it to later averaging.',
 'Derivation: from random increments to the memory density equation':'The title names the transformation from increment moments to probability density, allowing the main line/circle result to remain readable.',
 'Check: equality can also hold with a linear transfer rule':'The title states the exact claim challenged by the short counterexample; retain linear transfer as the relevant condition.',
 'Check: the residual matrix proves the lower bound':'The title identifies the purpose of the matrix algebra. Residual is made concrete by the immediately displayedQ definition.',
 'Mathematical solution: hyperbolic functions and finite-time readout error':'The title indicates both the needed function definitions and the finite-time result, so the fold is useful to a reader checking the derivation.',
 'Original paper figure: Burak and Fiete (2012), Figure S1':'The label identifies the exact source figure so it can be distinguished from guide teaching diagrams. It is reference information, not prose needing a transition.',
 'Original paper figure: Burak and Fiete (2012), Figure 1':'The label identifies the exact source figure and distinguishes it from the guide’s tilted-flow construction.',
 'Original paper figure: Burak and Fiete (2012), Figure 2':'The label identifies the source simulation figure, whose specific panels the text has just explained.',
 'Original paper figure: Burak and Fiete (2012), Figure 3':'The label identifies the published normalized-readout curves separately from the guide’s analytic reconstruction.',
 'Original paper figure: Burak and Fiete (2012), Figure S2':'The label identifies the supplementary partial-access comparison separately from the main full-access figure.'}
for x in stage1['extra_reader_text_inventory']:
    y={k:x[k] for k in ['source','location','text']}
    if 'line' in x:y['line']=x['line']
    related=[e for e in edits if e['source']==x['source'] and ('location' in e and (e['location'].rsplit('.',1)[0] in x['location']))]
    if x['location'].startswith('section_list'):
        k=x['unit_ref']; reason=units[k]['fields'][p['review_fields'][4]]
    elif x['location'].startswith('blocks'):
        ident=re.search(r'id=([^\]]+)',x['location']).group(1)
        meta_data=yaml.safe_load((base/x['source']).read_text(encoding='utf8'))
        block=next(b for b in meta_data['blocks'] if b['id']==ident)
        k=next(k for k in units if k.endswith('::'+block['placement']))
        reason='Keep the caption’s declared model/source, parameter values, observable result and limits because the figure must remain interpretable independently of nearby prose. '+units[k]['deletion_test']
    elif isinstance(x['text'],str):reason=fold_purposes[x['text']]
    else:
        stem=Path(x['source']).stem
        k=next(k for k in units if k.startswith('content/chapters/'+stem+'.md::ch:'))
        reason=units[k]['fields'][p['review_fields'][4]]+' The declared prerequisites match the actual preceding teaching.'
    y.update({'decision':'revise' if related else 'retain','reason':reason,'proposed_edit_ids':[e['id'] for e in related]})
    extra.append(y)

assert set(units)==set(p['units'])
for k,u in units.items():
    allowed={z['id'] for z in p['units'][k]['paragraphs']}
    for q in u['questions']:
        for ref in q['source_refs']:
            if ref!=k:assert ref.rsplit('/',1)[1] in allowed,(k,ref)
for e in edits:
    if e['source'].endswith('.md'):assert e['original'] in (base/e['source']).read_text(encoding='utf8'),e['id']
for s,h in stage1['source_hashes'].items():
    assert hashlib.sha256(Path(s).read_bytes()).hexdigest()==h,('source changed during review',s)

def write_result(completed):
    source_hashes=dict(stage1['source_hashes'])
    for path in [base/gsource,out/'memory-input.json',out/'memory-vale-input.json']:
        source_hashes[str(path).replace('\\','/')]=hashlib.sha256(path.read_bytes()).hexdigest()
    counts={x:sum(v['decision']==x for v in decisions.values()) for x in ['revise','retain_exception']}
    result={'call':{'run_id':'memory-language-20261029-02','reviewer_id':'/root/alignment_global','stage':'necessity_language',
       'context':'reviewer_continuation','started_at':'2026-10-29T12:52:19.0575041+02:00','completed_at':completed,
       'input_hash':p['input_hash'],'review_contract_hash':p['review_contract_hash'],
       'vale_input_hash':hashlib.sha256((out/'memory-vale-input.json').read_bytes()).hexdigest()},
       'units':units,'proposed_edits':edits,'vale_decisions':list(decisions.values()),
       'extra_reader_text_inventory':extra,'source_hashes':source_hashes,
       'coverage':{'units':29,'paragraphs':376,'extra_reader_text_records':len(extra),'vale_errors':256,'vale_decisions':counts,
                   'warnings_and_suggestions_context_checked':489},
       'warning_context':[
        'Sentence-length flags were checked against actual actors and conditions. The proposed splits target separate claims; mathematical premises and exact equations were retained.',
        'Citation years, issue numbers, equation references and explanatory mathematical parentheses retain their reference function.',
        'Passive voice is retained when the mathematical object/result matters more than an artificial human actor. We is retained for shared calculations, not invented agency.',
        'Separately, repeatedly, generally, sharply and slowly express distinctions used by the local mathematics: mean versus variance, repeated increments, generic versus special matrices, or slope size.',
        'Heading acronym warnings on LONG, TIME, FI and AND come from source IDs rather than unexplained displayed acronyms.',
        'Guarantee is in explicit denials of attainment; best names a derived optimum, so the excessive-claim flags do not justify weakening those distinctions.',
        'The very-different time-scale wording and non-error semicolon/list occurrences were independently repaired as proposed edits. Bibliographic-list separators remain.'],
       'coordination':[
        {'topic':'gain first definition','first_teaching':'content/chapters/01-foundations.md:129','later_explanation':'content/chapters/01-foundations.md:167','dependent_action':'Root/eye reviewer removes later first-definition marker in04-eye-drift.md:47; existing glossary gain entry remains.'},
        {'topic':'systematic drift first definition','first_teaching':'content/chapters/01b-persistence.md:124','dependent_action':'The proposed edit removes the duplicate first-definition span at02b-memory-long-delays.md:113 while retaining its model-specific meaning.'},
        {'topic':'translation symmetry','first_teaching':'content/chapters/02-memory-dynamics.md:265','dependent_action':'Proposed matching glossary entry is included; keep separate from readout translation invariance.'}],
       'scope_limits':['No manuscript, metadata, packet, Vale profile or rule severity was changed.',
                       'All edits remain proposals. Open unit statuses reflect unapplied language/definition repairs.',
                       'No figure pixel acceptance. Caption/alt text and visible fold labels were reviewed as text.',
                       'Stage3 connected flow remains a separate call. Optional-fold dependence for Brownian and finite-readout formulas is noted for that call, not silently accepted here.',
                       'Existing global-call evidence was not reassembled after root withdrew that request.'],
       'exception_application':'For independently retained false positives, the coordinator may use narrowly scoped native Vale comments covering only the cited rule and passage. Preserve source wording and existing profile/severity. This report does not insert comments or claim a clean rerun.',
       'timing':{'awake_execution':'unverified','token_stats':'unavailable','verified_checkpoints':['2026-10-29T12:52:19.0575041+02:00','2026-10-29T12:55:09.2319265+02:00','2026-10-29T13:01:00.0346657+02:00','2026-10-29T13:07:32.7199114+02:00']}}
    (out/'memory-stage2.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    elapsed=(datetime.fromisoformat(completed)-datetime.fromisoformat(result['call']['started_at'])).total_seconds()
    opened=sum(u['status']=='open' for u in units.values())
    text=f'''# Part I: necessity and terminology review

Call `memory-language-20261029-02`, independent reviewer `/root/alignment_global`, continuation after the separately recorded truth review. Requested configuration: Astra/high. Runtime model label and token stats are not independently exposed.

Started: {result['call']['started_at']}  
Completed: {completed}  
Wall time: {elapsed:.2f} seconds. Awake execution time is unverified. Duration uses actual Get-Date timestamps, including any pauses.

All 29 units and 376 paragraphs were read for contribution and terminology, alongside the chapter purposes, navigation summaries, captions, alt text and visible fold titles. The JSON gives passage-specific deletion tests, term/prerequisite judgments and concrete-wording records with all required sublabels.

There are {len(edits)} proposed edits, mostly individual prose/list sentence repairs and matching metadata changes. {opened} units remain open until their proposals are resolved. No manuscript changes were made.

The substantive findings are:

- Mark **gain** at its first teaching in Foundations line129. Its multiplication role is already used there and explained again at167. The eye reviewer should remove the later first marker.
- Mark **systematic drift** at the constant-bias example’s conclusion in Persistence line124, and keep the later model-specific explanation without a second mark.
- Mark **translation symmetry** where it is first explained in Memory Dynamics line265, with the included glossary entry. Do not merge it with the different readout use of translation invariance.
- State joint spike probabilities in the long-delay chapter’s correlated-noise preview. Fisher information and likelihood are formally taught in the following chapter.
- Remove repeated not-fitted/example-status wording and repeated lost-past-increments warnings where an earlier passage already supplies the full qualification. Keep the first necessary distinction and the conditions on each formula.
- Replace a few unnecessary phrases with their actual objects or claims, including efficient estimation, unrestricted converse, carrying information backward, and cross time covariance terms.
- Split actual prose semicolons and independently useful assumption bullets. Bibliographic citation separators, source ranges and exact mathematical names stay intact.

All 256 Vale error IDs have individual decisions: {counts['revise']} revise and {counts['retain_exception']} retain as justified exceptions. The other489 warning/suggestion rows were checked in context. One reported semicolon at Information line282 is absent from that line; the matching bibliographic separator is at278, and its location issue is recorded. No rule severity or profile was changed.

Each proposal includes the full exact original paragraph or metadata field and its replacement. Markdown originals match the current files, and all source hashes from Stage1 remain unchanged. The draft `memory-stage2-proposals.json` contains the same96 proposals for integration; `memory-stage2.json` is the complete record.

Figure pixels remain deferred. Stage3 must separately check the connected reading path, including whether the optional Brownian and hyperbolic-function notes leave the first-reading route with sufficient meanings for later formulas. This call does not claim full book acceptance. Token stats unavailable.
'''
    (out/'memory-stage2.md').write_text(text,encoding='utf8')
    return result

if __name__=='__main__':
    import sys
    if len(sys.argv)>1:write_result(sys.argv[1])
