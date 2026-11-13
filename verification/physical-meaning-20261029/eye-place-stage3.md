# Eye/place revised passages: stage 3 reader understanding and flow

Local review request ID: eye-place-stage3-20261029-111528. Reviewer: /root/physics_eye_place_review. Scope: the changed explanations and their connected preceding/following material in 04-eye-drift, 04b-eye-timing, 05-place-fields, and 05c-place-tests. Current source read after stage 2 repairs. No manuscript edits or builds.

Started: 2026-10-29T11:15:28.6945801+02:00. Checkpoint: 2026-10-29T11:15:44.3452754+02:00. Wall elapsed at checkpoint: 15.65 seconds. Awake execution time unverified; Windows sleep/resume events were not inspected.

Audience: undergraduate calculus, basic probability, linear algebra; neuroscience taught by the guide. Used the current foundations' spike/rate/synapse/tuning and covariance/MSD explanations as earlier context. Did not assume knowledge of ocular anatomy, a neural integrator, or biological synapse implementation beyond what the text explains. The original stage 1 and stage 2 reports remain separate historical calls. This stage judges the current reading path, not source correctness afresh or the entire guide.

## Verdict

Pass for the assigned changed passages and their affected connections. No further required repair. The actual reader can follow what is represented, which signal acts on which object, what each parameter changes under the specified comparison, and which parts remain effective models rather than identified biological mechanisms.

## Reader tasks checked

Eye fit and offset: The earlier pathway identifies stored eye position, motor neurons, muscles, and actual movement. The recording design and calibration passage establish that rate versus angle is a fitted relation. The new coefficient interpretation then explains why the same angle can be associated with different firing during velocity or acceleration. x is explicitly angle relative to E_T before x=f/k appears. A reader can set the derivatives to zero using assumed calculus and explain the halved predicted offset, while the next sentence explicitly blocks treating one cell's rate as sufficient control of the eye. No unprovided muscle-force theory is needed or implied.

Eye filter: Earlier text defines MSD, logarithmic slope, low-pass filtering, white noise, and stationarity. It shows why decaying filtering of nonaccumulating noise reaches a plateau. The Brownian-command example then identifies B, E, tau, and D before relying on their physical interpretation. The reader can explain that a larger command-angle gap drives faster eye motion, a larger tau slows the response for the same gap, and a larger D increases the source's spreading. The derivation and limits state how these differences appear in measured MSD. The repaired bridge distinguishes logarithmic slope alpha from ordinary MSD growth rate. The later full-model limit prevents the one-time-constant example being read as a complete account of actual muscles or feedback.

Place threshold, input spread, and rate gain: The visible map paragraph introduces h(x), position x, and a fixed spatial map. The normalization equation and its next paragraph define sigma_h, z, q, and a. The reader can then distinguish three comparisons: raising q on the same standardized map reduces its active set; increasing sigma_h at a fixed positive absolute threshold above the mean lowers q; changing a alters active rates while preserving the zero-rate boundary. The positive-Hz-cutoff qualification keeps a detected field distinct from that mathematical zero set. The following excursion-set definition turns that active set into fields and explains how peaks can belong to one connected field. No missing neural membrane model is needed for these parameter comparisons.

Place covariance and circuit account: Foundations teaches synapses, excitation, inhibition, and spatial tuning. The wiring section assigns input cells and their fixed connection weights, limits the signed effective-input interpretation, and then assigns u_i and W_i. Its covariance expansion is followed by shared-input overlap, including the sign condition for positive versus centered profiles. Uniform coverage and smooth tuning explain the spatial assumptions. The reader can distinguish more/stronger input changing amplitude from broader input changing distance scale, then use the Gaussian example to check that distinction. The closing paragraph explains why this sufficient construction does not identify measured synaptic wiring.

## Fold-closed conceptual reading

Read 05-place-fields lines 15, 17, 32-50 and 61-85 as a continuous main path with the formal GP note closed. It retains the reason nearby values matter, the map's physical input role, fixed-over-space meaning, covariance's role, the three spatial assumptions, normalization, response rule, parameter meanings, and field geometry. The exact finite-vector Gaussian definition and proof-related independence property remain in the fold for readers checking the mathematics. The later crossing passage also explicitly says that height and slope are jointly Gaussian before using their independence, so the formal note has not silently become an unstated premise of a physical explanation. A reader deriving the crossing law may open the formal definition; the main physical explanation does not require reconstructing it from outside expertise.

The root's earlier foundations covariance fold was checked only for its relevant main-path context: current visible prose explains shared variation, correlation's private-noise denominator effect, MSD, and measurement error. The present report does not approve the whole foundations edit.

## Paragraph and connected-unit decisions

The table below records actual current paragraph text hashes. Formula blocks and list items are included where their relationship is part of the reading check. Pure fold/container markup is excluded because it adds no prose; titles are included in their described neighboring decision. Equations retain their independent correctness approval from stage 1. All decisions are retain; the reason states the paragraph's contribution and its connection rather than treating fluent wording alone as approval.

| Passage | Text SHA256 | Decision and connection |
|---|---|---|
| 04-eye-drift.md:11-11 | 650C22648E27FAFC78F9297E562CC3F94135CC258EA8284A7043AB317A70AED6 | Retain. Storage circuit first: gives the lasting-command problem and defines the integrator before muscle delivery. |
| 04-eye-drift.md:13-13 | 5995A87B00A2781BAAF082D1452DAE3C172E39E017DE07508448FD744D1DA3B5 | Retain. Delivery pathway: defines motor neurons and muscle/plant roles used by the later fitted relation. |
| 04-eye-drift.md:47-47 | A5553C8B5555C7A82E678AAA235473290AF1992E87FB9DA54586D7C3F3ECBFBA | Retain. Calibration purpose: explains large movements and defines gain before applying the relation to drift. |
| 04-eye-drift.md:57-57 | 33ADABDE654E5601E7E317575A762B5ECAE78BAE70B3B4ECCF75ADC46AACEB9D | Retain. Physical path versus analysis: prevents interpreting reconstruction as a backward biological signal. |
| 04-eye-drift.md:61-61 | 2D5A4BD1401864E33FC9FC4990186090A957C2651F19CBB7B6CBD5E46EB26288 | Retain. Fit motivation: the same angle can occur with different velocity and acceleration, motivating all three terms. |
| 04-eye-drift.md:68-68 | 35FBEF1321D69097D5535FE106BD53CA030F8ADA3646621FE938D6269E80E804 | Retain. Observable symbols: assigns position, predicted rate and threshold before their units and interpretation. |
| 04-eye-drift.md:70-76 | C6B64B7C522734DD410658DC9EF29F3A73572480426E69215DD859127F750FC0 | Retain. Unit check: matches each derivative term to firing rate before discussing its different motor role. |
| 04-eye-drift.md:78-78 | 2F0CFE2B999F5CF1596F2E748098EDFABF2FF080EAE22FC7651FD73FCC536220 | Retain. New physical interpretation: explains holding, passing and changing speed; limits coefficients and defines timing before fitting. |
| 04-eye-drift.md:80-80 | F3FC314E12BF31A6FD59E7B34DFB99E911184C925B34E79A5945CD1023947062 | Retain. Observed versus predicted rate: introduces rate estimation and the objective after the relation is meaningful. |
| 04-eye-drift.md:87-87 | C36D17F381179B57D22C89B867C01EC25FAA88683B6C1562B24179D0EE188176 | Retain. Fit scope: defines trial indexing and active-cell limits before interpreting fixation correlations. |
| 04-eye-drift.md:89-89 | 8ACA25E2B1096D955EE6C31AAD4214D98E204EC98DE20C0201DF33E98BAC3816 | Retain. Empirical bridge: states the tested rate relationship and why a weak cell relationship is expected. |
| 04-eye-drift.md:102-102 | 70DC4869B589BDCB1411F4AA4E031D924439531945BDFF04FAD85B4DA0F4C0FE | Retain. Inverse purpose: establishes the common degree scale and says inversion is an analysis operation. |
| 04-eye-drift.md:104-108 | AD0B4656D4946705D459724973745A3111AEC9F91B7BA8BC4025C9A9CA0AC349 | Retain. Offset definition and inverse relation: supplies x before the steady comparison and the filter calculation. |
| 04-eye-drift.md:110-115 | 5F1A776D0F94F24316B2F8F51EACDD2907FCD17E47B7882464BB289F251F69D4 | Retain. Filter vocabulary and factorization: defines response-to-spike and maps differentiation to algebra. |
| 04-eye-drift.md:117-122 | 0B3F0BBBBAFCCB67525640A22F79791014881671D7434790C3A6617EF4DCD028 | Retain. Characteristic-time step: obtains two response times from the just-introduced quadratic. |
| 04-eye-drift.md:124-124 | 5FFABB8CF8CA1427670EEFBEE6AAEA524194EC2C4F862EFB952F2B0F52DB3E5F | Retain. Conditions and behavior: now keeps positivity/discriminant assumptions directly beside nonoscillating decay. |
| 04-eye-drift.md:126-131 | 6E4433F1BBD99694E8870609ACECC7DE31FE1E3C9961D9A9B5CFF18C9D3A10CF | Retain. Parameter consequence and identity bridge: steady offset and noncausal-fit limit lead back to the two time constants. |
| 04-eye-drift.md:133-148 | A1E1BD501F720322F1EB9A6AFA9A7D772B7859BF99132769ABB5A41DBEA55182 | Retain. Output reconstruction: response kernel, causal delay and sum of spike responses complete the calibrated analysis path. |
| 04b-eye-timing.md:3-5 | 55C0EA32C320C56ADE1385580878672C3488DF7296F6DD7BA94D5789723CD2EA | Retain. Timing question: explains why a single displacement interval cannot distinguish wandering from stationary fluctuation. |
| 04b-eye-timing.md:62-69 | A26333EC6FABBA2C3D0EB32E242FF8D5A4E449EDF3D3EB561338815A6C7162CE | Retain. Slope meaning: defines logarithmic slope and interprets linear versus locally ballistic growth before filter comparison. |
| 04b-eye-timing.md:71-99 | 185CCC2330A178F6883F9051C7111DCDE0F616B4D26FFAC844D8ED5CDC85EE1C | Retain. Contrasting input: definitions and plateau result establish the nonaccumulating-noise case first. |
| 04b-eye-timing.md:110-110 | D99C6E36130F3060DA8CE8653156DF6BAA9A8EBE1948EBB480525CE2177578F4 | Retain. Alternative model: introduces wandering command and explicitly limits the one-exponential reconstruction. |
| 04b-eye-timing.md:112-116 | 0706E80F33B78B9956DC12C31B9E1EDC7D2B3C59B1231C5CA16C8D23AE862304 | Retain. Command-response equations: follow the question they answer rather than introducing unexplained abstract filtering. |
| 04b-eye-timing.md:118-118 | 2F80D95493C1D424754D113C2B4BFE8DF26CEDA6CA85E632DE6391B89251BD56 | Retain. New mechanism: defines B/E and gap-driven velocity, explains tau, and distinguishes synaptic response time. |
| 04b-eye-timing.md:120-124 | CF72DD6D33530189C7B3BE29AF8330F3CE46215730C8E0CF9203AC5282F4A3C9 | Retain. Noise and velocity symbols: gives Brownian units and derives a velocity equation from the explained mismatch. |
| 04b-eye-timing.md:126-126 | E6A244842C79DF64DE991F24286C67E421AC4195C94EFDC7CA78D717BF851983 | Retain. Weighted-history construction: explains what survives from each independent input interval. |
| 04b-eye-timing.md:128-132 | FB9CE630A122EF0325286A6787A801C3BD46E4DE09CC536C924B39574D24E7DB | Retain. Integral meaning: supplies the weighted-sum limit and initial-transient condition before using infinite history. |
| 04b-eye-timing.md:134-143 | 107DB5207147CADBBBE4DFAED78FEC0079BC5C81F8387EA04B841B66DBA4EEBD | Retain. Covariance derivation: explains why only shared past increments survive averaging. |
| 04b-eye-timing.md:146-154 | 91DA826159382A89ED03D8980FBEF0FDBBD0066D5481AE70F9734A1A283EFC74 | Retain. From velocity to displacement: turns the covariance calculation into the statistic measured earlier. |
| 04b-eye-timing.md:157-169 | 1C82C20A927372CA5345E764F5C59654D531407E81B9BDB5D4EEEE355D634202 | Retain. Limits: interprets short-lag smooth motion and long-lag accumulation before parameter comparisons. |
| 04b-eye-timing.md:171-178 | 20043E46548D93A0260B36FE12F42F785ACCBC2AC643AEE98123E5A4F0E45470 | Retain. New parameter comparison and slope: distinguishes tau from D effects, then clearly labels logarithmic alpha. |
| 04b-eye-timing.md:188-190 | 0739910AD15CD06F43F8D53C10224DE45337D1216AAF23629D5ACABAB1E7EBDB | Retain. Model boundary: restricts the white-input slope to this example and returns to the fuller muscle/feedback setting. |
| 05-place-fields.md:15-15 | CF3931630BD66D71DE8518D443FC4B71F41ADE0A3E68C41D522D4C3108417994 | Retain. Map question: explains why a value histogram cannot determine field width. |
| 05-place-fields.md:17-17 | 86A390DA6D0D6DC37BA234E189086E68AA3B3D8E8CB12C0C1E054C665950CAEF | Retain. New visible map setup: gives h(x), fixed spatial sampling and covariance role before optional formal details. |
| 05-place-fields.md:21-28 | 95F6454F345B5A0EC6D31876A13A8AAAA54A9F4977D19185F7E0442F66ED013D | Retain. Formal fold: exact GP definition and Gaussian independence fact support calculation without replacing the main input explanation. |
| 05-place-fields.md:32-38 | 321DCE1C06BE6076CAEBA1C77D5097E2C6BC97FA029B7C3063E72064829ACF6B | Retain. Spatial assumptions: defines stationarity, isotropy, smoothness and a nonsmooth counterexample before derivatives. |
| 05-place-fields.md:40-46 | 3B3D2750419C0A4B9F7FAF5FEE78DB7BBFD45BE8087CB506B77045079FDD49C2 | Retain. Normalization and response: ties input spread to a dimensionless map and rectified firing. |
| 05-place-fields.md:48-48 | CE7EB0A4F37F7C549990CEB25320BEB5EAA6985BCC1DDA9D3463FB491977207B | Retain. Symbol and gain interpretation: defines q and a and maps paper symbols to the guide before comparing parameter changes. |
| 05-place-fields.md:50-50 | A6B1AD4CB5499653ECBF7B47A460D1E529731CB76C04082ECB9EC1FEC16005EF | Retain. New biological/parameter meaning: distinguishes threshold, input spread, firing gain and detection cutoff without identifying a hidden cause. |
| 05-place-fields.md:61-67 | 1ADCA7E600BDCF9EED9CD76DCF0B7AD85E09498D93A931763407A215215139CF | Retain. Active-set geometry: translates the response rule into fields and distinguishes connected fields from peaks. |
| 05-place-fields.md:69-83 | 2525542DF71E92D7512B44C79D115F5AF14AD6E3DA64377B2D6D4FCEA2E45C8D | Retain. Local distance scale: derivative variance becomes sigma and is interpreted as height relative to slope. |
| 05-place-fields.md:85-85 | EBDD8B0016BAD74B9E16AE42E4D433C8876D5071B8D33A62976EE07FD385B961 | Retain. Concrete map parameters: states which normalized covariance, threshold and gain produce the following example. |
| 05c-place-tests.md:200-200 | 30E3871F3BAD882F606126C235A5966435172AD279AEB11ADC8329E5945EE265 | Retain. Circuit question: motivates a sufficient construction rather than claiming that fit determines wiring. |
| 05c-place-tests.md:202-202 | AB2036762A39BE9D87E142DB79FF937001D5D7C0FBDEA0A4F66E9C082CC9EFFA | Retain. New physical setup: identifies input profiles, fixed weights and background before signed statistical symbols. |
| 05c-place-tests.md:204-208 | 226D8A5B607445FCBE6141541FF632AF4D568547BFDF2DDEA235BA3660A15F67 | Retain. Model symbols: assigns u/W/variance and the averaging ensemble before summation. |
| 05c-place-tests.md:210-210 | F03C2FB286E932A8ABDE3A5D115DAA53C64AD5BE34E90BDB9110F157AEE7D49F | Retain. Gaussian construction: gives many-input conditions and warns that anatomy alone does not satisfy them. |
| 05c-place-tests.md:212-220 | C78611CABAA3D69A556EE1107C3CAE87111A5F32B2D7935F782DA561C08A86C5 | Retain. Covariance derivation: uses the stated weight assumptions to reveal shared spatial input. |
| 05c-place-tests.md:222-222 | C4EB7325FA7F0D49084503224892C66AAC55A440DBD2635241E43C433C8F9C5D | Retain. New interpretation: explains shared fixed weights, positive-profile overlap and signed deviations immediately after the sum. |
| 05c-place-tests.md:224-228 | 7B6DFAD7573B36B30A8AFE7371AD6EFEADF23B5FB26496228FEC634B4B0397BB | Retain. Spatial simplification: translated uniformly covering profiles produce the separation-only covariance integral. |
| 05c-place-tests.md:230-236 | 606968FAD7E32382471364F65D362B2D076875BBDCA2A336C70C345BBDA6E7F0 | Retain. Assumption roles: assigns stationarity/smoothness/Gaussianity and extends to diverse profile shapes. |
| 05c-place-tests.md:238-238 | 1802CA0BD310D2485430F44358EEC676A43663FAC05D55C5C9BEC5A38D82B9B8 | Retain. New parameter consequences: separates amplitude/density from width and connects amplitude to earlier effective q. |
| 05c-place-tests.md:240-247 | D5B564FB3ADBB59D2D198A823FA460F15D47B2C239B64DAC3050A4DB684248F1 | Retain. Width example: supplies a concrete profile and shows the input-to-covariance width conversion. |
| 05c-place-tests.md:249-249 | E835B9977F7AED2F3E810F609834C0207090ED4589A1870F20EACD948C6210D8 | Retain. Evidence limit: fit does not recover measured synapses and spatial assumptions may fail in structured environments. |
| 05c-place-tests.md:251-251 | 8F0FA7F518ECF4E1C1E5A343CBFE1DF99C431550B705147F661DFB7BBF13384D | Retain. Synthesis handoff: carries the statistical result forward while keeping mechanism an additional measurement question. |

## Final connected read

Read the changed units again in their actual sequence after recording the decisions. The source progresses from concrete roles to formulas to controlled parameter effects and then to limits. No later step requires an unintroduced physical actor or turns the fitted coefficient into a measured biological implementation. The formal GP note can remain folded for the conceptual path; a mathematical derivation reader has its exact content available. No new missing premise, contradiction, or required move found. The static-fit paragraph interrupts the algebra briefly for the requested parameter meaning, then explicitly returns to the same factorization; this is acceptable rather than a required structure change. Token stats unavailable.

## Current source and rule hashes

C:\dev\clsc\burak-papers\guide\content\chapters\04-eye-drift.md SHA256 A41B01F6486D719A8C11CE80D4D1D8A6BF89356B3E339781F9C99494E20C8CE6
C:\dev\clsc\burak-papers\guide\content\chapters\04b-eye-timing.md SHA256 09D2FE568CD0BCF9A9130BF7318E273AA8B13C4142FAAE0DD74D0873D4A4DDD4
C:\dev\clsc\burak-papers\guide\content\chapters\05-place-fields.md SHA256 342268F4D10C4D5ACE00D23D10372638AC7BBE982CF574BB08B33764E921FCB9
C:\dev\clsc\burak-papers\guide\content\chapters\05c-place-tests.md SHA256 A30E5C2DD6F101524AFFD5761922B18D95D76361B46698F1EB9120C3755689C4
C:\dev\clsc\burak-papers\guide\content\chapters\01-foundations.md SHA256 E4FD06733F893BF1334702F3D7045844415A988032CC0B583105833CD430E42A
C:\Users\vital\.codex\skills\course-study-guide-builder\SKILL.md SHA256 B78068E9874E6D1D97B2017BF8F940492F9B08FC11B74F20FD75019FF388984A
C:\Users\vital\.codex\skills\course-study-guide-builder\references\pedagogy-language-contract.md SHA256 F4C1EB544CF640B708E1970D9572FDC758FCC6AEA806675D01A0256658DF847A
Completed: 2026-10-29T11:17:59.4901742+02:00. Measured wall elapsed 150.8 seconds. Awake time unverified.
