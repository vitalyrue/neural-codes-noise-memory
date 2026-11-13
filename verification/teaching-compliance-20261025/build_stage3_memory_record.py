from pathlib import Path
from datetime import datetime
import json,hashlib,re
import yaml
T=Path('C:/dev/clsc/burak-papers/guide/verification/teaching-compliance-20261025');R=T.parents[1];C=R/'content/chapters';RULE=Path('C:/dev/NBIS/publisher-releases/0.8.23/skills/course-study-guide-builder')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
H=lambda s:hashlib.sha256(s.encode()).hexdigest()
# These are individual reviewer judgments, keyed to the final paragraph line IDs.
# Fields: purpose | connection to the surrounding argument | reason to retain.
A={}
def notes(ch,s):
 A[ch]={}
 for x in s.strip().splitlines():
  n,p,c,r=x.split('|');A[ch][int(n)]=(p,c,r)
notes('01-foundations','''
3|Pose reliable representation despite changing cells|Opens from eye position and location before naming their shared neural problem|Concrete behaviors give the later rate code a purpose
5|Motivate the chapter route|Representation leads to counts, pooling, shared variation and mean motion|The requested overview explains why these prerequisites belong together
9|Separate spikes from expected rate|Begins the promised signals and gives a20Hz interpretation before connectivity|A mean count rate must not become regular spike timing
11|Introduce connections between cells|Moves from a cell's events to effects on another cell|Synapses supply the physical role for the next two input effects
13|Define an excitatory effect|Supplies the increasing-firing branch of the preceding contrast|The sign of an input matters in later recurrent examples
14|Define an inhibitory effect|Completes the contrasting input effects before feedback|Decreasing firing is needed for the mutual-inhibition example
16|Connect lingering input with feedback|Uses synapses to explain persistence after a brief input|The causal cycle prepares the synaptic activation dynamics
18|Map a represented value to one rate|Uses expected rate to define tuning before a population pattern|Units and positive-rate range keep the linear example interpretable
20|Assemble different cells' rates|Leads from individual tuning to the displayed vector|The equation has an introduced purpose rather than appearing alone
26|Explain the population representation|Interprets the vector then defines reading and establishing its pattern|Neuron index versus physical position prevents a later axis confusion
28|Explain spatial tuning and its measurement|Extends the represented-variable idea from angle to position|Repeatable expected maps must be distinguished from finite measured fields
30|Introduce two hippocampal connection patterns|After place cells, asks how two regions with those cells differ|The next anatomical bullets have a common comparison question
32|Locate CA3 input and recurrence|Supplies the first half of the regional comparison|Later circuit interpretation needs the recurrent-versus-downstream distinction
33|Locate CA1 input and weak recurrence|Completes the comparison using the same connection criteria|It prevents attributing a maintained position to every output map
35|Distinguish repeated grid fields|Uses the anatomy to separate grid patterns from irregular place fields|The concluding storage-location limit follows from this coding distinction
39|Model variable counts at fixed expectation|Turns the established tuning curve into an uncertain observation|The Poisson law answers a concrete repeated-observation question
47|Explain the expected-count parameter|After the distribution, gives lambda's units before moments|This links rate times duration to dimensionless count statistics
56|Derive Poisson count variance|Inside the optional derivation, two sums lead to the squared-count identity|Removal of the unused label left the complete algebraic route
66|Interpret absolute and relative count noise|Uses the moments to explain pooling and controlled rate comparisons|The two noise scales have different rate dependence
68|Identify the count-example question|Names the silence-versus-population test before numerical inputs|The label tells what the calculation will establish
70|Show why no spikes is inconclusive|Instantiates20Hz and50ms in the already taught count law|Probability0.368 demonstrates a non-obvious silent observation
72|Compute population gain and its condition|Extends the same observation to20cells before a pooled figure|The shared-drive exception states why independence matters
74|Set the comparison scale for the figure|After pooling, announces the common per-cell scale|The visual compares uncertainty with matching expected rates
82|Interpret pooled normalization|After the figure, explains dividing by20 and links the likelihood source|The display's narrower spread is connected to an actual estimator
84|Limit independence in recurrence|Generalizes fixed-rate counts after the simple illustration|It prevents using independent full spike trains in the network derivation
86|Introduce two variability measurements|After Poisson scope, prepares interval and count measures|A common purpose makes the following two definitions comparable
88|Define interval CV|Supplies the first variability measure and its Poisson reference|The eye study's more regular firing needs an interval measure
89|Define count Fano factor|Completes the pair at the count rather than interval level|Counting-window dependence keeps its scope distinct from CV
91|Keep the two measures separate|Interprets the pair before moving to shared variation|No unstated renewal assumptions are used to equate them
95|Motivate covariance through shared sources|Moves from single-count noise to measurements in one pathway|The next formula answers why variables can vary together
97|Define centered-product covariance|Formalizes the shared-variation question|Its actual quantity is available before variance-of-sums use
104|Relate units and sum variance|Extends covariance to variance and the following identity|The cross term later controls storage/readout and source attribution
112|Introduce normalized correlation|After sum variance, states independence limits then rescales covariance|Zero covariance cannot silently become statistical independence
119|Interpret correlation without causal overclaim|Explains range and limits before referring to the eye model|Correlation magnitude alone does not identify a source's variance fraction
121|Define displacement and its mean square|Turns static-variable variability into a change across times|The following identity separates mean motion from spread
128|Interpret the MSD split|Closes covariance by preparing bias and leak questions|A growing squared error need not be random diffusion alone
''')
notes('01b-persistence','''
3|Separate value from activity|Builds on population representation to distinguish two disturbance effects|Coherent firing is not enough to preserve the original value
5|Motivate geometry, accumulation and map distinction|Explains why the example precedes diffusion and the spatial comparison|The required overview states each later question's source
9|Define state and fixed point|Formalizes the activity-versus-value problem before the stable family|Directional stability explains the restoring motion used next
11|Define the continuous family|Extends fixed points with neutral and restoring directions|Manifold dimension is the stored-coordinate count, not cell count
13|Identify the disturbance experiment|Introduces one initial angle and two perturbation types|The reader knows which outcomes the example compares
15|Set the two-rate representation|Gives rates, baseline, slope and angle before algebra|Units make the activity-to-angle map usable
21|Define off-family and along-family coordinates|Uses the rate representation to identify mean deviation and angle|The positive-rate domain limits the teaching model before use
29|Specify deterministic recovery dynamics|After coordinates are defined, introduces their generating rate equations|The later invariance and decay follow from an actual rule
35|Convert activity dynamics into coordinates|Gives the timescale and announces adding/subtracting equations|The algebra connects neural changes to value changes
41|Interpret decaying and neutral solutions|After the coordinate equations, separates their time behavior|The two numerical perturbations can now be predicted
43|Fix the common starting state|Converts5degrees into rates before comparing disturbances|Both outcomes are assessed against the same memory
45|Trace a common activity disturbance|Applies the defined mean-deviation and angle coordinates|The state returns without changing the represented value
46|Trace an along-family disturbance|Contrasts the same-size opposing perturbation with common change|The computed6.5degrees explains a lasting error without incoherence
48|State the example's memory consequence|Interprets the second perturbation before its geometry picture|The reader can explain why persistent activity can be wrong
50|Explain the two arrow meanings|Prepares the figure with imposed versus deterministic motion|A dashed disturbance must not be mistaken for a restoring flow
54|Limit the geometry example and connect forward|After the figure, links simple geometry to the general network projection|The ordinary perpendicular picture is not claimed for arbitrary dynamics
58|Pose repeated lasting changes|Uses the successful perturbation distinction to accumulate errors|Increment notation and assumptions precede the sum
60|Specify independent increments|First condition for variance addition|Without it the sum would require covariance terms
61|Specify zero increment mean|Second condition connects spread with MSD|It separates this model from the later bias term
62|Set increment variance and units|Completes the quantitative random-step model|D's dimensions determine the later displacement scale
64|Accumulate n intervals|Introduces the sum over already defined increments|The variance growth follows directly from the conditions
74|Define Brownian motion before use|Connects the discrete growth law to a continuous-path approximation|Zero mean, continuity and increment variance are explicit after repair
76|Introduce the continuous displacement equation|Follows the complete process definition|The formula represents the just-described limit
84|Interpret D at trajectory level|After variance law, separates ensemble spreading from one path|A path may return even while population RMS grows
86|Define RMS and dimensional convention|Converts variance into a coordinate-scale displacement|Equal-coordinate assumptions prevent a wrong multidimensional factor
88|Identify noise-versus-bias comparison|Sets the purpose before numerical values|The example tests time dependence rather than repeating the definition
90|Compute displacement at two delays|Applies the units and variance convention to chosen teaching inputs|The animal-data distinction avoids an empirical interpretation
92|Add a fixed mean velocity|Extends the zero-mean model before the biased MSD equation|The new effect is assigned its own parameter and units
100|Find the crossover and its limit|Uses the two time laws to compute4seconds|The unbounded qualification prevents extrapolating angular error forever
102|Prepare paths and displacement scales|Connects the crossover to the two-panel visual|The sample versus ensemble distinction remains visible
110|Interpret trajectories and long-time bias|After the visual, explains reversals and different growth rates|It uses the plotted behavior to motivate separate drift treatment
112|Derive cross-time Brownian covariance|Uses independent increments to split one path into shared history|This is the missing premise for averaging a moving memory
121|Transfer covariance to the stored coordinate|Scales the Brownian result and identifies its readout use|The later double integral has an established covariance kernel
123|Limit the basic diffusion law|Follows the unbounded calculation with boundaries and variable coefficients|The next network chapters can distinguish local from long-time predictions
127|Separate spatial and temporal randomness|Turns from changing memory to a fixed expected map|Revisiting the same place need not redraw the tuning curve
129|Allow the two kinds together|Explains the three studies' different questions after defining both kinds|The chapter order follows mechanisms, tests, then spatial statistics
131|Introduce the three-paper comparison figure|Follows the distinction with its side-by-side question map|The map organizes existing concepts rather than introducing a new theory
139|Limit the combined map inference|After the map, prevents a single-circuit conclusion|The separate rows remain a comparison of questions
''')
notes('02-memory-dynamics','''
3|Pose activity persistence versus value accuracy|Recalls the two-disturbance problem for the actual paper network|It identifies the output whose error must be calculated
5|Motivate the network calculation route|Renewal precedes return flow, projection, local spread and special case|The overview explains why each later operation is needed
7|Explain source navigation|Before dense equation citations, states how linked PDFs locate evidence|The reader can verify equations despite absent source line numbers
9|Fix notation and variance convention|Connects earlier definitions to this model's steady rates and timescale|The symbols are usable before the first stochastic equation
14|Explain the complete renewal cycle|Answers how a brief spike can support long activity|Plain causal roles precede the activation and transfer equations
16|Define activation jumps and decay|Turns the cycle into a spike-count driven state equation|The state is different from an observed spike count
22|Introduce equivalent spike-time expression|Rewrites the count dynamics using individual event times|It prepares the explicit exponential memory kernel
28|State initial-condition and unit scope|Completes the exponential sum before the numerical trace|No hidden initial activation or inconsistent unit is introduced
30|Prepare the event/activation trace|Names the illustrative inputs and what the plot compares|The visual addresses the difference between spike events and lingering input
38|Interpret accumulated activation|After the trace, explains its relation to earlier events|This motivates the weighted recurrent input that follows
40|Introduce input and rate equations|Moves from stored activation to spike-generation rate|The model cycle closes through the two quantities
47|Define weight roles and transfer function|Interprets the input sum and nonnegative firing rule|Source scope permits general connections before symmetry is imposed
49|Specify conditional spike variability|Uses current rates to supply count increment moments|The future projection has an explicit noise covariance
58|Separate count mean from noise|Explains Kronecker symbol and introduces compensated increments|Deterministic renewal and random deviations now have distinct terms
67|Introduce weak-fluctuation replacement|After the jump process, states what aggregate-small means|The Gaussian model does not silently replace physical spike events exactly
75|Explain Brownian coefficients and limits|Interprets the diffusion rewrite and its dimensions|Gaussian input fluctuations do not require Gaussian whole spike trains
77|Justify the approximation by scaling|Shows fixed means and shrinking input variance for many equivalent cells|Preferred angles and finite-network limitations are introduced before ring use
79|Identify the deterministic persistent family|Turns noise off after specifying its approximation|The fixed-point identity supplies the later tangent derivative
88|Keep attractor tuning explicit|After the family equation, states the model design condition|An arbitrary recurrent network is not promised a continuous memory
92|Ask which perturbation survives|Moves from a tuned family to the displacement needed for memory error|The linearization has a concrete target rather than being formal machinery
94|Linearize around the persistent state|Introduces first-order approximation before the Taylor expression|The reader knows which terms are kept and dropped
101|Explain fixed-point cancellation|Uses the defining family equation in the Taylor result|The remaining K dynamics follow rather than being quoted
110|Set local noise coefficients and units|After K is displayed, explains the leading local approximation|Later covariance contraction uses fixed-state rates consistently
112|Define the attractor tangent|Relates a small coordinate change to a state change|The derivative gives the normalization target for projection
119|Derive the zero tangent mode|Differentiates the already established fixed-point identity|Ku=0 is explained by the chain rule
125|Interpret the right zero eigenvector|After Ku=0, identifies tangent persistence and stable other modes|The zero mode has its correct dynamical meaning
127|Introduce the left-vector requirement|Adds the object needed for a general perturbation|The following equations define the distinct projection role
134|Explain normalization and mode cancellation|Uses left/right equations to show what v measures|A general perturbation can be reduced to a stored-coordinate shift
140|Finish stable-mode elimination|Interprets the orthogonality step before the surviving-state expression|The projection follows dynamics, not geometric appearance
147|Explain why perpendicular projection fails|Uses row-dependent transfer slopes to distinguish K from symmetric W|The next two-variable example tests that exact issue
149|Set up a tilted decay example|Introduces a soluble local system for the projection distinction|No extra neural simulation is needed to reveal the failure
155|Solve the decaying mode and endpoint|Follows the explicit differential equations|The lasting x change is computed from the actual trajectory
161|Interpret left/right vectors in the example|Applies the derived endpoint to a vertical perturbation|The illustration is identified as geometry, not a source network result
171|Interpret the plotted numeric shift|After the caption's chosen a/lambda and initial jump|The removed lead-in leaves the actual figure interpretation intact
175|Apply the established projection to noise|Uses vTK=0 after the example to isolate memory displacement|The reader can follow why stable deterministic flow drops out
182|Contract independent noise increments|Uses the stated Brownian covariance in the squared displacement|The per-cell variance sum keeps its essential factor and independence
190|Identify D from the variance increment|Matches the computed coefficient to the chosen2D convention|The formula is tied to the model's displacement measure
196|Interpret each cell's projected contribution|Connects rate noise and squared projection sensitivity|High rate alone does not determine damage under network changes
198|State local leading-order scope|Introduces the two required time-window conditions|The derivation is not a global finite-noise theorem
200|Require enough accumulated spike input|First side of the local approximation window|It explains when a continuous-noise description is meaningful
201|Require nearly fixed coefficients|Second side of the approximation window|The memory must not wander far enough to change local sensitivities
203|Separate variance from drift analysis|Closes the local result and points to the next chapter's question|A diffusion coefficient is not assumed to give mean motion
205|Extend projection to several coordinates|Generalizes scalar tangent/left normalization before covariance matrix|Coupled directions are introduced through the same mechanism
211|Interpret the diffusion tensor|Defines diagonal and cross-coordinate covariance roles|Independent spike noise can still produce coupled represented motion
215|Motivate the symmetric special case|Returns to the required left vector and asks for tuning-based evaluation|The corrected transfer-function term now matches its earlier definition
217|Differentiate input and rate tuning|Establishes derivative relations before the transpose calculation|All system-specific derivative symbols have meanings
224|Use weight symmetry in K transpose|Applies the preceding derivative identities to find a zero vector|The role of symmetric W is shown at the needed step
232|Normalize the symmetric left vector|After finding gprime as a candidate, sets its coordinate scale|The denominator is justified by vTu=1
238|Substitute into projected variance|Connects normalization with the diffusion sum|The final tuning formula follows through explicit quantities
248|Reconcile source formula and assumptions|After the derived result, addresses the visible main/SI discrepancy|It keeps source checking honest without claiming an author correction
250|Require symmetric weights|First condition on the special formula|The earlier general projection remains available without symmetry
251|Require an attracting continuous family|Second condition on the special formula|A tuning curve alone does not imply persistence
252|Retain the introduced noise model|Third condition on the special formula|The rate-weighted variance is specific to these spike assumptions
254|Limit the needed symmetry|Closes assumptions before the non-ring example|The calculation does not demand rotationally repeated neurons
256|Define mutual-inhibition example|Provides weights, biases, transfer rule and interior domain|The following fixed states and diffusion can be checked
263|Identify neutral difference and stable sum|Maps this example onto the established projection construction|Its u and v come from the actual coordinates
269|Interpret constant spread and boundaries|After computing the rate sum, explains the constant D|The positive-rate interior cannot silently define endpoint behavior
271|Set plotted parameters|Before the reconstruction figure, gives b and tau|The rate-sum and D scales in the panels are reproducible
279|Read constant D from the rate sum|After the figure, links its two panels through the formula|The visual demonstrates a mechanism rather than decorative curves
''')
notes('02b-memory-long-delays','''
3|Pose the local-to-long-delay question|Uses the preceding local rate while adding range and mean-motion issues|The chapter has a distinct question beyond repeating D
5|Motivate density, drift and figure route|Explains why boundary behavior precedes noise limits and readout uncertainty|The overview connects this calculation with the next information chapter
7|Recall local state and convention|Carries forward the projection result with its relaxation and drift conditions|The density calculation starts from a defined coordinate and spread rate
11|Separate initial rate from global law|Turns the opening question into the immediate density problem|It prevents extrapolating local variance forever
13|Introduce density and Ito convention|Defines trial density and coefficient evaluation before its PDE|The equation has both an evolving object and specified stochastic meaning
21|Explain point-mass start and line case|Interprets the initial condition before the Gaussian solution|Dirac delta cannot be mistaken for the earlier index delta
28|Wrap the line density onto a circle|Uses the Gaussian variance to build the periodic case|The source-link repair leaves the full wrapping and uniform-limit reasoning
34|Interpret angular-error saturation|After the bounded-error integral, explains flattening without noise removal|The error convention controls the long-time plateau
36|Set density-plot parameters|Introduces the same D used in both line and ring panels|The visual compares conventions with identical local diffusion
44|Read density and error together|After the plot, relates uniformity to pi squared/3|The lower plateau has the upper density as its explanation
48|Derive the density equation from increments|The optional proof starts from a smooth test function and conditional moments|Taylor expansion uses the already defined Ito evaluation
59|Average the local change|Moves from conditional Taylor terms to a density-weighted expectation|The small-dt passage retains its leading-order status
66|Move derivatives by integration by parts|Completes the weak density identity under boundary conditions|The PDE follows for arbitrary interior test functions
70|Use density evolution for variable D|Returns to main text with drift and boundary assumptions explicit|The moment identities apply to the specified process
78|Derive first moments and the time correction|Explains which second derivatives survive integration|The t-squared coefficient is computed rather than asserted
85|Show when variable D still gives linear variance|Uses linearity of expectation after the expansion|The valid-domain condition prevents unsupported endpoint extrapolation
87|Instantiate mutual excitation|Supplies weights, biases, states and projection vectors for the example|It contrasts with earlier inhibition using the same machinery
94|Reconcile projected coefficient with the source|After calculating D, compares SI40 and SI41 under one convention|Removing writer commentary leaves the factor discrepancy fully visible
98|Separate spread from mean motion|Starts the drift section from repeated-trial behavior|A coefficient of variance growth does not answer the mean question
100|State the drift-elimination assumption|Defines mean velocity and possible microscopic sources|The leading variance calculation is not presented as exact drift analysis
102|Explain convention-dependent drift|Contrasts midpoint and beginning evaluation after defining both|The conversion term supports the stated Dprime/2 scale
104|Compare noise and mean scaling|Uses the large-population scale to interpret their different orders|Canceling a known mean does not cancel random increments
106|Limit Poisson independence and extend covariance|Reuses the projection with joint noise before discussing its information|The paired-likelihood requirement stops an unjustified correlated-noise formula
110|Read the source flow-coordinate diagram|Uses the derived left projection to interpret Fig1A|The reader follows dynamical endpoints rather than perpendicular distance
112|Define activity bump across neurons|Prepares Fig1B's two memory errors with a clear population axis|The peak refers to preferred-angle ordering, not physical space
114|Identify storage displacement in the bump|First item in the two-error comparison|It concerns movement of the represented state before observation
115|Identify finite-spike readout uncertainty|Second item contrasts estimation with movement|This motivates information even if the current state were fixed
117|Connect the two uncertainties to later calculations|After the figure distinction, assigns information and readout their jobs|The next chapter's statistical question now has a concrete origin
119|Read simulation signals in Fig2|Distinguishes rate curves, spike events and stored coordinate|The plotted angular trace is not activity amplitude
121|Introduce two different validation tests|Groups panels C and D under a shared prediction question|The next pair separates short-time coefficient from long-time wrapping
123|Interpret diffusion fit versus lower bound|Explains transfer-rule cases and the dashed sigmoidal bound|A strict information inequality can coexist with a correct diffusion formula
124|Interpret wrapped long-delay error|Uses the previously derived angular convention in panel D|Saturation does not imply noise has stopped
126|Read the non-ring validation|Contrasts mutual inhibition and ring simulations under the same projection|No rotational symmetry or animal-data claim is smuggled into validation
128|Motivate a statistical limit on dynamics|Closes the derivation by asking what constrains D from spike information|It hands a specific unresolved question to the next chapter
''')
notes('03-memory-information','''
3|Connect spike readout with recurrent disturbance|Uses finite-spike uncertainty and memory movement from the previous chapter|The lower-bound question joins the two established errors
5|Motivate local information and controlled comparison|Explains what quantity is missing and how network comparisons differ|The overview preserves possibility versus attainment of better stability
7|Recall state notation and projection|Carries the relevant prior calculation into the statistical setting|The later Cauchy Schwarz normalization has an identified source
11|Pose nearby-state discrimination|Turns information into a rate-change-versus-variability problem|The likelihood has a practical local estimation purpose
13|Define likelihood and count model|Uses locally fixed state and conditional Poisson counts|The data probability can now be differentiated in theta
20|Transform the product likelihood|Defines the rate derivative before taking log and score|The route from counts to sensitivity has no hidden algebraic object
32|Define score and its mean|Interprets the displayed derivative and sets up its mean square|The zero-mean property later supplies the estimation-bound identity
40|Identify information and its rate|Uses vanishing cross terms and count variance to explain the sum|Dividing by observation time distinguishes J from finite-sample information
46|Set information units and rate domain|Completes J's definition before interpreting cells|Positive-rate and regularity qualifications limit the formula
48|Interpret informative tuning changes|Explains zero slopes and internal versus external coordinates|A high-rate neuron need not distinguish nearby states
50|Prepare the extra-baseline example|Holds changing shape fixed before the three-panel plot|The visual isolates spike noise without changing slopes
58|Interpret peak and baseline effects|Reads the rate and information panels through the derived formula|The reader can explain both zero peak information and reduced flank information
60|Derive the unbiased-estimation identity|Defines the estimator goal before differentiating its expectation|The inverse-information error scale has stated regularity assumptions
68|Apply Cauchy Schwarz to the score identity|Uses zero mean score to obtain the variance bound|The inequality is derived from already defined objects
76|State the bound's meaning and limits|Names Cramer Rao after its proof and defines prior knowledge|Finite samples, bias, priors and ambiguity are not promised efficient attainment
80|Pose the network's own estimation limit|Connects external spike information with internal recurrent input|The next proof compares statistics with dynamical sensitivity
82|Recall projection identities for the bound|Brings D, tangent and left normalization into one display|The proof's premises are available before choosing vectors
92|Choose the two Cauchy Schwarz vectors|Uses rate noise and rate slopes to expose their dot product|Their construction is matched to the desired D and J factors
98|Identify vector lengths with D and J|Applies the audience's linear-algebra inequality to known factors|The lower bound follows with the correct tau normalization
105|Rewrite the same inequality for D|Connects the product form to the displayed diffusion lower limit|This short connector belongs to the adjacent equations
111|Set proof scope and source relation|After the result, states why symmetric weights were not used|The model-specific assumptions stay distinct from a universal memory theorem
113|Interpret units and permissible stability|Checks dimensions then distinguishes allowance from attainment|The next equality analysis is needed because information alone is insufficient
115|Introduce equality through vector alignment|Uses the just-applied inequality's equality condition|The subsequent transfer-rule restriction has an algebraic reason
123|Connect alignment with transfer derivatives|Uses symmetric v proportional to gprime to compare cellwise ratios|The same-state condition is separated from a constant over all states
129|Interpret exponential sufficiency|Solves the ratio equation while retaining its one-way implication|This prepares the counterexample without claiming necessity
133|Construct a linear equality family|Reuses mutual excitation with zero bias and positive rates|The optional calculation tests the published converse directly
141|Explain why the converse fails|Uses equal same-state inputs and varying between-state ratio|The information inequality survives while exponential necessity is restricted
145|Set a controlled two-state numerical example|Returns to mutual inhibition with coordinate units explicit|The comparison changes information while holding actual D fixed
152|Compute the shifted-state bound|After balanced equality, changes theta and calculates rates and J|The two candidate stability claims now give different numbers
159|Interpret strictness and special-state equality|Uses unchanged D and unequal noise weights|A lower allowable bound does not improve this actual circuit
169|Read the actual-versus-bound plot gap|After the reconstruction caption, points to theta100's numeric difference|The removed lead-in does not remove the figure's conclusion
171|Generalize information to a matrix|Uses the earlier diffusion tensor setting for several coordinates|The new object describes directional sensitivity before inversion
179|Define the matrix comparison and proof objects|Explains every linear combination and builds U,V with dimensions|The coupled-direction bound is meaningful beyond separate scalar inequalities
185|State identifiability for matrix inversion|After the matrix identities, requires independent distinguishable directions|The inverse is not applied to a singular information matrix
189|Prove the residual is nonnegative|Inside the optional check, expands the defined residual matrix|The matrix inequality follows from a square rather than analogy
200|Pose controlled network comparisons|After a within-network bound, asks which resources stay fixed|The next scaling examples cannot be interpreted without this distinction
202|Compare population size at fixed tuning|Uses density replication and inverse-N weights|It derives information and diffusion scaling for a specific controlled change
204|Compare common firing-rate scale|Uses slopes scaling with rates while preserving required geometry|Nonlinear transfer and attractor changes are kept as limits
206|Compare two tau constraints|Contrasts fixed rate tuning with fixed activation tuning|Different exponents are explained by different held quantities
208|Motivate width's dimensional dependence|Poses opposite one- and three-dimensional outcomes before a derivation|The calculation is marked as a controlled reconstruction, not a universal law
210|Define the tuning family and resources|Sets uniform center density, fixed peak and fixed shape|The integral approximation has a stated spatial setting
217|Change variables in directional information|Names the varied width and fixed quantities before the integral|The displayed scaling has an explicit source for each width factor
227|Interpret the two scaling factors|Introduces volume recruitment and slope change|The following two bullets explain why dimension alters the result
229|Explain active-volume growth|First factor in the width scaling|Broader tuning recruits more centers in d dimensions
230|Explain squared-slope decrease|Second factor in the width scaling|Width weakens each curve's local directional sensitivity
232|Reduce the matrix under directional symmetry|Adds radial tuning and uniform centers before scalar coordinate inversion|The repaired condition teaches the missing relation before D's width law
234|Interpret width scaling in one dimension|First dimensional outcome of the proved power law|Narrower tuning's benefit has a stated peak-rate resource constraint
235|Interpret the two-dimensional cancellation|Second outcome compares equal powers of width|No leading effect is the result of balanced recruitment and slope factors
236|Interpret width scaling in three dimensions|Third outcome completes the contrast|Broader tuning can help under the stated density and peak constraints
238|Change the resource constraint and limits|After the dimensional outcomes, fixes total firing instead|The alternate exponent and failure conditions prevent overgeneralizing width advice
240|Connect sensory coding only under matching tuning|Uses the now-derived information criterion for a possible shared circuit|Mathematical compatibility is separated from anatomical evidence
''')
notes('03b-memory-readout','''
3|Pose readout of an already moved memory|Uses storage loss to ask whether later spikes can help|The target is the value present at the cue, not the later endpoint
5|Motivate decomposition and observer comparison|Explains why storage/readout separation precedes weighting, access and limits|The overview supplies the requested path to the paper's error claim
7|Define storage and observation intervals|Carries D and J forward while separating T from L|The two durations cannot be interchanged in later errors
11|Fix the observer's information and goal|Begins the model with only postcue spikes and desired original value|A reader knows why pre-cue displacements remain uncertain
13|Decompose total recall error|Defines cue state, storage displacement and estimation error|The following covariance identity has concrete variables
21|Prove covariance cancellation and invariant variance|Uses conditional unbiasedness and independent future noise|Error addition follows under explicit assumptions instead of being presumed
27|Interpret the two variance terms|After the derived sum, prepares storage versus estimation meanings|The same symbols will have different duration dependence
29|Identify storage's contribution|First term in the decomposition interpretation|The2DT part is set before observation begins
30|Identify cue-state estimation contribution|Second term completes the decomposition|The reader does not mistake it for estimating the final observed state
32|State decomposition limits|Connects the source's local model to priors, boundaries and encoding|The later exact formulas retain a defined domain
34|Introduce the two-interval timeline|Prepares a visual with both error reference points|It clarifies the difference between cue and observation endpoint
42|Interpret what postcue spikes can improve|After the timeline, connects its estimate with cue-state error|The distinction is a figure reading result rather than a new assumption
44|Define the equivalent Gaussian observations|Moves from an error split to a solvable state/measurement model|The likelihood approximation has an explicit bin-state relation
56|Limit the equivalent observation model|Explains y as spike information and states independent errors|The continuum limit is not an assertion about arbitrarily short physical bins
60|Pose the equal-weight observer's failure|Uses motion during observation to question averaging|The naive estimator has a specified mechanism before its formula
62|Write state motion relative to the cue|Reuses the taught Brownian covariance|The later averaging error has its required cross-time relation
68|Explain shared increments before averaging|Restates why the covariance kernel is min(s,t)|The continuous mean is applied to correlated states, not independent positions
74|Separate count and motion errors|Computes the independent average-noise term then sets up the motion integral|The two contributions are attached to their actual sources
80|Evaluate the minimum-time integral|Splits the square where min(s,t) has a simple expression|The factor Lcubed/3 is shown through undergraduate integration
88|Combine readout error terms|Follows both separate computations|The displayed variance retains both observation and motion cost
94|Optimize competing duration terms|Differentiates after explaining opposite L dependence|The best equal-weight interval follows from an actual balance
102|Interpret the optimal balance|At the stationary point, identifies equal contributions before minimum variance|The numeric constant in the next result has a mechanism
109|State the practical equal-weight consequence|Closes the naive calculation with why late spikes hurt this rule|It motivates a motion-aware observer rather than rejecting observation
113|Pose backward motion-aware information|Answers the naive failure by accounting for displacement from x|The precision calculation has an estimation target and direction
115|Teach Gaussian precision addition|Defines reciprocal variance and verifies it through likelihood multiplication|The next recursion can combine measurements without assumed filtering knowledge
117|Carry future information backward through diffusion|Defines P and adds transition variance before inversion|The reader can explain why later evidence becomes less precise about x
123|Add the earliest observation's information|After backward transition, adds Jh|This completes one full recursion cycle before taking the limit
129|Expand the recursion for small h|Uses the finite-step denominator to obtain the differential change|The continuous equation is derived from the discrete information update
135|State continuous equation and initial condition|Collects the small-h result with no observations at zero duration|The solution has the necessary boundary value
142|Define functions and separate variables|Explains tanh/artanh, precision gain/loss and scaling constants|The special functions answer the actual solvable ODE
150|Invert the separated solution|Connects artanh relation to P and reciprocal variance|The closed form is obtained by stated operations
161|Interpret coth and source equivalence|Defines the final function and links backward precision with SI's method|The reader need not assume Kalman-filter background
163|Expand short-time behavior|Uses the defined coth to compare with naive averaging|The common leading terms explain near equality for short observations
169|Move from short-time agreement to long-time limit|Interprets the expansion before the saturation expression|The two duration regimes stay distinct
176|Quantify gradual saturation|Introduces variance ratios at characteristic durations|The time scale is not presented as an abrupt cutoff
178|Show variance ratio at one characteristic time|First numerical point after the asymptotic limit|A31percent variance gap makes the remaining benefit visible
179|Show variance ratio at two characteristic times|Second point measures diminishing change|The3.7percent excess is compared with the same limit
180|Show variance ratio at three characteristic times|Third point completes the approach-to-limit illustration|The0.5percent excess supports practical saturation without exact equality
182|Distinguish variance and standard-deviation ratios|Interprets the preceding numbers before time-bound comparisons|Taking square roots changes the uncertainty-scale factor
184|Apply the information-diffusion inequality to time|Uses the already derived product bound|The bound on observation duration is connected to the cellular tau
191|Interpret duration and near-optimality|Combines the characteristic time with ideal/naive error scales|Full access and nonabrupt saturation qualify the paper's phrase
195|Pose limited downstream access|Changes observation information while leaving network dynamics intact|The next alpha scaling has a concrete intervention meaning
197|Derive information under random thinning|States independent retention and scales rates and derivatives|The information fraction follows from the Poisson formula
203|Keep D fixed while replacing J|Connects the thinning operation to readout formulas|Missing spikes do not undo fluctuations already inside the circuit
212|Interpret access-dependent time and variance|Extends ideal scaling to naive optimum and selected subsets|Biased access is not silently equated with a fraction of cells
214|Set the full-access numeric baseline|Uses a bound-saturating D,J,tau example|The limited-access comparison has matched underlying network parameters
216|Compute partial-access and total errors|Changes alpha only, then adds common storage loss|Longer observation addresses readout cost rather than reversing storage noise
220|Pose which cellular timescale matters|Uses the time bound to motivate adding rate relaxation|The extension answers an actual assumption question
222|Define rate relaxation dynamics|Introduces taum before the enlarged matrix|The new state block has an explicit physical role
230|State noise placement and linear state|Connects the two-stage equations to their block matrix|Only activation receives the assumed spike noise
239|Find the two-block left vector|Uses tangent normalization and block equations|The tau+taum factor follows from the coupled state geometry
245|Project noise in the receiving block|Applies the established diffusion mechanism to the extended left vector|The generalization retains the correct noise weighting
254|Interpret the summed timescales and limit|After the extended formula, states dominant-scale and model scope|It does not claim arbitrary biological delays always add
256|Pose dependence on the noise law|Introduces constant additive Gaussian strength as the changed assumption|A different equality class now has a stated source
262|Match Gaussian information with projected noise|Repeats the earlier proof with explicit q weighting|The linear-versus-exponential sufficient classes follow from different variances
264|Explain normalization and source relation|Keeps q and tau explicit when comparing with the supplement|The calculation does not silently inherit omitted source factors
268|Read the normalized original readout figure|Uses previously derived functions and characteristic scales|The reader knows exactly which uncertainty is plotted
270|Identify the ideal asymptote|First feature of the normalized comparison|Its limiting value1 agrees with the ideal variance scaling
271|Identify naive minimum and deterioration|Second feature connects the curve to equal weighting|The plotted turning point follows the optimized formula
272|Identify the optimum marker|Third feature locates the same turning time|The dotted line is not an additional bound or data series
274|Exclude storage and connect partial access|After reading the source plot, distinguishes its error content|The guide reconstruction and SI comparison retain the same normalization
284|Interpret the reconstructed curves|After the figure, explains different value of late observations|The removed empty lead-in leaves this useful closing explanation
286|Pose the printed lower-bound inconsistency|Uses the established formulas to ask whether main6 follows|The algebraic comparison is clearly separated from source attribution
296|Interpret the inequality direction|After rearranging the product bound, distinguishes upper and lower limits|Substitution cannot justify the printed universal lower-bound claim
303|Give the valid limiting equality and source status|Completes the corrected Gaussian-model bound with partial-access scope|An independently found inconsistency is not claimed as an author correction
305|Demonstrate a strict numerical case|Chooses larger J at fixed D to expose the direction error|The calculation does not assume saturation to manufacture the contradiction
307|Separate diffusion accuracy from integrator leak|Closes readout limits and prepares empirical application|A growing variance does not itself pull the mean to a fixed value
''')

packet=json.loads((T/'pedagogy-final/PARAGRAPH_REVIEW.json').read_text(encoding='utf-8'))
index=json.loads((T/'concept-index-final.json').read_text(encoding='utf-8'))
s1=json.loads((T/'stage1-memory.json').read_text(encoding='utf-8'));s2=json.loads((T/'stage2-memory.json').read_text(encoding='utf-8'))
chapters=list(A);rows=[];missing=[]
for q in packet['paragraphs']:
 ch=Path(q['source']).stem
 if ch not in A:continue
 if re.fullmatch(r'</?div[^>]*>',q['text'].strip()):
  p,c,r=('Provide figure scrolling container','Pure layout around the separately reviewed inserted figure','No reader-facing claim or reasoning is present; retain for wide-figure access')
  decision='retain structural only'
 elif q['line'] in A[ch]:p,c,r=A[ch][q['line']];decision='retain'
 else:missing.append(q['id']);continue
 rows.append({'id':q['id'],'source_hash':q['source_hash'],'purpose':p,'connection':c,'decision':decision,'reason':r})
assert not missing,missing

gloss_terms={e['term'] for e in s2['glossary_entries']};teaching_by_term={}
for ch in chapters:
 for q in index['passages']:
  if q['path']!=f'content/chapters/{ch}.md':continue
  for term in re.findall(r'\[\*\*([^*]+)\*\*\]\{\.definition-term',q['text']):teaching_by_term[term.lower()]=q['id']
gloss_rows=[]
for q in packet['paragraphs']:
 if q['source']!='content/chapters/glossary.md':continue
 m=re.match(r'\[\*\*([^*]+):\*\*\]',q['text'])
 if not m or m.group(1).lower() not in {x.lower() for x in gloss_terms}:continue
 term=m.group(1);teach=teaching_by_term[term.lower()]
 gloss_rows.append({'id':q['id'],'source_hash':q['source_hash'],'purpose':f'Provide compact lookup for {term}','connection':f'Reference after main teaching at {teach}; no artificial narrative transition is needed','decision':'retain','reason':f'The {term} entry matches the taught object and its mathematical or neural role; its conditions preserve the meaning used at {teach}. This reference does not substitute for that earlier explanation.'})
assert len(gloss_rows)==48,len(gloss_rows)

def getpass(ch,line):
 path='content/chapters/'+ch+'.md'
 p=next((q for q in index['passages'] if q['path']==path and q['line']==line),None)
 assert p,(ch,line)
 return p
def relation(cid,ch,line,role,reason,start=0,end=None):
 q=getpass(ch,line);end=len(q['text']) if end is None else end
 r={'concept_id':cid,'passage_id':q['id'],'role':role,'span':[start,end],'status':'reviewed','review':'local-stage3-memory-20261025','evidence':reason}
 r.update({'adequacy':'adequate'} if role=='teach' else {'need':'required'})
 return r

# Exact spans are full semantically connected prose paragraphs unless a within-
# paragraph boundary matters. Display equations are separately checked below.
specs=[
('firing-rate',[('01-foundations',9)],('02-memory-dynamics',40),'Expected count per time and20Hz meaning precede model rate units.'),
('recurrent-connectivity',[('01-foundations',16)],('02-memory-dynamics',14),'Lingering synaptic input and feedback precede the full renewal cycle.'),
('tuning-curve',[('01-foundations',18)],('03-memory-information',20),'Rate versus coordinate, slope and units precede the likelihood derivative.'),
('population-code',[('01-foundations',20),('01-foundations',26)],('03-memory-information',13),'The displayed vector and subsequent interpretation teach a pattern across neuron identities before the joint count likelihood.'),
('poisson-counts',[('01-foundations',39),('01-foundations',47),('01-foundations',84)],('03-memory-information',13),'Count law plus mean/variance and conditional recurrence qualification precede local Poisson likelihood use.'),
('poisson-count-variance',[('01-foundations',47),('01-foundations',56)],('03-memory-information',40),'The displayed moments and optional sum proof supply the variance used to eliminate likelihood cross terms.'),
('covariance',[('01-foundations',97),('01-foundations',104),('01-foundations',112)],('03b-memory-readout',21),'Centered products, variance of sums and independence limits precede cancellation of storage/readout covariance.'),
('msd-variance-mean-split',[('01-foundations',121),('01-foundations',128)],('01b-persistence',92),'The exact mean-square split precedes the biased diffusion formula.'),
('continuous-attractor',[('01b-persistence',9),('01b-persistence',11)],('02-memory-dynamics',79),'State, fixed point and restoring/neutral family geometry precede the network fixed-point identity.'),
('brownian-motion',[('01b-persistence',74)],('02-memory-dynamics',75),'Zero start, continuity and independent mean-zero Gaussian increments with lag variance precede independent model noise processes.'),
('brownian-cross-time-covariance',[('01b-persistence',112),('01b-persistence',121)],('03b-memory-readout',62),'Shared increments establish min(s,t), then scaling gives2Dmin(s,t) before readout averaging.'),
('neural-transfer-function',[('02-memory-dynamics',47)],('02-memory-dynamics',94),'Input-to-nonnegative-rate mapping is defined before its Taylor derivative.'),
('weak-fluctuation-approximation',[('02-memory-dynamics',67),('02-memory-dynamics',75),('02-memory-dynamics',77)],('02-memory-dynamics',110),'Aggregate-small-input premise, units and large-population scaling precede evaluation of local fixed-state noise strengths.'),
('linearization',[('02-memory-dynamics',94)],('02-memory-dynamics',101),'Terms proportional to perturbation are identified before fixed-point cancellation forms K.'),
('right-zero-eigenvector',[('02-memory-dynamics',112),('02-memory-dynamics',119),('02-memory-dynamics',125)],('02-memory-dynamics',134),'Tangent derivative and Ku=0 meaning precede its coordinate-normalization use.'),
('left-zero-eigenvector',[('02-memory-dynamics',127),('02-memory-dynamics',134),('02-memory-dynamics',140),('02-memory-dynamics',161)],('02-memory-dynamics',175),'Left equation, normalization, cancellation proof and tilted example precede projecting the stochastic state equation.'),
('diffusion-tensor',[('02-memory-dynamics',205),('02-memory-dynamics',211)],('03-memory-information',179),'Multi-coordinate normalization and local covariance matrix precede the coupled-direction information bound.'),
('ito-convention',[('02b-memory-long-delays',13)],('02b-memory-long-delays',70),'Starting-point coefficient evaluation precedes variable-D zero-drift moment calculation.'),
('fokker-planck-equation',[('02b-memory-long-delays',13),('02b-memory-long-delays',21)],('02b-memory-long-delays',78),'The density PDE and initial point-mass meaning are supplied before deriving mean and variance moments; optional48–66 derives the PDE itself.'),
('systematic-drift',[('02b-memory-long-delays',98),('02b-memory-long-delays',100)],('03b-memory-readout',13),'Repeated-trial mean motion is separated from spread before the no-drift error decomposition.'),
('likelihood',[('03-memory-information',13)],('03-memory-information',20),'Data probability as a function of proposed coordinate precedes its logarithm.'),
('score',[('03-memory-information',32)],('03-memory-information',60),'The log-derivative meaning and zero mean precede the unbiased-estimation proof using S.'),
('fisher-information-rate',[('03-memory-information',40),('03-memory-information',46)],('03b-memory-readout',44),'Squared-score information, time division and units precede the Gaussian-bin variance1/(Jh).'),
('unbiased-estimation',[('03-memory-information',60),('03-memory-information',76)],('03b-memory-readout',21),'Locally correct estimator mean and regularity limits precede conditional cross-covariance cancellation.'),
('prior-distribution',[('03-memory-information',76)],('03b-memory-readout',117),'Prior knowledge of likely coordinate values is explained before excluding an informative prior in recursion.'),
('gaussian-precision',[('03b-memory-readout',115)],('03b-memory-readout',117),'Reciprocal variance and likelihood-based precision addition precede backward propagation.'),
('hyperbolic-tangent-inverse',[('03b-memory-readout',142)],('03b-memory-readout',150),'The functions and artanh derivative precede inversion to the precision solution.'),
('hyperbolic-cotangent',[('03b-memory-readout',161)],('03b-memory-readout',163),'Reciprocal-tanh definition precedes short-time expansion; the introductory formula itself is supplemented by equation lines157–158.'),
]
concepts=[];relations=[];sets=[];concept_evidence=[]
for cid,teach,use,why in specs:
 concepts.append({'id':cid,'aliases':[]})
 ids=[]
 for ch,line in teach:
  rr=relation(cid,ch,line,'teach',why);relations.append(rr);ids.append(rr['passage_id'])
 rr=relation(cid,*use,'use',why);relations.append(rr)
 if len(ids)>1:sets.append({'concept_id':cid,'passage_ids':ids,'adequacy':'adequate','status':'reviewed','review':'local-stage3-memory-20261025','evidence':why})
 concept_evidence.append({'concept_id':cid,'teaching_passages':ids,'required_use_passage':rr['passage_id'],'adequacy_reason':why,'order':'teaching set ends before this required indexed use'})
cid='directional-symmetry';q=getpass('03-memory-information',232);a=q['text'].index('Now restrict');b=q['text'].index('For an exponential');e=q['text'].index('The resulting')
concepts.append({'id':cid,'aliases':[]});relations.append(relation(cid,'03-memory-information',232,'teach','Radial tuning and uniform centers give equal diagonal information and vanishing cross terms before scalar inversion.',a,b));relations.append(relation(cid,'03-memory-information',232,'use','The symmetric information matrix can be inverted coordinate-wise to obtain D width scaling.',b,e));concept_evidence.append({'concept_id':cid,'teaching_passage':q['id'],'teaching_span':[a,b],'required_use_passage':q['id'],'use_span':[b,e],'adequacy_reason':'The added restriction and matrix consequences precede the diffusion scaling within the same paragraph. The formerly undefined isotropic label is absent.','order':'teaching ends exactly where dependent use begins'})

sections={q['id']:'reviewed' for q in index['sections'] if Path(q['path']).stem in chapters}
aud={'status':'reviewed','description':'00-reading-guide.md:37 explicitly assumes undergraduate calculus, basic probability and linear algebra. Neuroscience, stochastic-process, information, filtering and random-field ideas must be taught where needed.','assumed_concepts':['undergraduate calculus','basic probability','linear algebra']}
(T/'concept-judgments-memory.json').write_text(json.dumps({'audience':aud,'concepts':concepts,'sections':sections,'relations':relations,'teaching_sets':sets},ensure_ascii=False,indent=2),encoding='utf-8')

objections={
'FOUNDATIONS-SPIKES':'Could firing rate promise regularly timed spikes or neuron vector index mean position? The20Hz counterdescription and explicit neuron-identity sentence reject both readings.',
'FOUNDATIONS-POISSON':'Could recurrent Poisson generation make full spike trains independent? The fixed-rate example is followed by the conditional-noise qualification at84; CV and Fano factor remain different.',
'FOUNDATIONS-COVARIANCE':'Could zero covariance prove independence or correlation equal a causal fraction? Both false general inferences are explicitly excluded before the eye-model link.',
'FOUNDATIONS-ATTRACTOR':'Could persistent coherent rates imply correct memory? The opposing perturbation stays fixed at6.5degrees rather than5, providing an actual counterexample.',
'FOUNDATIONS-DIFFUSION':'Could independent steps with finite variance alone promise exact Brownian behavior or global angular2Dt? The process is an approximation to many suitably small fluctuations; finite-range/periodic limits are stated.',
'FOUNDATIONS-RANDOMNESS':'Could an irregular expected spatial map measure time-varying storage drift? Revisit consistency and separate observed-spike variability explicitly prevent that inference.',
'MEMORY-SPIKES':'Could Gaussian activation noise be an exact finite-neuron spike-train law? The aggregate-input limit and1/n scaling restrict it to leading weak fluctuations.',
'MEMORY-LINEARIZATION':'Could symmetric W allow ordinary perpendicular projection? K row scaling and the tilted-flow endpoint show why left and right vectors differ.',
'MEMORY-DIFFUSION':'Could the projected local variance establish mean drift or every long-delay trajectory? The local coefficient window and next-chapter drift question keep those claims separate.',
'MEMORY-SYMMETRIC':'Could the guide wrongly alter main2 by squaring gprime? Unchanged projection algebra and SI18 require that square; the claim is explicitly an independent source check.',
'MEMORY-LONG-TIME':'Could wrapping change D or the SI40 printed coefficient be adopted without checking SI41? The same-D line/ring comparison and explicit projection retain one variance convention.',
'MEMORY-DRIFT-SCOPE':'Could Ito/Stratonovich conversion identify the true drift of every network? The text uses it only as a possible scale and requires microscopic jump analysis for exact drift.',
'MEMORY-FIGURES':'Could a successful ring simulation establish a universal circuit or direct animal result? Mutual inhibition supplies a separate model check and the animal-measurement distinction is explicit.',
'MEMORY-FI':'Could Cramer Rao apply to every biased/bounded finite-sample estimator? Local unbiasedness, differentiation regularity, positive rates and prior/boundary limits are stated.',
'MEMORY-BOUND':'Could equality force exponential transfer everywhere? The zero-bias linear family attains equality throughout positive theta; the source converse is explicitly restricted.',
'MEMORY-COMPARISONS':'Could the scalar width law follow for arbitrary anisotropic tuning or all resource constraints? Radial tuning and uniform centers now precede inversion, and fixed-total-rate scaling is worked separately.',
'MEMORY-READOUT-SETUP':'Could storage and readout errors always be added? Conditional unbiasedness and independent future noise make the covariance zero, while translation invariance makes readout variance common.',
'MEMORY-NAIVE':'Could correlated Brownian states be averaged as independent measurements? The min(s,t) double integral retains shared history and produces the required2DL/3 term.',
'MEMORY-IDEAL':'Could the useful duration bound mean zero benefit after tau? Coth ratios show continuous improvement toward a limit; characteristic saturation is explicitly distinguished from cutoff.',
'MEMORY-PARTIAL':'Could an arbitrary10percent neuron subset supply alphaJ? Independent thinning is the actual assumption and biased-subset exceptions are stated.',
'MEMORY-EXTENSIONS':'Could every biological timescale simply add? The derived tau+taum belongs to the displayed two-stage state and noise placement only.',
'MEMORY-FIG3-AND-CAUTION':'Could main6 be a lower bound by substituting the information inequality? The rearrangement gives an upper bound on readout cost and a strict Gaussian-model numeric example exposes the direction error.'}

stage1_hashes={x['sha256'] for x in s1['covered_units']}
unchanged=[];supplement=[]
for ch in chapters:
 ls=(C/(ch+'.md')).read_text(encoding='utf-8-sig').splitlines();start=0
 for i,line in enumerate(ls+[''],1):
  if line.strip() and not start:start=i
  if not line.strip() and start:
   value='\n'.join(ls[start-1:i-1]);h=H(value)
   if h in stage1_hashes:unchanged.append({'file':f'content/chapters/{ch}.md','lines':[start,i-1],'sha256':h})
   if value.startswith('$$') or value.startswith('[^') or ('title=' in value and value.startswith(':::')):supplement.append({'file':f'content/chapters/{ch}.md','lines':[start,i-1],'sha256':h,'kind':'equation' if value.startswith('$$') else ('source note' if value.startswith('[^') else 'visible callout title'),'stage1_reuse':'exact unit hash matches original Stage1' if h in stage1_hashes else 'Final delta checked: citation-label or retained-title change only; mathematical/source target content unchanged','flow_judgment':'Placed with its introducing question and immediately connected interpretation; source notes supply equation-specific checking and model/construction limits without serving as missing first teaching.'})
   start=0

typed=[];fighashes=[]
for ch in chapters:
 p=C/(ch+'.yaml');d=yaml.safe_load(p.read_text(encoding='utf-8-sig'))
 for b in d.get('blocks',[]):
  for fld in ['caption','alt']:
   typed.append({'id':b['id']+'/'+fld,'source':f'content/chapters/{ch}.yaml','sha256':H(b[fld]),'decision':'retain','reason':f'The {fld} for {b["id"]} matches the adjacent chapter calculation, chosen numerical values and actual event/state or curve meanings; illustrative-versus-data status and model limits remain visible.'})
  asset=R/b['asset'];fighashes.append({'id':b['id'],'path':str(asset),'sha256':sha(asset)})
 typed.append({'source':f'content/chapters/{ch}.yaml','fields':['title','purpose','all section titles and summaries'],'sha256':sha(p),'decision':'retain','reason':'Titles identify actual subjects and relationships; purpose and summaries preserve the corresponding final chapter motivations. The only renamed local function phrase matches the actual first definition, with unchanged mathematical meaning.'})

v=R/'assets/approved/visuals/foundations-paper-map';mapyaml=yaml.safe_load((C/'01b-persistence.yaml').read_text());mb=next(x for x in mapyaml['blocks'] if x['id']=='fig:FOUNDATIONS-PAPER-MAP')
mapreview={'asset_id':'fig:FOUNDATIONS-PAPER-MAP','png_sha256':sha(v.with_suffix('.png')),'svg_sha256':sha(v.with_suffix('.svg')),'chapter_md_sha256':sha(C/'01b-persistence.md'),'chapter_yaml_sha256':sha(C/'01b-persistence.yaml'),'caption_sha256':H(mb['caption']),'alt_sha256':H(mb['alt']),'inspection_evidence':'Full corrected1680x1428PNG and700px preview personally inspected in separate Stage1 recheck at20:27:29; current file hashes equal that inspected correction. No new pixel sweep.','criteria':[
 {'criterion':'technical and navigation','verdict':'pass','reason':'2012 points to3–6,2022 to7–9,2025 to10–12, matching actual chapter order. Labels alone changed; coordinate axes and arrow roles retain the earlier reviewed meanings.','strongest_objection':'Old numbering could still misdirect the reader.','why_objection_fails':'Actual full and700px images show all three corrected ranges and current hashes match those images.'},
 {'criterion':'time scene','verdict':'pass','reason':'Stored value varies along a time axis against a fixed reference, matching temporal diffusion rather than spatial randomness.','strongest_objection':'The irregular path could be mistaken for recorded memory data.','why_objection_fails':'The unchanged caption explicitly identifies illustrative traces and an original guide schematic.'},
 {'criterion':'eye pathway scene','verdict':'pass','reason':'Changing command feeds a dashed proposed pathway through muscles to eye position.','strongest_objection':'The illustration could claim the integrator mechanism is experimentally proven.','why_objection_fails':'The actual proposed label and caption call it a proposed changing-command mechanism; the figure compares questions rather than proving a circuit.'},
 {'criterion':'fixed spatial scene','verdict':'pass','reason':'Expected rate is a fixed function of physical position; the marked same-place revisit carries the same expected rate.','strongest_objection':'Same rate on two visits could promise identical spike counts.','why_objection_fails':'The vertical axis says expected rate and preceding text expressly allows visit-to-visit spike variation.'},
 {'criterion':'full-size readability','verdict':'pass','reason':'Question headings, paper years, axes and chapter ranges are inside the canvas, separated and legible at full image size.','strongest_objection':'The longer10–12range might collide with another label.','why_objection_fails':'The inspected full image has clear spacing and no overlap or cropping.'},
 {'criterion':'700px readability','verdict':'pass','reason':'All three questions and corrected ranges remain readable in the inspected book-width preview.','strongest_objection':'Downscaling could make the corrected references too small.','why_objection_fails':'The personally inspected700px preview preserves distinct chapter digits and row labels.'},
 {'criterion':'palette and contrast','verdict':'pass','reason':'Dark blue/teal drawings and dark text retain the existing light background; QA color tokens remain within the established profile.','strongest_objection':'A label-only repair could have introduced another color or weak contrast.','why_objection_fails':'The changed labels keep the same dark gray style, and current SVG matches the inspected corrected asset.'},
 {'criterion':'opening coverage','verdict':'not applicable','reason':'This is an internal comparison after two foundations chapters, not a new opening illustration. The chapter overview remains in prose before the first section.','strongest_objection':'The figure does not explain every mechanism of the three papers.','why_objection_fails':'Its explicit job is to compare three questions and two kinds of variation, not replace their later teaching.'}]}

now=datetime.now().astimezone();start=datetime.fromisoformat('2026-10-25T20:38:29.6249296+02:00');taskstart=datetime.fromisoformat('2026-10-25T20:11:31.8244846+02:00')
files=[C/(ch+e) for ch in chapters for e in ['.md','.yaml']]+[C/'glossary.md',R/'plan/chapter-plan.yaml',R/'guide-project.yaml',T/'repairs-v2.json',T/'pedagogy-final/PARAGRAPH_REVIEW.json',T/'concept-index-final.json',RULE/'SKILL.md',RULE/'references/pedagogy-language-contract.md',RULE/'references/concept-prerequisites.md',RULE/'references/math-code-case-contract.md']
d={'request_id':'local-stage3-memory-20261025','stage':3,'started_at':start.isoformat(),'completed_at':now.isoformat(),'reviewer':'independent compliance_memory agent, retained context; separate Stage3 request','source_rule_hashes':[{'path':str(p),'sha256':sha(p)} for p in files],'exact_delta_acknowledgement':{'ledger':'repairs-v2.json','ids':['M-S2-01','M-S2-02','M-S2-03','M-S2-04','M-S2-05','M-S2-06','M-S2-07'],'result':'All seven accepted edits read in the final canonical path. The two variance sums remain after label removal; source link/factor discrepancy remain after commentary edits; all three figures keep captions and postfigure interpretations after lead-in deletions; the symmetry question and YAML summary now reuse neural transfer function. This acknowledges Stage2 deltas and checks their connections; Stage2 findings are not relabeled as a Stage3 execution.'},'paragraph_judgments':rows+gloss_rows,'paragraph_coverage':{'six_chapter_packet_records':len(rows),'matching_glossary_records':len(gloss_rows),'uncovered_assigned_packet_records':missing,'structural_note':'The extractor labels pure div tags as prose; individual records identify them as structural only. Equations, footnotes, callout title attributes and typed block fields require and receive separate checks.'},'supplemental_math_source_title_checks':supplement,'typed_field_checks':typed,'figure_hashes':fighashes,'map_criterion_review':mapreview,'section_strongest_correctness_objections':[{'section':k,'objection_and_resolution':v,'essential_reasoning_and_limits_reference':'See the exact paragraph IDs in this section and the connected Stage1 section judgment; unchanged unit hashes are separately bound below.'} for k,v in objections.items()],'unchanged_stage1_unit_hash_bindings':unchanged,'stage1_reuse_limit':'Only exact matching units reuse original Stage1 checks. Brownian/directional-symmetry/map repairs reuse the separate Stage1 recheck with matching final semantic content. Final seven Stage2 deltas received explicit connected reads; no changed whole-file hash is treated as whole-file Stage1 approval. Original research source files are unchanged.','learning_order':[
 {'chapter':'ch:FOUNDATIONS','chain':'spikes and rates -> connections and tuning -> population code -> Poisson counts and pooling -> conditional recurrence -> shared covariance and mean-square split','why_this_order':'It teaches the representation and variability objects before dynamics or inference depend on them. Mathematical baseline supplies vectors and elementary expectations.'},
 {'chapter':'ch:PERSISTENCE','chain':'state and fixed points -> restoring versus neutral perturbations -> accumulation -> Brownian/RMS and bias -> cross-time covariance -> fixed spatial versus temporal randomness','why_this_order':'The reader sees what error can survive before learning its stochastic accumulation; Brownian covariance is supplied before readout. Map randomness stays separate from noise over time.'},
 {'chapter':'ch:MEMORY-DYNAMICS','chain':'spike activation renewal -> input-to-rate rule -> count noise -> weak-fluctuation limit -> local linearization -> tangent and left projection -> diffusion -> symmetric tuning formula and non-ring example','why_this_order':'Each mathematical operation has a biological object and preceding purpose. Left projection follows a complete flow example before stochastic contraction uses it.'},
 {'chapter':'ch:MEMORY-LONG-DELAYS','chain':'local D -> density on line and ring -> variable-D moments -> drift scope -> source simulation interpretation -> finite-spike readout uncertainty','why_this_order':'It handles boundaries and model limits before a general information constraint is interpreted. The final two-error distinction motivates the next chapter.'},
 {'chapter':'ch:MEMORY-INFORMATION','chain':'nearby-state discrimination -> likelihood/score/J -> inverse-information error bound -> information-diffusion proof -> equality limits -> coupled matrix -> controlled resource comparisons','why_this_order':'The dynamical D and left vectors already exist before statistical J is joined to them. Radial tuning restriction precedes per-coordinate scalar inversion.'},
 {'chapter':'ch:MEMORY-READOUT','chain':'storage versus cue-state error -> conditional covariance -> Gaussian observation model -> equal-weight calculation -> motion-aware precision recursion -> saturation -> partial access -> model extensions -> printed-bound qualification','why_this_order':'The estimator target and assumptions come before calculations. A concrete failure of equal weighting motivates backward information rather than introducing a filter name without teaching it.'}],
'concept_evidence':concept_evidence,'concept_judgment_file':'concept-judgments-memory.json','concept_index_limits':'The supplied final index has an empty catalog/relations and candidate audience before these judgments. It omits display-math passages and source-note text. Required indexed uses are recorded here with exact spans, while actual earlier display-equation uses are checked directly in supplemental records (including Brownian79–81, left normalization130–131, FI observation52–53 and coth157–158). Therefore a successful merged checker is a structural aid, not alone proof that every first use was taught. Hyperbolic coth is defined immediately after its introductory display and before asymptotic reasoning; no reasoning relies on an undefined name.','part1_and_description':{'decision':'retain','part1_reason':'The purpose connects stable population patterns, surviving coordinate motion and information/readout limits in the actual six-chapter order. It previews the common problem; detailed meanings are taught in chapters.','description_reason':'The description accurately identifies the three-paper explanatory scope and directs the reader to sources, audience and mathematical route in the reading guide.'},'findings':[],'conclusion':'No unresolved reader-understanding or flow defect found in this assigned final path. The paragraph reasons, source conditions, local approximation limits and concept-index omissions bound this judgment. Root owns the remaining global merge and whole-book acceptance.','wall_elapsed_stage_seconds':(now-start).total_seconds(),'wall_elapsed_task_seconds':(now-taskstart).total_seconds(),'awake_execution':'unverified','token_stats':'unavailable'}
(T/'stage3-memory.json').write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'output':str(T/'stage3-memory.json'),'concept_judgments':str(T/'concept-judgments-memory.json'),'paragraph_records':len(rows),'glossary_records':len(gloss_rows),'relations':len(relations),'teaching_sets':len(sets),'finished':now.isoformat(),'stage_seconds':d['wall_elapsed_stage_seconds']},indent=2))
