from pathlib import Path
import csv, json, shutil, datetime
import yaml

ROOT = Path(__file__).resolve().parents[2]
EVIDENCE = Path(__file__).resolve().parent

def backup(relative):
    dest = EVIDENCE / 'baseline' / relative
    if not dest.exists():
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ROOT / relative, dest)

def write(relative, text):
    backup(relative)
    (ROOT / relative).write_text(text, encoding='utf-8', newline='\n')

relative = 'content/chapters/01-foundations.md'
text = (ROOT / relative).read_text(encoding='utf-8')
text = text.replace(r'\sum_{t_i^\alpha<t}', r'\sum_{t_i^\alpha\le t}')
text = text.replace('after initial transients. Here $s_i$ is dimensionless', 'once the contribution from any activation present at the starting time has decayed. The sum includes a spike at time $t$, so it gives the activation immediately after that spike. Here $s_i$ is dimensionless')
write(relative, text)

relative = 'content/chapters/glossary.md'
text = (ROOT / relative).read_text(encoding='utf-8')
text = text.replace('A point-mass distribution. In the initial-condition equation all probability is concentrated at the specified coordinate.', 'An ideal unit impulse, with integral one across its location. In the spike equation it adds one unit of synaptic activation at the spike time. In the probability initial condition it concentrates all probability at one coordinate.')
write(relative, text)

relative = 'source-maps/source-coverage.csv'
with (ROOT / relative).open(encoding='utf-8', newline='') as file:
    reader = csv.DictReader(file)
    fields, rows = reader.fieldnames, list(reader)
for row in rows:
    key = next(iter(row.values()))
    for field, value in row.items():
        if not isinstance(value, str):
            continue
        if key in ['P1-p06', 'P1SI-p01', 'P1SI-p02']:
            row[field] = value.replace('sec:MEMORY-SPIKES', 'sec:MEMORY-WEAK-NOISE')
        elif key in ['P1-p01', 'P1-p05']:
            row[field] = value.replace('sec:MEMORY-SPIKES', 'sec:MEMORY-SPIKES; sec:MEMORY-WEAK-NOISE')
backup(relative)
with (ROOT / relative).open('w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)

relative = 'source-maps/research-ledger.csv'
with (ROOT / relative).open(encoding='utf-8', newline='') as file:
    reader = csv.DictReader(file)
    fields, rows = reader.fieldnames, list(reader)
for row in rows:
    if next(iter(row.values())) == 'MD01':
        for field, value in row.items():
            row[field] = value.replace('sec:MEMORY-SPIKES', 'sec:MEMORY-SPIKES; sec:MEMORY-WEAK-NOISE')
backup(relative)
with (ROOT / relative).open('w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)

relative = 'source-maps/equation-registry.yaml'
text = (ROOT / relative).read_text(encoding='utf-8')
text = text.replace('guide_location: sec:MEMORY-SPIKES', 'guide_location: sec:MEMORY-SPIKES; sec:MEMORY-WEAK-NOISE', 1)
write(relative, text)

relative = 'source-maps/visual-ledger.yaml'
text = (ROOT / relative).read_text(encoding='utf-8')
start = text.index('- visual_id: fig:MEMORY-SPIKE-TRACE')
end = text.index('\n- visual_id:', start + 1)
block = text[start:end]
block = block.replace('calculated exactly from the chapter equation.', 'calculated exactly from Burak and Fiete (2012), Eq. 7.')
block = block.replace('caption_and_alt: content/chapters/02-memory-dynamics.yaml', 'caption_and_alt: content/chapters/01-foundations.yaml')
block = block.replace('toc_correspondence: ch:MEMORY-DYNAMICS,', 'toc_correspondence: ch:FOUNDATIONS,')
write(relative, text[:start] + block + text[end:])

relative = 'source-maps/terminology-ledger.yaml'
text = (ROOT / relative).read_text(encoding='utf-8')
for term in ['neural transfer function', 'weak fluctuation approximation', 'preferred angle']:
    start = text.index('- term: ' + term + '\n')
    end = text.find('\n- term:', start + 1)
    end = len(text) if end < 0 else end
    block = text[start:end]
    if term == 'neural transfer function':
        block = block.replace('content/chapters/02-memory-dynamics.md', 'content/chapters/01-foundations.md')
    else:
        block = block.replace('sec:MEMORY-SPIKES', 'sec:MEMORY-WEAK-NOISE')
    source = next(line.split(': ', 1)[1] for line in block.splitlines() if line.strip().startswith('source:'))
    line_number = next((i for i,line in enumerate((ROOT/source).read_text(encoding='utf-8').splitlines(),1) if term in line),None)
    if line_number:
        import re
        block = re.sub(r'  line: \d+', f'  line: {line_number}', block)
    text = text[:start] + block + text[end:]
write(relative,text)

relative = 'plan/chapter-plan.yaml'
data = yaml.safe_load((ROOT / relative).read_text(encoding='utf-8'))
for block in data['book']['parts'][0]['content']:
    if '.part-chapter-map' in block.get('text',''):
        block['text'] = block['text'].replace('**Background:** Neural firing rates and spike variability supply the quantities needed for the later memory calculation.', '**Background and model:** Spikes leave decaying synaptic activation; weighted activation sets input, and input sets firing rate. Equations 7–9 of Burak and Fiete (2012) establish these dynamics before the chapters on stability and diffusion. Neural coding and spike variability supply the remaining quantities for the memory calculation.')
write(relative, yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=110))

state = json.loads((EVIDENCE / 'STATE.json').read_text(encoding='utf-8'))
state['checkpoint_at_utc'] = datetime.datetime.now(datetime.timezone.utc).isoformat()
state['status'] = 'source move and metadata complete; scoped reading review, then HTML build'
(EVIDENCE / 'STATE.json').write_text(json.dumps(state,indent=2),encoding='utf-8')
print('Updated source explanation, term lookup, source locations, figure owner and Part I chapter map.')
