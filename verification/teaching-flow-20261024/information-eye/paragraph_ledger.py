from pathlib import Path
import json,datetime,hashlib
TASK=Path('C:/dev/clsc/burak-papers/guide/verification/teaching-flow-20261024')
G=TASK/'information-eye'
baseline=json.loads((TASK/'concept-baseline.json').read_text(encoding='utf-8'))
folds=json.loads((G/'fold-decisions.json').read_text(encoding='utf-8'))

# Passage-specific purpose and order judgments. Line numbers are the frozen source,
# not new proposal line numbers. The source text and hashes stay in the baseline.
notes={
'ch:MEMORY-INFORMATION':'''3|Sets the two competing effects of collecting spikes before introducing information; connects the preceding dynamical calculation to recall.
5|Keeps storage delay T separate from later observation L before either enters an error formula.
9|Motivates local distinguishability using nearby states before defining a likelihood.
11|Defines likelihood and the short-bin Poisson assumptions before taking logarithms.
18|Turns the count product into additive terms and defines the rate derivative used by the score.
30|Defines the score and its zero mean before using its square as information.
38|Explains vanished cross terms and defines information per time before presenting J.
44|Distinguishes J from Jh and states units and positive-rate limits before interpretation.
46|Explains the slope/noise ratio and internal-state meaning before the tuning figure.
48|Introduces the baseline-firing comparison so the coming figure has a specific question.
56|Interprets the zero-slope peak and baseline cost after the tuning figure, then links its source.
58|Defines local unbiasedness and differentiability conditions before the error-bound argument.
66|Uses zero mean score to connect the estimator identity to Cauchy Schwarz.
74|Names and limits the Cramer Rao result, including efficiency and prior assumptions, before applying information to the network.
78|Explains why recurrent and external readers face the same spike noise; motivates the bound.
80|Recalls the exact projection identities from Chapter 2 instead of silently assuming them.
90|Chooses noise-weighted vectors that connect the old diffusion formula to the new information formula.
96|Identifies vector lengths with 2D and J before invoking the inequality.
103|Connects the displayed Cauchy Schwarz inequality to its diffusion-bound rearrangement.
109|States that the left-vector proof does not require symmetry and keeps the model assumptions attached.
111|Checks dimensions and distinguishes a permitted minimum from a guaranteed actual diffusion rate.
113|States the equality test separately before discussing a sufficient transfer rule.
121|Explains zero-slope cells and the common transfer ratio needed in a symmetric circuit.
127|Solves the common-ratio condition and explicitly says exponential transfer is sufficient rather than necessary. Keep this qualification visible before the optional counterexample.
129|Constructs the linear mutual-excitation check from an already taught Chapter 2 model. Fold because the visible equality condition and caveat already state the needed limit.
137|Explains why changing the shared ratio across states defeats the unrestricted converse. Retain inside that exact optional check, not as a new assumption in the main result.
139|Starts the shorter numeric mutual-inhibition example with coordinate and units; keep visible to make lower-bound strictness concrete.
146|Checks units and balanced-state equality before changing the memory value.
153|Explains why actual diffusion stays fixed when the bound falls; prevents conflating more information with improved actual persistence.
155|Gives the strictness figure its question after the numeric example.
163|Interprets the figure gap and points to the paper equation before extending to multiple coordinates.
165|Defines matrix information for more than one represented coordinate; keep visible because the matrix statement depends on it.
173|Defines matrix order, states its meaning for coupled directions, and sets up U/V identities before optional residual algebra.
179|Checks the matrix statement through a nonnegative residual. Move after the visible invertibility condition and fold; no later step uses Q.
186|Keeps the invertibility condition and reason coupled directions matter visible. Move ahead of the residual check so its closed path has the claim and condition.
190|Asks what stays fixed before comparing networks, rather than reading a within-network inequality as a universal intervention rule.
192|Derives the population-size benefit under replicated tuning and weight scaling before varying firing rates.
194|Separates rate multiplication from changes that could destroy tuning or the attractor; retains its geometry conditions.
196|Compares two different time-constant experiments and explains why their powers differ.
198|Motivates the dimension-dependent width result and labels the teaching derivation before its assumptions.
200|Sets population density, shape, peak rate and boundary assumptions before varying width.
207|States what width variation holds fixed before replacing the sum with an integral.
217|Explains the volume/slope competition and interprets its dimension-dependent result after the integral.
219|Shows the different answer under a fixed spike budget and lists limits; keep with the width result so it cannot be read universally.
221|Connects sensory and internal information only under matched tuning, then limits the biological inference.
225|Sets the recall question at the cue and explains why perfect present knowledge cannot reverse storage noise.
227|Defines the storage and readout errors before their variance expansion.
235|Derives zero cross covariance under conditional unbiasedness and independent future noise, then adds translation invariance.
241|Assigns meaning to each variance term and lists where the decomposition changes.
243|Introduces the timeline with its storage-versus-readout distinction.
251|Interprets the timeline without suggesting later spikes recover past noise.
253|Introduces the Gaussian-bin observation model before its state and observation equations.
265|States independent errors, the meaning of y_k and the finite-spike approximation limit before either reader calculation.
269|Explains the benefit and cost of equal weighting before the Brownian calculation.
271|Introduces Brownian displacement and its time covariance for the integral that follows.
277|Explains shared increments before defining the continuous average.
283|Derives the count-noise term and sets up the distinct motion term.
289|Explains the triangular integration region rather than dropping the motion coefficient from a formula.
297|Combines the separately explained error terms into one variance.
303|Uses their opposing duration dependence to motivate differentiation for an optimum.
311|Connects that optimum to equal error terms and the minimum variance.
318|Interprets why more observations eventually hurt this specific equal-weight reader.
322|Introduces the ideal reader as accounting for intervening movement, then motivates backward information combination.
324|Defines precision and verifies its addition rule before any recursion uses it. Keep visible.
326|Defines P, the no-prior condition and the backward transition uncertainty before computing new precision.
332|Adds the earliest observation to backward-carried precision before taking a limit.
338|Introduces the small-bin expansion needed to read the differential equation.
344|Gives the continuous equation with its starting condition before solving it.
351|Defines the hyperbolic functions and interprets information gain versus diffusion loss before separation of variables. Keep this first teaching visible.
359|Connects the integrated equation to the precision and variance solutions.
370|Defines coth, identifies the teaching reconstruction and interprets the role of diffusion after the solution.
372|Sets up the short-time comparison to equal weighting before the series result.
378|Explains the short-time agreement before taking the long-interval limit.
385|Gives concrete diminishing-benefit ratios and distinguishes variance from standard deviation.
387|Applies the information bound to the characteristic time only after both have been derived.
394|Prevents interpreting tau as an abrupt deadline and compares variance and standard-deviation efficiency.
398|Introduces incomplete access as a readout change that does not quiet the memory circuit.
400|States independent thinning before deriving the observed-information fraction.
406|Keeps network diffusion fixed while changing observed information.
415|Interprets the longer useful interval and limits the alpha rule for biased subsets.
417|Gives the full-access numerical baseline before thinning it.
419|Computes reduced-access values and adds the same storage cost in both cases; keeps the irreversibility of storage loss explicit.
423|Motivates the time-scale extension through a question about which dynamics carry lasting noise.
425|Introduces added rate relaxation before the two-stage equations.
433|States noise placement, state and symmetry before the block matrix.
442|Derives the enlarged left vector using the two matrix blocks and normalization.
448|Uses noise in only one state block to obtain the extended diffusion bound.
457|Interprets tau plus tau_m with the dominance case and limits it to this two-stage model.
459|Motivates the noise-law comparison and defines constant-strength additive Gaussian noise before using it.
465|Recomputes matching information and diffusion, contrasts equality conditions, and preserves the pointwise exception.
467|Explains why the q normalization is explicit and ties the reconstruction to the source.
471|Teaches how to read the normalized figure, its extrema and the absence of storage variance before the figure.
473|Gives the figure its equal-weighting question.
481|Interprets the plotted contrast before discussing a printed inequality.
483|States the exact printed claim before checking its inequality direction.
493|Explains why an upper readout bound cannot supply a lower total bound and gives the defensible model statement.
500|States the asymptotic and saturation conditions and labels the apparent source inconsistency rather than an author correction.
502|Provides a strict-case number check that prevents silently assuming saturation.
504|Separates diffusion from leak and ends with the biological conditions needed to transfer the theory.''',
'ch:EYE-DRIFT':'''3|Introduces smooth drift, defines microsaccades and distinguishes recorded upstream evidence from a proposed memory source.
5|Connects neural diffusion to measured movement through mechanics before following the pathway.
9|Motivates a lasting eye command and defines the integrator before treating it as storage.
11|Defines motor neurons, recording site and ocular plant in signal order before discussing separate noises.
13|Separates shared, private and downstream sources and explains why population averaging treats them differently.
17|Gives animal and cell counts and the one-cell paired design before any covariance inference.
19|Explains segment selection and sampling, retaining the two-animal limit on repeated observations.
21|Explains why large movements calibrate a small-drift analysis and defines gain where the transfer assumption matters.
23|Introduces the pathway-versus-analysis diagram so its arrows answer a specific question.
31|Interprets the diagram and prevents reading analysis inversion as a physical reverse pathway.
35|Explains why position alone is insufficient before the fitted movement-rate relation.
42|Defines eye position, threshold and predicted rate before listing coefficient units.
50|Checks every fitted term's units and the direction of the neural lead.
52|Explains observed-rate construction and fitting objective before the loss expression.
59|Defines the trial index, explains held-out predictions and keeps smoothing and firing-threshold limits attached.
61|Describes the first weak relationship, defines p value and avoids interpreting it as a variance fraction.
65|Motivates a common degree scale and explains inversion of the calibrated fit.
67|Defines the threshold-relative coordinate and temporarily removes delay to derive the filter.
73|Defines causal filtering and impulse response before factoring the differential relation. Keep these definitions visible.
80|Connects quadratic factors to the two response decay times.
87|States positivity and nonoscillation conditions, then the two identities used by the visible numerical example.
94|Starts the optional impulse-response coefficient derivation. Move after the visible normalized kernel and unit explanation so the closed path already has the result.
100|Derives the pulse initial conditions for the two temporary coefficients; retain inside the coefficient fold.
107|Solves those temporary coefficients; retain with their defining derivation so no visible A or B depends on a closed fold.
115|Defines the step function, restores delay, defines spike impulses and gives the complete predictor. Keep visible before optional algebra.
122|Explains convolution and conversion units after the kernel; this is the visible result interpretation before the coefficient fold.
124|Starts the optional symbolic area check. Move after the concrete gain example, preserving the required calibration teaching visibly.
132|Checks constant-rate gain and the special repeated-root limit; fold after the visible numerical check because no later inference uses that limit.
134|Defines the constructed kernel's actual inputs before its displayed curve; keep visible as the shortest concrete gain calculation.
141|Checks the curve area and steady-rate gain, and labels its numbers as constructed rather than fitted.
143|Reports measured times and correlation, defines SEM and gives shuffle comparison before reasoning from R.
147|Asks whether independent motor noise alone can explain the observed correlation before estimating a common fraction.
149|Derives the explained variance fraction for the best fitted linear gain.
157|Defines coefficient of determination and distinguishes it from raw predictor squared error.
159|States the independent-predictor thought experiment before its nonnegative residual bound.
167|Interprets the 1/N bound and keeps the sampled-population representativeness premise attached.
169|Explains why the authors use mean correlation before squaring, rather than average noisy squares.
177|Compares the observed lower estimate with an independent population's scale and explains overlapping shared variance.
179|Supplies the biological independence premise needed to infer an upstream source and marks its lack of simultaneous testing.
183|Motivates estimating the common fraction using already-calibrated degrees before decomposing the signals.
190|Defines common and private terms and states unit gain and pairwise uncorrelatedness before covariance expansion.
192|Introduces the covariance expansion to show exactly where the independence approximation enters.
201|Uses that covariance to define the estimated common fraction.
208|Keeps calibration transfer and the neglected one-cell output covariance visible beside the estimator.
210|Sets up the correlation denominator contrast before relating R and chi.
218|Explains why private predictor noise can lower correlation without reducing common movement variance.
220|Introduces constructed variances as an illustration rather than cell measurements.
228|Adds those components into total variances and covariance before calculating R and chi.
235|Interprets the same example's 2.89 percent explained fraction versus 82 percent common fraction.
237|Gives the variance figure its specific small-correlation question.
245|Interprets the matching physical scale and denominator effect, then links source equations.
247|Explains noisy cell estimates outside zero-to-one and their errors before inverse-variance weighting.
255|Derives the weighting, states its normal independent-error assumptions and reports 0.82 plus/minus 0.07 with its exact scope.
259|Moves from one interval to many lags because source timing is a new question.
265|Connects the recalled MSD definition to segment averaging and available lag spacing.
267|States independent measurement-error assumptions before calculating the correction.
279|Explains the factor of two and the exact-zero-lag exception after the expansion.
281|Describes estimating and subtracting an average offset and why this cannot recover unknown trajectory errors.
283|Shows the subtraction's relative uncertainty and states how temporal correlation changes the correction.
285|Defines the illustrative Brownian movement and measurement variance before its figure.
293|Interprets the endpoint errors and preserves the distinction between illustrative movement and measured data.
297|Reports the observed MSD slope range before formally defining local slope.
304|Explains slope one and two and defines finite-range superdiffusion without claiming an unlimited power law.
306|Asks whether peripheral filtering is enough, then defines low pass filtering, white noise and stationarity before using covariance.
312|Gives white-noise intensity units before deriving the filtered covariance overlap.
319|Uses centered stationary position to derive MSD from covariance.
325|Explains why a decaying kernel gives a plateau, then ties it to the paper.
327|Defines a one-exponential teaching filter before giving its explicit white-noise MSD.
334|Interprets its short and long lags, distinguishes the smoother double response and gives the private-noise simulation comparison.
336|Introduces a wandering stored position as the competing input and states why filtering can preserve accumulated displacement.
338|Introduces the precise one-pole stochastic model for that teaching reconstruction.
344|Defines the Brownian scale and velocity before deriving the velocity process.
350|Explains relaxation and the decayed-transient assumption before the stationary velocity solution.
358|Uses shared increments to explain velocity covariance and then integrates it into displacement.
369|Sets up the small-lag series that leads to smooth quadratic displacement.
375|Interprets short-lag velocity persistence before the long-lag limit.
381|Connects long-lag growth to the local slope formula.
388|Interprets both limits and intermediate examples without inferring super-Brownian memory noise.
390|Introduces the normalized input comparison figure and names the one-pole shorthand.
398|Keeps the white-input short-lag slope restricted to this specific teaching filter.
400|Returns to the full muscle model and explains what the simple example establishes and which peripheral alternative it does not reject.
404|Introduces the proposed circuit after recording evidence, preventing a model from being mistaken for the directly recorded source.
406|Introduces right-population firing before the rectified rate expression.
413|Defines position, slopes, rate offset and feedback units and interprets opposite populations.
415|Introduces the synaptic dynamics as the next physical stage after firing.
423|Defines all synaptic variables and explains spike jumps and saturation before recurrent persistence.
425|Asks what recurrence must satisfy for storage and introduces the no-feedback mean drives.
433|Combines the cell equations into the readout dynamics so neutrality is derived rather than presumed.
441|States the continuum fixed-point requirement before linearizing a small displacement.
448|Interprets neutrality and stable transverse directions, preserves finite optimized-network mismatch, and separates deterministic drift from spike diffusion.
450|Moves the proposed position signal to motor neurons before their equations.
458|Defines motor variables, jump size and mean output before muscle response.
460|Introduces each motor unit's effective eye-position contribution before the plant and averaging equations.
467|Checks static common-position transmission and private-noise averaging while limiting the isolated-eye interpretation.
469|Gives heterogeneous parameters and separates neuron counts used in different simulations.
471|Introduces delayed feedback as the final loop rather than an earlier recording conclusion.
478|Checks feedback units, sign and velocity-like approximation without treating it as an absolute-target error.
480|Explains why a lag is not time since perturbation and reports model feedback effects without a hard delay cutoff.
484|Motivates parameter freedom, recalls CV and defines the model's sub-Poisson meaning before using a CV-squared scale.
486|Shows the retained-every-Mth-spike construction and its constant-rate limits.
488|Defines renewal intervals and derives the long-window count variance before using CV squared for diffusion.
496|Interprets accumulated spike variability and connects its projection factors to Chapters 2 and 3.
498|Defines absolute position slope and the comparable-population assumptions before computing information.
504|Carries the information scaling into the diffusion scale while keeping fixed geometry explicit.
511|Defines fractional sensitivity as a different normalization before the equivalent diffusion expression.
517|Checks the printed sensitivity ambiguity through units and limits the formula to a controlled scaling comparison.
521|Explains concrete parameter changes and distinguishes fixed-rate from fixed-fractional-slope rate changes.
523|Asks whether drift contaminates CV and states the small-change Brownian assumptions for that check.
530|Derives the time-mean correction and first-order interval expansion needed by the drift-only CV.
539|Compares the drift-only CV with observed regularity, labels the order-of-magnitude purpose and checks angular units.
543|Introduces the figure table as separate inference steps rather than repeated evidence for one conclusion.
551|Adds the specific supplemental controls and explains negative sampling estimates and direct-versus-internal output noise.
555|Separates common-source, time-dependence and model-fit conclusions at the chapter close.
557|States exactly what was not recorded or perturbed and preserves possible upstream alternatives and parameter ambiguity.
559|Limits the empirical scope and closes by connecting internal diffusion to filtered observable movement.'''
}
parsed={ch:{int(line):note for line,note in (s.split('|',1) for s in block.splitlines())} for ch,block in notes.items()}
records=[]; missing=[]
for ch in notes:
    units=[p for p in baseline['passages'] if p['chapter_id']==ch]
    for i,p in enumerate(units):
        if p['kind']=='prose' and p['text'].strip().startswith(('<div','</div')):
            point='Retain the figure/table display wrapper at its exact adjacent typed-block position; it supplies presentation rather than a separate teaching claim.'
        elif p['kind']=='block':
            point='Retain the original typed block and its caption, labels and content at this learning step; its surrounding prose introduces and interprets this specific visual or figure table.'
        else:
            point=parsed[ch].get(p['line'])
            if not point: missing.append((ch,p['line'],p['text'][:100])); continue
        fold=next((f for f in folds if f['chapter']==Path(p['path']).stem and f['start']<=p['line']<=f['end']),None)
        row={k:p[k] for k in ('id','chapter_id','section_id','path','line','end_line','kind','sha256')}
        row.update(purpose_and_order_reason=point,decision='move-and-fold' if fold and 'move_after' in fold else 'fold' if fold else 'retain',
                   predecessor=units[i-1]['id'] if i else 'preceding chapter',successor=units[i+1]['id'] if i+1<len(units) else 'following chapter')
        if fold: row['fold_title']=fold['title']
        if ch=='ch:MEMORY-INFORMATION' and p['line']==186: row['decision']='move-before-optional-check'
        if ch=='ch:EYE-DRIFT' and p['line'] in (115,122,134,141): row['decision']='retain-visible-before-moved-optional-check'
        records.append(row)
assert not missing,missing
(G/'paragraph-purpose-order.json').write_text(json.dumps(dict(timestamp=datetime.datetime.now().astimezone().isoformat(),baseline='concept-baseline.json',source_hashes=baseline['source_sha256'],scope='All 241 extracted prose and typed-block passages in Chapters 3 and 4. Equations embedded between these passages retain exact text, with four logged optional spans; no paragraph removed or rewritten.',records=records),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(timestamp=datetime.datetime.now().astimezone().isoformat(),passages=len(records),chapter_counts={ch:sum(r['chapter_id']==ch for r in records) for ch in notes},missing_notes=len(missing)),indent=2))
