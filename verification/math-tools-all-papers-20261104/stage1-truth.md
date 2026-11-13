# Independent Stage 1: mathematical truth and source checks

Started UTC: 2026-11-04T14:26:30Z
Finished UTC: 2026-11-04T14:28:21.669131+00:00
Wall-clock elapsed: 112 seconds.
Awake execution time: unverified; no Windows sleep/resume logs inspected.
Token stats unavailable.

Scope: introduction, transition after the preserved bound section, and the four new sections SHARED, FILTERS, RANDOM-FIELDS, CROSSINGS-PEAKS in 00-mathematical-tools.md. No prior review reports consulted. Writer source maps were used only to locate primary passages. Actual paper PDFs and the listed source texts were checked independently. No manuscript edits or builds.

Verdict: no required mathematical or source-location corrections found within this scope. The explanations separate teaching constructions from paper results and retain the assumptions needed for the displayed claims. This is a truth review only, not wording or reader-flow acceptance.

## Paragraph-based checks

1. Introduction and transition from memory: the three reading paths accurately distinguish retained neural values, eye displacement inference, and spatial place field statistics. The transition does not identify current-state readout with preservation of the original value. No new bound is asserted beyond the preserved section.

2. SHARED, covariance definitions and teaching model: covariance units, correlation normalization and its finite-positive-variance qualification are correct. Under the specified independence assumptions, Cov(X,Y)=ab Var(S), Var(Y)=b²Var(S)+Var(eta_y), and the gain-adjusted fraction identity follow exactly for a nonzero a. The unit-gain example gives rho=1/sqrt(31.25)=0.178885 and fraction 0.8. The chosen variances are explicitly illustrative. Private variance in X can make rho small without reducing the shared fraction in Y.

3. SHARED, paper application: main PDF p. 9 Eqs. 4–7 defines the calibrated causal prediction; p. 10 Eqs. 11–15 defines common and private components and the 350 ms variance estimate. The chapter correctly presents calibration during drift as an assumption. Its small residual private covariance caveat matches the paper's order-1/N_m statement. Supplement PDF p. 2 Eqs. S1–S2 supplies the independent population bound. No causal conclusion is obtained from covariance alone in the teaching model.

4. FILTERS, definitions and response: the causal convolution, normalized exponential response, time-domain equation tau E'=U−E, and units agree. These equations describe the explicitly simplified first order response; the chapter does not mistake this response for the complete two-time-scale eye plant plus feedback model. White noise is correctly treated as a generalized signal with intensity rather than finite pointwise variance. The statements about stationary position refer to constant second moments and separation-dependent covariance, which the text spells out.

5. FILTERS, worked calculation: for nonnegative lag, overlap gives C_E(lag)=A exp(−lag/tau)/(2tau), so the plateau is A/tau and short-lag white-input MSD is linear. For Brownian command, velocity obeys the corresponding Ornstein Uhlenbeck equation with covariance D exp(−|s|/tau)/tau. Integrating it gives 2D[lag−tau(1−exp(−lag/tau))]. Its small-lag coefficient D/tau and large-lag growth 2D are correct. Units A=deg² s, D=deg²/s, C_v=deg²/s² and MSD=deg² agree. Filtered Brownian position is not called stationary; stationary increments require the stated relaxed velocity transient. Main PDF p. 10 Eqs. 18–22 supports the measurement-noise and white-filter discussion. Supplement pp. 4–5 supports the feedback qualification.

6. RANDOM-FIELDS, map and law: main PDF p. 3 and p. 13 Eqs. 2–3 support one sampled spatial map per cell, joint Gaussian values and thresholding. Mean removal and threshold rescaling are equivalent to the source's zero-mean convention. F=a[z−q]_+ has firing-rate units with a carrying rate units. Connected active components, not individual maxima, define fields. The chapter correctly distinguishes a fixed map traversed in time from repeated random draws.

7. RANDOM-FIELDS, covariance and regularity: Gaussian mean and covariance determine the finite-dimensional laws. Stationarity, isotropy and their difference are correctly stated. With positive height and slope variances, ell_c=sqrt(−C(0)/C''(0)) gives Var(z')=ell_c^−2. Main PDF p. 14 Eq. 4 and its simulated covariance match the chapter. The Gaussian covariance example is consistent with this local scale; the chapter correctly says that the scale alone does not fix distant correlations. The exponential covariance counterexample has a cusp at zero and fails the derivative requirement. Joint Gaussianity, differentiable sample maps and nondegenerate height/slope are explicitly retained; peak calculations add second derivatives.

8. CROSSINGS-PEAKS, exact counts: the slope-weighted integral, independence of normalized height and slope for stationary jointly Gaussian derivatives, and nu_+=exp(−q²/2)/(2 pi ell_c) are correct. This is an exact mean crossing density under the given regularity assumptions at every finite q, not a high-threshold approximation. Supplement PDF pp. 11–12 Eqs. S9–S13 supports the result despite some printed intermediate notation errors. Counting active components intersecting [0,L] adds precisely Pr(z(0)>q); main PDF p. 15 Eq. 8 has that endpoint term. The convention for clipped fields is correctly made explicit.

9. CROSSINGS-PEAKS, high peaks and size law: conditional directional second derivative has mean −b/ell_c² and b-independent conditional variance. At a typical high maximum, replacing b=q+epsilon by q in the leading curvature gives radius ell_c sqrt(2epsilon/q). For count-sampled high fields, U=q epsilon tends to a unit-mean exponential; the peak-count weighting changes only lower-order terms in dimensions above one. The size transformation s=v_d r^d yields survival exp(−beta S^(2/d)) with beta=q²/(2 ell_c² v_d^(2/d)). Hence 1D Rayleigh, 2D exponential and 3D exponent 2/3 agree with main PDF p. 3 Eq. 1. Beta has inverse size^(2/d) units, so the exponent is dimensionless. The chapter does not claim an exact finite-threshold size law.

10. Source algebra cautions: direct reading of supplement PDF p. 14 S22 gives radius sqrt(2epsilon/curvature magnitude), while printed S23 omits sqrt(2). Direct expansion of the exponential ratio on PDF p. 15 gives −q epsilon−epsilon²/2, despite the printed positive final quadratic term. The footnote accurately identifies both printed issues and keeps the correct limiting calculation. The chapter labels these formulas as a teaching reconstruction.

## Required findings versus unsupported concerns

Required fixes: none found.

Do not flag the first order eye filter for failing to reproduce the full model: it is expressly a teaching simplification with the full model deferred. Do not equate correlation with variance fraction: the gain and private contribution conditions are already present. Do not demand isotropy for the 1D crossing formula: stationarity and the supplied derivative conditions suffice. Do not reject the endpoint term because S12 omits it: the finite-domain counting convention and main Eq. 8 support it. Do not require finite-threshold peak laws: the chapter labels them limits.

Possible later wording clarification, not a mathematical error: “typical high fields” means selecting fields by their count, not selecting a random active location, which would favor larger fields. The present derivation uses the field-count meaning and its answer is correct.

## Actual input hashes (SHA-256)

- `guide/content/chapters/00-mathematical-tools.md`: `72091074fd3b5de6c4e5243be54f48c147a3eb68367cac62cfbef439329a8ef3`
- `research/ben-shushan-2022-main-text.txt`: `b52b017ad8d63af12d7301407e3cace4c0725b1f906ab3543b8a8014666c8eb5`
- `research/ben-shushan-2022-si1.txt`: `b636bfa42abc26bd1bc2dea5b3224ae14f92723ba5783f2aea3e1db8280b53b0`
- `research/mainali-2025-full-text-layout.txt`: `c5ea5963f2243b1b1e8fd409069973861492e9d2d83f0a574111724e4049ac86`
- `guide/assets/papers/ben-shushan-2022-fixational-drift.pdf`: `15f273f99bd8d8e8daa09a9f7809e04c53da514b146750c0ec517812e3478caa`
- `guide/assets/papers/ben-shushan-2022-supplement-1.pdf`: `323335499cb6428f68714fb1c855a9b87d5fe38449d31e26acce76417358a7d6`
- `guide/assets/papers/mainali-2025-universal-statistics.pdf`: `de2ca50a46f5b0d8d14e86269f1beacf6aadde7122bb348568aad92b12fd802e`
- `guide/assets/papers/mainali-2025-supplement.pdf`: `05af1fdf3079906871da12fdafa1f28895380f594a8c6bda3cafc5b503f07c31`
