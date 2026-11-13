# Concept index and prerequisite check

Use this when drafting or reviewing teaching order. The teaching rule is in `pedagogy-language-contract.md`; this page describes the Publisher tool. Run it from the Publisher repository. If the tool is not available in a deployed environment, report that limit and do the passage-based review directly. Do not treat a label, bold first use, glossary entry, keyword hit, or link as proof of adequate teaching.

`python tools/concept_prerequisites.py prepare --project <guide-project.yaml> --chapter ch:ID --output <index.json>` writes a passage packet. Repeat `--chapter` for the local reading path; omit it only for an authorized whole-book review. It reads the project, plan, Markdown, and sidecar blocks. It does not write to the guide. For a read-only guide, add `--read-only-project` and put the output outside that guide. It uses the quality companion's paragraph extractor, with section batches and exact paragraph or block locations, text and hashes. Code, tables, math, and unusual Markdown still need direct inspection; extraction is not semantic approval.

The packet starts with an unreviewed audience baseline, empty concept catalog, unreviewed sections, and no relations. A reviewer can create a small JSON judgments file for the concepts that matter. Do not keep a second full copy of every paragraph. Example shape:

```json
{
  "audience": {"status": "reviewed", "description": "Audience and assumed knowledge with evidence", "assumed_concepts": []},
  "concepts": [{"id": "classification-recall", "aliases": ["recall"]}],
  "sections": {"ch:EXAMPLE/s1": "reviewed"},
  "relations": [
    {"concept_id": "classification-recall", "passage_id": "ch:EXAMPLE/p20",
     "role": "teach", "adequacy": "adequate", "span": [0, 12],
     "status": "reviewed", "review": "actual reviewer call ID",
     "evidence": "Why this passage teaches enough for the later use"}
  ],
  "teaching_sets": []
}
```

Find passage IDs and zero-based character spans in the packet's `text`. Roles are `teach`, `use`, `preview`, and `reference`. A `teach` relation needs `adequacy: adequate|partial|insufficient`; a `use` relation needs `need: required|optional`. Teaching becomes available at the end of its span, not its start; a use that begins inside unfinished teaching does not pass. Use `status: candidate` while judgment is not independently reviewed, and `reviewed` only with actual review evidence. `review` identifies the call or person; the tool checks presence, not whether that review happened or was right. A teaching set can combine two or more `teach` passages with `concept_id`, `passage_ids`, `adequacy`, `status`, `review`, and `evidence`; the end of its last teaching span determines when the combined teaching is available. Keep aliases unambiguous. A reviewed audience assumption can satisfy a required use, but a subject-specific meaning still needs a passage when the audience baseline does not cover it.

Import and check without changing guide sources:

```powershell
python tools/concept_prerequisites.py prepare --project <guide-project.yaml> --chapter ch:ID --previous <packet.json> --judgments <judgments.json> --output <index.json>
python tools/concept_prerequisites.py check --index <index.json> --scope local --output <findings.json>
```

The checker recomputes current source, section, block, and plan evidence. It compares reviewed adequate teaching sites with required uses in chapter, line, then paragraph-span order. Previews and references do not satisfy a use. It reports the use and each candidate teaching site, including missing or later teaching. Candidate uses remain candidate findings. A missing teaching site in a partial index is unknown, not a confirmed omission. `--scope book` cannot clear when planned chapters or section judgments are missing. A local clear result means only that the indexed local scope has no unresolved relation-order finding; it does not approve unread chapters or the full teaching path.

For a read-only guide, also add `--read-only-project` to `check` if writing its optional findings file.
Exit code 0 means clear for the declared scope, 2 means findings or incomplete coverage, and 3 means malformed or stale input. None of these exit codes is a human acceptance decision.

For later edits, run `prepare` with `--previous <index.json>`. Matching passage and section hashes can retain judgments. Changed passages and sections lose reviewed coverage; plan, alias catalog, audience, or rule changes downgrade carried relations. Recheck affected prerequisites and transitions, including unchanged passages whose connection changed. The tool checks hashes and declarations, not meaning. Do not turn a concept finding into a fixed chapter swap: first decide which passage needs teaching, a reminder, a moved explanation, or a different presentation order, then review the boundaries. No manuscript change follows from a diagnostic run alone.
