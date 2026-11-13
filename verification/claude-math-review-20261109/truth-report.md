# Truth-and-reasoning review: tools chapter, memory dynamics, memory information, place sizes, place tests

I found no false equation or wrong number in the five chapters. I recomputed every displayed derivation and every worked number by hand, and they hold. The findings below are about meaning, not arithmetic: symbols used without a definition, one symbol standing for different things, two "cells" examples whose rates are too high for single neurons, one claim that needs a condition, and source claims I couldn't check.

## 1. What I read, and the limits

**Read:**
- All five assigned chapters in full: `00-mathematical-tools.md`, `02-memory-dynamics.md`, `03-memory-information.md`, `05b-place-sizes.md`, `05c-place-tests.md`.
- The supporting passages you supplied, to check what earlier chapters actually teach: the reading guide, `01-foundations.md`, `01b-persistence.md` and `04b-eye-timing.md`.

**Not available to me:**
- The paper and supplement PDFs.
- The figure and table blocks (`{{block:…}}`).
- The chapters `ch-place-fields`, `ch-memory-long-delays`, `ch-memory-readout` and `ch-eye-drift`, and the Exam review.

**What that means:**
- The tools available here are document tools only, so I couldn't open local files or run code. All arithmetic was checked by hand.
- I can't confirm any equation number, page locator, figure value or printed-erratum claim. That includes the 2017 correction, the S18/S23/S25 errors, the Figure 3C–D exponents, the processing details, "35 results", and the mouse/rat labelling.
- The guide-derived counterexamples and reconstructions are checked as mathematics only.

## 2. Findings, in priority order

**F1. A symbol is used before it is defined (medium)**
- **Where:** [00-mathematical-tools.md:209](C:\dev\clsc\burak-papers\guide\content\chapters\00-mathematical-tools.md) and 223.
- **Excerpt:** "$\chi_Y=\frac{b^2\operatorname{Var}(S)}{\operatorname{Var}(Y)}$"
- **Problem:** $\chi_Y$ first appears inside the equation. Line 213 then says "shared variance fraction" without connecting it to $\chi_Y$. The 0.80 in the example is the key number in this section, and the reader can't tell what it measures.
- **Fix:** Before the equation, add: "Let $\chi_Y$ be the fraction of $Y$'s variance contributed by the shared command, $b^2\operatorname{Var}(S)/\operatorname{Var}(Y)$." Also state that the second form needs the gain ratio $b/a$, which calibration supplies.

**F2. One letter stands for several things within the tools chapter (medium)**
- **Where:** [00-mathematical-tools.md](C:\dev\clsc\burak-papers\guide\content\chapters\00-mathematical-tools.md):243 and 100, 237, 277, 19, 199, 317, 87, 240, 365.
- **Problem:**
  - $\tau$ is the synaptic time constant in the bound $D\ge1/(2\tau^2J)$ (line 152). It is then reused at line 243 as the muscle response time, with no warning. 04b:150 does give that warning, but later.
  - $h$ means three things: the observation window (100), the impulse response (237) and the spatial input map (277).
  - $b$ means three things: a bias (19), a gain (199) and a length (317).
  - $K$ is both a matrix (60) and a spike count (87). $U$ is both the filter input (240) and the scaled excess (365).
- **Why it matters:** The chapter's purpose is to tie each variable to a physical part of the system. A reader can reasonably think the muscle filter's $\tau$ is the memory circuit's $\tau$.
- **Fix:** At line 243, write $\tau_m$ (or add the 04b:150 sentence). Rename the filter kernel (for example $k(u)$) or the window (for example $T$). Use $g_X, g_Y$ for the gains, as 01-foundations:344 already does.

**F3. The left vector is defined by its effect, not by a condition the reader can use (low–medium)**
- **Where:** [00-mathematical-tools.md:60–62](C:\dev\clsc\burak-papers\guide\content\chapters\00-mathematical-tools.md).
- **Excerpt:** "If a right eigenvector $\mathbf u$ satisfies $K\mathbf u=\lambda\mathbf u$…" then "It need not point along the tangent $\mathbf u$"
- **Problem:**
  - $\mathbf u$ is introduced as a generic eigenvector with eigenvalue $\lambda$, then silently becomes the neutral tangent (eigenvalue zero).
  - The key statement $\delta\theta=\mathbf v^T\delta\mathbf s$ is never given its defining conditions, $\mathbf v^TK=0$ and $\mathbf v^T\mathbf u=1$, in the main text. They appear only in the folded example (76).
- **Fix:** Write a generic eigenvector as $\mathbf z$, as 02:107 does. Then add: "The tangent $\mathbf u$ satisfies $K\mathbf u=0$. The left zero vector satisfies $\mathbf v^TK=0$, normalized by $\mathbf v^T\mathbf u=1$."

**F4. Units called "cells" fire at rates single neurons can't sustain (medium, physical meaning)**
- **Where:** [02-memory-dynamics.md:303](C:\dev\clsc\burak-papers\guide\content\chapters\02-memory-dynamics.md) and [03-memory-information.md:254](C:\dev\clsc\burak-papers\guide\content\chapters\03-memory-information.md).
- **Excerpts:** "two mutually inhibiting cells", and "both rates are $1000\,\mathrm{s}^{-1}$"
- **Problem:** 1000 spikes/s is not a sustainable rate for one neuron. Also, the weak-fluctuation Gaussian description (02:41) needs many contributions, and a single cell doesn't supply them. The tools chapter (34) calls these "populations", and 01:296 says each unit "can represent two groups of neurons".
- **Mathematical status:** The variance result $2D=\bar r_1+\bar r_2$ still holds, because this model's dynamics are linear over the positive range. It is the Gaussian distribution and the "cell" label that are wrong.
- **Fix:** Call them "units (populations)". Add one sentence: the variance formula is exact for this linear model, while the Gaussian description of the displacement requires each unit to pool many neurons.

**F5. A published-correction claim I couldn't verify, and it sits uneasily with the reading guide (medium)**
- **Where:** [02-memory-dynamics.md:290](C:\dev\clsc\burak-papers\guide\content\chapters\02-memory-dynamics.md).
- **Excerpt:** "Burak and Fiete's published correction (2017) confirms the squared expression"
- **Problem:** The mathematics supports the squared $g_i'$: I rederived it from the projection, and SI S18 is cited as agreeing. The existence and content of the 2017 correction can't be checked from what was supplied. Separately, 00-reading-guide:196 says the guide's source checks are "not author-confirmed corrections". A reader will see a conflict.
- **Fix:** Confirm the DOI and what it says. Then add one clause to reading-guide:196 to exempt this case.

**F6. $Q(q)$ is used without a definition in the place-tests chapter (low–medium)**
- **Where:** [05c-place-tests.md:104, 109–114, 141](C:\dev\clsc\burak-papers\guide\content\chapters\05c-place-tests.md).
- **Excerpt:** "Corners supply $Q(q)$ in total" and "$Q(q)\simeq\phi(q)/q$"
- **Problem:** The tools chapter writes $\Pr[z(0)>q]$ (line 343), not $Q$. I couldn't check whether `ch-place-fields` defines $Q$.
- **Fix:** If it doesn't, add: "$Q(q)=\Pr(z>q)$, the Gaussian upper-tail probability."

**F7. A figure's result is stated without the values that produce it (low–medium)**
- **Where:** [02-memory-dynamics.md:191](C:\dev\clsc\burak-papers\guide\content\chapters\02-memory-dynamics.md).
- **Excerpt:** "As $y$ decays, $x$ changes by one."
- **Problem:** The shift equals $(a/\lambda)y_0$. The text never gives the figure's $a$, $\lambda$ or $y_0$, so the reader can't check the "one" against the formula above it.
- **Fix:** State the plotted values, for example "With $a/\lambda=1$ and $y_0=1$…".

**F8. A claim that is true only for positive thresholds (low)**
- **Where:** [05c-place-tests.md:214](C:\dev\clsc\burak-papers\guide\content\chapters\05c-place-tests.md).
- **Excerpt:** "decreasing $q$ increases them"
- **Problem:** The crossing rate is $\nu_+\propto e^{-q^2/2}$. It rises as $q$ falls only when $q>0$; for $q<0$ it falls.
- **Fix:** Write "for the positive thresholds fitted here", provided the fitted $q$ values are positive. I couldn't check the table.

**F9. Matrix equality asserted, only scalar equality derived (low)**
- **Where:** [03-memory-information.md:394](C:\dev\clsc\burak-papers\guide\content\chapters\03-memory-information.md).
- **Excerpt:** "For an exponential network that attains the matrix bound"
- **Problem:** The chapter derives only the scalar equality condition. The matrix case does hold for symmetric exponential networks: each $\mathbf v^\alpha$ lies in the span of $\mathbf g'^\beta\propto\mathbf r'^\beta/\bar{\mathbf r}$, so $V=U(U^TU)^{-1}$ and $Q=0$. That isn't shown. Also, line 298 uses $u_i^\alpha=\tau\,\partial_\alpha\bar r_i$ without restating it.
- **Fix:** Add one sentence with that span argument and a reminder of $u_i^\alpha=\tau\partial_\alpha\bar r_i$.

**F10. Wrong word for the time constant (low)**
- **Where:** [03-memory-information.md:359](C:\dev\clsc\burak-papers\guide\content\chapters\03-memory-information.md).
- **Excerpt:** "A larger cellular time constant"
- **Problem:** $\tau$ is the synaptic decay time everywhere else in these chapters.
- **Fix:** Change to "synaptic time constant".

**F11. Unclear whether an example uses the paper's parameters or the guide's (low)**
- **Where:** [00-mathematical-tools.md:53](C:\dev\clsc\burak-papers\guide\content\chapters\00-mathematical-tools.md).
- **Excerpt:** "a deterministic calculation with the paper's tuned parameters"
- **Problem:** The footnote calls this calculation a "teaching reconstruction". The reader can't tell whether $W=-1$ and $\phi=g/\tau$ are the paper's values.
- **Fix:** Say "with weights tuned as in the paper's mutual-inhibition model", or confirm the values against PDF p. 6.

**F12. A matrix $Q$ appears with nothing to refer to (low)**
- **Where:** [00-mathematical-tools.md:172](C:\dev\clsc\burak-papers\guide\content\chapters\00-mathematical-tools.md).
- **Excerpt:** "For any matrix $Q$ and vector $\mathbf z$… this is the nonnegative quantity used in that proof."
- **Problem:** $Q$ refers to a proof the reader hasn't seen yet.
- **Fix:** Delete the sentence, or name $Q$ as "the residual matrix in Chapter 5".

**F13. $S$ changes role between adjacent passages (low)**
- **Where:** [00-mathematical-tools.md:373 vs 385–401](C:\dev\clsc\burak-papers\guide\content\chapters\00-mathematical-tools.md).
- **Problem:** $S$ is the random size at line 373 but a fixed threshold size at lines 385 and 401, where the random size becomes $s$.
- **Fix:** Use $s$ for the random size and $S$ for the threshold throughout.

**Outside this stage, for the terminology pass:** Some terms get two first-definition marks:
- "left zero vector" (tools:62) and "left zero eigenvector" (02:127) are two names for one object.
- "Hessian" is marked at tools:347 and again at 05b:30.

## 3. Prerequisites, checked against the earlier chapters

Nothing essential is missing apart from F1 ($\chi_Y$) and F6 ($Q(q)$, if `ch-place-fields` doesn't define it). What the reading path supplies:

- **Poisson facts:** The tools chapter (100) states mean = variance inline before Chapter 1 teaches the Poisson distribution. That is enough for its use there.
- **Central limit theorem:** Used at tools:87 and 05c:263. It falls within the declared basic-probability background.
- **Brownian motion:** The tools fold (261) uses "Brownian" before 01b:126 defines it. Main-text line 247 already gives the $2D\ell$ meaning, so I count this as adequate. Optionally write "diffusing" in the fold.
- **Conditioning on a probability-zero event:** Taught at tools:321.
- **Joint Gaussianity and independence:** Taught at tools:279–292.
- **Conditional Gaussian mean:** Taught at 05b:56.
- **Positive semidefinite order:** Defined at 03:298.
- **Cauchy–Schwarz:** Explained at 03:143 and 03:169.
- **Gamma function, Weibull distribution, Betti numbers, Morse theory, skew, kurtosis:** Each is defined where it is first used.

## 4. Material that is adequately taught

I checked each item below and it holds.

**[00-mathematical-tools.md](C:\dev\clsc\burak-papers\guide\content\chapters\00-mathematical-tools.md)**
- Two-unit fixed-line algebra (40–53) and the tilted-decay example (68–76).
- Poisson Fisher information and the worked numbers 0.02, 0.5, 0.52 and the 25× ratio (100–129).
- Cramér–Rao bound and bound units (140–155). Singular-$J$ example (165–172).
- Covariance model and the numbers ρ≈0.18, χ=0.80 (199–224).
- Filter results: $C_E=\frac{A}{2\tau}e^{-\ell/\tau}$, and $M_{\rm diffusion}$ with both of its limits (253–268).
- Gaussian counterexample (287–289). Correlation length (311). Rice formula (326–338). Endpoint correction (343).
- Change of variables (367–380). β and the size laws (385–403).

**[02-memory-dynamics.md](C:\dev\clsc\burak-papers\guide\content\chapters\02-memory-dynamics.md)**
- Compensated spike-count noise and the $1/n$ scaling (25–67).
- Linearization, $K\mathbf u=0$, and left-vector orthogonality (85–150).
- Slide-while-decaying example, including $\mathbf z$ and $\mathbf v^T\mathbf z=0$ (158–181).
- $2D=\sum v_i^2\bar r_i$ and its multi-coordinate version (201–228). Dual-weights example (234).
- Symmetric derivation of $K^T\mathbf g'=0$ and the normalization (256–287).
- Two-unit result $2D=b/\tau$ and the unit conversion to 01b (303–313).

**[03-memory-information.md](C:\dev\clsc\burak-papers\guide\content\chapters\03-memory-information.md)**
- Background-spike example: information ×1/4 (36–43).
- Score and $E[S^2]$ derivation (84–115). Cramér–Rao proof (135–151).
- Cauchy–Schwarz bound and units (169–204).
- Equality condition $c=1/(\tau J)$ and the exponential solution (208–226). The linear mutual-excitation counterexample is valid and stable (231–242).
- Numbers 1000, 1000, then 1/15 and 750 (254–270). Residual-matrix identity (298–319).
- Scaling with $N$, rate, and $\tau$ under each stated held-fixed condition (341–356). Width scaling $w^{d-2}$ and the fixed-budget $w^{-2}$ alternative (376–404).

**[05b-place-sizes.md](C:\dev\clsc\burak-papers\guide\content\chapters\05b-place-sizes.md)**
- Conditional Hessian mean and gradient independence (48–63). Excess law (78–95).
- $s$ and $\epsilon$ in 1D (99–105). $v_d$ values and β (135–143). Density, moments, Weibull mapping (156–212).
- Means 0.5013 / 0.2513 / 0.1260 and the general $(\sqrt{2\pi}\sigma/q)^d$ (215).
- Exact mean 3.746 m vs 5.469 m (46.0%), and 3.73% at $q=5$ (219).
- Slice restriction (240–249). Rayleigh boundary-slope law and the width cross-check giving $\beta=q^2/(8\sigma^2)$ (286–306).

**[05c-place-tests.md](C:\dev\clsc\burak-papers\guide\content\chapters\05c-place-tests.md)**
- Euler-characteristic examples and the Morse sign logic (17–40).
- Signed densities $\eta_{1,2,3}$, including the κ cancellation and the three integrals (44–98).
- Box formulas and rectangle generalization (104–119). Value −20.06 at $L/\sigma=10$, $q=0$ (129).
- High-threshold count recovering $\mu_s$ (133–141). Cutoff shift $q+t/a$ (145).
- Moment definitions (173). Wiring covariance and $\sqrt\pi b$ autocorrelation with $\sqrt2$ width (256–305).

**How each file separates guide reconstructions from paper claims:**
- **Tools chapter:** Done in the footnotes. F11 is the one blur.
- **Memory dynamics:** Clear, apart from F5.
- **Memory information:** Exemplary. The converse counterexample is explicitly labelled as the guide's own calculation.
- **Place sizes:** Clear. The erratum claims are unverified here.
- **Place tests:** Clear. The data claims are unverified here.