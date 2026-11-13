# Eye and place changes: independent connected-reader stage 3

Reviewer: `/root/context_memory`. Local request ID: `eye-place-stage3-20261028` (not a platform call ID). Start checkpoint: 2026-10-28 15:43:37.949 +02:00. No manuscript edits. This is the separate reader-understanding and flow call, following the recorded truth and wording calls.

**Required connected-reader repairs: none found.**

Read `04-eye-drift.md` from its opening through the pathway, revised recording setup, calibration purpose, figure introduction and interpretation, and first fitted equation with units. Read `04c-eye-circuit.md` from its opening through the revised two-group setup, recurrence and persistence equations, motor and muscle stages, revised visual-feedback setup, sign explanation and feedback limits. Read `05-place-fields.md` from its revised opening through the Gaussian-process definition, assumptions, normalized threshold rule, field definition, local spatial scale and input-to-rate figure interpretation. Also read the related YAML figure captions and alt text. This scope includes preceding and following paragraphs; it does not claim a full reread of all three chapters.

The connected path lets the intended reader answer the needed questions without adding unseen neuroscience knowledge:

- **What was recorded, and why are larger movements involved?** The eye chapter first identifies the stored command, motor neurons and eye mechanics. The revised recording paragraph then puts one neuron's spikes beside one eye's angle in a concrete head-still task. The following selection paragraph states which samples enter the drift analysis. The next paragraph explains that larger movements calibrate the relation later applied during fixation. The pathway figure is introduced after these roles exist, and its surrounding text and caption distinguish a physical pathway from a later calculation. The fitted equation is motivated by position, movement and acceleration before its coefficients are interpreted. Retain this order.
- **What acts on what in the proposed circuit?** The model chapter first says that the recording result does not identify this particular circuit. Its two groups and the signs of their interactions are then stated before the rate equation. The revised synaptic paragraph provides a complete feedback cycle before the coupled equations: spikes, scaled input, persistent synaptic output, represented angle, changed rates. The next paragraph explains the modeled scaling and decay. The persistence calculation is then motivated as a further condition on this already introduced loop. Its conclusion preserves approximate tuning and residual drift. The following motor and muscle equations carry the represented angle into movement, so the reader need not invent a direct jump from stored angle to physical eye motion.
- **What does feedback respond to, and what can its delay establish?** The revised setup identifies the moving retinal image before the feedback equation. The next paragraph follows a rightward change through the sign of the position difference and resulting rate contribution. Its slow-change approximation has explicit conditions. The following figure discussion separates an ongoing process's time lag from the age of a new disturbance and limits the conclusion to the coupled model. The cited model figures support the explanation rather than supplying its first premise. Retain this sequence.
- **What do dimensions and the modeled input mean for place fields?** The revised opening names animal movement and its position coordinates before comparing field lengths, areas and volumes. The following observed variety motivates a common model. The input interpretation then gives the reader a biological object for the random function and separates it from measured rate estimates. The track/upcrossing preview states why threshold and spatial scale matter. The next paragraph prevents interpreting the map as a changing time signal. The first technical section motivates spatial dependence, then defines the random function and assumptions before normalization, thresholding and field geometry. The input-to-rate figure and its caption use the same positions and threshold rule and explicitly identify a simulated teaching map. Retain this order.

At the end of the connected read, the revised setting and object relationships still fit the adjacent paragraphs. No added context depends on an explanation supplied only by a later figure. The passages keep experimental evidence, a possible biological interpretation, model assumptions and calculated consequences separate.

This call does not re-audit mathematical proofs, reproduce experiments or inspect rendered figures. It does not approve the whole guide or later unreviewed connections. Current source hashes follow.

```text
A33A3A7FC25B234AE32B961F2404CAE223C6120C7CD8AA04E3EB85394388777B  C:\dev\clsc\burak-papers\guide\content\chapters\04-eye-drift.md
C6ADCF74E8B88789986AD18EEF462710C077B6CDFF146B5FA70070BED0B6F088  C:\dev\clsc\burak-papers\guide\content\chapters\04-eye-drift.yaml
75AE2098D255171990F67776A65676F7948D4E75B6D0D1F2AC044A208622874B  C:\dev\clsc\burak-papers\guide\content\chapters\04c-eye-circuit.md
5241516BAA09B0B96E5969AD688D0D8D486EC682601AA3FBC49D6F8F0A74C1FB  C:\dev\clsc\burak-papers\guide\content\chapters\05-place-fields.md
19EC82B79B842D2C178AD15137FCD917FA716787B83D745AAD8150D3D4660F96  C:\dev\clsc\burak-papers\guide\content\chapters\05-place-fields.yaml
F4C1EB544CF640B708E1970D9572FDC758FCC6AEA806675D01A0256658DF847A  C:\Users\vital\.codex\skills\course-study-guide-builder\references\pedagogy-language-contract.md
```
Completed: 2026-10-28T15:44:42.0492700+02:00. Wall elapsed since the initial checkpoint is about 1.1 minutes. Awake execution time is unverified. Token stats unavailable.

## Focused clarification requested after the connected read

At 15:44, the coordinator added the explicit criterion that a reader may arrive at the place chapter directly. Under that criterion, one local opening repair is required. This does not reverse the earlier judgment that the sequential reading path already teaches place cells and the hippocampus.

- Exact passage: `05-place-fields.md`, opening, line 3: “The recordings include bats flying through tunnels, rats moving over an arena floor, and bats flying through a room.”
- Missing local referent: the sentence identifies the animals and movement but does not identify the recorded cells. A direct-arrival reader has to infer that these are neural recordings of place cells, rather than only animal-position recordings. The chapter title names field statistics but does not supply that measurement relationship.
- Proposed exact replacement: “The study compares recordings of hippocampal place cells from bats flying through tunnels, rats moving over an arena floor, and bats flying through a room.”
- Source support: the main paper identifies hippocampal area CA1 as its subject and compares place-cell recordings in the tunnel, arena and room settings (main text around lines 118-153, 198-200; Fig. 2 and Fig. 4 descriptions). The added words identify the measured cells without claiming that inputs or connections were recorded.
- Scope of judgment: required for the newly explicit direct-arrival requirement; a supported local orientation improvement on the original sequential path. No repeated definition of hippocampus or place field is necessary here. Existing earlier definitions remain sufficient for those concepts.

The new criterion and recommendation are recorded separately to preserve the earlier completed reading judgment. No manuscript edit made. Current chapter hashes above still apply. Source check checkpoint: 2026-10-28 15:44:56.917 +02:00.
