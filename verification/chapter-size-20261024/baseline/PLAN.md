# Teaching guide plan

Task start: 2026-10-22T19:06:07.5341124+03:00.
User request: Use course-study-guide-builder to turn the prior research overview into a proper guide for all three papers, with the needed background and step-by-step derivations.

## Audience and scope

Assume undergraduate calculus, probability basics, and linear algebra. Do not assume neuroscience, stochastic-process theory, Fisher information, Gaussian random-field geometry, neural decoding, or motor control. Teach those meanings before their dependent use. The reader should be able to reconstruct the central calculations and interpret the paper figures, not merely repeat the abstracts.

The output is an editable Publisher project and local HTML guide. No DOCX/PDF or public deployment is requested. Preserve the original overview and downloaded papers. Do not modify Publisher or shared skills. Source code listings are optional; use them only when they add understanding and run any included listing. Use numerical checks for concrete claims and limiting cases. No full experimental reproduction is required or implied.

## Structure and work owners

1. `ch:FOUNDATIONS`, `01-foundations.md` (root): spikes, synapses, tuning, rate maps, conditional Poisson variability, variance and covariance, fixed points, attractor geometry, diffusion, temporal versus spatial randomness.
2. `ch:MEMORY-DYNAMICS`, `02-memory-dynamics.md` (memory writer): synaptic jump/decay dynamics; deterministic mean; fixed-point tuning; linearization; left/right neutral directions; projection of noise and diffusion; symmetric-weight special case.
3. `ch:MEMORY-INFORMATION`, `03-memory-information.md` (memory writer): Poisson Fisher information derived from likelihood; Cramer-Rao meaning; Cauchy-Schwarz information-diffusion bound; equality conditions; neuron/rate/tuning/time-scale comparisons; ideal/naive readout derivations; partial readout; apparent printed inequality issue.
4. `ch:EYE-DRIFT`, `04-eye-drift.md` (eye writer): fixation and motor pathway; actual reused experiment; forward position/velocity/acceleration fit; inverse filter; covariance estimate and its assumptions; measurement-noise MSD correction; filtered white noise versus filtered Brownian input; integrator/motor/muscle/feedback model; evidence and limits.
5. `ch:PLACE-FIELDS`, `05-place-fields.md` (place writer): spatial GP and covariance; thresholding; stationarity/isotropy/smoothness; Kac-Rice upcrossing derivation; field length and gap relations; rare-peak derivation of dimensional size law; slices, field counts, shape/peak-rate/slope predictions; Euler characteristic meaning and formulas with derivation scope clear; parameter inference and processing; limits of random-wiring inference.
6. `ch:SYNTHESIS`, `06-synthesis.md` (root): connect the models without confusing static maps and dynamics; experimental support versus model prediction; related work with specific comparisons; focused next calculations and open questions.
7. `ch:GLOSSARY`, `glossary.md` (root): first-use terms and concise definitions with identical spelling.
8. `ch:REFERENCES`, `references.md` (root): numbered full references, last and unlettered.

Each main chapter should contain connected explanations, all intermediate steps needed for its central results, at least one concrete example that exposes a real distinction or limitation, and figure-reading guidance tied to exact paper figures. Prefer a few useful examples over formula substitution exercises. Reader exercises are optional and would need answers. Do not pad chapters to an arbitrary word count.

## Shared notation and references

- D is a one-dimensional diffusion coefficient; MSD = 2 D t. d is spatial dimension. State conventions before converting from other papers.
- theta is a memory coordinate in chapters 2-3. In chapter 5 use q for normalized threshold and explain that the paper writes theta. Use C for GP covariance and sigma for correlation length. x is a physical spatial coordinate.
- tau is the common synaptic time constant in the basic 2012 model; T is storage delay; L is the recall observation interval. Do not confuse readout duration with memory lifetime.
- P1 is Burak-Fiete 2012; P1SI is its supplement. P2 is Ben-Shushan et al.2022; P2SI is supplementary notes; P2REV is open peer review. P3 is Mainali et al.2025. Page source IDs are `P1-p01`, `P1SI-p01`, etc., padded to two digits.
- Cite specific equations/figures/sections with each consequential result. Use Markdown footnotes with globally unique labels, such as `[^p1-diffusion]`. Each footnote includes full source details and DOI plus its locator. Root consolidates the final reference list.
- First teaching occurrence uses `[**term**]{.definition-term custom-style="Definition Term"}`. Root owns shared foundational terms; paper writers mark only terms first introduced in their own chapters, and supply a term list for glossary integration.
- Use `$$` display math and `$` inline math; outputs must render mathematics. Use descriptive headings with stable explicit IDs. Keep exact paper titles in citations.
- Computational or geometric derivations reconstructed for teaching must say so. An inaccessible supplement does not become a directly checked source because its formula is repeated elsewhere.

## Evidence and review

Original files and extracted text are in `../papers`, `../notes`, and `../research`. These notes are leads, not replacements for the source. Reuse them to avoid repeating searches. Record source coverage in the paper's page order, even though guide order follows prerequisites. Each page gets a final disposition and actual heading-level explanation location; nonteaching title, references, disclosures, or duplicated pages may be intentionally omitted or consolidated with a reason. Supplemental derivations that matter to the requested explanation must be taught, or a concrete access/verification limit recorded.

Each writer owns only its assigned chapter files and a writer evidence file in `verification/writers/`; do not edit shared plans, global ledgers, configuration, or other authors' files. Include a compact source-page map, terms introduced, equations/claims and how checked, source/access limits, needed earlier concepts, and numerical-check evidence. Root integrates those records.

After drafting, freeze files for independent staged reviews: (1) truth and reasoning, (2) necessity and terminology, (3) reader understanding and flow. Request stages in separate sequential calls for each connected scope; independent scopes may run in parallel. A writer cannot accept its own chapter. Reviewers inspect actual source passages and earlier teaching, with section/paragraph locations and source/rule hashes. Root integrates book-level dependencies and chapter handoffs. Repairs receive affected rechecks. Full original paper derivations and guide reconstructions remain distinct.

HTML checks: local links and IDs, footnotes, representative equations, navigation, and representative desktop/narrow views. No exhaustive visual sweep. Semantic reading covers the full guide text. Publisher build/validation does not establish teaching quality. Dirty/unpinned installed tooling is staging-only and must be reported as such if present.

## Timing and checkpoints

Use measured ISO timestamps with offsets. Preserve start and successive checkpoints across interruptions. Report wall time separately from awake execution; do not infer awake duration without evidence. Initial estimate 60-90 minutes, revised as work resolves. Reading/math agents use GPT-6.1-sol/high; use scripts for deterministic inventory and checks. Subagents send a brief status every few minutes and at completion, with measured time. No further subagents without coordination. Token stats unavailable unless the tool actually exposes them.
