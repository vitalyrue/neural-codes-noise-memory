# Neural memory in electronic hardware

<!-- vale ai-tells.SequencingMarkers = NO -->
<!-- vale ai-tells.VerbTricolon = NO -->
> “Lastly, I would like to mention that systems of nerve cells, which stimulate each other in various possible cyclical ways, also constitute memories.”
<!-- vale ai-tells.VerbTricolon = YES -->
<!-- vale ai-tells.SequencingMarkers = YES -->

John von Neumann, *The Computer and the Brain* (1958), [printed page 66, PDF page 78](https://vpb.smallyu.net/%5BAuthor%5D%20John.Von.Neumann/The%20Computer%20and%20The%20Brain.pdf#page=78).

Von Neumann compares mutually stimulating nerve cells with electronic circuits that preserve a state through feedback. In the following pages he also questions whether active elements alone could provide the nervous system's main large-capacity store. His comparison invites us to distinguish a memory's physical mechanism from the information it keeps. It does not establish that every brain memory uses persistent activity, or that present hardware follows one historical line from his book.

The setting here is experimental and computational neuroscience joined with electronic engineering. We ask how a silicon circuit can retain a quantity such as an angle, and what physical processes limit its accuracy. [A durable connection weight, a lasting activity pattern, and an accurately remembered value are three different achievements.]{.key-statement}

<!-- vale ai-tells.VerbTricolon = NO -->
The path starts with what is stored and where, then explains what feedback preserves. With those distinctions in place, we compare digital spiking processors, analog neural circuits, and phase-change weight storage. The final chapter turns the comparison into measurements of drift, noise, decoding error, and energy. Parts I and II provide the neural models and experimental reasoning. This Part extends them to selected hardware research current to **October 30, 2026**.
<!-- vale ai-tells.VerbTricolon = YES -->

For a first pass, read the physical explanations, main results, and interpretations. Worked calculations and deeper derivations are folded. The comparison assumes the calculus, basic probability, and linear algebra used earlier. Electronics terms are introduced as they become necessary.
