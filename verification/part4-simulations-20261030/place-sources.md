# Mainali et al. (2025): simulation and source evidence

Research checkpoint: 2026-10-30T16:47:17Z. Root task started 2026-10-30T16:43:18Z. Wall time at checkpoint: 3m59s. Awake execution time is unverified; no Windows sleep/resume or clock-change claim is made. Model assigned by root: GPT-6.1-sol, high reasoning. Token stats unavailable.

This is a source record for the writer, not acceptance of a new chapter. Only this report was written. No manuscript, build, tests, or shared files were changed. The paper and code were read, not executed.

## Sources read and live access

- Main article: `../research/mainali-2025-text-columns.txt` and `../research/mainali-2025-full-text-layout.txt`, corresponding to `papers/mainali-2025-universal-statistics.pdf`. DOI: https://doi.org/10.1016/j.neuron.2025.01.017 . PDF pages 13–15 are STAR Methods pp. e1–e3. PDF p. 10 is printed p. 1118, including resource availability.
- Supplement: `verification/writers/place-supplement.txt`, from `papers/mainali-2025-supplement.pdf`. Its cover is PDF p. 1; printed p. 1 starts at PDF p. 2. URL: https://ars.els-cdn.com/content/image/1-s2.0-S0896627325000431-mmc1.pdf . Methods S1–S4 occupy printed pp. 8–14; Figures S1–S5 printed pp. 1–7.
- Live public repository: https://github.com/5183nischal/gp-model . Current `main` commit returned by GitHub API: `eae7eab801bb6ca016b3a6ff4f35d6a47df98d6a`. Inspected README, pyproject, Gaussian-field utility, 1D/3D model and analysis classes, and 2D analysis class. The exact published archive was also read, so the methods below do not depend only on current `main`.
- Published code DOI https://doi.org/10.5281/zenodo.14650880 is a concept DOI. Live REST response from https://zenodo.org/api/records/14650880 resolves to version record `14650881`, DOI https://doi.org/10.5281/zenodo.14650881 , published 2025-01-15, open access, CC BY 4.0. Archive `gp-model-main.zip`, 120127 bytes, MD5 `02bf2e789d8603e2fa588feac4f640bf`. File URL https://zenodo.org/api/records/14650881/files/gp-model-main.zip/content . Read in memory with ZipArchive; no archive unpacked into workspace.
- The web tool opened GitHub and raw pyproject but could not open Zenodo. PowerShell HTTPS requests to the official Zenodo API and archive succeeded. API response and archive contents were actually inspected.

## What is being simulated

**Static maps:** For each model CA1 cell, draw one smooth random spatial input map, subtract a threshold, and rectify. Then measure connected active regions in those maps and compare their statistics with recorded rate maps. Spatial position is the independent coordinate. The map is not updated in time as the animal moves.

**Not a recurrent/spiking network simulation:** Figure 1B and Methods S2 motivate Gaussian spatial input with a large randomly weighted sum of presynaptic tuning profiles. Methods S2 derives the limit and covariance. It does not provide a time-dependent recurrent CA1 network, spike generator, synaptic learning simulation, or animal-trajectory model. The archived model code directly smooths random numbers; it does not instantiate those input neurons and synaptic weights.

**Reanalysis:** The experimental side consists of earlier recordings and reported summaries, not new experiments collected for the 2025 article. The acknowledgment on printed p. 1118 says full bat maps were shared by the original authors and a 20-cell sample of rat arena maps was shared by Fellous. Therefore do not say every analysis can be reproduced solely from the two public data links without checking access to all required maps.

## Equations and parameter meaning

STAR Methods Eq. 2 (p. e1): `h(x) ~ GP[0, r(x-x')]`. Eq. 3: firing rate is proportional to `max(h(x) - theta sqrt(r(0)), 0)`. Eq. 4 (p. e2): local spatial scale `sigma = sqrt(-r(0)/r''(0))`. The guide writes `q` for paper `theta`, `C` for covariance `r`, and `d` for spatial dimension `D`.

The two shape parameters are normalized threshold `theta` and local spatial scale `sigma`. An overall positive gain sets firing rate in Hz and is matched separately for some rate and EC comparisons. Normalizing input variance absorbs the amplitude into threshold/gain; it is not a third spatial shape parameter.

The article says simulations use a translation-invariant Gaussian correlation function (STAR p. e2). A Gaussian covariance consistent with Eq. 4 is `r(Delta)/r(0) = exp(-Delta^2/(2 sigma^2))` in 1D. Smoothness, stationarity, and relevant nondegeneracy conditions underlie crossing/EC formulas. Isotropy is used for the dimensional field-shape arguments. Universal high-threshold laws additionally need the high-threshold limit, and independent rare-event/Poisson behavior needs sufficiently decaying long-distance correlations.

Methods S2, printed pp. 9–10, Eqs. S2–S8, starts from `u_i(x)=u_0(x-x_i)` and `h(x)=sum_i W_i u_i(x)`. Independent zero-mean finite-variance weights and dense uniform coverage yield a Gaussian limit and covariance proportional to the autocorrelation of the input profile, averaged over shapes when inputs differ. This is a possible input mechanism, not a measured weight matrix or a uniquely inferred circuit.

## Numerical generation actually present in the archived code

The archived `src/gp_model/utils.py`, function `GaussField(N,P,var=1,sigma=1)`, uses:

1. `numpy.random.normal(0, sqrt(var), P)` separately for each model cell.
2. `scipy.ndimage.gaussian_filter(..., sigma=sigma, mode='reflect')` on that 1D array.
3. Division by `sqrt(mean(field**2))` for each sampled map.

Archived `place_fields_model_1d.py`, `PlaceFieldModel1D`, uses the data map's bin count, physical length, and inferred threshold. It passes `sigma / data.resolution` as the Gaussian filter width and rectifies with `numpy.maximum(psp - theta, 0)`. `multiple` controls model-cell number relative to the input data (default 1). The generic code does not fix every figure's cell count.

Archived `place_fields_model_3d.py` draws arrays with the same spatial array shape as the data, smooths independent normal noise using `gaussian_filter(..., sigma=self.sigma, mode='wrap')`, divides by each map's root mean square, subtracts `theta`, and sets negative values to zero. Its function default `N=3*115` is a package default, not verified as the paper's final 3D sample size or every figure's run size. The docstring disagrees with the default, so use the executed signature if discussing code.

**Width convention to keep visible:** Code `sigma` is Gaussian *filter width*. In an ideal infinite continuous white-noise smoothing construction, its covariance is proportional to `exp(-Delta^2/(4 b^2))`, where `b` is filter width. Thus the local scale in STAR Eq. 4 is `sqrt(2)*b`, not `b`. The model's own `rho=0.5/sigma**2` in 1D and `lamda=1/(sqrt(2)*sigma)` in 3D show this convention. Finite binning, truncation, boundary rules, and sample RMS normalization also matter. Do not copy the README's filter width into the guide's Eq. 4 notation without conversion.

A README demonstration uses `N=500`, physical length 200, resolution 0.2, filter width 2.5, threshold 1, producing a `(500,1000)` array. This is explicitly dummy data. It is not evidence of the discretization used for every published panel. Neither inspected article nor supplement gives a complete per-figure simulation grid, seed, and run manifest. Report those settings as unavailable where needed, not guessed.

The code's 1D reflected edge handling and 3D wrapped filter boundary handling are implementation choices. The theoretical closed-box EC expressions have their own boundary terms. Filtering with wrap does not by itself establish that later topology analysis treats the domain as a torus. A new guide reproduction should say which boundary rules it uses.

## Measurements and fitting, with exact locators

| Stage | Source and operation |
|---|---|
| Initial maps | STAR “Data processing,” e2: identified bat rate maps from 1D/3D source studies, rectified at about 0.5 Hz for denoising. 3D maps have 10 cm bins on each axis and receive a median filter of size 2 using `scipy.ndimage`. |
| 1D fields/gaps | STAR “Fields in 1D,” e2: fields are connected nonzero intervals; gaps are connected zero intervals. Archived `PlaceField1D` groups consecutive binary values; length is number of bins times `length/P`. This gives bin-resolved lengths, not interpolated continuous crossings. |
| 200 m bats | STAR “Parameter inference in 1D,” e2: match mean field length and mean gap via simulation. Figure 4A reports local scale 2.4 and threshold 1.1. |
| 6 m bats | Same section: match mean field length and occupied fraction, since most cells have a single field. Figure 4A gives scale 1 and threshold 2.4. Figure 5D reports 40 cells; do not use this count for other datasets. |
| 130 m bats / 48 m rat maze | Match mean length and mean field count. Figure 4A gives 130 m scale 2.2, threshold 1.2. Figure S1 gives rat scale 0.34, threshold 1.8, removes large empirical outliers and matches the original 15 cm minimum field cutoff in simulated fields. |
| 40 m virtual track | Fit beta directly to available field-size histogram (not a two-summary raw-map fit). Main Figure 1F identifies four mice. STAR calls them rats in one sentence; use the main caption's mice. |
| 2D rats | STAR e2: fit mean field size and mean count from Harland et al. (2021). Correct silent-cell exclusion using Eq. 5: conditional mean `lambda/(1-exp(-lambda))`. Most 2D results use published full-dataset statistics; line slices and EC use the 20 supplied maps. |
| 3D bats | STAR e2: fit mean field volume and occupied fraction from full rate maps. Figure 4A gives scale 4.0, threshold 1.3; its distance-unit conversion is unclear against 10 cm bins. Do not present 4.0 as verified metres. |
| Simulation uncertainty | STAR e2: histogram error bars use 10^4 model realizations, each matching experimental cell number. These are model sampling spreads, not all animal/measurement uncertainty. |
| Lognormal comparison | STAR e2: simulation field-size density estimated using `scipy.stats.gaussian_kde`, compared with best fitted lognormal; likelihood/AIC/BIC favor the excursion model. In-sample comparison, not a reported held-out forecast. |
| 3D components | STAR “Fields in 3D,” e3: `scipy.ndimage.label`; volumes more than 3 SD above the mean removed as probable merged fields, including slice analyses. Archived class defaults need explicit run arguments to match this published removal rule; do not substitute package default outlier threshold for the paper procedure. |
| Peak counts | STAR e3: `scipy.signal.find_peaks`; exclude incomplete fields at boundaries; smooth with Gaussian SD 0.5–1 m for 200 m tunnel or 0.3–0.6 m for 6 m tunnel; report mean and SD across smoothing settings. Model error bars are independent-simulation SD. |
| Peak rate versus width | STAR e3: take maximal rate inside each connected field; 1D maps additionally rectified at 1 Hz; compare log-log slope and fit intercept to absorb linear gain. Figure S5 tests cutoff sensitivity. |
| Boundary slopes | STAR e3: line through two consecutive boundary samples 0.1 m apart. This is a finite difference estimate. |
| Euler characteristic | STAR e3, Eqs. 8–10: analytic expected EC in 1D/2D/3D including boundary terms. Empirical EC uses Gudhi Betti numbers and their alternating sum. Mean maximum rate normalized between data/model to fit gain before EC. |
| Variable thresholds | Figure S4, printed p. 5: positive-conditioned skew normal threshold per cell; mean fixed to baseline threshold, remaining two parameters fit the forward/backward count and median-size correlations. Two independent maps share a cell threshold. Size/gap distributions are additional comparisons. |

Figure 4A (single crop inspected from the already available `research/mainali-2025-parameters-crop.png`) also lists 2D area, scale, threshold as: `(0.5,0.1,2.2)`, `(2.2,0.2,1.6)`, `(8.2,0.3,1.2)`, `(18.6,0.4,1.2)`. Areas are m²; scale is a distance parameter. Avoid converting the label's environment units into scale units mechanically.

## Figure map for a methods chapter

- Figure 1A–B, printed p. 1112: map generation and proposed random-input interpretation. 1C–E: 200 m length/gap/moment comparisons, finite-threshold simulations versus limiting Rayleigh curve. 1F: histogram fit for four virtual-track mice.
- Figure 2, pp. 1113–1114: 2D/3D rate maps, sizes/counts and lower-dimensional slices. Restricting a spatial Gaussian field to a straight line or plane keeps Gaussian structure; these slice comparisons add information beyond fitted means.
- Figure 3, p. 1115: shape measurements (local peaks, maximum rate, width, boundary slopes) and EC threshold curves. Panels F/G/H are 1D/3D/2D EC in the main captions; STAR has displaced references in places, so use the main captions.
- Figure 4A–B, p. 1116: fitted parameter table and cross-environment trends. Figure 4C: simpler peak counts in short tunnel.
- Figure 5, p. 1117: threshold changes field heterogeneity; simulated examples and high-threshold/parabolic trend; 6 m tunnel field-size test.
- S1 p. 1: rat maze fit and minimum field-size matching. S2 pp. 2–3: spherical alternative with matched joint volume/peak-rate statistics can fail slice/EC comparisons; curvature from local surface derivatives. S3 p. 4: count/scale/propensity trends. S4 p. 5: cell-specific threshold extension. S5 pp. 6–7: denoising/cutoff sensitivity.

## Software and data availability wording

Article key resources (e1) explicitly names **Python 3.11**. It explicitly uses SciPy for median filtering, KDE, connected components and peak finding; Gudhi for EC. The code confirms NumPy random-number and array operations and SciPy Gaussian filtering. The archived pyproject requires Python >=3.10 and declares Gudhi, Jupyter, Matplotlib, NumPy, scikit-image, scikit-learn, SciPy and tqdm. These are package requirements, not proof that all packages are part of every simulation stage. No Brian, NEST, NEURON, MATLAB, or other neural simulator is established by these sources.

The published ZIP contains source, README and dependency files. Its inspected listing has **no recording data or per-figure notebooks/run manifests**. It supports generating and analyzing maps; code availability alone does not establish a one-command replication of every published figure.

Public data links in the STAR resource table are https://doi.org/10.5281/zenodo.4646727 and http://amygdala.psychdept.arizona.edu/lab.html . Printed p. 1118 seems to render the bat DOI with a trailing zero (`46467270`), while the key table gives `4646727`. A live official REST request to https://zenodo.org/api/records/4646727 succeeded: it resolves to version `4646728`, DOI https://doi.org/10.5281/zenodo.4646728 , titled *Data for "Multiscale representation of very large environments in the hippocampus of flying bats"*, with open access and one deposited file. No recording archive was downloaded. The rat lab link was not established as accessible in this check. The 3D/full-map and 20-cell sample access described in acknowledgments should remain visible. Extra reanalysis information can be requested from the lead contact.

## Contributions already present in the actual guide

Read current Markdown: `05-place-fields.md`, `05b-place-sizes.md`, `05c-place-tests.md`, `06-synthesis.md`, plus the current place comparison table YAML. The following is based on those files, not old review records.

| Guide scope | Central / supporting / guide-derived |
|---|---|
| Place-field count, gaps, scale | **Central:** Mainali, Azeredo da Silveira, and Burak (2025), Eqs. 2–5, Methods S1/S3. **Supporting:** Mainali (2026) author teaching notes for crossing argument. **Guide-derived:** expanded narrow-band crossing explanation; explicit inversion from mean length/gap; endpoint correction worked example; silent-cell conditioning example; normalized notation. |
| High peaks and sizes | **Central:** Mainali et al. (2025), Eq. 1, Methods S3/S4 and Figs. 2–3/5. **Supporting:** Mainali (2026) for crossing slope notes; Adler (1981) and Nosko (1988) are cited through the source for theorem background, not independently proved by this guide. **Guide-derived:** isotropic Hessian/ball calculation, beta constants, corrected supplement algebra, width-from-slope check, and explanation of slice sampling. |
| Holes, measurements, wiring | **Central:** Mainali et al. (2025), Figs. 1–5/S1–S5, Methods S2 and STAR EC. **Supporting:** Taylor (2006) for Gaussian EC framework; original recording studies below. **Guide-derived:** explicit low-dimensional determinant algebra and box-face factors after importing the topological theorem, numerical topology examples, Gaussian input-profile autocorrelation integral, distinctions between a sufficient circuit account and a unique inference. |
| Synthesis | **Central:** Burak and Fiete (2012); Ben-Shushan, Shaham, Joshua, and Burak (2022); Mainali et al. (2025), compared across maps/dynamics/behavior. **Guide-derived:** local common-displacement calculation `Cov(delta R_i,delta R_j) ≈ 2 D t f_i'(x) f_j'(x)`, rank-one interpretation, worked example and proposed joint experiment. Explicitly not a jointly tested source model. |

The current synthesis's supporting author-year studies and roles:

- Seung (1996), Aksay et al. (2007), Burak and Fiete (2009): neural integration/path-integration background.
- Koyluoglu et al. (2017), Seeholzer, Deger, and Gerstner (2019): capacity and short-term-plasticity extensions that alter storage assumptions.
- Eliav et al. (2021), Harland et al. (2021), Yartsev and Ulanovsky (2013): existing place recording sources. Rich, Liaw, and Lee (2014) supply the 48 m maze reanalysis in the central article; Lee et al. (2020) the 40 m virtual-track data. These should be distinguished from central model authors.
- Maimon et al. (2026): later CA3 versus CA1 comparison already discussed in synthesis. This does not supply the 2025 model or its original simulations.
- Druckmann et al. (2014), Bittner et al. (2017): measured connectivity/learning alternatives showing why Gaussian maps do not uniquely identify wiring.
- Nghiem et al. (2025): eye-motion/perception supporting study, separate from the source of eye drift.

For the new Part IV introduction, a defensible short label is: **Central models:** Burak and Fiete (2012), Ben-Shushan et al. (2022), and Mainali et al. (2025). **Supporting methods and data:** give the chapter's relevant original studies with author-year, not one undifferentiated bibliography. **Guide additions:** comparison table, explanation of simulation stages, and any proposed reproduction procedure; those additions must not be called the original authors' executed workflow.

## Main limits to preserve in the prose

Static spatial fit supplies neither temporal memory drift nor spike-timing dynamics. Gaussian inputs do not uniquely identify random connectivity. High-threshold size/count approximations and exact smooth-Gaussian crossing/EC results have different ranges. Processing can change small regions, holes, peaks and tails. Matched summary quantities are fitted; other distributions/shapes add tests, with separate gain fits visible. The published sample sizes, grids/seeds and raw-map access are not fully specified for every panel. The archived source code is useful evidence of implementation but contains defaults/conventions that must not be treated as exact published run settings.
