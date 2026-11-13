# Part I Stage 3: understanding and teaching order

Request final-memory-flow-20261029-03. Reviewer /root/accept_memory, GPT-6 Astra, high reasoning. Context reviewer_continuation. Started 2026-10-29T13:48:54.6710733+02:00. Input 9f0a39deb00485620bcd26154f68eec0f7b2dcd002687073df8013f86be406a8. Contract 593934f3af51c49175417df3e4263df20a0835575d099bad4f0070163b4a17dc. Completion is appended after checks. Awake execution unverified. Token stats unavailable.

The six assigned chapters were reread in connected order, with the preceding reading guide, equations, folds, captions, labels and sidecars. The separate eye-timing deletion does not change this group's files. No unassigned chapter is accepted here. Earlier stage reports remain unchanged.

## 0 ch:FOUNDATIONS
Refs: F3,F9
Problem: How can changing neural activity still represent a useful position or location?
Prerequisites: The reading guide has introduced neurons and the three scientific questions. The opening uses ordinary language and postpones formal coding and noise tools to the sections that teach them.
Continuity: The common persistence problem leads to spike meaning, count variability, shared variation and displacement statistics in that order.
Roles: Neural signals represent behaviorally useful quantities; the three papers study different aspects of that representation.
Bridge: The opening connects biological tasks to quantities that subsequent chapters model, without requiring an equation yet.
Trace: Not applicable: line 5; this opening identifies the common problem. Concrete cell and count traces follow in its assigned sections.
Example: Not applicable: line 9; the roadmap sets dependencies rather than claiming a numerical example.
Alternatives: Common problem: describe variable representations. Options: memory loss, eye drift and spatial firing maps. Relationship: complementary questions. Criteria: what varies and what is measured. Selection or scope: all three are introduced, then their mechanisms are separated. Verdict: adequate.
Chain: Understand the shared behavioral need; identify neural events and coding; quantify observation variability; distinguish shared and directional changes.
Next: The reader now needs the meaning of a spike and a firing-rate pattern.

## 1 sec:FOUNDATIONS-SPIKES
Refs: F13,F17,F22,F24,F32,F38,F47
Problem: What neural quantity represents angle or location, and what is merely a noisy observation of it?
Prerequisites: Neuron is taught in the reading guide. Spike, rate, synapse, excitation, inhibition and recurrence are taught here before tuning and population coding use them.
Continuity: Events lead to connections, lingering effects, rate tuning, population vectors and spatial examples. Anatomy clarifies the scope of the spatial models.
Roles: The sending cell emits spikes; connections affect receiving cells; the population rate pattern represents a coordinate; an observer decodes spikes.
Bridge: The scalar rate curve becomes a vector across cell identities. A spatial rate map divides observed spikes by occupancy, separating expected firing from an estimate.
Trace: The 20 Hz interpretation and local linear angular tuning make rate and slope concrete; CA3/CA1 and grid/place comparisons fix the biological objects.
Example: Inputs, rate units and slope units are supplied for the linear tuning example; its positive-rate domain limits the conclusion.
Alternatives: Common problem: interpret neural responses. Options: expected tuning versus finite rate map, cell index versus physical position, grid versus place fields. Relationship: distinct objects, not competing estimates of one quantity. Criteria: what is indexed and how measured. Selection or scope: preserve each role. Verdict: adequate.
Chain: Define event and expected rate; explain influence and feedback; map coordinate to rates; combine cells; distinguish measured spatial maps from expected functions.
Next: A rate pattern alone does not say how much a brief spike count can vary.

## 2 sec:FOUNDATIONS-POISSON
Refs: F51,F59,F68,F80,F88,F92,F108,F116,F119
Problem: How uncertain is a finite spike count, and why can population averaging help?
Prerequisites: Rate and tuning have been taught. The count law, mean, variance and conditional independence are supplied before pooling or recurrent-noise use; basic expectation algebra is the audience baseline.
Continuity: Count probabilities lead to moments, relative spread, a worked example, the recurrent conditional qualification and distinct empirical variability measures.
Roles: K counts spikes in a finite interval; lambda is an expected count; repeated observations vary even with the same modeled rate.
Bridge: Rate times duration becomes expected count; count moments become uncertainty of a rate estimate.
Trace: One 20 Hz cell over 50 ms has expected count one and silence probability 0.368; twenty independent cells reduce relative spread while preserving mean rate per cell.
Example: The cell count, duration, conditional independence and common per-cell plotting axis are stated. The conclusion concerns independent variability and explicitly excludes automatic cancellation of shared input variation.
Alternatives: Common problem: quantify spike variability. Options: count variance/Fano factor and interval CV. Relationship: different statistics. Criteria: sampled object and counting conditions. Selection or scope: no substitution without extra assumptions. Verdict: adequate.
Chain: Specify the count distribution; obtain mean and variance; compare signal with its spread; pool independent counts; qualify recurrence and empirical measures.
Next: Shared fluctuations survive pooling, motivating covariance and physiological pathway distinctions.

## 3 sec:FOUNDATIONS-COVARIANCE
Refs: F123,F129,F133,F137,F161,F168,F172,F174,F180,F199,F203,F204,F206
Problem: Which changes in recorded eye movement indicate shared drive, random spreading, mean bias, gain or measurement error?
Prerequisites: Spikes, rates and independent versus shared variability are established. Covariance and correlation receive visible physical meanings before optional formulas. Lag and displacement are defined before MSD.
Continuity: The pathway precedes statistics; shared-drive inference precedes normalization; random versus directional movement precedes the MSD split and parameter consequences.
Roles: Shared command and private spike contributions affect muscles; predicted displacement is an analysis; measured eye position also contains recording error.
Bridge: Neural co-variation becomes displacement covariance. Centering separates variance from mean motion, while gains convert input fluctuations to measured units.
Trace: The X=g_X S+private-noise construction shows why private noise lowers correlation. Doubling a constant bias doubles mean displacement and quadruples its squared MSD contribution.
Example: Units, independence and the position of gains and added noise are explicit. The example is a teaching construction, not the full eye inference model.
Alternatives: Common problem: explain a changed MSD or correlation. Options: shared drive, private noise, bias, gain, muscle smoothing and measurement noise. Relationship: distinct potentially combined causes. Criteria: covariance, mean, lag shape and units. Selection or scope: no statistic alone identifies a circuit. Verdict: adequate.
Chain: Identify the pathway; explain shared and private variation; define covariance and normalization; separate mean from spread; map each physical change to an observable feature.
Next: The upstream circuit must explain how a represented command persists yet wanders.

## 4 ch:PERSISTENCE
Refs: P3,P5
Problem: Why can a stable activity pattern still hold a wrong value?
Prerequisites: Population coding is established. The opening distinguishes activity from represented value before asking for state-space geometry.
Continuity: Two kinds of disturbance motivate restoring and neutral directions, then repeated errors and the contrast with fixed spatial randomness.
Roles: Neural activities form the representation; the represented angle is one quantity decoded from many activities.
Bridge: A biological representation becomes a point in activity space with different disturbance directions.
Trace: Not applicable: line 3; the opening prepares the two-cell trace taught next.
Example: Not applicable: line 6; this is a dependency roadmap, not an additional worked model.
Alternatives: Common problem: interpret disturbed activity. Options: a changed activity pattern with the same value or a different persistent value. Relationship: different directions in representation space. Criteria: the lasting decoded coordinate. Selection or scope: distinguish both. Verdict: adequate.
Chain: Separate representation from value; ask which disturbances decay; follow the lasting changes across time.
Next: State, fixed point and neutral direction give this distinction a precise model.

## 5 sec:FOUNDATIONS-ATTRACTOR
Refs: P11,P17,P19,P21,P27,P35,P55,P57,P61,P62,P74
Problem: Which disturbances does feedback remove, and which become memory error?
Prerequisites: Rates, tuning and recurrence are available. State and fixed point precede the attractor definition; neutral direction and represented dimension are explained before the example.
Continuity: A physical account comes before formal geometry; a visible sum/difference account prepares optional equations and two numerical disturbances.
Roles: The common rate change is restored; the rate difference represents angle and is neutral. An imposed disturbance is separate from deterministic recovery.
Bridge: The two rates become mean deviation x and decoded angle theta, making the stable and neutral coordinates explicit.
Trace: From rates (50,30), a (+3,+3) change recovers the same angle; (+3,-3) leaves a 6.5-degree fixed state.
Example: The baseline, tuning slope, decay rate, positive-rate domain and common initial condition are supplied. The conclusion concerns this guide model; larger networks require their actual return flow.
Alternatives: Common problem: classify a disturbance. Options: common-rate and opposite-rate changes. Relationship: restoring versus neutral directions. Criteria: final angle after recovery. Selection or scope: the model corrects only the common component. Verdict: adequate.
Chain: Define the state family; identify restored and neutral coordinates; solve their dynamics; compare disturbances; limit the geometric shortcut.
Next: Repeated retained coordinate changes produce a distribution of memory errors.

## 6 sec:FOUNDATIONS-DIFFUSION
Refs: P80,P86,P102,P114,P120,P124,P130,P142,P156,P162,P171,P175
Problem: How do repeated small retained errors accumulate, and how does random spread differ from bias?
Prerequisites: The attractor's lasting coordinate changes are understood. Equal-step independence, zero mean and variance are stated before the sum. Brownian properties are taught before later stochastic equations require them.
Continuity: Physical increments lead to optional step algebra, a visible variance law, units and RMS, optional bias numbers, visible shared-history meaning and long-time limits.
Roles: D measures half the coordinate variance rate; one trajectory can reverse while the ensemble spreads. Mean bias and recording coordinates are separate quantities.
Bridge: A sum of retained increments becomes Brownian motion and 2Dt; variance becomes RMS in coordinate units; shared increments become cross-time covariance.
Trace: D=0.02 and v=0.10 produce equal random and squared-bias MSD terms at four seconds. The Brownian split explains covariance at two times.
Example: Chosen numerical values and unbounded-domain assumptions are explicit. Paths are illustrative; RMS is not a boundary. Later readout restates the covariance formula and its physical reason.
Alternatives: Common problem: characterize error over time. Options: random diffusion, constant bias, finite/periodic domains and feedback. Relationship: different mean, variance and boundary effects. Criteria: time dependence and coordinate convention. Selection or scope: 2Dt is local or unbounded under its conditions. Verdict: adequate.
Chain: Accumulate independent zero-mean steps; define the variance rate; interpret RMS; add bias separately; explain shared history; state domain limits.
Next: A fixed random spatial function is another kind of variability and must not be confused with this temporal process.

## 7 sec:FOUNDATIONS-RANDOMNESS
Refs: P181,P183,P187,P197
Problem: Does spatial irregularity imply temporal instability of the represented position?
Prerequisites: Rate maps and temporal diffusion have both been taught. The unit explains their indexing directly.
Continuity: Revisiting a fixed map contrasts with a wandering memory, then the paper map assigns each question its proper kind of variation.
Roles: Position indexes a fixed expected-rate function; time indexes changes of the internal state; actual spikes can remain variable on each visit.
Bridge: The argument separates functions of physical position from stochastic paths through time.
Trace: Evaluating the same location twice gives the same expected rate under the fixed-map model, though observed spikes differ.
Example: Cell and environment are held fixed for the map comparison; the schematic does not establish one combined circuit.
Alternatives: Common problem: interpret variability. Options: temporal wandering and fixed spatial randomness. Relationship: compatible but non-equivalent. Criteria: indexed variable and repeated-observation meaning. Selection or scope: each paper addresses its own question. Verdict: adequate.
Chain: Identify what varies; hold the map fixed across revisits; allow spike variability; reject unsupported cross-inferences; choose the next paper route.
Next: The memory chapters derive the dynamics of a wandering coordinate in a recurrent circuit.

## 8 ch:MEMORY-DYNAMICS
Refs: D3,D5,D7,D9
Problem: How can the cell model determine the rate of lasting memory loss?
Prerequisites: Foundations supplied recurrence, attractors and D. The opening recalls coordinate notation and source-navigation conventions before the detailed calculation.
Continuity: Activation renewal leads to return-flow projection and then variance, with symmetry reserved for a later specialization.
Roles: Current theta and initial Theta differ; bars denote steady states; tau is the synaptic decay time.
Bridge: The roadmap connects cellular spike effects to a coordinate-level diffusion prediction.
Trace: Not applicable: line 5; the detailed traces belong to the model and projection sections that follow.
Example: Not applicable: line 9; the opening fixes notation and scope rather than claiming a worked example.
Alternatives: Common problem: compute diffusion. Options: general return-flow projection or the symmetric-weight tuning formula. Relationship: general method and special case. Criteria: reciprocal weight symmetry. Selection or scope: derive the general result first. Verdict: adequate.
Chain: Define the model; separate transient and retained changes; add noise variance; specialize only with stated symmetry.
Next: The first required object is activation left by earlier spikes.

## 9 sec:MEMORY-SPIKES
Refs: D13,D15,D17,D23,D39,D48,D54,D58,D78,D86,D90,D94,D103
Problem: How do brief random events renew activity that decays continuously?
Prerequisites: Spike, rate, recurrence, Poisson counts and Brownian increments have preceding teaching. The transfer function and aggregate approximation are explained locally before their reasoning use.
Continuity: The exact jump model and trace precede weighted receiving input, noise moments, Gaussian approximation and steady states.
Roles: N_i counts events; s_i stores outgoing decaying effects; W maps them to g_i; phi maps input to rate; renewed spikes feed back.
Bridge: Event times become an activation sum, then a coupled dynamical system and a controlled Gaussian approximation.
Trace: The five-spike trace shows unit jumps and exponential decay; population replication preserves mean input while reducing variance.
Example: Unit-jump normalization, time constant and illustrative spike inputs are stated. The replication argument explains a limiting approximation, not an exact finite-network identity.
Alternatives: Common problem: describe spike-driven state evolution. Options: exact jump process and weak aggregate Gaussian approximation. Relationship: original model and leading approximation. Criteria: small total-input fluctuations and sufficient population scaling. Selection or scope: preserve the exact model's meanings. Verdict: adequate.
Chain: Count spikes; accumulate decaying activation; map weighted input to rate; separate mean and fluctuation; justify the approximation; identify balanced steady states.
Next: A small state disturbance must be followed through the local return dynamics.

## 10 sec:MEMORY-LINEARIZATION
Refs: D107,D109,D116,D129,D131,D138,D144,D148,D157,D163,D174,D180,D192
Problem: Which part of an arbitrary state disturbance remains as a changed memory?
Prerequisites: The fixed-point equation, activation-rate relation, transfer rule and noise model are already established. Linearization is explained using Taylor expansion; left and right zero vectors are taught with their distinct roles.
Continuity: Physical recovery motivates a linear matrix, tangent direction, normalized coordinate extractor and a tilted-flow check.
Roles: The right vector is the persistent state direction; the left vector measures the retained coordinate and removes decaying modes.
Bridge: A cell-state perturbation becomes a scalar memory displacement through the actual dynamical projection.
Trace: The two-variable system has y decay while x shifts by a/lambda times the starting y, so perpendicular projection misses the retained shift.
Example: The local equations and stable lambda are stated; the example is a guide construction, not a neural simulation from the paper.
Alternatives: Common problem: extract final memory from disturbed activity. Options: perpendicular geometric projection and left-vector return-flow projection. Relationship: the former is not generally valid. Criteria: actual decay directions and normalization. Selection or scope: use the dynamical projection. Verdict: adequate.
Chain: Taylor-expand; cancel the fixed terms; interpret the matrix; differentiate the fixed family; normalize the left vector; remove decaying modes; read the retained coordinate.
Next: Projecting random spike increments through that coordinate gives the diffusion rate.

## 11 sec:MEMORY-DIFFUSION
Refs: D210,D212,D219,D227,D235,D241,D243,D245,D246,D250
Problem: How much coordinate variance do the independent spike fluctuations leave after recovery?
Prerequisites: Left projection and Brownian increment covariance have been taught. The variance rule for independent weighted increments is restated before use.
Continuity: The scalar projected variance precedes multiple coordinates, interpretation and the two local time-scale conditions.
Roles: Each cell supplies a rate-dependent noise variance and a retained-coordinate weight; their product contributes to D.
Bridge: Activation noise covariance becomes coordinate displacement covariance and then a diffusion tensor.
Trace: The displayed sum explicitly eliminates cross terms and multiplies each cell's variance by its squared left-vector weight.
Example: This is a symbolic trace, with weak noise, local coefficients and sufficient spike aggregation stated. A separate numerical trace follows under symmetry.
Alternatives: Common problem: describe retained fluctuations. Options: scalar diffusion and a joint tensor for several coordinates. Relationship: scalar case and extension. Criteria: number and coupling of represented coordinates. Selection or scope: include cross-coordinate terms when needed. Verdict: adequate.
Chain: Apply the left vector; use independent increment covariance; match 2D; generalize the coordinate weights; state the valid local window.
Next: Symmetric weights may remove the need to solve a general left-vector problem explicitly.

## 12 sec:MEMORY-SYMMETRIC
Refs: D254,D258,D265,D273,D281,D291,D295,D299,D305,D312,D318,D334
Problem: When can diffusion be expressed using tuning curves and transfer responses?
Prerequisites: The general diffusion formula, left normalization and chain rule are available. Reciprocal weight symmetry is stated separately from translation symmetry.
Continuity: Input and rate derivatives yield a left vector, a specialized formula, its source check and an optional two-cell verification.
Roles: Reciprocal weights identify g-prime as a left direction; normalization converts it to coordinate response. The example's neutral coordinate is activation difference.
Bridge: Connectivity-dependent projection becomes a tuning-derivative expression without assuming a ring.
Trace: Mutually inhibiting cells have opposing rates but constant sum, giving constant interior D; the plotted positive-rate domain excludes boundaries.
Example: Weights, biases, transfer rule, coordinate and plot values are explicit. The example does not specify boundary behavior where linear rates would become negative.
Alternatives: Common problem: simplify network diffusion. Options: reciprocal weight symmetry and translation symmetry. Relationship: distinct conditions, only the former is required here. Criteria: the transpose calculation. Selection or scope: the formula applies beyond rings. Verdict: adequate.
Chain: Differentiate tuning identities; use W symmetry; normalize g-prime; substitute into projected variance; check units, assumptions and a simple network.
Next: The local D must be embedded in a distribution over time, with domain and drift effects checked.

## 13 ch:MEMORY-LONG-DELAYS
Refs: L5,L9,L11
Problem: What changes when a wandering value leaves the local region or reaches a boundary?
Prerequisites: D and the local approximation have been taught; this opening recalls them with coordinate and initial-value notation.
Continuity: The preceding local-window limit motivates density evolution, drift distinctions and source-figure interpretation.
Roles: The memory coordinate moves; its domain and local noise rate constrain the resulting error distribution.
Bridge: A local variance rate becomes a question about a distribution over a larger domain and longer time.
Trace: Not applicable: line 6; the opening names mechanisms that the following line-circle calculation will isolate.
Example: Not applicable: line 9; this unit is the dependency roadmap.
Alternatives: Common problem: extend a local prediction. Options: unbounded line, wrapped angle, varying D and mean drift. Relationship: different extensions. Criteria: domain and dynamics. Selection or scope: first isolate boundaries with constant D. Verdict: adequate.
Chain: Recall the local result; identify conditions that can change; choose controlled long-delay comparisons.
Next: A density equation makes those comparisons quantitative.

## 14 sec:MEMORY-LONG-TIME
Refs: L15,L17,L21,L39,L43,L51,L58,L64,L78,L80,L90,L98,L109,L116
Problem: How do boundaries and state-dependent rates change memory-error distributions?
Prerequisites: Brownian increments and local D precede this section. Itô evaluation, trial density and point-mass initial condition are taught before their use; the optional PDE derivation uses stated moments and calculus.
Continuity: Constant-D line and circle establish the boundary effect before a mutual-excitation example varies D.
Roles: p is a distribution across trials; the angular reporting interval is bounded; excitation changes both rates and their noise while leaving projection weights fixed.
Bridge: Increment moments yield density evolution; wrapping a Gaussian yields angular error; projection of the excitation model gives D(theta).
Trace: The same D gives unbounded 2Dt but wrapped mean squared error approaching pi squared over three. The excitation example shows linear variance despite linear state-dependent D.
Example: Domain, coordinate convention, positive rates and boundary-term conditions are stated. Source factor differences are distinguished from author corrections.
Alternatives: Common problem: predict long-delay error. Options: line versus circle and constant versus state-dependent D. Relationship: controlled changes of domain or local noise. Criteria: coordinate geometry and moment evolution. Selection or scope: do not infer changed neural noise from a wrapped plateau. Verdict: adequate.
Chain: Define density and noise convention; obtain its evolution; solve and wrap constant-D motion; interpret the plateau; derive moments under varying D; test a neural example.
Next: A variance calculation still does not settle systematic motion of the mean.

## 15 sec:MEMORY-DRIFT-SCOPE
Refs: L129,L131,L139,L141,L143,L145
Problem: What does the diffusion calculation leave unresolved about mean drift and correlated noise?
Prerequisites: Random spread and mean bias were separated in foundations. Itô and state-dependent D are taught immediately before the Stratonovich comparison.
Continuity: Physical mean-versus-spread meaning precedes drift sources, convention comparison, order estimates and correlated-noise scope.
Roles: Weight mismatch and noise geometry can move the mean; tuning may cancel a mean velocity without cancelling individual random increments.
Bridge: Different increment conventions produce an extra written drift, while correlated increments replace a diagonal noise covariance by Q.
Trace: Substituting b=sqrt(2D) into the conversion term gives D-prime over two; the correlated extension uses v-transpose Q v.
Example: Both are local symbolic checks. The conversion is a possible scale estimate, not the exact microscopic drift of every network.
Alternatives: Common problem: describe noisy state motion. Options: Itô and Stratonovich conventions, independent and correlated fluctuations. Relationship: different processes or noise assumptions unless transformed consistently. Criteria: increment evaluation and joint covariance. Selection or scope: keep the analyzed Poisson model separate from extensions. Verdict: adequate.
Chain: Separate mean and spread; identify microscopic drift sources; state convention effects; compare orders; limit compensation; explain what correlated noise would change.
Next: Original figures can now be read as tests of specific dynamics and as a bridge to readout uncertainty.

## 16 sec:MEMORY-FIGURES
Refs: L149,L151,L155,L156,L158,L169,L174,L176,L178,L191
Problem: Which plotted object or comparison tests which part of the memory model?
Prerequisites: Return-flow projection, diffusion, angular wrapping and tuning have already been taught. Activity bump and rotational symmetry receive local explanations before panel reasoning.
Continuity: Figure 1 separates memory coordinate and readout uncertainty; Figure 2 compares network dynamics across architectures; the ending motivates information.
Roles: Rates, spike marks, represented angle, simulated variance and a lower bound are distinct plotted quantities.
Bridge: The original artwork is translated into the guide's coordinate, projection and error concepts.
Trace: Follow an off-attractor point along noise-free flow, compare its next retained endpoint, then distinguish bump movement from finite-spike localization uncertainty.
Example: Panel descriptions state the simulation scope and reporting convention. Original artwork remains optional while its necessary meanings are explained visibly.
Alternatives: Common problem: test the diffusion prediction. Options: ring and mutual-inhibition designs. Relationship: different architectures using the same projection principle. Criteria: predicted versus simulated displacement statistics. Selection or scope: these are model tests, not animal measurements. Verdict: adequate.
Chain: Identify the coordinate; separate storage and observation errors; assign every curve its quantity; compare model predictions with simulations; pose the information question.
Next: Derive a statistical measure of finite-spike uncertainty from the same tuning curves.

## 17 ch:MEMORY-INFORMATION
Refs: I5,I7,I13
Problem: Why should spike-based estimation accuracy constrain the motion of a stored value?
Prerequisites: The spike model, tuning and retained-coordinate diffusion are established. Information is first explained as local distinguishability rather than assumed as a known technical quantity.
Continuity: The shared spike source connects observer uncertainty to recurrent noise, while the opening separates a bound from achieved performance.
Roles: The network and observer both receive random spikes; neither has direct access to noiseless expected rates.
Bridge: The dynamical D will be compared with statistical sensitivity J for the same coordinate and network.
Trace: Not applicable: line 5; the opening poses the connection that the score and projection calculations will prove.
Example: Not applicable: line 9; numerical equality and strictness examples follow the bound.
Alternatives: Common problem: interpret better information. Options: a lower permitted minimum or a lower achieved D. Relationship: possibility versus actual circuit performance. Criteria: equality condition. Selection or scope: do not infer one from the other. Verdict: adequate.
Chain: Identify shared spike variability; quantify distinguishability; connect it to the retained-noise response; interpret a lower bound.
Next: A count likelihood and its local sensitivity provide the required information measure.

## 18 sec:MEMORY-FI
Refs: I17,I19,I21,I28,I40,I48,I54,I62,I70,I72,I74,I88
Problem: How does a short spike sample distinguish nearby represented values?
Prerequisites: Positive rates, conditional Poisson moments and tuning slopes are available. Likelihood, score, information rate, unbiasedness and prior distribution are explained before dependent steps.
Continuity: Physical distinguishability leads to likelihood, score variance, an error bound, its limits and a controlled tuning illustration.
Roles: Counts are observations; theta is the proposed parameter; J is information per unit duration, not total information or a firing rate.
Bridge: The rate distribution becomes likelihood sensitivity, then an inverse-information error scale.
Trace: Compute score variance using Poisson moments; compare same-slope tuning curves with different baseline firing.
Example: The likelihood is local and regular, and the finite-sample bound need not be attained. Extra baseline changes count noise while leaving slope fixed.
Alternatives: Common problem: infer a state from spikes. Options: internal versus sensory parameter, unbiased local estimation versus changed priors/bias. Relationship: different targets or inference conditions. Criteria: the actual tuning law and information duration. Selection or scope: the current internal-state model. Verdict: adequate.
Chain: State the observation law; differentiate log likelihood; compute score variance; define J; derive inverse-information variance; interpret slope and noise contributions.
Next: The same slopes and noise can be compared with the network's normalized projection.

## 19 sec:MEMORY-BOUND
Refs: I92,I94,I104,I110,I125,I129,I131,I141,I151,I155,I165,I195,I209,I221,I238
Problem: What minimum diffusion follows from spike information, and when is it attained?
Prerequisites: D, J, tangent normalization and Cauchy Schwarz are available or restated. Matrix ordering and invertibility are explained before the matrix inverse is used.
Continuity: General inequality precedes interpretation, equality conditions, counterexamples and multidimensional extension.
Roles: Two weighted vectors encode retained spike noise and information; their fixed dot product enforces the scalar bound.
Bridge: Normalized network geometry becomes a statistical lower bound through vector lengths; quadratic forms extend it to all coordinate combinations.
Trace: The linear excitation family attains equality without an exponential transfer. The inhibition example keeps D fixed while its information bound becomes strict away from zero.
Example: Parameters, positive-rate domains and coordinate units are supplied. Main text already states exponential sufficiency and non-necessity before the optional counterexample.
Alternatives: Common problem: attain or interpret the bound. Options: pointwise matching, exponential sufficient class, linear equality family and strict inequality. Relationship: criterion, sufficient examples and failures of equality. Criteria: projection weights proportional to information weights. Selection or scope: preserve the general criterion. Verdict: adequate.
Chain: Fix the dot product by normalization; identify the two lengths; apply Cauchy Schwarz; test equality; separate sufficiency from necessity; require full rank for matrix inversion.
Next: Improving a network requires a controlled comparison, not just reading the bound in isolation.

## 20 sec:MEMORY-COMPARISONS
Refs: I248,I254,I260,I262,I264,I270,I274,I282,I289,I291,I305,I306,I308,I318,I322
Problem: Which network changes improve persistence when other resources or tuning properties are held fixed?
Prerequisites: Scalar and matrix information bounds precede the comparisons. Every new scaling family supplies its varied and fixed quantities. Radial symmetry is explained before off-diagonal terms are discarded.
Continuity: Neuron count, rate and synaptic-time comparisons lead to width versus dimension, then an alternative resource constraint and sensory-memory scope.
Roles: N, rate scale, tau and width are controlled parameters; tuning shape, density and firing budget determine what else changes.
Bridge: Population sums become scaled sums or integrals; changes in active-cell volume and slope explain dimension-dependent information.
Trace: Fixed-rate tuning gives inverse-square tau scaling, while fixed activation curves give inverse tau. Width contributes competing volume and squared-slope powers.
Example: The integral assumes uniform dense coverage away from boundaries. Fixed peak versus total population rate produces different conclusions, which are explicitly compared.
Alternatives: Common problem: improve persistence. Options: change population, rate, time or width under different constraints. Relationship: controlled comparisons, not universal rankings. Criteria: fixed quantities, actual information and achieved equality. Selection or scope: use the law whose assumptions match the proposed change. Verdict: adequate.
Chain: Choose controls; propagate their effect through tuning and projection; calculate J and D scaling; test another resource constraint; limit biological co-location claims.
Next: Knowing J and D allows a calculation of what a downstream observer can recover over time.

## 21 ch:MEMORY-READOUT
Refs: R5,R9,R11
Problem: How long should an observer collect spikes when the state keeps moving during observation?
Prerequisites: Information rate, diffusion and the difference between current and initial state are established. Storage delay T and observation duration L are explicitly separated here.
Continuity: Cue-state recovery motivates total-error decomposition, observer comparison, partial access and model extensions.
Roles: The original value precedes storage; the cue state starts readout; later spikes estimate that cue state without revealing the earlier random path.
Bridge: A persistent-state model becomes an estimation problem with a defined observation window and target.
Trace: Not applicable: line 6; the opening prepares the explicit timeline and Gaussian-bin model next.
Example: Not applicable: line 9; this roadmap does not add another numerical case.
Alternatives: Common problem: estimate a moving memory. Options: equal weighting and a diffusion-aware observer. Relationship: different inference rules on the same future observations. Criteria: cue-state error versus observation duration. Selection or scope: compare both before changing access assumptions. Verdict: adequate.
Chain: Separate storage history from cue-state evidence; define T and L; compare inference rules; check extensions and total-error claims.
Next: A local observation model makes the two error sources calculable.

## 22 sec:MEMORY-READOUT-SETUP
Refs: R17,R19,R31,R35,R43,R55,R56,R58,R60
Problem: Under what assumptions can storage variance and readout variance be added?
Prerequisites: Likelihood, information duration, Brownian increments and unbiasedness were taught earlier. Translation invariance receives its local readout meaning before one common readout variance is used.
Continuity: Observer access precedes Gaussian bins, error definitions, the cross-covariance proof, limitations and the timeline.
Roles: Theta is original memory, x the cue state, x-hat its estimate, s storage displacement and e readout error. y_k summarizes bin evidence rather than a new physical measurement.
Bridge: Spike likelihood is represented by Gaussian observation noise; the timeline becomes a variance decomposition with its cross term explicitly checked.
Trace: Conditional zero mean of e given storage history gives zero covariance with s, leading to 2DT plus readout variance.
Example: The timeline identifies both errors and the conditions for adding them. The approximation requires informative weak-noise bins, not exact Gaussianity at arbitrarily short physical times.
Alternatives: Common problem: decompose recall error. Options: the local unbiased translation-invariant model or state dependence, boundaries, priors and encoding uncertainty. Relationship: base case and changed inference problems. Criteria: zero cross term and cue-independent readout variance. Selection or scope: use the sum only with the stated conditions. Verdict: adequate.
Chain: Define access and target; specify transitions and observations; split errors; show the cross term vanishes; impose equal readout statistics across cue states.
Next: The readout variance can now be computed for a specific weighting rule.

## 23 sec:MEMORY-NAIVE
Refs: R72,R74,R80,R86,R92,R102,R108,R118,R125
Problem: Why does equal weighting eventually make a longer observation worse?
Prerequisites: The observation model and information rate are established. Brownian cross-time covariance is taught in persistence and both its identity and shared-history meaning are restated locally.
Continuity: The weighting rule precedes separate count and motion errors, their sum, its optimum and interpretation.
Roles: Each observed bin estimates a different current state; the target remains the cue state x.
Bridge: Correlated motion across times becomes a double covariance integral, while independent observation noise averages down.
Trace: Splitting the square into two triangles yields the motion term 2DL/3; adding 1/(JL) gives a finite optimal interval.
Example: The symbolic trace states all variables and keeps motion and count contributions separate. Its minimum concerns this weighting rule, not the ideal observer.
Alternatives: Common problem: reduce readout error by waiting. Options: observation-noise reduction and accumulated-motion error. Relationship: opposing duration effects. Criteria: total cue-state variance. Selection or scope: the equal-weighting optimum balances the two. Verdict: adequate.
Chain: Write the average; account for shared motion; integrate its covariance; add count noise; differentiate; interpret the finite optimum.
Next: An observer that accounts for state motion can use later evidence more appropriately.

## 24 sec:MEMORY-IDEAL
Refs: R129,R133,R135,R143,R151,R157,R164,R168,R187,R205,R212,R218,R220,R227
Problem: How can additional observations keep helping while their benefit approaches a limit?
Prerequisites: Gaussian likelihood and independent transitions are established. Precision and its addition rule are derived before recursion. Hyperbolic functions are defined in the optional exact solution before dependent series calculations.
Continuity: The physical inference question leads to precision addition, a backward step, a differential equation, its interpretation, optional solution and visible limiting result.
Roles: P measures information about the beginning of the interval. Later likelihoods lose precision when moved backward through state uncertainty; new observations add precision.
Bridge: A discrete Gaussian inference step becomes a scalar precision equation, then reciprocal error and a characteristic observation time.
Trace: One recursion step adds Jh after transition variance reduces later precision. The visible ratios at one, two and three characteristic times quantify saturation.
Example: No informative prior and the local Gaussian assumptions are stated. The finite-time function calculation is optional, while the physical mechanism, asymptotic error, time scale and non-abrupt limit remain visible.
Alternatives: Common problem: estimate the cue state. Options: equal weighting and diffusion-aware inference. Relationship: same data with different use of temporal dependence. Criteria: readout variance over L. Selection or scope: ideal inference is a benchmark, not a demonstrated neural implementation. Verdict: adequate.
Chain: Define precision; move future likelihood backward through diffusion; add new information; derive gain-minus-loss evolution; solve or interpret the limit; compare with tau under the bound.
Next: The full-access assumption can be relaxed without changing the memory network's own D.

## 25 sec:MEMORY-PARTIAL
Refs: R233,R235,R241,R252,R258,R260
Problem: What changes when a downstream area observes only part of the spike information?
Prerequisites: J, D and ideal/naive time scales are established. Independent thinning is specified before identifying alpha as an information fraction.
Continuity: The physical access limitation precedes information rescaling, time/error consequences, selection caveats and an optional numerical case.
Roles: The full network continues to diffuse; the observer receives fewer spikes. Access is not a change to the recurrent dynamics.
Bridge: Thinned rates and slopes imply alpha J, which is substituted into the existing readout formulas.
Trace: One-tenth access increases characteristic time and limiting readout variance by square root of ten while leaving the two-second storage term unchanged.
Example: Tau, J, D, alpha and T are supplied with units. The equality-case full-access baseline is separated from the partial-access observer.
Alternatives: Common problem: model limited access. Options: unbiased spike thinning and a selected neuron subset. Relationship: equal spike fraction need not mean equal information fraction. Criteria: actual rate derivatives and noise. Selection or scope: alpha J requires the stated sampling condition or an information-fraction definition. Verdict: adequate.
Chain: Keep network D fixed; reduce observed rates and slopes; compute observed information; rescale time and variance; test selection assumptions.
Next: Other dynamical time scales and noise laws can also change the quantitative conclusions.

## 26 sec:MEMORY-EXTENSIONS
Refs: R266,R270,R278,R280,R289,R297,R308,R312,R318,R320,R322
Problem: Which parts of the bound depend on the cell dynamics or the noise law?
Prerequisites: Linearization, left projection, score-based information and the equality criterion are already taught. New rate-adjustment time and Gaussian strength q are explicitly introduced.
Continuity: A two-stage dynamical extension precedes a separate constant-noise extension, with each model stated before its derivation and interpretation.
Roles: Synaptic activation and rate are separate state blocks; noise enters the activation block. In the Gaussian comparison, q is the common variance scale.
Bridge: The same projection and information methods apply to an enlarged state or a changed likelihood, revealing which factors change.
Trace: Block normalization produces tau plus tau_m. Constant Gaussian noise yields J as squared slope over q and makes a linear transfer a sufficient equality class.
Example: Noise placement, symmetry and normalization are explicit. The time-sum result is not extended to arbitrary collections of biological time constants.
Alternatives: Common problem: extend the base model. Options: immediate versus gradual rate response and Poisson versus constant Gaussian noise. Relationship: changed dynamical or likelihood assumptions. Criteria: projected covariance and matched information. Selection or scope: recompute under the chosen model. Verdict: adequate.
Chain: State the changed model; build its linear or likelihood representation; project noise; match information; derive the modified factor or equality condition; limit its scope.
Next: The source readout figures and printed total-error claim can now be interpreted with the assumptions kept separate.

## 27 sec:MEMORY-FIG3-AND-CAUTION
Refs: R330,R332,R333,R334,R336,R362,R364,R374,R383,R385,R387
Problem: What do the readout curves show, and what total-error inequality actually follows?
Prerequisites: Ideal and naive formulas, normalization, partial access and storage decomposition are already taught. Main text gives the necessary curve features before optional original artwork.
Continuity: Normalized readout interpretation precedes the printed-bound comparison, a strict example and the final distinction between diffusion and leak.
Roles: Plots show readout variance, not total error. Storage adds 2DT. A lower information bound supplies an upper limit on the cellular-time replacement term.
Bridge: Mathematical formulas become normalized curves and then an inequality-direction check against the source.
Trace: A strict case with J=40000 gives total asymptotic variance 0.0205 below the printed 0.021 value, while satisfying the actual information inequality.
Example: D, tau, J and T are given with units, and equality is not assumed. The claim is an independent source inconsistency check, not an author correction.
Alternatives: Common problem: describe final recall error. Options: valid Gaussian-model lower bound and a substituted cellular-time expression. Relationship: they coincide at saturation, but not universally. Criteria: inequality direction and equality condition. Selection or scope: retain the derived bound with its assumptions. Verdict: adequate.
Chain: Identify plotted quantities; separate storage from readout; apply the information inequality in the right direction; test a strict case; distinguish uncertainty growth from restoring leak.
Next: Applying these memory predictions to eye motion requires measured spike statistics, calibration, drift, signal access and mechanical response.

## 28 part:MECHANISMS::part-opening
Refs: PART
Problem: How can sustained neural activity still lose accuracy in the remembered angle?
Prerequisites: The preceding reading guide has established neurons and the question. The Part opening uses plain biological descriptions; continuous attractor in the title is a topic preview, not an assumed working tool.
Continuity: Neural signals lead to persistent representations, noise-driven motion, information limits and readout. The six chapter roles follow that dependency order.
Roles: A population firing pattern represents angle; random timing perturbs it; an observer estimates it from spikes.
Bridge: The Part connects representation, dynamics and statistical inference without introducing unsupported notation.
Trace: Not applicable: chapter-plan.yaml Part purpose; this opening states the path and leaves worked traces to the six chapters.
Example: Not applicable: Part purpose; no standalone numerical claim is made.
Alternatives: Common problem: understand memory accuracy. Options: representation, persistence dynamics and estimation. Relationship: dependent explanatory levels. Criteria: what the reader must know before the next question. Selection or scope: teach in that order. Verdict: adequate.
Chain: Explain signals and representation; derive retained stochastic changes; connect the resulting stability to spike-based estimation.
Next: The foundations begin with the neural events that make both representation and noise possible.

## Front-matter promise and fold check

For this group, the promise in 00-reading-guide.md:74,106,133 is met. Neural primitives precede the network model; Brownian increments precede stochastic dynamics; projection precedes diffusion; likelihood and information precede readout; precision is taught before backward inference. The glossary is a lookup aid, not the sole source of any required teaching.

The main path supplies the physical meaning and results needed to continue. Examples include covariance/shared-drive meaning at 01-foundations.md:129-133, the visible MSD split at174-181, restored versus persistent two-cell changes at01b-persistence.md:21, D and variance growth at114-124, and shared history at156-157. The readout section restates Brownian covariance and its reason at03b-memory-readout.md:74-80, so a skipped earlier proof does not leave the calculation unexplained. The ideal-observer gain/loss interpretation at164 and asymptotic result at205-228 remain outside the hyperbolic-function solution fold. Exponential sufficiency and non-necessity are visible at03-memory-information.md:151 before the optional counterexample. Matrix meaning and invertibility appear at221 and238 outside the short residual proof. Original source figures are folded, but their panel meanings and comparison results remain visible.

Formal definitions inside folds, such as Brownian motion, covariance formulas and hyperbolic functions, are needed for a full calculation path. The guide does not pretend that skipping those details teaches the algebra. The main conceptual path retains the associated physical explanation and required outcome, and later reasoning-dependent use either follows the teaching in reading order or restates the needed identity. No required fold-placement repair was found.

Paragraph decisions are in the JSON with current full IDs. They distinguish 329 teaching-content records, 46 layout/fold records and 82 comment-only lint controls. Hidden controls are not counted as newly taught material. The three conditional internal-summary notes from Stage 2 remain internal metadata observations; no current standalone rendered summary was found. Figure pixel acceptance and publication acceptance remain outside this call.

## Completion

Completed 2026-10-29T14:12:51.6346771+02:00. Stage 3 verdict: pass for the assigned Part I text and current connected teaching path. No required understanding or flow repair was found. All 29 units have the ten remaining fields and supported reader questions. All 457 current paragraph IDs retain their source hashes and have purpose, connection, decision and reason: 329 teaching passages, 46 layout/fold records and 82 hidden controls. The concept record covers 47 concepts, 185 passage-span relations, 25 distributed teaching sets and 28 chapter sections.

Wall time 1436.964 seconds. Awake execution unverified. Historical Stage 1 and Stage 2 records are preserved. Current source/rule reuse remains for the separate requested recheck; pixels and publication acceptance are outside this call. Token stats unavailable.

Checkpoint record:

- 2026-10-29T13:53:44.5612383+02:00: wall 289.9 s; since previous 289.9 s; awake unverified. Connected source reading complete; paragraph and concept records underway.

- 2026-10-29T13:58:31.5683940+02:00: wall 576.9 s; since previous 287.0 s; awake unverified. 329 teaching records identified with 46 layout/fold records and 82 hidden controls; no required flow defect.

- 2026-10-29T14:05:34.1580578+02:00: wall 999.5 s; since previous 422.6 s; awake unverified. 329 specific paragraph drafts and 29 unit narratives saved; concept and structural records remained.

- 2026-10-29T14:11:12.2814621+02:00: wall 1337.6 s; since previous 338.1 s; awake unverified. Concept spans saved; final schema assembly and validation remained.

- 2026-10-29T14:12:51.6346771+02:00: wall 1437.0 s; since previous 99.4 s; awake unverified. Completed all unit, paragraph and concept records; counts, IDs, hashes and spans checked.
