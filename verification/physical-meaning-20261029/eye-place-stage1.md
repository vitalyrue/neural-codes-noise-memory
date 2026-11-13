# Eye/place revised passages: stage 1 truth and reasoning

Local review request ID: eye-place-stage1-20261029-110902. Reviewer task: /root/physics_eye_place_review. Stage requested by root: correctness only, with independent wording and reader-flow calls still pending. Manuscript not edited.

Started: 2026-10-29T11:09:02.1169458+02:00.
Checkpoint: 2026-10-29T11:09:38.3453696+02:00. Measured wall elapsed at checkpoint: 36.23 seconds. Awake execution time unverified; sleep/resume logs not read. Earlier review work and idle time before this call are not counted as this stage's duration.

Scope frozen at request: inserted/changed prose and its connected equations in 04-eye-drift.md, 04b-eye-timing.md, 05-place-fields.md, and 05c-place-tests.md. Read actual manuscript passages, the matching entries of edits.json, original .before snapshots, and the rules already loaded for this task. Mainali supplemental Methods S1/S2 was directly rechecked during this call; source facts from the earlier same-task read of the local Ben-Shushan and Mainali PDFs are identified below. This is a focused repair review, not a new full-chapter audit.

## Verdict

All inserted scientific and parameter claims are correct under their written assumptions. One small notation repair is needed because the GP definition moved into a fold. No scientific claim needs reversal, no biological implementation is established from fitted coefficients, and no equation change is required.

Required repair S1-N1: 05-place-fields.md line 17 says "The model assigns a random input value to each position" without assigning that input the symbol h(x). The only earlier assignment of h is now inside the optional fold, lines 21-25. Main text line 43 then uses z(x)=h(x)/sigma_h. Put h(x) in the visible input sentence, for example "The model assigns an input h(x) to each position, with nearby values linked...". This keeps the input's physical role outside the formal fold. This is a symbol-definition issue, not a false mathematical formula. C is introduced visibly in the stationarity sentence at line 34, so it does not need a second formal definition.

## Passage judgments

1. 04-eye-drift.md lines 61-78, forward-fit interpretation: retain. Position, velocity, and acceleration terms have the printed movement-to-rate equation's roles. The prose describes their association with motor firing without claiming that a spike itself measures position, speed, or acceleration. Their units remain explicit and give spikes/s in each term. The warning that m is not measured eye mass is correct because m has units spikes s/degree and belongs to an empirical firing relation. Source: Ben-Shushan main p. 9, Eqs. 2-3; the source's muscle/plant use is p. 11, Eqs. 28-31. No unsupported literal stiffness, friction, force, or inertia identification was added.

2. 04-eye-drift.md lines 102-130, inverse-fit parameter interpretation: retain. Setting derivatives to zero in m x''+r x'+k x=f gives x=f/k. With the same f and fixed E_T, k doubled halves the predicted offset. The statement is expressly about a fitted relation and rejects interpreting manipulation of one cell as sufficient control of the eye. r and m enter both characteristic times. The adjacent nonoscillation claim still depends on the explicit k,r,m>0 and r^2>4km condition immediately preceding the new paragraph, so it remains true. The insertion makes "In this case" farther from that condition, which can be considered in the later wording/flow call but does not change the mathematics.

3. 04b-eye-timing.md lines 110-123, command-following interpretation: retain. The equation gives E'=(B-E)/tau. For tau>0, positive B-E gives rightward velocity with the stated angle convention, and greater tau lowers the velocity for the same mismatch. This is an effective one-exponential teaching reconstruction, already explicitly distinguished from the full muscle model. It does not imply that the actual eye has only one time constant. Distinguishing this tau from the recurrent model's synaptic decay time prevents an incorrect parameter identification. B and E are degrees, tau seconds, velocity degrees/s, and D degrees squared/s.

4. 04b-eye-timing.md lines 149-178, parameter effects on MSD: retain. M=2D[ell-tau(1-exp(-ell/tau))] gives the short-lag law D ell^2/tau, a transition controlled by ell/tau, and dM/dell=2D(1-exp(-ell/tau)), which tends to 2D. Thus larger tau reduces short-lag MSD, delays the crossover, and does not remove long-lag accumulation. M is exactly proportional to D at fixed tau. "MSD growth rate" correctly refers to the ordinary derivative, while the following local logarithmic slope is alpha and tends to one. The derivation assumes stationary velocity after initial transients, as retained immediately before it. This is the guide's labeled reconstruction of the filtering distinction in Ben-Shushan main pp. 6-8 and Fig. 5, not a new empirical fit.

5. 05-place-fields.md line 17 and GP fold lines 19-30: retain scientific statements, apply S1-N1 for visible notation. The prose says a GP is a distribution over fixed spatial input maps, not a temporal random walk. The selected covariance must support the derivative regularity; it does not claim every Gaussian process is smooth. The fold correctly states the finite-dimensional Gaussian definition, expectation across maps, and the zero-covariance/independence fact restricted to joint Gaussian variables. The later crossing calculation explicitly restates joint Gaussianity when it uses independence. No GP property was lost; only h's visible assignment needs repair.

6. 05-place-fields.md lines 40-50, normalized threshold/gain interpretation: retain. Source: Mainali supplement Methods S1 describes threshold-linear transfer of mean spatial synaptic input, influenced by intrinsic dynamics and noise; main p. 1116 identifies intrinsic cell properties and inhibition as possible sources of threshold differences. The guide says "can reflect," so it does not claim the rate maps identify a particular mechanism. With the input mean absorbed into threshold, q=(T-m)/sigma_h. The inserted positive-numerator condition is needed and present: at fixed positive T-m, larger sigma_h lowers q. At fixed standardized map, increasing q shrinks its active set. a>0 multiplies rates and leaves the zero set unchanged. A fixed positive detection cutoff t introduces the level q+t/a, so the inserted cutoff qualification is correct and agrees with 05c line 117. Input h's absolute physical units are unspecified; the prose does not invent volts or amps.

7. 05c-place-tests.md lines 200-218, effective input and signed weights: retain. Actual source recheck: supplement S2 says spatial profiles may represent rate deviations from means and that balancing can arise through lateral inhibition or regulation of excitatory and inhibitory input. It also specifies independent zero-mean weights with finite second moment. The guide keeps that simplified statistical description separate from measured signs of biological synapses. Its profiles may have nonzero spatial means because E_W[h(x)]=sum_i E[W_i]u_i(x)=0 at each fixed position. This expectation is over weights, not a promise that one map's spatial mean is exactly zero. The relevant existing clarification remains visible.

8. 05c-place-tests.md lines 214-238, shared-input covariance and parameter comparison: retain. Independent zero-mean weights give E[W_i W_j]=v_W delta_ij, hence C(x,y)=v_W sum_i u_i(x)u_i(y). Each positive-profile shared input contributes nonnegatively; centered profiles can give either sign, as the inserted sentence states. For dense uniform coverage the integral multiplies by v_W rho. Increasing either factor while holding profiles and the other factors fixed changes amplitude without changing normalized dependence on distance. Spatial dilation of the profiles dilates their autocorrelation. The Gaussian example directly checks width: its autocorrelation is proportional to exp[-Delta^2/(4b^2)], so sigma=sqrt(2)b. Input strength can change normalized threshold at a fixed absolute threshold; "can" correctly avoids promising a change at a zero threshold or under a compensating threshold change. Units of h and W remain effective model units, not measured synaptic conductance.

## Boundaries and remaining work

No source figures were changed; no builds or rendered visual checks were needed for this correctness call. Wording and flow are not approved by this report. Root should apply the h(x) repair, then recheck this narrow notation point before requesting or completing later stages. Any later change in meaning or assumptions returns to correctness review. Token stats unavailable.

## Frozen source and rule hashes

C:\dev\clsc\burak-papers\guide\content\chapters\04-eye-drift.md SHA256 79AB27AFD4B79AE930308B5AAE2AB7372DF51438FAA28A8453772DA213E4D916
C:\dev\clsc\burak-papers\guide\content\chapters\04b-eye-timing.md SHA256 5EC09C5367F2EB8FD042B8736FE2019B7E11B5D39D6E550797EFB01DC8373693
C:\dev\clsc\burak-papers\guide\content\chapters\05-place-fields.md SHA256 342268F4D10C4D5ACE00D23D10372638AC7BBE982CF574BB08B33764E921FCB9
C:\dev\clsc\burak-papers\guide\content\chapters\05c-place-tests.md SHA256 A30E5C2DD6F101524AFFD5761922B18D95D76361B46698F1EB9120C3755689C4
C:\Users\vital\.codex\skills\course-study-guide-builder\SKILL.md SHA256 B78068E9874E6D1D97B2017BF8F940492F9B08FC11B74F20FD75019FF388984A
C:\Users\vital\.codex\skills\course-study-guide-builder\references\pedagogy-language-contract.md SHA256 F4C1EB544CF640B708E1970D9572FDC758FCC6AEA806675D01A0256658DF847A
C:\dev\clsc\burak-papers\guide\verification\physical-meaning-20261029\edits.json SHA256 33AC4A9B600782B7F7E350348072362E2376D41C5857A9D8B51AF28059D7F391
C:\dev\clsc\burak-papers\guide\verification\physical-meaning-20261029\04-eye-drift.md.before SHA256 75A063FB0EE980F2A6B8AE0EC5EF3754A233BCC91F07935F4E5BA6D116015739
C:\dev\clsc\burak-papers\guide\verification\physical-meaning-20261029\04b-eye-timing.md.before SHA256 76FCC3C48A68737FBA410B944FC92E74C01A163FECDD963C3865B6F95FB8EE8A
C:\dev\clsc\burak-papers\guide\verification\physical-meaning-20261029\05-place-fields.md.before SHA256 478D029C3F8DA895BBC218F66BEBA290562B49DB84F5223B196C85D96501F71D
C:\dev\clsc\burak-papers\guide\verification\physical-meaning-20261029\05c-place-tests.md.before SHA256 6E8E9088EDD71BA192FF786D805CFD92A24E76DD3553217743F3F597F8205955
C:\dev\clsc\burak-papers\guide\assets\papers\ben-shushan-2022-fixational-drift.pdf SHA256 15F273F99BD8D8E8DAA09A9F7809E04C53DA514B146750C0EC517812E3478CAA
C:\dev\clsc\burak-papers\guide\assets\papers\mainali-2025-universal-statistics.pdf SHA256 DE2CA50A46F5B0D8D14E86269F1BEACF6AADDE7122BB348568AAD92B12FD802E
C:\dev\clsc\burak-papers\guide\assets\papers\mainali-2025-supplement.pdf SHA256 05AF1FDF3079906871DA12FDAFA1F28895380F594A8C6BDA3CAFC5B503F07C31

Completed: 2026-10-29T11:11:06.3502539+02:00

## Focused recheck after coordinator repair

The coordinator added h(x) and x to the visible input-map sentence and wrapped the plain GP description in the definition style. Actual revised line read at 2026-10-29T11:11:16.5520014+02:00:

> The model assigns an input h(x) to each position x, with nearby values linked so that a cell can have a continuous active region. A Gaussian process specifies a distribution of such maps.

S1-N1 is resolved. h now has a visible physical role before z=h/sigma_h, and x is explicitly the animal's spatial position. The style span changes no scientific claim. Formal GP definitions and assumptions remain present in the fold, and later Gaussian independence use remains explicit. No new truth or notation issue found. Stage 1 is now clear for the assigned revised passages. Wording and flow remain separate, pending stages.

Record detail: hashes in the first block were collected at report creation. The coordinator's h(x) repair may have landed before that hash collection; the initial text observed in this call is recorded by the original S1-N1 quote, and the current text is bound by the recheck hash below. No initial pre-repair source hash is fabricated. The .before snapshot passages were directly reread during this recheck, confirming the unchanged adjacent equations against the prior version.
C:\dev\clsc\burak-papers\guide\content\chapters\05-place-fields.md CURRENT RECHECK SHA256 342268F4D10C4D5ACE00D23D10372638AC7BBE982CF574BB08B33764E921FCB9
Recheck completed: 2026-10-29T11:11:49.6401369+02:00. Measured wall elapsed since stage start: 167.52 seconds. Awake execution time unverified.
