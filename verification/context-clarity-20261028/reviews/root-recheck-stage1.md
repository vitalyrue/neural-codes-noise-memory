# Root changes: independent stage 1 truth/context recheck

Reviewer: /root/context_place. Local request ID: root-recheck-stage1-20261028. Started 2026-10-28T15:40:11.0371480+02:00. This reviewer did not write or apply these root changes. No edits were made in this recheck. Later wording and reader-flow calls remain separate.

Audience: undergraduate calculus, basic probability and linear algebra, with no neuroscience assumed. Scope: all 20 exact replacements in edits-root.json, including the current guide description, content/index.md, connected 00-reading-guide.md, two Part purposes in plan/chapter-plan.yaml, and all 14 chapter YAML purposes. The exact new text of every logged edit was checked against its current file and found present. The connected current reading guide was read in full. Purposes were compared with actual chapter teaching and chapter ranges; substantive source context was checked in the original local 2012 and 2022 paper extracts and the already inspected 2025 paper and supplement. This is a context recheck of the changes, not a new proof audit or empirical reproduction.

## Required repair R1

- File and location: content/chapters/03-memory-information.yaml, purpose, line 4.
- Exact current sentence: "This chapter measures the best accuracy available from those spikes and derives the constraint that this information places on the circuit’s memory stability."
- Problem: "measures the best accuracy available" describes an attainable optimum as though it were computed in general. The chapter instead derives a bound for regular, locally unbiased estimation and explicitly states that not every finite spike sample admits an estimator attaining it. This short purpose can be read independently in navigation, so the later qualification does not fully repair the promise made here.
- Strongest reasonable reading considered: "best accuracy" can informally refer to an information limit, and the linked chapter explains that meaning. That reading supports the intention, but "measures ... available" still removes the bound-versus-attainment distinction from the standalone excerpt. The repair should keep the summary at the same scope as the actual result.
- Proposed replacement sentence: "This chapter sets a bound on estimation error under the model’s assumptions and derives the constraint that spike information places on the circuit’s memory stability."
- Chapter evidence: 03-memory-information.md, MEMORY-FI, lines 60-76, derives Var(estimator) >= 1/(Jh), calls this a local bound for regular unbiased estimation, and explicitly denies guaranteed finite-sample attainment. MEMORY-BOUND, lines 78-113, then derives the information-diffusion lower bound. These are the two contributions the purpose should describe.
- Original source support: research/burak-fiete-2012-main.txt lines 295-308 explains error equal to or greater than inverse information and the resulting lower bound; lines 331-339 separately states the weak-fluctuation/informative-sample conditions used for ideal-estimator attainment. This is not a request to change the bound or its mathematical derivation.

## Remaining changes

No other required truth/context repair was found in the other 19 replacements. The landing/index and opening identify neuroscience, animal species and the different kinds of evidence without presenting the three studies as one experiment. The reading guide retains the two-macaque, single-cell paired-recording, 350 ms, horizontal-motion, fitted-gain and common-noise qualifications in the connected text. The 2012 contribution remains a model and mathematical constraint. Both Part introductions give chapter ranges matching the current plan. The remaining chapter purposes agree with the chapters’ subjects and do not turn the proposed memory-circuit mechanism or random-input account into direct anatomical measurements. The place-size purpose retains the high-threshold qualification. The synthesis purpose preserves the distinction between supported links and untested circuit connections.

The unchanged broad statement about holding an eye angle is read as the behavioral goal, not as a claim of exactly zero eye movement, since the following eye section explicitly introduces drift. No extra correction is needed for that phrase. Wording economy and the repeated landing instruction in content/index.md are deferred to the separately requested wording stage.

Original source context consulted: burak-fiete-2012-main.txt, especially the abstract, Information-Diffusion Inequality, and saturation discussion; ben-shushan-2022-main-text.txt, especially lines 118-132, 148-193, 254, 315-325, 335-368 and 428-485; mainali-2025-full-text-layout.txt and place-supplement.txt as recorded below. The eye source supports the paired OMN recordings, inferred common contribution and proposed diffusing integrator followed by muscle filtering and delayed visual feedback. The place source supports existing rodent/bat recordings, spatial-size laws and a possible summed-input interpretation.

One required repair remains before this stage can pass the changed set. No manuscript, YAML, index, plan or publication changes were made by this reviewer. Awake execution time was not independently established from Windows sleep/resume events. Token statistics are unavailable.

## Current file and rule SHA256 hashes- C:\dev\clsc\burak-papers\guide\content\chapters\00-reading-guide.md: BAF2D942885C7B61B94626E3585FF034695AEC56E42B9F25395DBDEDDEA7558F
- C:\dev\clsc\burak-papers\guide\content\chapters\00-reading-guide.yaml: 2BB7B78863519586C00559B9788BEF5DCB5ABAA9429CF08B31ACB4775EC0B00B
- C:\dev\clsc\burak-papers\guide\content\chapters\01-foundations.yaml: CD114481B60CBE395A5FEC5FA712389D6F21558596C444C2980564F608EE3DB7
- C:\dev\clsc\burak-papers\guide\content\chapters\01b-persistence.yaml: DF5138C8652286D947D32AE264913E933487B541CDC37E85163CBFDF0EFD2B3F
- C:\dev\clsc\burak-papers\guide\content\chapters\02-memory-dynamics.yaml: 6EBA69913DA5AE03A855B3A01E145625834546706B043724A1D1A4CBED3DC5D8
- C:\dev\clsc\burak-papers\guide\content\chapters\02b-memory-long-delays.yaml: 74C754C51B537127522AF75C938AB1A0641BBBD7D6AE3172F54F56370BE58EC8
- C:\dev\clsc\burak-papers\guide\content\chapters\03-memory-information.yaml: 4D05E45BCBC738BFA12077D01D4996E0AA1EED1A631176AC96EA75B8DC17DCB4
- C:\dev\clsc\burak-papers\guide\content\chapters\03b-memory-readout.yaml: 398AFFD102EA7D8FAD6AC4D3978E0CC6050766D2AA407AD43D9F9350AB20FBE8
- C:\dev\clsc\burak-papers\guide\content\chapters\04-eye-drift.yaml: DDA712870A7119D548377C229C5019C63CDF71B574A739FBD8C47E5C42B55A3B
- C:\dev\clsc\burak-papers\guide\content\chapters\04b-eye-timing.yaml: 22F36F586432480746EFDB9C24341C13F32334E27273A3F645B780175FAC8C36
- C:\dev\clsc\burak-papers\guide\content\chapters\04c-eye-circuit.yaml: C7989CC4C794582D67E3BA8760C4E2B3CC47B85FD7E667876C44DD8FD10BFFBA
- C:\dev\clsc\burak-papers\guide\content\chapters\05-place-fields.yaml: 19EC82B79B842D2C178AD15137FCD917FA716787B83D745AAD8150D3D4660F96
- C:\dev\clsc\burak-papers\guide\content\chapters\05b-place-sizes.yaml: CCC808D83C6E70AB1FCADEFE964C3AB285987EE1D0E7807C842BFFD1948524F5
- C:\dev\clsc\burak-papers\guide\content\chapters\05c-place-tests.yaml: B7806F53797ABE3F06E528822B4FD86F67AC80C2FE6A63EB953CE2D626F4E2F2
- C:\dev\clsc\burak-papers\guide\content\chapters\06-synthesis.yaml: 60B396173D94B5B4E2A078A71B2C7FF64EE651F2DCE0D736CC343F54EB8DF9A2
- C:\dev\clsc\burak-papers\guide\content\index.md: 9AF6FFF28D91BDAB808F48AE4F333142F60DB48B5026A5046C2220DD75917670
- C:\dev\clsc\burak-papers\guide\guide-project.yaml: 45F330CEC771D6223E8EC81341DEA1781E4D4C32D27A1A82B0F616E813313907
- C:\dev\clsc\burak-papers\guide\plan\chapter-plan.yaml: 394E5BFDCCA536683BACFEF577C10434B25361DDFD31F5588248FAB976BBF8E6
- C:\dev\clsc\burak-papers\guide\verification\context-clarity-20261028\edits-root.json: CF654C0E098A1DE0D069BB77EF1ADE2F362A72FAB031113DB0F30EA0833651F4
- C:\dev\clsc\burak-papers\research\burak-fiete-2012-main.txt: 10A33FFFF51519638BAE8F54B97994E1235646BE284189E86A33E077EE291354
- C:\dev\clsc\burak-papers\research\ben-shushan-2022-main-text.txt: B52B017AD8D63AF12D7301407E3CACE4C0725B1F906AB3543B8A8014666C8EB5
- C:\dev\clsc\burak-papers\research\mainali-2025-full-text-layout.txt: C5EA5963F2243B1B1E8FD409069973861492E9D2D83F0A574111724E4049AC86
- C:\dev\clsc\burak-papers\guide\verification\writers\place-supplement.txt: FC8484E4094AD26BD34089322120B1E44619B2AD3541A6034D1272F7711887C4
- C:\Users\vital\.codex\skills\course-study-guide-builder\SKILL.md: B78068E9874E6D1D97B2017BF8F940492F9B08FC11B74F20FD75019FF388984A
- C:\Users\vital\.codex\skills\course-study-guide-builder\references\pedagogy-language-contract.md: F4C1EB544CF640B708E1970D9572FDC758FCC6AEA806675D01A0256658DF847A
- C:\dev\clsc\burak-papers\guide\content\chapters\01-foundations.md: 5CDF42D7EF8AA1E11A21E1CEEF450382170BCAED9ACF052F20D7BB82D82EF63E
- C:\dev\clsc\burak-papers\guide\content\chapters\01b-persistence.md: 299F9015CAC9EF69CC5581E7D71F088BC5704A10589C16C2F2C6A5D97B461BCB
- C:\dev\clsc\burak-papers\guide\content\chapters\02-memory-dynamics.md: F21241A321A3F30F1895E0B7E1FC52E119BCC14A18887811EDE4328E7004132E
- C:\dev\clsc\burak-papers\guide\content\chapters\02b-memory-long-delays.md: 8586645D980D1392B638B210B04DDBCD377F8C9AC9E90711398629B45EF5C563
- C:\dev\clsc\burak-papers\guide\content\chapters\03-memory-information.md: 0493CE19F0101B56B8299939FFB23F7ED2E13568A048742CBFF2BA2CA2A736C1
- C:\dev\clsc\burak-papers\guide\content\chapters\03b-memory-readout.md: 40838058F6EADE08EAE8425E0BC055531A46955DD0B489C634B2575F83E75452
- C:\dev\clsc\burak-papers\guide\content\chapters\04-eye-drift.md: A33A3A7FC25B234AE32B961F2404CAE223C6120C7CD8AA04E3EB85394388777B
- C:\dev\clsc\burak-papers\guide\content\chapters\04b-eye-timing.md: BDFBEC009BE758D492904F440D03CD1E9517586BBBCDA7A07C69A54845ABAB7F
- C:\dev\clsc\burak-papers\guide\content\chapters\04c-eye-circuit.md: 75AE2098D255171990F67776A65676F7948D4E75B6D0D1F2AC044A208622874B
- C:\dev\clsc\burak-papers\guide\content\chapters\05-place-fields.md: 5241516BAA09B0B96E5969AD688D0D8D486EC682601AA3FBC49D6F8F0A74C1FB
- C:\dev\clsc\burak-papers\guide\content\chapters\05b-place-sizes.md: 22CFCF168C65E15570F97E530918178DF51FA3ED1EC9BB1DFF91E7DB6EBC3B03
- C:\dev\clsc\burak-papers\guide\content\chapters\05c-place-tests.md: F8B0FCE794965F1B99FA90FC183BECC131B8DD46F25E6876A369C2BF5C431B23
- C:\dev\clsc\burak-papers\guide\content\chapters\06-synthesis.md: D5DB21F66CB38EA9808E21AE37E89E26F04E7427931192E8108519E3CA58192C
Finished 2026-10-28T15:42:22.0896467+02:00. All 20 logged new passages present. Scope remains review only.
