from pathlib import Path
from datetime import datetime
import json,re,hashlib
task=Path('C:/dev/clsc/burak-papers/guide/verification/prose-structure-20261024')
notes={
'00-reading-guide.md':'''Connects three concrete behaviors before technical terms.
Defines neuroscience and neuron by the cells' role; brain wording suits this opening.
Sets up persistence versus accuracy, so the later diffusion result answers a need.
Separates model, approximation, simulation and inference steps without calling them all measurements.
Keeps lower bound, time-dependent uncertainty and the limits of its model together.
Teaches drift and retina in the sentence that explains why retinal motion matters.
Explains calibration and the separate circuit-model test before interpreting either.
All numerical scope and noise/calibration conditions are necessary to the 82 percent interpretation.
Place cell, hippocampus and place field have immediate plain meanings.
Gives model input, threshold operation, measured dimensions and fitting role.
States predicted irregular features and the missing connectivity measurement; no empty claim of a universal mechanism.
Connects the three contributions while keeping a combined-circuit question open.
Audience baseline and chapter progression explain how to use the list.
Chapter labels map complete chapter groups to their teaching contributions; separate bullets help lookup.
Introduces the two alternative reading paths without making either a required detour.
The two path labels name the papers and keep the specific place-field prerequisite exception.
Glossary, references and paper-figure functions are different and useful to state once here.
Supplies the specific guide-map destination after foundations.
Explains optional folds and that prerequisites remain in main text; needed for reading decisions.
Delete the first sentence because it only praises the level of detail; the remaining sentences explain numerical and teaching scope.
Distinguishes interpreting evidence, numerical checks and empirical reproduction; these qualifications cannot be cut.
Defines D and MSD together with the exact setting in which MSD equals 2Dt.
Short introduction identifies the symbol list as recurring notation.
Symbol bullets separate d, memory theta, threshold q and covariance C without unnecessary definition prose.
Distinguishes main published copies from supporting information before the links.
Three source entries retain publication identities, separate supplements and local-PDF page conventions.
Explains PDF behavior and apparent source-equation errors without claiming author-confirmed corrections.'''.splitlines(),
'01-foundations.md':'''Gives behavioral reasons for studying variable signals before definitions.
Preview explains the dependency from representation through counts to covariance and drift.
Spike and firing-rate definitions have a concrete 20 Hz interpretation.
Synapse definition introduces the receiving-cell effect comparison.
Two bullets expose opposite effects, and the inhibitory pronoun points to the preceding tendency to fire.
Explains persistence through decaying synaptic effects and recurrence rather than a bare term.
Tuning curve is defined with role, units and negative-rate limit before use.
Introduces the population vector with the required neuron differences.
Population code, encoding and decoding meanings connect directly to the vector and memory problem.
Spatial rate-map teaching retains a useful local reminder after the reading guide and adds the estimator and uncertainty.
Introduces the specific anatomical comparison rather than repeating a heading.
The CA3/CA1 bullets reveal different recurrent excitation and input relationships.
Grid-cell explanation adds a distinct spatial pattern and keeps map output separate from state maintenance.
New transition links expected tuning to variable spike observations before the Poisson formula.
Expected-count units prepare the mean and variance interpretation.
Factorial-moment algebra is short and necessary for the optional variance derivation.
Explains relative count noise and why comparing networks requires fixed quantities.
The example title names its two learning outcomes rather than adding a new term.
One-cell numbers make apparent silence understandable under a positive rate.
Population comparison explains averaging and retains the shared-drive exception.
Introduces the common plotted scale needed to compare the two distributions.
Interprets normalization after the figure and keeps a precise source link.
Conditional independence explanation prevents confusing recurrent spike trains with independent count innovations.
Introduces two measurements that will be contrasted.
CV and Fano definitions measure different objects; interval meaning is supplied directly and no extra glossary detour is needed.
The explicit no-substitution conclusion is necessary after the metric comparison.
Delete the second sentence because saying identities are short and interpretation matters adds no identity or interpretation.
Covariance name and centered-value meaning prepare its formula.
Units and variance-of-sum identity are needed to interpret later shared fluctuations.
Independence versus zero covariance is a needed warning before correlation normalization.
Correlation range, nonzero-variance condition and no automatic causal fraction are essential.
Defines displacement and time lag before the MSD split.
Explains why MSD alone mixes random spread and mean motion; prepares the next chapter.'''.splitlines(),
'01b-persistence.md':'''Introduces the difference between neural activity and the represented value before geometry.
Explains why the example precedes diffusion and why fixed spatial randomness comes last.
State, fixed point and directional stability are explained in ordinary terms.
Continuous attractor, neutral direction and manifold meanings remain together with their distinct dimensions.
The example title states exactly what is compared.
Sets neuron activities, rates and angular units before the example equations.
The positive-rate domain and both coordinate meanings are required to use the example.
Introduces the assumed dynamics at the point of calculation.
The inverse-time unit and adding/subtracting operation support the equations that follow.
Interprets decay versus retained angle, so the two disturbances have a criterion.
The same starting state makes the following bullets alternatives, not consecutive perturbations.
Both full disturbance traces belong together as a comparison and keep intermediate values.
The wrong-angle conclusion is explicitly tied to the second case.
Explains both arrow meanings before the figure can be misread as flow in both directions.
Keeps illustrative-model scope and motivates the nonperpendicular projection derived later.
Defines increments and equal-duration setup before listing premises.
Three independent assumptions deserve bullets and retain units.
Introduces accumulated n-step quantities without inventing a numbered procedure.
The substitution t equals n delta-t leads naturally into the continuous approximation.
Brownian motion is defined before its later covariance is needed; physical-network approximation limits remain.
MSD and RMS meanings retain the 1D and equal-coordinate-D qualifications.
The second example title identifies the comparison with fixed bias.
Numbers illustrate D units and elapsed time without being passed off as empirical estimates.
Constant bias is introduced as an additional assumption before the formula.
The crossover and separate-drift conclusion interpret the numerical comparison.
Introduces the two different kinds of evidence in the figure.
The individual-path warning and bias-versus-root-time comparison are required figure interpretation.
Brownian covariance derivation needs the decomposition and independent increment, so keep connected prose.
Explains why the covariance will matter for averaging a moving memory.
Finite range, periodicity, feedback and state dependence limit the basic result.
Clearly distinguishes randomness over space from randomness over time.
Explains coexistence and why neither paper's measurements determine the other quantity.
Introduces the map by the shared question being compared.
The map's limit prevents reading it as evidence of one joint circuit.'''.splitlines(),
'02-memory-dynamics.md':'''The opening distinguishes firing persistence from retaining the supplied value.
The calculation path links spike renewal, surviving displacement and tuning-based diffusion.
PDF navigation instructions explain the limits of exact viewer placement.
Notation and units are needed before the synaptic model; repeated D is a useful chapter-local reminder.
Structural heading separated by an extra newline, with no prose decision needed.
Feedback cycle explains the puzzle before the equation.
Defines spike count and activation update objects.
The alternative spike-time notation introduces the exponential sum.
Initial-transient and dimensionless-activation conditions clarify the sum.
Introduces the spike/activation figure with its illustrative event count.
Interprets the distinction between discrete events and retained activation.
Defines firing-rate units and introduces the input/rate rule.
Weights, bias and transfer function roles are taught before use; the example range remains qualified.
Conditional independence and short-interval condition are needed for the stochastic moments.
Kronecker symbol and mean/fluctuation split teach the equation's meaning.
Weak fluctuation approximation has a mechanism, not merely a blue name.
Brownian units and the distinction from Gaussian whole spike trains are essential limits.
Population scaling and preferred-angle meaning explain why the approximation can hold.
Connects deterministic dynamics and fixed states using prior attractor teaching.
Warns that an arbitrary recurrent circuit does not automatically have the required continuous family.
Identifies lasting displacement as the quantity the next calculation must extract.
Linearization definition specifies retained and discarded orders.
Fixed-point cancellation explains the appearance of the linear dynamics.
Fixed-point noise evaluation and K units define the local scope.
Introduces the tangent displacement before assigning its eigenvector role.
The derivative and chain rule explain why the tangent is a zero mode.
Right-zero-vector meaning is immediately explained; other-mode decay remains necessary.
Left-zero-vector is an exact needed term, introduced by its defining equation.
Normalization and stable-mode calculation explain why the left vector extracts the lasting shift.
The zero product conclusion justifies discarding decaying modes.
Explains why a perpendicular projection can be wrong, including symmetric-W versus nonsymmetric-K distinction.
The two-variable example isolates the geometry with fewer prerequisites than a new network simulation.
Gives initial state and decaying-coordinate solution before the final shift.
The explicit vectors explain the vertical-perturbation consequence and preserve illustrative scope.
Introduces the trajectory figure by the error it resolves.
Interprets the figure's particular unit shift through the left vector.
Projection multiplication follows directly from the just-derived left-vector identity.
Independent-increment covariance supplies the variance calculation, so connected prose is appropriate.
Matching 2D dt sets the convention and source connection.
Contribution interpretation prevents treating rate alone as a complete damage comparison.
Two temporal requirements need to be visible separately after the local weak-noise limit.
Both bullets specify the allowable interval, not independent optional choices.
Explains their local consequence and why drift is a separate next question.
The multi-coordinate extension states normalization before the tensor equation.
Diffusion tensor has a plain matrix meaning and explains diagonal/off-diagonal entries.
The question motivates the symmetric-weight simplification.
Derivative definitions prepare the fixed-point identities.
Symmetry is invoked where it permits transposing the equation.
Proportionality and normalization follow the left-vector calculation.
The tangent normalization explicitly connects the denominator to the previous equation.
Printed-source qualification, inverse-function range and source locators are necessary; keep them before the conditions.
Three simultaneous premises are easier to find as bullets.
Translation-symmetry statement rules out an unnecessary restriction after the list.
Two-cell example states connectivity, biases and valid transfer range before its fixed states.
Sum/difference coordinates and left/right vectors explain its constant diffusion.
Positive-rate boundary limit prevents extending the interior formula to invalid rates.
Plot parameter values specify the teaching display.
Interprets the fixed rate sum as the reason for constant D in the interior.'''.splitlines(),
'02b-memory-long-delays.md':'''Three concrete ways a local error rate can fail at long delays motivate the chapter.
The roadmap explains density, drift and the storage/readout distinction in their dependency order.
Notation reminder retains constant-D, boundary and drift conditions.
Local-versus-long-time distinction motivates a density equation without introducing new terms first.
Itô evaluation rule gives the needed operational meaning before the Fokker Planck equation.
Dirac delta is explained as a point mass and distinguished from the prior discrete delta symbol.
Wrapped Gaussian construction teaches angular error reporting; source-mapping sentence can stay because it explains the alternate notation.
Plateau interpretation prevents confusing bounded error with disappearing noise.
Plot D and units fix the displayed example.
Figure interpretation compares uniform angular density, bounded wrapped error and unbounded line error.
The test-function calculation supplies the optional derivation's starting object and moments.
Small-order remainder and averaging explain the passage to expected density change.
Boundary alternatives and integrating twice explain why derivatives move onto Dp.
State-dependent D and boundary conditions precede the two moment identities.
The new To obtain introduction states the actual integration operation rather than empty completeness wording.
Linear-D case is a useful counterexample to assuming state dependence always curves the variance graph.
Mutual-excitation example states its weights and coordinate before applying the tensor/projection result.
Explicit factor-two source discrepancy prevents a silent convention change.
Separates spread and mean motion in plain language before naming systematic drift.
Systematic-drift definition and microscopic-process limit are needed, not removable caution.
Stratonovich rule and conversion explain why equal written coefficients can yield different processes.
Different orders of random and mean displacement explain cancellation limits without promising a realizable decoder.
Conditional independence versus recurrent correlations limits the Poisson formulas; the joint-likelihood requirement is essential.
Figure-1 flow instructions make the abstract lasting-state definition concrete.
Activity bump definition gives the population object before the two-error contrast.
Storage motion and finite-spike reading uncertainty are genuine parallel quantities.
The information/readout links explain which uncertainty is treated next.
Rate curves, spike marks and angular trace are distinguished so the reader knows what is being compared.
Introduces two complementary panel questions.
Panel bullets keep formula agreement separate from bound equality and wrapped long-time error.
Second network design tests generality of projection, while simulation-versus-animal scope remains clear.
The closing transition identifies the completed dynamical quantity and the next information question.'''.splitlines(),
'06-synthesis.md':'''The opening states the three different explanatory tasks without self-praise.
The path from separate objects to a shared-position calculation and joint experiment is useful.
Introduces three real questions instead of a numbered method.
Map, memory motion and observed movement labels separate the three roles and keep the eye account conditional.
Different position symbols refer to different physical/mathematical objects, so this paragraph is essential.
The guide-map link supports comparison without replacing the nearby explanation.
The new transition specifies the missing motion model after the static place map.
The assumed fixed map and changing estimate are both defined before the composition equation.
The fixed-function versus changing-input distinction and extra spike variability are necessary.
The small displacement, zero mean and variance conditions precede linearization.
Centered rate changes are connected to the covariance calculation in prose.
All local linearization and noise-source limits prevent reading the equation as general recurrent covariance.
The numeric slopes, D, duration and units make the example checkable.
Opposite slopes explain anticorrelation without implying inhibitory connectivity.
The 10 Hz baseline introduces the figure's positive-rate display.
The line geometry and private-noise contrast interpret the figure.
Plain one-direction wording explains the result and tells what must be measured next.
The new transition connects predicted changes to required measurements before comparing evidence.
Place-field bullet keeps fitting, extra gain and finite-threshold checks separate.
Eye bullet keeps calibration, source correlations, animals and movement direction attached to inference.
Memory bullet contrasts a mathematical bound with fitting and prevents 1/N alone becoming a full test.
Introduces related studies by the assumptions and open questions they address.
Integrating movement label unites eye integration and navigation; path integration is immediately explained.
Capacity and synaptic-change label accurately groups changes to storage assumptions.
Large-environment label keeps data origins distinct and preserves the later CA3/CA1 contrast.
Connectivity/learning label states the actual alternative mechanisms; dendrite explanation is short and sufficient here.
Perceptual-benefit label distinguishes a possible use of motion from identifying its source.
Same-population requirement and possible-sequence wording set scope before the ordered test.
Four steps have a real dependency order and the behavioral filter step stays conditional.
The conclusion preserves both fit limitations and the status of the joint proposal.'''.splitlines()}
rows=[]; files=[]
for n,why in notes.items():
    path=task/'proposed/content/chapters'/n; t=path.read_text(encoding='utf-8')
    ps=[p for p in t.split('\n\n') if p.strip() and not p.startswith(('#','$$','<','{{',':::','[^'))]
    assert len(ps)==len(why),(n,len(ps),len(why))
    for i,(p,w) in enumerate(zip(ps,why)):
        a=t.index(p)
        rows.append({'file':n,'paragraph_index':i,'start_line':t[:a].count('\n')+1,'paragraph_sha256':hashlib.sha256(p.encode()).hexdigest(),'opening':p[:160],'decision':'revise' if w.startswith('Delete') else 'retain','necessity_and_terminology':w})
    files.append({'path':str(path),'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'prose_and_list_units':len(ps),'scope':'Every prose paragraph, list group and example label read. Equations and source footnotes retained as required evidence. Pure markup excluded from wording decisions.'})
repairs=[]
for n,start,old,new,why in [
('00-reading-guide.md','The central theory','The central theory is derived step by step. Examples chosen for the guide distinguish independent from shared fluctuations, complete from limited access to neural signals, and exact formulas from approximations for rare fields. Their numbers are checked separately from the published experimental measurements. A teaching reconstruction is labeled when its simplified model differs from the paper\'s full model.','Examples chosen for the guide distinguish independent from shared fluctuations, complete from limited access to neural signals, and exact formulas from approximations for rare fields. Their numbers are checked separately from the published experimental measurements. A teaching reconstruction is labeled when its simplified model differs from the paper\'s full model.','The first sentence only asserts that the guide derives theory in detail. The remaining paragraph explains the concrete scope and evidence distinctions.'),
('01-foundations.md','To identify where','To identify where variability enters a pathway, the eye paper compares measurements that share some fluctuations and have other fluctuations of their own. The required probability identities are short, but their interpretation matters.','To identify where variability enters a pathway, the eye paper compares measurements that share some fluctuations and have other fluctuations of their own.','The removed sentence gives neither an identity nor its interpretation. The first sentence supplies the purpose and the next paragraph defines covariance directly.')]:
    t=(task/'proposed/content/chapters'/n).read_text(encoding='utf-8'); assert t.count(old)==1
    repairs.append({'file':n,'start_line':t[:t.index(old)].count('\n')+1,'kind':'wording deletion','before':old,'after':new,'reason':why,'premises_and_limits_preserved':'No scientific statement, assumption, formula, source, interpretation step or scope limit is removed.','review_route':'Stage 2 wording recheck plus Stage 3 connected read; Stage 1 unaffected because only empty commentary is deleted.'})
g=task/'proposed/content/chapters/glossary.md'; gt=g.read_text(encoding='utf-8'); grows=[]
for term,why in [('encoding','Short action definition matches its contrast with decoding.'),('excitatory input','Receiving cell and direction of effect are explicit; keep model scope.'),('inhibitory input','Receiving cell and reduced firing tendency are explicit; keep model scope.'),('neuron','Everyday signaling-cell phrase supplies the family without anatomical detail irrelevant here.'),('retina','Location plus light sensitivity supplies exactly the role needed for image motion.'),('hippocampus','Memory/navigation role is sufficient before place-cell teaching.'),('dendrite','Branching input structure supplies exactly the object needed for the learning paragraph.'),('path integration','Updating position from movement is the shortest useful meaning before the velocity-driven model.')]:
    line=next(l for l in gt.splitlines() if l.startswith('- [**'+term+':**]'))
    grows.append({'term':term,'entry':line,'decision':'retain','reason':why})
report={'request_id':'stage2-foundations-synthesis','stage':2,'reviewer':'/root/structure_place, GPT-6.1-sol/high','started_at':'2026-10-24T21:41:55.9489131+03:00','completed_at':datetime.now().astimezone().isoformat(),'awake_execution':'unverified','scope':'Separate necessity and terminology review of every paragraph in six actual proposed chapters plus eight assigned glossary entries. No edits.','source_files':files,'paragraph_assessments':rows,'small_repairs':repairs,'glossary_sha256':hashlib.sha256(g.read_bytes()).hexdigest(),'glossary_assessments':grows,'other_findings':[],'verdict':'Two small wording deletions recommended. Lists, introduced definitions, exact terms and connected derivations otherwise retained for passage-specific reasons. No mechanical synonym changes. Stage 3 remains pending.','token_stats':'unavailable'}
(task/'stage2-foundations-synthesis.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'file':str(task/'stage2-foundations-synthesis.json'),'paragraphs':len(rows),'repairs':len(repairs),'completed_at':report['completed_at']},indent=2))
