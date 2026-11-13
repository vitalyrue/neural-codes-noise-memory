# Stage 2 focused repair recheck

**PASS.** All three required wording repairs are resolved. Separate stage2 call; no reader-flow review is claimed.

Reviewer `/root/math_table_review`, requested GPT-6.1 Sol high. Exact serving build/backend request ID unavailable. Host start 2026-11-04T18:20:37.693798+02:00, finish 2026-11-04T18:21:46.779729+02:00; wall elapsed 0:01:09.085931. Awake time unverified. Since prior truth-recheck checkpoint: 0:01:34.880315. No observed clock change.

Read the three changed derivation cells and adjacent formulas/decoding cells. Each passes the deletion and meaning checks:

- **Row1:** 'Each spike increases ... by one' now assigns the change to the event; 'the count process N_i records these events' defines the count's role. The separate decay sentence names activation as its subject. Both statements earn their space because the formula distinguishes an event count from a decaying state. No opaque actor or unnecessary repeat was introduced.
- **Row26:** 'Mean positive part of the spatial slope' names the correct expectation without the conditional-positive-mean ambiguity. The next sentence explains height-slope independence. This addition is necessary mathematical precision, not extra specialist vocabulary.
- **Row27:** Writing mu_s/(mu_s+mu_g) states the required fraction directly. It removes an ambiguous pronoun while retaining the active/inactive-mean derivation. Repeating that short ratio is useful because the cell states the step used in the adjacent inverse formula.

## Exact reuse of unchanged judgments

All unchanged judgments in the complete35-row `stage2-wording.md` are adopted, including the section intro, top reference link and beta paragraph. Verified by reversing only the three recorded replacements in memory and serializing with the file's existing YAML settings and Windows CRLF line endings: the resulting SHA256 is `66D302B80CC1607268807F6ED03CAA1C23A807BD0CEA093629746B61B83FE844`, exactly the source hash reviewed in stage2. Thus the remaining102 table cells and all other YAML content are unchanged. The Markdown hash also exactly matches the prior stage2 version, confirming the same surrounding context. This check supports reuse; the actual wording judgments above decide the changed cells.

No reader-source edits, build or visual review performed. The three repairs already passed their separate truth check. No required stage2 issue remains. Stage3 reader understanding/flow is still pending. Token stats unavailable.

## Current hashes

- `content\chapters\00-mathematical-tools.md`: SHA256 `BECA4E530159D77B49C58495FC126530C6671AF8994E4310EF1F95BF9BC0DA02`
- `content\chapters\00-mathematical-tools.yaml`: SHA256 `ADE8100D6E7F9271C0BBD3DDBD9A708BDF252B60AACE126D9FF708BF00F48BF6`

Teaching-rule hashes remain those recorded in stage2-wording.md; no rule file changed.
