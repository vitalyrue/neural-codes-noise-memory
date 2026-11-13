# Eye drift: source and simulation evidence

UTC start inherited from parent: 2026-10-30T16:43:18Z. Checkpoint: 2026-10-30T16:46:39Z. Source research only; no manuscript edits, builds, simulation runs, raw-recording downloads, or visual checks. Wall time includes all time since the inherited start. Awake execution time cannot be separated without Windows sleep/resume logs, which were not queried.

Scope: Ben-Shushan, Shaham, Joshua and Burak (2022), *Fixational drift is driven by diffusive dynamics in central neural circuitry*, Nature Communications 13, 1697, https://doi.org/10.1038/s41467-022-29201-y. Local main text, SI1, SI2, SI5, existing eye chapters and synthesis inspected. Current GitHub code and Zenodo metadata independently checked on 2026-10-30. Statements below separate published Methods, code observations and guide teaching calculations.

## Main conclusions for the writer

1. There is real, public MATLAB model code. Do not describe code as unavailable or guess Python. The final paper p.12 explicitly links the repository. The current repository supplies `.m` functions and `.mat` parameter/data files; no runtime version is given in its README.
2. The paper has two different kinds of evidence: reanalysis of paired OMN/eye recordings supports a shared drive before OMNs; simulations test whether an integrator with neural noise can supply such a drive. The simulation match does not identify the integrator as the unique physical source.
3. The final main Methods p.11 state N=30,000, Nm=1,000, tau_s=20 ms, feedback A=.015. SI1 contains older figure/equation references and a 15,000-neuron example. Keep these values attached to their source, rather than mixing them.
4. The public code provides a concrete integration step, seed scheme and initialization, which are not specified in the main Methods passage. These are code settings, not a verified recipe reproducing every published figure.
5. Several code/paper differences and an absent function prevent claiming that the repository is a complete, tested figure reproduction package. No code was run in this research pass.

## Sources and live availability

| Item | Evidence and location |
|---|---|
| Final article | Local `C:/dev/clsc/burak-papers/research/ben-shushan-2022-main-text.txt`, PDF pp.1-13; online https://www.nature.com/articles/s41467-022-29201-y . Browser fetch redirected to inaccessible Nature identity endpoint, so detailed text claims use the already stored final PDF/text. |
| Supplement notes/figures | Local `C:/dev/clsc/burak-papers/research/ben-shushan-2022-si1.txt`, 14 PDF pages; source https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41467-022-29201-y/MediaObjects/41467_2022_29201_MOESM1_ESM.pdf . |
| Peer review | Local `C:/dev/clsc/burak-papers/research/ben-shushan-2022-si2.txt`, 35 PDF pages. Page 16 response promises annotated GitHub code; the final paper's public-code statement and live repository supersede that historical private-code status. |
| Reporting summary | Local `C:/dev/clsc/burak-papers/research/ben-shushan-2022-si5.txt` contains only the XFA PDF viewer placeholder. Its research-design fields were not read and must not be claimed as checked. |
| Model repository | https://github.com/The-Burak-lab/Fixational-drift-is-driven-by-diffusive-dynamics-in-central-neuralcircuitry , public, checked via GitHub page and API. Commit `27d4093008c6756fe8ae2ad77567176ed626bd17`; snapshot text and API tree saved in `eye-code-snapshot/`. |
| Raw recordings | Final paper p.12; https://doi.org/10.5281/zenodo.6076911 . Zenodo API https://zenodo.org/api/records/6076911 returned public CC BY 4.0 metadata and file list; full JSON saved in `eye-code-snapshot/zenodo-record.json`. Raw spreadsheet files were not downloaded. |

Zenodo describes one `.xls` file per recorded cell, one sheet per trial: horizontal and vertical eye angles in columns 1-2, spike times in column 3. Angles are degrees, eye sampling is 1 ms, spike times are milliseconds. To predict eye position, spikes were binned at 1 ms. This describes raw recordings, whereas `monkeys_MSD.mat` in the code repository contains already calculated empirical MSD data. Those two data products are different.

## What was recorded, fitted and compared

Main p.9, “Behavioral task and recordings”: earlier recordings from two male rhesus macaques; wire eye coil, brainstem electrodes, identified abducens OMNs; voltage sampled at 25 kHz, offline sorting with **Plexon and custom software**. This is the actual stated recording/sorting software. It does not establish that every later analysis used Plexon or any particular custom language.

Main p.9, Eqs.2-3: each OMN's parameters k, r, m, time shift Delta t and threshold E_T were **fitted to simultaneous recorded rate and eye motion**, including fixation and smooth pursuit, by squared-error minimization. Measured rate was inverse interspike interval; trials going below 20 Hz were discarded. The acceleration estimate used a third-order Savitzky-Golay filter with a 21 ms window and two-sided numerical differentiation. Prediction used leave-one-trial-out fitting.

Main pp.9-10: microsaccades detected using 2-D speed 10 deg/s and acceleration 1000 deg/s^2; remove 30 ms before/after; manual verification. Displacement/correlation analysis uses nonoverlapping 350 ms segments. Figure 2 has 57 OMNs across two animals and 302 eligible segments per cell on average. These are individual-cell recordings, not simultaneous population recordings (SI2 p.19). Simulated Figure 5e-f instead uses 57 simulated OMNs with 100 trials per OMN (caption p.8).

Main p.10, Eqs.11-17: recording analysis estimates shared variance fraction chi from covariance of measured eye displacement and single-OMN reconstructed displacement. It assumes calibrated/unbiased gain and uncorrelated shared and private noise. This is the recording result, not an integrator parameter fit.

Main p.10, Eqs.18-19 and SI1 p.8, Extended Data 2: measured eye MSD has an additive displacement-noise offset 2 Var(measurement error), about 10^-3 deg^2. In the synthetic check, add Gaussian white measurement noise to a known simulated trajectory, estimate/subtract the short-lag plateau, and compare with the known noise-free MSD. Do not call this synthetic Gaussian noise a measured physical neural input.

## Published generative model, in causal order

Main pp.10-11, Eqs.23-35; final main equation numbers should be used.

| Stage | Equation and meaning | Parameters and their status |
|---|---|---|
| Continuous attractor circuit | Eq.23: lambda_i^R = [zeta_i^R E_OI + lambda_i^0 + zeta_i^R F]_+; opposite tuning slope in matching left cell. Eq.24: tau_s dS_i/dt = -S_i + X_i. Eq.25: E_OI = sum_i eta_i(S_i^R-S_i^L). Eq.26: X_i = xi_i/(lambda_t+lambda_i). | Two paired left/right populations with within-population excitation and cross-population inhibition; architecture adapted from Aksay et al. (2007), a goldfish model. Neural spikes replace rates; tuning and variability adapted to primate evidence. lambda_t=60 Hz is a model choice. tau_s=.020 s in final main simulation. |
| Tuning distribution and fixed-point fitting | Eq.27: zeta_i = .032 E_T + 4.04 + Gaussian residual, in the paper's rate/angle units. eta_i optimized so mean-rate readout approximates a continuum of fixed points from -50 to +50 degrees. | Distribution regression and dispersion chosen to match McFarland and Fuchs (1992), correlation .61. Individual tuning curves sampled, not measured from the paper's 57 cells. Readout weights are optimized to maintain the attractor, not fitted to macaque drift trajectories. Exact zeta, lambda^0, eta are said to be in SI Data 1. |
| Motor neuron rates/spikes | Eq.28: lambda_i^M = [k_i(E_OI-E_Ti)]_+. Eq.29: tau_MN ds_i^M/dt = -s_i^M + xi_i^M. | OMN spikes generated with low interval variability. tau_MN is not assigned a numeric value in this main passage; public code sets .010 s. |
| Muscle/eye response | Eq.30: s_i^M = k_i(E_i-E_Ti) + r_i dE_i/dt + m_i d^2E_i/dt^2. Eq.31: E = (1/Nm) sum_i E_i. Equivalent to a double-exponential filter. | The model's OMN parameters sampled from literature-based distributions, not simply the parameters fitted to each recording. E_T uniform from -45 to -5 degrees; omit neurons whose thresholds exceed -5 degrees as negligible near central gaze. |
| Motor parameter distributions | Eqs.32-33: k_i=.18 E_T+8.07+epsilon_k; r_i=.02 E_T+1.23+epsilon_r. Gaussian residuals reproduce dispersion; correlations .81 and .67. k>=1.1, r>=.25. m sampled from typical values, constrained by m<r^2/(4k). | Relations from Fuchs, Scudder and Kaneko (1988), ranges/typical values from Robinson et al. (1981). Exact motor parameters said to be in SI Data 2; illustrated in SI1 p.13, Extended Data 9. |
| Delayed visual feedback | Eq.34: F(t)=A[E(t-tau_d)-E_OI(t)]. | tau_d approximately .070 s, based on physiological delay evidence; A=.015 chosen for main simulation agreement. Feedback mainly changes long-lag MSD slope and magnitude, rather than creating the short-lag superdiffusive slope. |
| Sub-Poisson spikes | Generate Poisson events at M times target rate and keep every Mth event. With constant rate this produces gamma-distributed intervals, CV=1/sqrt(M). Eq.35 chooses OMN CV from mean ISI plus Gaussian residual. | Integrator CV approximately .22; OMN CV about .07. These are experimentally motivated assumptions, not directly fitted neural noise time series. Eq.35 printed regression uses 10^-2[6.34 + .17 ISI + epsilon_CV], with ISI stated in ms. |

Final main p.11: N=30,000 integrator neurons, Nm=1,000 OMNs, tau_s=20 ms, A=.015. Main p.6 explicitly says many combinations of parameter values can reproduce the MSD magnitude; the model is not uniquely identified by the fit. Its diffusion scaling Eq.1 is a scaling argument rather than another directly measured output. Existing guide flags a normalization issue in that printed scaling formula, so avoid inserting a new unsupported numeric computation based on it.

## Actual public code and numerical procedure

All links below are fixed to the inspected commit. Local identical text snapshots are in `eye-code-snapshot/`; line references are to those snapshots.

Base URL: https://github.com/The-Burak-lab/Fixational-drift-is-driven-by-diffusive-dynamics-in-central-neuralcircuitry/blob/27d4093008c6756fe8ae2ad77567176ed626bd17/

| File | Verified role |
|---|---|
| `Run_model.m` | Main function takes N, nMN, redOI, A_feed, Time, NoOfTraj and branch argument `verbose`. Sets central gaze SE=0 (line 15), tau_s=.02 s, feedback delay .07 s, dt=1e-5 s (line 33), save interval MOD=100. Thus stored trajectory interval is 1 ms. Sets Seed=trajectory index (line 45), calls simulation per trajectory, then CalculateMSD. No default N, trial count, duration or thinning factor supplied by a documented worked invocation. |
| `Full_model_simulation.m` | Sets `rng(Seed)` (line 25), tau_MN=.01 s (28), loads or constructs OI fit and loads `OMNparameters.mat`. OMN populations trimmed or duplicated if requested count differs. Initializes rates for SE=0, synapses at the mean saturated drive, OMN position at readout, OMN synapses at starting rates, velocities=0, feedback=0 (lines 82-108). Randomly initializes thinning counters. |
| Same file: time loop | Spike candidates use `rand < M*dt*rate` tests then counters retain each Mth event (OI lines 155-168, motor lines 212-218). This is a discrete-time approximation of the paper's Poisson thinning. Synapses use first-order Euler decay (133,171-172); motor velocity uses an Euler increment (136), then position uses the new velocity (137). Feedback starts after the 70 ms delay (141-142). No adaptive ODE solver or stochastic differential equation library is called. |
| Same file: outputs | Saves OMN spike times, internal OI trajectory, final eye trajectory, per-OMN position contribution, step/save interval, total time, fixation target, noise-thinning and feedback settings (lines 186-199). An output name such as OMNprediction must not be confused with experimentally reconstructed position. |
| `Build_OI_circuit.m`, `Duplicate_OI_circuit.m` | Load a fitted circuit file if present; otherwise fit a small network or duplicate an existing 5,000/10,000 set, dividing readout weights by duplication count. The tree contains `NetParm_Fuchs_N_5000.mat` and `_10000.mat`. |
| `Fit_OI_circuit.m` | Samples tuning thresholds [-60,5] degrees with regression .032,4.04,.61; clips zeta>=1.2; uses eye-position grid [-50,50]; fits readout with `lsqlin`, bounds .1/N to 100/N and MaxIter=3000 (line 30). This optimization maintains the mean attractor. |
| `draw_from_linear_regression.m` | Samples uniform independent-variable values where applicable and normal residuals using `normrnd`; residual variance chosen from slope, independent-variable variance and desired correlation. |
| `CalculateMSD.m`, `msdFFT.m` | Compare generated trajectories with empirical `monkeys_MSD.mat`, compute MSD via autocorrelation and squared-position terms; `msdFFT.m` actually calls MATLAB `xcorr(...,'unbiased')`. README describes this as using Wiener-Khinchin/FFT. |

Software statement suitable for the guide: “The authors released MATLAB `.m` code and `.mat` model/data files. The entry function runs the time-stepped circuit and eye model and compares its MSD with recorded data. The repository does not specify a MATLAB version or a complete environment file.” Dependencies visible in source include `lsqlin`, `normrnd`, and `xcorr`; do not claim a checked toolbox/version installation.

## Limits of the public reproduction package

These are source observations, not run failures. They belong in a short reproducibility note, not in the main biological explanation.

- `Run_model.m` includes a `rate` branch calling `Model_wo_spiking_noise`; no such file is present in the current complete API tree. A full “rate branch works” claim is unsupported.
- The public `Full_model_simulation.m` line 71 samples OMN CV using slope .18, intercept 7.3, correlation .79, and clips CV to [.04,1]. It rounds thinning to 1/CV^2 and caps thinning at 400. These settings differ from the final paper's Eq.35 (.17, 6.34). The code uses a central-gaze expected ISI to set that OMN's thinning factor once, rather than continually resetting it.
- Code builds right and left vectors of length N, so its argument N counts entries in each paired population. The final paper calls N the number of network neurons. Do not silently equate a call with N=30,000 to the paper's total population count without resolving that counting convention. No data-file array sizes were inspected in this pass.
- Source line 135's restoring position term uses shared `X_0(i)`, while the printed Eq.30 uses the individual contribution E_i. This is an observed implementation difference; its effects were not tested.
- SI1 pp.4-5 uses 15K OI neurons, CV .20, 1K OMNs. SI1 p.9 no-feedback comparison uses N=40K, CV .23/Nm=1200 for short-lag fitting and CV .20/Nm=1500 for long-lag fitting. These are particular comparison settings, not the final main-method parameter set.
- SI1 p.10 Extended Data 4 and p.10 Extended Data 5 retain broken or earlier figure/equation cross-references. The content and page/figure labels identify the result; final main equation numbers must be used in prose.
- No installation, full simulation, timing benchmark, parameter-file content check or published-figure reproduction was attempted. Public code availability is verified; exact end-to-end reproducibility is not established.

## Numerical outputs and figure mapping

| Figure | Data source and output | What the result tests |
|---|---|---|
| Main Fig.1, p.3 | Recorded eye motion and single-OMN rates; fitted k,r,m,threshold and time-shift relation. | Calibration and weak but positive rate relation during fixation. |
| Main Fig.2, p.4 | Recorded and OMN-reconstructed 350 ms displacements. Mean R=.17 plus/minus .02; weighted shared variance estimate chi=.82 plus/minus .07. | A substantial common drive before OMNs, conditional on gain/independence assumptions. These values are not a direct measurement of diffusion inside the integrator. |
| Main Fig.3, p.6 | Empirical MSD with measurement-noise offset removed; black simulation of private OMN spikes filtered by motor/eye dynamics. | Independent private OMN variability has small, saturating displacement variance, unlike recorded continued drift. |
| Main Fig.4c-d, p.7 | Simulated integrator-only readout; 100 trajectories for MSD, log slope approaching 1 at sufficiently long lags. Main p.6: MSD over 350 ms of order .1 deg^2. | The noisy attractor's stored coordinate diffuses before muscle filtering. Figure 4c readout is not already a full physical-eye output. |
| Main Fig.5b-d, p.8 | Full model vs measured trajectories; plotted simulated trace digitized for visual comparison. Internal E_OI and smoother actual E separated. Model MSD matches magnitude and shape of measured MSD. | Sufficiency of combined noisy integrator, motor/plant filtering and delayed feedback. |
| Main Fig.5e-f, p.8 | Synthetic eye and OMN spikes analyzed with the same estimator as recordings: 57 OMNs, 100 trials each. Caption reports chi=.82 plus/minus .07; mean R=.17 plus/minus .02; one-sided t test p=10^-14 for synthetic R. | Can the measurement method recover the imposed central contribution despite noisy individual cells? Label these as simulation validation values; the recording R p value is 3.8*10^-12, not 10^-14. |
| SI1 Extended Data 2, p.8 | Synthetic Gaussian measurement-noise addition and subtraction, plateau 10^-3 deg^2 = twice position-error variance. | Validates measurement-noise subtraction when that noise model is true. |
| SI1 Extended Data 3, p.9 | Feedback/no-feedback MSD and log-slope comparisons. | Feedback lowers long-lag slope, improving quantitative matching. Distinct no-feedback parameters listed above. |
| SI1 Extended Data 4, p.10 | Synthetic constant OI command, peripheral motor spike noise only. chi=-.09 plus/minus .22; mean R=-.006 plus/minus .013, shuffle comparison p=.67. | A no-central-drive control, not evidence that the real recorded central drive is absent. |
| SI1 Extended Data 5, p.10 | Match monkey I using Nm=900; CV regression 10^-2[8+.18 ISI]; A=.060. | Example of adjusting literature-compatible model choices between animals. |
| SI1 Extended Data 9, p.13 | Tuning/model parameter distributions. | Shows sampled model diversity; not the fitted distribution of all experimentally recorded cells. |
| SI1 Extended Data 10, p.14 | Full simulation vs removing output/OMN spiking noise while retaining internal OI spiking to drive diffusion. Differences matter mainly at 1-10 ms. | Separates diffusion-driving internal noise from direct output spike fluctuations. The attractor is still stochastic in this control. |

## Contribution map for Part introductions

This map is checked against the current chapter Markdown, not inferred from file titles alone.

| Existing chapter(s) | Central author-year contribution | Supporting contribution | Guide-derived material to label |
|---|---|---|---|
| `04-eye-drift.md` | **Central: Ben-Shushan et al. (2022)**, recordings, calibration/inversion, covariance estimate of shared displacement drive. | Earlier recorded data reused by the study, including Chaisanguanthum et al. (2014); anatomical/integrator background gives context but does not itself supply the 2022 chi estimate. | Factorization of inverse filter, units/static gain/repeated-pole case; expanded residual-variance bound; ordinary-language account of assumptions. Footnotes explicitly call these guide derivations. |
| `04b-eye-timing.md` | **Central: Ben-Shushan et al. (2022)**, empirical MSD correction, distinction between saturating filtered private fluctuations and accumulating drive. | Mechanical filtering and measurement assumptions are the paper's model ingredients. | Normalized one-exponential example and full filtered-Brownian derivation are teaching reconstructions, explicitly labeled in footnote p2-white-noise. |
| `04c-eye-circuit.md` | **Central: Ben-Shushan et al. (2022)**, primate spiking integrator to full-eye model, feedback, parameter/noise checks and limits on localization. | **Supporting: Aksay et al. (2007)**, inherited goldfish integrator architecture; **McFarland and Fuchs (1992)**, primate OI tuning distribution; **Fuchs et al. (1988)** and **Robinson et al. (1981)**, motor-parameter constraints; **Burak and Fiete (2012)**, noise/diffusion scaling connection. These are supporting sources as used by the central paper, not additional coequal empirical eye-drift tests. | Derivation of mean readout self-consistency G(z); gamma/thinning interval-sum derivation; CV-drift integral steps; dimensional discussion of slope normalization; example calculations. |
| `06-synthesis.md` | **Central comparison: Burak and Fiete (2012), Ben-Shushan et al. (2022), Mainali et al. (2025)**. They address maintained state dynamics, physical eye movement and spatial field statistics respectively. | Current supporting sections discuss **Seung (1996)** and **Aksay et al. (2007)** for eye integrator background; **Burak and Fiete (2009)** for modeled path integration; **Nghiem et al. (2025)** for acuity/active-sensation relevance. Other synthesis supporting sources concern memory extensions or place coding and should be mapped by those specialists. | The joint calculation delta R_i approximately f_i'(x0) delta x and Cov(delta R_i,delta R_j) approximately 2Dt f_i'(x0)f_j'(x0) is a guide calculation linking objects. It is not a model jointly tested by the three studies. The proposed joint experiment is guide synthesis. |

Suggested Part-introduction statement: “The central study here is Ben-Shushan et al. (2022). It combines earlier macaque recordings with a model adapted from Aksay et al. (2007), using primate tuning and noise constraints from supporting studies. The filter calculations and worked examples marked ‘Guide derivation’ explain the paper's steps; they are not additional recorded results.”

For a new methods/simulations Part, use **Central: Ben-Shushan et al. (2022)** for that model case and **Supporting: Aksay et al. (2007)** where model inheritance is explained. Label a new run of code or simplified teaching implementation as **Guide simulation**, with its chosen parameters and outputs separated from the authors' published simulation.

## Scope of memory use

Memory registry only used to preserve the existing text/local-HTML versus deferred figure-acceptance boundary, not to establish new scientific or software facts. Relevant entry: `MEMORY.md:89-98`, rollout `01a16429-56cd-7531-92ce-552e368634a9`. All model and availability facts above were checked against current local sources or the live public repository/API.


Completion checkpoint: 2026-10-30T16:49:44.2262475Z. All findings above are source/code inspection, with no new simulation or full reproduction claim. Token stats unavailable.

