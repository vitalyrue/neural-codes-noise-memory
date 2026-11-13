# Initial local reader and figure assessment

Recorded: 2026-10-24T18:07:45+03:00. Root start: 2026-10-24T18:06:16.7630300+03:00. Wall-clock elapsed about 1 minute 28 seconds. Awake execution time is unverified. Token stats unavailable.

Reviewer: GPT 6.1 sol, high reasoning. Scope: actual Chapter 2 Markdown and sidecar, plus the existing tilted-decay PNG. Audience: calculus, basic probability and linear algebra; no expert neuroscience knowledge. This is a neutral initial assessment, not acceptance of later text or artwork.

## What is already present

The chapter follows spikes to synaptic activation, the surviving part of a perturbation, the diffusion formula, symmetric weights, and long-time error. The equations have accompanying explanations and useful limits. The tilted-decay plot already explains the hardest geometric distinction: an initially vertical jump can leave a horizontal shift because the decaying motion is tilted. The actual image shows the imposed jump, the flow, fixed-point line, tangent and final shift. Preserve this example; another attractor projection picture would add little.

The current sidecar has one figure and an empty source_loci list. Footnotes give the DOI and paper page/equation ranges, but the reader cannot jump to the specific supporting passage. These page/equation references are useful foundations for precise links.

## Three useful additions

1. **Spikes and synaptic activation, near the first two equations (Markdown lines 11–22).** Align a few illustrative spike marks with the sum of their exponentially decaying activations. Show each upward jump of one and the decay between jumps; label time in units of tau or give an explicit tau. This connects the count process to the smooth-looking state without assuming previous neuroscience knowledge. Say that the spike times are chosen for illustration and that this is a guide construction, not a recorded neural trace. The paper-model claims currently point to main equations 7–9 and SI Section I; the exact supporting equation must be inspected before the new link is accepted.

2. **Random spread across trials, after the boxed diffusion result (around lines 173–181).** Show several sample memory-coordinate traces starting at the same value, with a companion density or spread view at two times. State that the ensemble mean remains at the start in the constant-D, zero-drift model and that variance is 2Dt; do not make the sample mean of a few traces look identically zero. Label the simulation as a direct illustration of the reduced diffusion equation, not a simulation of the paper network. The teaching question is why continuing activity can coexist with increasing memory uncertainty. The source connection is SI S10–S15 for the projection and S28–S32 for the density description; exact pages and passages need source checks.

3. **Unbounded versus wrapped error, in the long-delay section after the Gaussian and ring explanation (around lines 272–289).** Compare the same diffusion on a line with its reported angular error on a ring. A plot of mean squared error can show initial slope 2D and the ring limit pi squared over 3. A companion wrapped density can show what flattening means. Keep the convention [-pi, pi) visibly attached to the saturation value, and do not imply that noise stops. This adds distinct teaching beyond the existing tilted-decay plot and prepares the later explanation of Fig. 2D. Source connection: SI S28–S32 and main Fig. 2D, after checking the actual source.

These are ranked by the new connection each supplies. The two-cell rate curves would also be useful, but are less urgent than showing what a spike does and what diffusion means over repeated trials.

## How precise source links should work

- Put a short linked paper locator beside the supported claim, caption or derivation, keeping the complete reference footnote.
- Use the local supplied PDF with the correct PDF page fragment as a dependable page-level fallback. Distinguish PDF page index from the paper's printed page number in the records.
- Papers do not provide durable numbered text lines. For an actual passage-level jump, create a small source-passage view with fixed anchors, the exact page/equation/figure locator, and a short quotation or a clearly labelled page crop of the original passage. Link onward to the original local PDF page. Keep source text distinct from the guide's explanation.
- Record the source file hash, printed page, PDF page, exact start/end text or crop box, and anchor in the project evidence. Inspect the original PDF passage and click the resulting link in the browser. Do not describe an extracted-text line number as the paper's original line number.
- Use separate links when the main paper and supplement support different parts. In particular, retain the visible cautions around main Eq. 2 and SI S40; a source link is evidence to inspect, not proof that the printed formula agrees with the guide.

## Review limits and next stage

Read: course-study-guide-builder SKILL, pedagogy-language contract, visual-integration contract, reference-citation contract; course-diagram-builder SKILL, visual-qa and review-acceptance. No reader files were edited. No whole-book audit or paper-claim approval was performed. The recommendations above identify where plots help, but do not approve later plot parameters, source snippets, captions, links, palette or display-width readability. Those require the actual draft and final pixels in separate truth, wording and connected-flow review calls.
