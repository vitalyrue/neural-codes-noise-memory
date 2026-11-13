# Stage2: common notation wording and necessity

- Separate request cross-paper-notation-stage2-20261105; reviewer /root/exam_review_check; inherited Sol high; exact backend unavailable.
- Actual host start 2026-11-05T13:03:42.638163+02:00; finish 2026-11-05T13:04:25.606242+02:00; wall elapsed 43.0s. Awake execution unavailable because sleep/resume logs were not collected.
- Scope: new common quantities, changing-letter list, shortened paper-key wording and tools route. No flow/source/math audit or edits.

## Verdict

PASS. No required wording repair or optional polishing recommended. The new key now answers the cross-article request: it groups quantities by meaning and units, then separately lists letters whose meaning changes. It does not rely on a repeated letter to imply the same physical quantity.

## Passage-based decisions

- Common-key introduction: same quantity can have different letters is the reason for this key; local paper details remain explicitly separate. Retain.
- Firing-rate bullet: names all three rate aliases and uses familiar expected spikes per time with Hz/spikes/s units. This supplies one common definition instead of three repeated definitions. Retain.
- Coordinate bullet: labels represented value, actual angle and physical position separately, gives angle/distance/model units and states each keeps its own model meaning. Repetition here is a necessary guard against treating all coordinates as the same physical object. Retain.
- Indices/counts bullet: cell-array scope plus E1 spike/P11 dimension exceptions is concrete. Dimensionless count and neuron-vs-field N meanings are relevant distinctions; no count tutorial added. Retain.
- Time bullet: seconds grouped once, response-role differences kept local, P9 spatial t exception explicit. This is a short units rule rather than pretending every tau has the same biological meaning. Retain.
- Diffusion bullet: states coordinate²/time and the precise ordinary 2Dt situation, then short-lag filtered-output exception. That condition earns its sentence because two papers share D but show different output curves. Retain.
- Information bullet: J scope and units are direct; scalar-vs-matrix exceptions point to exact rows. No additional information-theory lesson needed on this return page. Retain.
- Hats/arrays bullet: short notation conventions identify estimates/predictions and array transpose. Row still specifies observations, so common hat convention does not hide what is estimated. Retain.
- Changing r/W/h list: each letter maps to specific physical role and, where needed, exact result ID. This is distinct from common quantity aliases and should not be merged into the firing-rate paragraph. Retain.
- Changing C/s/chi list: shared displacement vs covariance, activation vs time vs field size, fraction vs topology are genuine collisions. Units/roles are ordinary enough for physics/CS and specific enough to prevent wrong substitution. Retain.
- Sigma/V list: spatial scale, input standard deviation, eye measurement standard deviation and variance/environment size are the needed interpretations. Explicit units are already in adjacent common or local keys; another generic standard-deviation definition would add clutter. Retain.
- Memory additions: removed rate/coordinate/count/seconds/D/J repetition now common. Remaining activation, bias/weight/transfer, steady bar, rate slope, synaptic time, projection and error-variance subscript details are model-specific. The common-key backlink and both-table scope tell reader what was moved. Retain.
- Eye additions: remaining lag, measured vs spike-predicted angle, MSD/covariance, normalized kernel and350ms correlation meanings supplement common units/hats/D. Its statement that filter normalization is local is necessary. Retain.
- Place additions: remaining dimension, fixed map/threshold normalization, gain, spatial covariance and scale, tails/crossings and geometric sizes/constants are spatial-model details. Shared physical position and rate definitions need not be copied. Retain.
- Step3 and tools route: now accurately say common meanings, selected-paper additions, then row extras. Source/guide-location promise remains valid because all35 row contents remain unchanged. Retain.

## Deletion test and reuse

- A few alias reminders remain both in changing-letter list and local keys: their jobs differ, cross-paper warning versus exact in-model definition. These brief repetitions help avoid wrong substitution; deleting them is not required for the requested compact common key.
- Existing row wording judgments remain applicable to byte-identical YAML. This call did not reopen source formulas or prior full-row reviews; only the changed grouping and instructions were judged. Mean, variance, standard deviation and density remain assumed baseline.
- `content/chapters/00-exam-review.md` SHA256 `93e6d639d6a89e1c478196b0f161525a2a2c458b29f38bf9416866b86fc2b2de`
- `content/chapters/00-mathematical-tools.md` SHA256 `4805e574f757ba940c15d4669d47911876ad7daf4e2630212477b803a59d256f`
- `content/chapters/00-exam-review.yaml` SHA256 `e46668a7d36da8306487a3e87e6af2ebecdcd699ed1bca03a02d85151a9956e9`
- `C:/Users/vital/.codex/skills/course-study-guide-builder/references/pedagogy-language-contract.md` SHA256 `f4c1eb544cf640b708e1970d9572fdc758fcc6aea806675d01a0256658df847a`
- No unresolved required wording finding. No reading-flow or rendered-output verdict in this call. No memory used. Token stats unavailable.
