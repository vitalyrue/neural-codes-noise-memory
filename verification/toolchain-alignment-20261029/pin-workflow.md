# Pin workflow review

Started 2026-10-29T11:42:00.0415898+02:00. Report checkpoint 2026-10-29T11:43:54.6087433+02:00. Wall elapsed 114.6 seconds. Read-only source/configuration review, plus this report. Awake execution time unverified. Token stats unavailable.

## Findings

The guide's publisher lock says `development`; its teaching skill says `development`, and diagram says `optional`. These are placeholders, not the installed tool versions. Existing guide history explicitly preserves this distinction.

The clean Publisher 0.8.23 release index selects teaching 2.1.0-rc.38, quality 1.0.25, and diagram 1.6.1. Canonical CURRENT_STATE records release commit `825ab072f34e06df5d8da6f31552fa0206073045` and a later local diagram 1.6.2 package. Root agent separately verifies upstream latest and source identity.

All three current Codex installations passed real read-only release-wrapper checks during this task. Teaching and quality match the clean released manifests. Diagram 1.6.2 matches the local canonical manifest. Reinstallation is unnecessary for those same intended bytes.

## Exact check commands

From `C:/dev/NBIS/publisher-releases/0.8.23`:

```powershell
python tools/release_skill.py --publisher-root . --skill-name course-study-guide-builder --version 2.1.0-rc.38 --install-root C:/Users/vital/.codex/skills --check
python tools/release_skill.py --publisher-root . --skill-name course-quality-gate --version 1.0.25 --install-root C:/Users/vital/.codex/skills --check
```

From `C:/dev/NBIS/study-guide-publisher`:

```powershell
python tools/release_skill.py --publisher-root . --skill-name course-diagram-builder --version 1.6.2 --install-root C:/Users/vital/.codex/skills --check
```

All exited zero with `status: pass`, `mode: check`. No package installation or release generation was performed.

## Guide lock updates

Publisher 0.8.23 has no supported `pin` or `lock update` CLI command. CLI inspection confirms that its commands are init/build/validate/compile/state/version/quarto/audit/doctor/release-audit. `tools/release_skill.py` releases/installs reusable skills, and explicitly does not update book locks or certify books.

Guide locks are guide-owned configuration. The prohibition on hand-editing generated manifests/index records applies to reusable package release records. A controlled YAML update of guide locks from verified release metadata is appropriate; do not rewrite release manifests or the release index to make checks pass.

Do not use `skills/course-study-guide-builder/scripts/create_skill_lock.py` directly on this runtime guide. That legacy helper emits a singular `skill` object and `optional_skills`, while runtime doctor/release audit read `skills.course-study-guide-builder`. It also hashes the current tree rather than recording the independently verified intended release manifest. The established Module 1 lock is a useful shape example, not permission to copy its unrelated project/runtime fields.

Publisher lock should retain its existing renderer/content-model fields and update only publisher identity to verified version/source/tag/full commit/clean release status. Use `working_tree_dirty: false` only for the verified clean release export, never for the dirty canonical checkout.

Skill lock should retain project fields and populate the `skills` mapping with the verified selected versions and `release_manifest_sha256` values. SHA256 values measured here:

| Package | Version | Manifest SHA256 |
| --- | --- | --- |
| course-study-guide-builder | 2.1.0-rc.38 | a2be2493d765406636b1899f2630dc0288326350b15f122607b758610d9fa55a |
| course-quality-gate | 1.0.25 | eb1aab6e60dd6561ed1eb68cf934f89b91a25da04ff129001a8c9335378749b1 |
| course-diagram-builder (clean release) | 1.6.1 | 4a040e54ac3db57740de7e8b3d09d4ee8d2f6ecaab81e04207d2598558588988 |
| course-diagram-builder (local candidate) | 1.6.2 | 4fc9c464de9df88e3b754a59921985e8047f00177471e9efd9a11f0f207f9a15 |

The clean release and locally installed diagram versions differ. Preserve global 1.6.2. If selecting clean release 1.6.1 for this book, use its existing frozen bundle directly for book diagram checks, such as `run_quality_gate.py ... --diagram-skill-root C:/dev/NBIS/publisher-releases/0.8.23/skills/course-diagram-builder`. This is already the documented Module 1 approach. Do not imply installed 1.6.2 is a clean upstream release. Alternatively record local 1.6.2 as a local candidate explicitly, accepting that a fully clean released tool set has not been selected. Root must choose and disclose this distinction.

After authorized guide lock edits, run from the guide directory:

```powershell
publisher validate --project guide-project.yaml
publisher doctor --project guide-project.yaml --installed-skills-root C:/Users/vital/.codex/skills --output .build/doctor.json
```

For the required final handoff checkpoint, update Open work and run `publisher doctor --project guide-project.yaml --write-checkpoint`. Never add `--record-reviewed-chapter` for tool alignment. Do not update semantic review acceptance, visual acceptance or the structure lock merely to remove findings. Existing content review holds may remain after version alignment. Doctor primarily checks teaching skill identity; independent wrapper checks above provide quality/diagram file verification.

## Evidence read

- Canonical Publisher AGENTS.md, CURRENT_STATE.md and docs/SKILL_RELEASE_WORKFLOW.md.
- Clean release index, CLI, doctor/release audit implementation and legacy create_skill_lock.py.
- Guide CURRENT_STATE.md, guide-project.yaml and both placeholder locks.
- Module 1 prior alignment REPORT.md, COMMANDS.json and current lock shape.

No builds, whole-book reviews, full tests, lock mutations, package mutations or acceptance actions were performed.
