from pathlib import Path
import datetime, hashlib, json, re
GROUP=Path(__file__).parent
ROOT=GROUP.parents[2]
packet=json.loads((GROUP/'concepts-unreviewed.json').read_text(encoding='utf-8'))
purposes={}
def load(chapter,rows):
    for row in rows.strip().splitlines():
        line,purpose=row.split('|',1)
        purposes[f'ch:{chapter}/p{line}']=purpose
load('FOUNDATIONS',r'''
3|Holding eye position and keeping track of location motivate retaining a value despite changing cells; this introduces the shared question before neural terms.
5|Two kinds of disturbance separate the represented value from its activity pattern; this is the reason the later population vector and attractor geometry matter.
9|Spikes and expected rate are distinguished with 20 Hz; that expectation/event distinction is needed by tuning curves and Poisson counts.
11|Synaptic decay and recurrent connections explain how brief events can sustain activity; the next tuning description therefore concerns a possible persistent signal.
13|A local linear tuning curve connects rate to angle and gives units and the negative-rate limit; those cell responses can now form a population vector.
15|Different cell tuning curves motivate combining rates into one vector; keeping the short pre-equation lead-in attached to the vector prevents a bare formula.
21|The population vector represents a value, with neuron identity separated from physical location; decoding and encoding then have a concrete object.
23|Place-cell tuning extends representation into space and distinguishes an expected field from a finite-recording estimate; this prepares the separate spatial reading path.
25|CA3, CA1 and grid-cell context prevents treating place-map output as the location of the maintained position estimate; it finishes spatial context before the return to spike variability.
29|A fixed represented value can still yield different counts, motivating the Poisson law; its condition precedes its probability formula.
37|The expected count has no units and the two moments are given visibly; later rate uncertainty uses these moments without needing their proof open.
44|Factorial moments verify the visible Poisson variance identity; fold here because the calculation introduces no new prerequisite for the following example.
52|Relative count error falls as inverse square root of expected count while absolute variance rises; this connects the moments to population averaging and fair network comparisons.
54|The example label identifies the apparent-silence question and pooled-population comparison; it stays visible with its worked numerical trace.
56|A 50 ms interval at 20 Hz has mean one and a substantial no-spike probability; this makes the expectation/event distinction concrete before pooling cells.
58|Twenty conditionally independent counts show why pooling improves relative precision and why shared drive survives; this is the premise of the displayed comparison.
60|The shared per-cell rate scale prepares the two distributions for direct comparison; it belongs immediately before their figure.
68|Normalizing pooled counts preserves the mean rate while narrowing spread; the source locator follows the interpretation rather than interrupting the calculation.
70|Changing state makes count independence conditional, preventing the earlier averaging example from being mistaken for independent complete recurrent spike trains.
72|CV and Fano factor measure distinct aspects of variability; their limits complete the count discussion before covariance compares shared fluctuations.
76|The eye-pathway problem motivates covariance identities as tools for shared versus separate fluctuations; this supplies a reason for the probability review.
78|Centered covariance defines the shared-variation quantity before its units and algebra are used.
85|Covariance units and the variance special case connect the definition to the sum/difference identity that follows.
93|Independence implies zero covariance but the converse fails; normalized covariance is then introduced without confusing it with independence.
100|The dimensionless correlation range and source-fraction warning prevent an unsupported causal reading; Chapter 4 will supply the needed signal model.
102|A time-lag displacement is defined before decomposing its mean square; this is the link from generic probability identities to memory error.
109|Random spread and mean motion can both increase MSD; this interpretation is needed before the later unbiased diffusion and bias example.
113|State, deterministic dynamics, fixed point and directional stability supply the meanings needed to discuss a family of persistent states.
115|Continuous attractors distinguish neutral and restoring directions and coordinate dimension from cell count; the two-rate construction can now show those meanings.
117|The example label identifies two disturbances to the same stored angle; it stays attached to the concrete trace and figure.
119|Two activities, baseline, slope and angle units define the teaching construction before its rate equations are interpreted.
125|The fixed-point line and positive-rate domain precede the mean-activity deviation and angle coordinates; this makes the coordinate transformation meaningful.
133|The assumed dynamics establish the model being solved, with no claim that these equations fit an animal recording.
139|The positive inverse-time constant and add/subtract step lead directly to the separated restoring and neutral equations.
145|Exponential decay of x and constant theta interpret those separated equations before the numerical disturbances test them.
147|Common and opposing rate disturbances expose recovery versus persistent angle error, providing the shortest useful trace of the chapter's distinction.
149|The two arrows are distinguished as restoring flow and imposed neutral disturbance; this prevents reading the figure as motion in both directions.
153|The construction is limited to teaching geometry and introduces the need for the dynamics-based projection derived in Chapter 2.
157|Independent zero-mean increments with equal variance per unit time motivate accumulated error and give the premises for variance addition.
167|Replacing n intervals by elapsed time connects the discrete sum to the continuous Brownian approximation.
175|Brownian increments, relevant approximation scales and D's interpretation are taught before using continuous diffusion as a physical model.
177|MSD and its square root give distinct quantities and units; the multidimensional convention warns against mixing reported diffusion parameters.
179|The example label frames a concrete comparison of random diffusion with fixed bias; its assumptions and numerical steps remain visible.
181|Illustrative D yields displacement scales at two delays and is separated from monkey estimates; this fixes the scale before adding a deterministic velocity.
183|The added constant velocity supplies the second model term before its equation and MSD are used.
191|The crossover at four seconds explains why a small bias can dominate long delays; zero drift is therefore a real model restriction.
193|Sample paths and displacement scales are identified as different figure contents before the comparison is shown.
201|A path may return while its ensemble spread grows; square-root versus linear displacement connects the figure to the bias crossover.
203|Independent increments still give correlated positions; the short Brownian covariance proof must remain visible for later moving-memory averaging.
212|The scaled covariance 2D min(s,t) connects that proof to Chapter 3 readout error and the distinction from stationary-input smoothing.
214|Finite range, periodicity, feedback and changing D limit indefinite linear growth; this prepares Chapter 2's long-delay discussion.
218|A random spatial function is fixed after drawing it, unlike accumulating temporal noise; revisit variability is separated from the expected rate map.
220|Temporal storage noise and irregular fixed tuning can coexist without one determining the other; this explains the choice to teach dynamics before spatial statistics.
222|The three questions are ready to be compared by the type of variation studied; the map follows this comparison prompt.
230|The map compares questions without proving one connected biological circuit; that limit belongs after the figure's visual juxtaposition.
''')
load('MEMORY-DYNAMICS',r'''
3|Persistent firing can coexist with coordinate error; this recalls Chapter 1's distinction and motivates deriving motion before Chapter 3 reads it.
5|PDF page and equation locators explain how to inspect the supplied sources; keeping this brief reference before the technical section avoids later interruptions.
7|Theta, initial Theta, bars, tau and D units are established before the neural model equations rely on them.
11|Decaying activation renewed by recurrent spikes gives one complete model cycle before equations introduce its separate components.
13|A cell's counting process and dimensionless activation establish the spike-jump equation's variables and physical interpretation.
19|The event-time sum provides the equivalent activation trace; it remains beside the jump equation and before the plotted example.
25|Initial transients and unit jump size qualify the spike-history formula, preventing an unexplained activation scale.
27|Five illustrative events prepare the trace figure and separate its chosen input from empirical data.
35|The figure's decaying history is interpreted as activation rather than the spike train itself; this prepares weighted input from those activations.
37|Rate units and the input/rate relation connect activation to the next spike-generation step.
44|Weights, bias and the transfer function identify who affects whom and how input becomes rate; this completes the deterministic model cycle.
46|Conditional Poisson counts specify elementary noise assumptions before their expectation and covariance formulas.
55|The zero-or-one symbol and count-mean split explain the jump-noise equation; this makes later covariance notation unambiguous.
64|The weak-fluctuation approximation defines its small-input-change premise before replacing jump noise by Gaussian increments.
72|Brownian independence and dimensional consistency explain the Gaussian coefficient and limit the approximation to summed input fluctuations.
74|Population replication and weight scaling show how mean input stays fixed while variance shrinks; preferred-angle meaning remains visible for the later ring figure reading.
76|Removing noise gives the deterministic fixed-point family and activation/rate relation; the next caveat separates this design assumption from a generic network.
85|Continuous fixed-point families require tuning; this prevents recurrent feedback alone from appearing to guarantee a line or ring attractor.
89|Relaxing versus lasting effects frame the reason to linearize and project a general perturbation.
91|Linearization is defined and applied to the transfer rule; the small-perturbation premise precedes the matrix dynamics.
98|The fixed-point condition cancels constant terms and yields K plus local noise; this is the mathematical bridge from the model to projection.
107|Local evaluation of noise strengths and inverse-time units qualify K before its zero mode is identified.
109|The tangent u is the activity change per coordinate change; this makes its later normalization an interpretable quantity.
116|Differentiating the fixed-point equation gives Ku=0; the eigenvector term follows the operation rather than replacing it.
122|The right zero eigenvector identifies the neutral tangent, while all other modes must decay; this states the attraction condition needed by the projection.
124|The left zero eigenvector and normalization define the object that extracts coordinate change from arbitrary activity perturbations.
131|Normalization recovers a pure coordinate shift, and the stable-mode calculation explains why other components contribute nothing lasting.
137|The left vector's annihilation of stable modes leads to the surviving-state formula; the core calculation remains open for Chapter 3.
144|Tilted decay explains why ordinary perpendicular projection can fail, even with symmetric W; this motivates the following minimal example.
146|A two-variable local flow isolates tilted relaxation without requiring a neural simulation; lambda's positivity supplies stability.
152|The fixed line and explicit y decay lead to the final x value, exposing the lasting effect of a transient disturbance.
158|The example's u and v show why vertical disturbance changes final memory; its status as a teaching construction limits the claim.
160|The exact trajectory is introduced as the visual check of flow-based rather than perpendicular projection.
168|The plotted y decay and retained x shift connect the figure back to what the left vector measures.
172|Multiplying by the left vector removes restoring dynamics, leaving the random memory increment whose variance is calculated next.
179|Independent Brownian covariance removes cross terms, linking individual spike variance to total coordinate variance.
187|Matching the variance to 2D dt produces the local coefficient with the source locator next to the result.
193|Rate variability and squared lasting effect explain each contribution; changing firing rates also changes tuning/projection and cannot be compared in isolation.
195|Local state, weak noise and allowed time scales qualify the result before extensions or long-delay applications.
197|Several coordinate tangents and dual left vectors extend the scalar projection formula to a covariance matrix.
203|The diffusion tensor definition and coordinate coupling remain visible; a fold here would hide a first definition and the point of the extension.
207|Symmetric weights raise the specific question of expressing v through measurable tuning/input relationships; this motivates the special-case derivation.
209|Input and rate derivatives are defined and linked by fixed-point differentiation before the symmetric matrix identity.
216|The transpose calculation proves g prime is a left zero vector under symmetric W; it supports the normalization rather than asserting it.
224|Proportionality to g prime and its normalized formula connect the transpose identity to the general projection.
230|The activation tangent supplies the normalization scale, and substitution produces the symmetric-weight expression for D.
240|Invertibility, symmetric-weight/stability/noise assumptions and the independently noticed missing square qualify the formula before its example.
242|Mutual inhibition supplies a different continuous-attractor design and a positive-rate interior on which its fixed points are valid.
249|The sum decays while the difference retains memory; explicit u and v connect the design to constant projected noise.
255|Constant summed variability explains constant interior D and retains the boundary limit; this result is the point of the following plot.
257|The plotted bias and time constant are given beside the example they parameterize.
265|The constant rate sum is linked directly to the flat D curve, completing the plotted example before long-delay limitations.
269|A local growth coefficient cannot settle all later error behavior; boundaries and variable D motivate a density description.
271|The density and Itô convention supply the visible zero-drift equation; the test-function proof is moved to a later optional fold so the basic line/ring consequences can be read first.
282|Averaging the conditional Taylor increment produces the density-weighted identity; move with the proof because the main path uses the resulting density equation, not this intermediate calculation.
289|Compact support or vanishing boundary terms permit two integrations by parts; the final sentence refers back to the now-visible Fokker Planck equation and its first definition remains outside the fold.
297|The point-mass initial condition and unbounded constant-D Gaussian are explained visibly; neither their meaning nor their domain can be hidden with the proof.
304|Wrapping the Gaussian and defining reported angular error explain the uniform ring limit and pi squared over three result.
310|The ring's flattening is interpreted as an error-range effect while noise persists; this prevents the plot from being read as noise removal.
312|The chosen D supplies scale for the density/error plots and remains next to their figure.
320|The uniform wrapped density and contrasting line growth are interpreted before the optional density proof, then the text turns to variable D.
322|Zero drift, Itô and vanishing-boundary conditions precede the mean/variance evolution equations used for variable-D behavior.
330|Integration-by-parts moment checks and the smooth-D expansion explain how changing D affects higher-time terms; retain this short derivation beside its result.
337|A linear D leaves variance linear within the valid domain; this prevents overreading a straight variance graph as proof that D is constant.
339|Mutual excitation gives explicit tangent, dual vector and state-dependent D, providing a concrete test of the preceding linear-D distinction.
346|The variance slope and apparent printed factor-of-two discrepancy are checked with an explicit convention; this remains visible with its source links.
350|Trial-to-trial spread is distinguished from a reproducible mean change, posing the limit of a D-only calculation.
352|Systematic drift is defined, with deterministic mismatch and possible noise-induced mean motion; the microscopic-process limit prevents the variance approximation from claiming the exact mean.
354|Stratonovich first definition and conversion show why a written coefficient is insufficient to identify state-dependent noise; this is qualified as a scale estimate, not an exact neural drift calculation.
356|Orders of random and mean motion explain the leading variance focus and why canceling a mean does not cancel random increments; decoder conditions remain explicit.
358|Conditional spike independence is separated from recurrent correlations; a covariance-matrix extension requires a matching likelihood and is not claimed as the paper's general Poisson result.
362|Figure 1A's flow endpoints ground the instantaneous-memory definition in the left-vector construction already taught.
364|The activity bump and finite observed spikes distinguish moving memory from uncertainty reading it; the new term stays visible before Chapter 3 depends on the distinction.
366|Figure 2A-B separates rate curves, spike events and angle trajectory before comparing model predictions.
368|Simulation displacement is compared with the analytic formula and its separate lower bound; ring flattening retains its angular-error interpretation.
370|Mutual inhibition gives the second simulated design and shows symmetry is not needed for projection; the model checks are separated from animal measurements.
372|D derived from the network motivates the next chapter's statistical quantity and their bound; this closing bridge is retained for the reading order.
''')

records=[]
passages=packet['passages']
for i,p in enumerate(passages):
    text=p['text']
    if text in ['<div class="figure-scroll">','</div>']:
        decision='retain structural markup'
        reason='Pure scroll-container markup; no reader-facing paragraph. Keeps the existing figure placement and narrow-screen behavior.'
    elif p['kind']=='block' or text.startswith('{"alt":'):
        decision='retain typed block exactly'
        reason='Figure caption, alt text and numerical/scientific limits were read in the sidecar; image and interpretation stay beside the actual example. Old block object is byte-independent structurally identical in proposed YAML.'
    else:
        assert p['id'] in purposes,p['id']
        decision='retain'
        if p['id']=='ch:FOUNDATIONS/p44': decision='fold in place'
        if p['id'] in ['ch:MEMORY-DYNAMICS/p271','ch:MEMORY-DYNAMICS/p282','ch:MEMORY-DYNAMICS/p289']: decision='split/move proof with recorded bridge'
        reason=purposes[p['id']]
    prev=next((x for x in reversed(passages[:i]) if x['chapter_id']==p['chapter_id'] and x['id'] in purposes),None)
    nxt=next((x for x in passages[i+1:] if x['chapter_id']==p['chapter_id'] and x['id'] in purposes),None)
    rawlines=(ROOT/p['path']).read_text(encoding='utf-8').splitlines()
    rawsource='\n'.join(rawlines[p['line']-1:p['end_line']])
    records.append({**p,'raw_source':rawsource,'raw_source_sha256':hashlib.sha256(rawsource.encode('utf-8')).hexdigest(),'decision':decision,'purpose_and_order_reason':reason,'previous_reader_paragraph':None if prev is None else prev['id'],'next_reader_paragraph':None if nxt is None else nxt['id']})

# The passage extractor omits footnote entries and display equations. Account for both directly.
for stem in ['01-foundations','02-memory-dynamics']:
    path=ROOT/'content/chapters'/f'{stem}.md'
    text=path.read_text(encoding='utf-8')
    for m in re.finditer(r'^\[\^([^\]]+)\]:.*(?:\n(?!\n|\[\^).*)*',text,re.M):
        records.append(dict(path=str(path.relative_to(ROOT)),line=text[:m.start()].count('\n')+1,kind='source-footnote',text=m.group(0),sha256=hashlib.sha256(m.group(0).encode()).hexdigest(),decision='retain exactly',purpose_and_order_reason=f'Source details for {m.group(1)} remain available after the main teaching path; cited source locations and cautions are not folded or rewritten.'))
    for m in re.finditer(r'\$\$.*?\$\$',text,re.S):
        before=text[:m.start()].rstrip().split('\n\n')[-1]
        after=text[m.end():].lstrip().split('\n\n')[0]
        records.append(dict(path=str(path.relative_to(ROOT)),line=text[:m.start()].count('\n')+1,kind='display-math',text=m.group(0),sha256=hashlib.sha256(m.group(0).encode()).hexdigest(),decision='retain exact equation; see changes.json for proof moves',purpose_and_order_reason='Equation connects its actual introducing and interpreting prose, quoted here for the local dependency check.',introducing_prose=before,following_prose=after))

(GROUP/'paragraph-decisions.json').write_text(json.dumps(dict(timestamp=datetime.datetime.now().astimezone().isoformat(),scope='Author assessment of both whole chapters and sidecar figures, not independent acceptance.',audience='00-reading-guide: undergraduate calculus, basic probability and linear algebra; teach neuroscience and stochastic-process meanings.',source_sha256=packet['source_sha256'],records=records),ensure_ascii=False,indent=2),encoding='utf-8')
print('Recorded',len(records),'paragraph, block, footnote and display-math units; extractor passages',len(passages))
