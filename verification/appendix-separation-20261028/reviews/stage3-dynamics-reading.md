# Stage 3: reader understanding and flow, dynamics and reading guide

Local request ID: stage3-dynamics-reading-20261028-170252. Reviewer: separate_readout, Sol high, independent of these files' authors. Started 2026-10-28T17:02:52.562103+02:00; completed 2026-10-28T17:04:38.020465+02:00. Separate call after Stages 1 and 2. Read-only review; no source edits.

Audience: undergraduate calculus, probability and linear algebra, without assumed neuroscience. Checked actual earlier explanations of spikes, rates, synapses, tuning, conditional independence, continuous attractors and Brownian spreading in `01-foundations.md` and `01b-persistence.md` rather than supplying them from neuroscience knowledge. Scope is the changed dynamics reading path, the new reading-guide role guidance and appendix table, plus a narrow check of the added model-equation clarification. This is not whole-book acceptance.

## Required repair: identify the scalar result after the multi-coordinate equation

Location: `02-memory-dynamics.md`, MEMORY-DIFFUSION, line 203 in the reviewed version.

Old:

> **Interpretation.** Each neuron's contribution combines its spike variability, $\bar r_i$, with the squared effect of one activation fluctuation on the final memory, $v_i^2$.

Required replacement:

> **Interpretation.** For one memory coordinate, each neuron's contribution combines its spike variability, $\bar r_i$, with the squared effect of one activation fluctuation on the final memory, $v_i^2$.

The immediately preceding displayed result is now `2D_{alpha beta} = sum_i v_i^alpha r_i v_i^beta`. Its off-diagonal contributions are products of two coordinate effects, rather than a square. The unchanged interpretation's bare “Each neuron's contribution” and following “The formula” therefore attach naturally to the nearest multi-coordinate result. The new clause points back to the scalar result whose squared weights the paragraph actually explains. Keep the rest of the paragraph unchanged. This is a newly introduced referent problem from the move, even though an expert can infer the intended scalar meaning.

The proposed repair keeps the correct mathematics and every qualification; it needs only a connected recheck of the scalar result, multi-coordinate result, repaired interpretation and later tensor explanation.

## Connected reading judgments

- **Entry and spike renewal:** earlier chapters supply firing rate, synapse, recurrent connectivity and conditional Poisson variability. The chapter opening supplies theta, initial value, tau and the diffusion convention. The new mechanism paragraph explains the feedback cycle before the count/decay representation; formal input weights, transfer rule, count fluctuations, Gaussian approximation, population limit and steady-state equation then appear in a usable order. The final balance interpretation answers how recurrent activity offsets decay and keeps tuning explicit.
- **Lasting displacement:** the mechanism poses the difference between temporary perturbation and retained displacement before the mathematics. Linearization is defined before the state expansion; the tangent derives from the steady-state family, left-vector normalization extracts the coordinate displacement, and stable-mode removal explains the projection. The tilted-return example then makes the difference from perpendicular projection concrete. No new reader prerequisite was moved after its use.
- **Diffusion:** the next mechanism paragraph connects the preceding lasting shift to random spike generation. General weighted variance addition then maps to v and yields scalar D. Several coordinates extend the same covariance calculation using already introduced tangent and left-zero-vector roles. Apart from the scalar-interpretation referent above, the extension is understandable: the later diffusion-tensor paragraph defines the matrix and diagonal/cross-coordinate meanings. Moving that definition again is not required to understand an intervening derivation, since no additional derivation depends on an unexplained property of the tensor.
- **Symmetric weights:** equal reciprocal connections are explained before the special-case calculation. The chain rule connects the input/rate slopes; the left-vector identity supplies the formula; the interpretation, assumptions and mutually inhibitory example explain the result's use and limits. The previous general local-noise conditions are retained. The section does not promise that symmetry alone provides the attractor or that higher rates alone imply worse memory.
- **Frontmatter guidance:** the three roles tell the reader which question each passage answers. The new two-sentence variant, “An equation that specifies how a cell responds belongs to the model. A derivation works out what follows from that choice,” is correct and sufficient. It gives a concrete role boundary before the spike example without implying that model assumptions must avoid equations. Its actor, object and consequence are clear and it adds no new mathematical prerequisite. This narrow new-text check passes correctness, necessity and wording.
- **Conceptual first pass:** “inspect the displayed result and its variables” asks the reader to consult the symbols' explanations rather than promising that all details can be skipped. Reading the mechanism and interpretation gives a qualitative account; the following instruction reserves understanding why the result holds and calculating with it for the derivation. “Assumptions remain part of both readings” preserves the model limits. It does not promise independent numerical use after reading only the neural opening.
- **Appendix map:** the plain neural questions make the technical source headings usable for a reader new to neuroscience. Seven source sections map to actual explanation locations, and the introduction says equivalent teaching derivations are sometimes used, so it does not promise complete equation-by-equation reconstruction. It distinguishes ideal readout as an inference benchmark from biological implementation. Source-page and guide-link checks from Stage 1 remain current because table bytes are unchanged.

## Current reviewed hashes

- `02-memory-dynamics.md`: `837c4b2490bee22b449b75db2d0d575ec639dddf2e4583797fff46a302963607`
- `00-reading-guide.md`: `95ab3465e87b7f67635aa9e43d478f3b1b4cbe18f30a12ba7917b045ef2f0262`
- `00-reading-guide.yaml`: `7ee74d6dfe7e8c88a63a258a351a6e01a574ff3eb99fd242503dee6da010687e`

Status: one required referent repair remains open. Other changed passages pass this local understanding/flow review. No manuscript edits, HTML rebuild, browser test or visual sweep performed.

Checkpoint 2026-10-28T17:04:38.020465+02:00: wall elapsed since review start 105.5 seconds; time since previous command checkpoint 53.3 seconds. Awake execution unverified; no clock change established. Token stats unavailable.
