# Place group: Stage 1 truth and reasoning

Local request: `final-place-truth-20261029-01`. Reviewer: `/root/accept_place`, assigned GPT-6 Astra, high reasoning. Fresh first manuscript review; no authorship of assessed text.

Input: `3fa06682def9f93bbafd2b39bfe5f3a5641febda3bbd57c2f9caf86c8b465283`.
Contract: `593934f3af51c49175417df3e4263df20a0835575d099bad4f0070163b4a17dc`.

Stage 1 found no required scientific correction in the frozen text. This is not complete teaching acceptance or release approval. Stage 2 and Stage 3 remain pending, and figure pixel acceptance remains deferred.

All 22 units, 429 extracted paragraph records and 258 selected claim rows are represented in the JSON. Hidden Vale comments and structural wrappers are distinguished from reader text. Equations, typed tables, source notes, captions, alt text and available SVG labels were read alongside the prose.

## Source and numerical checks

The source strings of all six Markdown files matched the neutral packet. The Mainali paper and supplement were read directly; supplement PDF pages 13-15 were rendered to verify S18, S23 and S25. Those printed expressions support the guide correction box. The recalculated means, crossing count, Poisson conditioning, limiting means, percentage errors, negative EC example and synthesis covariance agree with the text.

Source metadata and bounded related-study claims were checked using local primary text and the cited publisher/author records. Some DOI resolver attempts failed; alternate primary pages supplied the needed source identity. This review does not claim a complete live-link or rendered-footnote pass.

## Unit answers

### content/chapters/glossary.md::ch:GLOSSARY

Does lookup preserve the distinctions on which the place and synthesis calculations depend?

Yes. Gaussian process means finite joint Gaussian values, excursion set means positions above a level, and local diffusion means variance growth of a coordinate. The entries do not turn a spatial random map into motion. The left/right vector entries agree with the earlier linearized network calculation.

Correctness objection: The short Poisson or diffusion entries could imply independent complete spike trains or identify spatial scale with temporal diffusion.

Decision: retain. The Poisson entry explicitly excludes that recurrent-train inference; diffusion units are coordinate squared per time, whereas Gaussian process and stationarity entries describe a map over position. The definitions match the chapter uses.

References: content/chapters/glossary.md::ch:GLOSSARY::p7, content/chapters/glossary.md::ch:GLOSSARY::p23, content/chapters/glossary.md::ch:GLOSSARY::p41, content/chapters/glossary.md::ch:GLOSSARY::p49, content/chapters/glossary.md::ch:GLOSSARY::p58, content/chapters/glossary.md::ch:GLOSSARY::p79, content/chapters/glossary.md::ch:GLOSSARY::p91, content/chapters/glossary.md::ch:GLOSSARY::p100

### content/chapters/references.md::ch:REFERENCES

Do the entries identify the works actually cited in the reviewed explanations?

Yes. The 2012, 2022 and 2025 entries match their papers, the Gaussian notes are separate, Taylor is the cited EC theorem source, and the remaining entries match the related-study paragraph. No source-identity contradiction was found. Citation styling and full first-use order belong to Stage 2/3.

Correctness objection: An inaccessible DOI or a newly published article could hide an incorrect source identity.

Decision: retain. The relevant publication identities were recovered from primary pages, local paper text or publication metadata. Some DOI resolver attempts failed, but alternate publisher or author records identify the works. Failed resolver attempts are not recorded as successful link checks.

References: content/chapters/references.md::ch:REFERENCES::p3, content/chapters/references.md::ch:REFERENCES::p6, content/chapters/references.md::ch:REFERENCES::p9, content/chapters/references.md::ch:REFERENCES::p12, content/chapters/references.md::ch:REFERENCES::p16, content/chapters/references.md::ch:REFERENCES::p20, content/chapters/references.md::ch:REFERENCES::p24, content/chapters/references.md::ch:REFERENCES::p35, content/chapters/references.md::ch:REFERENCES::p38, content/chapters/references.md::ch:REFERENCES::p41, content/chapters/references.md::ch:REFERENCES::p58, content/chapters/references.md::ch:REFERENCES::p62, content/chapters/references.md::ch:REFERENCES::p65

### content/chapters/05-place-fields.md::ch:PLACE-FIELDS

What is random, and what changes when the animal moves?

The ensemble contains different input functions. During traversal of one draw, x changes and the function is evaluated at x. The chapter does not introduce diffusion or learning.

Correctness objection: Calling the random input a rate map might imply that the data directly measure synaptic input or that the field map evolves while the animal moves.

Decision: retain. p9 identifies combined synaptic input as the interpretation and says recordings estimate firing rates; p17 explicitly fixes each drawn map over movement. Mainali Methods S1 and Eq. 2-3 support these roles.

References: content/chapters/05-place-fields.md::ch:PLACE-FIELDS::p3, content/chapters/05-place-fields.md::ch:PLACE-FIELDS::p7, content/chapters/05-place-fields.md::ch:PLACE-FIELDS::p9, content/chapters/05-place-fields.md::ch:PLACE-FIELDS::p15, content/chapters/05-place-fields.md::ch:PLACE-FIELDS::p17

### content/chapters/05-place-fields.md::sec:PLACE-GP

Why can Gaussian heights be used in the crossing calculation, while firing rates cannot simply be assumed Gaussian?

The process definition applies to h and z before rectification. The jointly Gaussian height and derivative have the derivative covariance given in the chapter; applying max(u,0) adds zero mass and changes the distribution. The chapter says this before crossings depend on it.

Correctness objection: The gain or input amplitude could be treated as interchangeable with threshold or distance scale.

Decision: retain. p68 separates their effects and explicitly limits gain-invariant boundaries to the zero-rate definition. p105 allows equal local scales with different long-distance covariance. This preserves both parameter roles and the regularity assumptions.

References: content/chapters/05-place-fields.md::sec:PLACE-GP::p23, content/chapters/05-place-fields.md::sec:PLACE-GP::p27, content/chapters/05-place-fields.md::sec:PLACE-GP::p36, content/chapters/05-place-fields.md::sec:PLACE-GP::p47, content/chapters/05-place-fields.md::sec:PLACE-GP::p50, content/chapters/05-place-fields.md::sec:PLACE-GP::p52, content/chapters/05-place-fields.md::sec:PLACE-GP::p54, content/chapters/05-place-fields.md::sec:PLACE-GP::p66, content/chapters/05-place-fields.md::sec:PLACE-GP::p68, content/chapters/05-place-fields.md::sec:PLACE-GP::p85, content/chapters/05-place-fields.md::sec:PLACE-GP::p98, content/chapters/05-place-fields.md::sec:PLACE-GP::p105

### content/chapters/05-place-fields.md::sec:PLACE-KAC-RICE

Why does a steep crossing not count more than once, and why does the finite track need a correction?

Its larger slope is canceled by its narrower threshold-band width. A field can enter before x=0, so it intersects the track without a counted upcrossing; its expected indicator is Q(q).

Correctness objection: The exact crossing density could be mistaken for an exact finite-track field count without the left endpoint term.

Decision: retain. p177-185 gives the exact counting identity and warns that removing incomplete fields changes the convention. The caption uses two upcrossings plus one initially active field consistently.

References: content/chapters/05-place-fields.md::sec:PLACE-KAC-RICE::p123, content/chapters/05-place-fields.md::sec:PLACE-KAC-RICE::p125, content/chapters/05-place-fields.md::sec:PLACE-KAC-RICE::p131, content/chapters/05-place-fields.md::sec:PLACE-KAC-RICE::p139, content/chapters/05-place-fields.md::sec:PLACE-KAC-RICE::p149, content/chapters/05-place-fields.md::sec:PLACE-KAC-RICE::p157, content/chapters/05-place-fields.md::sec:PLACE-KAC-RICE::p173, content/chapters/05-place-fields.md::sec:PLACE-KAC-RICE::p177, content/chapters/05-place-fields.md::sec:PLACE-KAC-RICE::p185

### content/chapters/05-place-fields.md::sec:PLACE-INFERENCE

Can a low count distinguish a high threshold from a slowly changing map?

Not alone. The field/gap ratio determines the active fraction and thus q; their total mean then gives sigma. This is a model-based inference under the stated averaging and selection conventions.

Correctness objection: Exact first moments could be used to claim a Poisson count distribution at all thresholds, or fitted selected-cell means could be treated as unconditional.

Decision: retain. p229 supplies the extra rare-event/dependence conditions and a periodic counterexample; p237-246 derives the selection correction. Both distinctions are necessary and correctly stated.

References: content/chapters/05-place-fields.md::sec:PLACE-INFERENCE::p189, content/chapters/05-place-fields.md::sec:PLACE-INFERENCE::p191, content/chapters/05-place-fields.md::sec:PLACE-INFERENCE::p204, content/chapters/05-place-fields.md::sec:PLACE-INFERENCE::p206, content/chapters/05-place-fields.md::sec:PLACE-INFERENCE::p223, content/chapters/05-place-fields.md::sec:PLACE-INFERENCE::p229, content/chapters/05-place-fields.md::sec:PLACE-INFERENCE::p237, content/chapters/05-place-fields.md::sec:PLACE-INFERENCE::p246

### content/chapters/05b-place-sizes.md::ch:PLACE-SIZES

Which later result is approximate and which has an independent exact argument?

The parabolic geometry and induced size laws are asymptotic. The slope selection law follows directly from stationary Gaussian crossing weights.

Correctness objection: The reader might infer that every field is parabolic at the fitted threshold.

Decision: retain. The opening explicitly identifies the high-threshold approximation and the following section lists the limit and derivative requirements. Finite-threshold departures are later quantified.

References: content/chapters/05b-place-sizes.md::ch:PLACE-SIZES::p3, content/chapters/05b-place-sizes.md::ch:PLACE-SIZES::p9, content/chapters/05b-place-sizes.md::ch:PLACE-SIZES::p11

### content/chapters/05b-place-sizes.md::sec:PLACE-RARE-PEAKS

Why does peak height lead to a Rayleigh width law?

The typical excess is order 1/q, while curvature is order q. Width is proportional to sqrt(U)/q; U has an exponential limiting law. Peak rate is proportional to excess and hence to width squared at fixed high q.

Correctness objection: Selecting a maximum could invalidate the height-conditioned Hessian mean, or the finite data exponents could be claimed as the limiting exponent two.

Decision: retain. p43 acknowledges maximum-selection curvature weighting and only claims its leading high-peak shape. p96 reports source exponents 1.42/1.46 and 1.75/1.71 as finite-threshold comparisons, not measurements of two. The primary Figure 3 labels confirm the numbers.

References: content/chapters/05b-place-sizes.md::sec:PLACE-RARE-PEAKS::p17, content/chapters/05b-place-sizes.md::sec:PLACE-RARE-PEAKS::p21, content/chapters/05b-place-sizes.md::sec:PLACE-RARE-PEAKS::p22, content/chapters/05b-place-sizes.md::sec:PLACE-RARE-PEAKS::p23, content/chapters/05b-place-sizes.md::sec:PLACE-RARE-PEAKS::p24, content/chapters/05b-place-sizes.md::sec:PLACE-RARE-PEAKS::p28, content/chapters/05b-place-sizes.md::sec:PLACE-RARE-PEAKS::p35, content/chapters/05b-place-sizes.md::sec:PLACE-RARE-PEAKS::p43, content/chapters/05b-place-sizes.md::sec:PLACE-RARE-PEAKS::p45, content/chapters/05b-place-sizes.md::sec:PLACE-RARE-PEAKS::p57, content/chapters/05b-place-sizes.md::sec:PLACE-RARE-PEAKS::p73, content/chapters/05b-place-sizes.md::sec:PLACE-RARE-PEAKS::p79, content/chapters/05b-place-sizes.md::sec:PLACE-RARE-PEAKS::p90, content/chapters/05b-place-sizes.md::sec:PLACE-RARE-PEAKS::p92, content/chapters/05b-place-sizes.md::sec:PLACE-RARE-PEAKS::p96

### content/chapters/05b-place-sizes.md::sec:PLACE-SIZE-LAW

Why do the three density shapes differ even though their transformed variable agrees?

Size is proportional to radius to the power d. The nonlinear map U=beta s^(2/d) changes the density by a dimension-dependent Jacobian; merely removing units with w does not remove that shape difference. The 3D divergence is integrable and creates no atom at zero.

Correctness objection: A wrong width factor or inverted mean-size scale in the printed supplement could contaminate the guide formulas.

Decision: retain. Inspected the printed S18, S23 and S25 directly: the guide correctly distinguishes division by mean, the missing sqrt(2), and the negative finite-height quadratic exponent. Its constants also agree with the independent boundary-slope derivation and exact 1D high-q mean.

References: content/chapters/05b-place-sizes.md::sec:PLACE-SIZE-LAW::p113, content/chapters/05b-place-sizes.md::sec:PLACE-SIZE-LAW::p115, content/chapters/05b-place-sizes.md::sec:PLACE-SIZE-LAW::p117, content/chapters/05b-place-sizes.md::sec:PLACE-SIZE-LAW::p126, content/chapters/05b-place-sizes.md::sec:PLACE-SIZE-LAW::p134, content/chapters/05b-place-sizes.md::sec:PLACE-SIZE-LAW::p136, content/chapters/05b-place-sizes.md::sec:PLACE-SIZE-LAW::p145, content/chapters/05b-place-sizes.md::sec:PLACE-SIZE-LAW::p147, content/chapters/05b-place-sizes.md::sec:PLACE-SIZE-LAW::p156, content/chapters/05b-place-sizes.md::sec:PLACE-SIZE-LAW::p166, content/chapters/05b-place-sizes.md::sec:PLACE-SIZE-LAW::p168, content/chapters/05b-place-sizes.md::sec:PLACE-SIZE-LAW::p176, content/chapters/05b-place-sizes.md::sec:PLACE-SIZE-LAW::p184, content/chapters/05b-place-sizes.md::sec:PLACE-SIZE-LAW::p188, content/chapters/05b-place-sizes.md::sec:PLACE-SIZE-LAW::p190, content/chapters/05b-place-sizes.md::sec:PLACE-SIZE-LAW::p198, content/chapters/05b-place-sizes.md::sec:PLACE-SIZE-LAW::p200, content/chapters/05b-place-sizes.md::sec:PLACE-SIZE-LAW::p204

### content/chapters/05b-place-sizes.md::sec:PLACE-SLICES

What is counted after a line cuts a 3D field?

Connected active intervals on the line. A 3D component may be missed or cut into several intervals, and its sampling probability depends on geometry. The chapter states those differences before using the slice comparison.

Correctness objection: A matching volume histogram might automatically imply matching line and plane histograms.

Decision: retain. The text explains hit probability and cut position and cites the spherical comparison in S2. That primary caption matches volume and peak rate by construction but reports slice and EC disagreement, supporting the stated distinction.

References: content/chapters/05b-place-sizes.md::sec:PLACE-SLICES::p210, content/chapters/05b-place-sizes.md::sec:PLACE-SLICES::p212, content/chapters/05b-place-sizes.md::sec:PLACE-SLICES::p216, content/chapters/05b-place-sizes.md::sec:PLACE-SLICES::p222, content/chapters/05b-place-sizes.md::sec:PLACE-SLICES::p224, content/chapters/05b-place-sizes.md::sec:PLACE-SLICES::p226, content/chapters/05b-place-sizes.md::sec:PLACE-SLICES::p233, content/chapters/05b-place-sizes.md::sec:PLACE-SLICES::p242

### content/chapters/05b-place-sizes.md::sec:PLACE-SLOPES

Why is the positive boundary derivative not half Gaussian?

The sampling event is a crossing. Crossings weight each positive slope by its magnitude, changing the normalized density to Rayleigh.

Correctness objection: Rayleigh boundary slopes might be presented as a high-threshold result or as a half-Gaussian derivative sampled at random positions.

Decision: retain. The height factor cancels exactly; p267 states q independence and contrasts the spatially uniform derivative sample. The width check is separately labeled high threshold. STAR Methods confirms the 0.1m finite difference.

References: content/chapters/05b-place-sizes.md::sec:PLACE-SLOPES::p257, content/chapters/05b-place-sizes.md::sec:PLACE-SLOPES::p259, content/chapters/05b-place-sizes.md::sec:PLACE-SLOPES::p267, content/chapters/05b-place-sizes.md::sec:PLACE-SLOPES::p273, content/chapters/05b-place-sizes.md::sec:PLACE-SLOPES::p279, content/chapters/05b-place-sizes.md::sec:PLACE-SLOPES::p283

### content/chapters/05c-place-tests.md::ch:PLACE-TESTS

What is the new evidence beyond a size histogram?

The arrangement of components and holes across thresholds, with measured boundaries retained, can reject shapes that share the same sizes. It still does not uniquely identify a circuit.

Correctness objection: A good spatial fit might be claimed to recover the producing synapses.

Decision: retain. The opening asks how much the agreement tells us and the wiring section concludes that additional circuit measurements are needed. This is the right interpretation of a sufficient statistical construction.

References: content/chapters/05c-place-tests.md::ch:PLACE-TESTS::p3, content/chapters/05c-place-tests.md::ch:PLACE-TESTS::p7, content/chapters/05c-place-tests.md::ch:PLACE-TESTS::p9

### content/chapters/05c-place-tests.md::sec:PLACE-TOPOLOGY

Why can expected chi be negative while a field count cannot?

Chi subtracts tunnels/holes as well as adding components and cavities. The q=0 cube example has more negative topological contribution on average. Only the sparse high-level regime makes each component approximately one solid blob.

Correctness objection: Negative EC or omission of boundary factors could make the formulas look like impossible negative field counts.

Decision: retain. The chapter defines holes and cavities first, labels signed densities, retains Q(q) and face terms, and only identifies EC with field count at high thresholds. Taylor Eq.1.4/5.1 supports the polynomial structure; the box algebra is shown in the guide.

References: content/chapters/05c-place-tests.md::sec:PLACE-TOPOLOGY::p13, content/chapters/05c-place-tests.md::sec:PLACE-TOPOLOGY::p17, content/chapters/05c-place-tests.md::sec:PLACE-TOPOLOGY::p19, content/chapters/05c-place-tests.md::sec:PLACE-TOPOLOGY::p21, content/chapters/05c-place-tests.md::sec:PLACE-TOPOLOGY::p23, content/chapters/05c-place-tests.md::sec:PLACE-TOPOLOGY::p25, content/chapters/05c-place-tests.md::sec:PLACE-TOPOLOGY::p35, content/chapters/05c-place-tests.md::sec:PLACE-TOPOLOGY::p37, content/chapters/05c-place-tests.md::sec:PLACE-TOPOLOGY::p39, content/chapters/05c-place-tests.md::sec:PLACE-TOPOLOGY::p49, content/chapters/05c-place-tests.md::sec:PLACE-TOPOLOGY::p59, content/chapters/05c-place-tests.md::sec:PLACE-TOPOLOGY::p63, content/chapters/05c-place-tests.md::sec:PLACE-TOPOLOGY::p79, content/chapters/05c-place-tests.md::sec:PLACE-TOPOLOGY::p93, content/chapters/05c-place-tests.md::sec:PLACE-TOPOLOGY::p99, content/chapters/05c-place-tests.md::sec:PLACE-TOPOLOGY::p114, content/chapters/05c-place-tests.md::sec:PLACE-TOPOLOGY::p120, content/chapters/05c-place-tests.md::sec:PLACE-TOPOLOGY::p121, content/chapters/05c-place-tests.md::sec:PLACE-TOPOLOGY::p123, content/chapters/05c-place-tests.md::sec:PLACE-TOPOLOGY::p129, content/chapters/05c-place-tests.md::sec:PLACE-TOPOLOGY::p137, content/chapters/05c-place-tests.md::sec:PLACE-TOPOLOGY::p139

### content/chapters/05c-place-tests.md::sec:PLACE-DATA

Which comparisons add evidence beyond fitting mean field size?

Length and gap histogram shapes, log-length moments, slices and topology are additional comparisons with the conditions specified. The variable-threshold correlations themselves are fitted; the continued length/gap agreement is the additional check.

Correctness objection: A fitted statistic, rate multiplier or cell-selection decision could be hidden as an independent prediction.

Decision: retain. The text identifies what was fitted, the separate gain, processing thresholds, subset counts, and the two fitted parameters in the varying-threshold extension. S1-S5 and Methods support those distinctions. It also flags the main/STAR mouse-rat mismatch rather than silently resolving it.

References: content/chapters/05c-place-tests.md::sec:PLACE-DATA::p147, content/chapters/05c-place-tests.md::sec:PLACE-DATA::p151, content/chapters/05c-place-tests.md::sec:PLACE-DATA::p163, content/chapters/05c-place-tests.md::sec:PLACE-DATA::p165, content/chapters/05c-place-tests.md::sec:PLACE-DATA::p169, content/chapters/05c-place-tests.md::sec:PLACE-DATA::p173, content/chapters/05c-place-tests.md::sec:PLACE-DATA::p174, content/chapters/05c-place-tests.md::sec:PLACE-DATA::p175, content/chapters/05c-place-tests.md::sec:PLACE-DATA::p176, content/chapters/05c-place-tests.md::sec:PLACE-DATA::p177, content/chapters/05c-place-tests.md::sec:PLACE-DATA::p179, content/chapters/05c-place-tests.md::sec:PLACE-DATA::p183, content/chapters/05c-place-tests.md::sec:PLACE-DATA::p203, content/chapters/05c-place-tests.md::sec:PLACE-DATA::p229

### content/chapters/05c-place-tests.md::sec:PLACE-WIRING

Which assumptions create Gaussianity and which create spatial covariance?

Random weighted summation supplies the finite joint Gaussian limit under its conditions. The input profiles and their overlap determine covariance; dense uniform placement gives translation invariance, and smooth profiles supply the regularity assumed for the map.

Correctness objection: Anatomical input count alone or Gaussian output statistics could be said to prove a random circuit.

Decision: retain. The text requires active contributors and CLT conditions, separates amplitude from width changes, and calls this one possible mechanism. It explicitly allows correlations, structured input, plasticity or recurrent processing and asks for further circuit measurements.

References: content/chapters/05c-place-tests.md::sec:PLACE-WIRING::p244, content/chapters/05c-place-tests.md::sec:PLACE-WIRING::p246, content/chapters/05c-place-tests.md::sec:PLACE-WIRING::p248, content/chapters/05c-place-tests.md::sec:PLACE-WIRING::p254, content/chapters/05c-place-tests.md::sec:PLACE-WIRING::p258, content/chapters/05c-place-tests.md::sec:PLACE-WIRING::p268, content/chapters/05c-place-tests.md::sec:PLACE-WIRING::p272, content/chapters/05c-place-tests.md::sec:PLACE-WIRING::p280, content/chapters/05c-place-tests.md::sec:PLACE-WIRING::p281, content/chapters/05c-place-tests.md::sec:PLACE-WIRING::p282, content/chapters/05c-place-tests.md::sec:PLACE-WIRING::p284, content/chapters/05c-place-tests.md::sec:PLACE-WIRING::p286, content/chapters/05c-place-tests.md::sec:PLACE-WIRING::p288, content/chapters/05c-place-tests.md::sec:PLACE-WIRING::p297, content/chapters/05c-place-tests.md::sec:PLACE-WIRING::p299, content/chapters/05c-place-tests.md::sec:PLACE-WIRING::p303

### content/chapters/06-synthesis.md::ch:SYNTHESIS

What would be missing from a model that matches field shapes but has no dynamics?

It would not specify how a represented position changes or how a downstream measurement filters it. The synthesis makes those missing pieces its subject.

Correctness objection: Shared vocabulary such as position or noise might make the three papers appear to test the same object.

Decision: retain. The next unit identifies each coordinate and its role and the local calculation is explicitly a new guide construction. The opening is supported by those concrete distinctions.

References: content/chapters/06-synthesis.md::ch:SYNTHESIS::p3, content/chapters/06-synthesis.md::ch:SYNTHESIS::p5

### content/chapters/06-synthesis.md::sec:SYNTHESIS-QUESTIONS

What extra specification turns a fixed spatial tuning curve into a dynamical prediction?

A time path for the represented coordinate. Without x(t), f_i(x) supplies values across space, not a time course or a diffusion coefficient.

Correctness objection: The 2022 behavioral fit could be called an experimental test of the full 2012 information-diffusion bound.

Decision: retain. p29 explicitly denies that inference and identifies the unmeasured information quantity. This is supported by the studies actual methods and the earlier information chapter.

References: content/chapters/06-synthesis.md::sec:SYNTHESIS-QUESTIONS::p13, content/chapters/06-synthesis.md::sec:SYNTHESIS-QUESTIONS::p15, content/chapters/06-synthesis.md::sec:SYNTHESIS-QUESTIONS::p16, content/chapters/06-synthesis.md::sec:SYNTHESIS-QUESTIONS::p17, content/chapters/06-synthesis.md::sec:SYNTHESIS-QUESTIONS::p19, content/chapters/06-synthesis.md::sec:SYNTHESIS-QUESTIONS::p21, content/chapters/06-synthesis.md::sec:SYNTHESIS-QUESTIONS::p29

### content/chapters/06-synthesis.md::sec:SYNTHESIS-JOINT-CALCULATION

Why do two cells become correlated even though their tuning functions are fixed?

They share the same random displacement. Each converts it to a rate change through its own slope, so the covariance is the displacement variance multiplied by those slopes.

Correctness objection: The formula could be mistaken for total recurrent spike-count covariance or used across a firing threshold.

Decision: retain. p39 and p58 explicitly distinguish expected rates from spike counts, name additional variability, and restrict the linear approximation near thresholds or large moves.

References: content/chapters/06-synthesis.md::sec:SYNTHESIS-JOINT-CALCULATION::p33, content/chapters/06-synthesis.md::sec:SYNTHESIS-JOINT-CALCULATION::p39, content/chapters/06-synthesis.md::sec:SYNTHESIS-JOINT-CALCULATION::p43, content/chapters/06-synthesis.md::sec:SYNTHESIS-JOINT-CALCULATION::p50, content/chapters/06-synthesis.md::sec:SYNTHESIS-JOINT-CALCULATION::p58

### content/chapters/06-synthesis.md::sec:SYNTHESIS-COVARIANCE-EXAMPLE

What produces the negative sign, and what would private noise change?

Opposite tuning slopes map the same position change into opposite rate changes. Independent private noise adds variances without adding this covariance, reducing the absolute correlation.

Correctness objection: Negative covariance could be interpreted as an inhibitory connection, or -1 could be claimed with other noise sources present.

Decision: retain. p81 limits the result to the single common source and directly separates covariance sign from connection sign. p91 explains the line in rate-change coordinates.

References: content/chapters/06-synthesis.md::sec:SYNTHESIS-COVARIANCE-EXAMPLE::p68, content/chapters/06-synthesis.md::sec:SYNTHESIS-COVARIANCE-EXAMPLE::p81, content/chapters/06-synthesis.md::sec:SYNTHESIS-COVARIANCE-EXAMPLE::p83, content/chapters/06-synthesis.md::sec:SYNTHESIS-COVARIANCE-EXAMPLE::p91, content/chapters/06-synthesis.md::sec:SYNTHESIS-COVARIANCE-EXAMPLE::p95

### content/chapters/06-synthesis.md::sec:SYNTHESIS-EVIDENCE

Why is 1/N scaling not enough to test the information-diffusion inequality?

The inequality also specifies the information quantity, time constants and noise/dynamics assumptions. Many mechanisms can have the same population-size scaling without matching that quantitative bound.

Correctness objection: The eye paragraph might exclude every peripheral noise process, including slow correlated ones.

Decision: retain. It states that changing amplitude alone cannot reproduce the accumulating signal. The earlier timing chapter explicitly distinguishes a slow correlated peripheral hypothesis from the white-noise alternative rejected by the comparison. Read together, the scope is adequate.

References: content/chapters/06-synthesis.md::sec:SYNTHESIS-EVIDENCE::p103, content/chapters/06-synthesis.md::sec:SYNTHESIS-EVIDENCE::p105, content/chapters/06-synthesis.md::sec:SYNTHESIS-EVIDENCE::p109, content/chapters/06-synthesis.md::sec:SYNTHESIS-EVIDENCE::p114

### content/chapters/06-synthesis.md::sec:SYNTHESIS-RELATED

Do structured connections and plasticity contradict a useful Gaussian description of field statistics?

No. The statistical model does not uniquely specify its biological construction. These studies identify structure and learning that may coexist with a good aggregate spatial description, while motivating separate circuit measurements.

Correctness objection: A related study may be used as direct support for a macaque variance estimate or a unique random-wiring account.

Decision: retain. The paragraph explicitly withholds those transfers. Maimon reports predominantly single CA3 fields and multiple CA1 fields with similar sizes; Druckmann reports nonuniform clustered connectivity; Bittner links plateau events to plasticity and field formation; Nghiem addresses visual benefit rather than generator identity.

References: content/chapters/06-synthesis.md::sec:SYNTHESIS-RELATED::p119, content/chapters/06-synthesis.md::sec:SYNTHESIS-RELATED::p121, content/chapters/06-synthesis.md::sec:SYNTHESIS-RELATED::p123, content/chapters/06-synthesis.md::sec:SYNTHESIS-RELATED::p125, content/chapters/06-synthesis.md::sec:SYNTHESIS-RELATED::p128, content/chapters/06-synthesis.md::sec:SYNTHESIS-RELATED::p131

### content/chapters/06-synthesis.md::sec:SYNTHESIS-NEXT

What two kinds of data are required for the proposed joint test?

Spatial tuning estimates and fluctuations from the same population, with enough information about correction signals and measurement filters to interpret their relationship.

Correctness objection: Agreement with both statistics could be claimed to uniquely verify a complete circuit.

Decision: retain. p142 says it constrains the model more and calls for further tests after a mismatch. It also explicitly labels the work proposed, so no experiment or replication is fabricated.

References: content/chapters/06-synthesis.md::sec:SYNTHESIS-NEXT::p135, content/chapters/06-synthesis.md::sec:SYNTHESIS-NEXT::p137, content/chapters/06-synthesis.md::sec:SYNTHESIS-NEXT::p138, content/chapters/06-synthesis.md::sec:SYNTHESIS-NEXT::p139, content/chapters/06-synthesis.md::sec:SYNTHESIS-NEXT::p140, content/chapters/06-synthesis.md::sec:SYNTHESIS-NEXT::p142

## Limits and timing

- Stage2 necessity, terminology, definition emphasis and contextual wording.
- Stage3 every-paragraph purpose/connections and final connected reader-understanding assessment.
- Guide figure pixel acceptance, layout, and exact artwork-excerpt fidelity, as instructed. Textual labels/captions were checked; no approval of rendered artwork is claimed.
- Full publication link/footnote rendering audit and release-format checks. Some DOI resolver attempts failed while alternate primary sources supplied identity and content.

Measured Stage 1 start: 2026-10-29T13:19:47.4518693+02:00. Completion: 2026-10-29T13:34:27.4925756+02:00. Wall time for Stage 1: 880.0 seconds. Wall time since preparation: 1727.7 seconds. Time since the previous public checkpoint: 62.1 seconds.
One commentary label, 13:22:42, was mistyped. The next measured timestamp was 13:21:43.5424428+02:00; this was a reporting error, not evidence of a system-clock change.
Awake execution time unverified. Token stats unavailable.

Record validation: all current unit, paragraph and selected claim IDs are covered. All supported question references resolve. All 12 Markdown and sidecar hashes remain unchanged. The 429 paragraph records include 328 reader text records, 71 hidden controls and 30 structural wrappers.
