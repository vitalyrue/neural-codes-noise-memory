# Neural Codes, Noise, and Memory

Open [the HTML guide](site/index.html), beginning with **Reading path and paper copies**. It contains six chapters, the glossary and references. Paper PDFs and mathematical supplements are linked from the reading path and included in the site folder.

The guide assumes undergraduate calculus, basic probability and linear algebra. It teaches the neuroscience and additional mathematical ideas before the central derivations. Experimental interpretation, worked examples, related work and limits accompany the calculations. Imported full theorems are identified, and no original experiment or full network simulation is claimed as reproduced.

For the current local server, open http://127.0.0.1:8765/guide/site/index.html. If the server has stopped, serve the parent `burak-papers` folder with Python's HTTP server. Math rendering uses the MathJax CDN, so internet access is needed for its runtime.

Editable text is in `content/chapters/`; `guide-project.yaml` and `plan/chapter-plan.yaml` define publication structure. `CURRENT_STATE.md` records the final handoff and safe build sequence. `verification/DELIVERY.json` identifies the delivered model/output. Staged independent reports and current paragraph judgments are in `verification/reviews/` and `verification/pedagogy/`. Source maps distinguish taught material, consolidation and intentional omission.

After editing or building tables, run `verification/check_tables.py`. It checks every reader table against its typed source cells and rejects flattened pipe-table text. Tables use sidecar blocks and a `table-responsive` wrapper in the Markdown.

Local HTML checks pass. The authoritative Publisher release check still requires pinned Publisher and skill versions; the current development locks have not been changed to imply a clean release.
