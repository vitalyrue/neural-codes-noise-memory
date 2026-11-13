# Burak and Fiete source research and Part I contribution map

Read-only research assignment. No manuscript, build, lock, or shared record changed.

Measured checkpoints: first local inspection 2026-10-30T16:45:06Z; source/browser checkpoint 2026-10-30T16:46:58Z. Root task start supplied as 2026-10-30T16:43:18Z. Awake time is unverified because Windows sleep/resume logs were not read. Earlier chat labels 16:49/16:51 were mistaken estimates, not measured timestamps.

## Material finding: official 2017 correction

The supplied Early Edition PDF, main p. 2 Eq. 2, omits the square on the input slope in the numerator. **An official correction published May 8, 2017 confirms that precise error.** DOI: https://doi.org/10.1073/pnas.1706051114 ; full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC5441759/ ; PubMed: https://pubmed.ncbi.nlm.nih.gov/28483997/ .

The correction says: “The authors note that, due to a printer’s error, Eq. 2 appeared incorrectly.” The corrected equation is

\[
2D(\theta)=\frac{\sum_i \bar r_i(\bar g_i')^2}{[\tau\sum_i\bar r_i'\bar g_i']^2}.
\]

This agrees with supplied SI S18 (p. 4) and the current guide's equation. The correction changes no simulation settings. It does not address SI S40/S41, S71, S85, the exponential converse, or the main Eq. 6/S83 inequality direction. Keep those independent guide checks separate.

**Integration action:** `content/chapters/02-memory-dynamics.md:292` currently says the missing square is “not an author-confirmed correction.” That sentence is now outdated and should cite the 2017 correction. A Part introduction can describe the source as **Burak and Fiete (2012), with Eq. 2 corrected in 2017**. This is a narrow source update, not a reason to change the guide's correct equation.

## Sources read and live availability check

Local primary evidence: `../research/burak-fiete-2012-main.txt` (six PDF pages), `../research/burak-fiete-2012-si.txt` (20 SI pages), the main PMC HTML, and current Part I Markdown. Page numbers below are supplied PDF page numbers. Main bibliographic pages are PNAS 109(43), 17645–17650.

Live primary-source locations checked on October 30, 2026:

- Main article: https://pmc.ncbi.nlm.nih.gov/articles/PMC3491496/ and https://doi.org/10.1073/pnas.1117386109 . Its supplement area supplies supporting information, not an identified code archive.
- Fiete Lab old publications entry: https://fietelab.mit.edu/publications/ . The 2012 entry links main and SI PDFs: https://fietelab.mit.edu/wp-content/uploads/2018/12/infodiff_PNAS.pdf and https://fietelab.mit.edu/wp-content/uploads/2018/12/infodiff_PNAS_SI.pdf .
- Current Fiete Lab publications: https://fietelab.github.io/publications/ . The 2012 entry links the paper; no code link appears with this entry.
- Burak Lab publications: https://www.buraklab.me/publications . Its 2012 entry links PNAS; no code link appears with this entry. The page labels itself updated February 2025.
- https://github.com/orgs/FieteLab/repositories was accessible; it is a general lab list, not evidence of this paper's software. The attempted organization URL for The-Burak-lab returned 404 and cannot support an absence claim.

**Safe tools statement:** The paper documents its equations, Euler integration, time steps, and spike generation. It does not identify a programming language, simulator package, plotting package, operating system, hardware, random seed, or code version. No public code or simulation-data archive was identified in the checked paper/supplement and author publication entries. This limited search does not prove that no code exists. Do not infer MATLAB or Python from other lab projects. There are no new animal recordings in this theoretical/simulation paper.

## What was simulated, and why

The full model is a recurrent linear nonlinear Poisson network. Each emitted spike raises its neuron's synaptic activation by one; activation then decays:

\[
\dot s_i+s_i/\tau=\sum_a\delta(t-t_i^a),\quad
g_i=\sum_jW_{ij}s_j+b_i,\quad r_i=\phi(g_i).
\]

Main Eqs. 7–9, p. 5. Stochastic spike timing feeds back through recurrent input. The simulation checks whether the paper's diffusion formula predicts the wandering memory, rather than fitting the formula to an observed biological diffusion rate.

The analytical approximation replaces the spike drive with mean rate plus Gaussian fluctuations of covariance `r_i(t) delta_ij delta(t-t')` (main Eqs. 10–11, pp. 5–6; SI I, pp. 1–2). This approximation is distinct from the direct stochastic spike simulation. It requires many incoming spikes and small input fluctuations; expressions keep the leading order in the large-population expansion. The deterministic rate model must have a continuous family of stable states, with systematic drift removed to the stated order. Stable directions relax while noise along the neutral direction changes the stored value. SI S7–S18, pp. 3–4, gives the linearization and left-null-vector calculation used to predict `2D=sum_i v_i^2 r_i`.

### Ring network: main Fig. 2A–D, Methods p. 6

| Item | Reported setting or procedure |
|---|---|
| Network | N=1,024; neuron labels `theta_n=2*pi*n/N`; rotationally invariant inhibitory connections |
| Weights | `W_ij=w(theta_i-theta_j)`, `w(theta)=A exp[k1(cos(theta)-1)]-A exp[k2(cos(theta)-1)]`; A=1, k1=1, k2=0.3 |
| Transfer rules | `tau*phi(g)=10 exp(g)` or `tau*phi(g)=0.2[1+tanh(g+4)]` |
| Bias and decay | Common b=-2; tau=10 ms |
| Initial state | Independent uniformly distributed activation values between 0 and 0.01 |
| Duration/repeats | 100 trials, each 1,000 s |
| Integration | Stochastic Euler; dt=0.1 ms |
| Spike generation | At each step a spike is generated with probability `r_i(t)*dt` |
| Decode | Find the angle of the neuron with maximal instantaneous firing rate at each step |
| Measure | Average squared angle differences across lags and time, excluding first 10 ms; wrap differences to (-pi,pi) |
| Predict | Solve noise-free steady tuning numerically, insert into D and J formulas (main Eqs. 2,3; corrected Eq. 2), then compare with measured MSD |

The simulation Methods use the above literal finite-network weights. SI S6 uses `W_ij=(1/N)w(theta_i-theta_j)` to define a large-N scaling limit. Do not silently add another factor of 1/N to the finite simulation parameters.

Fig. 2B illustrates one spike-driven trajectory and snapshots 10 s apart, with peak rates about 85 Hz. Fig. 2C compares short-lag diffusion for exponential and sigmoid transfer functions with the parameter-free theoretical prediction; sigmoid diffusion lies above its information bound. Fig. 2D includes long lags, where wrapped angular error levels off rather than growing without limit. Its prediction uses SI S32, pp. 7–8, with periodic boundaries, not a line formula extended forever. Error bars in C,D are SEM over 100 trials. The maximal-rate decoder is a numerical method used for this ring, not the paper's ideal memory-readout estimator.

### Mutual inhibition: main Fig. 2E–G, Methods p. 6

| Item | Reported setting or procedure |
|---|---|
| Network | Two neurons, equivalently two populations |
| Weights | W11=W22=0; W12=W21=-1 |
| Bias/transfer | Common b=5,000; linear `tau*phi(x)=x` over valid positive rates |
| Decay/integration | tau=100 ms; Euler dt=0.4 ms |
| Duration | Tmax=200 s |
| Spiking | Inhomogeneous Poisson process with rate from current recurrent state |
| Readout/measure | Rate difference `Delta r=r1-r2`; average `[Delta r(t+T)-Delta r(t)]^2` over t from 0 to Tmax-T |
| Initial state, seed, independent repeat count | Not specified in this Methods paragraph |

This checks a nonperiodic memory model whose continuous states do not come from ring rotation. For two populations with M cells each, weights scale as W/M and group rates are sums of individual-cell rates. Large group rates must not be presented as ordinary 25,000 Hz firing by two biological neurons. The ring's Bernoulli one-spike-per-step rule cannot simply be reused at these aggregate rates: near equal activity, a group emits an expected 10 spikes per 0.4 ms. The source specifies a Poisson process here but does not document its count sampler or event handling. A reconstruction needs to make this choice explicit.

Coordinate caution: the paper writes fixed states `2*tau*r = theta*(1,-1)+b*(1,1)` and predicts `D_theta=b/(2*tau)`. Thus theta is an activation difference, whereas a literal rate difference is theta/tau and has diffusion `D_theta/tau^2`. The supplied Methods also print `r_i=g_i` beside the stated rule `tau*r_i=g_i`. The current guide makes the activation coordinate explicit. Do not mix the rate-difference axis and activation-coordinate diffusion formula in a new table or reproduction.

### Mutual excitation: SI Fig. S1 and S38–S41, pp. 8–10

Two units have zero self weights, cross weights +1, linear `phi(x)=x/tau`, and bias `(b0,-b0)`. Fixed activations are `(theta+b0/2,theta-b0/2)`. Fig. S1 starts all trials at Theta=100; B compares variance across **4,000 random trials** with theory. The figure's horizontal range is 0–5,000 ms. The SI does not give b0, tau, integration step, seed, or a full simulation protocol for this figure. Do not manufacture those values from a plot slope.

The point is that state-dependent diffusion need not produce a curved variance trace: linear D(theta) gives a linear variance dependence while the model remains in its valid positive-rate domain. **Printed discrepancy:** S40 gives D=theta/(2*tau), but S41 gives variance Theta*t/(2*tau). Under `Var=2Dt` and the stated activation coordinate, direct projection gives D=theta/(4*tau), consistent with S41. The present guide explicitly reports this as its own check. The 2017 correction does not resolve it.

### Readout curves: main Fig. 3 and SI Fig. S2

These illustrate derived estimation formulas, not additional documented spiking-network simulation protocols. SI VI, pp. 12–16, assumes a locally Gaussian spike-based observation, locally constant D and J, and estimates the state at the start of readout from later observations. The ideal estimator is equivalent to a reverse Kalman filter. Its variance term is `sqrt(2D/J)*coth(sqrt(2DJ)*DeltaT)` (S75); naive equal-time weighting gives `(2/3)D*DeltaT+1/(J*DeltaT)` (S79). Fig. S2 sets available spike fraction alpha=0.1 and rescales time/error. Neither figure establishes a biological circuit implementing the ideal estimator. The main Fig. 3 caption's SI numbers are stale; use S75 and S79–S81 in the supplied SI.

Main Eq. 5 and SI S75 give characteristic ideal-readout time `1/sqrt(2DJ)<=tau` under the model assumptions. Partial readout replaces J with alpha J only under the suitable information-access assumption. The guide also separates storage variance before recall from readout variance after it. Its critique of main Eq. 6/S83 is a guide calculation, not the 2017 correction.

## Limits to carry into Part IV

- This is model validation against stochastic simulations, not a fitted explanation of all biological memory errors.
- The direct Poisson diffusion expression is not established for arbitrary correlated spike trains or sub-Poisson oculomotor spiking. Main Discussion p. 5 calls broader extensions conjectures.
- Gaussian noise with fixed strength and two neural time scales are analytical extensions (SI VII, pp. 17–19), not documented additional figure-specific simulation studies. With two time constants, the bound uses their sum.
- Exponential transfer is sufficient for equality with symmetric weights and Poisson noise. Current guide supplies a linear-family counterexample to an unrestricted “only if” claim; do not repeat the printed converse as a universal result.
- Ring error saturation comes from bounded angular reporting. It does not mean the original angle has become recoverable.
- For a reproduction, label any language, library, seed, Poisson count sampler, convergence check, timestep study, FFT implementation, or hardware benchmark as a guide choice unless a further primary source supplies it.

## Compact Part I contribution map from actual current Markdown

Current chapter plan Part I contains Chapters 1–6 below. The central research source is Burak and Fiete (2012). The official Eq. 2 correction is Burak and Fiete (2017), DOI above. Supporting sources provide context; guide-derived material expands or qualifies source results.

| Chapter/file | Central source contribution | Supporting or guide-derived material |
|---|---|---|
| 1 `01-foundations.md` | 2012 Poisson spike model and input-free population representation; main Eqs. 7–10, SI S43 | Eye-motion context: Ben-Shushan, Shaham, Joshua, and Burak (2022), main Figs. 1–2 and Methods Eqs. 2–7. Spatial-map context: Mainali, Azeredo da Silveira, and Burak (2025). Later CA3/CA1 context: Maimon and colleagues (2026), explicitly later than the 2025 paper. Finite Poisson count/pooled-count examples and covariance/measurement-error calculations are guide teaching calculations. |
| 2 `01b-persistence.md` | 2012 Introduction, Fig. 1, SI I–III: persistent family, stable versus neutral directions, noise-driven memory loss | Two-activity angle example is an invented teaching model, not the paper's simulation. Independent-step/Brownian derivations, bias comparison, and covariance-in-time expansion are guide teaching steps. Fixed random map distinction uses Mainali et al. (2025). Cross-paper map is the guide's comparison, not a demonstrated common circuit. |
| 3 `02-memory-dynamics.md` | 2012 main Eqs. 1,7–11 and SI S1–S27: spiking, large-N approximation, linearized dynamics, left projection, scalar/matrix diffusion, symmetric formula | Brownian increment notation, expanded left-vector explanation, and tilted linear-decay example are guide derivations. Mutual-inhibition example uses the source network but explicit activation coordinate and b=20 illustration are guide choices. Add 2017 correction attribution to squared numerator. |
| 4 `02b-memory-long-delays.md` | 2012 SI S28–S41, systematic drift discussion, main Figs. 1–2 and SI S1: domain/boundary effects and state-dependent diffusion | Uniform angular variance calculation; explicit factor-of-two check in S40/S41; covariance projection `2D=v^T C v`; explanation of limits on correlated-noise claims are guide derivations/qualifications. The source itself says its broader correlated-noise extension is conjectural. |
| 5 `03-memory-information.md` | 2012 main Eqs. 3–4, SI S42–S56: internal Fisher information, information-diffusion inequality, multidimensional result, sensory-memory comparison | Expanded score/CR proof, shorter projection proof, residual-matrix proof, linear-family counterexample, explicit held-quantity comparisons, tuning-width integral and alternative total-rate budget are guide derivations. The width argument is discussed in 2012, which cites Zhang and Sejnowski; this assignment did not independently read that cited paper. |
| 6 `03b-memory-readout.md` | 2012 SI S57–S95, main Eq. 5, Figs. 3/S2: storage/readout split, naive/ideal estimators, partial access, two timescales, fixed Gaussian noise | Double-integral covariance proof, backward precision recursion, random-thinning explanation, retained Gaussian noise-strength q, and checks of S71/S85/main Eq. 6/S83 are guide derivations. Do not imply the ideal readout was implemented as a biological circuit or tested in new data. |

Suggested Part I introduction attribution, for adaptation: “The central source is Burak and Fiete (2012), which derives a limit on how accurately a noisy continuous-attractor network can preserve a value and tests its diffusion formula in simulated networks. We use its 2017 correction to Eq. 2. Ben-Shushan and colleagues (2022), Mainali and colleagues (2025), and Maimon and colleagues (2026) supply the eye-motion, spatial-map, and later anatomical context. The worked examples, expanded proofs, and explicitly marked checks of printed equations are calculations developed for this guide.”

This source research is not an independent acceptance review of new manuscript text. No full tests or visual document checks were performed.

Completion checkpoint: 2026-10-30T16:48:58Z. Wall-clock elapsed since supplied root start: 5 minutes 40 seconds. Time since measured previous checkpoint: 2 minutes. Own measured source-work interval: 3 minutes 52 seconds. Awake execution time remains unverified. Research scope complete; token stats unavailable.
