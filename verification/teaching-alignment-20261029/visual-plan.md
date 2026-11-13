# Visual review plan and fresh sample findings

Started: 2026-10-29T10:26:45Z (12:26:45 Asia/Jerusalem).
Independent reviewer: /root/alignment_visual_plan. I did not create these figures.
Scope: read-only artwork, manuscript and visual ledger. Only this report folder was written.

## What the current checks establish

The ledger has 52 selected figures: 22 original guide figures and 30 exact paper excerpts. Every asset matches its ledger hash. All 21 existing criterion-level records still match the exact image bytes; their rule, style, generator and QA inputs also match. Their chapter inputs changed. Twenty additionally have changed ledger context. The remaining original attractor and all 30 paper excerpts lack the current review contract and criterion record.

The pinned 1.6.1 auditor reports 31 missing-record findings, 47 changed-input findings and 20 changed-context findings. These are 98 findings about 52 figures, not 98 defective pictures. No content defect is implied by a stale hash. See visual-audit.json and visual-current-inventory.json for exact per-figure findings and changed paths. Source PDF hashes match all 30 excerpt entries.

The source references in some original contracts still point to their former chapters, for example memory readout to 03-memory-information and place sizes to 05-place-fields. Rebuild each connected-source list from actual current placement before review; do not simply rehash old chapter lists. Compiled chapter source hashes must then be obtained from the final BookModel after prose work stops.

## Three fresh views, before consulting prior findings

The first image call inspected a rendering of the actual attractor SVG, the current synthesis PNG and current paper Figure 1 PNG. Additional views inspected the same attractor in Edge, synthesis at 700 px and paper Figure 1 at 624 px. This is a sample review only. The original high-resolution synthesis view was downsampled slightly by the tool; its intended-width view was exact. No all-52 pixel review was done.

### Original attractor: fig:FOUNDATIONS-ATTRACTOR

Current source: 01b-persistence.md, section FOUNDATIONS-ATTRACTOR and its YAML figure block. The equations give r1+r2=80 Hz, theta=(r1-r2)/4 degrees, and equal-rate disturbances that decay. The points (50,30), (53,33), (53,27) and the angles 5 and 6.5 degrees in the actual figure agree. The orange arrow correctly returns toward (50,30); the teal arrow moves to a different fixed point. The caption distinguishes a deterministic response from an imposed disturbance. Technical meaning passes this bounded source check.

The visual explanation works: activity space separates a change off the fixed line from a change along it. However, the diagonal visibly runs through the orange common-change label in the actual browser rendering. The short teal dashed arrow lies over the dark fixed-point line, making its dashed character hard to see. The book text relies on the dashed/solid distinction. This is a real readability finding, not merely missing paperwork. It does not reverse the mathematics, but I would not issue an unqualified readability pass.

The browser screenshot is about 691 px wide; the YAML declares 6.4 inches (614.4 CSS pixels at 96 px/in). Exact current in-book width still needs checking. The MuPDF rendering changed font/grid appearance; use attractor-browser.png as the more relevant evidence. Suggested small repair if artwork edits are separately authorized: move the orange text off the diagonal, and make the imposed-disturbance identity legible without depending on dashes hidden over the line. Preserve points, directions and the exact example. No artwork was edited here.

Strongest objection: the picture could make every disturbance look like a deterministic drift. Current prose and caption correctly distinguish them, but the arrow styling needs clearer support.

Palette: navy/teal with explicitly locked historical orange exceptions. No fresh vector QA was produced, so formal palette acceptance remains pending. Coverage: internal quantitative illustration; opening-map coverage does not apply.

### Recent guide plot: fig:SYNTHESIS-SHARED-POSITION

Current source: 06-synthesis.md, joint calculation and covariance example, plus its YAML caption/alt. The actual upper curves have slopes +2 and -1 Hz/m and cross at 10 Hz. At +0.1 m, the marked rates are 10.2 and 9.9 Hz. The lower marked point is (+0.2,-0.1) Hz, on a line with slope -1/2. Independently recalculating with displacement variance 0.01 m2 gives rate variances 0.04 and 0.01 Hz2, covariance -0.02 Hz2 and correlation -1 when this is the sole source. Technical meaning passes the bounded check.

Both scenes explain a relationship beyond labels: the fixed tuning curves give opposite responses to one displacement, and the lower graph shows their one-dimensional joint change. Labels, units and the local-example qualifications match the current text. The 700 px preview is legible and uncut. Navy and teal distinguish the rates; gray guides distinguish reference coordinates. The current source explicitly says these are expected-rate changes, locally linearized, without other private/shared fluctuations, and that negative covariance is not evidence of inhibition. Those qualifications resolve the strongest objection.

This is a good candidate for carrying forward the unchanged-image technical, visual-explanation and readability evidence after a real context review. It is not accepted for release here: current counterpart review and final compiled source bindings remain outside this sample.

### Exact source crop: fig:PAPER-PLACE-1

Current source: 05-place-fields.md, PLACE-GP, its YAML figure block, and original PDF page 4. The original PDF caption was read after the first image inspection. The actual crop contains panels A-F: thresholded traces and data, a random weighted-input architecture, length/gap distributions, log-length moments and mouse comparisons. The guide caption and alt describe those visible panels without redrawing or changing them. The source caption distinguishes data/model colors, simulations from high-threshold formulas, and architecture from uniquely established circuitry. No crop clipping was seen in this sample.

The 624 px insertion preview makes several source labels, inset text and the architecture formula very small. The full-size image is much easier to read. An explicit full-size image link and source-PDF link are present. Readability therefore remains conditional on checking that enlargement actually works in the current book, and on not treating the 624 px view as a complete readable rendering of every panel. This is a display concern, not a reason to recolor the source figure.

The surrounding passage explains the threshold model before the crop. The ledger's teaching_introduction is only the fragment 'Here z has variance one'; record the actual surrounding paragraph in a new contract instead of treating this fragment as adequate evidence by itself. The source crop includes results developed later in the guide; its optional source-figure fold makes that reasonable, but its caption should not be counted as teaching every later result here.

## Prior evidence that can be reused, with limits

Historical records were consulted only after the three initial image views.

- Original guide figures: 21 independent criterion records preserve exact image hashes and unchanged generators, styles and QA. Reuse their prior unchanged-image observations and claim rows, then independently read changed introductions, captions, alt, interpretation, placement, connected chapter passages and counterpart descriptions. Record what changed and why each old finding remains true. A changed chapter hash does not require redrawing every image or recomputing unchanged math. If the changed passage alters meaning or reveals a contradiction, reopen the affected claim and actual image. Keep the original historical records.
- Synthesis has a substantive historical independent stage1-A09.json with a numerical calculation, per-scene evidence and claim rows. Its explicit original limit was candidate suitability, with final source checks later. Do not cite that stage alone as current release approval.
- Attractor's figure-final.json inspected the same SVG but only a supplied full-size rendering in its old chapter. It did not approve all sizes, does not use the current criterion format, and the fresh readability concern means it needs a full new criterion review after any authorized correction.
- Paper crops: all 30 preparer records report source/crop viewing. The saved independent memory review covers five crops. The independent eye sample covers three crops: main Figure 5 and Extended Data 7 and 8. The remaining twelve eye crops were only independently checked as metadata, not viewed. The saved resolution says root sampled place Figures 1 and S2. That does not establish complete independent review of all ten place crops.
- The memory Figure 2 alt objection was explicitly declined after checking the source caption, which mentions rate traces and spikes. Preserve both the objection and resolution; do not silently repeat the rejected edit.

These existing records reduce repeat work, but preparer inspection is not independent approval. For the source crops, plan fresh independent full source/crop checks for the twelve eye crops outside the sample and the place crops without established independent review. First establish reviewer identity and exact-byte matches for the historical independent records. This turn independently viewed place Figure 1, but has not completed its book-width enlargement/claim review. There is no defensible automatic all-30 acceptance yet.

## Exact source excerpts do not fit the pinned generated-art contract

The user's exact cut-and-paste instruction rules out recoloring or redrawing these images to satisfy a house palette. Classify them as exact source figure excerpts, with source PDF/page/crop rectangle, source hash, image hash, original authors and crop preparer as separate fields. Their teaching role may be quantitative-figure, but their production route is source-excerpt, not vector-generation.

Pinned visual_review.py only accepts routes raster or vector. It requires every palette verdict to pass. The raster route requires a generated-image palette audit satisfying the selected profile; the vector route requires spec/profile/build QA. No source-excerpt route, palette not-applicable branch, or author override for original-source colors exists. The documented author override concerns map coverage, not paper-figure color preservation. Thus the 30 crops cannot honestly meet the existing generated-art palette contract by filling out missing fields.

Do not fake a vector specification for a PDF crop, mark them unselected, remove them from the actual figure inventory, loosen the palette limit after inspection, or claim full original color fidelity from house-palette membership. A proper source-excerpt acceptance branch should validate exact source fidelity/crop completeness and preserved color semantics in place of generated-art palette membership. Accuracy, visual explanation, readable display/enlargement, caption/alt/placement and independent review remain required. This needs a deliberate contract/runtime change and version handling; until then report the capability gap and retain staging-only status.

## Smallest practical completion plan

1. Finish current prose changes and freeze the actual chapter/figure context. Save hashes and a current inventory once. Estimate: 5-10 minutes of focused setup after prose finishes.
2. For the 21 original figures with genuine unchanged-image evidence, run bounded independent context reviews grouped by current chapter. Reuse old claim rows only after checking their continuing truth. Reopen pixels for changed meaning, changed placement/width or a known concern. Estimate: 20-35 minutes across the guide, depending on text changes.
3. Treat the attractor as a separate small correction/review decision. Estimate: 5-10 minutes for a focused repair and independent check if authorized.
4. Agree on the source-excerpt acceptance capability before creating formal records for all 30. Reuse verified independent crop evidence where present; freshly inspect remaining source/crop pairs and final readable views. Estimate: 25-45 minutes of visual work, plus whatever contract implementation is needed. This longer viewing pass should be scoped with the user first.
5. Only after real judgments exist, bind them to the final exact inputs and compiled chapter hashes. Run the directly relevant acceptance audit and sample the current reader controls for enlargement/scrolling. No full-document pixel sweep or unrelated semantic audit is implied.

The practical choice is bounded reuse plus targeted fresh checks, rather than asking the user to authorize an unneeded complete rereview of 52 unchanged images. This plan cannot promise authoritative acceptance before the source-excerpt gap is resolved.

## Timing correction and limits

Actual persisted start was 10:26:45Z. The inventory checkpoint was 10:28:43.545213Z, wall elapsed 1 minute 58.5 seconds. Earlier messages estimated 12:30 and 12:34 local; those were my incorrect estimates and must not be used as wall-clock evidence. No system clock change was established. Awake execution time is unverified; Windows sleep/resume events were not queried. Completion timestamp is recorded in visual-plan-completion.json.

No manuscript, ledger, image or old review was changed. These are fresh findings and a review plan, not 52 figure approvals. Token stats unavailable.

## Final scope decision

User chose: Finish text first; leave figure acceptance pending. The completion plan above is future work only. No extended pixel review, artwork repair, source-excerpt contract implementation or acceptance update is authorized by this report. Work stopped after the bounded three-figure assessment.

