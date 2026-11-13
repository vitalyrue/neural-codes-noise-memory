"""Keep the four editable figure definitions aligned with their individually reviewed text."""
from pathlib import Path
import json
OUT = Path(__file__).resolve().parent
source = OUT / 'draw_foundations_information.py'
text = source.read_text(encoding='utf-8')
changes = [
 ('Estimates above 100 Hz are outside the displayed range.', 'Only estimates through 100 Hz are drawn.'),
 ('Dividing the pooled count by 20 keeps the expected rate per cell fixed,', 'Dividing the pooled rate estimate by 20 keeps the expected rate per cell fixed,'),
 (r'$(r_i\\prime)^2/r_i$', r'$(r_i^{\\prime})^2/r_i$'),
]
for old, new in changes:
    assert text.count(old) == 1, repr(old)
    text = text.replace(old, new, 1)
source.write_text(text, encoding='utf-8', newline='\n')
print('Synchronized three previously recorded wording repairs in generator metadata; plotting functions unchanged.')
