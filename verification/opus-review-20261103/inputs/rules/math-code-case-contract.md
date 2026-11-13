# Mathematics, code, experimental protocols, and case contract

## Equations and formal derivations

Render reader-facing equations as native OfficeMath in DOCX (or clean LaTeX/Typst math in non-Word builds). Raw LaTeX source text is not final reader output; mathematical subscripts, superscripts, Greek characters, and tensor indices must render legibly.

For each core equation, law, or theorem, provide:
- **Provenance & Context**: Origin, assumptions, and physical/mathematical domain.
- **Variable Roles**: Explicit definitions, dimensions, units, or tensor shapes for every symbol.
- **Derivation / Mechanism**: Step-by-step mathematical derivation, proof sketch, or logical transition.
- **Example**: Concrete numerical, algebraic, or geometric example demonstrating computation.
- **Interpretation & Limitations**: Intuitive geometric or physical meaning, failure regimes, and boundary constraints. Number equations by chapter when the publication profile requires it.

## Examples and notation

Label a reader-facing calculation callout `Example:` followed by what it computes. The publisher also accepts the older `Worked calculation:`, `Worked example:`, and `Example calculation:` titles for the same panel, so an existing guide keeps its styling until its next review; prefer the short label in new and revised material. Changing these titles across a guide is a wording pass and follows the rules in the language contract.

An example earns its space by showing something the definition does not. Choose inputs where the result is not obvious from the formula, where two candidate methods diverge, where a limit binds, or where the failure appears. Cut an example that restates the formula with round numbers, confirms what the preceding sentence already said, or arrives at a result the reader could have written down without it. One example that exposes the mechanism is worth more than three that repeat it.

Explain the notation the subject introduces, not the notation the stated audience already has. For a reader assumed to know undergraduate mathematics, do not gloss standard operators such as the sum, product, exponential, or ordinary subscripts and superscripts. Define instead what each symbol ranges over in this equation, which positions, vocabulary entries, or examples the index covers, and which quantity the result is, because that part is specific to the system being taught. Gloss a standard symbol only where the passage uses it unusually, or where the audience baseline records that the notation is new to the reader.

## Code and computational walkthroughs

Introduce the purpose and input/output contract before code. Map important lines to the taught mechanism. State whether the example is runnable, abbreviated, or pseudocode; explain expected output, state changes, failure handling, and library/version ownership.

Run each listing before accepting what the text says about it. Keep a small test with the guide's review records that executes the listing on the inputs the prose makes claims about: a typical input, an empty input, an invalid input, and each failure path the text describes. Replace model providers, network calls, credentials, and large downloads with stand-ins. Check what the code returns and what it records, not only that it runs. For example, a trace that stores the passages selected before the prompt is built does not show what the model received; a stand-in renderer that drops them exposes the gap. A statement about a listing's behavior without such a test is unchecked. When a listing cannot run, because it is pseudocode, a fragment, or needs hardware the reviewer lacks, the text says so and the review records how each claim was checked instead.

Avoid fragmented decorative snippets that do not teach execution flow. Keep code out of raster artwork unless the visual meaning requires it.

## Experimental protocols, assays, and case studies

Assignments, lab guides, or research papers may supply realistic protocols, biological assays, schemas, constraints, and experimental measurements. Convert them into structured teaching cases:
- Trace hypotheses, control setups (positive/negative controls), inputs, intermediate states, and quantitative outputs.
- Explain experimental decision points, measurement techniques (e.g., spectrophotometry, sequencing depth, benchmark metrics), and error analysis.
- Expose reasoning and evidence without producing submission-ready homework solutions.
