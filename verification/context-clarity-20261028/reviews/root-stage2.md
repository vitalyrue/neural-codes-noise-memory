# Root changes: stage 1 closure, then independent stage 2

Reviewer: /root/context_place. Local request ID: root-stage2-20261028. Started 2026-10-28T15:43:58.3987354+02:00. No manuscript, YAML, index or plan edits were made. Stage 3 reader-flow review has not been requested or performed.

## Stage 1 closure, narrow call completed first

Read review-fixes.json and the current purpose in content/chapters/03-memory-information.yaml. The R1 replacement is present exactly:

"This chapter sets a bound on estimation error under the model’s assumptions and derives the constraint that spike information places on the circuit’s memory stability."

Verdict: R1 is closed. The new sentence identifies a bound under assumptions rather than promising that a finite spike sample attains an exact optimum. It matches the regular-unbiased estimation bound in 03-memory-information.md lines 60-76 and its subsequent information-diffusion constraint. No further truth/context correction arises from this narrow repair. The other 19 root edits retain the prior Stage 1 verdict; this is not a new whole-book truth audit.

## Stage 2 wording and necessity, separate call

Scope: root changes only, read as standalone excerpts and beside their connected text. Read the current guide description, content/index.md, 00-reading-guide.md opening and connected section, two Part purposes in plan/chapter-plan.yaml, and all 14 chapter YAML purposes. Also read metadata-sync.json so that duplicated reader-visible summary text can be kept consistent if a proposed correction is accepted. Four sidecars were serialized with different line wrapping during this interval; their current purposes were reread and their wording is unchanged apart from the already reviewed R1.

Audience: undergraduate mathematics and no assumed neuroscience. Exact terms that have an explained meaning in the reading path are retained; an excerpt is not required to repeat the complete biological tutorial. Purpose text legitimately says what its chapter teaches, since its job is navigation. This does not justify the same wording as an added explanatory paragraph inside every chapter.

### Required wording repair W1: repeated reading-path instruction in the source index

- File: content/index.md, first paragraph, final sentence.
- Exact sentence proposed for deletion: "Begin with the reading path for the setting, contribution, and limits of each study, followed by the background and step-by-step calculations."
- Connected text: the next paragraph immediately begins "Begin with the reading path for paper copies, assumed knowledge, and the route through the mathematics."
- Deletion test: Removing the first instruction leaves the full science/recording setup and the following navigation instruction. The reader still knows where to begin, where the paper copies and assumptions are, and how the guide proceeds through the mathematics. The repeated invitation adds no necessary premise, condition or explanation. Keep the existing following paragraph.
- Scope: Delete this sentence in content/index.md only. The same sentence in guide-project.yaml has a useful standalone navigation role and should stay, because that description does not contain the following index paragraph.

### Required wording repair W2: repeated three-question summary in the reading-guide opening

- File: content/chapters/00-reading-guide.md, READING-FIELD, final sentence of its first paragraph. Matching section summary in 00-reading-guide.yaml contains the same sentence.
- Exact sentence proposed for deletion: "The three papers use these methods to study different parts of the problem: maintaining a value, locating the source of an irregular movement, and explaining the spatial patterns through which cells represent position."
- Connected earlier wording: the new opening already states "They ask how activity can retain a value, how an internal fluctuation can move the eyes, and why a cell can respond at several separate locations."
- Deletion test: Removing the later sentence keeps every contribution of READING-FIELD: concrete tasks, the neuron definition, brief variable signals, the scientific field, and the model-versus-recording method distinction. It also keeps the three study questions in the opening. The removed sentence restates those questions without assigning an additional method or condition to any particular paper.
- Proposed repair: Delete the exact sentence in the Markdown and matching READING-FIELD section summary. Preserve the immediately preceding sentence about models connecting assumptions to predictions and recordings testing them. Do not remove the biological task examples merely because they concern the same three studies; those examples connect each task to variable cellular signals.

### Remaining wording decisions

No additional required wording repair was found. The guide description establishes the setting and kind of evidence; Part purposes identify each chapter group's learning job and sequence. Repeating a topic across a standalone purpose and its chapter is useful navigation, unlike the immediate restatements identified above.

The 14 purposes are retained for these contributions: reading-guide purpose gives settings and scope; foundations gives spikes and group rate patterns; persistence separates activity from represented value; memory-dynamics follows recurrent spike effects; long-delays identifies boundaries and drift; information now states a bound; readout identifies observation time and unrecoverable prior changes; eye-drift states the paired-measurement inference; eye-timing distinguishes accumulating changes from fluctuations around a fixed command; eye-circuit labels a possible mechanism; place-fields identifies location-sensitive cells and a threshold mechanism; place-sizes identifies movement geometry and the limiting approximation; place-tests links measured regions to model checks and circuit limits; synthesis separates established links from further questions. Their technical words are needed for those jobs and are supported by the connected chapters. No synonym replacements or repeated full definitions are required.

Stage 2 status: two required deletions remain for coordinator decision and application. Stage 1 closure applies only to R1; these deletions have not been applied or rechecked. No Stage 3 judgment is claimed.

Wall-clock timing is recorded below. Awake execution time was not established from Windows sleep/resume logs. Token statistics are unavailable.

## Current SHA256 snapshot- C:\dev\clsc\burak-papers\guide\guide-project.yaml: 45F330CEC771D6223E8EC81341DEA1781E4D4C32D27A1A82B0F616E813313907
- C:\dev\clsc\burak-papers\guide\content\index.md: 9AF6FFF28D91BDAB808F48AE4F333142F60DB48B5026A5046C2220DD75917670
- C:\dev\clsc\burak-papers\guide\plan\chapter-plan.yaml: 394E5BFDCCA536683BACFEF577C10434B25361DDFD31F5588248FAB976BBF8E6
- C:\dev\clsc\burak-papers\guide\content\chapters\00-reading-guide.md: BAF2D942885C7B61B94626E3585FF034695AEC56E42B9F25395DBDEDDEA7558F
- C:\dev\clsc\burak-papers\guide\content\chapters\03-memory-information.md: 0493CE19F0101B56B8299939FFB23F7ED2E13568A048742CBFF2BA2CA2A736C1
- C:\dev\clsc\burak-papers\guide\verification\context-clarity-20261028\edits-root.json: CF654C0E098A1DE0D069BB77EF1ADE2F362A72FAB031113DB0F30EA0833651F4
- C:\dev\clsc\burak-papers\guide\verification\context-clarity-20261028\review-fixes.json: FB92199B1ADD0A568E1E435C00F28D35A38893F8683FF3490E86B9DE0E68D3A3
- C:\dev\clsc\burak-papers\guide\verification\context-clarity-20261028\metadata-sync.json: 484BDC49417534C7F715A10A4C8A8E924F30C0BFBD3675237C5F0B5F784202C5
- C:\dev\clsc\burak-papers\guide\content\chapters\00-reading-guide.yaml: 5A77C64478D9D70FC763BF27C5B1F95308711B29BE94E763D42482AA41363D53
- C:\dev\clsc\burak-papers\guide\content\chapters\01-foundations.yaml: CD114481B60CBE395A5FEC5FA712389D6F21558596C444C2980564F608EE3DB7
- C:\dev\clsc\burak-papers\guide\content\chapters\01b-persistence.yaml: DF5138C8652286D947D32AE264913E933487B541CDC37E85163CBFDF0EFD2B3F
- C:\dev\clsc\burak-papers\guide\content\chapters\02-memory-dynamics.yaml: 6EBA69913DA5AE03A855B3A01E145625834546706B043724A1D1A4CBED3DC5D8
- C:\dev\clsc\burak-papers\guide\content\chapters\02b-memory-long-delays.yaml: 74C754C51B537127522AF75C938AB1A0641BBBD7D6AE3172F54F56370BE58EC8
- C:\dev\clsc\burak-papers\guide\content\chapters\03-memory-information.yaml: 02B8E3B9090CF044FC4ADAE189EE2750263D88486B195386152900D7E87D2FB6
- C:\dev\clsc\burak-papers\guide\content\chapters\03b-memory-readout.yaml: 74DFEAE4F066DB6F1990750109DEABAF6B61797D9AD8BA8CCE82112FB6EDEDBF
- C:\dev\clsc\burak-papers\guide\content\chapters\04-eye-drift.yaml: C6ADCF74E8B88789986AD18EEF462710C077B6CDFF146B5FA70070BED0B6F088
- C:\dev\clsc\burak-papers\guide\content\chapters\04b-eye-timing.yaml: 22F36F586432480746EFDB9C24341C13F32334E27273A3F645B780175FAC8C36
- C:\dev\clsc\burak-papers\guide\content\chapters\04c-eye-circuit.yaml: 88E31F914A95315EFA80C88CC9EA088ED23A2B084A0B433AB0542B400EB9A1BC
- C:\dev\clsc\burak-papers\guide\content\chapters\05-place-fields.yaml: 19EC82B79B842D2C178AD15137FCD917FA716787B83D745AAD8150D3D4660F96
- C:\dev\clsc\burak-papers\guide\content\chapters\05b-place-sizes.yaml: CCC808D83C6E70AB1FCADEFE964C3AB285987EE1D0E7807C842BFFD1948524F5
- C:\dev\clsc\burak-papers\guide\content\chapters\05c-place-tests.yaml: B7806F53797ABE3F06E528822B4FD86F67AC80C2FE6A63EB953CE2D626F4E2F2
- C:\dev\clsc\burak-papers\guide\content\chapters\06-synthesis.yaml: 60B396173D94B5B4E2A078A71B2C7FF64EE651F2DCE0D736CC343F54EB8DF9A2
- C:\Users\vital\.codex\skills\course-study-guide-builder\SKILL.md: B78068E9874E6D1D97B2017BF8F940492F9B08FC11B74F20FD75019FF388984A
- C:\Users\vital\.codex\skills\course-study-guide-builder\references\pedagogy-language-contract.md: F4C1EB544CF640B708E1970D9572FDC758FCC6AEA806675D01A0256658DF847A
Finished 2026-10-28T15:46:03.7811139+02:00. Review only; two Stage 2 findings remain.
