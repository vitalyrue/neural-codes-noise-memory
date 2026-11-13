# Illustration plan for the three-paper teaching guide

Task started: 2026-10-23T21:43:30.3359267+03:00.
Scope: planning only. No artwork generation, guide changes, or publication is authorized by this plan. The recommendations below await the user's choice about production.

## Recommendation

Keep the existing Chapter 1 attractor diagram. Add eight figures in two batches: four figures that make central calculations visible, then an orientation map and three supporting geometry or pathway figures. Leave three further candidates optional. This gives each proposed figure one clear question to answer.

The drawings should use exact vector shapes and calculated curves. Generic brain illustrations and chapter decoration would add little here. Original paper data figures already have reading guidance in the chapters; a new schematic should not imitate experimental data.

The audience knows basic calculus, probability and linear algebra. A visual should appear after its essential terms have been taught, and before the calculation that becomes easier with it. Chapter numbers below refer to the current six main chapters.

## Proposed set and order

| ID | Chapter | Figure | Main question | Batch |
| --- | --- | --- | --- | --- |
| V01 | 1 | Two kinds of randomness, three paper questions | What changes with time, and what stays fixed across space? | 2 |
| V02 | 2 | A disturbance that slides while it decays | Why does the left zero vector determine lasting memory error? | 1 |
| V03 | 3 | Storage, observation and recall error | Why can more observation help an ideal reader but harm simple averaging? | 1 |
| V04 | 4 | From stored eye position to recorded movement | Which steps are physical, measured, inferred or proposed? | 2 |
| V05 | 4 | One filter, two different noise sources | Why does filtered white noise plateau while filtered wandering position keeps accumulating? | 1 |
| V06 | 5 | From a spatial curve to place fields and crossings | How do threshold crossings count fields, including an active left endpoint? | 1 |
| V07 | 5 | From peak height to length, area and volume | Why does changing dimension change the field-size law? | 2 |
| V08 | 5 | Fields, holes and threshold | When can Euler characteristic stand in for field count? | 2 |

Batch 1 has the largest immediate teaching value. Batch 2 supplies orientation and the remaining hard spatial ideas. These are recommendations, not eight mandatory additions regardless of layout.

The eight figure IDs use nine insertion points: V03's timeline and error curves belong at different stages of the derivation. Final numbering can treat those as two linked figures.

## V01. Two kinds of randomness, three paper questions

**Placement:** end of `sec:FOUNDATIONS-RANDOMNESS`, after the distinction between temporal fluctuations and a fixed spatial map. Link to it from the reading guide and Chapter 6 rather than repeat it.

**Picture:** three aligned lanes, with plain question labels and chapter references:

1. A stored value changes over time: a small wandering trace, then the question “How quickly is memory lost?” Chapters 2–3, Burak and Fiete 2012.
2. A stored eye-position command passes through muscles: a simple command-to-movement strip, then “Where does fixational drift come from?” Chapter 4, Ben-Shushan et al. 2022.
3. A fixed spatial map is evaluated as position changes: one irregular map with two visits to the same position, then “Why these field sizes and shapes?” Chapter 5, Mainali et al. 2025.

Keep the lanes separate. A bracket labeled “comparison in Chapter 6” can collect them. Do not draw a serial causal arrow from the 2012 memory model to the 2025 hippocampal map. The papers do not establish one shared circuit. The two visits should have the same expected rate, while any illustrated spike counts can differ.

**Caption lesson:** “The first two papers concern changes over time. The third models variation across space in a map that stays fixed once drawn.”

**Method and label:** original conceptual map, based on the guide's foundations distinction and the three paper questions. Any traces are illustrative and labeled as such. No Fisher information, Gaussian-process acronym, or filtering equation is introduced here.

**Size/access:** one full-width vector figure, three stacked lanes at narrow widths; readable labels without zoom. Alt text describes the time-versus-space distinction and the three questions, not only the boxes.

## V02. A disturbance that slides while it decays

**Placement:** `sec:MEMORY-LINEARIZATION`, immediately after the local example `dx/dt = a y`, `dy/dt = -lambda y`.

**Picture:** a horizontal line of fixed points `y=0`; a starting state on it; a vertical imposed disturbance to `(x0,y0)`; and its exact straight, tilted recovery to `(x0+a y0/lambda,0)`. Equal-time marks crowd toward the endpoint as the state slows. The path obeys `x=x0+(a/lambda)(y0-y)`. Add a faint perpendicular projection to `(x0,0)` as a geometric comparison, explicitly labeled “not the dynamical endpoint.” Use a small positive numerical ratio, for example `a/lambda=1/2`, with dimensionless teaching coordinates. Show the tangent `u=(1,0)` and label the lasting coordinate `v^T delta s = delta x+(a/lambda)delta y`. The left vector is a linear measurement of displacement, not a second trajectory.

**Caption lesson:** “A disturbance can move along the memory line while its decaying part disappears. The lasting shift follows the dynamics, not perpendicular projection.”

**Support/label:** exact solution of the Chapter 2 teaching system, illustrating the left/right zero-vector construction used in Burak and Fiete 2012, SI linearization and projection. Original guide construction, not a simulated paper network.

**Check before insertion:** trajectory and endpoint satisfy both differential equations; arrows distinguish the imposed disturbance from subsequent flow; `v^T u=1`; do not label a vertical disturbance as a stable eigenmode. This extends the existing Chapter 1 diagram, whose example has a simpler recovery direction.

**Size/access:** one 650–750 CSS-pixel-wide vector panel at desktop width; equations remain in adjacent text. Alt text states the initial and final coordinates and the nonzero lasting shift.

## V03. Storage, observation and recall error

**Placement:** the timeline goes in `sec:MEMORY-READOUT-SETUP`, after storage error and cue-state error are defined. The curve panel goes in `sec:MEMORY-FIG3-AND-CAUTION`, after both readout derivations. They are two linked panels with separate placements, so the opening does not reveal unexplained formulas.

**Picture A:** a timeline from encoding at 0 to recall cue at T to observation ending at T+L. Distinguish the original value, the wandering value at the cue, and the estimate made using later observations. Mark storage error and readout error separately. Print `V_total = 2DT + V_read(L)` with the nearby text's zero-cross-covariance conditions. An illustrative trajectory is explicitly one possible path.

**Picture B:** plot the calculated dimensionless readout curves against `z=L sqrt(2DJ)`. The vertical axis is `V_read/sqrt(2D/J)`. Show the ideal curve `coth(z)` approaching 1 and simple averaging `z/3+1/z`, with its minimum at `(sqrt(3),2/sqrt(3))`. Use a broken-axis-free range that displays both the minimum and the later rise. State that both curves diverge as z approaches zero; start the numerical plot at a positive value.

**Caption lesson:** “Later spikes reduce count noise, but they also describe a memory that has moved. Simple averaging eventually becomes worse; ideal readout reaches a limit.”

**Support/label:** analytic reconstruction from the chapter's derivations and Burak and Fiete 2012, Fig. 3, SI Eqs. S75 and S79–S81. Not digitized data. The source's printed equation-locator and bound-direction issues are already explained in the text; use the checked guide formulas.

**Check before insertion:** derivatives give the printed minimum; ideal curve stays at or above 1 and below the simple-averaging curve; storage variance `2DT` is absent from the readout-only plot. Do not invent an ideal-observer weighting kernel or imply that later observation reverses earlier storage error.

**Size/access:** timeline full width; plot about 650 CSS pixels wide. Alt text gives the temporal ordering, the two curve limits and the averaging minimum.

## V04. From stored eye position to recorded movement

**Placement:** end of `sec:EYE-RECORDINGS`, once the pathway and the one-cell recording design are defined. Refer back to it during inverse filtering and shared-variance analysis.

**Picture:** a small mechanism strip: proposed storage circuit → population of motor neurons → muscles and eye mechanics → physical eye position. Attach a shared-input marker before the motor population, private spike variability at individual neurons, and downstream physical variability after them. Put measurement noise on a separate branch into the recorded eye-position signal, not into the physical eye. Label the attractor storage mechanism “proposed source.”

A separate observation strip shows one recorded neuron and recorded eye position, paired during a recording. Mark “one neuron at a time”; do not depict a simultaneously recorded population. An analysis arrow, with its own line style and legend, leads from the single-neuron recording through the calibrated filter to predicted eye position. This arrow is a calculation, not backward biological causation. Keep the detailed filter formula in its later section.

**Caption lesson:** “The recordings pair one motor neuron with eye movement. Shared-input inference and the proposed storage mechanism are later steps in the argument.”

**Support/label:** original schematic based on the chapter's recording description and Ben-Shushan et al. 2022, Figs. 1–2 and 4–5. Biological labels must agree with `sec:EYE-PATHWAY`; the diagram is not a complete anatomical wiring map.

**Check before insertion:** measured versus proposed labels remain visible; physical and analysis arrows have distinct meanings; no direct motor-neuron pair covariance is implied. Avoid a feedback loop here because the delayed-feedback model is introduced later and has additional terms.

**Size/access:** two simple stacked strips rather than a wide anatomy drawing. Alt text follows physical flow first, then lists the two recorded signals and the analysis operation.

## V05. One filter, two different noise sources

**Placement:** `sec:EYE-FILTERED-MSD`, after the one-pole MSD derivation and before the qualification about the paper's fuller model.

**Picture:** two small input → identical one-pole filter → position strips above paired theoretical MSD plots. Compare stationary white input and Brownian stored position. Define dimensionless lag `x=lag/tau`. Each curve uses its own explicitly printed normalization: `1-exp(-x)` versus `x-1+exp(-x)`. Label “plateaus” and “continues growing” on the curves. An optional small slope strip shows transitions 1→0 and 2→1; omit it if the main curves already make the contrast clear.

**Caption lesson:** “Filtering can smooth a wandering position while preserving its long-lag growth. Filtering stationary white input instead produces a plateau.”

**Support/label:** guide calculation for the one-pole teaching model; not the paper's fitted curves or measured data. Connect to Ben-Shushan et al. 2022, Fig. 3 and main Eqs. 20–22 through the existing chapter discussion. The diagram's white input is an idealized process; do not draw it as an ordinary finite-variance function value at each instant.

**Check before insertion:** plotted formulas have their stated short- and long-lag limits; own-scale normalization does not imply equal physical noise amplitudes; do not transfer the one-pole white-input short-lag slope to the paper's double-exponential muscle model. The two inputs are alternative hypotheses at the filter input, not white velocity versus Brownian velocity.

**Size/access:** two aligned panels with matched lag axes; stacked when needed. Alt text explains plateau versus continued growth and the different normalizations.

## V06. From a spatial curve to place fields and crossings

**Placement:** `sec:PLACE-KAC-RICE`, after the thin-band explanation and before its integral. Refer back from `sec:PLACE-INFERENCE`.

**Picture:** one smooth constructed curve `z(x)` with threshold q and shaded above-threshold intervals. The left edge begins inside an active interval. Mark the two upcrossings of two later complete fields, an example field length, and a gap. In a separate magnified inset, compare two positive crossing slopes through the band `q±epsilon`. Their horizontal widths are `2epsilon/v`; weighting by slope makes each crossing count once in the limiting integral. A small aligned strip may show the rectified expected firing rate, if it does not crowd the inset.

**Caption lesson:** “Each upcrossing starts a new field, but a field may already be active at the left boundary. The slope weight corrects how long a crossing spends near the threshold.”

**Support/label:** constructed curve for counting, not recorded data and not necessarily a GP sample. Mainali et al. 2025, Fig. 1A–B, Methods S3 Eqs. S11–S15, plus the guide's exact finite-track identity. Keep the identity `N_fields = N_upcrossings + 1{left endpoint active}` next to the drawing, before taking expectations.

**Check before insertion:** count connected active intervals, not peaks; show a clipped left field clearly; distinguish a deterministic count from its expectation and the probability `Q(q)` of an active endpoint. Do not apply the same count after silently excluding clipped fields. The slope inset must use nonzero positive crossings.

**Size/access:** a full-width curve with one uncrowded inset. Alt text enumerates the fields and crossings and explains why their counts differ by one in this example.

## V07. From peak height to length, area and volume

**Placement:** `sec:PLACE-SIZE-LAW`, after s, U and beta are defined, before the density change of variables. The parabolic peak was introduced in `sec:PLACE-RARE-PEAKS`; refer back to it.

**Picture:** a local high-peak parabola with threshold q, excess epsilon and radius `r_*`. Mark its full width as `2r_*`. Then show `U=q epsilon` and `r_*=(sqrt(2) sigma/q)sqrt(U)`. Branch to interval, disk and ball with sizes `2r_*`, `pi r_*^2`, `4pi r_*^3/3`. Finish with `U=beta s^(2/d)`, and the shape powers 2, 1 and 2/3. The exponential variable U is the shared starting point, not identical numerical field size across dimensions.

**Caption lesson:** “The same high-peak excess determines a radius. Converting that radius to length, area or volume changes the size distribution.”

**Support/label:** guide reconstruction of the high-threshold approximation; Mainali et al. 2025, main Eq. 1 and Methods S4. Use the corrected constants derived in the guide, including full 1D length, rather than copying the apparent supplement width error.

**Check before insertion:** length, area and volume have distinct units; the approximate round shape and exponential overshoot are high-threshold limits. Do not depict every observed field as spherical, or label the approximation exact at the fitted bat threshold. Probability-density curves are optional and should use dimensionless size divided by its own mean; the 3D divergent density has no point mass at zero.

**Size/access:** one top peak panel and three compact geometry panels beneath it. Alt text follows excess → radius → dimensional size and gives the three powers.

## V08. Fields, holes and threshold

**Placement:** `sec:PLACE-TOPOLOGY`, after the definitions of Euler characteristic and Betti numbers, before the Morse-theory calculation.

**Picture:** three or four increasing thresholds of exactly the same constructed smooth 2D map. Use active sets chosen to show a hole and a split. Below each print components, holes and `chi = components - holes`. A sparse inset with a solid ball, solid torus and hollow spherical shell can add the 3D counts 1, 0 and 2, but only if it remains readable; otherwise leave the 3D examples in prose.

**Caption lesson:** “Euler characteristic combines field connectivity and holes. It can represent field count only when holes and higher-dimensional features are negligible.”

**Support/label:** constructed topology example, not observed place fields; Mainali et al. 2025, Fig. 3F–H and STAR Methods Eqs. 8–10. Keep the field fixed across the threshold sequence and check the domain's boundary convention.

**Check before insertion:** masks must be nested as q rises; component and hole counts must match the actual masks; chi need not be monotone. Negative chi means more holes than components in 2D, not a negative number of fields. A shell's enclosed cavity adds to 3D chi. Do not imply that topology becomes simple at every practical experimental threshold.

**Size/access:** three or four panels across desktop width, stacked or two by two on narrow screens. Alt text states the counts and their change across thresholds.

## Optional additions

| ID | Placement | Drawing and lesson | Reason to defer |
| --- | --- | --- | --- |
| V09 | `sec:SYNTHESIS-COVARIANCE-EXAMPLE` | One small displacement moves two tuning responses in opposite directions; slopes +2 and -1 with coordinate variance 0.01 give rate variances 0.04 and 0.01 and covariance -0.02. Label this the guide's proposed bridge between a fixed map and noisy position. Negative covariance does not establish inhibition. | Useful final connection, but the text already has a short numerical example. |
| V10 | `sec:EYE-CHI` | Branch common C into X=C+epsilon and Y=C+eta. Variance bars use the chapter's independent-component example: 0.00820, 0.22446 and 0.00180 deg². Show R≈0.17 beside chi≈0.82, with definitions. | Add if the two percentages remain confusing after V04. Keep separate from the filtering plot. |
| V11 | `sec:PLACE-SLICES` | One nonconvex parent field yields two slice intervals; uniformly spaced lines hit a large region more often and off-center cuts are shorter than diameters. | Valuable sampling explanation, but secondary to constructing and counting fields. |

Detailed briefs and source locators for V05–V08, V10 and V11 are in `REVIEW_EYE_PLACE.md`. That assessment also records specific false implications to avoid. Its rankings are chapter-local; this plan sets the whole-guide order.

## Production and review boundaries

- Retain `fig:FOUNDATIONS-ATTRACTOR`; it already teaches restoring versus persistent disturbances. V02 adds the missing tilted-flow case rather than replacing it.
- Use one style across new figures: warm light background, dark readable text, a small consistent set of colors, arrows with explicit meanings, and direct labels. Color must not be the only distinction. Never rely on a tiny legend for a central assumption.
- Preserve source vectors and the calculations behind plots. Export appropriately sized SVG or PNG only after math and label checks. A generated raster picture is unsuitable for exact slopes, counts or equations.
- Before insertion, write one introductory sentence, a caption stating the conclusion and source status, an interpretation sentence, and alt text. Keep the needed definitions and assumptions in visible text.
- Select final sizes in the actual chapter layout. Review each finished figure at reading size and check a representative desktop and narrow layout. This plan does not authorize a long whole-guide visual sweep.
- Any source paper panel proposed later needs direct inspection of that exact panel and a source/rights decision before copying. Source locators here are based on existing chapter evidence; this pass did not recheck all paper panels at full size.
- Do not rewrite chapter explanations to fit an attractive picture. If a planned panel needs concepts taught later, split its placement, as in V03.

## Planning record

- Root inspected the actual chapter structure, existing visual ledger and the rendered attractor figure, and reused current writer evidence rather than repeating literature searches.
- A separate reader assessed Chapters 4–5 and saved six detailed candidates in `REVIEW_EYE_PLACE.md`. The coordinator selected the whole-book set and requested a final focused critique.
- No chapter, source table, existing image, generated HTML, or publication lock is changed. No build or whole-book audit is needed for this planning document.
- Task timestamps and final critique outcome are recorded below before handoff. Awake execution time and token statistics are unavailable unless separately verified.
- Final focused review found one necessary repair: V02's linear system has a straight tilted recovery path, not a curved path. The brief now gives the exact eliminated-time relation and shows slowing with time marks. The reviewer confirmed the repair and reported no remaining blocking issues in this plan. This is planning review, not acceptance of artwork that has yet to be made.
- All twelve section anchors used by the core and optional briefs were found in the current chapter sources. Only the existing attractor figure was visually sampled; no long visual sweep was performed.

- Planning completed: 2026-10-23T21:52:23.0303892+03:00. Wall elapsed: 533 seconds. Last measured source-check checkpoint: 2026-10-23T21:51:34.4491038+03:00. Awake execution time unverified. Token stats unavailable. Only planning files added; artwork production remains pending.

