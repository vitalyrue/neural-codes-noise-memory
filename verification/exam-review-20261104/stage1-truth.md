# Stage 1: correctness and reasoning

- Reviewer: /root/exam_review_check. Local request ID: exam-review-stage1-20261104. Model requested by coordinator: Sol high; exact backend version not exposed.
- Fresh scope: current new exam-review page and connected mathematical-tools route, primary local papers and actual linked guide passages. No historical verdicts read.
- Actual host start: 2026-11-04T19:15:19.6891384+02:00
- Audience: physics/CS background and basic probability; this is a return reference after studying linked chapters, not a first mathematical introduction.
- Method: checked displayed formulas and symbol dimensions, all 35 three-cell rows, 3 map rows, all new narrative and recall text, exact guide headings/section numbers, primary PDF equation/page ranges and claimed guide/source distinctions.
- Wall-clock timing uses host timestamps. Awake execution time is unavailable because Windows sleep/resume events were not collected; do not equate it with wall time.

## Findings and disposition

Initial defects reported to coordinator: (1) matrix-only-in-support prose contradicted core K; (2) universal prime convention contradicted phi input derivative; (3) five old row-number aliases; (4) E2 population mean must be distinguished from a sample estimate; (5) extraction residue in derivation cells. Coordinator is applying repairs. Current snapshot state is recorded below.

## Three-cell row judgments

| Result | Formula and symbol cell | Source, location and derivation cell | Decoding cell |
|---|---|---|---|
| M1 | Unit-spike activation and count-process rewrite are dimensionally consistent; W sender/receiver indices correct. | Main 7-9 p5 and Chapter1 section1.2 match; count rewrite properly distinguished from printed impulse train. | Fixed weights renew activity; phi maps input to rate, not physical eye angle. |
| M3 | Left/right neutral conditions and 2D=sum v_i^2 r_i follow projection; coordinate-squared/second units correct. | SI S8-S15 p3 verified directly; guide sections3.2 and3.3 have actual derivation. | Retained shift after stable directions relax is the needed left projection; weak-noise and tuning limits preserved. |
| M7 | Independent fixed-state Poisson FI is sum slope²/rate, interval information hJ; regular local unbiasedness stated. | Main3 p2 and SI S42-S43 pp9-10 support J and likelihood; displayed CR variance bound correctly guide derived. | Present local precision is separated from original-cue accuracy and finite-sample attainability. |
| M8 | Cauchy Schwarz with tau sum v_i r_i prime=1 gives exact dimensionless 2DJtau²>=1 under leading model. | Main4 p3 and SI S45-S49 pp10-11 checked; short proof is accurately guide equivalent. | Common tau, tuned family, weak independent noise and absent anchoring keep claim in scope. |
| M9 | Normalized equality weights follow proportionality and normalization; exponential phi suffices for symmetric W. | SI S49-S51 p11 checked; guide linear counterexample computed in actual section5.2 and disproves broad necessity. | Sufficiency separated from necessity; model assumptions remain active. |
| M13 | Precision Riccati solution gives coth variance, sqrt(2D/J) limit and characteristic time <=tau. | SI S58-S75 pp13-15 and main5 p4 checked; guide independent precision proof properly labeled. | Monotone improvement to limit does not claim hard observation deadline or biological implementation. |
| M2 | Conditional Poisson moments use fixed theta, dimensionless counts, and h in seconds; exact within model. Stale row3 alias must become M3. | SI S43 p9 and main9 p5 support conditional count model; moment derivation correctly assigned to guide. | Conditional cell independence does not imply independent recurrent trajectories, correctly distinguished. |
| M4 | Squared input slopes and tau-squared denominator agree with SI S18 and have correct units. | SI S16-S18 p4 directly checked; corrected source expression identified rather than repeating main typo. | Symmetry is a special case, not a premise of general projection. |
| M5 | D and J matrix indices and units agree; PSD inequality requires invertible J as stated. | SI S21-S24 pp5-6, S44 p10, S52 p11 and proof p12 verified; linked guide sections contain matrix argument. | Off-diagonal covariance can arise from projecting independent noise into multiple coordinates. |
| M6 | Ito zero-drift PDE, Gaussian line density and 2Dt match; constant D and line domain are explicit. | SI S28-S32 pp7-8 supplies source; circle limit and variance-rate are labeled guide deductions. | Boundary/wrapping caveat prevents false unlimited angular variance; circle plateau pi²/3 correct. |
| M10 | N, rate and tau scaling powers require preserved geometry/resource constraints as stated. Stale row11 alias must become M11. | Main p2 comparison and guide5.3 agree; displayed powers are guide algebra, not printed source equations. | Circuit adjustment and equality/preserved geometry caveats prevent arbitrary parameter-change claim. |
| M11 | Information integral has recruited-volume w^d and slopes w^-2; D exponent needs equality/isotropy. Stale row10 alias must become M10. | Main p4 width discussion and guide5.3 actual integral support reconstruction label. | Fixed peak rate/density distinguished from fixed total spike budget; d=1,2,3 consequences follow. |
| M12 | Double Brownian covariance integral gives 2DL/3; derivative gives sqrt(3/(2DJ)), with correct units. | SI S76-S81 pp15-16 checked; guide6.2 repairs missing cross-time terms explicitly. | Nonmonotone equal-weight error is cue-state readout in separate-noise Gaussian model. |
| M14 | Storage addition, thinning alphaJ and alpha^-1/2 scales follow stated independence/local-unbiased assumptions. Stale row5 alias must become M5. | SI S57 p12 and S82-S83 p16 checked; guide cautions printed Eq6 direction and reconstructs valid lower limit. | Random thinning vs selected cells distinguished; 2D(T+tau) only at equality is mathematically correct. |
| M15 | Rate relaxation units and 1/[2(tau+tau_m)^2 J] bound agree with symmetric two-stage model. | SI S84 p17, S85-S92 pp17-18 checked; negative rate-decay correction follows own S84. | Sum-of-times claim restricted to specified model and noise placement, not arbitrary biology. |
| M16 | Matched additive q_n gives FI=sum slope²/q_n and 2D=q_n sum v² with correct dimensions. | SI S93-S95 p19 checked; missing printed normalization honestly marked as guide reconstruction. | Linear symmetric sufficiency and noise-dependent equality condition agree with matched likelihood. |
| E1 | Second-order filter, factorization and causal impulse response normalize correctly; k/r/m units correct. | Main Methods2-7 p9 checked directly; guide7.4 contains inversion and delay. | Single-cell calibrated predictor not asserted sole eye controller; positive distinct decay times stated. |
| E3 | Shared covariance and chi≈R sqrt(VarX/VarY) agree algebraically, dimensions degree² cancel. | Main11-17 p10 checked; 0.82±0.07 is weighted estimation uncertainty, not animal scatter. | Gain transfer, pairwise noise covariances and order1/N_m term prevent unqualified causal localization. |
| E5 | Stationary convolution covariance and 2(C0-C_lag) MSD have correct noise/kernel units. | Main20-22 p10 checked; guide8.2 matches. | Finite plateau requires overlap decay; empirical continued growth limited to observed range. |
| E6 | Stationary velocity covariance D/tau_f exp(-|s|/tau_f) integrates to displayed MSD and correct limiting powers. | Guide8.2 actual derivation checked; main Fig3 pp5-6 is context and full model23-34 p11 distinguished. | Separate eye filter tau_f and memory synaptic tau avoid applying unrelated time constants. |
| E2 | Orthogonal standardized predictors give sum R_i²<=1. Revise angle brackets to population mean; sample only estimates it. | Supplement1 S1-S2 PDFp2 checked; guide7.5 residual variance proof applies to population. | Jensen lower estimate 0.17²≈0.029 correct; sampled representativeness needed, with sampling error qualifier. |
| E4 | Two independent reading errors add 2sigma_m² at positive lag and cancel at zero. | Main18-19 p10 and supplement1 PDFp8 control match; guide8.1 explicit expansion correct. | Temporal correlation requires lag-dependent correction; independence from movement preserved. |
| E7 | Absolute/fractional slope change explains opposite rate scalings; dimensions degree²/s correct. | Main1 p6 is comparison, not claimed exact source; guide9.2 derives Poisson/renewal scale. | Full sub-Poisson saturating circuit not identified with simplified scale; fixed-geometry restrictions explicit. |
| P1 | Gaussian normalization, threshold/gain and local scale sqrt(-C0/Csecond0) valid; covariance unnormalized. | Main2-4 pp13-14 and supplementS1 p9 match; guide10.1 normalization explicit. | Spatial map fixed within traversal; ell_c vs sigma_0 and time noise distinguished. |
| P3 | Rice upcrossing density and endpoint Q correction correct; finite-track count includes clipped fields. | SupplementS9-S13 pp11-12 and main8 p15 verified; guide10.2 matches. | Exact any-threshold Gaussian model, not universal empirical identity; positive q count decline correctly scoped. |
| P4 | Occupancy divided by crossing density gives stationary complete-field/gap means; inverse tail and scale algebra correct. | SupplementS14-S15 p12 and guide10.3 support exact means and guide inversion. | Finite ratios, clipping and cell selection not mistaken for stationary component means. |
| P6 | High peak radius ell_c sqrt(2epsilon/q) and exponential qepsilon give beta=q²/(2ell_c² v_d^(2/d)); units inverse distance². | Main1 p3 and supplementS22-S25 pp14-15 checked; missing sqrt2 and quadratic sign corrections follow algebra. | Counted-once fields and high-threshold domain explicit; Rayleigh/exponential/Weibull powers correct. |
| P2 | Independent zero-mean weights cancel cross terms, yielding v_W sum u_i(x)u_i(y); units consistent. | SupplementS2-S8 pp10-11 and guide12.3 checked directly. | Many non-dominating contributions required for Gaussian limit; stationarity/isotropy not automatic. |
| P5 | Poisson rare locations and exponential long gaps approximate; zero-truncated mean lambda/(1-exp(-lambda)) exact given Poisson. | Supplementp13 high-threshold discussion and main5 p14 checked; guide10.3 adds necessary decay condition. | Weak dependence, boundaries and selection caveats prevent exact finite-threshold interpretation. |
| P7 | Fmax=aepsilon gives aq/(2ell_c²)(s/v_d)^(2/d); full-width v1=2 correct. | SupplementS22-S23 pp14-15 and guide11.1 match reconstructed constant; empirical figures only comparison. | Square law applies to linear size, not volume; finite-threshold fitted deviations retained. |
| P8 | Exponential transform yields Gamma(1+kd/2) beta^(-kd/2); units distance^(dk). Stale row27 alias must become P4. | Supplementp13 mean and S18 normalization issue checked; guide11.2 derives general moments. | Higher moments test limiting shape after scale fixed; high-threshold and field-count sampling retained. |
| P9 | Restriction of joint Gaussian map has covariance C((t-tprime)e); t is spatial, not temporal. | MainFig2 p5 and guide11.3 checked; explicit restriction formula honestly guide explanation. | Slice dimension sets limiting law; hit weighting and centre cuts differ as stated. |
| P10 | Slope-weighted Gaussian derivative normalizes to ell_c² v exp(-ell_c²v²/2); density units distance. | Main boundary prediction and finite-difference method p15 support context; explicit density from guide11.4. | Exact q independence under stationary Gaussian model and gain scaling av correctly distinguish measured firing slopes. |
| P11 | Signed EC densities and binomial face factors reproduce closed-box formulas in d=1,2,3. | Main8-10 p15 and guide12.1 signed determinant/boundary derivation checked directly. | Components/holes/tunnels/cavities and boundary vs periodic boxes correctly distinguished. |
| P12 | Leading EC volume term gives q^(d-1)exp(-q²/2) count asymptotic with correct dimensionless count. | SupplementS16 p13 and guide12.1 match. | Large-region high-threshold volume dominance explicit; ordinary-threshold EC not asserted field count. |

## Map rows: three cells each

- Memory: modeled recurrent circuit and continuous value are the source setting; spikes/feedback/surviving noise/FI chain matches main pp2-3; diffusion bound and simulation status do not claim fitted animal behavior. All three cells retained.
- Eye: macaque OMN/movement recording setting verified in Methods p9; calibration/covariance/filter chain matches Methods pp9-11; shared contribution and nonunique circuit localization correctly separated. All three cells retained.
- Place: rodent/bat comparisons and thresholded spatial map match paper; crossings, peaks, slices and holes are actual tests; exact crossing scope separated from limiting sizes. All three cells retained.

## New prose paragraph and visible title judgments

The following judgments concern truth/reasoning only. They do not stand in for the separate wording and reading-flow stages.
- Paragraph 2, SHA256 `ccd0ebbab3546511921d64caf9316553810a012d1a1855855d19ccbb666f9d86`: Return-reference purpose fits actual compact rows and linked longer chapters; no promise that novice mastery is required before Part I.
- Paragraph 3, SHA256 `15082b84f2a011358927c4f1cd324c6922c147ec08654f585cdc758b7b3dea7c`: Quick-review label describes procedure rather than adding a scientific claim.
- Paragraph 4, SHA256 `fafa1f1e289c22cc6cee1a6c500e084636bb7fdb3c9f1d457ac94f3ff37c5c06`: Three steps correctly describe visible chains, closed supporting notes and symbol/source/guide cells; PDF-viewer page convention matches verified primary files.
- Paragraph 5, SHA256 `fb12c8c12c86c8ab4a8a72d40c87380d625f6e657ccbf483760ae0dd446cff44`: Role labels do not claim exam prediction. Guide-derived equations are explicitly distinguished from source context and linked derivations.
- Paragraph 11, SHA256 `134354b58af57c9311acff1bccdead6f68cf61432f328e0ddc4c89168bf0bf7c`: Stable recurrent family and surviving coordinate displacement correctly describe tuned leading-noise theory; no biological fit claimed.
- Paragraph 12, SHA256 `7f54da0a6156306d95fc8ee815527fc556cb44dddf5a06f2de47271505f39ec5`: M1/M3/M7/M8/M9/M13 chain is causal model, projection, information, bound/equality, readout; M6/M14 correctly identified as additional storage/recall results.
- Paragraph 13, SHA256 `cb07848f0423c5ab1dd086fb742aeeccb1a1bf3aa4b7aad66b96c884563be13c`: Scalar stored-coordinate diffusion/FI vs supporting matrix generalization is valid after repair; prime convention requires explicit transfer-input exception.
- Paragraph 23, SHA256 `f24816a2e1dcbcbab1e731539969a4c14a72eb26b3e930354e86521b56201343`: Shape restoration does not restore original neutral coordinate; accurate present-state readout can coexist with inaccurate original cue memory.
- Paragraph 26, SHA256 `7a6874fb6c41df347897cd622f9e4c739616ee26be7900961e50a0cfa5cdbbe6`: Macaque horizontal fixation and calibration in degrees are source setting; covariance question and independent-filtered-noise test are distinct.
- Paragraph 27, SHA256 `3a6e2125a56fbc90336528f187d38a9df2e80ecc274dbacaccb1def1bbb9da3f`: E1 to E3 to E5/E6 chain matches arguments; E6 guide model and E2 separate bound correctly identified.
- Paragraph 28, SHA256 `c3445924cf9b643acce891ac84e6f8d7db74f61c8cabce915f1a4fa5c6f9cc55`: MSD lag is separation of readings; eye filtering and synaptic decay are different processes.
- Paragraph 38, SHA256 `6a7dc774c9a39b2843d0ccd08e42f2d9a039514fcfe64f9d1d82b484d4804207`: Extra private predictor variance reduces correlation while covariance/VarY can remain large; gain/noise and biological upstream premise retained.
- Paragraph 41, SHA256 `2329ad1773c92db80e82d02796b384e166ff7b8f88bb91a793c958f07ca4aea7`: Fixed spatial Gaussian draw, threshold regions, crossings and high-peak statistics describe different steps without equating exact counts and limits.
- Paragraph 42, SHA256 `1f74278553c6f41b8ac623aab363cc29572f0c16b2d033bfbdb29962e6278fbd`: P1/P3/P4/P6 chain correctly separates exact model means from limiting law; P9/P11 correctly point to further structure tests.
- Paragraph 43, SHA256 `85295bcd81c339fee50aa3d69bd01d722d94d0a965f7a4dceb0483a4f015ad86`: Spatial coordinate vs temporal diffusion and ell_c alias vs sigma_0 distinction are correct.
- Paragraph 53, SHA256 `f29c1d121aac497812f8ac1616950c5654918d5342d36913403ebda5b940794e`: Rice uses conditional height/slope at threshold without high-q requirement; isolated nearly quadratic peak and excess-height limit are additional assumptions.
- Paragraph 56, SHA256 `7513bf87e83444d71b191521914d330ebe796d5aa6dec9f897df5e5b06bb33ca`: Question prompt adds no new result.
- Paragraph 57, SHA256 `c089a0f553f84074124b506f0d23bf4dbb69f8a10eb068fb47215d8d56847c9d`: All six distinction bullets retained: circuit state/value/decoder; present FI/storage diffusion; calibrated causal-fraction assumptions; command/filter observation; temporal vs fixed spatial ensemble; exact Gaussian identities vs high-threshold and dependence conditions. Each cited row supports the distinction.
- All six section headings and seven details summaries: describe their actual mechanisms or question and contained result scope; no claim of empirical universality introduced. Table titles/result role labels agree with cells; title and captions add no stronger guarantee.

## Connected route and plan

- Mathematical-tools opening line11 points to same frontmatter HTML filename as the new page; ending section retains old tbl-math-results anchor and routes all 35 results to new organization. The promise of symbols, exact locations and guide links is satisfied in source; rendered color/legibility is outside stage1.
- plan/chapter-plan.yaml places ch:EXAM-REVIEW after mathematical tools in front_matter, not in numbered Part I chapter list. Existing chapter and section numbers used by locators checked against actual source headings.
- Each guide anchor in all35 locator cells exists at the claimed chapter and section number. Local paper filenames exist and viewer-page references were inspected directly. No external source fetched.

## Scope limits

- Source semantics only, no rendered HTML appearance, PDF full-document visual inspection, browser link-click exercise or publication acceptance. Short reference entries rely on their actual linked full derivations; this is justified by the explicit return-after-study purpose.
- Primary PDF checks cover consequential cited equations and page ranges, not a new audit of all source-paper claims or all unchanged guide derivations. Printed source mistakes mentioned in cells were checked against their own equations and the linked reconstruction.
- No runnable code listing is introduced by the new page. No memory files used. Token stats unavailable.

## Current source and rule hashes

- `content/chapters/00-exam-review.md`: `af6404ec51657704ed23c07b72b7f5bdc1c08860b03c1297b10682888fd7c97c`
- `content/chapters/00-exam-review.yaml`: `3cea9532241c733cac77444b576c464722031ab1de002c2367303a872cb55d05`
- `content/chapters/00-mathematical-tools.md`: `06999cadaf9423ee8e18042d97b8148491d66e781b183f9d9af2414db37fcab5`
- `content/chapters/00-mathematical-tools.yaml`: `b8297855c3c9c2a203bd2753ccf89d24f1a148cb90885e059ad75bc55431da4d`
- `plan/chapter-plan.yaml`: `91b400ddd7381146fc957a1ae2f3d301df65347e12bf417de882818190b11ea8`
- `C:/Users/vital/.codex/skills/course-study-guide-builder/SKILL.md`: `b78068e9874e6d1d97b2017bf8f940492f9b08fc11b74f20fd75019ff388984a`
- `C:/Users/vital/.codex/skills/course-study-guide-builder/references/math-code-case-contract.md`: `ce2313f897b63e74ba59a3afe1bbc4046d3aa84584072cda7e76470a7e3cef9a`
- `C:/Users/vital/.codex/skills/course-study-guide-builder/references/pedagogy-language-contract.md`: `f4c1eb544cf640b708e1970d9572fdc758fcc6aea806675d01a0256658df847a`
- `../papers/ben-shushan-2022-fixational-drift.pdf`: `15f273f99bd8d8e8daa09a9f7809e04c53da514b146750c0ec517812e3478caa`
- `../papers/ben-shushan-2022-supplement-1.pdf`: `323335499cb6428f68714fb1c855a9b87d5fe38449d31e26acce76417358a7d6`
- `../papers/ben-shushan-2022-supplement-2.pdf`: `3f3c933f7cd1326d847565363481d7e79e922025ac354ae3872818f5aca3aa7c`
- `../papers/ben-shushan-2022-supplement-5.pdf`: `0147c43ba112ac00ac8c92ada30a5baafd26ed28532b51cb0c85d8baf43cf19b`
- `../papers/burak-fiete-2012-persistent-activity-si.pdf`: `9bbff1fb83db4aa4b76364a92de7c481de1f27ccdd6735dce78ae1d7b8496efb`
- `../papers/burak-fiete-2012-persistent-activity.pdf`: `6ea4f05bf1d0c8870baf8f042e9fc4392c1806e9100d94d2b0d3ab35f345adea`
- `../papers/mainali-2025-supplement.pdf`: `05af1fdf3079906871da12fdafa1f28895380f594a8c6bda3cafc5b503f07c31`
- `../papers/mainali-2025-universal-statistics.pdf`: `de2ca50a46f5b0d8d14e86269f1beacf6aadde7122bb348568aad92b12fd802e`
- `content/chapters/01-foundations.md`: `54569cc3a6a93bb9ea9a67be0f81a4bfc1b498d17bc533845167b8da4165539d`
- `content/chapters/02-memory-dynamics.md`: `6c016d520a5779894e3b14c107f38b4e7f22a03898ee7fe81d785d90d6e0bba1`
- `content/chapters/02b-memory-long-delays.md`: `bf1a04441d4254a09e99fc74ce7f7df26d6a322cfbbc9f9a18e6fc414d7f8c02`
- `content/chapters/03-memory-information.md`: `c75d99460ccee887d4bd95a7eabfd464c8ff2ad064a79f65b603880c289e128f`
- `content/chapters/03b-memory-readout.md`: `59959bd393fa36624773027c68f297886ce6f109abbde1d79118bc36539629c0`
- `content/chapters/04-eye-drift.md`: `2fbb5f1d55126fb952e44e9e8650fc7ddc00c7e8b5dcebab8e44182a7507dc05`
- `content/chapters/04b-eye-timing.md`: `15916da716dc5c8c64acbf9be65c837877c48674ac2c265a2b4737c9f7bdebfb`
- `content/chapters/04c-eye-circuit.md`: `70cc1b6c75b857b6f2671d5154d57d47d2159bb65f1c8a013e6565d5e81f42b7`
- `content/chapters/05-place-fields.md`: `60dcdf27c11276c338bbd9f6974896905e5b0dac526237cc5d90bab057d2efdf`
- `content/chapters/05b-place-sizes.md`: `da845923ade9f098aa30ccf0e6a80e498c9992c0db729c07ad5321b05399385a`
- `content/chapters/05c-place-tests.md`: `5258984325a2a397540b59f489167a3cb73a62438526a57298ec98d379cd4996`

- Actual host checkpoint/report written: 2026-11-04T19:20:13.464791+02:00
- Wall-clock elapsed at report write: 293.8 seconds. Awake execution unavailable. This is not final repair recheck yet.

## Final narrow repair recheck

- Request: coordinator asked a separate narrow recheck in this continuing stage1 call after applying repairs. Source and surrounding row text were reread from disk.
- Prime convention now explicitly separates derivatives of tuning curves from the transfer function input derivative. Scalar diffusion/FI wording keeps core neural matrices allowed. Both corrected paragraphs retained after rereading the memory chain.
- Five cross-result aliases now target M3, M11, M10, M5 and P4 respectively. E2 now defines angle brackets as the population mean and calls the sample an estimate with sampling uncertainty. These repairs resolve all reported semantic findings.
- All35 derivation/location cells were checked for the earlier extraction debris; the missing detached punctuation is gone and the causal derivation sentences retain their needed steps. Eye/place symbol keys use inline LaTeX for the same quantities; E2 and five aliases are the only claimed meaning changes.
- Stage1 verdict: PASS for current new page and connected route, at the final hashes below. No unresolved correctness/reasoning finding in this scope. Separate stage2 and stage3 calls remain required.

- Final `content/chapters/00-exam-review.md` SHA256 `af6404ec51657704ed23c07b72b7f5bdc1c08860b03c1297b10682888fd7c97c`
- Final `content/chapters/00-exam-review.yaml` SHA256 `3cea9532241c733cac77444b576c464722031ab1de002c2367303a872cb55d05`
- Final `content/chapters/00-mathematical-tools.md` SHA256 `06999cadaf9423ee8e18042d97b8148491d66e781b183f9d9af2414db37fcab5`
- Final `content/chapters/00-mathematical-tools.yaml` SHA256 `b8297855c3c9c2a203bd2753ccf89d24f1a148cb90885e059ad75bc55431da4d`
- Final `plan/chapter-plan.yaml` SHA256 `91b400ddd7381146fc957a1ae2f3d301df65347e12bf417de882818190b11ea8`

### Final individual row cell hashes

- MAP1: cell1 `e04cdba936934173609a815468de09b37fc9b300fc57900580a2982c4bcfa584`, cell2 `4bc526ef7f3c10e1b9adba33bc5fcc95651201730c552445d6f1ad39ff921c62`, cell3 `ba770c213ad8324800d3cb435055b4af11c09fc697155c8aa9974feb88862143`
- MAP2: cell1 `fa9a75774ffaf2ecaba1a3d324a11a7251b4767884553c5e3c84d3814ad9bab4`, cell2 `800339b7e67e0247f85f818bdec4c783893bdca6bd5b791b8bd38c1af57722c0`, cell3 `5304e1433cbc05aa98f85c372b40791b0bf55f1ef5fbfbb3a4072b106a6a58c3`
- MAP3: cell1 `6db62fc7cdc58949b823a916f29e4e6d1693e6917222dd56fe37c2d725dd7b1d`, cell2 `0711e18fe71569c686eb91e4e89b83fdfddd936512e085461f81213a53ec8aaa`, cell3 `2fb5e6d966a1e3bb7b5607dc7f51108f262a99f91aed40d7c8bec84149afd728`
- M1: cell1 `40f4f2574e2d49e0d9d96ad8fced27a2f62ba6b34cc4fef51f2262a1182d5b20`, cell2 `23a3d12b5c42c9fa6341ae8a0e728bf610d84737517d7c9b6934528df1f087e7`, cell3 `584cd547e2d6f63466a34ae79ca7a292119eac2096886dafe810440473f53932`
- M3: cell1 `9baa7a7591f226d5db121dbc9cf8eba3c3de2a5935f9f68809c4d516613b8d51`, cell2 `c2770cab570ab325e9b2f0b48fe0eb187052f8e201f7fb717e803f830ffb2ae6`, cell3 `3ab8778aed53070468845950be7d9c6641449400c122b8f05ebad50b24cf7b34`
- M7: cell1 `eb268b4d0c8b97cb80fc80d3e8d4e59cce1fc7ec6c349d551b2048c8d4ab7cb8`, cell2 `01a9ba3031838b343f2705ce30b543ee00a1a4a9b8c0be391184e137390b7710`, cell3 `a301f24205d091761de7b9d34c44de7faa60cdeda2da76399e921c5239f5a9ce`
- M8: cell1 `9a3f4e650056d94839efac8929f62891f033436cbbdd1dd0332b303764b5c1ff`, cell2 `43b4b5fa49426482eb38d3193bc9582567950de40885ce5b04d2cdb78b4e277e`, cell3 `2c885e789bad11af899ba39559f965fe94c2612e341d46dac4de8ad19eeede12`
- M9: cell1 `37f89998f53540a4f3ea940c23d8b98bd8d1724433cf6325235bfe77b0894376`, cell2 `17a16d4b51ce8a9fa45d600a5bc8f97908fbae5d3d1e069fed161c9341e51c72`, cell3 `441ca1a414c81b8d721a9e4ee169c8e8f6d93a84dcbbedcdde37da15c7e54a74`
- M13: cell1 `cccde6c8cc1433cac5956a9ccdfe20fb51ed74c305a1fb564caadedd754f86ff`, cell2 `205beea404aafe4d710d34de9cdc5a2f9443c7a8fa8e6c807e243c02fe7b043f`, cell3 `8d04c97d4f4072065fa26fbd440a6bce6f1177a77d53e7cc67081419864b02c4`
- M2: cell1 `0160eea1d63c7be4d99f0daa75ef4d33aaf93c9545ec132870ffb5467763905e`, cell2 `50c69bc3347f17aa5f2406c40a72a4ae6a6589143fc33d8d107aa728b5e9fcdb`, cell3 `da97e73fd71adf117678a194e33d810f85e1243e4f9193ab8a71232313f03d9d`
- M4: cell1 `bc8f2b3c9eb7a6d99a64a3a8e45a253c2761e36506834ce101d62af745674b8c`, cell2 `c908044b32970f41e870560175e55fa16d63ca42b4697e5e63cb2aaa1daef621`, cell3 `bab8af7e6ed7e1ef84538e9cf3636dcbc4f3c3f3454dc734141d4b86eeb4205a`
- M5: cell1 `cf9eb50ccf120f48ddba8fed62960680e247044e64ffbd3c9c7be4f34f957aea`, cell2 `c9dbb56066c13877ecec67f6e6b9b53e334558d1b8180e74d7fbd1fd47a20079`, cell3 `be2061b0efabca90544560d02cca6f2fca06d5770a11fe413d2ffab2c94e743b`
- M6: cell1 `e8e2a1319ac8e8823a272eb03d9974f960bb45903d6fec47f3f5842c33467aeb`, cell2 `607a6dc1d5ba2a13eaad7a868dd65648aebb9d11d0f20c89ddee7484ef9bc91f`, cell3 `be6fab6588518e5ed7cb0c278f9dfd7334c97520b21fb356678648081e845450`
- M10: cell1 `bb5f9a88fe4f64f524ecce8876ec9aec30f56f3ddcb69a770310c74b0b9aac64`, cell2 `dd25eaa3cf523a0f8354bcd5bcde8fe0b2b228e8b33f104c2e4a4eba7579f456`, cell3 `b1e8e8521b28f05d63c2897a62ac8de6d1c3bc40d869c92cac3655e7dab93db4`
- M11: cell1 `077fb64c463c0e5147d6c89ea97c01ea3c62bb41b54f8bbfff15f9df3de1b954`, cell2 `fc16eaebdfb4575bd1c20f7e30d8c72634d50ca11a155632f70018f6e4a6bc70`, cell3 `d8106b32d31edd8afdb994fe480dc1260b33baf7bd86f26511e7a5369dc96e04`
- M12: cell1 `dfe1664ba8efe9ca528c1c967ca7bd3b4fdf9431d173861c5f2cc879f9df2b87`, cell2 `ddee2daf6f0ec66358169f99c4c356dee88fdd4aaed569c5e29a9c98f542d44e`, cell3 `5ea3710e4a1a158892f672a494feb112c66eb2c2ee5f4706f525278afa5dea6e`
- M14: cell1 `9121ec80a4d1508cfc75ffa7d6cdcd779bb370f38ff8feb95be134b1c2d81bbb`, cell2 `7b5be84264f80d8c532a65bb77dc777569a720fa0b9510645c27f57447b8d3d0`, cell3 `da2725d3bfa019d9ada778fa8fa12b2249c5099b4aac079032319f3c35db269d`
- M15: cell1 `29d1f5c3c2efa8cd7ce1d5b6aa2ccff72bb68999d79875b7e79614f10e3557ff`, cell2 `e8e642b7e41163d4008a2af5b570e309986ea71ec0f1dde2bc1e1173c149b368`, cell3 `c7b1d7f7e7c5e55763722fc59a08ad65e677caf4ef3d08a1aa96e158e6b5597a`
- M16: cell1 `d9c0564af7dec061ed007208ecadfd8e7dff5e581def13a1b555a4e3bf58604e`, cell2 `0c57904fe862f9895f67bc7eaf23f0c78ffbb2ced5ff03af93a20eeda1e21d88`, cell3 `5f3795b2977ee490e407294a3ecc9c29b44c542f35ce0edaf193d06950c0ea68`
- E1: cell1 `204a65b89d0276b7edbb74b35d849dc18af53c7dc76acb38ddf93902e1325d13`, cell2 `733213e3a7a5ed3b19dbd63e8d38188fce9f89a42c451b8847efed503a05327c`, cell3 `3fb0524a645533638dc47dbf524edd952a365436e6a54279d4d8de6bf3331574`
- E3: cell1 `bedcfc3d54a606547a6fd9ae45ced5e67a0453e2c5359ff44e67d8f1f997240d`, cell2 `558013e429b376b47d147caa361ea695ea147476ee1c7dd8827bac6ffd6e355f`, cell3 `762930bd0612de7ce559ba02c923b83422c0667a191405e8121c439f10724485`
- E5: cell1 `799c54f0a337d99f8663394a845e534ae2ccd4be2fa1c6ac3f5409e0e23d7663`, cell2 `50bebc9f56ffc3db10872640b3699262ab7ca44c4cd2052ab465cf7427811c36`, cell3 `716e8e602d44f2a5c456b2210e45ca75b6e722cc2bc2237f6ed3c60ca83c6d9a`
- E6: cell1 `d6d79c141023d43f3cb0cbb83449871160e9a5efd8cc24311a6b97d6c520b00e`, cell2 `8989d7c2210055a397195df5f53453910a06a3bc682aba00980f5a2d628ad1c2`, cell3 `43ca879c757b6851adcadb8b860cfb5601e8b4e72f88cb3eae2e626e1447533c`
- E2: cell1 `1efb674407468c29a4cfd439618d08d0da570e0f90026a3116c47e015cda74ed`, cell2 `6ec174b970ecdd241929c14e1239168e846c218d862244ed898e3f7dd2731360`, cell3 `697a7541f84310d220b4adbe3030e19f0fd6c93423597ba1710b7ab76b88d48c`
- E4: cell1 `82fcdfae825752c8be5f3fb372de69f8aed4770e1c8f4d9c22b2986c02feae1b`, cell2 `c116c851224ef88b9f177a9a25913e10cbadbd568d3a4680a0d15fed5bce9863`, cell3 `a6ed0fd40aad7bb18e7c5b476a0cdd816e5d00d735c982ca17c8c6a6fa1eedef`
- E7: cell1 `70090b775a5801bc8d07e93922b13275f1d22f06ea45a36a1c30c5052bc7e487`, cell2 `084578a9c7c803da5338c1b701928c406e7811895f1847d96290b25a8547abaa`, cell3 `b9d6a29aecad1ab5241e58a261ccf3718240662ad39d5f823e811f0e45088b13`
- P1: cell1 `01a8f01531849fee603b674f13ed7e586afbf209d74868a687c27cdc6e42b398`, cell2 `00db8aa7bb404a2e437a607e4c1a6b6cdfd61f133dfd0699dfc13708fa29774d`, cell3 `e52c87b21c8943a3c1e811e72c3bd81211c6933b8e6d0c9ca2a319a5abcb4b91`
- P3: cell1 `4137f1b277ccef166ab7b0db0b95d6f23937381a37b753f641e39be1ccde55f2`, cell2 `b3b176e97681be231c75a64bb1a966667f885430e3d6749aed536b511660be12`, cell3 `236378164f11655a0816f2bfe68d7f252804aef8df67c95b22f54d5b25c44cda`
- P4: cell1 `1b6201c0aa5af05008ab5120580a07ae3430dfbc075e48236c7866322b76df1d`, cell2 `29332263a6045377a8d429f8f40d6ce466c6c2928cff1fbd6b2a1c82e4fd283f`, cell3 `c897216e5be6007a7c86b1deac6217455e588879543668a701fc740a3134d321`
- P6: cell1 `71527a1d83c052214c89c8ecb23d9b4b4c5d013ff51d84eb8794be505f03f4d4`, cell2 `27b913cbe6489124f32597c5bfdf5f1c192a3f18884f8c1166add6959c357123`, cell3 `bc8187ae1dbfb16d9b180d041bc6c769e5b7a54d4c59507307080d1eb378ba09`
- P2: cell1 `8a9740318fbbf5dab40a076b5ecfa4b762a73224f4427a181e1b892eb00f33e3`, cell2 `0e6b612ed474ef4dc3c291691906f34a39ca7e75979216d647304d8ca189b3fd`, cell3 `5322ed8ff04b7f20eab5b50cf96c042b6b77242ffdc4c4d5a168dec8d7d92389`
- P5: cell1 `75bd9d6f45ed33baea6800759fce4c7e73ce8ca0646f687e67c131a15c6b6d8c`, cell2 `2c296f7e396a00f43d2bd5ab814ca6e4a5f580ca1c6f350f7e6c7c094393132d`, cell3 `1941787d7f448d3dd5ef16d4f7785d9b111767583f2dcc88f7b56f39975ead4c`
- P7: cell1 `1341c1100d7c9d046247735f3bcdb8fe72e503cb18cf0c755627500e3a964cdf`, cell2 `d3568ade0dd8cc41897cef51c12ca09a38dcf1f68c73d248866a21bc34d9292c`, cell3 `6cd749f731e92d3438030618644ba81155c1f45c5ea580b4c0bec7a9e10ece34`
- P8: cell1 `9c1a8aed05faf89ee3a8d9e06dfd8da83a3a325c5c70b0ddee2d6953a0b01fe8`, cell2 `f7afba38592822552feba711c5e324913142dcc25df39927eecf5c7edfc6257f`, cell3 `ebab270cabc61dc63373e97e1d1e493fbe9e21276f0d9b8e3ad55449d4012f43`
- P9: cell1 `d1a99f7f493fe116ca51bf4b9e1f88f3d9a7cecac3740161b3dbdac2d7eec4e5`, cell2 `27546fb7f99e124e14c3314c09eeb9ab40c7cad4d31517866d7ddd83ada06fa1`, cell3 `119b3e4e14fde555ac57fb1b408a5191bca5fa0e0bd270f9634fa03414f09a7d`
- P10: cell1 `99c5dbeca9003fcaa0f86ec5897bcac3c5ef9ae3ecfc67efcaaa64111721c069`, cell2 `c1965ec82a0221420ba63cf00c31d6428719eeddfbbbddeb464f956e1304887e`, cell3 `99419f8baaa0340a0fe97802331b1e97f538305c3c2279ffcf983b89d8f7d97f`
- P11: cell1 `96f7db1c284f39364bc04e2296a0555b0555520a3b44f7b199c8f19fa79642cf`, cell2 `47969f068eea2500280bb68086b4e4da8b6015a6c221e439c508f4a0cbd349c4`, cell3 `2e9fc7a1cd2b53b02107ed09ef25787492d2228ad84e2a24ca1362d2549d6383`
- P12: cell1 `261477809265f24096aac368e112f7e3b367eb44bd9633123ebe72c2f894ea37`, cell2 `803dc4d77e4fb1bf1c2f7b9b93a52eb0b4e90a9c8666aea889d6d70e74efc157`, cell3 `9296e31bb147b4532174b35263c5f7d76d94824cefef71a9ae89d03142fec8f5`

- Actual host finish: 2026-11-04T19:20:51.489390+02:00
- Wall-clock elapsed: 331.8 seconds (5.53 minutes). Time since report checkpoint 2026-11-04T19:20:13.464791+02:00: 38.0 seconds. Awake execution time unavailable. No clock change observed.
- Token stats unavailable.
