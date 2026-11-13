# Fundamental circuit dynamics now precede their consequences

The user requested that the equations defining neural dynamics belong in Chapter 1. The source change is complete and served at the existing private Tailscale address.

## Reader change

- Chapter 1 section 1.2 now teaches Burak and Fiete (2012), Eqs. 7–9: unit spike additions and activation decay; weighted input; input-to-rate conversion. The original Eq. 7 is displayed and linked to PDF page 5. Its count form and exponential solution remain beside the explanation.
- The existing spike/activation trace figure moved with this section. Its asset, dimensions, alternative text and visible status are unchanged. Its caption now names Eq. 7.
- Chapter 3 starts with the weak-noise approximation and retains the later stability, projection and diffusion calculations. It points back to Chapter 1 for the circuit model.
- The local tuning-curve baseline is now r_(i,0), keeping it distinct from input bias b_i. The delta glossary entry covers the time impulse as well as its probability use. The spike-time convention explicitly includes the current spike; the initial-state qualification is stated in ordinary language.
- Chapter openings, the Part I chapter map, source locations, relevant source-map links and old bookmarks were updated. No chapters were added or reordered.

## Review and checks

The independent reviewer completed three separate calls for correctness, necessity/terminology, and connected reading. Stage 2 found the unexplained phrase “initial transients”; the final wording explains the decaying contribution of initial activation. Recheck and Stage 3 report no remaining required repairs in the reviewed scope. Records: stage1.json, stage2.json, recheck.json and stage3.json.

The concept tool reports zero relation-order findings for the reviewed dependencies. Its coverage is deliberately partial and clear=false because other sections and chapters were not reviewed in this task. It is not whole-guide acceptance.

Native validation passed. move-checks.json confirms every prior stable ID remains, the only added ID is sec:MEMORY-WEAK-NOISE, chapter order/titles remain, and the figure asset/dimensions are unchanged. The structural lock was updated after the accepted move.

One HTML build completed successfully. The asset helper copied eight hash-checked source PDFs and installed the updated bookmark routes. html-checks.json confirms both live chapter responses match the built files, with the model, figure, blue-definition markup and highlight markup present. The old model and figure anchors route to Chapter 1.

Browser display inspection was attempted but unavailable: new tabs did not attach and the existing guide tab could not be accessed. No fresh screenshot, interactive bookmark check, or visual acceptance is claimed. Typography and print sources were not changed. No extended figure audit, whole-book semantic audit, numerical simulation rerun, PDF/DOCX build, Git action or public publication was performed. Earlier figure acceptance holds remain.

## Timing

Started 2026-11-01T11:36:24Z. This record was written at 2026-11-01T11:53:51.049078+00:00. Wall time at that checkpoint: 17.5 minutes. Awake execution time is unverified. Token stats unavailable.

Final doctor: Publisher and skill locks match; standard release audit passed with zero findings. The broader ledger still requires 24 chapter reviews; this scoped change does not clear that hold. Final completion: 2026-11-01T11:54:29.191076+00:00, wall 18.1 minutes.
