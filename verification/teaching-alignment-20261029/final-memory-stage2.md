# Part I final review, Stage 2 necessity and language

Local request: final-memory-language-20261029-02. Reviewer: accept_memory, GPT-6 Astra, high reasoning. Context: reviewer_continuation after this reviewer's independent Stage 1. Started: 2026-10-29T13:33:01.4644193+02:00. Completion and measured timing are recorded below after validation. Awake execution time is unverified. Token stats unavailable.

Frozen input hash: 3fa06682def9f93bbafd2b39bfe5f3a5641febda3bbd57c2f9caf86c8b465283. Review contract hash: 593934f3af51c49175417df3e4263df20a0835575d099bad4f0070163b4a17dc.

Scope: 29 units, 457 extracted paragraph records, 331 selected claim rows, 380 advisory alerts, 176 bounded suppression regions. The 82 comment-only paragraph records are hidden controls, not reader prose. This call owns Definition and emphasis and Concrete wording fields. Stage 3 owns the remaining ten fields and every-paragraph decisions. Scientific judgments already made in Stage 1 are not counted as a new scientific call here. No manuscript edits, replacement passages, pixel review, or release acceptance.

## 0 ch:FOUNDATIONS
Definition: Adequate. The opening uses ordinary words before formal treatment. Neuron was defined in the reading guide; the chapter does not recolor it. The highlighted statement identifies persistence of a represented quantity, not a slogan about neuroscience.
Phrase: Both abilities require a useful quantity to remain represented in a changing biological system.
Paraphrase: A changing set of cells must still represent the position or location needed for behavior.
Actor: Neural activity across the relevant circuit.
Object: A useful eye position or location value.
Action: Continues representing the value while individual activity changes.
Condition: The brief command has ended or the animal is tracking its location.
Reason: Retain. This establishes the common reader problem before distinguishing the three papers. The following roadmap states the causal prerequisites, not only section titles.
Question: Why begin with spikes before discussing memory stability?
Answer: The reader needs the meaning and variability of the representation before asking how a circuit preserves it.

## 1 sec:FOUNDATIONS-SPIKES
Definition: Adequate. Spike, firing rate, synapse, excitatory and inhibitory input, recurrent connectivity, tuning curve, population code, encoding, decoding, rate map and grid cell receive blue first teaching definitions. Earlier neuron, hippocampus, place cell and place field remain ordinary text. The rate equation supplies units and the nonnegative-rate limit.
Phrase: The position of a cell in this vector is a neuron identity, rather than a location in physical space.
Paraphrase: An entry in the rate vector identifies a cell; it is not a place in the arena.
Actor: The vector index.
Object: The population's firing rates.
Action: Selects the rate belonging to one neuron.
Condition: Physical position or eye angle is represented by the pattern across the entries.
Reason: Retain. The contrast prevents confusing neuron space with represented space. Removing it would make the later attractor and spatial-map discussion easier to misread. The rate versus clock-like firing contrast likewise prevents a specific beginner error.
Question: Does 20 Hz mean one spike exactly every 50 milliseconds?
Answer: No. It specifies the expected count per second under the conditions, while individual spike times can vary.

## 2 sec:FOUNDATIONS-POISSON
Definition: Adequate. Poisson process is blue where the count distribution is introduced. CV and Fano factor are separately defined with their distinct denominators and measurements. Conditional independence is explained in words, not left as a label. The already introduced firing rate remains plain.
Phrase: CV and Fano factor cannot be substituted for one another without additional assumptions.
Paraphrase: Variation of intervals between spikes and variation of counts are different measurements.
Actor: The two variability measures.
Object: Interspike intervals and finite-interval counts.
Action: Quantify different kinds of spread.
Condition: A relation between them requires assumptions about spike generation and the counting interval.
Reason: Retain. The sentence prevents transferring the ocular-neuron interval result directly into a count-noise model. The worked counts and common-rate axes each teach a separate part of population averaging.
Question: Why can independent spike generation still give correlated recurrent spike trains?
Answer: Independence is conditional on the current modeled state; that state changes through recurrent activity and can be shared across cells and time.

## 3 sec:FOUNDATIONS-COVARIANCE
Definition: Adequate. Covariance and correlation coefficient have blue definitions followed by formulas and a shared-signal construction. Gain is a multiplier with specified units, and displacement is a difference of two positions. MSD was introduced earlier and is not recolored. Emphasis marks physical distinctions rather than unrelated terminology.
Phrase: Extra private noise can lower $\rho$ even when the shared drive has not weakened.
Paraphrase: Adding independent noise can reduce measured correlation without reducing the common input.
Actor: Private noise in the two measurements.
Object: The normalized correlation coefficient.
Action: Increases the spread in its denominator without increasing shared covariance.
Condition: The added contributions are independent under the displayed signal model.
Reason: Retain. This makes the consequence of normalization concrete and motivates the later eye-motion inference. Separate mean displacement, variance and measurement-error passages prevent different interpretations of a larger MSD from being merged.
Question: Why is weak correlation not enough to show a weak shared movement command?
Answer: Private variability can enlarge the denominator of correlation while leaving the shared contribution unchanged.

## 4 ch:PERSISTENCE
Definition: Adequate. The opening prepares the distinction between activity and represented value before naming state-space concepts. It does not require a new blue term in this unit.
Phrase: A disturbance can change those activities without changing the represented value.
Paraphrase: Some activity changes disappear as the circuit returns to the pattern for the same angle.
Actor: A disturbance and the circuit's restoring response.
Object: The neural activities representing an angle.
Action: Changes activity without a lasting change in the stored angle.
Condition: The disturbance lies in a direction the circuit corrects.
Reason: Retain. Together with the next sentence it makes the upcoming two-direction example necessary. The chapter's roadmap distinguishes accumulated error from a fixed irregular map.
Question: Why can stable-looking activity still be an inaccurate memory?
Answer: A different stable pattern can represent a different value, so remaining on the family does not recover the original value.

## 5 sec:FOUNDATIONS-ATTRACTOR
Definition: Adequate. State, fixed point, continuous attractor and attractor manifold are blue at their teaching definitions. Neutral is explained as absence of restoring force along the family. Dimension counts represented coordinates, not neurons. Diagram terms name the imposed disturbance and deterministic recovery separately.
Phrase: It is stable in a direction if a small disturbance in that direction decays.
Paraphrase: Stability in one direction means that a small change along it fades away.
Actor: The deterministic circuit response.
Object: A small disturbance of the state.
Action: Reduces that disturbance over time.
Condition: The direction is restoring; the direction along the memory family is neutral.
Reason: Retain. Direction-dependent stability is the premise of the worked two-cell calculation. The solid versus dashed arrow explanation tells the reader which change the model causes and which change was imposed.
Question: Why does the common activity disturbance recover while an opposite change can persist?
Answer: The model restores the rate sum to its fixed value but leaves the rate difference, and hence the represented angle, unchanged.

## 6 sec:FOUNDATIONS-DIFFUSION
Definition: Adequate. Brownian motion, root mean squared displacement and systematic drift have explicit blue definitions. The earlier diffusion coefficient and MSD are used consistently. The path, variance and RMS distinctions are explained before the plotted paths and envelope are interpreted.
Phrase: A single memory trajectory can turn back even while the spread across trials grows.
Paraphrase: One trial can move back toward its start although repeated trials become more dispersed.
Actor: One random memory path and the collection of repeated trials.
Object: Individual displacement and across-trial spread.
Action: Can change differently over time.
Condition: The independent-step model gives growing variance, not monotone motion in each trial.
Reason: Retain. Single is useful here because the point is the contrast between one path and a distribution. The bias and covariance examples add consequences needed later, rather than repeat the variance formula.
Question: Is the dashed RMS envelope a boundary that every path must stay inside?
Answer: No. It is a scale computed from mean squared displacement; individual paths can cross it.

## 7 sec:FOUNDATIONS-RANDOMNESS
Definition: Adequate. The unit reuses rate map and diffusion in their earlier senses. Fixed spatial function is described directly instead of introducing another technical term. The three-paper figure labels distinguish time and position axes.
Phrase: Revisiting a place evaluates the same expected-rate function, although the actual spikes can still vary from visit to visit.
Paraphrase: The same position can have the same expected firing rate without producing the same spikes on every visit.
Actor: The fixed spatial function and variable spike generation.
Object: Expected rate and observed spikes at a revisited place.
Action: Reuses the expectation while allowing observation variability.
Condition: The cell and environment are held fixed in the map model.
Reason: Retain. This is the essential distinction between spatial randomness and temporal noise. Removing the qualification would wrongly imply repeated identical spike trains.
Question: Can an irregular place map by itself measure the rate of memory diffusion?
Answer: No. It describes variation across physical positions, not the temporal wandering rate of an internal position estimate.

## 8 ch:MEMORY-DYNAMICS
Definition: Adequate. Existing continuous attractor and spike terms are reused. Supporting Information is expanded before SI. The PDF navigation note has an operational purpose and does not replace a scientific explanation.
Phrase: We then follow a small disturbance through the circuit's return toward a stable pattern and identify the change in stored value that remains.
Paraphrase: Follow the circuit's recovery to find the memory error left after the transient changes fade.
Actor: The circuit's return flow.
Object: A small activity disturbance.
Action: Removes stable components and leaves a coordinate shift.
Condition: The weak local perturbation calculation applies.
Reason: Retain. The inclusive we describes the reader's calculation and gives a useful dependency order: spike renewal, projection, spreading, symmetry, longer delays.
Question: Why is the return toward the attractor needed before calculating diffusion?
Answer: Raw activity changes include transient components that do not become lasting memory error.

## 9 sec:MEMORY-SPIKES
Definition: Adequate. Neural transfer function, weak fluctuation approximation and preferred angle are blue with input-output meaning, approximation scale and rate-peak meaning. Variables are tied to activation, spikes, rates and input units. A jump is described explicitly before Gaussian increments are used.
Phrase: A spike from cell $j$ raises $s_j$ by one and therefore changes the input to cell $i$ by $W_{ij}$.
Paraphrase: One spike adds one activation unit, and the connection weight converts it into input to the receiving cell.
Actor: A spike in cell j acting through its outgoing connection.
Object: Activation s_j and input g_i.
Action: Adds one activation unit and a weighted input increment.
Condition: The model's unit-jump activation convention and fixed weights.
Reason: Retain. The connector expresses the actual substitution into the input equation. This passage gives the biological meaning that the symbols alone would not provide. The later decay and transfer-function sentences complete the feedback path.
Question: What does the weak fluctuation approximation approximate?
Answer: Small aggregate fluctuations in total input, not the entire spike train of each individual neuron as a Gaussian path.

## 10 sec:MEMORY-LINEARIZATION
Definition: Adequate. Linearization and right and left zero eigenvectors are blue with equations and different physical roles. The normalization is explained. Zero in left zero eigenvector is a mathematical eigenvalue, so the negation diagnostic must not alter it.
Phrase: Its purpose is to extract the lasting memory displacement from a general perturbation.
Paraphrase: Applying the left vector gives the part of the disturbance that remains as a changed memory.
Actor: The normalized left zero eigenvector acting on the perturbation.
Object: The lasting memory coordinate change.
Action: Selects that change and discards decaying modes.
Condition: Local stable modes decay and the tangent normalization is one.
Reason: Retain. The automated suggestion to replace extract with remove reverses the intended operation. The tilted-flow example makes this operation concrete and justifies retaining the distinction from perpendicular projection.
Question: Why are the left and right zero vectors both needed?
Answer: The right vector gives the persistent state direction; the left vector measures which persistent coordinate a general disturbed state reaches.

## 11 sec:MEMORY-DIFFUSION
Definition: Adequate. Diffusion tensor is blue and immediately separated into diagonal spreading and cross-coordinate covariance. Projection, rates and Brownian increments reuse earlier meanings. The emphasized mechanism identifies spike variability and retained shift.
Phrase: changing rates can also change the tuning curves and the projection weights.
Paraphrase: A rate change can change both the noise size and how strongly that noise moves the stored value.
Actor: A change to network firing rates and associated tuning.
Object: Rate variability and projection weights.
Action: Changes multiple factors in the diffusion formula.
Condition: Networks are being compared, rather than one rate factor being varied in isolation.
Reason: Retain. The qualification prevents treating the displayed sum as a claim that high-rate cells always worsen memory. Its later controlled-comparison section supplies the promised detailed cases.
Question: What determines one cell's contribution to diffusion?
Answer: Its spike variance rate multiplied by the square of the retained coordinate change caused by an activation fluctuation.

## 12 sec:MEMORY-SYMMETRIC
Definition: Adequate. Symmetric weights are explained as equal reciprocal input weights, without implying identical firing responses. Translation symmetry has its blue definition here and is distinguished from the weight symmetry assumption. The two-cell coordinate is explicitly activation difference.
Phrase: Although the two firing rates change with the stored value, their summed spike variability is constant.
Paraphrase: One rate rises as the other falls, leaving their total Poisson variance rate unchanged.
Actor: The two mutually inhibiting cells.
Object: Their summed spike variability.
Action: Preserve the sum as the represented value changes.
Condition: The linear interior range with positive rates and fixed projection weights.
Reason: Retain. Although states a real mathematical contrast that explains constant D, not a defensive hedge. The boundary warning and coordinate convention are needed to prevent overextending the example. The source discrepancy note explains why the displayed numerator differs from the paper.
Question: Does symmetric connectivity make every state disturbance project perpendicularly?
Answer: No. Different transfer-function slopes can still make the linear dynamics nonsymmetric.

## 13 ch:MEMORY-LONG-DELAYS
Definition: Adequate. Boundaries, wraparound and systematic drift are introduced in ordinary terms using earlier diffusion teaching. Uppercase LONG in the anchor is hidden identification text, not an unexplained reader acronym.
Phrase: The value may approach a boundary, wrap around an angular range, or reach a region where the spreading rate differs.
Paraphrase: Long waits can expose domain limits or spatial changes in the noise rate.
Actor: The wandering stored value.
Object: Its permitted coordinate range and local diffusion rate.
Action: Moves into conditions where a single local spreading rate is insufficient.
Condition: Observation extends beyond the initial local region.
Reason: Retain. These are three genuinely distinct reasons the next chapter is needed. A three-item diagnostic does not justify deleting a necessary case.
Question: Why does a local value of D not determine all long-delay errors?
Answer: Boundaries, coordinate wrapping, changes in D and mean drift can alter the distribution after a long wait.

## 14 sec:MEMORY-LONG-TIME
Definition: Adequate. Itô convention is blue before state-dependent noise is interpreted. Fokker Planck equation and Dirac delta are blue beside their equations, and the delta is distinguished from the earlier zero-or-one symbol. The excitation example explicitly says its coordinate is not an angle.
Phrase: It reflects the bounded way angular error is reported.
Paraphrase: Error measured within one turn cannot spread without limit even though local diffusion continues.
Actor: The wrapped angular error convention.
Object: Long-time mean squared angular error.
Action: Makes the reported error approach the uniform-circle value.
Condition: Constant diffusion on a circle and errors reported in the stated interval.
Reason: Retain. This sentence identifies the cause of flattening and prevents interpreting the plot as a change in local spike noise. The line comparison, state-dependent example and source-factor note each supply a distinct limit or calculation.
Question: Does the plateau in wrapped error mean that the circuit stopped receiving noise?
Answer: No. The same local diffusion can continue while a bounded angular error distribution approaches uniformity.

## 15 sec:MEMORY-DRIFT-SCOPE
Definition: Adequate. Systematic drift is recalled in plain text with its earlier meaning. Stratonovich convention has a blue first definition, contrasted with Itô using the conversion term. Correlated fluctuations are described through their covariance matrix rather than an unexplained new label.
Phrase: They cannot remove the random increments by subtracting a known average.
Paraphrase: Correcting a predictable mean does not reveal or cancel each random change.
Actor: Changes to weights or biases that cancel mean drift.
Object: The random increments of the stored value.
Action: Leave the stochastic part present.
Condition: Mean drift compensation without knowledge of each noise realization.
Reason: Retain. This distinction is required to understand why a drift correction does not eliminate diffusion. The phrase in addition introduces the second physical source of mean motion; it is not empty emphasis.
Question: Does zero drift in the written noise-free model settle the exact noisy mean motion?
Answer: No. State-dependent noise and curved dynamics can add mean motion, and the microscopic process matters.

## 16 sec:MEMORY-FIGURES
Definition: Adequate. Activity bump is blue and describes a peak across preferred angles. Sigmoidal is explained as S-shaped. Observer means an estimator with finite spikes; sees is ordinary shorthand for the data it receives and does not attribute cognition to software. Figure 1B is a panel label, not one byte.
Phrase: The dashed bound is a lower limit for the sigmoidal case, not a separate fitted trajectory.
Paraphrase: The dashed curve shows the lowest allowed diffusion error for that case, rather than another simulated memory path.
Actor: The dashed curve in the original figure.
Object: The lower information bound for the sigmoidal network.
Action: Provides a comparison limit.
Condition: The figure's stated network and information calculation.
Reason: Retain. The contrast tells the reader how to read a particular curve and avoids a plausible misreading. Fold labels distinguish original paper figures from guide constructions; panel explanations have real interpretive work.
Question: What distinct uncertainties does Figure 1 separate?
Answer: Movement of the stored coordinate during memory and uncertainty in estimating its current location from a finite spike sample.

## 17 ch:MEMORY-INFORMATION
Definition: Adequate. The opening explains information as distinguishability of nearby values before introducing its formal measure. Previously taught coordinate, rate, diffusion and synaptic time constant are recalled without repeated definition color.
Phrase: More information can permit better stability without ensuring that a particular circuit achieves it.
Paraphrase: Better spike information lowers a possible noise limit but does not force the circuit to attain that limit.
Actor: Information available in the spike distribution.
Object: The lower limit on diffusion for a specified circuit.
Action: Permits, but does not guarantee, a smaller diffusion coefficient.
Condition: The circuit's retained-noise response must also satisfy the equality condition.
Reason: Retain. Particular distinguishes the actual network from the bound. Deleting the qualification would overstate what the next derivation proves.
Question: Does a lower information bound guarantee a lower actual diffusion coefficient?
Answer: No. The bound limits what is possible, and the network can remain strictly above it.

## 18 sec:MEMORY-FI
Definition: Adequate. Likelihood, score, Fisher information, internal Fisher information rate, unbiased, Cramér Rao bound and prior distribution are blue with meanings before their reasoning-dependent use. The rate-versus-duration distinction is explicit. FI in the anchor is hidden, not a reader heading acronym.
Phrase: High rates with zero slope do not distinguish neighboring values, so they contribute no local information.
Paraphrase: A cell can fire often without helping tell nearby stored values apart if its rate does not change between them.
Actor: A cell with locally flat tuning.
Object: Distinguishability of neighboring values.
Action: Adds no local parameter information despite its high rate.
Condition: The Poisson information formula uses the local squared tuning slope.
Reason: Retain. This explains the numerator rather than equating activity with information. Currently refers to the stimulus at the observation time, not a date-sensitive product claim. Guarantee is negated to state the bound's limit.
Question: Why does extra baseline firing reduce the information in the illustrated pair?
Answer: It increases Poisson count variance without changing the rate derivative that separates nearby values.

## 19 sec:MEMORY-BOUND
Definition: Adequate. Equality and lower bound are kept distinct, including the matching-noise condition. The matrix ordering is explicitly defined by every quadratic form, and invertibility is stated before the inverse. Scientific quantity names are not decorative labels.
Phrase: Continuous variation of the represented value alone does not supply them.
Paraphrase: Merely having a continuous family does not impose the extra conditions needed to force an exponential transfer function.
Actor: The continuous-family assumption.
Object: Restrictions linking participating input values across cells and states.
Action: Does not establish those additional restrictions.
Condition: Testing the converse of the sufficient exponential equality condition.
Reason: Retain. The counterexample and this limit are necessary to prevent repeating the source's overstrong converse. To conclude is a literal inference condition here, not a generic conclusion marker. The information-diffusion name denotes the paired quantities of the inequality.
Question: What does the linear equality example show?
Answer: An exponential rule is sufficient in the stated setting but is not necessary without further restrictions.

## 20 sec:MEMORY-COMPARISONS
Definition: Adequate. Held fixed has its normal comparison meaning; it is not figurative possession. Tuning width and resource constraints are made concrete through a, rho, f and w. The isotropic special case is explained as every direction being equivalent rather than assumed from a label.
Phrase: The inequality compares diffusion and information for the same network.
Paraphrase: The bound relates properties of one circuit, so comparisons between circuits need specified controls.
Actor: The information-diffusion inequality and the proposed parameter comparison.
Object: D, J and the quantities held unchanged.
Action: Separates a within-network bound from changes between networks.
Condition: Neuron count, rate, time constant or tuning width is varied.
Reason: Retain. Each controlled example demonstrates a different hidden change. At the same time describes simultaneous parameter variation. The alternative fixed-total-rate calculation is needed because it reverses the width conclusion's scope.
Question: Why can slower synapses give different powers of tau in different comparisons?
Answer: Holding firing-rate curves fixed differs from holding activation curves and dimensionless weights fixed, which changes rates as tau changes.

## 21 ch:MEMORY-READOUT
Definition: Adequate. Storage delay, recall cue and observation interval are separated using ordinary words before notation. The repeated J link recalls information rate. The emphasized question gives a genuine estimation task.
Phrase: Later spikes can help estimate the value present at that cue, but they cannot reveal the particular random displacements that occurred before it.
Paraphrase: Future observations can estimate the cue state, but cannot reconstruct the earlier noise history in this model.
Actor: Later observed spikes.
Object: The state at the recall cue and the earlier storage error.
Action: Improve cue-state estimation without undoing prior random changes.
Condition: Future noise and observations have the stipulated independence from storage history.
Reason: Retain. Particular points to the unknown realized increments, not a vague modifier. This establishes why storage error and readout error must be treated separately.
Question: Which value is estimated from the later spikes?
Answer: The value at the recall cue, which already differs from the original value by accumulated storage error.

## 22 sec:MEMORY-READOUT-SETUP
Definition: Adequate. Translation invariance is blue with the precise readout-error meaning. The variables Theta, x, x-hat, s, e, T and L are tied to the timeline. Gaussian observations are explicitly an approximation summarizing spike information, not another directly measured coordinate.
Phrase: Conditional on that history, the readout error then has mean zero.
Paraphrase: Once the storage history is fixed, the readout does not systematically overestimate or underestimate its cue state.
Actor: The locally unbiased readout estimator.
Object: Its error relative to x.
Action: Has zero conditional mean.
Condition: Local unbiasedness at every x and future-noise independence from storage history.
Reason: Retain. The conditioning is necessary for the zero-covariance step. Removing it would turn the variance sum into an unsupported general claim. The timeline caption repeats these assumptions because the image must explain what its two errors mean.
Question: Why can storage and readout variances be added here?
Answer: The conditional zero-mean readout error gives zero cross covariance with the storage error; translation invariance gives one readout variance for every cue state.

## 23 sec:MEMORY-NAIVE
Definition: Adequate. Naive is defined by the actual operation, equal weighting as if the state were stationary. Brownian covariance is recalled from the persistence chapter. No new decorative term emphasis is needed.
Phrase: The two contributions have opposite dependence on $L$.
Paraphrase: Longer observation reduces observation noise but increases error from averaging a moving state.
Actor: Observation-noise and state-motion terms in the variance.
Object: Readout error as observation duration changes.
Action: One falls while the other grows.
Condition: Equal weighting in the local Gaussian model.
Reason: Retain. The count of two refers directly to the derived terms and motivates differentiation for the best duration. It is not an empty numbered forecast.
Question: Why does waiting longer eventually hurt equal weighting?
Answer: Late observations concern a state farther from the cue state, and their motion contribution eventually exceeds the reduction of independent observation noise.

## 24 sec:MEMORY-IDEAL
Definition: Adequate. Precision is blue as reciprocal scalar Gaussian variance. Hyperbolic tangent, its inverse and hyperbolic cotangent are blue with explicit formulas. Ideal means the stated inference rule, not an established neural implementation. Saturation is explained as gradual approach to a limit.
Phrase: The term $2DP^2$ reduces that gain because later observations are separated from the cue state by diffusion.
Paraphrase: Uncertainty from motion weakens the information that later observations provide about the earlier state.
Actor: Diffusive state transitions in the backward information calculation.
Object: Precision about the cue state.
Action: Subtract from the gain supplied by observation information.
Condition: Independent Gaussian increments and the scalar precision recursion.
Reason: Retain. The term-by-term interpretation connects the differential equation to the inference problem. Best refers to the calculated minimum, not an unsupported superiority claim. The characteristic-time qualification prevents reading tau as an abrupt cutoff.
Question: Does observation after tau have exactly zero benefit?
Answer: No. The ideal variance approaches its asymptotic limit continuously; tau is a characteristic time in the equality case with full spike access.

## 25 sec:MEMORY-PARTIAL
Definition: Adequate. The spike fraction alpha is tied to unbiased random thinning and then distinguished from an arbitrary selected subpopulation. Earlier information and diffusion meanings are preserved. No new term requires blue emphasis.
Phrase: That reduces its information without reducing the fluctuations that already move the full memory network.
Paraphrase: The observer receives fewer useful spikes while the full circuit continues to experience the same internal noise.
Actor: Restricted access by a downstream observer.
Object: Observed information rate, contrasted with network diffusion.
Action: Reduces the former while leaving D unchanged.
Condition: The model changes access to spikes, not the full network dynamics.
Reason: Retain. This is the decisive causal distinction behind the square-root increase in duration and error. Some of the specifies a subset of the network's spikes and is already concise natural language.
Question: When does a fraction of spikes equal the same fraction of information?
Answer: Under unbiased random thinning, or when alpha is defined as the actual information fraction; arbitrary selected cells can differ.

## 26 sec:MEMORY-EXTENSIONS
Definition: Adequate. The two time constants have explicit roles in synaptic activation and rate adjustment. The Gaussian noise strength q is defined by its variance convention, and the matched likelihood is supplied. Left zero vector reuses the earlier definition.
Phrase: This result belongs to the two stage model and noise placement just described.
Paraphrase: Adding the two time constants is justified for these coupled equations with this source of noise.
Actor: The derived two-stage system.
Object: The effective time factor in the diffusion-information bound.
Action: Produces the sum of the two specified time constants.
Condition: Noise enters the activation block as modeled, with the stated dynamics and symmetry.
Reason: Retain. This limits the result before a reader might add arbitrary biological time scales. The Gaussian extension teaches why changing the noise law changes the equality condition, so it is not redundant with the Poisson derivation.
Question: Can any collection of neural time constants simply be added in this bound?
Answer: No. The sum follows from this two-stage model and where noise enters its equations.

## 27 sec:MEMORY-FIG3-AND-CAUTION
Definition: Adequate. Figure axes distinguish readout variance from total storage-plus-readout error. Saturated is tied to equality in the earlier bound. Integrating a signal and leak are explained through mean and variance behavior rather than unexplained labels. Original-figure fold titles are specific.
Phrase: Substituting an upper bound for this term cannot establish the printed universal lower bound on total error.
Paraphrase: An upper estimate of the readout contribution cannot prove that every total error is at least that large.
Actor: The proposed inequality substitution.
Object: The ideal asymptotic readout contribution and total variance.
Action: Fails to justify the claimed lower-bound direction.
Condition: The information-diffusion inequality need not be saturated.
Reason: Retain. This states the exact logical fault before the numerical strict case. Removing it would leave the reader with two inconsistent error formulas and no explanation. The final leak distinction preserves the difference between mean decay and growing uncertainty.
Question: Why is the paper's universal total-error bound qualified?
Answer: Its substituted cellular-time readout term is an upper bound unless equality holds, so it cannot supply that universal lower bound.

## 28 part:MECHANISMS::part-opening
Definition: Adequate. The opening says nerve cells, firing patterns, remembered angle and random spike timing in ordinary words. Continuous attractor in the Part title is a topic label whose first full teaching definition occurs in the persistence chapter. No formal reasoning depends on an unexplained title term here.
Phrase: Random spike timing can change that angle even while the circuit sustains its activity.
Paraphrase: Ongoing firing does not ensure that the represented angle stays correct.
Actor: Random spike timing within the model circuit.
Object: The angle represented by its population pattern.
Action: Changes the angle while activity persists.
Condition: The continuous-attractor model described by the Part.
Reason: Retain. This is the central causal problem connecting the six chapters. The chapter-number roadmap states what the reader gains at each step and does not make the Part opening a compressed abstract full of unexplained notation.
Question: What connects the six chapters in this Part?
Answer: They explain the representation, derive how noise changes it, then connect its stability and readout accuracy to spike information.

## Diagnostic and scope notes

All 380 alert records and all 176 control regions were read in current chapter context. Repeated Google and Microsoft reports on the same phrase are retained as separate diagnostic records with shared passage reasoning in the JSON. Exact rule files were read by rule message and applicable patterns, including the units, quotes, punctuation, negative-object and numbered-lead rules. This was not inferred from zero Vale errors.

The definition audit found 59 distinct blue terms across the reading guide and these six chapters, all with matching glossary entries after normalizing heading capitalization and glossary colons. Each main teaching definition occurs once in this reading scope. Sidecar copies of the same section are not counted as new teaching occurrences. This is a text and markup judgment, not a new rendering check of blue color.

Citation years and journal issue numbers explain most parenthesis alerts. Citation page, equation and panel ranges explain most dash controls. Semicolons separate source locations that already contain commas, preserving the relation between a claim and its main-paper and supplement sources. Their use is bounded to citations here. No prose em dash was accepted. The information-diffusion paired quantity name has an en dash in one source passage; its technical relationship is unambiguous and does not act as an interrupting sentence dash.

Passive clauses put the scientific quantity under discussion first. In the reviewed examples their actor is specified nearby, is the estimator/measurement convention, or is irrelevant to the mathematical statement. Inclusive we guides an actual calculation. Formal connectors mark a stated inference, comparison or worked example. The retained contrasts prevent concrete confusions: rate versus clock, cell index versus physical position, expected map versus observed spikes, left projection versus perpendicular projection, conditional increments versus whole trains, and information bounds versus actual performance. They are not retained merely because the checker was disabled.

Scope history: the coordinator initially described section summaries as reader-facing standalone navigation text. A bounded reread found the three incomplete metadata excerpts below and initially classified them as required repairs under that description. The coordinator then corrected that renderer claim. Independent inspection at 13:43 confirmed that the active Quarto renderer uses chapter.content_blocks and section titles/IDs, not section.summary. The only runtime section.summary references found are semantic_review.py:120,139 and release_audit.py:330. guide-project.yaml:38-62 enables Quarto and disables Word and LaTeX. Each body lead-in is immediately followed by its equation or list at 01-foundations.md:53-57, 01b-persistence.md:88-90 and 03b-memory-readout.md:332-334. Therefore these are conditional internal-metadata findings, not required current reader-text repairs. They are preserved here rather than erased. No rendered layout judgment is made.

- M-LANG-01, content/chapters/01-foundations.yaml:23, sec:FOUNDATIONS-POISSON. The summary ends with "obeys" without supplying the distribution or a complete result. If rendered alone, needed meaning: a complete statement of the Poisson count model or its count-variability result. Conditional internal-metadata note, not a current reader defect.
- M-LANG-02, content/chapters/01b-persistence.yaml:23, sec:FOUNDATIONS-DIFFUSION. The summary ends with "The calculation assumes:" without the assumptions. If rendered alone, needed meaning: a complete statement connecting repeated independent increments, their mean and variance conditions, and linear variance growth. Conditional internal-metadata note, not a current reader defect.
- M-LANG-03, content/chapters/03b-memory-readout.yaml:43, sec:MEMORY-FIG3-AND-CAUTION. The summary ends with "The plotted features are:" without the list. If rendered alone, needed meaning: a complete account of the plotted readout behavior, or removal of that dangling promise if the preceding summary is sufficient. Conditional internal-metadata note, not a current reader defect.

Stage 1 format clarification: system setup verdict retain meant adequate. Expert-objection disposition retain meant the tested objection does not apply, for the reasons recorded in Stage 1. The Stage 1 report remains unchanged.

Stage 2 judgment: pass for current reader-facing necessity, terminology and definitions. No required current reader-text defect remains. The three conditional metadata findings above are not cleared by a repair; their classification changed after checking the actual renderer. Body claims and reviewed diagnostic passages have a teaching contribution in their connected context: prerequisite, mechanism, derivation, example, necessary qualification, source comparison, or figure interpretation. Definition and emphasis judgments are adequate. This does not pre-judge Stage 3 paragraph flow or later artwork and publication acceptance.


Completed: 2026-10-29T13:47:04.9869733+02:00. Wall time 843.523 seconds. Since previous checkpoint 212.545 seconds. Wall since preparation 2540.944 seconds. Awake execution unverified. No clock change observed. Token stats unavailable. Final status: pass for Stage 2 current reader text; Stage 3 remains pending.
