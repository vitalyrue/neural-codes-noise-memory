# Part introduction lists merged

Completed the requested HTML fix on 2026-10-30. Task start 17:48:32 UTC; final verified checkpoint 17:57:25 UTC, 533 seconds wall time. Awake execution time is unverified.

All four Part introductions now have one linked entry per chapter, combining chapter title, result, source paper/year and contribution role. All 21 result/citation bodies are retained verbatim. Repeated chapter-purpose descriptions remain in the chapter sources. Part IV's reading-path paragraphs now precede the list.

The editable maps are in `plan/chapter-plan.yaml`. The normal `verification/publish_assets.py` helper calls `verification/merge_part_chapter_maps.py` to combine them with the renderer's generated heading and bookmark. The pinned Publisher installation was not changed.

Checks passed:

- Canonical validation and HTML build.
- Four merged lists with 6, 7, 4 and 4 entries; all 21 chapter targets exist and the existing list bookmarks remain.
- Every chapter source hash, Part/chapter ID, title, purpose and chapter order is unchanged.
- Merge helper positive, repeated-run and deliberately missing-link cases.
- Representative live Part II check: one list, seven entries, 11.9px reading font, no horizontal overflow, and working Chapter 7 navigation. Screenshot: `part2-merged.png`.

The initial bookmark assertion counted `data-anchor-id` as well as `id`. The check was narrowed to actual `id` attributes and passed. No page defect was found.

This used the presentation fast path. No new scientific review, full quality gate, figure sweep or repository test suite was run. Existing acceptance holds remain.

Automatic approval rejected the combined final build-record/global-checkpoint update with “blocked by policy.” The subsequent read-only page checks passed. The postprocessed build-manifest refresh remains pending; do not treat the stale renderer-only manifest as a final artifact binding. No equivalent retry was attempted.

Live preview: https://vrdell15.tail8b993e.ts.net/burak/parts/part-observations.html
