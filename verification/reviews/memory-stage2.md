# Memory, foundations, and glossary: stage 2 necessity and terminology

Reviewer: independent agent /root/review_memory_guide. Local request ID memory-stage2-20261022T194410+0300. This is a separate stage 2 call after stage 1 and its repair recheck. No chapters were edited. Model configuration requested by PLAN is GPT-6.1-sol/high; exact runtime model/version is not exposed. I reused the source/math context, read the current prose in order, and did not repeat mathematical tests.

Started: 2026-10-22T19:44:10.8918667+03:00. Measured checkpoints: 19:45:25.6495350 and 19:46:51.9522023, all 2026-10-22 +03:00. End, measured wall duration, input hashes and content-block locators are in JSON. Awake execution is unverified; sleep/resume logs were not inspected. Token stats unavailable.

Audience remains undergraduate calculus, basic probability and linear algebra, without neuroscience, stochastic-process, Fisher-information, or control-theory knowledge. I applied the deletion test before asking to expand or replace wording. Findings below concern necessary meanings or needless reader-facing task history. They do not call for synonyms wherever a word recurs.

## Findings requiring local decisions

### N1: stochastic convention and point-mass notation need their first-use meanings

`02-memory-dynamics.md`, sec:MEMORY-LONG-TIME, lines 237–260 and 278; sec:MEMORY-DRIFT-SCOPE, line 310. “Itô increment” first appears at line 237, while its meaning, evaluating the coefficient at the beginning of the increment, arrives at line 278. “Stratonovich equation” at line 310 never says that its limiting convention uses midpoint evaluation. The continuous delta in p(theta,0)=delta(theta-Theta), line 260, is also unexplained; the only earlier delta explanation, line 41, concerns the different Kronecker delta delta_ij.

Deletion test: the state-dependent density calculation and the drift comparison need their conventions, and the initial condition needs to represent all probability at Theta. Removing those ideas loses necessary assumptions, so retain them and put their meanings beside the first use. Move the brief Itô explanation before the Taylor calculation, add a short midpoint description at Stratonovich's first use, and explain that this delta denotes a point mass at Theta rather than the earlier 0/1 matrix symbol. Full stochastic-calculus or distribution-theory sections are unnecessary. Add lookup entries only for technical names actually kept as introduced terms. Priority: medium.

### N2: ring-network words need a plain connection to firing rates

`02-memory-dynamics.md`, sec:MEMORY-SPIKES line 60: “equally spaced preferred angles”; sec:MEMORY-SYMMETRIC line 216: “a particular bump shape”; sec:MEMORY-FIGURES lines 320–324: “the bump,” “preferred angles,” and “sigmoidal.” Earlier foundations teach tuning curves and periodic coordinates, but not preferred angle, an activity bump, or sigmoidal shape.

Deletion test: preferred-angle labels and a localized rate peak are needed to interpret the ring figures; merely removing them loses what is moving. At line 60 explain preferred angle as an angle where that neuron's tuning curve peaks. At the first retained bump use, describe a localized peak of population activity across those preferred angles; an alternative is to drop the early “particular bump shape” aside and explain the activity bump beside Fig.1B. At line 324 add the direct meaning “S-shaped” when introducing sigmoidal. These short definitions connect source labels to already taught rates without another neuroscience section. Priority: medium.

### N3: define prior knowledge before it changes an error-bound assumption

`03-memory-information.md`, sec:MEMORY-FI line 64: “A strong prior”; sec:MEMORY-READOUT-SETUP line 213: “informative priors”; sec:MEMORY-IDEAL line 288: “no informative prior.” Likelihood is taught at line 11; a prior distribution is not taught in the earlier reading path or glossary.

Deletion test: these qualifications matter. Previous knowledge that narrows likely memory values changes the estimation problem and the total-error decomposition. Keep the qualification and explain at the first use that a prior represents knowledge about likely parameter values before seeing the observed spikes. One sentence suffices; this does not require a Bayesian-estimation chapter. Priority: medium.

### N4: “innovation” has an untaught specialist meaning

Locations checked individually: `02-memory-dynamics.md` line 179, “independent spike innovations”; line 314, “Spike innovations” and “correlated innovations”; `03-memory-information.md` line 421, “replace Poisson innovations.” Earlier dynamics lines 41–58 already explain the new spike-count fluctuation dM_i and its Brownian approximation, but never connect it to “innovation.” In ordinary speech innovation means a new idea, so its meaning as newly generated randomness is not supplied by word familiarity.

Deletion test: the fluctuation is essential; the extra technical label is not needed to follow the covariance projection or Gaussian comparison. Either define “innovation” once where dM_i is introduced, or use direct descriptions at these separately reviewed occurrences: newly generated spike-count fluctuations at 179/314, an extra source of correlated fluctuations at 314, and Poisson spike-count fluctuations at 421. Do not automatically replace the word outside these passages. Priority: medium.

### N5: closed-form readout functions need usable definitions

`03-memory-information.md`, sec:MEMORY-IDEAL, lines 313–334: artanh first appears at line 318, tanh at 324, and coth at 329. Line 332 defines coth through cosh and sinh, which themselves have not been introduced. The recorded baseline does not explicitly include hyperbolic functions.

Deletion test: these functions express the paper's closed-form curve and its limits, so do not delete the curve or rename its standard functions. Supply a compact exponential definition, for example tanh z=(e^z-e^-z)/(e^z+e^-z), identify artanh as its inverse on (-1,1), and write coth z=1/tanh z. Alternatively make an explicit supported audience-baseline decision that these functions are assumed. The former adds only the meanings needed for the reader to evaluate the derived curve and understand why it approaches its limit. Priority: medium.

### N6: “sparse projection” changes the meaning of projection without explanation

`03-memory-information.md`, sec:MEMORY-PARTIAL, line 379, example label “a sparse projection changes the useful interval.” Earlier projection means the linear operation extracting a surviving memory coordinate. Here it means limited biological connections or access to a fraction of spikes, as explained at lines 360–377. The word's two roles are not mapped.

Deletion test: the example must remain because it separates observation cost from unchanged storage diffusion. Its biological label adds no required meaning. Propose the label “Example: limited spike access changes the useful interval.” This keeps the actual experimental/model choice visible and avoids introducing a second technical meaning for projection. This is a proposed local label change, not an edit or request for general title changes. Priority: low.

### N7: remove the previous-task history from the reading guide

`00-reading-guide.md`, sec:READING-PAPERS, line 13: “The 2025 supplement was unavailable during the earlier overview task and was retrieved for this guide.”

Deletion test with the surrounding paragraph and the three paper links: removing this sentence leaves the reader with the same published copies, supplement access, page locators, and source limits. No mathematical premise, definition, limit, or navigation choice is lost. The earlier overview is work history the reader does not need. Remove this sentence; keep availability/history in project evidence. Priority: low.

## Retained passages and deletion-test reasons

These decisions cover the full current reading path, including equations, notes, example labels and the final foundations caption/alt. Standard calculus/linear-algebra notation is not expanded merely because it is mathematical. Footnotes remain lookup/source records, with a shorter form justified by their role after the main explanation.

| Passage | Decision and concrete reader need |
|---|---|
| 00 opening and sec:READING-START, lines 3–9 | Retain the audience and two paths: removing them leaves place-field readers unable to tell which memory material is required. “Gaussian process” here is a route label, not a dependent calculation; full teaching belongs in its chapter. |
| 00 sec:READING-PAPERS, lines 13–19 | Retain paper names, accessible source links, main-versus-SI distinction, page-layout caveats and the independent-correction qualifier. They let readers check formulas and distinguish printed source errors from guide changes. Only the task-history sentence fails the deletion test, N7. |
| 00 sec:READING-SCOPE, lines 23–27 | Retain reconstruction versus empirical reproduction and D/d/theta/q conventions: deleting them merges claims the guide carefully keeps separate. |
| 01 opening, lines 3–5 | Retain the physical examples and activity-versus-value distinction; neither sentence simply restates the title, and the later two-direction example needs this question. |
| 01 sec:FOUNDATIONS-SPIKES, lines 9–25 | Retain spikes, rates, synapses, recurrence, tuning, coding, place fields/maps and grid-cell distinctions. These terms have immediate roles in the model; positive-rate limits and occupancy corrections prevent wrong inferences. Anatomy gives the later CA1 discussion a setting without requiring a separate anatomy lesson. |
| 01 sec:FOUNDATIONS-POISSON and COUNT-EXAMPLE, lines 29–62 | Retain count moments, silent-cell example and population comparison: the examples distinguish zero observed spikes from zero rate and independent from shared variation. “Factorial moments” is followed immediately by the exact quantities summed, so its meaning is supplied by the operations; no extra definition section is needed. “Homogeneous” refers back to the constant-rate setup; replacing it with constant-rate would be optional polishing rather than a necessary finding. |
| 01 sec:FOUNDATIONS-COVARIANCE, lines 66–99 | Retain covariance, correlation, units and MSD decomposition. Each has a distinct later role; the warning about correlation versus variance fraction is a necessary limit, not filler. |
| 01 sec:FOUNDATIONS-ATTRACTOR and ATTRACTOR-EXAMPLE, lines 103–143 | Retain fixed point, neutral direction, manifold and the two perturbations. Removing either disturbance loses the difference between stable activity and correct value. The dashed/solid-arrow explanation is needed because the arrows represent different actions. |
| 01 sec:FOUNDATIONS-DIFFUSION and DIFFUSION-EXAMPLE, lines 147–194 | Retain increments, Brownian motion, D convention, bias comparison, min(s,t) covariance and finite-range limits. The 4-second crossover and shared-increment proof do more than substitute into a formula. The stationary-noise phrase at 192 is a preview, not used as a premise here; its later teaching is not required to complete this calculation. |
| 01 sec:FOUNDATIONS-RANDOMNESS, lines 198–200 | Retain: the two random objects index different variables. Without this distinction readers could mistake static irregular fields for temporal memory drift. |
| 02 opening and sec:MEMORY-SPIKES, lines 3–71 | Retain theta/Theta, activation units, jump/decay, transfer function and n-scaling. The Gaussian-versus-individual-spike qualification prevents applying the approximation to the wrong object. “Gaussian process” in that negative scope sentence does not need a full spatial-GP introduction here; its immediate meaning is Gaussian noise evolving in time. Preferred angle needs N2. |
| 02 sec:MEMORY-LINEARIZATION, lines 75–144 | Retain both left/right definitions, normalization, stable-mode calculation and tilted example. The example supplies a case where ordinary perpendicular projection fails, so it is not a decorative repeat of the algebra. Tangent, transpose, vector and eigenvector are within the declared undergraduate baseline and are tied to their actual roles. |
| 02 sec:MEMORY-DIFFUSION, lines 148–179 | Retain covariance projection, cellwise interpretation, validity interval and tensor extension. The tensor's purpose and off-diagonal meaning are explained; its exact name is needed to read the source's multidimensional result. Innovation needs N4. |
| 02 sec:MEMORY-SYMMETRIC, lines 183–231 | Retain symmetry calculation, normalization, source-square warning, two-cell example and boundary qualification. The example shows varying rates with constant D, distinct from the tilted example. The independent-correction qualifier remains useful beside the actual source difference even though the reading guide gives a general warning. |
| 02 sec:MEMORY-LONG-TIME, lines 235–302 | Retain the new test-function derivation, wrapped density, moment argument and mutual-excitation example. They distinguish short-time local variance, bounded long-time variance and state-dependent linear variance growth. No deletion preserves all three distinctions. Definitions need N1. |
| 02 sec:MEMORY-DRIFT-SCOPE, lines 306–314 | Retain mean drift, convention sensitivity, N scaling and correlated-noise limits. The limits are needed before treating the Poisson formula as biological law. Define the stochastic names at their uses, N1, and resolve innovation, N4. |
| 02 sec:MEMORY-FIGURES, lines 318–328 | Retain concrete figure-reading instructions and simulation-versus-animal distinction; these map source graphics to already derived quantities. Bump/preferred-angle/sigmoidal need N2. |
| 03 opening and sec:MEMORY-FI, lines 3–64 | Retain T/L distinction, likelihood, score, Fisher rate, unbiasedness and the CR calculation. The terms are defined by their roles before use, apart from prior, N3. “Efficient estimation can approach the bound” explains its intended statistical role through the following action; defining the adjective separately would add more than it helps. |
| 03 sec:MEMORY-BOUND, lines 68–166 | Retain scalar proof, exact equality, exponential sufficiency, linear-family counterexample, strict inequality example and matrix proof. The two examples answer different questions: the first refutes unrestricted necessity across states; the second separates information growth from actual diffusion at a fixed model. Standard positive-semidefinite comparison is defined directly by its quadratic form, so no extra terminology is needed. |
| 03 sec:MEMORY-COMPARISONS, lines 170–201 | Retain held-quantity caveats, width integral and firing-budget alternative. Deleting the alternatives turns conditional scaling into a universal promise. Sensory/internal curve matching is necessary to explain the paper's colocation suggestion. |
| 03 sec:MEMORY-READOUT-SETUP, lines 205–227 | Retain Gaussian observation representation, storage/readout split and its limitations. “Translation invariant” summarizes the immediately stated unbounded, constant-statistics setting; defining the shift interpretation would be optional here, while prior itself needs N3. |
| 03 sec:MEMORY-NAIVE, lines 231–280 | Retain equal-weight mean, covariance integral and derivative: removing any loses why more samples can increase error. “Naive” denotes the explicitly introduced static-state assumption, rather than a judgment about the reader. |
| 03 sec:MEMORY-IDEAL, lines 284–356 | Retain precision, independent-likelihood multiplication, backward variance addition and differential equation. These let the reader derive the readout curve without assuming Kalman filtering. Keep characteristic-time and variance/SD qualifications. Supply hyperbolic meanings, N5. |
| 03 sec:MEMORY-PARTIAL, lines 360–381 | Retain thinning calculation, unchanged D, biased-subset caveat and numerical delay comparison. These distinguish information access from noise creation. Change only the ambiguous example label, N6. |
| 03 sec:MEMORY-EXTENSIONS, lines 385–429 | Retain two-block derivation, q normalization and sufficient-class comparison. The 2-timescale and Gaussian cases answer source questions not already answered by the base model. Resolve innovation at 421, N4. |
| 03 sec:MEMORY-FIG3-AND-CAUTION, lines 433–456 | Retain rescaled figure reading, inequality-direction chain, strict numeric example and integrator-versus-readout distinction. Deleting the strict example could leave readers thinking the printed bound is correct whenever equality is not assumed. The author-correction qualifier is relevant beside this particular discrepancy. |
| 01 footnotes 202–210, 02 footnotes 330–343, 03 footnotes 458–477 | Retain source details, exact locations and reconstruction qualifiers as reference records. They need not teach source-only names such as reverse Kalman filter because the body supplies a different self-contained derivation. Full repeated citation fields are a citation-format decision, not unnecessary mathematical teaching. |
| 01-foundations.yaml, fig:FOUNDATIONS-ATTRACTOR | Retain caption's distinction between imposed disturbance and recovery. Alt text describes required coordinates but joins words/numbers, for example “and30” and “to6.5degrees”; restore spaces for intelligible alternative text. This is a direct accessibility correction, not a new term or math change. |

## Glossary decisions

Read all 64 entries, lines 5–68. Retain the short lookup form: they follow the full teaching and do not need examples or artificial transitions. Exact established names such as Fisher information, Fokker Planck, Betti numbers and Kac–Rice belong because readers need to match the paper and body; plain paraphrases in their definitions explain their roles.

The neural terms at 5–6,12,17,23,25–26,29,40–46,48,50–51,56–57,62–64 carry distinct objects or functions and should not be merged just to shorten the list. The probability/estimation entries at 8,10–11,14–16,22,24,32,35–37,47,49,52–55,60,65–66,68 preserve the difference between covariance/correlation, count/interval variability, likelihood/score/information, and left/right vectors. The dynamics/filter entries at 9,13,18–19,27,31,38–39,54,58,61,63 are useful lookup names for separate mechanisms. The spatial entries at 7,20–21,28,30,33–34,59,67 are relevant to the other paper and need not be removed because this review's core derivation is about memory.

No blanket glossary synonym changes are proposed. Stationary process and Stationarity provide a general and spatial lookup route; merging them is optional, not required. If N1/N3 introduce Itô, Stratonovich, Dirac delta or prior as technical terms, their lookup entries should match the body spelling and concise meanings. If direct ordinary descriptions replace an unnecessary label, no extra glossary entry is needed.

## Verdict and limits

Stage 2 changes are limited to the specific first-use gaps, the ambiguous example label, the prior-task history sentence, and spaces in final alt text. Retain the derivations, limits, examples and source warnings above. A broad prose rewrite or global substitution is not justified. Stage 3 understanding/flow is not performed in this call. Stage 2 remains pending local decisions/repairs and an affected recheck.
