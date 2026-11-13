# Place group: Stage 2 necessity and language

Request: `final-place-language-20261029-02`. Reviewer: `/root/accept_place`, assigned GPT-6 Astra, high reasoning. Context: reviewer_continuation.

Input hash: `3fa06682def9f93bbafd2b39bfe5f3a5641febda3bbd57c2f9caf86c8b465283`.
Contract hash: `593934f3af51c49175417df3e4263df20a0835575d099bad4f0070163b4a17dc`.

No required current reader-text repair was found. Four incomplete-if-standalone synthesis summary values are preserved as conditional internal-metadata notes. Independent inspection of the pinned Quarto renderer confirms that it uses the body paragraphs and their lists, not these summaries as standalone reader text. The review covers all 22 assigned units. The JSON records 511 advisory alert decisions across 160 source lines, 139 bounded control decisions, and 23 newly marked terms with matching glossary entries. These counts describe coverage, not an automatic quality result.

## Unit judgments

### content/chapters/glossary.md::ch:GLOSSARY

Every glossary item uses the prescribed blue definition span. The 23 terms first marked in the reviewed teaching chapters have matching glossary spellings. Definitions distinguish a critical point from the extra nondegeneracy condition, a stationary process from the spatial Stationarity entry, and Rayleigh from Weibull. This is lookup after main teaching, as p3 says.

Reviewed phrase: The positions where a function exceeds a specified level.

Plain meaning: An excursion set contains every position whose function value is higher than the cutoff.

Retain: This is the shortest useful lookup meaning. The exact term excursion set is needed to locate the chapter calculation; replacing it by a loose synonym would break lookup.

Necessity: Short entries let readers recover meanings without replaying derivations. Repeating the blue term here is the explicit glossary exception, not a second chapter introduction. The warnings about sample means, conditional rates, and regularity preserve meaning rather than inflate the entries.

References: content/chapters/glossary.md::ch:GLOSSARY::p3, content/chapters/glossary.md::ch:GLOSSARY::p20, content/chapters/glossary.md::ch:GLOSSARY::p41, content/chapters/glossary.md::ch:GLOSSARY::p55, content/chapters/glossary.md::ch:GLOSSARY::p74, content/chapters/glossary.md::ch:GLOSSARY::p87, content/chapters/glossary.md::ch:GLOSSARY::p99, content/chapters/glossary.md::ch:GLOSSARY::p100

### content/chapters/references.md::ch:REFERENCES

The bibliography introduces no new technical definition. Italics identify publication titles, and author names and titles retain source spelling. Definition blue is not appropriate for titles or identifiers.

Reviewed phrase: The paper's supporting information shares its main article entry.

Plain meaning: The article and its supplement are found under one bibliography item.

Retain: This tells the reader where to find supporting equations. Removing it could make an absent separate supplement entry look like a missing source.

Necessity: Names, dates, article titles, venues, and identifiers enable retrieval. Author-separating semicolons and page ranges are bibliographic conventions, not inflated explanatory prose. The title containing very large is a source title, not the guide praising a result.

References: content/chapters/references.md::ch:REFERENCES::p3, content/chapters/references.md::ch:REFERENCES::p6, content/chapters/references.md::ch:REFERENCES::p20, content/chapters/references.md::ch:REFERENCES::p24, content/chapters/references.md::ch:REFERENCES::p44

### content/chapters/05-place-fields.md::ch:PLACE-FIELDS

Place cell, place field, hippocampus, synapse and firing rate are taught earlier. Upcrossing is newly marked at line15 and immediately means an upward passage through the threshold. It is taught before the counting calculation.

Reviewed phrase: The recordings estimate firing rates rather than measuring this input directly.

Plain meaning: The measured maps describe firing; the summed synaptic input is a model interpretation.

Retain: The contrast prevents a concrete measurement error. It is needed where the modeled input is first related to the experiment.

Necessity: Tunnel, floor, and room examples explain why dimension changes. The synaptic interpretation connects the model to cells. The fixed-map limit prevents readers importing the earlier time-noise model. Removing those distinctions would leave the later fit claims ambiguous.

References: content/chapters/05-place-fields.md::ch:PLACE-FIELDS::p7, content/chapters/05-place-fields.md::ch:PLACE-FIELDS::p9, content/chapters/05-place-fields.md::ch:PLACE-FIELDS::p15, content/chapters/05-place-fields.md::ch:PLACE-FIELDS::p17

### content/chapters/05-place-fields.md::sec:PLACE-GP

Gaussian process is blue at23 with its map role;28 supplies the finite jointly Gaussian definition, and37 defines jointly Gaussian vector before the zero-covariance implication is used. Stationarity, Isotropy and Smoothness have separate marked meanings at47/50/52. Excursion set at79 is completed by its displayed set and connected-field explanation. Each has one marked teaching occurrence and a matching glossary entry.

Reviewed phrase: A fitted threshold describes the balance of input and response.

Plain meaning: The fitted cutoff combines properties of incoming activity and the cell's response.

Retain: Balance is made concrete by the preceding q, input-amplitude, and gain cases. The sentence prevents assigning a single biological cause to a statistical parameter.

Necessity: The height histogram counterexample motivates covariance before its formula. The smoothness counterexample is needed because Gaussian values alone do not permit derivatives. Repeated fixed-map wording at17/23/117 has different local uses: overall scope, the draw/evaluate operation, and interpreting a plotted horizontal axis. It is not three unexplained slogans.

References: content/chapters/05-place-fields.md::sec:PLACE-GP::p21, content/chapters/05-place-fields.md::sec:PLACE-GP::p23, content/chapters/05-place-fields.md::sec:PLACE-GP::p27, content/chapters/05-place-fields.md::sec:PLACE-GP::p36, content/chapters/05-place-fields.md::sec:PLACE-GP::p47, content/chapters/05-place-fields.md::sec:PLACE-GP::p50, content/chapters/05-place-fields.md::sec:PLACE-GP::p52, content/chapters/05-place-fields.md::sec:PLACE-GP::p68, content/chapters/05-place-fields.md::sec:PLACE-GP::p79, content/chapters/05-place-fields.md::sec:PLACE-GP::p85, content/chapters/05-place-fields.md::sec:PLACE-GP::p105

### content/chapters/05-place-fields.md::sec:PLACE-KAC-RICE

Upcrossing was taught at15. Kac–Rice formula is blue at132 only after the narrow-band counting operation is explained. The following integral gives its precise role. Phi and Q are defined at185 where the finite endpoint correction needs them. The exact mathematical name and its en dash should remain.

Reviewed phrase: Multiplication by $v$ compensates for the shorter spatial window of a steep crossing.

Plain meaning: A faster crossing spends less distance in the narrow height band; weighting by its slope restores one count.

Retain: Compensates names the cancellation just calculated. Shortening this to a label such as slope weighting would hide why the integral counts crossings.

Necessity: The narrow-band example, Gaussian independence argument and endpoint term each supply a different necessary step. The last boundary qualification distinguishes retaining intersecting components from removing incomplete fields.

References: content/chapters/05-place-fields.md::sec:PLACE-KAC-RICE::p123, content/chapters/05-place-fields.md::sec:PLACE-KAC-RICE::p131, content/chapters/05-place-fields.md::sec:PLACE-KAC-RICE::p139, content/chapters/05-place-fields.md::sec:PLACE-KAC-RICE::p151, content/chapters/05-place-fields.md::sec:PLACE-KAC-RICE::p157, content/chapters/05-place-fields.md::sec:PLACE-KAC-RICE::p173, content/chapters/05-place-fields.md::sec:PLACE-KAC-RICE::p177, content/chapters/05-place-fields.md::sec:PLACE-KAC-RICE::p185

### content/chapters/05-place-fields.md::sec:PLACE-INFERENCE

Field and gap are already defined by connected active and inactive intervals. The normal tail is defined at185. Poisson process was taught in foundations;232 specifies its new spatial use and the additional rare-event and distance-dependence limits. No duplicate blue definition is needed.

Reviewed phrase: Field lengths help separate those possibilities.

Plain meaning: Lengths add information that distinguishes a higher threshold from a more slowly varying map.

Retain: Those possibilities has the explicit high-threshold and slow-map antecedents in the preceding sentence. This short bridge supplies the reason for the inversion.

Necessity: The ratio caveat limits what the displayed means assert. The example shows inverse inference and finite boundaries. Silent-cell conditioning answers a separate sampling problem; it is not another version of the endpoint correction.

References: content/chapters/05-place-fields.md::sec:PLACE-INFERENCE::p189, content/chapters/05-place-fields.md::sec:PLACE-INFERENCE::p191, content/chapters/05-place-fields.md::sec:PLACE-INFERENCE::p204, content/chapters/05-place-fields.md::sec:PLACE-INFERENCE::p206, content/chapters/05-place-fields.md::sec:PLACE-INFERENCE::p223, content/chapters/05-place-fields.md::sec:PLACE-INFERENCE::p229, content/chapters/05-place-fields.md::sec:PLACE-INFERENCE::p237, content/chapters/05-place-fields.md::sec:PLACE-INFERENCE::p246

### content/chapters/05b-place-sizes.md::ch:PLACE-SIZES

No new technical name is needed in the opening. It uses ordinary peak, radius, length, area and volume before formal Hessian or distribution terms appear. The notation reminder explicitly distinguishes d from the map parameters.

Reviewed phrase: Its height above the threshold sets a radius

Plain meaning: The amount by which the peak exceeds the cutoff determines how far the nearby active region extends.

Retain: The approximation is announced in the preceding sentence and the high-threshold condition is repeated at the exact-versus-limiting distinction. Sets does not imply a general exact rule for arbitrary fields.

Necessity: The opening moves from a mean to the missing size distribution. The short notation reminder avoids making readers infer whether size means length, area or volume; the next derivation depends on that distinction.

References: content/chapters/05b-place-sizes.md::ch:PLACE-SIZES::p3, content/chapters/05b-place-sizes.md::ch:PLACE-SIZES::p9, content/chapters/05b-place-sizes.md::ch:PLACE-SIZES::p11

### content/chapters/05b-place-sizes.md::sec:PLACE-RARE-PEAKS

Hessian is marked with its matrix-of-second-derivatives meaning and principal-curvature role at28. Rayleigh distribution is marked at90 as a scaled square root of an exponential variable; the subsequent density derives the same object. Exponential variables and the Gaussian conditioning calculation are explained before the transformation is used.

Reviewed phrase: The remaining question is how $\epsilon$ is distributed when we select one high field at a time.

Plain meaning: We need the peak excess distribution for fields counted equally, not for arbitrary spatial points.

Retain: The sampling phrase is essential. Deleting it would make the Gaussian value tail at random positions seem interchangeable with the field-weighted excess law.

Necessity: The Hessian and conditioning explanation establish curvature, then the survival ratio establishes excess height. The finite-threshold exponent examples stop the asymptotic squared-width prediction from being described as an observed exact exponent.

References: content/chapters/05b-place-sizes.md::sec:PLACE-RARE-PEAKS::p15, content/chapters/05b-place-sizes.md::sec:PLACE-RARE-PEAKS::p28, content/chapters/05b-place-sizes.md::sec:PLACE-RARE-PEAKS::p35, content/chapters/05b-place-sizes.md::sec:PLACE-RARE-PEAKS::p57, content/chapters/05b-place-sizes.md::sec:PLACE-RARE-PEAKS::p73, content/chapters/05b-place-sizes.md::sec:PLACE-RARE-PEAKS::p90, content/chapters/05b-place-sizes.md::sec:PLACE-RARE-PEAKS::p92, content/chapters/05b-place-sizes.md::sec:PLACE-RARE-PEAKS::p94, content/chapters/05b-place-sizes.md::sec:PLACE-RARE-PEAKS::p96

### content/chapters/05b-place-sizes.md::sec:PLACE-SIZE-LAW

Gamma function is blue and defined by its integral and factorial relation at115 before ball volume and moments rely on it. Weibull distribution is blue with its survival probability at185. Rayleigh is reused plainly. Units and the distinction between dimensionless w and transformed U are explicit.

Reviewed phrase: Removing units does not erase the difference between length, area, and volume distributions.

Plain meaning: Scaling each size to a unitless value leaves different density shapes; the nonlinear U transformation is another operation.

Retain: This negation addresses the adjacent density-collapse figure, where a reader could otherwise mistake unit normalization for the full transformation.

Necessity: The moment integral checks normalization and scale. The q=1.1 versus q=5 numerical comparison makes the approximation error usable. The printed-source corrections belong here because otherwise the reader obtains conflicting constants from the cited supplement.

References: content/chapters/05b-place-sizes.md::sec:PLACE-SIZE-LAW::p113, content/chapters/05b-place-sizes.md::sec:PLACE-SIZE-LAW::p115, content/chapters/05b-place-sizes.md::sec:PLACE-SIZE-LAW::p145, content/chapters/05b-place-sizes.md::sec:PLACE-SIZE-LAW::p156, content/chapters/05b-place-sizes.md::sec:PLACE-SIZE-LAW::p166, content/chapters/05b-place-sizes.md::sec:PLACE-SIZE-LAW::p168, content/chapters/05b-place-sizes.md::sec:PLACE-SIZE-LAW::p176, content/chapters/05b-place-sizes.md::sec:PLACE-SIZE-LAW::p184, content/chapters/05b-place-sizes.md::sec:PLACE-SIZE-LAW::p188, content/chapters/05b-place-sizes.md::sec:PLACE-SIZE-LAW::p190, content/chapters/05b-place-sizes.md::sec:PLACE-SIZE-LAW::p198, content/chapters/05b-place-sizes.md::sec:PLACE-SIZE-LAW::p204

### content/chapters/05b-place-sizes.md::sec:PLACE-SLICES

Slice is established as restriction to a line or plane at213, not as selecting a field centre. Joint Gaussianity, covariance, isotropy and connected components have prior teaching. Panel letters are source labels, so I is not a first-person pronoun. Centre is ordinary British spelling and need not be changed.

Reviewed phrase: Large fields are more likely to be hit by a spatially sampled line

Plain meaning: A line chosen through space encounters bigger fields more often.

Retain: The sampling bias is the necessary reason the original radius distribution cannot simply be reused for line lengths.

Necessity: The restriction proof and the sampling warning answer different questions. The spherical alternative demonstrates that matching volumes does not ensure the right spatial structure. Figure-panel guidance lets readers locate the actual slice comparisons.

References: content/chapters/05b-place-sizes.md::sec:PLACE-SLICES::p210, content/chapters/05b-place-sizes.md::sec:PLACE-SLICES::p212, content/chapters/05b-place-sizes.md::sec:PLACE-SLICES::p216, content/chapters/05b-place-sizes.md::sec:PLACE-SLICES::p222, content/chapters/05b-place-sizes.md::sec:PLACE-SLICES::p227, content/chapters/05b-place-sizes.md::sec:PLACE-SLICES::p230, content/chapters/05b-place-sizes.md::sec:PLACE-SLICES::p242

### content/chapters/05b-place-sizes.md::sec:PLACE-SLOPES

Derivative and boundary are already taught. Rayleigh keeps its earlier exact term and is not marked again. The text explicitly distinguishes a derivative at an arbitrary spatial position from a slope selected at a crossing.

Reviewed phrase: A field boundary is a selected position, however, and selecting it changes the derivative distribution.

Plain meaning: The distribution at crossings differs from the distribution at a randomly chosen position.

Retain: Selected is statistical selection, not a vague choice by an observer. The following crossing integral supplies its operation.

Necessity: The exact q-independent slope law needs its separate derivation to avoid inheriting the high-threshold restriction. The width calculation is a short independent check on the missing square-root-of-two factor, not an unnecessary second full derivation.

References: content/chapters/05b-place-sizes.md::sec:PLACE-SLOPES::p257, content/chapters/05b-place-sizes.md::sec:PLACE-SLOPES::p259, content/chapters/05b-place-sizes.md::sec:PLACE-SLOPES::p267, content/chapters/05b-place-sizes.md::sec:PLACE-SLOPES::p273, content/chapters/05b-place-sizes.md::sec:PLACE-SLOPES::p279, content/chapters/05b-place-sizes.md::sec:PLACE-SLOPES::p283

### content/chapters/05c-place-tests.md::ch:PLACE-TESTS

The opening uses rings, tunnels, regions and holes before naming Euler characteristic. q, sigma and a are restated as a short notation reminder, and d is separated from the earlier diffusion coefficient D.

Reviewed phrase: One may contain rings or tunnels that the other lacks.

Plain meaning: Equal field-size statistics can conceal different holes in the active map.

Retain: The concrete shapes establish the question before the technical topology name. They make the missing information visible without extra terminology.

Necessity: The question motivates tests beyond size. The short boundary warning matters for the forthcoming exact formula, while the circuit question prepares the distinction between statistical success and unique biological cause.

References: content/chapters/05c-place-tests.md::ch:PLACE-TESTS::p3, content/chapters/05c-place-tests.md::ch:PLACE-TESTS::p7, content/chapters/05c-place-tests.md::ch:PLACE-TESTS::p9

### content/chapters/05c-place-tests.md::sec:PLACE-TOPOLOGY

Euler characteristic is marked before the 1D/2D/3D counting definitions; Betti numbers follows concrete counts. Critical point and Morse theory are marked with the zero-gradient condition and signed-count theorem role. The stated Hessian restriction belongs to the theorem conditions, not the general meaning of critical point. Glossary wording preserves that distinction.

Reviewed phrase: These are signed densities per length, area, and volume, not three formulas for positive field counts.

Plain meaning: The quantities count components and holes with signs per spatial size; they need not be nonnegative.

Retain: Signed is exact mathematical vocabulary needed before the negative example. Replacing it by a softer word would conceal the reason negative values are allowed.

Necessity: Disk/ring and ball/tunnel/cavity examples teach the alternating count. The boundary derivation prevents applying an infinite-volume expression to a small box. The later negative expected-chi example tests the formula, whereas35 interprets the constructed 2D picture; retaining both supports two different reader tasks.

References: content/chapters/05c-place-tests.md::sec:PLACE-TOPOLOGY::p17, content/chapters/05c-place-tests.md::sec:PLACE-TOPOLOGY::p19, content/chapters/05c-place-tests.md::sec:PLACE-TOPOLOGY::p21, content/chapters/05c-place-tests.md::sec:PLACE-TOPOLOGY::p23, content/chapters/05c-place-tests.md::sec:PLACE-TOPOLOGY::p25, content/chapters/05c-place-tests.md::sec:PLACE-TOPOLOGY::p35, content/chapters/05c-place-tests.md::sec:PLACE-TOPOLOGY::p37, content/chapters/05c-place-tests.md::sec:PLACE-TOPOLOGY::p39, content/chapters/05c-place-tests.md::sec:PLACE-TOPOLOGY::p59, content/chapters/05c-place-tests.md::sec:PLACE-TOPOLOGY::p99, content/chapters/05c-place-tests.md::sec:PLACE-TOPOLOGY::p114, content/chapters/05c-place-tests.md::sec:PLACE-TOPOLOGY::p123, content/chapters/05c-place-tests.md::sec:PLACE-TOPOLOGY::p139

### content/chapters/05c-place-tests.md::sec:PLACE-DATA

Skew, excess kurtosis and lognormal distribution are marked with formulas or a transform meaning at166 before interpreting the comparison. Mean curvature and Gaussian curvature at183 are marked with the two principal bend operations and sphere/saddle examples. In-sample and held-out are expressed through the fitting-versus-additional-test discussion rather than an unexplained evaluation label.

Reviewed phrase: Two distribution parameters were chosen to match the two empirical correlations

Plain meaning: The threshold-distribution fit uses both measured correlations as fitting targets.

Retain: The passive form keeps the fitting operation in focus. The paper and its model are already the actors, so inventing we or the team would not clarify the mechanism.

Necessity: The table and processing list define what the reported tests actually compare. Uncertain final sample sizes, mice/rats wording, and the unresolved 3D unit conversion must remain visible to prevent false precision. The heterogeneous-threshold extension needs its own parameter accounting.

References: content/chapters/05c-place-tests.md::sec:PLACE-DATA::p147, content/chapters/05c-place-tests.md::sec:PLACE-DATA::p151, content/chapters/05c-place-tests.md::sec:PLACE-DATA::p163, content/chapters/05c-place-tests.md::sec:PLACE-DATA::p165, content/chapters/05c-place-tests.md::sec:PLACE-DATA::p169, content/chapters/05c-place-tests.md::sec:PLACE-DATA::p173, content/chapters/05c-place-tests.md::sec:PLACE-DATA::p177, content/chapters/05c-place-tests.md::sec:PLACE-DATA::p183, content/chapters/05c-place-tests.md::sec:PLACE-DATA::p203, content/chapters/05c-place-tests.md::sec:PLACE-DATA::p229

### content/chapters/05c-place-tests.md::sec:PLACE-WIRING

Input profiles, weights and their variance are defined before the covariance calculation. The Gaussian limit is described through independent vectors, normalization and no dominant input. The existing Gaussian-process, stationarity and smoothness terms are reused without new blue spans.

Reviewed phrase: A large anatomical input count alone does not establish how many inputs contribute there.

Plain meaning: Many anatomical connections do not guarantee that many of them are active at this position.

Retain: Alone and there have precise jobs: count is insufficient evidence, and there refers to each position. The negative corrects a likely biological overreading of the central-limit argument.

Necessity: The overlap interpretation explains covariance instead of leaving only an equation. The separate amplitude/width cases explain what each circuit parameter changes. The final alternatives preserve the difference between a sufficient construction and a uniquely identified circuit.

References: content/chapters/05c-place-tests.md::sec:PLACE-WIRING::p244, content/chapters/05c-place-tests.md::sec:PLACE-WIRING::p246, content/chapters/05c-place-tests.md::sec:PLACE-WIRING::p248, content/chapters/05c-place-tests.md::sec:PLACE-WIRING::p254, content/chapters/05c-place-tests.md::sec:PLACE-WIRING::p268, content/chapters/05c-place-tests.md::sec:PLACE-WIRING::p278, content/chapters/05c-place-tests.md::sec:PLACE-WIRING::p280, content/chapters/05c-place-tests.md::sec:PLACE-WIRING::p281, content/chapters/05c-place-tests.md::sec:PLACE-WIRING::p282, content/chapters/05c-place-tests.md::sec:PLACE-WIRING::p286, content/chapters/05c-place-tests.md::sec:PLACE-WIRING::p297, content/chapters/05c-place-tests.md::sec:PLACE-WIRING::p299

### content/chapters/06-synthesis.md::ch:SYNTHESIS

The opening uses earlier neural code, circuit and behavior concepts without new terms. It states the comparison problem before the section distinguishes represented and physical position.

Reviewed phrase: keeping each claim with the mathematical or experimental test that supports it

Plain meaning: Evaluate each conclusion using the kind of evidence that can establish it.

Retain: Supports is a concrete evidential relation developed in the next sections. The sentence gives a criterion for comparing the papers, not praise for the guide.

Necessity: The opening prevents combining three different successes into one untested whole-circuit claim. Its short plan is justified because the next calculation is a new hypothetical connection whose status must stay clear.

References: content/chapters/06-synthesis.md::ch:SYNTHESIS::p3, content/chapters/06-synthesis.md::ch:SYNTHESIS::p5

### content/chapters/06-synthesis.md::sec:SYNTHESIS-QUESTIONS

Spatial map, memory motion and observed movement are bold list labels, not new technical terms disguised as definitions. The following paragraph distinguishes each paper's position coordinate. Fisher information is earlier teaching, and no repeat blue marker is needed.

Reviewed phrase: The objects differ even when the word position appears in all three.

Plain meaning: Position can mean a represented network coordinate or the physical position used to evaluate a rate map.

Retain: Objects is immediately resolved by theta(t), the internal command, measured eye position and physical map position. It is not left as abstract vocabulary.

Necessity: The comparison table gives common columns for the random object, determinants and observation. The Fisher-information limit stops a claim that the eye experiment tested equality in the memory bound.

References: content/chapters/06-synthesis.md::sec:SYNTHESIS-QUESTIONS::p13, content/chapters/06-synthesis.md::sec:SYNTHESIS-QUESTIONS::p15, content/chapters/06-synthesis.md::sec:SYNTHESIS-QUESTIONS::p16, content/chapters/06-synthesis.md::sec:SYNTHESIS-QUESTIONS::p17, content/chapters/06-synthesis.md::sec:SYNTHESIS-QUESTIONS::p19, content/chapters/06-synthesis.md::sec:SYNTHESIS-QUESTIONS::p29

### content/chapters/06-synthesis.md::sec:SYNTHESIS-JOINT-CALCULATION

The setup defines x(t), f_i and R_i before use and labels the construction as a guide calculation. The local displacement and starting point are defined before Taylor expansion. Covariance and expected rate are prior definitions.

Reviewed phrase: conditional on the starting position

Plain meaning: The averaging holds the initial represented position fixed.

Retain: Conditional is an exact probabilistic restriction. Replacing it with a general association phrase would wrongly suggest an unconditional spike-covariance formula.

Necessity: The short Taylor step is the direct connection between map shape and time variation. The expected-rate, small-displacement and extra-noise limits are essential because the previous papers contain richer spiking models.

References: content/chapters/06-synthesis.md::sec:SYNTHESIS-JOINT-CALCULATION::p33, content/chapters/06-synthesis.md::sec:SYNTHESIS-JOINT-CALCULATION::p39, content/chapters/06-synthesis.md::sec:SYNTHESIS-JOINT-CALCULATION::p43, content/chapters/06-synthesis.md::sec:SYNTHESIS-JOINT-CALCULATION::p50, content/chapters/06-synthesis.md::sec:SYNTHESIS-JOINT-CALCULATION::p58

### content/chapters/06-synthesis.md::sec:SYNTHESIS-COVARIANCE-EXAMPLE

No new definition needs emphasis: slope, variance, covariance and correlation are already taught. The example gives slope units, D, time and the display baseline before reporting the numbers. Calculation and figure is a content label; Example in the heading is not a duplicate Example: example construction.

Reviewed phrase: Both changes are set by the same position displacement

Plain meaning: One random position error determines both rate changes.

Retain: The passive form has its actor in the same sentence. One direction in the two-rate plane describes the displayed line, not an unexplained geometric metaphor.

Necessity: The two opposite slopes isolate the sign of covariance with only one random quantity. The baseline only keeps displayed rates positive and is explicitly separated from the covariance. Private-noise commentary explains why the ideal line is not a universal data prediction.

References: content/chapters/06-synthesis.md::sec:SYNTHESIS-COVARIANCE-EXAMPLE::p68, content/chapters/06-synthesis.md::sec:SYNTHESIS-COVARIANCE-EXAMPLE::p81, content/chapters/06-synthesis.md::sec:SYNTHESIS-COVARIANCE-EXAMPLE::p83, content/chapters/06-synthesis.md::sec:SYNTHESIS-COVARIANCE-EXAMPLE::p91, content/chapters/06-synthesis.md::sec:SYNTHESIS-COVARIANCE-EXAMPLE::p95

### content/chapters/06-synthesis.md::sec:SYNTHESIS-EVIDENCE

Place-field statistics, Eye drift and Memory stability are parallel list labels. The text reuses previous gain, covariance, MSD and information-rate meanings. It does not mark these terms a second time.

Reviewed phrase: Shared covariance then carries information that independent private fluctuations cannot supply under the decomposition's assumptions.

Plain meaning: Under the stated decomposition, correlation across the observations reveals a shared contribution that independent private noise does not create.

Retain: Carries information is resolved by the concrete covariance/decomposition claim. The condition prevents an absolute assertion about all correlated sources. A replacement synonym would not improve this local mechanism.

Necessity: The section sorts fitted quantities, extra tests and mathematical bounds. The separate gain, stationary-noise amplitude and 1/N limits are needed because each would otherwise make the evidence look stronger than it is.

References: content/chapters/06-synthesis.md::sec:SYNTHESIS-EVIDENCE::p103, content/chapters/06-synthesis.md::sec:SYNTHESIS-EVIDENCE::p105, content/chapters/06-synthesis.md::sec:SYNTHESIS-EVIDENCE::p109, content/chapters/06-synthesis.md::sec:SYNTHESIS-EVIDENCE::p114

### content/chapters/06-synthesis.md::sec:SYNTHESIS-RELATED

Path integration is blue at121 with updating a position estimate from movement. Dendrite is blue at128 with branching input structures. Both have matching glossary entries. Earlier CA1, CA3, plasticity, integrator and retina teaching provides the other meanings; titles and author names are source identity, not definitions.

Reviewed phrase: The source and use of eye motion are different questions.

Plain meaning: What produces the motion differs from what the motion helps the visual system do.

Retain: The sentence supplies the reason the perception study belongs next to a noise-source account and prevents a false contradiction between useful motion and internal noise.

Necessity: The grouped references add model limits, new circuit constraints and distinct behavioral functions. Each group states its relationship to the three core papers; a bare list of related titles would lose that connection.

References: content/chapters/06-synthesis.md::sec:SYNTHESIS-RELATED::p119, content/chapters/06-synthesis.md::sec:SYNTHESIS-RELATED::p121, content/chapters/06-synthesis.md::sec:SYNTHESIS-RELATED::p123, content/chapters/06-synthesis.md::sec:SYNTHESIS-RELATED::p125, content/chapters/06-synthesis.md::sec:SYNTHESIS-RELATED::p128, content/chapters/06-synthesis.md::sec:SYNTHESIS-RELATED::p131

### content/chapters/06-synthesis.md::sec:SYNTHESIS-NEXT

No new technical definition is introduced. Tuning maps, fluctuations, diffusion and filters refer to the preceding calculations. If comparing behavior is an explicit conditional list label, not a new term.

Reviewed phrase: Fit diffusion only over a range where the local approximation and measurement corrections are justified.

Plain meaning: Estimate diffusion from measurements only in the range where this model and its corrections apply.

Retain: Only supplies an operational limit, and the passive justified refers to model and measurement checks. The instruction is appropriate in a proposed procedure, not an unexplained command to believe a claim.

Necessity: The sequence specifies measurements that would test the new connection. Its final proposed-work label prevents confusing a useful experiment with one the guide or source papers already performed.

References: content/chapters/06-synthesis.md::sec:SYNTHESIS-NEXT::p135, content/chapters/06-synthesis.md::sec:SYNTHESIS-NEXT::p137, content/chapters/06-synthesis.md::sec:SYNTHESIS-NEXT::p138, content/chapters/06-synthesis.md::sec:SYNTHESIS-NEXT::p139, content/chapters/06-synthesis.md::sec:SYNTHESIS-NEXT::p140, content/chapters/06-synthesis.md::sec:SYNTHESIS-NEXT::p142

## Conditional internal-metadata notes

- content/chapters/06-synthesis.yaml:18 (sec:SYNTHESIS-QUESTIONS): If displayed independently, identify the distinction between a spatial map, change in the represented coordinate, and observed downstream movement. The reader should not be left waiting for the three questions.
- content/chapters/06-synthesis.yaml:30 (sec:SYNTHESIS-EVIDENCE): If displayed independently, give a complete statement about matching each model claim to its relevant test, without introducing an absent list. The existing map-and-rate-change requirement can remain.
- content/chapters/06-synthesis.yaml:36 (sec:SYNTHESIS-RELATED): If displayed independently, state the role of the related studies in testing assumptions or leaving circuit choices open as a complete summary, without promising absent items.
- content/chapters/06-synthesis.yaml:41 (sec:SYNTHESIS-NEXT): If displayed independently, describe the proposed joint measurements as a complete summary, without introducing an absent sequence. Preserve that the work is proposed and concerns the same population.

These observations were initially classified as required reader-text repairs under a standalone-output assumption. That classification was withdrawn after independent inspection of pinned Publisher 0.8.23. Quarto renders chapter.content_blocks and their paragraph/list nodes, without using section.summary. The observations and classification history remain in the JSON. No current metadata rewrite is required, and no manuscript edits were made.

## Diagnostic and format decisions

511 alerts represent 160 unique source lines. Duplicate Google/Microsoft warnings and source-punctuation matches are retained with reasons. Native error count does not establish semantic quality. Bounded controls were inspected as passages, not treated as proof that rules were satisfied.

All reader-facing chapter purposes, captions, alt text and fold titles preserve the relevant objects and scope. Four section-summary metadata values end with list lead-ins; these are preserved as conditional notes because the pinned Quarto renderer does not display them independently. In the body, all four lead-ins have their lists. The other 12 metadata summaries are complete even alone. Artwork identity and pixels remain deferred.

The Stage 1 report remains unchanged. Its system-field verdict retain means adequate. Its expert-objection disposition not sustained on complete reading means does not apply. These mappings apply to all 22 assessments for their original individual reasons. They clarify serialization only.

## Timing and limits

Stage 2 started at 2026-10-29T13:34:56.7709936+02:00. Completed at 2026-10-29T13:45:02.0593273+02:00. Wall time for Stage 2: 605.3 seconds. Wall time since preparation: 2362.2 seconds. Time since the previous public checkpoint: 178.6 seconds.
Stage 3 remains pending. No guide pixel acceptance or release approval is claimed. Awake execution time unverified. Token stats unavailable.
