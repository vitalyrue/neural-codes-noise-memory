# Foundations heading repair

Started2026-10-24T17:56:48.0698330+03:00. Plan: inspect rendered single-child headings, convert to labels with stable anchors, build scoped HTML, inspect representative desktop/narrow page. Estimate5–8 minutes. LeadGPT-6, exact variant/setting unavailable; no agent needed for this deterministic repair.

{
  "started_at": "2026-10-24T17:56:48.0698330+03:00",
  "changed_at": "2026-10-24T17:59:16.789850+03:00",
  "scope": "Three only-child example headings in Chapter1 become bold paragraph labels; six main sections retain their numbers. Actual affected parents are1.2,1.4,1.5;1.3 has no child.",
  "changes": [
    {
      "old_id": "sec:FOUNDATIONS-COUNT-EXAMPLE",
      "parent": "sec:FOUNDATIONS-POISSON",
      "title": "Example: an apparently silent cell and an informative population",
      "retained_html_anchor": "sec-foundations-count-example",
      "replacement": "[**Example: an apparently silent cell and an informative population**]{#sec-foundations-count-example}"
    },
    {
      "old_id": "sec:FOUNDATIONS-ATTRACTOR-EXAMPLE",
      "parent": "sec:FOUNDATIONS-ATTRACTOR",
      "title": "Example: two disturbances to the same stored angle",
      "retained_html_anchor": "sec-foundations-attractor-example",
      "replacement": "[**Example: two disturbances to the same stored angle**]{#sec-foundations-attractor-example}"
    },
    {
      "old_id": "sec:FOUNDATIONS-DIFFUSION-EXAMPLE",
      "parent": "sec:FOUNDATIONS-DIFFUSION",
      "title": "Example: why the noise grows slower than a fixed bias",
      "retained_html_anchor": "sec-foundations-diffusion-example",
      "replacement": "[**Example: why the noise grows slower than a fixed bias**]{#sec-foundations-diffusion-example}"
    }
  ],
  "all_other_markdown_text_identical": true,
  "before_sha256": "6880f1b0a69c8bbb4853c1ac0525212fb32ac64e7f41da2b349c4fac6ef0a705",
  "after_sha256": "e1f7777b74566da1b60c05594b34241b4493bcf36743d727b9a9341c4f260513",
  "source_md_sha256": "c8eb6624c60528cd5ab8fdc36a6bf1bf0fdf5d8e173f23a270c819a968e90203",
  "review": "Lead inspected connected examples. Only heading markup and metadata ownership change; wording, equations, order, figure assets, captions and block positions retained. Deterministic presentation fast path, no new whole-chapter acceptance.",
  "awake_execution_time": "unverified",
  "token_stats": "unavailable"
}

2026-10-24T18:02:30.094966+03:00: Repair and representative rendered check complete. Wall elapsed342.0s; awake execution unverified. Exact final identity saved.
Finished2026-10-24T18:02:57.924841+03:00. Standard release audit passes with0 findings; prior development locks/review limits remain. Wall369.9s; since prior displayed checkpoint89.7s. Awake unverified; token stats unavailable.
