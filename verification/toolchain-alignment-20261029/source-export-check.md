# Clean source export check

Started 2026-10-29T11:45:03.0539804+02:00. File check ran 11:45:20.323783 to 11:45:21.003639. Final checkpoint 11:45:33.7527790+02:00, wall elapsed 30.7 seconds. Awake execution time unverified. Token stats unavailable.

All 456 tracked files in `C:/dev/NBIS/publisher-releases/0.8.23` match the exact Git blob IDs recorded by commit `825ab072f34e06df5d8da6f31552fa0206073045` in `C:/dev/NBIS/study-guide-publisher`. This includes runtime, reusable skills, release manifests, release index, schemas and templates. No files are missing. No differing line endings were accepted or normalized. Raw file bytes were hashed as Git blobs and compared directly.

The export has 43 additional Python bytecode cache files, listed separately in source-export-check.json. No extra source or configuration files were found. These caches were excluded naturally from the tracked-file comparison. The canonical Git checkout still has its pre-existing changes; this result applies to the fixed export alone. It supports recording the verified clean released source with `working_tree_dirty: false` when that export is the selected runtime. Upstream commit/tag identity is separately checked by the main agent.

Detailed per-file paths, SHA256 hashes, byte lengths and expected/actual Git blob IDs are in source-export-check.json. No source changes, installs, builds or tests were performed.

## Vale profile

A complete hidden-file search of the clean release found no `.vale.ini`. The package does not ship a default project Vale profile. `audit_vale_prose.py` searches the guide and its ancestors for `.vale.ini`; absent one it reports an error. `--advisory-only` deliberately runs its built-in warnings without claiming Vale ran. The quality skill and prose/style contract distinguish those warnings from a project's configured Vale rules.

Do not copy another course's profile without a decision or invent rules to satisfy a tool-alignment check. Reporting the guide's missing Vale configuration, or deliberately skipping Vale for tool alignment, is honest and supported. Adding a project Vale profile is separate configuration work requiring a choice of rules.
