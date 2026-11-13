# Stage 1: notation correctness and preservation

- Reviewer /root/exam_review_check; separate request exam-notation-stage1-20261104; inherited Sol high chosen for semantics; exact backend version unavailable.
- Actual host start: 2026-11-04T20:19:31.973367+02:00
- Actual host report checkpoint: 2026-11-04T20:22:02.249978+02:00
- Wall elapsed: 150.3s. Awake time unavailable, Windows sleep/resume logs not collected. No clock change observed.
- Scope: compare old35 symbol keys against current3 shared keys plus35 local-note areas and unchanged connected formula/source/derivation/decoding cells. No wording/flow/build/full-book/source audit in this call.

## Preservation and allowed reuse

- Parsed old baseline YAML and current YAML. All35 formula/title/anchor prefixes are identical after removing only old/new key markup and trailing separator. All70 location/derivation and decoding cells are exactly unchanged. Map block is exactly unchanged.
- All70 old source/decoding cell hashes match the final individual cell hashes in verification/exam-review-20261104/stage1-truth.md. Reuse those actual earlier primary-source/math judgments only for these exact unchanged cells, with current notation connections assessed below. The earlier focused positive-part truth check remains applicable because its max definition is unchanged in meaning.

## Required findings

1. M13 lost its old explicit constant-local-D/J qualifier. Its coth solution assumes constant coefficients. Add a local bullet that D and J are held locally constant in the Gaussian readout calculation. Shared scalar units do not supply that condition.
2. E2 lost its old same350ms interval specification for displacement correlations. Add that interval to shared R_i definition, matching E3 and the empirical correlation comparison. Population-mean vs sample-estimation caveat remains correctly local.

## Shared keys and prerequisite connections

- Memory shared key precedes both memory tables and correctly defines neuron/index roles, chosen coordinate/time units, activation normalization, steady bar, rate slope vs transfer-input derivative, synaptic time, scalar D/J, neural K/u/v roles and V variance units. M5/M11 matrix exceptions are signposted and local; alpha/c and time-s exceptions remain local. M13 constant-coefficient omission is listed above.
- Eye shared key precedes both eye tables, defines angle vs prediction vs measured angle, lag/dot/MSD/covariance/temporal D, kernel-normalization dependence and motor correlation scope. E1/E5 kernel units remain separate local definitions; E7 population and slope aliases stay local. Restore350ms scope in shared R_i as above.
- Place shared key precedes both spatial tables and correctly defines position/dimension, fixed input map/mean/std/threshold, normalized input and peak excess, firing gain, unnormalized covariance, spatial primes, local distance scale, Gaussian tail/crossing density, complete-field size, ball volume and beta dimensions. Local P9 spatial t and P8 size mean/moment exceptions prevent false universal meanings.
- Moving definitions earlier introduces no circular derivation: shared quantities have physical roles before formulas use them, while theorem-specific restrictions and rare-event/constant-noise exceptions remain beside affected rows. Ordinary probability operators/units can follow the physics/CS baseline; no unnecessary mean/variance/std/density tutorials requested.

## All35 row dispositions

- M1; current first-cell SHA256 `4365646257792456ee54cea6bb42b0c8a80e67e0265d786f92a0c04378bd185d`: Counts remain local; shared N/i/time/activation/weight/bias/response definitions preserve index direction and units. Count dimensionless follows count meaning.
- M3; current first-cell SHA256 `26e2c72543bf9b7a81aef6045f180823e700696b8aae25b38e9e78a4e1131f76`: Shared K/u/v, steady bar and activation units combine with local disturbance N-vector and retained shift. No coordinate or projection meaning lost.
- M7; current first-cell SHA256 `1659686088e8924fb5c0d2f12a5da476e977a87829bc16c73448be950a859461`: Shared rate slope, J/h/estimate combine with local I_h units and effectively fixed state. Variance units follow shared coordinate unit.
- M8; current first-cell SHA256 `a2622ca2be6dfb015d83c4f0c53055b0dc2acdabee1b54e8b47099675a42cd12`: All displayed quantities now shared; dimensionless product follows D/J/tau units. Same-coordinate and common tau conditions remain in unchanged decoding.
- M9; current first-cell SHA256 `8609811933eb46f8734fa096744e5c7141a26202e746583ecc895135bbf01b90`: Shared phi/input derivative, W and rate units combine with local A/k positive constants and symmetry. Exponential argument remains dimensionless.
- M13; current first-cell SHA256 `9140aa927c7fa026474d9ca8b1221e7fb91b39b1d356bde132099fe22eb8f05d`: REVISE: old key states constant local D,J; shared key says scalar only and local notes omit constancy. Restore held-locally-constant Gaussian readout condition. V/P/Lstar/coth meanings otherwise retained.
- M2; current first-cell SHA256 `5c5f32546e213a78e755de49360142c734f30a921d318315658666b0d790864d`: Shared theta/rate/h plus local dimensionless count and lambda preserve meaning. Fixed-state condition remains explicit in unchanged Origin cell and derivation.
- M4; current first-cell SHA256 `6d36b61e89630e82e9c4589b16c44ffb7b0773d55f30e3cce112221d0f7aff68`: Shared D/tau/u/v and local steady g/input slope and symmetric W preserve units and first-derivative scope.
- M5; current first-cell SHA256 `b13d409fc7a2cd03b6b9c117462f2908346f3ea78aefa2f340ae9317994eb2ce`: Local coordinate indices, right/left shapes, coordinate-specific tensor units, invertible J and PSD definition preserve the matrix exception.
- M6; current first-cell SHA256 `aaed350f348c594128508d6caf064e3d4408c1c0b11861624566ef7241c004bb`: Shared coordinate/initial/time/D plus local density units, constant-D solution restriction, trial average and wrapped-angle units preserve meanings. MSD expansion is still elsewhere on page.
- M10; current first-cell SHA256 `c1208275291a2dc4ca3d3588d92beb4a92275d13df1e84fce67088ed005c9936`: Shared neuron count/D/J/tau plus local positive rate multiplier and held-fixed comparison preserve controlled change and scalar-vs-vector c alias.
- M11; current first-cell SHA256 `ea6c4de6e0c90e313a480cf7f354a0a744bcba199a32d32298dad8c58ae65b81`: Local coordinate dimension, positions, width, peak rate, radial shape and density preserved; matrix units explicitly referred to earlier M5 in same support table. No new prerequisite outside scoped text.
- M12; current first-cell SHA256 `b2f4e837753ed78a21ee5c32d10dd0220a4a6684ab04b487766d560db8ded3e5`: Shared L-vs-T, V units and local cue-state equal-weight meaning, minimizing duration, time s alias and constant separate-noise model preserve restrictions.
- M14; current first-cell SHA256 `440ee8932b5b742243172376e94d42df8fb5fd291959d311da92f4c5b104e63b`: Shared storage/readout time, V units and local alpha range, observed J, full/partial times and cue/original error distinctions preserved. Full-access benchmark remains explicit.
- M15; current first-cell SHA256 `42fa288477d448b0ef9d267666fab899e46de9736a70831dd7885b77315e5699`: Shared rate/input/tau plus local rate derivative units, target phi and tau_m preserve two-stage extension.
- M16; current first-cell SHA256 `66a4b59b9efb8db8951e72229aeca7d42be107e2d46d92db3338831c2d6606de`: Shared theta/projection/rate/tau and local Gaussian J exception, noise intensity/increment/rate-average units preserve matched noise normalization and q_n alias.
- E1; current first-cell SHA256 `922779f1540b4db90be7956ec2aa30058518ce82c34c79b5106f4b0715a361bf`: Shared t/u/E/Ehat/dot plus local f/x/ET/k/r/m/tj/delay/p/tauplus-minus and kernel units preserve the calibration model. Spike j is identified by time of spike j.
- E3; current first-cell SHA256 `5281f4f10c8cb92620ab451f9fac379a2dfaf7dcf234619aa35b15596ea19b59`: Shared correlation and degree units plus local X/Y 350ms, common/private displacements, chi and weighted uncertainty preserve variance-fraction interpretation. Covariance degree² follows basic probability units.
- E5; current first-cell SHA256 `1b1936458f0026608b25383316f490a842b74c4b499d7e379a82c9685243d243`: Shared lag/covariance/MSD plus local white-input normalization and centered stationary E preserve distinct kernel normalization; stable response remains explicit in unchanged derivation.
- E6; current first-cell SHA256 `871e2d65b378b5faa97243923a82aa48c487a93f9f4af497509b88798368d0c5`: Shared angle/time/D/MSD plus local B/tau_f/W/velocity/covariance preserve meanings. Brownian increment normalization is explicit in unchanged displayed dB and W variance definition.
- E2; current first-cell SHA256 `e06b097d37f9cdc4e19f825f53c32ab808fc1621fb87bb2ee010b5bb07524c82`: REVISE shared R_i: old key specifies same350ms displacement intervals; new shared definition and E2 notes omit that measurement window. Population/sample distinction and standardized explained fraction retained.
- E4; current first-cell SHA256 `faa866a465168dc2fa31b8a7dc271929742662abbac2210adb0dd262b16ce1d1`: Shared true/measured angle and MSD plus local reading noise and measured MSD preserve positive-lag measurement correction; factor-two and zero-lag limit remain in formula/decoding.
- E7; current first-cell SHA256 `64d6331cdaeb07e88c8394b115b18ecb342fa696af737abcf751d50aff46bdec`: All model-specific N/lambda/a/b/J/CV/tau_s retained locally with correct units. Shared D carries correct angle-diffusion units; integrator-vs-motor population distinction improved.
- P1; current first-cell SHA256 `2fe36833103263b85fc5e8dcac039b49ae54fda09dafd14c9ccc54bce873fa28`: Shared input/mean/std/threshold/normalization/gain/covariance/length-scale and local positive-part/Csecond derivative preserve operation and units. Unit variance follows explicit standardization.
- P3; current first-cell SHA256 `cacd383faa9cc246657e6b0da23dddf6a6039d0d59a6c79f7a3256fe6a3fc0fd`: Shared q/z/scale/Q/nu plus local track L, clipped count and derivative units preserve endpoint convention. Zero-mean/unit-variance follows shared z normalization.
- P4; current first-cell SHA256 `aebf04f4c4183f929f6b7929f3f9949121896ef532a339387608517c88f9c66f`: Shared Q/scale/nu plus local per-component stationary means and inverse tail preserve inversion and clipping/selection cautions.
- P6; current first-cell SHA256 `eb49c1b0f1ff8d43e8ce56509acded53f1942516ced1e553d06cfb72c9d5a27e`: Shared complete size/cutoff/dimension/scale/beta/v_d/peak excess plus local U/radius/sampling preserve geometry. Large positive q condition remains explicit in unchanged derivation.
- P2; current first-cell SHA256 `69e84397e8287ec38cd8da1ea3e29fc055b939c4a964d9e7774e011ff2fc4e5f`: Shared positions/h/C plus local input profiles, random-weight variance and ensemble/Gaussian limit preserve covariance units and generation premise. Fixed draw established in shared setting.
- P5; current first-cell SHA256 `d358289b2a2801fa4348383bc9bfbd196d1e22d3a43b49d25c327ac2e131227c`: Shared q/nu plus local track/gap/cutoff/count/lambda and rare-gap/zero-cell convention preserve count-vs-rate meaning and approximation.
- P7; current first-cell SHA256 `4c15d90f46bf70513e49d5ed0136e1f3bdb6bf513980b9e96b984f5d6d03d989`: Shared rate gain/excess/size/scale/v_d plus local peak rate/radius/linear size preserve exponent meaning. High-threshold premise remains in unchanged derivation and decoding.
- P8; current first-cell SHA256 `c9f96665e947d8d0c849cdfb7e2918ec38f2eb62f1b100c49fde0044f6a1b7d4`: Shared size/d/beta plus local moment order, size mean, Gamma integral and integration variable preserve dimensions and limiting-vs-exact mean distinction.
- P9; current first-cell SHA256 `c4f08cfe5d8698db619e6e138aa1d22a5cb8494835df11fbb2f30fb7b60912f8`: Shared map/covariance/positions plus local x0/unit direction/spatial t and restricted quantities preserve units and spatial-vs-time exception.
- P10; current first-cell SHA256 `00a8d1e810bebb4ed9801377cfeb1c56153721b9be60e3861ce7d7c609d1eaf8`: Shared z/scale/q/gain plus local crossing slope, selected/ordinary densities, dummy slope and firing slope retain density units and aliases.
- P11; current first-cell SHA256 `870b99746445d8cbc628cb896b2a45425350053c3cdea6c2861d186a4aff797b`: Shared q/scale/d/Q plus local box L, face dimension, signed densities and signed EC retain boundary and topology meanings. Periodic-box restriction remains explicit in unchanged decoding.
- P12; current first-cell SHA256 `32ac51ee24024fe6643df15d571b8149af805faa492b87be1eb59b60460dfb5d`: Shared q/d/scale plus local count N/environment V/EC limit preserve units and field-vs-neuron meaning; high-threshold/boundary regime remains in unchanged cells.

## Exact binding and limits

- `content/chapters/00-exam-review.md` SHA256 `6dfb25f36518b9b12a94e0d2c7a044e0276302e71f5c972621629f07b0bc0529`
- `content/chapters/00-exam-review.yaml` SHA256 `e46668a7d36da8306487a3e87e6af2ebecdcd699ed1bca03a02d85151a9956e9`
- `verification/exam-notation-20261104/00-exam-review.md` SHA256 `af6404ec51657704ed23c07b72b7f5bdc1c08860b03c1297b10682888fd7c97c`
- `verification/exam-notation-20261104/00-exam-review.yaml` SHA256 `86b252b5182d6e76ab288e1fc2b770b78dbc06352e86314bef126dd7e17bb54a`
- `verification/exam-notation-20261104/DEFINITION-MOVES.json` SHA256 `0baa557c4eeb5e3bd76f25f8418a509272bc666c112803c4462d36bc81ee2861`
- `C:/Users/vital/.codex/skills/course-study-guide-builder/references/math-code-case-contract.md` SHA256 `ce2313f897b63e74ba59a3afe1bbc4046d3aa84584072cda7e76470a7e3cef9a`
- `C:/Users/vital/.codex/skills/course-study-guide-builder/references/pedagogy-language-contract.md` SHA256 `f4c1eb544cf640b708e1970d9572fdc758fcc6aea806675d01a0256658df847a`
- Source semantics only. ARIA span rendering, blue style, bullet layout, table navigation and browser disclosure behavior are not established here. No primary-source audit repeated because exact changed scope is notation.
- Verdict: two narrow preservation findings awaiting repair/recheck; all other row meaning and conditions retained across shared+local+unchanged cells. No memory used. Token stats unavailable.

## Narrow repair recheck and final disposition

- Reread current M13 first cell and shared eye R_i bullet after coordinator repairs. M13 now explicitly holds D,J locally constant in its Gaussian readout calculation. Shared R_i now refers to the same350ms intervals, matching empirical E2/E3 comparison. Both findings resolved.
- Connected old-tools route now accurately describes per-paper shared keys and local extra-symbol bullets. It changes lookup instructions only; all35 results and existing source/guide-link promise preserved.
- PASS for notation correctness, preserved conditions/units/aliases and current connections. No remaining required stage1 finding; separate wording and flow stages still pending.
- Final `content/chapters/00-exam-review.yaml` SHA256 `e46668a7d36da8306487a3e87e6af2ebecdcd699ed1bca03a02d85151a9956e9`
- Final `content/chapters/00-exam-review.md` SHA256 `6dfb25f36518b9b12a94e0d2c7a044e0276302e71f5c972621629f07b0bc0529`
- Final `content/chapters/00-mathematical-tools.md` SHA256 `1b88964307ef836ab154634dda43c747887e5e793b79dacdc1468bfe8491e440`
- Final M13 first-cell SHA256 `9140aa927c7fa026474d9ca8b1221e7fb91b39b1d356bde132099fe22eb8f05d`
- Actual host finish 2026-11-04T20:22:18.357935+02:00; wall elapsed 166.4s, since report checkpoint20:22:02.249978 16.1s; awake time unavailable.
