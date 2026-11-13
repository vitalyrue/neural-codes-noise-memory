# Illustration assessment for Chapters 4 and 5

Planning only. No artwork generated, chapter text changed, or build run.

Root task start: 2026-10-23T21:43:30.3359267+03:00. First measured checkpoint for this assessment: 2026-10-23T21:44:28.5575407+03:00. Draft checkpoint: 2026-10-23T21:45:42.3689957+03:00. Awake execution time is unverified.

## Basis and choice

Read the connected teaching passages in `04-eye-drift.md` and `05-place-fields.md`, their figure-reading passages and source notes, and the writer evidence locators. Read the visual integration contract. The only existing approved visual is `assets/approved/visuals/attractor-directions.svg`, used in foundations. These suggestions do not duplicate it. Source figure locators below identify the supporting figures; no new full-size inspection of those source panels was performed in this planning pass.

Six candidates follow, ranked by the reasoning they make visible. They are possible additions, not a claim that all six must be drawn. Start with 1, 2 and 3; add 4 and 5 if the whole-book figure count remains manageable. Candidate 6 is useful if readers find the sampling argument hard.

## 1. The same muscle filter has different effects on two noise sources

- **Type:** mathematical plot with a small mechanism diagram. Essential.
- **Place:** `sec:EYE-FILTERED-MSD`, immediately after the paragraph ending “without faster than Brownian accumulation inside the memory circuit,” before the actual-model qualification.
- **Hard step:** a smooth eye trajectory need not mean that the stored position itself accumulates faster than diffusion. A smooth input can also be stationary, so appearance alone cannot distinguish the hypotheses.
- **Drawing:** two rows: stationary white input to the same one-pole filter to position, and Brownian stored position to that filter to position. To the right, show dimensionless theoretical MSD curves against `x = lag/tau`: `1-exp(-x)` and `x-1+exp(-x)`, each explicitly normalized to its own scale. A second small panel shows their logarithmic slopes: white input tends from 1 to 0; filtered Brownian position tends from 2 to 1. Label the plateau and continuing growth directly. Keep the color assigned to each hypothesis identical in the diagram and plots.
- **Take-away:** a decaying filter makes stationary white input saturate, while it smooths a wandering position without removing its long-lag accumulation.
- **Label/source:** “Guide calculation for the one-pole teaching model; not the paper's fitted curves.” Ben-Shushan et al., main Fig. 3, main Eqs. 20–22 and the chapter's explicit one-pole derivation. The mechanism link to memory and muscles is supported by main Figs. 4–5.
- **Do not imply:** this one-pole white-input curve has the same short-lag smoothness as the paper's double-exponential muscle model; normalization establishes equal physical noise amplitudes; a lag below the feedback delay is unaffected by feedback; or these curves are empirical data. Avoid random traces here because their finite samples can hide the mathematical distinction.

## 2. One spatial curve gives both fields and crossing counts

- **Type:** exact geometric teaching plot. Essential.
- **Place:** `sec:PLACE-KAC-RICE`, after the local band-width explanation and before the Kac–Rice integral. Refer back to it from `sec:PLACE-INFERENCE` rather than duplicate it.
- **Hard step:** turning a level crossing into an integral weighted by slope, and relating crossings to connected fields without losing the endpoint field.
- **Drawing:** one smooth constructed `z(x)`, a horizontal `q`, and shaded above-threshold intervals on the same x-axis. The first interval is already active at the left boundary. Mark upward crossings, one full field length, and one gap. In a magnified inset, draw the vertical band `q±epsilon` at two positive slopes; show horizontal widths `2epsilon/v`. A short bracket under each crossing states that the weighting makes each contribute one. Keep the input height axis separate from a small aligned rectified-rate strip, if that strip is included.
- **Take-away:** each upcrossing starts one new field; a clipped field can already exist at the left edge; steep crossings spend less distance near the threshold and therefore receive a slope weight.
- **Label/source:** “Constructed smooth curve for counting; not a sampled cell or a new fit.” Mainali et al., main Fig. 1A–B for threshold construction, supplement Methods S3, Eqs. S11–S15; chapter's exact finite-track counting identity. A constructed smooth curve need not be labeled a Gaussian-process sample.
- **Do not imply:** height above threshold equals field count; every peak is a separate field; a derivative at a uniformly chosen position has the crossing-selected slope distribution; or the endpoint correction applies unchanged after discarding clipped fields.

## 3. Raise the threshold and watch components and holes separately

- **Type:** topology map and count strip. Essential.
- **Place:** `sec:PLACE-TOPOLOGY`, immediately after the first paragraph defining Euler characteristic and Betti numbers, before the Morse-theory input.
- **Hard step:** why Euler characteristic can differ from the number of fields and why a negative value is meaningful.
- **Drawing:** three or four increasing thresholds applied to exactly the same smooth constructed 2D map. Show only the nested active sets, with connected components assigned visible outlines and holes left white. Under each mask print components, holes and `chi = components - holes`. Choose verified levels that show a hole and a split, so the count need not change monotonically. Include one simple separate 3D inset comparing a solid ball, solid ring and hollow shell, labeled `(components, tunnels, cavities)` with chi values 1, 0, 2. Make the inset optional if it makes the main image crowded.
- **Take-away:** Euler characteristic tracks connectivity and holes across thresholds. It approximates field count only when high-threshold components have become simple solid blobs.
- **Label/source:** “Constructed shapes to explain the counts; not observed place fields.” Mainali et al., main Fig. 3F–H and STAR Methods Eqs. 8–10. The exact masks must come from one fixed map, not unrelated drawings pretending to form a threshold sequence.
- **Do not imply:** topology is monotone in threshold, a negative chi is a negative number of fields, the 3D formula subtracts enclosed cavities, or the square/cube boundary terms apply to a periodic domain. A hole clipped by the outer boundary must be counted using the actual chosen closed-domain convention.

## 4. A weak correlation can coexist with a large common movement fraction

- **Type:** signal and variance diagram. High value.
- **Place:** `sec:EYE-CHI`, after the constructed numerical example giving `R≈0.170` and `chi=0.820`, before experimental uncertainty and weighting.
- **Hard step:** distinguishing correlation between one noisy neuron and movement from the fraction of real movement supplied by common drive.
- **Drawing:** a common displacement `C` branches to `X=C+epsilon` and `Y=C+eta`. Separate private contributions enter only their own sum. Label both outputs as displacement in degrees. Below, use variance bars with a shared physical scale and a clearly marked zoom if needed: `Var(C)=0.00820`, `Var(eta)=0.00180`, `Var(epsilon)=0.22446 deg^2`. Display `Cov(X,Y)=0.00820`, `R≈0.17` and `chi≈0.82`. The first visual should not depend on knowing anatomy. An optional small note connects X to the calibrated one-cell inverse prediction and Y to measured eye displacement.
- **Take-away:** private prediction noise inflates the single-neuron denominator in R; it does not remove the common contribution to actual movement.
- **Label/source:** “Constructed independent-component example using the chapter's values.” Ben-Shushan et al., main Eqs. 11–16 and Fig. 2. The independence/gain conditions are printed near the branching diagram, not hidden only in a caption.
- **Do not imply:** these are individual-cell measurements; R and chi are interchangeable percentages; zero sample correlation proves independence; simultaneously recorded neurons established private-noise independence; or upstream common drive uniquely proves the proposed integrator mechanism.

## 5. The same excess height becomes length, area, or volume

- **Type:** geometric derivation diagram plus optional mathematical plot. High value.
- **Place:** `sec:PLACE-SIZE-LAW`, after the display defining `s`, `U` and `beta`, before the density change of variables.
- **Hard step:** why the exponent `2/d` changes across dimensionalities even though the same local high-peak argument supplies a radius.
- **Drawing:** start with one parabola near a rare high peak. Mark threshold q, excess epsilon and radius `r_*`, with full width explicitly `2r_*`. A short calculation arrow gives `U=q epsilon` and `r_*=(sqrt(2) sigma/q)sqrt(U)`. Branch to an interval, disk and ball, each labeled `s=2r_*`, `s=pi r_*^2`, `s=4pi r_*^3/3`. Conclude with `U=beta s^(2/d)` and shape powers 2, 1, 2/3. If showing densities, use dimensionless size divided by its own mean on the horizontal axis and mark the 3D integrable divergence; do not put metres, square metres and cubic metres on one raw axis.
- **Take-away:** the change from radius to d-dimensional size transforms an exponential excess into Rayleigh, exponential and Weibull size laws.
- **Label/source:** “Guide reconstruction of the high-threshold limit.” Mainali et al., main Eq. 1, supplement Methods S4, and the chapter's corrected parabola constants. The step from conditional Hessian to approximately round high peaks remains an asymptotic model assumption, not an exact shape claim at the bat-data threshold.
- **Do not imply:** every observed field is a sphere or parabola, the limiting scale is exact at q=1.1, beta has different distance dimensions in the three cases, or 3D's divergent density places positive mass at zero volume.

## 6. A slice changes what is counted and how it is sampled

- **Type:** spatial sampling map. Useful second pass.
- **Place:** `sec:PLACE-SLICES`, after the paragraph contrasting a uniformly selected field with spatially sampled lines, before the source-figure reading paragraph.
- **Hard step:** why a line through a 3D map uses a 1D excursion law but does not simply inherit the distribution of full-field radii or central diameters.
- **Drawing:** first panel shows one connected, nonconvex 2D active region intersected by a straight line in two separate intervals. Keep the parent component outline and the two slice components visibly distinct. A second panel shows a large and a small round region crossed by a uniformly spaced family of lines; the large region is hit more often and off-centre cuts are shorter than diameters. A compact dimension strip shows 3D map to plane to line, labeling measured volume, area and length. Use arrows to mean restriction of the same spatial map, never passage of time.
- **Take-away:** the observation's dimension determines the excursion-size law, while hit probability and cut position determine sampling. One original field does not necessarily yield one slice field.
- **Label/source:** “Constructed geometry illustrating the sampling rule.” Mainali et al., main Fig. 2A–J and supplementary Fig. S2A–C. The latter supplies the useful empirical comparison: matching full volumes need not match slices. Retaining selected exact source panels can complement this diagram later, but their data should not be redrawn from the schematic.
- **Do not imply:** centre cuts represent uniformly sampled spatial lines; spherical-field matches of volume validate slice predictions; each line intersection is a distinct original cell or field; or the constructed nonconvex shape is a direct GP model simulation.

## Whole-book choices for the coordinator

- Prefer these exact plots and geometric maps over generic neurons, brains, animals, or arrows between topic headings. The paper's data figures can remain linked at the paragraph that interprets them unless a particular panel is needed beside the derivation.
- An eye anatomy opener is lower priority than the two eye reasoning figures above. If another map already covers memory circuit to motor neurons to muscle to eye, reuse it here and add only the distinction between the proposed mechanism and the measured inference.
- Do not combine crossing counts, the high-peak size law, slicing and topology into a single dense Chapter 5 figure. They answer different questions and carry different assumptions.
- Every selected figure still needs an introduction tied to the adjacent calculation, conclusion-bearing caption, interpretation, accessible description, fixed display size, source label and full-size review. This planning file does not certify future drawings.

Token stats unavailable.

Completed assessment: 2026-10-23T21:47:21.2722402+03:00. Wall time since root task start: 231 seconds. Since previous measured checkpoint: 99 seconds. Awake execution time unverified.

