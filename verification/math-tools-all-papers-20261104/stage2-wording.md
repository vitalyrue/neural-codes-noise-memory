# Stage 2: necessity, terminology and plain wording

Started UTC: 2026-11-04T14:29:39Z
Finished UTC: 2026-11-04T14:31:45.829923+00:00
Wall-clock elapsed: 127 seconds.
Awake execution time: unverified; Windows sleep/resume logs not inspected.
Token stats unavailable.

Scope: current new introduction, transition from the preserved bound, and four new mathematical-tools sections. Related passages in the six requested chapters were inspected for first definitions, aliases and backlinks. Their remaining previously reviewed content was not audited. No edits or builds. Stage 1 conclusions were not treated as evidence for the changed text: moved definitions and the field-selection sentence were checked directly.

Verdict: substance and plain wording are good. A few short local clarifications are needed to meet the requested rule that technical terms and symbols have meanings at first use. Essential mechanisms mostly remain outside folds; the final names of the predicted size laws should also be visible there.

## Required local findings

1. SHARED, final application paragraph: define N_m at its use. “Of order 1/N_m in its many motor neuron model” does not explicitly say that N_m is the number of motor neurons. Suggested wording: “of order 1/N_m, where N_m is the number of motor neurons in its model.” This is a symbol-definition issue, not an objection to the source result.

2. FILTERS, worked calculation opening: define delta and C_E rather than making the reader infer them. A sufficient short addition is: “Here delta is the Dirac delta, an ideal impulse with unit area, and C_E(lag) is the output covariance at that lag.” Calculus and basic probability do not by themselves supply the continuous-time delta convention. No full lesson on distributions is needed. The later sentence explicitly calls C_v velocity covariance, so that symbol has the necessary role.

3. RANDOM-FIELDS, final assumptions paragraph: “regular, nondegenerate height and slope distributions” leaves the important new technical word nondegenerate unexplained. Its meaning is supplied later in 05-place-fields.md, but the tools chapter precedes it. Explain it briefly here, or use plain wording suitable for this model: heights and slopes have finite positive variances and no exact linear constraint. Keep the separate differentiability and second-derivative requirements. This request concerns reader understanding of an existing condition; it does not call for stronger mathematical assumptions.

4. CROSSINGS-PEAKS, end of peak example: the only sentence identifying the limiting length distribution as Rayleigh, area distribution as exponential and volume exponent as 2/3 is inside the example fold. The visible closing paragraph says “These size laws,” but a reader leaving the fold closed has not seen which laws result. Put the one-sentence result outside the fold, next to its high-threshold qualification. Keep the quadratic formulas and probability transformation inside. This follows the introduction's promise that meanings and conclusions remain in the main text.

## Paragraph-based assessment and retentions

Introduction: each paper supplies a concrete question and matching tools. The prerequisites assume expectation, variance, standard deviation and density; the new sections do not reteach those basics. Keep the three reading paths because they let a reader choose a paper without treating all seven sections as one derivation. The memory-to-eye transition has a necessary job: it connects internal fluctuations to recorded signals and movement without repeating the bound.

SHARED opening: the common-command versus private-noise question gives the covariance calculation a reason. The main definitions explain what covariance and correlation compare, while the closed mathematical-definition fold gives exact formulas and units. Moving those formulas did not change their truth. The short formula reminder is relevant to the inference and does not become a lesson on variance or standard deviation.

SHARED model: X, Y, S and the private eta contributions have physical roles and degree units. The blue gain definition appears where a and b acquire their roles; its plural suffix is outside the styled singular term, which is intelligible and consistent. Chi_Y is visibly the ratio of shared movement variance to total Y variance. Optionally name it in a short clause before the equation, but the present numerator, denominator and immediately following sentence already make its meaning recoverable. Calibration, the nonzero-a condition and private-noise effect remain visible. The numerical panel demonstrates a useful failure of interpreting small correlation as a small common contribution. The final application paragraph adds actual paper assumptions, not a second generic definition.

FILTERS opening and response paragraph: the physiological delay motivates the tool. Causal filter, impulse response and convolution have direct definitions before their equations are used. U and E are input/output angles; h and tau have units; the mismatch drives velocity. Keep this physical equation explanation in the main text. White noise intensity is correctly separated from finite pointwise variance, and stationary position is explained through mean, variance and covariance. The difference between lag and clock time is needed here. The Brownian/diffusing-command paragraph connects accumulated changes to short and long lag behavior, with the position-versus-increments distinction visible. The fold contains the longer calculation and the main text retains the physical contrast. The single-time-constant and measurement limits are relevant. Optional small polish: write “mean squared displacement (MSD)” on its first use so the later abbreviation has an explicit expansion.

RANDOM-FIELDS opening and Gaussian paragraph: the fixed sampled map and joint Gaussian requirement are necessary for later calculations. The definition of a jointly Gaussian vector immediately follows its first use and is sufficient for this audience. Stationarity and isotropy have distinct roles; keep both because the crossing result and peak shape use different assumptions. Normalization identifies the original threshold, dimensionless q, rectifier and rate conversion. The connected-component sentence prevents confusing multiple peaks with multiple fields. The local distance scale paragraph correctly limits what correlation length can tell the reader. The cusp example is useful because Gaussian marginals do not guarantee derivative-based calculations.

CROSSINGS-PEAKS opening: upcrossing is defined before use, and threshold density times conditional slope explains the displayed formula. The physical slope-weighting explanation remains outside the derivation fold, as it should. The folded narrow-band argument supplies the longer steps without hiding the reason for slope weighting. The finite-track endpoint correction has an immediate counting purpose and should stay. The next paragraph explicitly says that fields are counted once rather than weighted by their occupied space; this implements the earlier clarification correctly. The radius/excess/dimension mechanism is visible. Within the example, epsilon, b, q, U, s and S have enough local context to follow the calculation. Optional short improvement: identify v_d as the factor converting radius^d into size, and beta as its scale factor, although their equations and v_1,v_2,v_3 values already give the needed role.

## Aliases, repeated definitions and links

- 01-foundations.md points back to the shared-signal section and retains its physiological explanation. Its later covariance/gain reminders are plain text, not competing blue first definitions.
- 03b-memory-readout.md points to the filtering section for continuous-time white noise and then applies the convention to the spike-noise equation. It retains the required variance-per-dt interpretation.
- 04-eye-drift.md points to the filter introduction. Causal filter, impulse response and convolution are explained locally as applications without new blue first definitions. Gain is explained in ordinary text. Its full spike filter has different units from the teaching angle-to-angle filter, and those units are explicitly given, so the difference is handled.
- 04b-eye-timing.md points to the filter introduction and keeps the data comparison. White-noise and low-pass reminders do not repeat blue first definitions. Its stationary-process definition has a narrower temporal context than spatial stationarity in the tools chapter and is useful. Optional link cleanup: the later “white noise” link still goes to the readout chapter, which now points back to tools; a direct tools link would save a hop.
- 05-place-fields.md explicitly translates sigma_0 to sigma_h and ell_c to sigma before using its own formulas. Upcrossing, Gaussian process, joint Gaussian, stationarity, isotropy, excursion set and Kac Rice are no longer competing blue first definitions in the inspected passages. The retained blue smoothness explanation has its own role.
- 05b-place-sizes.md points to peak geometry and translates ell_c to sigma before the curvature derivation. The retained Hessian definition belongs in that detailed chapter because the new tools section avoids that term.

No request here for a full-book audit, extra figures, rebuilding outputs or replacing the physics/CS prerequisite level. Stage 3 reader-flow review remains separate.

## Current input SHA-256 hashes

- `content/chapters/00-mathematical-tools.md`: `648824c78598649cdfb625743340bf5a04c6b11d6396238b55f70049aea4a083`
- `content/chapters/01-foundations.md`: `75873336ef2a58832418c9aedc8d72e422dd63ea9a98e42bbd4fe4bb0244138e`
- `content/chapters/03b-memory-readout.md`: `59959bd393fa36624773027c68f297886ce6f109abbde1d79118bc36539629c0`
- `content/chapters/04-eye-drift.md`: `2fbb5f1d55126fb952e44e9e8650fc7ddc00c7e8b5dcebab8e44182a7507dc05`
- `content/chapters/04b-eye-timing.md`: `15916da716dc5c8c64acbf9be65c837877c48674ac2c265a2b4737c9f7bdebfb`
- `content/chapters/05-place-fields.md`: `60dcdf27c11276c338bbd9f6974896905e5b0dac526237cc5d90bab057d2efdf`
- `content/chapters/05b-place-sizes.md`: `f07c8d921362f614019d56cbd3a4b150d12c6d0fae12a6958ef71f6b152dccb1`
