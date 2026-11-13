# Numbered HTML examples

This project extension labels code and worked examples in reading order within
each chapter. `number_page(html, chapter, mode="unified")` returns transformed
HTML and a label/target inventory. Use `mode="separate"` for independent code
and worked-example sequences. Numbering is positional; inserting an example
renumbers later examples. Existing listing IDs are retained as link targets.

The caller chooses which detailed setup paragraphs belong inside a fold and
marks any short outside reference with `data-example-reference="<listing-id>"`.
This extension links that reference to its generated example label. It does not
choose folds, alter body text, or grant semantic acceptance.

The Module 1 HTML build wrapper invokes this extension after its folding pass
and records the labels in its build manifest. The reusable source is also
provided in the Publisher project template. This is an HTML extension; DOCX and
PDF numbering are not implemented by this file.
