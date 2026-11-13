"""Prepare reviewable Chapter 2 additions without changing reader sources."""
from pathlib import Path
import json
import re
import yaml

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
source = OUT / 'baseline/content/chapters/02-memory-dynamics.md'
original = source.read_text(encoding='utf-8')
text = original
locators = json.loads((OUT / 'source-locators.json').read_text(encoding='utf-8'))['locators']
files = {'main': 'burak-fiete-2012-persistent-activity.pdf', 'si': 'burak-fiete-2012-persistent-activity-si.pdf'}
changes = []

def link(label, key):
    loc = locators[key]
    top = max(0, round(loc['bbox_points_top_left'][1]) - 25)
    href = f"../papers/{files[loc['source_id']]}#page={loc['pdf_page']}&zoom=125,0,{top}"
    return f'[{label}]({href})'

def replace(old, new, purpose):
    global text
    assert text.count(old) == 1, (purpose, text.count(old))
    text = text.replace(old, new)
    changes.append({'purpose': purpose, 'before': old, 'after': new})

def add_after(marker, addition, purpose):
    replace(marker, marker + '\n\n' + addition, purpose)

intro_note = 'Paper and Supporting Information (SI) links open the cited PDF page, near the passage where the viewer supports it. Use the equation, figure, or paragraph label to find the passage; the PDFs have no numbered text lines.'
opening = text.split('\n\n')[1]
add_after(opening, intro_note, 'Explain how to use precise paper links')

# Keep all scientific content and equations; add links to existing descriptions.
replace('The paper allows general connectivity and transfer functions at first.[^p1-model]',
        'The paper allows general connectivity and transfer functions at first (' + link('Model, Eqs. 7–9, p. 5', 'main-model') + ').[^p1-model]', 'Model passage link')
replace('It does not require each single neuron\'s entire spike train to look like a Gaussian process.[^p1-weak]',
        "It does not require each single neuron's entire spike train to look like a Gaussian process (" + link('SI Eqs. S2–S5, p. 2', 'si-gaussian') + ').[^p1-weak]', 'Weak fluctuation passage link')
replace('The left vector discards every decaying mode.',
        'The left vector discards every decaying mode (' + link('SI Eqs. S12–S13, p. 3', 'si-left') + ').', 'Left projection passage link')
replace('Matching this to $2D\\,dt$ yields the general local result',
        'Matching this to $2D\\,dt$ yields the general local result (' + link('SI Eqs. S14–S15, p. 3', 'si-project') + ')', 'Diffusion result link')
replace('This follows from SI Eq. S18,', 'This follows from ' + link('SI Eq. S18, p. 4', 'si-s18') + ',', 'Symmetric result link')
replace('The supplied Early Edition main Eq. 2 appears', 'The supplied Early Edition ' + link('main Eq. 2, p. 2', 'main-eq2') + ' appears', 'Source discrepancy comparison link')
replace('This model underlies the mutual inhibition example in Fig. 2.',
        'This model underlies the mutual inhibition example in ' + link('Fig. 2E–G, p. 3', 'main-fig2-caption') + '.', 'Mutual inhibition paper figure link')
replace('This teaches the content of SI Eq. S31 without needing the special function notation used there.',
        'This teaches the content of ' + link('SI Eq. S31, p. 7', 'si-wrapped') + ' without needing the special function notation used there.', 'Wrapped density passage link')
replace('This is SI Eq. S37.', 'This is ' + link('SI Eq. S37, p. 8', 'si-s37') + '.', 'Variable diffusion passage link')
replace('agreeing with SI Eq. S41 and the slope tested in Fig. S1.',
        'agreeing with ' + link('SI Eq. S41, p. 9', 'si-s41') + ' and the slope tested in ' + link('Fig. S1, p. 10', 'si-excitation-fig') + '.', 'Excitation source comparison links')
replace('beyond the leading variance calculation.[^p1-systematic]',
        'beyond the leading variance calculation (' + link('SI “Systematic drift,” pp. 4–5', 'si-drift-limit') + ').[^p1-systematic]', 'Systematic drift passage link')
replace('The paper discusses such correlated models as future extensions;',
        'The paper discusses such correlated models as future extensions (' + link('Discussion, p. 5, paragraph beginning “Our spiking model”', 'main-correlations') + ');', 'Correlations discussion paragraph link')
replace('Figure 1A shows the definition of the memory coordinate.',
        link('Figure 1A, p. 2', 'main-fig1') + ' shows the definition of the memory coordinate.', 'Paper figure reading entry link')
replace('Figure 2 tests the diffusion calculation in two different network designs.',
        link('Figure 2, p. 3', 'main-fig2') + ' tests the diffusion calculation in two different network designs.', 'Second paper figure entry link')

pending = yaml.safe_load((OUT / 'pending-visual-ledger.yaml').read_text(encoding='utf-8'))
rows = pending['visuals'] if isinstance(pending, dict) else pending
intro1 = 'For five illustrative spike times, the plot shows the events and the activation they leave behind.'
rows[0]['teaching_introduction'] = intro1

def figure_block(row):
    return row['teaching_introduction'] + '\n\n<div class="figure-scroll">\n\n{{block:' + row['block_id'] + '}}\n\n</div>\n\n' + row['interpretation']

# Split an existing paragraph at a natural teaching boundary; retain its words.
marker = 'after initial transients. Here $s_i$ is dimensionless in the convention that each spike adds one unit.'
replace(marker + ' The rate $r_i$', marker + '\n\n' + figure_block(rows[0]) + '\n\nThe rate $r_i$', 'Spike trace figure after activation definition')
marker = 'This model underlies the mutual inhibition example in ' + link('Fig. 2E–G, p. 3', 'main-fig2-caption') + '.[^p1-two]'
add_after(marker, figure_block(rows[1]), 'Opposing rates figure after exact model calculation')
marker = "The flattening of a ring network's error curve can therefore occur while its local noise mechanism remains unchanged. It reflects the bounded way angular error is reported.[^p1-fp]"
add_after(marker, figure_block(rows[2]), 'Line and ring figure after angular variance derivation')

fn_replacements = {
'p1-model': ('Main text pp. 1–2 and 5, Eqs. 1 and 7–9.', link('Main Eq. 1 and the steady state, p. 2', 'main-steady-state') + '; ' + link('Model, Eqs. 7–9, p. 5', 'main-model') + '.'),
'p1-weak': ('Main text pp. 5–6, Eqs. 10–11; Supporting Text, Section I.', link('Weak Fluctuations, Eqs. 10–11, p. 5', 'main-weak') + ', ' + link('continuation, p. 6', 'main-large') + '; ' + link('SI Eqs. S2–S5, p. 2', 'si-gaussian') + '.'),
'p1-large': ('Supporting Text, pp. 1–2, Eqs. S1–S6.', 'Supporting Text: ' + link('Eq. S1, p. 1', 'si-population') + '; ' + link('Eqs. S2–S5, p. 2', 'si-gaussian') + '; ' + link('ring population limit, Eq. S6, p. 2', 'si-ring-large') + '.'),
'p1-projection': ('Supporting Text, pp. 3–4, Eqs. S7–S15.', 'Supporting Text, p. 3: ' + link('linearization, Eqs. S7–S10', 'si-linearization') + '; ' + link('tangent, Eq. S11', 'si-tangent') + '; ' + link('left vector, Eqs. S12–S13', 'si-left') + '; ' + link('projected diffusion, Eqs. S14–S15', 'si-project') + '.'),
'p1-multid': ('Supporting Text, pp. 5–6, Eqs. S21–S27.', 'Supporting Text: ' + link('Eq. S21, p. 5', 'si-multid-start') + '; ' + link('Eqs. S22–S27, p. 6', 'si-multid') + '.'),
'p1-symmetric': ('main Eq. 2; Supporting Text, p. 4, Eqs. S16–S18.', link('main Eq. 2, p. 2', 'main-eq2') + '; ' + link('Supporting Text, Eqs. S16–S18, p. 4', 'si-symmetric') + '.'),
'p1-two': ('Fig. 2E–G and Network Simulations, p. 6.', link('Fig. 2E–G and caption, p. 3', 'main-fig2-caption') + '; ' + link('Network Simulations, mutual inhibition, p. 6', 'main-two-sim') + '.'),
'p1-fp': ('Supporting Text, pp. 6–8, Eqs. S28–S32.', 'Supporting Text: ' + link('density equation, Eqs. S28–S29, p. 7', 'si-fp') + '; ' + link('Gaussian on a line, Eq. S30, p. 7', 'si-gaussian-line') + '; ' + link('wrapped density and uniform limit, Eq. S31, p. 7', 'si-wrapped') + '; ' + link('angular error, Eq. S32, p. 8', 'si-wrapped-moment') + '.'),
'p1-variable': ('Supporting Text, p. 8, Eqs. S33–S37.', link('Supporting Text, Eqs. S33–S37, p. 8', 'si-variable') + '.'),
'p1-excitation': ('Supporting Text, pp. 8–10, Eqs. S38–S41 and Fig. S1.', link('Supporting Text, Eqs. S38–S41, p. 9', 'si-excitation') + '; ' + link('Fig. S1, p. 10', 'si-excitation-fig') + '.'),
'p1-systematic': ('Supporting Text, pp. 4–5, Systematic drift, Eqs. S19–S20.', 'Supporting Text: ' + link('“Systematic drift,” p. 4', 'si-drift-limit') + '; ' + link('Eqs. S19–S20 and continuation, p. 5', 'si-drift') + '.'),
'p1-correlation': ('Discussion, p. 5.', link('Discussion, p. 5, paragraph beginning “Our spiking model”', 'main-correlations') + '.'),
'p1-fig1': ('Fig. 1, p. 2.', link('Fig. 1 and caption, p. 2', 'main-fig1') + '; ' + link('flow definition, “In what follows,” p. 2', 'main-flow-definition') + '.'),
'p1-fig2': ('Fig. 2, p. 3; Network Simulations, p. 6.', link('Fig. 2 and caption, p. 3', 'main-fig2') + '; Network Simulations: ' + link('ring model, p. 6', 'main-ring-sim') + ' and ' + link('mutual inhibition, p. 6', 'main-two-sim') + '.'),
}
for key, (old, new) in fn_replacements.items():
    line = next(line for line in text.splitlines() if line.startswith(f'[^{key}]: '))
    assert old in line, key
    replace(line, line.replace(old, new), f'Precise links in footnote {key}')

meta = yaml.safe_load((OUT / 'baseline/content/chapters/02-memory-dynamics.yaml').read_text(encoding='utf-8'))
names = ['memory-spike-trace', 'memory-inhibition-rates', 'memory-line-ring']
for row, name in zip(rows, names):
    row['asset'] = f'assets/approved/visuals/{name}.png'
    meta['blocks'].append({'id': row['block_id'], 'kind': 'figure', 'placement': row['placement'], 'asset': row['asset'], 'caption': row['caption'], 'alt': row['accessibility_description'], 'width_inches': 7.29167, 'html_fold': 'never'})

# The source summary loses its leading plain-text match when the first words become a link.
meta['section_list'][-1]['summary'] = meta['section_list'][-1]['summary'].replace('Figure 1A shows', 'Figure 1A, p. 2 shows')
(OUT / 'proposed-chapter.md').write_text(text, encoding='utf-8', newline='\n')
(OUT / 'proposed-chapter.yaml').write_text(yaml.safe_dump(meta, allow_unicode=True, sort_keys=False, width=84), encoding='utf-8')
(OUT / 'integration-rows.yaml').write_text(yaml.safe_dump({'visuals': rows}, allow_unicode=True, sort_keys=False, width=84), encoding='utf-8')
(OUT / 'insertions.json').write_text(json.dumps(changes, ensure_ascii=False, indent=2), encoding='utf-8')
# Round-trip check proves that the described changes recover the original chapter.
reverse = text
for item in reversed(changes):
    assert reverse.count(item['after']) == 1
    reverse = reverse.replace(item['after'], item['before'])
assert reverse == original
print(json.dumps({'changes': len(changes), 'pdf_links': len(re.findall(r'\.pdf#page=', text)), 'new_figures': len(rows), 'original_recovered': reverse == original}))
