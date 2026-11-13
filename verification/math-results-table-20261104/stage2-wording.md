# Stage 2: necessity and wording

Reviewer `/root/math_table_review`, requested GPT-6.1 Sol high. Exact serving build and backend request ID unavailable. Separate wording/necessity call following stage1; this is not the reader-understanding/flow stage.

Host start 2026-11-04T18:17:08.303152+02:00, finish 2026-11-04T18:19:13.422014+02:00. Wall elapsed 0:02:05.118862. Awake time unverified; no sleep/resume-log review. Time since preceding stage1 final checkpoint 0:02:45.887440. No observed system clock change. No reader edits.

Read all three cells of every parsed row in the current35-row table, the entire section introduction, added top reference link, and repaired beta sentence in its connected paragraph. Audience: physics/CS with calculus, linear algebra and basic probability. The table is explicitly a compact reference with links to full teaching, rather than a replacement for those derivations. Stage1 source checks are not repeated here.

## Decision and deletion test

Keep all35 rows. Each gives a requested model, principal result, relevant extension, physical parameter consequence or distinct test. Deleting whole rows would lose part of the requested all-major-results coverage. The derivation and interpretation cells perform different jobs: the former states mathematical transitions, the latter states circuit/movement/map consequences and limits. Repeated assumptions often constrain a different formula, so deleting them solely as repetition would weaken meaning.

Three narrow wording corrections are required. No broad rewrite is needed. These do not challenge the formulas accepted in stage1.

1. **Row1 derivation, who changes what:** 'A spike count N_i increases outgoing activation s_i by one' assigns a one-unit change to the count variable itself rather than to each spike. Replace with 'Each spike increases outgoing activation s_i by one; N_i counts these spikes. Between spikes, s_i decays over time tau.' A count can increase by several events over an interval, so 'by one' must attach to an individual spike.
2. **Row26 derivation, mean positive slope:** use 'mean positive part of the spatial slope' rather than 'mean positive spatial slope'. The first means E[(z')_+], which the formula needs; the current wording can mean E[z'|z'>0], which is twice as large in this symmetric Gaussian setting. The height-conditioning location and independence are already supplied in the connected teaching.
3. **Row27 derivation, which ratio:** 'Their ratio gives active fraction' follows the two means mu_s and mu_g, but mu_s/mu_g is not active fraction. Replace with 'The field mean divided by the sum of both means gives the active fraction.' The displayed q inversion is already correct.

## Per-row wording judgments

1. Retain the spike/count model and input-to-rate distinction. Required actor/one-spike wording repair above. W_ij's sending and receiving roles are explicit.
2. Retain the mean/variance relation and conditional independence qualification. 'Absolute count noise' distinguishes amount of count variation from relative precision. 'Complete neural trajectories' is a useful qualification for a recurrent system.
3. Retain K, u and v explanations. The left vector's role is tied to the explicit disturbance and surviving shift, not left as an unnamed operation. 'Transverse directions' is specialist wording supported by the linked projection treatment and physics baseline; replacing it is optional.
4. Retain the special symmetric case and source-correction note. 'Primes' has its equation-specific meaning given locally; standard derivatives need no further glossary.
5. Retain the tensor, FI matrix and matrix inequality together. Diagonal versus off-diagonal entries are translated into individual and coupled coordinate changes. 'Every linear combination' states the practical meaning of the matrix order symbol.
6. Retain line versus wrapped-error qualifications. 'Systematic drift' means mean movement in the connected chapter; 'point initial value' is ordinary distribution language for this reader. Noise continuing despite an MSD plateau is a needed physical distinction.
7. Retain the current-state versus original-cue distinction. The log-probability derivative is identified as the object being squared. 'Regular locally unbiased' names real CR conditions, with the linked proof supplying their details.
8. Retain the action chain: spikes convey the value and renew its activity. The bound is tied to fixed J and tau and the model assumptions, avoiding an unrestricted statement about all memory.
9. Retain the equality condition and sufficient-versus-necessary distinction. 'Retained effect' has its v_i meaning from row3; it is not an unexplained benefit claim. The linear counterexample reference prevents an overstrong interpretation.
10. Retain controlled parameter comparisons. The fixed distribution, weight rescaling and fixed rate/input relation say what acts and what is held fixed. 'Tuning/input geometry' is shorthand with a full linked explanation, acceptable in this reference role.
11. Retain width powers and the fixed firing-resource condition. 'Recruited cells' means more tuning curves contribute to the integral, explained by the volume factor. No need to expand the full integral here. Title tightening is optional, below.
12. Retain separate observation and movement contributions. 'Observation square' refers to the displayed double-covariance integration in the linked derivation. Later observations represent a moved state, so the direction of harm is concrete.
13. Retain the precision update, reciprocal variance and saturation-time interpretation. 'Backward in time' describes likelihood combination, not physical movement backward. The linked derivation defines precision and coth; expanding both here would repeat full teaching.
14. Retain storage plus readout and alpha-information distinction. The final sentence now expressly says full spike access, so the full-access asymptote cannot be mistaken for the partial-access one. The printed-source correction is tied to its mathematical qualification.
15. Retain the two-stage extension. 'Linearize both sets of variables' identifies the objects, and 'combined tangent' links to the mode calculation. The row explicitly limits the sum of times to this model.
16. Retain the matched constant-noise calculation. q_n is locally defined and explicitly distinguished from spatial threshold q. 'Matched' means the information and diffusion calculations use the same noise law, stated in the preceding sentence.
17. Retain inverse fitting, calibration and one-cell prediction limits. k,r,m are tied to position, velocity and acceleration; r is expressly disambiguated. The equation and linked passage supply f's input role.
18. Retain predictor standardization and nonnegative residual argument. 'Representative average' correctly attaches a requirement to applying the population bound to sampled cells. No need to add a general statistics lesson.
19. Retain calibrated displacement variables and shared/private split. 'Upstream' has a physical motor-pathway meaning in the linked chapter. The extra biological independence premise is visible rather than hidden inside a numerical result.
20. Retain the error-offset derivation and zero-lag distinction. The errors act at two readings, and each contributes variance. Correlated errors are correctly said to need a different correction.
21. Retain stationary-noise versus accumulating-MSD distinction. 'Filter overlap' is defined by the displayed integral; the physical conclusion follows directly. The observed-range qualification limits the data claim.
22. Retain the guide derivation label. B drives E through a response time, and the decoding states how tau_f and D change the curve. The row explicitly separates synaptic time and the paper's full muscle/feedback model.
23. Retain slope normalization and count-noise scale estimate. Absolute a and fractional b are locally defined before their opposing rate comparisons. 'Renewal' and 'sub-Poisson' are necessary noise-model terms taught in the linked chapter. The source ambiguity is an actual limitation, not decorative caution.
24. Retain threshold, gain and spatial-scale definitions. The action of raising threshold is stated as removing active space. ell_c versus input standard deviation is a needed symbol distinction.
25. Retain independent random weights and covariance computation. 'Cross terms vanish' states the mathematical cause; the decoding distinguishes input amplitude from profile width and does not promise a Gaussian map from arbitrary weights alone.
26. Retain exact crossing and finite-track correction. Replace 'mean positive slope' as above. 'Clipped boundary fields' is the precise counting rule; it is explained as components intersecting the track.
27. Retain parameter inference from two means. Specify the active-fraction ratio as above. Complete fields, complete gaps and selection/clipping matter to using sample means, so those qualifications survive deletion testing.
28. Retain dependence decay, rare-event approximation and zero-field selection. 'Excursions' is already defined by the thresholded map; 'bulk count' is locally explained as dropping finite-track boundary effects. The probability statements answer different questions from row27's means.
29. Retain smooth/stationary/isotropic and high-positive-threshold conditions. Peak excess epsilon and volume factors are tied to radius and size conversion. Names Rayleigh, exponential and Weibull identify different laws whose forms are given, rather than serving as unexplained labels.
30. Retain the peak-rate consequence of the geometry. It says which exponent applies to linear size and that area/volume differ. The finite-threshold qualification prevents calling a limiting square law an exact data fit.
31. Retain moments as a shape test after matching the mean. Gamma is defined at the linked derivation. Occupied-volume sampling is contrasted because it would change the distribution, not for rhetorical effect.
32. Retain Gaussian restriction and distinct slice sampling. The actor is choosing points on a line/plane, and the retained object is a joint distribution. Its interpretation distinguishes a spatial intersection from one central cut per field.
33. Retain crossing-selection weighting. v=z' is defined locally, its selection weighting is explicit, and the rate gain changes the observed slope scale. The exact label is correctly separate from the high-threshold size law.
34. Retain components/holes/tunnels/cavities and boundary terms. Euler characteristic is explicitly decoded into counts in2D/3D, with eye chi separated. The signed critical-point argument is a useful derivation outline with a linked detailed calculation.
35. Retain high threshold and large-region conditions. The derivation names which terms are dropped, and the decoding prevents the exact EC law being treated as an exact ordinary component count.

## Introduction, role labels and specialist words

The top reference link is useful navigation and does not promise a new prerequisite. The beta sentence supplies a necessary unit check with ordinary words. The section opening defines the requested 'decoding' column as physical interpretation and limits, avoiding the narrower usual neural meaning. Model/method/extension/guide labels keep model choices separate from derived conclusions. Exact/approximation labels attach to mathematical assumptions rather than biology. Most specialist words name actual tools and have either a local definition, a prelude definition or a linked derivation: Fisher information, Ito increments, tangent/left vector, renewal, Kac-Rice, isotropy, and Euler characteristic earn their place. Basic expectation, variance, density, derivatives and linear algebra do not need reteaching for this audience.

## Optional preferences, not acceptance blockers

- Row11 title could be 'How tuning width affects precision' or 'Tuning width and dimension', because the result changes the benefit of width rather than forcing width itself to depend on dimension.
- The introduction repeats the model scope in two adjacent exact/approximation sentences. They could be combined, but the repetition does not obstruct a needed meaning.
- Some compound wording could be expanded, such as 'stable transverse directions' to 'disturbances away from the memory family decay'. The current technical shorthand is allowed by the physics/CS baseline and reference-table role, so no mandatory expansion is requested.

No further deletion or wording change is required. Stage2 passes after the three narrow corrections are checked. Stage3 flow/understanding remains pending. No rendered-page judgment is claimed. Token stats unavailable.

## Reader and rule hashes

- `content\chapters\00-mathematical-tools.md`: SHA256 `BECA4E530159D77B49C58495FC126530C6671AF8994E4310EF1F95BF9BC0DA02`
- `content\chapters\00-mathematical-tools.yaml`: SHA256 `66D302B80CC1607268807F6ED03CAA1C23A807BD0CEA093629746B61B83FE844`
- `C:\Users\vital\.codex\skills\course-study-guide-builder\references\pedagogy-language-contract.md`: SHA256 `F4C1EB544CF640B708E1970D9572FDC758FCC6AEA806675D01A0256658DF847A`
- `C:\Users\vital\.codex\skills\course-study-guide-builder\references\math-code-case-contract.md`: SHA256 `CE2313F897B63E74BA59A3AFE1BBC4046D3AA84584072CDA7E76470A7E3CEF9A`
