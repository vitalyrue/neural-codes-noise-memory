# Stage 2: necessity and wording

- Reviewer /root/exam_review_check; separate request ID exam-review-stage2-20261104. Inherited Sol high requested by coordinator; exact backend not exposed.
- Actual host start: 2026-11-04T19:21:17.389194+02:00
- Actual host finish: 2026-11-04T19:23:41.771338+02:00
- Wall-clock elapsed: 144.4 seconds. Awake execution unavailable; sleep/resume logs not collected. No clock change observed.
- Scope: current exam-review MD/YAML, all35 results in six result tables, map and prose, connected old-tools route. No edits, build, source expansion or stage3 flow verdict in this call.
- Audience: physics/CS and basic probability. Mean, variance, standard deviation and density are assumed; their ordinary definitions should not be added.

## Required finding

P1 first cell displays `F=a[z-q]_+`, while its Symbols and units does not explain the positive-part brackets. The word thresholding and the statement z>q explain active regions but do not fully state the firing output below threshold. Add the short local operator definition `[u]_+=max(u,0)`, meaning positive excess is retained and negative excess becomes zero. This is a subject-use operator definition, not a statistics tutorial. This one finding remains open for a narrow recheck.

## Deletion test and proportionality

Retain all35 results as required. Repeated row-local D/J/time/unit definitions serve independent formula lookup, which was the user complaint; deleting them would recreate the lookup failure. The three overview chains and 14 visible core results keep the first review route shorter, with21 additional rows closed. Exact source equation/page mapping and guide-origin distinctions are longer than ordinary index cells, but answer the specific location request and explain why several source formulas differ. Their labels separate searching, derivation and interpretation. No mandatory table rewrite or repeated stylistic substitution is warranted.

## Per-row three-cell wording judgments

| Result | Formula and local symbols | Location/origin/derivation | Meaning and limits |
|---|---|---|---|
| M1 | Sender/receiver W indices and unit-spike activation remove the actual decoding ambiguity. | Count-process vs printed impulse notation deserves the short source explanation. | Fixed weights vs changing activity states what physically stores the value. |
| M3 | K,u,v dimensions and retained v-transpose disturbance explain the unfamiliar projection roles. | Exact S8-S15 map separates definitions and variance result; route explains lasting projection. | Retained shift and half variance growth translate symbols into physical effect. |
| M7 | Information rate vs interval information and estimate units are essential local definitions. | Likelihood route makes score meaning concrete as log-probability derivative; conditions retained. | Current-state precision vs cue certainty gives a usable interpretation. |
| M8 | Dimensionless product and common tau identify the comparison scale. | Short normalized projection/Cauchy Schwarz route directly answers how bound follows. | Fixed J/tau and tuned-noise conditions bound the network-design conclusion. |
| M9 | phi input derivative and k input units avoid mixing two derivative meanings. | Explicit reconstruction/necessity qualification prevents search for an absent printed equation. | Sufficiency vs necessity and matched spike effect explain equality rather than restating display. |
| M13 | Characteristic time, variance, precision and coth defined without reteaching ordinary statistics. | Precision route and source-sign caveat support reconstruction without pretending exact source notation. | No hard deadline and no biological implementation claim protect actual meaning. |
| M2 | K_i/count vs K/matrix alias warning is needed in independent lookup. | Source count aliases are mapped before the short rare-event route. | Conditional independence vs whole-trajectory correlations is necessary, not filler. |
| M4 | Input slopes and pairwise W symmetry identify exactly what is specialized. | Correction locator is needed because printed main numerator differs. | Decoding tells why this special formula is convenient and what remains general. |
| M5 | Coordinate indices, shapes and PSD meaning prevent scalar reading of matrix inequality. | Separate diffusion/FI/bound page references are useful because source splits them. | Coupled directions explain the off-diagonal terms beyond repeating formula. |
| M6 | Initial/current coordinate and constant-D qualification distinguish the three displays. | Printed line/wrapped results and guide-derived plateau are separated. | Boundary plateau interpretation adds meaning needed before applying 2Dt. |
| M10 | Rate multiplier vs preferred-position vector and held-fixed resources are needed. | Replication and preserved geometry state what changes and what is adjusted. | Circuit-adjustment limit prevents memorizing unconditional scaling rules. |
| M11 | Density, width, gain and dimension are concrete resources of the scaling comparison. | Recruited-volume vs squared-slope route explains width power with little added setup. | One/two/three dimension consequences and fixed-spike-budget distinction earn the prose. |
| M12 | Observation L vs storage T prevents conflating readout and retention. | Brownian covariance integration explains why growing time adds error. | Equal weighting helps then hurts is the intended meaning of the optimum. |
| M14 | Observed fraction vs coordinate alpha and cue/storage intervals are necessary aliases. | Thinning and independent error addition expose assumptions needed for substitutions. | Selected-neuron caveat and equality-only 2D(T+tau) prevent two exam errors. |
| M15 | Rate response time vs synaptic decay time gives each derivative a physical role. | Two-stage normalization and corrected decay sign are enough to locate longer proof. | Arbitrary biological times cannot be added; this limit is needed. |
| M16 | Noise intensity q_n vs threshold q and q_n/h rate variance explain units. | Matched likelihood/noise reconstruction explains factors missing from printed source. | Noise-dependent optimal transfer rule gives purpose to extension. |
| E1 | k,r,m and causal delay units translate motor rate into movement; r alias warning useful. | Factorization and explicit PDF Methods titles are directly searchable. | Single-cell prediction is separated from single-cell control. |
| E3 | Prediction, measured displacement, shared component and errors have distinct local roles. | Covariance expansion points to the actual assumptions, not correlation alone. | Weighted uncertainty and biological independence condition retain the limit on causal reading. |
| E5 | Input unit U and convolution-kernel units prevent mixing eye filter with spatial h. | Stable-response overlap and squared difference are short mechanism route. | Plateau vs continuing observed growth makes the comparison meaningful. |
| E6 | Command B, observed E, temporal D and eye tau_f prevent memory-parameter substitution. | Explicit guide-only one-time-constant label and velocity-covariance integral are needed. | Smooth motion from accumulating command supplies causal interpretation. |
| E2 | Population mean vs sampled estimate and R-squared rescaling define bound meaning. | Residual variance route uses ordinary linear prediction, no extra vocabulary required. | Representative-average caveat matters to applying the population result. |
| E4 | Two readings and positive lag explain the factor two; no variance tutorial added. | Expansion of E+noise shows exactly what is corrected. | Zero lag and temporal correlation identify where constant offset fails. |
| E7 | Absolute a vs fractional b slopes are necessary to interpret rate change. | Renewal CV scale is marked simpler than complete paper model. | Fixed-slope comparison explains opposite rate effects without a false general rule. |
| P1 | REVISE: [z-q]_+ is the only displayed threshold operator without local meaning. Add [u]_+=max(u,0), keeping positive excess and replacing negative excess by zero. All other symbols/units/aliases earn their space. | Normalization-to-threshold route makes what acts on what concrete; source/gain reconstruction label useful. | Connected active region and fixed sampled map explain a field without extra probability definitions. |
| P3 | Upcrossing density, track length and clipped-component convention define count output. | Height-times-positive-slope route plus endpoint term explains two contributions. | Any-threshold Gaussian scope and parameter effects guide use of formula. |
| P4 | Per-field/gap means vs per-position/input means are necessary distinctions. | Fraction ratio followed by inverse tail makes parameter recovery understandable. | Two means constrain parameters before histogram test; selection/clipping warnings are relevant. |
| P6 | Size units, cutoff, radius, ball volume and counted-once convention permit interpretation across d. | Parabola, peak excess and geometry are the three necessary steps; corrections explain missing source constants. | Rayleigh/exponential/Weibull labels remain exact terms, with dimensions and high-threshold limits given. |
| P2 | Fixed input profiles vs random weights and averaging over weight choices are essential. | Cross-term cancellation and small-contribution condition explain covariance/Gaussian route. | Amplitude vs spatial width differences stop a misleading circuit interpretation. |
| P5 | Count/gap/threshold aliases and zero-cell conditioning define three distinct quantities. | Rare independent locations and short widths connect spacing to gaps. | Weak dependence and endpoint/selection limits are needed, not optional hedging. |
| P7 | Rate gain, excess and linear-size vs area/volume are needed to read exponent. | Radius elimination explains formula with no new unrelated input. | Limit vs empirical fit distinction is central to interpreting square law. |
| P8 | Gamma integral and moment-order k explain uncommon notation; ordinary mean/variance not retaught. | Exponential substitution is short route; source S18 issue explains guide formula. | Shape test after fixing mean gives moments a purpose. |
| P9 | Spatial t vs temporal t and unit direction distinguish restriction equation. | Restriction of joint Gaussian values explains preservation without new modeling assumptions. | Hit sampling vs central cuts is necessary before using slice laws. |
| P10 | Boundary-selected slope vs ordinary slope and firing gain av are defined. | Slope weighting explains why the density differs from a half Gaussian. | Exact threshold independence vs rate-gain scale states the useful prediction. |
| P11 | Signed EC and inverse-volume densities distinguish topology from positive field count. | Named source theorem is only a proof route; decoding supplies components/holes meaning. | Dimension-specific counts and real-boundary caveat are needed for use. |
| P12 | Environment measure V vs variance symbols and simple-blob requirement define approximation. | High-threshold leading-volume step connects to preceding EC formula. | Boundary/holes omission states where count approximation may fail. |

## Map and prose judgments

- Map memory cells retained: physical recurrent circuit, spike/feedback/noise chain and limited result use concrete actors and distinct jobs. Fisher information is an exact technical term developed in linked tools; replacing it by a loose synonym would obscure connection.
- Map eye cells retained: record/calibrate/compare/filter verbs say what researchers do; shared component and nonunique source limit are necessary.
- Map place cells retained: draw/threshold/count/use peaks sequence says what changes; exact vs limiting final cell earns its space.
- Prose unit 2, SHA256 `ccd0ebbab3546511921d64caf9316553810a012d1a1855855d19ccbb666f9d86`: Concrete recall prompt and return-after-study scope retained; it tells readers why this page exists.
- Prose unit 3, SHA256 `15082b84f2a011358927c4f1cd324c6922c147ec08654f585cdc758b7b3dea7c`: Short procedure label retained; it introduces the following numbered actions.
- Prose unit 4, SHA256 `fafa1f1e289c22cc6cee1a6c500e084636bb7fdb3c9f1d457ac94f3ff37c5c06`: Three actions retained: explain chain, locate a break, use local keys/links. SI and PDF-viewer page convention remove lookup ambiguity.
- Prose unit 5, SHA256 `fb12c8c12c86c8ab4a8a72d40c87380d625f6e657ccbf483760ae0dd446cff44`: Role-label qualification retained because central is not an exam guarantee; guide/source distinction is necessary and precise.
- Prose unit 11, SHA256 `134354b58af57c9311acff1bccdead6f68cf61432f328e0ddc4c89168bf0bf7c`: Stored coordinate, fixed recurrence, disturbances and retained value change form a plain causal summary.
- Prose unit 12, SHA256 `7f54da0a6156306d95fc8ee815527fc556cb44dddf5a06f2de47271505f39ec5`: Result IDs earn their space by connecting mnemonic chain to rows; M6/M14 redirect avoids silently losing storage/recall context.
- Prose unit 13, SHA256 `cb07848f0423c5ab1dd086fb742aeeccb1a1bf3aa4b7aad66b96c884563be13c`: Derivative exception and scalar-vs-matrix note prevent actual symbol confusion; each sentence supports local reading.
- Prose unit 23, SHA256 `f24816a2e1dcbcbab1e731539969a4c14a72eb26b3e930354e86521b56201343`: Recall answer retained: restore shape vs original coordinate supplies a plain mechanism; present decoding vs old cue is necessary.
- Prose unit 26, SHA256 `7a6874fb6c41df347897cd622f9e4c739616ee26be7900961e50a0cfa5cdbbe6`: Calibration in degrees and independent filtered-noise question are concrete experimental tasks, not empty introduction.
- Prose unit 27, SHA256 `3a6e2125a56fbc90336528f187d38a9df2e80ecc274dbacaccb1def1bbb9da3f`: Guide E6 vs paper model and separate E2 bound distinctions are essential; keep technical result labels.
- Prose unit 28, SHA256 `c3445924cf9b643acce891ac84e6f8d7db74f61c8cabce915f1a4fa5c6f9cc55`: MSD lag and eye response/synaptic decay distinction prevent time-parameter confusion; no generic timing tutorial needed.
- Prose unit 38, SHA256 `6a7dc774c9a39b2843d0ccd08e42f2d9a039514fcfe64f9d1d82b484d4804207`: Correlation denominator explanation retained as causal reason, not generic statistics instruction; calibrated covariance and upstream premise matter.
- Prose unit 41, SHA256 `2329ad1773c92db80e82d02796b384e166ff7b8f88bb91a793c958f07ca4aea7`: Fixed map, connected active regions, crossing counts, peaks and extra structure tests are the needed model summary.
- Prose unit 42, SHA256 `1f74278553c6f41b8ac623aab363cc29572f0c16b2d033bfbdb29962e6278fbd`: P1/P3/P4/P6 links connect actual argument; extra P9/P11 direction preserves scope.
- Prose unit 43, SHA256 `85295bcd81c339fee50aa3d69bd01d722d94d0a965f7a4dceb0483a4f015ad86`: Space vs time and ell_c/sigma/sigma_0 aliases directly answer likely physical confusion.
- Prose unit 53, SHA256 `f29c1d121aac497812f8ac1616950c5654918d5342d36913403ebda5b940794e`: Exact crossing vs isolated peak approximation is necessary exam recall; no deletion without losing the extra assumption.
- Prose unit 56, SHA256 `7513bf87e83444d71b191521914d330ebe796d5aa6dec9f897df5e5b06bb33ca`: Short question prompt retained to frame distinctions.
- Prose unit 57, SHA256 `c089a0f553f84074124b506f0d23bf4dbb69f8a10eb068fb47215d8d56847c9d`: Six bullets retained individually: activity/value/estimate distinguishes objects; present precision/storage separates goals; correlation/fraction states inference conditions; command/movement names filter action; temporal/spatial randomness separates ensembles; exact/limiting states extra high-threshold/dependence assumptions. None repeats only its heading.
- All section titles/details summaries retained: physical mechanism or test question identifies contained material. Result titles use established metric/model names and simple physical nouns; uncommon exact terms are supported by local meanings or linked studied material. No fancy-word replacement is required.
- Old tools opening and ending route retained: explains what review page contains and where to start. Keeping the old table anchor helps existing links. Repeating the route at entry and old location serves different navigation entry points.

## Current source/rule binding

- `content/chapters/00-exam-review.md` SHA256 `af6404ec51657704ed23c07b72b7f5bdc1c08860b03c1297b10682888fd7c97c`
- `content/chapters/00-exam-review.yaml` SHA256 `86b252b5182d6e76ab288e1fc2b770b78dbc06352e86314bef126dd7e17bb54a`
- `content/chapters/00-mathematical-tools.md` SHA256 `06999cadaf9423ee8e18042d97b8148491d66e781b183f9d9af2414db37fcab5`
- `C:/Users/vital/.codex/skills/course-study-guide-builder/references/pedagogy-language-contract.md` SHA256 `f4c1eb544cf640b708e1970d9572fdc758fcc6aea806675d01a0256658df847a`
- `C:/Users/vital/.codex/skills/course-study-guide-builder/references/math-code-case-contract.md` SHA256 `ce2313f897b63e74ba59a3afe1bbc4046d3aa84584072cda7e76470a7e3cef9a`

- Verdict: one required local symbol-definition fix in P1; all other reviewed wording retained with reasons above. No stage3 reading-flow acceptance claimed. No memory used. Token stats unavailable.

## Narrow wording repair recheck

- Coordinator added the P1 positive-part definition, and I reread the whole P1 symbol key and its derivation/decoding. The new sentence says what the operator does and identifies u as a placeholder for z-q. It supplies the missing local meaning without reteaching probability or adding a new example. Required wording finding closed. Separate focused truth check is still requested by coordinator.
- Final stage2 wording verdict: PASS in this scope; no remaining required wording repair. No stage3 verdict claimed.
- Final source YAML SHA256 `86b252b5182d6e76ab288e1fc2b770b78dbc06352e86314bef126dd7e17bb54a`
- Final P1 first-cell SHA256 `16672c03207335f8106ee3c88f650c007e9389bc8c6d31600a7f1c724a390486`
- Actual host finish after wording recheck: 2026-11-04T19:24:01.815690+02:00. Wall elapsed since19:21:17.3891943: 164.4s; since previous checkpoint19:23:41.771338: 20.0s. Awake time unavailable.
