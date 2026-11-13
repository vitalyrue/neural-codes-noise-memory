"""Record individual language judgments and proposed edits, without changing sources."""
import json,re,hashlib
import yaml
from pathlib import Path
from datetime import datetime
root=Path(__file__).parent
guide=root.parent.parent
inp=json.loads((root/'eye-input.json').read_text(encoding='utf-8-sig'))
alerts=json.loads((root/'eye-vale-input.json').read_text(encoding='utf-8-sig'))
out={'call':{'run_id':'local-request:eye-language-20261029-02','reviewer_id':'/root/alignment_eye_truth','stage':'necessity_language','context':'reviewer_continuation','started_at':'2026-10-29T12:45:28.9455912+02:00','completed_at':None,'input_hash':inp['input_hash'],'review_contract_hash':inp['review_contract_hash']},'units':{},'proposed_edits':[],'vale_decisions':[],'scope':{'units':25,'paragraphs':236,'vale_alerts':625,'vale_errors':190,'source_edits':False,'figure_pixel_acceptance':'deferred','awake_execution_time':'unverified','token_stats':'unavailable'}}
edits_by_line={}
def edit(stem,line,replacements,reason,delete=False):
    source='content/chapters/'+stem+'.md'
    lines=(guide/source).read_text(encoding='utf-8').splitlines()
    start=line-1
    while start>0 and lines[start-1].strip():start-=1
    end=line
    while end<len(lines) and lines[end].strip():end+=1
    original='\n'.join(lines[start:end])
    replacement=original
    if delete:replacement=''
    for old,new in replacements:
        assert replacement.count(old)==1,(stem,line,old,replacement.count(old))
        replacement=replacement.replace(old,new,1)
    ids=[]
    for key,u in inp['units'].items():
        if key.startswith(source+'::') and any(start+1<=p['line']<=end for p in u.get('paragraphs',[])):ids.append(key)
    if not ids:
        # Footnote definitions belong to the section that uses their citation.
        tag=re.match(r'(\[\^[^]]+\])',original)
        if tag:
            ids=[k for k,u in inp['units'].items() if k.startswith(source+'::') and tag.group(1) in u.get('review_source','')]
    assert ids,(stem,line)
    eid=f'eye-L{len(out["proposed_edits"])+1:02d}'
    row={'id':eid,'source':source,'line':start+1,'end_line':end,'original':original,'replacement':replacement,'reason':reason,'affected_unit_ids':ids}
    out['proposed_edits'].append(row)
    for n in range(start+1,end+1):edits_by_line[(source,n)]=row
    return eid

edit('00-reading-guide',7,[('; the eyes','. The eyes'),('; a moving animal','. A moving animal'),('; recordings','. Recordings')],
'The three task requirements and model-versus-recording distinction are all needed. Full stops preserve them while removing three prose semicolons under the strict profile.')
edit('00-reading-guide',54,[('; open one','. Open one')],
'Keep the first-reading advice and access to longer calculations. Splitting the instruction removes a prose semicolon without changing optionality.')
edit('00-reading-guide',66,[('; probability','. Probability')],
'The separate jobs of linear algebra and probability are needed here. Two sentences express them without a semicolon.')
edit('00-reading-guide',72,[('; the guide','. The guide')],
'Local-copy access and differences in teaching derivations are separate useful facts. Preserve both with sentence punctuation.')
edit('00-reading-guide',97,[('; guide citations','. Guide citations')],
'The cover offset explains the page-number warning. Preserve that reason and split the two clauses; keep source title, author names and citation ranges unchanged.')
edit('00-reading-guide',99,[('These links open PDF files. ',''),('Several printed intermediate equations require care; the guide identifies apparent inconsistencies beside the affected calculations and follows an explicitly shown derivation.','The guide identifies apparent inconsistencies in several printed intermediate equations beside the affected calculations and follows an explicitly shown derivation.')],
'Deletion test: every immediately preceding source link already says PDF. The general require-care clause adds no detail beyond the next clause. Merge its only specific content, printed intermediate equations, into the actual action and preserve the author-confirmation limit.')
edit('04-eye-drift',13,[('The study separated these cell types using their eye movement response parameters.','The study separated these cell types by how their firing changed with eye position and movement.')],
'The classification basis matters, but eye movement response parameters is an unexplained noun string before fitting is taught. The replacement states the measured relationship in ordinary words; the source figure and later fit give its parameters.')
edit('04-eye-drift',34,[('; there were','. There were')],
'One-cell recording and absence of simultaneous neural pairs are required to interpret covariance. Keep both, replacing the prose semicolon.')
edit('04-eye-drift',36,[('; they do not','. They do not')],
'The difference between repeated observations and independent animals is needed with the sample counts. Preserve it in a separate sentence.')
edit('04-eye-drift',47,[('[[**Gain**]{.definition-term custom-style="Definition Term"} is the scale that converts a change in one signal into a change in the other.]{.definition-explanation}','Gain is the scale that converts a change in one signal into a change in the other.')],
'Gain is already taught in 01-foundations.md:129 and used causally at line167. Retain this short reminder but remove the late first-definition marker. Coordinator should mark the earlier teaching passage; this edit alone does not close that cross-group requirement.')
edit('04-eye-drift',49,[],
'Deletion test: this sentence announces the same physical/recording/calculation separation already conveyed by the next figure and its caption. Removing it loses no setup beyond the preceding calibration paragraph.',delete=True)
edit('04-eye-drift',57,[],
'Deletion test: the figure caption states the proposed source and one-cell calculation, while p34 already explains why there is no directly measured OMN-pair covariance. This paragraph repeats those points after the caption. Removing it preserves the next section’s direct problem, predicting rate during motion.',delete=True)
edit('04-eye-drift',78,[('; the acceleration','. The acceleration')],
'The velocity and acceleration effects are distinct necessary parts of the fitted model. Split them without dropping the mass/gain interpretation or neural lead.')
edit('04-eye-drift',89,[('; Fig. 1d','. Fig. 1d')],
'The single-cell and population panel distinction is useful. A full stop removes the prose semicolon; Fig.1d is a panel identifier, not a unit error.')
edit('04-eye-drift',141,[('; it imposes causality',', which makes the response zero before the input')],
'The step-function action is required. State its concrete effect instead of adding a semicolon and restating the already defined causality label; preserve the delayed kernel and impulse definition.')
edit('04-eye-drift',148,[('; adding those responses','. Adding those responses')],
'A spike response and the sum of responses are both necessary for the units argument. Split the clauses while preserving the normalization.')
edit('04-eye-drift',176,[('This checks the gain as well as the time constants; it is not a fit to a recorded cell.','This checks the gain and the time constants.')],
'The gain check interprets the calculation. The denial of a recorded-cell fit repeats p169’s constructed example label and can be deleted without losing the example’s status.')
edit('04-eye-drift',235,[('; for several thousand','. For several thousand')],
'The population-size comparison is part of the bound argument. Preserve the comparison and the independent-only qualifier, using a full stop.')
edit('04-eye-drift',241,[('uses the fact that the inverse filter has a calibrated gain in degrees','uses the inverse filter’s calibrated gain in degrees')],
'The calibrated gain is necessary, but the fact that contributes no condition or mechanism. The shorter phrase names the object used by the covariance calculation.')
edit('04-eye-drift',310,[('Private prediction noise enlarges the denominator of R without changing the covariance. ', '')],
'Deletion test: p279 teaches the denominator mechanism and the figure caption repeats the falling-R result. Keep the useful figure-reading detail about equal physical scales and the source link.')
edit('04b-eye-timing',48,[('; a constant subtraction','. A constant subtraction')],
'The temporal-correlation caveat is necessary to bound the correction. Preserve the exact covariance formula and state the resulting limitation in its own sentence.')
edit('04b-eye-timing',58,[('The offset comes from two independent position errors, one at each endpoint. Its removal changes the average MSD; it does not recover each trajectory’s unknown error. ', '')],
'Deletion test: p35 derives the two-endpoint offset, p37 states that subtraction does not recover trial noise, and the figure caption repeats the offset. Keep why Brownian motion was chosen for this illustration and the source link.')
edit('04b-eye-timing',69,[('; it does not','. It does not')],
'The finite-lag limitation is necessary when introducing superdiffusion. Preserve it with a full stop inside the definition explanation.')
edit('04b-eye-timing',118,[('; it is not','. It is not')],
'The eye-filter and synaptic time constants must remain distinct. Split the prose clauses without changing their meanings.')
edit('04b-eye-timing',178,[('; at $\\ell=5\\tau$','. At $\\ell=5\\tau$')],
'Both sample slopes show the changing local exponent and are useful. Replace only the prose semicolon, preserving the mathematical values and interpretation.')
edit('04c-eye-circuit',9,[('; the other fires','. The other fires')],
'Opposite response directions define the two populations. Full stops retain the bilateral mechanism and approximate-persistence qualifier.')
edit('04c-eye-circuit',28,[('; one spike','. One spike')],
'Between-spike decay and spike-triggered jumps are distinct state changes required by the mechanism. Split the clauses, preserving the jump formula and saturating-response distinction.')
edit('04c-eye-circuit',53,[('With spikes, perturbations along the nearly neutral direction additionally accumulate.','With spikes, perturbations along the nearly neutral direction also accumulate.'),('; Figure 4','. Figure 4')],
'The noise-driven change is additional to deterministic mismatch, so keep the additive meaning with ordinary also. The source-versus-teaching distinction and figure’s role remain; split the prose semicolon.')
edit('04c-eye-circuit',72,[('; at constant mean rate','. At constant mean rate')],
'Spike jump and steady mean output are both needed to distinguish the motor-output convention. Preserve them in separate sentences.')
edit('04c-eye-circuit',116,[('; the model uses','. The model uses')],
'The Poisson reference and actual model CVs are needed before the thinning derivation. Replace the prose semicolon only.')
edit('04c-eye-circuit',118,[('; the simple interval derivation','. The simple interval derivation')],
'Constant-rate derivation versus time-varying simulation is a necessary scope distinction. Keep it with a full stop.')
edit('04c-eye-circuit',151,[('; the version','. The version'),('deg$^2$/s.  This scaling','deg$^2$/s. This scaling')],
'The units comparison and fixed-geometry condition are necessary. Split the semicolon and remove the duplicate space; preserve all symbols and the source-normalization ambiguity.')
edit('04c-eye-circuit',190,[('; that negative estimate','. That negative estimate')],
'A negative sample estimate must not be mistaken for negative physical variance. Retain the interpretation while replacing the prose semicolon.')
edit('04c-eye-circuit',267,[('Some supplement cross references use earlier figure/equation numbers; p. 5 also mentions','Some supplement cross references use earlier figure/equation numbers. Page 5 also mentions')],
'These are two explanations of source-version differences, not a compact list of citation locations. Use sentences while preserving the 15K/30,000 distinction.')
edit('04c-eye-circuit',275,[('; the output-noise comparison','. The output-noise comparison')],
'This footnote describes what two source figures establish, rather than merely separating citation locations. Split the explanatory prose without changing either locator.')

# The specific replacement operations above are report-only. Each proposal stores
# the complete exact source paragraph and complete proposed paragraph for review.
def sideedit(stem,section,replacements,reason):
    source=f'content/chapters/{stem}.yaml'
    data=yaml.safe_load((guide/source).read_text(encoding='utf-8'))
    original=next(s['summary'] for s in data['section_list'] if s['id']==section)
    replacement=original
    for old,new in replacements:
        assert replacement.count(old)==1,(stem,section,old)
        replacement=replacement.replace(old,new,1)
    eid=f'eye-L{len(out["proposed_edits"])+1:02d}'
    out['proposed_edits'].append({'id':eid,'source':source,'yaml_field':f'section_list[id={section}].summary','original':original,'replacement':replacement,'reason':reason,'affected_unit_ids':[f'content/chapters/{stem}.md::{section}']})
sideedit('00-reading-guide','sec:READING-FIELD',[('; the eyes','. The eyes'),('; a moving animal','. A moving animal'),('; recordings','. Recordings')],'The reader-visible summary repeats the three prose semicolons in p7. Keep it aligned with the individually reviewed paragraph repair.')
sideedit('04-eye-drift','sec:EYE-RECORDINGS',[('; there were','. There were')],'The navigation summary repeats the p34 recording-design prose semicolon. Preserve the one-cell and no-simultaneous-pairs facts.')
sideedit('04-eye-drift','sec:EYE-CHI',[('uses the fact that the inverse filter has a calibrated gain in degrees','uses the inverse filter’s calibrated gain in degrees')],'The reader-visible summary has the same unnecessary the fact that as p241; preserve calibrated-gain meaning.')
sideedit('04c-eye-circuit','sec:EYE-CIRCUIT-MODEL',[('; the other fires','. The other fires')],'The summary repeats the bilateral population prose semicolon at p9; preserve both directions and approximate persistence.')
sideedit('04c-eye-circuit','sec:EYE-SCALING',[('; the model uses','. The model uses')],'The summary repeats p116’s prose semicolon. Preserve the Poisson reference and both model CV values.')

specific={}
def reason(rule,stem,line,why):specific[(rule,stem+'.md',line)]=why
# Context judgments for logical connectors: keep derivation links when they
# actually connect a premise to a consequence; a connector is not automatically filler.
for stem,line,why in [
 ('00-reading-guide',19,'Retinal-image changes are why the origin of drift matters to visual signals; therefore states that causal link.'),
 ('00-reading-guide',27,'In particular locations means selected spatial positions, not a formal transition. It is part of the place-cell definition.'),
 ('00-reading-guide',33,'Therefore gathers the three already explained contributions into their different evidence roles.'),
 ('00-reading-guide',66,'For example introduces a real illustrative spike disturbance after the general model/derivation distinction.'),
 ('04-eye-drift',11,'Therefore links the need for ongoing muscle command to why a brief movement command is insufficient.'),
 ('04-eye-drift',30,'This is why connects private-noise averaging to the usefulness of one noisy neuron; removing it weakens the stated reason.'),
 ('04-eye-drift',34,'Thus connects the one-cell-at-a-time design to inability to measure neural-pair covariance directly.'),
 ('04-eye-drift',61,'Therefore motivates adding motion and acceleration terms after position-only prediction is shown insufficient.'),
 ('04-eye-drift',78,'Thus summarizes the distinct coefficient roles; In particular introduces the likely mass-coefficient misconception. Both refer to the preceding equation.'),
 ('04-eye-drift',158,'Therefore links continuity and the impulse-integrated velocity jump to the following two equations for A and B.'),
 ('04-eye-drift',165,'Hence connects substitution B=-A to the solved kernel amplitude; this is an algebraic consequence.'),
 ('04-eye-drift',188,'Thus connects the kernel-area integral to the static position offset, the calibration check being taught.'),
 ('04-eye-drift',225,'Consequently connects nonnegative residual variance to the summed-correlation inequality.'),
 ('04-eye-drift',235,'Thus carries the Jensen lower bound into the 2.9% versus 0.1% comparison; it identifies the inference.'),
 ('04-eye-drift',262,'Therefore connects covariance cancellation under the stated assumptions to the common-variance estimator.'),
 ('04-eye-drift',322,'Additionally names the normal-error assumption beyond the independence used for minimum-variance weighting. The extra assumption matters; it is not merely decorative.'),
 ('04b-eye-timing',48,'For instance marks constructed numbers; This is why connects 25% subtraction uncertainty to the need for an uncertainty assessment.'),
 ('04b-eye-timing',71,'Consequently connects stationarity to constant position variance, which is needed for the plateau argument.'),
 ('04b-eye-timing',90,'Consequently connects disappearing kernel overlap to the finite MSD plateau.'),
 ('04b-eye-timing',178,'Thus connects the calculated intermediate slopes to filtering of ordinary internal diffusion.'),
 ('04c-eye-circuit',81,'Therefore connects each active unit transmitting the common mean position to averaging preserving that common signal.'),
 ('04c-eye-circuit',118,'Therefore connects summing M independent exponential intervals to their mean, variance and CV.'),
 ('04c-eye-circuit',120,'Thus connects interval-time variance to the long-window count variance approximation.')]:reason('ai-tells.FormalTransitions',stem,line,why)

for stem,line,why in [
 ('00-reading-guide',3,'The three paper questions are actual distinct scientific questions, and memory/eye/navigation is a noun list, not an ornamental sequence of verbs.'),
 ('00-reading-guide',13,'Derivation, comparison with simulation and relation to estimation are the study’s distinct methods/results. Removing one changes the study summary.'),
 ('00-reading-guide',33,'The three nouns identify different evidence types: a mathematical constraint, source evidence and spatial statistical explanation. This comparison is the point of the paragraph.'),
 ('00-reading-guide',40,'This navigation item identifies the actual memory topics taught; the match is not three parallel verbs.'),
 ('00-reading-guide',42,'Spatial maps, size predictions and shape/origin tests are actual chapter contributions, not an arbitrary rhythmic list.'),
 ('00-reading-guide',60,'Cells/signals, changes and assumptions are separate parts of a mechanism description. Each is needed to distinguish model setup from mathematical consequence.'),
 ('00-reading-guide',61,'Tool, conditions and assigned neural quantities are the necessary parts of applying a mathematical argument; the match is a noun list.'),
 ('00-reading-guide',96,'These are the three actual source files, including open peer review. Deleting or changing the count would make the reference list less useful.'),
 ('04-eye-drift',36,'Detection, exclusion margins and manual inspection are the actual sequential segment-cleaning steps. Each changes what data enters the analysis.'),
 ('04-eye-drift',89,'Centering, joining and comparing are the actual rate-correlation procedure. All three steps are needed to explain the computed statistic.'),
 ('04b-eye-timing',37,'Estimating, independently checking and subtracting the apparatus plateau are distinct actual analysis steps, not ornamental parallelism.')]:reason('ai-tells.VerbTricolon',stem,line,why)

for stem,line,why in [
 ('00-reading-guide',37,'Taught describes the human-authored guide’s explanations, not cognition attributed to a machine.'),
 ('00-reading-guide',72,'Teaching derivation labels an educational reconstruction; the derivation is not said to think or learn.'),
 ('00-reading-guide',78,'Teaching reconstruction identifies the status of an illustrative model, not an intentional computer actor.'),
 ('04-eye-drift',89,'A one-sided test asks whether is conventional shorthand immediately resolved into its null reference and p-value. The test is not assigned human beliefs.'),
 ('04b-eye-timing',110,'Teaching reconstruction tells readers that the one-exponential example is simpler than the source’s fitted model; removing it would blur evidence status.'),
 ('04b-eye-timing',190,'The derivation teaches the distinction describes its purpose in this book, not a neural or software component with human agency.'),
 ('04b-eye-timing',200,'Teaching reconstructions identifies which formulas were derived for explanation rather than copied from the source.'),
 ('04c-eye-circuit',53,'Teaching derivation distinguishes the guide’s readout reduction from the paper’s displayed equations; no machine cognition is implied.')]:reason('ai-tells.AnthropomorphicCognition',stem,line,why)

for stem,line,why in [
 ('04-eye-drift',192,'A single cell is the experimental unit; removing single obscures why its prediction is noisier than the population-driven eye movement.'),
 ('04-eye-drift',235,'The sole source limits the rejected hypothesis to independent motor noise alone; it must not be removed.'),
 ('04-eye-drift',241,'The single-cell prediction must be distinguished from the true movement driven by the whole population.'),
 ('04-eye-drift',300,'The single-cell signal is the variable with large private prediction noise, unlike actual movement; the modifier identifies the object.'),
 ('04-eye-drift',342,'A single OMN is part of the quoted source subsection title and identifies the statistical explanatory-power question.'),
 ('04b-eye-timing',3,'A single interval length refers specifically to the previous 350ms analysis and motivates the next multi-lag calculation.'),
 ('04b-eye-timing',35,'A single position error must be contrasted with two endpoint errors; this determines the factor of two.'),
 ('04b-eye-timing',69,'A single power law would assert the same exponent at all lags; the word is needed for the finite-range caveat.'),
 ('04b-eye-timing',194,'The single-position variance is half the displacement-noise plateau under the stated independence assumption; single identifies which variance.')]:reason('ai-tells.FillerIntensifier',stem,line,why)

for stem,line,why in [
 ('00-reading-guide',103,'Inferred versus directly recorded is the central evidence limitation; deleting it would strengthen the 82% finding incorrectly.'),
 ('04-eye-drift',57,'This paragraph’s distinction is already stated by the figure caption; removal is proposed from the deletion test, not from a blanket ban on contrast.'),
 ('04c-eye-circuit',81,'The effective motor-unit contribution could be mistaken for a literal separate eye response. This contrast explains what Ei means before interpreting the average.'),
 ('04c-eye-circuit',94,'The hard-delay-cutoff misconception is plausible because the equation includes a 70 ms delay. The preceding explanation shows why MSD lag differs from time since perturbation.'),
 ('04c-eye-circuit',151,'Fixed-geometry scaling is different from a universal circuit formula. This scope statement is required to avoid overreading the proportionality.'),
 ('04c-eye-circuit',178,'These source-SI numbers support only an order-of-magnitude CV check; they must not be mistaken for a fitted full-model diffusion estimate.')]:reason('ai-tells.ContrastiveFormulas',stem,line,why)
for stem,line,why in [
 ('04-eye-drift',102,'Reversing the full-trial fit rather than refitting tiny residuals is the paper’s actual method and explains why the predictor has a calibrated gain.'),
 ('04-eye-drift',192,'SEM measures uncertainty in the mean, not cell spread or animal variability. This is a likely statistical confusion with a material consequence.'),
 ('04b-eye-timing',35,'The correction uses variance of two endpoint errors rather than one position error; the contrast explains a nontrivial factor of two.'),
 ('04b-eye-timing',71,'Ideal continuous-time white noise lacks finite pointwise variance; intensity versus point variance is necessary before the delta-covariance calculation.'),
 ('04c-eye-circuit',28,'The saturating synaptic rule differs from the earlier 2012 linear-synapse example. This distinction prevents applying the earlier normalization unchanged.')]:reason('ai-tells.StrawmanContrast',stem,line,why)

other=[
 ('ai-tells.ExplainerHeadings','00-reading-guide',1,'This frontmatter heading names the actual purpose: what evidence the three papers establish. It is specific to the book and is not a generic why-this-matters heading.'),
 ('ai-tells.CataphoricForecasting','00-reading-guide',3,'The book actually covers three papers; this is the subject being described, not a count used to manufacture a list.'),
 ('ai-tells.CataphoricForecasting','00-reading-guide',33,'The three contributions refer back to three completed paper summaries and compare their evidence types, rather than forecasting a list.'),
 ('ai-tells.CataphoricForecasting','04c-eye-circuit',182,'The five main figures are the actual set being mapped to inference steps in the table. The count has a reference role.'),
 ('ai-tells.CataphoricForecasting','04c-eye-circuit',254,'Two missing tests accurately enumerates the two absent experiments immediately below; the count helps bound the stated limitation.'),
 ('ai-tells.BareHolds','00-reading-guide',7,'Hold an angle while looking at a target is a concrete eye-control goal, not an unexplained claim that a result holds.'),
 ('ai-tells.BareReaches','00-reading-guide',19,'The image reaches the retina in the physical optical sense; the same sentence explains that the retina is light-sensitive tissue.'),
 ('ai-tells.ParallelStaccato','00-reading-guide',23,'The adjacent sentences distinguish a possible circuit explanation from the lack of unique localization. They make different necessary claims, not repeated sentence rhythm.'),
 ('ai-tells.ParallelStaccato','00-reading-guide',31,'Possible random connectivity and absence of direct connectivity measurement are different claims. The second limits the first and must remain.'),
 ('ai-tells.EmptyPaddingStacked','00-reading-guide',27,'Particular locations is the physical meaning of a place cell; markup after it is not padding.'),
 ('ai-tells.EmptyPadding','00-reading-guide',45,'Particular papers limits the following routes to a chosen paper interest. The phrase is ordinary and no simpler deletion preserves the distinction from the full-book path.'),
 ('ai-tells.EmptyPadding','04-eye-drift',3,'Particular source distinguishes the specific integrator proposal from the broader upstream location established by recordings.'),
 ('ai-tells.ServesAsDodge','00-reading-guide',33,'The colon is followed by concrete evidence roles for all three papers. It does not substitute an empty serves-as phrase for a mechanism.'),
 ('ai-tells.ServesAsDodge','04-eye-drift',102,'The paragraph explicitly identifies input and output when reversing the fitted relation; the colon supplies the mechanism rather than concealing it.'),
 ('ai-tells.ServesAsDodge','04c-eye-circuit',261,'The sentence supplies the precise link: internal diffusion becomes smooth, finite-lag superdiffusive mechanical output. It is not an empty claim about a connection.'),
 ('ai-tells.StackedAnaphora','00-reading-guide',64,'The parallel model-equation/derivation sentences contrast assumption with consequence, the central distinction needed here; their repetition is purposeful.'),
 ('ai-tells.FigurativeHolds','00-reading-guide',70,'A mathematical result holds means it follows under its assumptions. The surrounding text keeps assumptions visible and uses standard mathematical language.'),
 ('ai-tells.RestatementMarkers','00-reading-guide',80,'To clarify states the selection purpose for related work; the sentence distinguishes a targeted comparison from an exhaustive literature search.'),
 ('ai-tells.FigurativeCarries','04-eye-drift',13,'Neurons carry signals to other neurons describes neural transmission, not an unrelated metaphor. It distinguishes INNs from muscle-driving OMNs.'),
 ('ai-tells.MortalityMetaphors','04-eye-drift',30,'A common command survives averaging means its contribution remains when independent private deviations cancel. The preceding sentence gives the mathematical mechanism; no life/death meaning is suggested.'),
 ('ai-tells.ExplainerLeads','04-eye-drift',30,'This is why follows the explicit shared-versus-private averaging mechanism and links it to the noisy single-cell evidence. It does not merely announce an explanation.'),
 ('Google.Units','04-eye-drift',89,'Fig.1d is a panel label in the source figure, not the quantity one day. Preserve the source identifier.'),
 ('ai-tells.FillerPhrases','04-eye-drift',158,'Tends to zero states the limiting position change as a pulse narrows. Replacing it by equals zero would remove the limiting argument.'),
 ('ai-tells.ConsequenceParticiple','04-eye-drift',250,'Meaning the same one-for-one displacement scale explicitly defines unit gain; it is a necessary clarification of the assumption.'),
 ('ai-tells.ExplainerLeads','04b-eye-timing',48,'This is why draws the operational conclusion from a calculated 25% uncertainty and is grounded in the immediately preceding numbers.'),
 ('ai-tells.FillerPhrases','04b-eye-timing',90,'Tends to zero is the mathematical long-lag limit of kernel overlap. Exact zero at finite lag is not claimed.'),
 ('ai-tells.FillerPhrases','04b-eye-timing',128,'Tends to zero describes the partition-width limit defining the stochastic integral. Removing it changes the construction.'),
 ('ai-tells.NounString','04b-eye-timing',198,'Central source is the source subsection title quoted in a citation locator; timing argument identifies the relevant part of that source discussion.'),
 ('ai-tells.NegatedSubject','04c-eye-circuit',3,'Neither result identifies the circuit limits the two earlier inferences exactly where the integrator hypothesis is introduced.'),
 ('ai-tells.NegatedSubject','04c-eye-circuit',256,'No integrator neurons were recorded is a concrete absent measurement and a necessary limitation, not habitual negative framing.')]
for row in other:reason(*row)

for a in alerts:
    if a['severity']!='error':continue
    key=(a['rule'],Path(a['source']).name,a['line'])
    proposed=edits_by_line.get((a['source'],a['line']))
    why=None;decision='retain_exception';eid=None
    if a['rule']=='ai-tells.EmDashUsage':
        ranges=re.findall(r'[A-Za-z0-9.]+–[A-Za-z0-9.]+',a['source_line'])
        why=f"At {a['source']}:{a['line']}, the matched character is an en dash in a range ({', '.join(ranges)}), not an em dash inserting a prose aside. Preserve the exact chapter, figure, equation, page or time endpoints."
    elif a['rule']=='ai-tells.SemicolonUsage':
        if proposed:
            decision='revise';eid=proposed['id'];why=proposed['reason']
        else:
            assert a['source_line'].startswith('[^'),a
            why=f"At {a['source']}:{a['line']}, this semicolon separates source locators within the citation, not independent explanatory sentences. Retain the exact main/SI/page or equation references."
    elif a['rule'] in ['Google.Spacing','Microsoft.Spacing']:
        assert proposed;decision='revise';eid=proposed['id'];why='The extra space after the units sentence is a genuine spacing defect; the proposed full-paragraph repair removes it without changing notation.'
    elif a['rule']=='ai-tells.NounString' and a['line']==13 and Path(a['source']).name=='04-eye-drift.md':
        decision='revise';eid=proposed['id'];why=proposed['reason']
    elif a['rule']=='ai-tells.FillerPhrases' and a['line']==241:
        decision='revise';eid=proposed['id'];why=proposed['reason']
    elif a['rule']=='ai-tells.FormalTransitions' and Path(a['source']).name=='04c-eye-circuit.md' and a['line']==53:
        decision='revise';eid=proposed['id'];why='Additionally is unnecessary formality here; also retains the additive relation to deterministic drift.'
    elif proposed and not proposed['replacement']:
        decision='revise';eid=proposed['id'];why=proposed['reason']
    else:
        assert key in specific,('Missing individual alert judgment',key,a['id'])
        why=specific[key]
    row={'id':a['id'],'source':a['source'],'line':a['line'],'rule':a['rule'],'match':a['match'],'decision':decision,'reason':why}
    if eid:row['edit_id']=eid
    out['vale_decisions'].append(row)
assert {x['id']for x in out['vale_decisions']}=={x['id']for x in alerts if x['severity']=='error'}

field='Concrete wording and sentence contribution: phrase, plain-language paraphrase, actor, object, action or state change, condition or consequence, verdict, and replacement or retention reason'
def unit(suffix,line,phrase,paraphrase,actor,obj,action,condition,why,deletion,definition='The first-definition terms in this unit have a meaning supplied by the marked passage; later mathematical terms rely on the stated audience or earlier teaching.'):
    key=next(k for k in inp['units'] if k.endswith(suffix))
    related=[e for e in out['proposed_edits'] if key in e['affected_unit_ids']]
    status='open' if related else 'pass'
    verdict='revise' if related else 'retain'
    fields={field:f'line {line}; phrase: {phrase}; paraphrase: {paraphrase}; actor: {actor}; object: {obj}; action: {action}; condition or consequence: {condition}; verdict: {verdict}; replacement or retention reason: {why}',
      'Definition and emphasis':definition,
      'Deletion test':deletion}
    findings=[{'id':e['id'],'kind':'language','source':e['source'],'line':e.get('line'),'issue':e['reason'],'proposed_edit_id':e['id']}for e in related]
    out['units'][key]={'status':status,'findings':findings,'questions':[{'question':'What teaching contribution is lost if the reviewed explanation is removed?','answer':deletion,'source_refs':[key]},{'question':'Does the wording identify a real actor, object and consequence without unnecessary phrasing?','answer':fields[field],'source_refs':[key]}],'fields':fields}

unit('ch:READING-GUIDE',3,'how activity can retain a value','how neural signals keep representing a useful quantity','neural activity','stored values, eye control and location','represents and sometimes loses information','the three papers ask different questions',
'Retain the three-paper comparison and the heading What the three papers establish: both identify the actual scope. The three-item structure is required by the three source contributions.',
'Removing the first paragraph would leave the reader without the subject or the relationship between the three papers. The different setting and question for each source are useful, not filler.',
'Neuroscience is explained through nerve cells and behavior before specialist models appear. No new term is used as an unexplained computational premise.')
unit('sec:READING-FIELD',7,'Mathematical models connect assumptions about cells and their interactions to predictions','models work out consequences; recordings test them','models and recording analysis','assumptions, predictions and observed activity','derive and test','different tasks need a maintained representation',
'Keep the causal setup and all three concrete tasks. Split prose semicolons in the paragraph and matching sidecar; each clause supplies a distinct task or evidence role.',
'Deleting the behavior examples would remove the observable problem. Deleting the model/recording distinction would blur theory with experiment. No sentence should be deleted here.',
'Neuron is explained and blue-marked at the first teaching occurrence; the plural suffix remains outside the marked singular base.')
unit('sec:READING-MEMORY',11,'Yet the remembered value can change while the activity persists','continued firing need not preserve the correct value','neural network','represented value','keeps activity but accumulates error','the continuous family and noise assumptions delimit the result',
'Retain the contrast because persistence versus accuracy is the paper’s central problem. Retain weak-fluctuation and no-anchor qualifiers, and the explicit lower-bound language.',
'Removing the distinction between persistent activity and changing value would remove the scientific problem. The method summary and bound interpretation supply different necessary contributions; their three-part list is not ornamental.',
'Continuous family is explained by different patterns representing different values. The advanced methods are introduced as the later learning goals, not assumed vocabulary.')
unit('sec:READING-EYE',23,'The recordings do not uniquely locate the noise inside that memory circuit','the measurements support an upstream source but do not identify a unique circuit','recording analysis','source of displacement variance','supports a shared neural contribution','calibrated movement relation and noise assumptions',
'Retain the limit adjacent to the model explanation. Therefore in p19 connects retinal-image changes to the importance of understanding the movement.',
'Removing the 350 ms interval or variance object would make 82% ambiguous. Removing the calibration/noise conditions or circuit limit would strengthen the evidence. The apparent parallel sentence pair carries these separate jobs.',
'Fixational drift and retina are first defined in plain physical terms and blue-marked here; later eye chapters correctly use them without new first-definition marks.')
unit('sec:READING-PLACE',27,'becomes more active in particular locations','the cell fires more at some places than others','place cell','physical location and firing rate','responds more strongly at selected positions','connected active regions define its fields',
'Retain particular locations: in particular is not a transition in this sentence. Retain the wiring caveat and distinction among exact, approximate and empirical results.',
'Definitions of place cell, hippocampus and field are needed before the threshold model. Removing the two subsequent paragraphs loses the mechanism, predictions or evidence limits; the final cross-paper comparison supplies a distinct integration task.',
'Place cell, hippocampus and place field receive meanings in their blue-marked passages. The map is fixed over space, as later foundations explain; no moving temporal noise is implied here.')
unit('sec:READING-START',54,'The expandable notes preserve longer calculations and extensions','additional derivation steps can be opened when needed','reader','main path and expandable notes','chooses depth of reading','first reading still includes assumptions and results',
'Keep the actual chapter routes and audience baseline. Split the semicolon in p54 while preserving the option to inspect calculations.',
'Removing the baseline or routes hides which preparation each paper needs. Removing optional-reading guidance changes how the collapsible explanations are meant to be used. Chapter ranges are necessary locators, not em-dash prose.',
'The list of advanced subjects is a promise of teaching, not a collection of unexplained first-use definitions. Detailed adequacy of the full path remains the later flow stage.')
unit('sec:READING-MECHANISM-MATH',64,'An equation that specifies how a cell responds belongs to the model','a response rule is an assumption; derivation works out its consequences','model author and mathematical derivation','neural response rule','chooses a rule and derives its consequences','the neural prediction depends on circuit and spike statistics',
'Retain the two parallel sentences because they teach the core distinction. Split prose semicolons in p66 and p72, retaining the roles of projection, probability and original appendix access.',
'Removing the spike example would leave the model-versus-math distinction abstract. The readout example adds observer access, a different necessary condition. The appendix map is a practical source locator rather than a redundant full derivation.',
'Mechanism, derivation and interpretation are explained by their roles. Source titles and seven appendix-section labels remain exact.')
unit('sec:READING-SCOPE',82,'In the basic one-dimensional model','for this explicitly limited diffusion model','modeled coordinate','squared displacement','spreads with elapsed time','constant D, no bias and no boundary',
'Retain the assumptions attached to 2Dt and the distinction between numerical checks and reproduction of experiments. Teaching reconstruction is an evidence-status label, not anthropomorphism.',
'Deleting the scope paragraph would let a successful arithmetic check stand for an empirical reproduction. Deleting the conditions on 2Dt would overgeneralize it. The symbol list prevents later conflicts with the source’s theta.',
'Diffusion coefficient and mean squared displacement are first blue-marked and defined here. Later re-explanations should be reminders, not new first-definition emphasis.')
unit('sec:READING-PAPERS',99,'Several printed intermediate equations require care','the guide identifies apparent inconsistencies and shows its calculation','guide authors','printed intermediate equations','identify and explain apparent inconsistencies','these are independent checks, not author-confirmed corrections',
'Merge the vague require-care clause into the concrete identify clause. Delete These links open PDF files because all adjacent links already say PDF. Split the cover/page-number prose semicolon, preserving exact bibliography.',
'The published source identities, supplement distinctions and page-locator guidance are needed. The generic PDF sentence and general warning add nothing beyond more specific adjacent text; proposed edits retain that specific content.',
'Italicized phrases are work titles, not newly introduced terms. Author initials, journal details, source titles and page ranges remain unchanged.')
unit('ch:EYE-DRIFT',3,'Their model then proposes a particular source','the model tests one specific possible circuit origin','authors’ circuit model','shared changing command','proposes an origin for it','recording evidence establishes a broader upstream location',
'Retain particular source because it distinguishes the circuit hypothesis from the earlier shared-drive inference. The opening asks a physical question before previewing the comparison.',
'The bridge through muscles explains why internal diffusion cannot be compared directly with raw eye trajectories. Removing calibration from the third paragraph would leave no reason for the next recording and fitting sections.',
'Microsaccades is defined by brief rapid movement and matches the glossary. Fixational drift is correctly a reminder of its frontmatter definition.')
unit('sec:EYE-PATHWAY',13,'their eye movement response parameters','how firing changes with eye position and movement','researchers','recorded neuron types','separate OMNs from other neurons using responses','the classification is based on measured response relationships',
'Replace the unexplained noun string with the measured relationship. Retain the physical transmission wording carry signals and the shared/private averaging explanation; these are concrete neural actions.',
'The pathway, component roles and three possible noise locations are prerequisites for the inference. The averaging explanation is the reason one noisy cell can reveal shared drive, not an expendable summary.',
'Integrator, OMNs, abducens nucleus and ocular plant are blue-marked with local roles. The proposed classification repair avoids adding unexplained threshold and sensitivity terms before the forward-fit section.')
unit('sec:EYE-RECORDINGS',57,'The recording design provides one cell and eye movement at a time','one neuron and the eye are paired, not neuron pairs','experimenters','recordings','pair spikes with movement','cannot directly measure covariance between two recorded neurons',
'Retain the design and limitation in p34. Delete the announced-diagram sentence p49 and repeated after-figure paragraph p57 because the caption already supplies their physical-versus-analysis distinction. Split p34/p36 semicolons.',
'Deleting p34’s design limit would damage the later upstream inference. Deleting p49 and p57 does not: p34 and the figure caption preserve all their content. Keep p47’s gain reminder, but move its first-definition marking to the actual earlier teaching.',
'Gain is already adequately taught at 01-foundations.md:129 and 167. Its late blue marker at p47 is a first-definition placement error. Proposed eye edit removes that marker; the earlier marking needs coordinator integration.')
unit('sec:EYE-FORWARD-FIT',78,'m is not a direct measurement of the eye’s mass','the fitted acceleration coefficient is not a measured mechanical mass','fitted relationship','motor firing rate','combines position, velocity and acceleration terms','coefficients describe combined neural/mechanical behavior',
'Retain this likely misconception correction and the full model/units explanation. Split p78 and p89 prose semicolons. Preserve the source panel label Fig.1d and actual three-step correlation procedure.',
'Removing the term-by-term roles leaves the equation uninterpreted. Removing full-trial leave-one-out, threshold or p-value limits changes how the evidence should be read. The prose contrasts have concrete scientific work.',
'The p value definition states the reference distribution rather than claiming a probability that the hypothesis is true. Its marked name matches the glossary.')
unit('sec:EYE-INVERSE-FILTER',158,'tends to zero','approaches zero as the pulse duration shrinks','position response','narrowing unit-area pulse','has vanishing position change while velocity jumps','the limit determines impulse-response coefficients',
'Retain the limit language, algebraic connectors and raw-fit-versus-inverse distinction. Split prose semicolons; replace the step function’s imposes-causality clause with its concrete zero-before-input effect. Remove the repeated not-a-recorded-fit sentence at p176.',
'The factorization, impulse response and static-gain example each answer a different question: decay times, weights and calibration. Deleting any breaks the derivation. The repeated denial of fitting adds no information beyond p169’s constructed label.',
'Causal filter, impulse response, convolution and SEM are defined with their roles and conditions. SEM’s contrast with cell/animal variation is necessary, not a strawman.')
unit('sec:EYE-SHARED-VARIANCE',235,'independent OMN noise as the sole source','all motion arising only from independent motor fluctuations','independent-noise hypothesis','movement variance','fails the explained-variance bound','the sampled average must represent the motor population',
'Retain sole: it limits the hypothesis rejected. Retain the bound’s Consequently/Thus links, rescaled-R-squared definition and representative-sample condition. Split the population-size semicolon.',
'Removing the residual-variance proof would turn the 1/Nm rule into an unsupported assertion. Removing representativeness or independence would change its applicability. The 2.9% versus 0.1% comparison demonstrates why the result matters.',
'Coefficient of determination is explicitly restricted to an optimized linear prediction, consistent with its glossary meaning.')
unit('sec:EYE-CHI',241,'uses the fact that the inverse filter has a calibrated gain in degrees','uses the calibrated inverse-filter gain','analysis','calibrated displacement predictions','extracts common variance through covariance','unit common gain and negligible cross-covariances',
'Remove the fact that while retaining calibrated gain. Delete the repeated denominator explanation at p310, keeping the bars’ common-scale guidance. Retain single cell, unit-gain definition and weighted-error conditions.',
'The covariance expansion, example and uncertainty weighting do different jobs and must stay. The repeated p310 sentence is already explained at p279 and in the figure caption; removing it loses no mechanism.',
'Chi is introduced as the common variance fraction in the equations and surrounding prose. No extra blue term is needed for a symbol whose role is locally stated.')
unit('ch:EYE-TIMING',3,'a single interval length','the earlier 350 ms comparison only fixes one lag','previous analysis','shared displacement variance','estimates a fraction at one lag','does not determine how changes accumulate across lags',
'Retain single because it motivates the new measurement. The chapter opening gives a different question from the previous fraction calculation and separates recording error from physical motion.',
'Deleting the single-interval limitation would leave the reason for the multi-lag comparison unstated. The two candidate inputs are needed setup for the later filtered-MSD derivation.',
'MSD is a reminder, not a newly marked definition. Filter and stochastic-process terms are introduced in the detailed section before calculations use them.')
unit('sec:EYE-MEASUREMENT-NOISE',48,'an estimated noise contribution','a measured estimate of the apparatus offset','analyst','observed MSD','subtracts an estimated offset','uncertainty in the estimate can dominate the remainder',
'Retain estimated: the uncertainty is precisely the lesson. Split the correlated-noise caveat semicolon. Remove the repeated offset/unknown-trajectory warning at p58 while preserving why the Brownian illustration was chosen.',
'Removing the two-endpoint derivation loses the factor of two. Removing zero-lag or correlated-error conditions changes the result. The repeated p58 explanation is already in p35,p37 and the caption, so its deletion is safe.',
'Single-position error is needed to distinguish its variance from the difference of two errors. The experiment/example distinction is explicit.')
unit('sec:EYE-FILTERED-MSD',128,'the limit of these weighted sums as h tends to zero','a stochastic integral is built from increasingly fine weighted increments','integral construction','Brownian increments','sums their surviving contributions','increments on disjoint intervals are independent',
'Retain precise limit language, source/model contrasts and the one-pole simplification. Split prose semicolons in p69,p118,p178 while preserving finite-lag scope and distinct time constants.',
'Removing the weighted-sum explanation would require unexplained stochastic calculus beyond the audience baseline. Removing covariance-to-MSD steps loses the reason for the curve. The example is simpler than the full model and explicitly bounded.',
'Superdiffusion, low pass filter, white noise and stationary process are blue-marked with definitions. White-noise intensity versus finite pointwise variance is essential, not decorative contrast.')
unit('ch:EYE-CIRCUIT',3,'Neither result identifies the circuit','the two established results do not choose a unique source circuit','recording and timing evidence','circuit identity','constrains but does not determine it','the next model is a possible explanation',
'Retain the negative statement because it prevents a likely overreading exactly as the model begins. The opening’s parameter-freedom sentence raises a real test of how informative a match is.',
'Deleting the limit would turn a model hypothesis into an apparent experimental identification. Deleting the output path would make model and measured motion look directly comparable.',
'Previously taught integrator, motor neuron and muscle roles are reused without duplicate blue definitions.')
unit('sec:EYE-CIRCUIT-MODEL',53,'perturbations along the nearly neutral direction additionally accumulate','random changes accumulate in addition to possible deterministic drift','spiking noise','stored coordinate','adds lasting random changes','the optimized continuum is approximate',
'Use also for the needed additive connection. Split the identified prose semicolons while retaining exact formulas, state changes, approximate persistence and the causal delay explanation.',
'Every model stage supplies a new input/output or interpretation. The full-loop description is needed to understand recurrence. The limits on exact neutrality, active units and lag interpretation prevent plausible mathematical mistakes.',
'The first use of each S,X,EOI,Ei and feedback symbol gives a role and units. No new model label is treated as self-explanatory. The source-versus-teaching-derivation distinction is necessary.')
unit('sec:EYE-SCALING',151,'a comparison under fixed network geometry and noise assumptions','scaling applies only while the stated circuit and noise properties remain comparable','parameter comparison','diffusion scale','changes with the controlled parameter','absolute and fractional rate slopes are different controls',
'Retain the fixed-geometry limitation, the source normalization ambiguity and the two rate comparisons. Split prose semicolons and correct the duplicate space. Preserve renewal/CV terms and physical units.',
'Removing constant-rate qualification makes the renewal derivation too broad. Removing one slope definition reverses the meaning of a rate change. The CV-drift estimate checks a separate possible source of variability and is not redundant.',
'Sub-Poisson spiking and renewal process are defined under the construction actually used. CV was taught earlier and is recalled without a duplicate blue marker.')
unit('sec:EYE-FIGURES',190,'internal stochastic spikes remain in the latter comparison','the noise-removal control keeps the spikes that cause diffusion','model control','internal and direct-output spiking','removes direct output noise but retains internal diffusion','comparison does not turn off the entire noise mechanism',
'Retain the five-figure reading table as a reference connecting panel evidence to claims. Split the negative-estimate semicolon and explanatory footnote semicolon, preserving source locators.',
'The table does not redo the derivations; it tells the reader how to inspect source panels. The ED10 sentence supplies a crucial distinction not obvious from its short no-noise legend. Removing that sentence would misdescribe the control.',
'The table reuses established R,chi,MSD and model roles; their abbreviation use is appropriate in this later reference section.')
unit('sec:EYE-LIMITS',256,'No integrator neurons were recorded in this study','the source circuit was not directly observed','experimenters','integrator neurons','did not record them','source identity remains open',
'Retain this concrete negative evidence and the second missing perturbation test. Retain the parameter-degeneracy statement and output-filter connection; they explain what the result permits.',
'Deleting either missing test would weaken the reason the circuit is not uniquely identified. The closing result is needed to connect this experiment back to the memory theory and forward to synthesis.',
'The alternatives reuse the pathway’s established roles. No needless technical term or repeated first-definition marker was found.')
unit('part:OBSERVATIONS::part-opening','Part purpose','which connections remain untested','which links between the studies still need evidence','synthesis chapter','connections across memory, eye and spatial studies','compares what is established','eye and spatial studies address different parts of neural representation',
'Retain the current Part title and concrete purpose. They explain the transition from memory theory to eye and spatial observations without claiming one demonstrated circuit.',
'Removing the chapter-group roles would hide why the two different observational studies share a Part. Removing untested connections would overstate what their combination establishes.',
'Neural code was taught in foundations; hippocampal nerve cells is a plain reminder. The opening adds no undefined algorithm or model name.')

assert set(out['units'])==set(inp['units'])
out['cross_group_findings']=[{'id':'eye-first-gain','source':'content/chapters/01-foundations.md:129','issue':'First adequate gain teaching precedes its blue marker at 04-eye-drift.md:47. Mark the singular base gain in the earlier foundation passage and retain the later sentence only as a plain reminder.','related_edit_id':'eye-L10','status':'open','owner':'coordinator and memory group'}]
out['landing_fields']={
 'content/index.md:1':{'decision':'retain','reason':'The title names the three-paper subject rather than advertising a generic overview.'},
 'content/index.md:3':{'decision':'retain','reason':'Nerve cells, stored values and the animal recording settings identify the subject concretely. The three-way list reflects actual papers, not a writing pattern to remove.'},
 'content/index.md:5':{'decision':'retain','reason':'The audience baseline and reading-route instruction are necessary for using the guide. The teaching-before-calculation promise must remain subject to the full flow review.'},
 'guide-project.yaml:guide.description':{'decision':'retain','reason':'The description tells a prospective reader what settings and explanations the guide contains. Its neuroscience terms have ordinary reminders and no unnecessary product or authoring vocabulary.'}
}
out['sidecar_reader_fields']={'reviewed':['00-reading-guide.yaml purpose and eight section summaries','04-eye-drift.yaml purpose and six section summaries','04b-eye-timing.yaml purpose and two section summaries','04c-eye-circuit.yaml purpose and four section summaries'],'proposed_repairs':[e['id']for e in out['proposed_edits']if e['source'].endswith('.yaml')],'retained':'Purpose lines give concrete behavioral questions and preserve possible/proposed circuit language. The summaries that repeat repaired first paragraphs need the five matching narrow edits; no title changes are required.'}
out['advisory_review']={
 'alerts_reviewed':len([a for a in alerts if a['severity']!='error']),
 'judgment':'Read warnings and suggestions in their paragraphs, including flagged passive voice, sentence lengths, parentheses, adverbs and terminology. No automatic style substitutions were used.',
 'retained_examples':[
  'Firing is the scientific term for spike production; replacing it as an employment euphemism would be wrong.',
  'Fitted, sampled and recorded passive clauses keep the relevant measurement or quantity in focus; the authors are already identified, so the actor is not concealed.',
  'Approximate, nearly, slowly, finite and independent qualify mathematical conditions. Smoothly describes actual movement. These are not removable intensifiers.',
  'EYE and FIT in heading-acronym alerts are anchor IDs, not displayed unexplained acronyms. MSD is already defined before the substantive timing headings.',
  'Estimated noise contribution at timing p48 is necessary because uncertainty in that estimate is the point of the calculation.',
  'Author initials, journal punctuation, source figure identifiers and numeric equation/page ranges retain their literal forms.',
  'Long definitions of p value, white noise and sub-Poisson firing contain necessary conditions; shortening by dropping them would create a teaching or truth defect.'
 ],
 'repairs':'Prose semicolons not selected by the custom error rule were also inspected and proposed for repair, including eye p34/p141 and circuit p28/p72/p116/p151 and the explanatory feedback footnote.'
}
out['suppression_limits']='Only the individual retain_exception judgments authorize considering narrow native Vale rule comments at their cited passages. No rule-profile, severity or broad-disable change is proposed. Comments should not suppress a neighboring real prose semicolon or a separate unresolved wording issue.'
out['call']['completed_at']=datetime.now().astimezone().isoformat()
out['summary']={'open_units':sum(u['status']=='open'for u in out['units'].values()),'pass_units':sum(u['status']=='pass'for u in out['units'].values()),'proposed_edits':len(out['proposed_edits']),'error_revise':sum(d['decision']=='revise'for d in out['vale_decisions']),'error_retain_exception':sum(d['decision']=='retain_exception'for d in out['vale_decisions'])}
sources={u['source'] for u in inp['units'].values() if (guide/u['source']).is_file()}
sources.update({'content/index.md','guide-project.yaml'})
sources.update(s.replace('.md','.yaml') for s in list(sources) if s.startswith('content/chapters/') and (guide/s.replace('.md','.yaml')).is_file())
out['source_snapshot_sha256']={s:hashlib.sha256((guide/s).read_bytes()).hexdigest() for s in sorted(sources)}
out['validation']={'unit_ids':'all 25 match the assigned input','vale_error_ids':'all 190 matched exactly once','proposed_originals':'all 40 matched the current full paragraph or YAML field','repair_references':'all revise decisions point to existing edit IDs','manuscript_changes':'none'}
(root/'eye-stage2.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
elapsed=(datetime.fromisoformat(out['call']['completed_at'])-datetime.fromisoformat(out['call']['started_at'])).total_seconds()
report=f'''# Eye and frontmatter Stage 2 language review

Started: {out['call']['started_at']}. Completed: {out['call']['completed_at']}.
Wall-clock elapsed: {int(elapsed//60)}m {int(elapsed%60)}s. Awake execution time unverified. Token stats unavailable.

Reviewed all 25 assigned units and 236 paragraphs, including equations, captions, footnotes, headings, landing text and the assigned sidecar purposes and summaries. No manuscript or Stage 1 report changes were made. Figure pixel acceptance remains deferred.

The report leaves 16 units open and 9 passing for this stage. It proposes 40 exact edits: 35 Markdown paragraphs and five matching navigation summaries. All proposed originals were checked against current source. These are proposals, not completed fixes.

The main changes split real prose semicolons, remove repeated explanations around figures, replace one unclear early noun string, remove “the fact that”, and correct a duplicate space. The deletion judgments preserve necessary assumptions, source limitations, units, physical actors and calculation steps. Scientific firing, numeric ranges, author initials, mathematical limits and actual logical connectors are retained.

All 190 Vale error IDs have an individual decision: 31 revise and 159 retain as exceptions, each with a passage-specific reason. The other 435 warnings and suggestions were also reviewed in paragraph context. Retained alerts do not justify broad profile or severity changes. Any native Vale comments must be limited to the independently judged passage and rule.

One definition issue crosses the review groups: gain is adequately taught in foundations at line 129 before the blue marker in eye drift at line 47. Edit eye-L10 removes the later marker while retaining its short reminder. The coordinator must arrange the earlier marker with the memory group to close this issue.

Landing text and existing titles are retained. Five sidecar summaries need the same local repairs as their chapter paragraphs. Global order and flow remain for the separate flow review.

Machine-readable decisions, full original/replacement paragraphs, affected unit IDs, source hashes and all Vale error decisions are in eye-stage2.json. The source-hash snapshot records this review's current files.
'''
(root/'eye-stage2.md').write_text(report,encoding='utf-8')
print(out['call']['completed_at'],out['summary'])
