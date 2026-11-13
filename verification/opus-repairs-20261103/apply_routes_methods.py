from pathlib import Path
from datetime import datetime, timezone
import json, hashlib, re

root = Path(__file__).resolve().parents[2]
edits = []

def change(path, old, new, reason, source):
    edits.append(dict(path=path, original=old, replacement=new, reason=reason, source=source))

def purpose(path, new):
    text = (root / path).read_text(encoding='utf-8')
    old = re.search(r'^purpose:.*?(?=^role:)', text, re.M | re.S).group()
    change(path, old, 'purpose: ' + json.dumps(new, ensure_ascii=False) + '\n',
           'Keep chapter metadata aligned with the revised methods opening.', 'Guide methods organization; no new scientific claim.')

reading = 'content/chapters/00-reading-guide.md'
change(reading,
'- **Place fields:** read the two foundations chapters and then chapters 10–12. The spatial calculation does not require the readout derivation in chapter 6.',
'- **Place fields:** start with [tuning curves, population codes, and rate maps](../chapters/ch-foundations.html#sec-foundations-spikes), then [variable spike counts](../chapters/ch-foundations.html#sec-foundations-poisson), and [fixed spatial maps versus values that change over time](../chapters/ch-persistence.html#sec-foundations-randomness). Continue with chapters 10–12. This short route supplies the shared foundations without requiring the eye-mechanics or memory-readout calculations.',
'SR3: give the place-field reader the exact relevant foundation sections while retaining chapter order.',
'Guide sec:FOUNDATIONS-SPIKES, sec:FOUNDATIONS-POISSON, sec:FOUNDATIONS-RANDOMNESS; Opus stage3 SR3.')
change(reading,
'Throughout the guide, $D$ denotes the',
'''The following map is a **guide-derived comparison** of the source papers' contributions. Read each paper's column downward: the mathematical prediction, numerical comparison, and animal-data comparison answer different questions.[^orientation-memory][^orientation-eye][^orientation-place]

<div class="table-responsive">

{{block:tbl:READING-EVIDENCE}}

</div>

Throughout the guide, $D$ denotes the''',
'C3: collect the physical system, model, prediction, simulation, data, and limits in one visible map.',
'Burak and Fiete main PDF pp.1–3,5–6, Fig.2; Ben-Shushan main pp.3–8,10–11, Figs.2–5; Mainali main pp.3–8,13–15, Figs.1–5.')
sidecar = 'content/chapters/00-reading-guide.yaml'
new_table = '''- id: tbl:READING-EVIDENCE
  kind: table
  placement: sec:READING-SCOPE
  headers:
  - Step in the evidence
  - Burak and Fiete (2012)
  - Ben-Shushan et al. (2022)
  - Mainali et al. (2025)
  rows:
  - - Physical system and question
    - A proposed neural circuit maintaining a continuous value after a cue ends. How quickly does its accuracy deteriorate?
    - Motor-neuron activity and eye motion during macaque fixation. Where does the shared motion originate?
    - Place-cell responses in rodent and bat environments. Why do field sizes and shapes vary?
  - - Actors, variables, and interactions
    - Recurrent weights couple synaptic activations to firing rates. Random spikes renew activation and disturb the represented coordinate.
    - Two neural populations produce an internal eye-position command. Motor spikes, muscles, and delayed feedback connect it to actual eye angle.
    - Each cell receives a smooth Gaussian spatial input function. Thresholding gives its active regions; the map itself is fixed during analysis.
  - - Derived prediction
    - Spike fluctuations produce memory diffusion. An information bound limits stability under the model assumptions.
    - Shared and private fluctuations imply displacement-covariance relations. Filtering a diffusing command predicts the time dependence of eye motion.
    - Covariance, threshold, and dimension determine field statistics, with exact results and high-threshold approximations kept separate.
  - - Simulation comparison
    - Stochastic ring and two-population networks test theoretical memory diffusion. These are model tests, not animal-data validation.
    - A noisy integrator and motor pathway test whether the proposed mechanism can produce the observed motion and analysis results.
    - Generated spatial maps test analytical approximations and provide finite-threshold comparisons with recorded field statistics.
  - - Empirical comparison
    - This study does not directly test the bound against animal recordings.
    - Paired single-neuron and eye recordings support a substantial shared source upstream of the final motor neurons, under the inference assumptions.
    - Existing rodent and bat recordings test field sizes, arrangements, shapes, and connectedness. Parameters fitted to summaries remain distinct from additional comparisons.
  - - What remains unknown
    - Whether a biological memory circuit meets the assumptions or approaches the bound.
    - Whether the shared source is specifically the modeled integrator. A successful model does not uniquely locate it.
    - Which connections, learning rules, and dynamics generate the spatial inputs. A statistical fit does not establish a memory circuit.
  caption: Guide-derived map of the three source papers' evidence. Each column follows a separate study; the table does not claim a jointly tested circuit.
  first_column_role: row-labels
  html_fold: never
'''
change(sidecar, 'source_loci: []', new_table + 'source_loci: []',
'Render the evidence map with the guide existing native table pattern, inside its responsive wrapper.',
'Same source pages as the reading-guide map introduction.')
change('content/chapters/06-synthesis.md', 'Nghiem, T. E., Witten', 'Nghiem, T. A. E., Witten',
'F11: align initials with the original article.', 'Original PNAS article DOI 10.1073/pnas.2416266122; confirmed Opus review F11.')

p = 'content/chapters/11-simulating-memory.md'
old = "Burak and Fiete (2012) derive memory diffusion from assumptions about recurrent connections and random spike timing. To test that prediction, they simulate individual spikes and measure how the stored value moves. The central result remains an analytical bound. The simulations check its predicted motion in different network designs, including the limits imposed by an angular coordinate."
new = "To compare a simulated memory trace with Burak and Fiete's (2012) theory, the numerical update and the measurement of the stored value must match the model. The [foundation chapter](ch-foundations.html#sec-foundations-simulation) explains the spike-update cycle, and the [long-delay chapter](ch-memory-long-delays.html) interprets its diffusion tests. Here the additional task is to recover the published network settings, distinguish a numerical position measurement from the theoretical coordinate, and identify choices left open for an independent reproduction."
change(p, old, new, 'SR2: lead with the methods chapter additional purpose and link existing teaching.', 'Guide Chapters 1 and 4; Burak and Fiete main Methods pp.5–6.')
purpose('content/chapters/11-simulating-memory.yaml', new)
old = "In the ring model, neurons are ordered by their preferred angles. Their connections support a localized activity pattern whose position represents an angle. Figure 2A–D compares the wandering position with predictions calculated from the network's steady tuning curves. Two transfer functions test different relationships between diffusion and spike information: the exponential case attains the bound under the model assumptions, while the illustrated sigmoid case lies above it.[^simmem-ring]"
new = "In the ring model, neurons are ordered by preferred angle, and the position of their localized activity pattern represents the stored angle. The [earlier Figure 2 discussion](ch-memory-long-delays.html) explains the diffusion and information comparison. To reproduce that comparison, keep the exponential and sigmoid transfer functions as separate runs, with a theoretical prediction calculated from each run's steady tuning curves.[^simmem-ring]"
change(p, old, new, 'SR2: replace repeated result interpretation with the operational distinction between runs.', 'Burak and Fiete main Fig.2A–D p.3 and Network Simulations p.6.')
sc = 'content/chapters/11-simulating-memory.yaml'
sc_text=(root/sc).read_text(encoding='utf-8')
old_summary=re.search(r"  summary: 'In the ring model,.*?(?=  level: 2)",sc_text,re.S).group()
change(sc, old_summary, '  summary: ' + json.dumps(new, ensure_ascii=False) + '\n', 'Keep section summary aligned.', 'Same Figure 2 and Methods sources.')
old = "For this simulation the authors decode the angle of the neuron with the largest instantaneous rate. That convenient numerical readout differs from the ideal spike-based estimator studied later in the paper."
new = "For this simulation the authors record the preferred angle of the neuron with the largest instantaneous rate. This is a numerical proxy for the represented position. The theoretical coordinate $\\theta$ is assigned by following noise-free relaxation back to the attractor; the largest-rate rule does not carry out that projection. Its output lies on the finite lattice of preferred angles, and brief changes in the pattern's shape can shift its maximum during relaxation. These effects matter when interpreting very short lags. This rule also differs from the ideal spike-based estimator studied later in the paper."
change(p, old, new, 'F09: distinguish maximum-rate measurement, flow-projected theoretical coordinate, and spike estimator; expose finite lattice and transient limits.', 'Burak and Fiete main Fig.1A p.2, Network Simulations p.6; guide ch:MEMORY-LONG-DELAYS projection explanation. Finite lattice and transient caution are guide-derived consequences of this measurement rule.')

p = 'content/chapters/12-simulating-eye-drift.md'
old = "Ben-Shushan et al. (2022) ask whether fluctuations in a neural memory circuit can explain the small eye movements that continue during fixation. Their simulation must turn a changing neural command into muscle action and eye position. It must also produce signals that can be analyzed like the recordings. The paper's central evidence combines a shared-source inference from data with a model showing that a noisy integrator can account for the observed motion."
new = "A reproduction of Ben-Shushan et al. (2022) must distinguish the recording analysis from the simulated eye-control pathway. The [circuit chapter](ch-eye-circuit.html) explains why a noisy internal command is a possible source of drift. Here the added detail is how the published parameters, spike generator, update intervals, saved samples, and MATLAB files determine the numerical experiment, and which code or data gaps limit reproduction. The pathway below gives the mechanism needed to interpret those choices."
change(p, old, new, 'SR2: introduce the unique numerical, code, and data content while keeping the causal pathway for methods readers.', 'Ben-Shushan main Methods pp.9–12 and inspected code; no new implementation claim.')
purpose('content/chapters/12-simulating-eye-drift.yaml', new)
old = "The empirical analysis uses earlier recordings of 57 ocular motor neurons from two macaques, paired with eye-position measurements. These are separate single-cell recordings, not a simultaneous recording of all 57 neurons. The authors fit each cell's relation to eye position, velocity, and acceleration, then use it to reconstruct movement from that cell's spikes. A trial held out of the fit tests prediction on data that did not determine the fitted parameters.[^simeye-data]"
new = "The empirical analysis uses earlier recordings of 57 ocular motor neurons from two macaques, paired with eye-position measurements. These are separate single-cell recordings, not a simultaneous recording of all 57 neurons. The authors fit each cell's firing-rate relation to eye position, velocity, and acceleration. For firing-rate prediction, they fit all trials except one and predict the firing rate in the omitted trial, repeating this leave-one-out procedure across trials. The analysis also uses the fitted movement relation to reconstruct motion from that cell's spikes.[^simeye-data]"
change(p, old, new, 'F03: attach leave-one-out validation specifically to firing-rate prediction without inferring the validation scheme for movement reconstruction.', 'Ben-Shushan main Methods p.9, extracted lines929–931 explicitly specify firing-rate prediction.')
sc='content/chapters/12-simulating-eye-drift.yaml'
sc_text=(root/sc).read_text(encoding='utf-8')
old_summary=re.search(r'  summary: The empirical analysis.*?(?=  level: 2)',sc_text,re.S).group()
change(sc, old_summary, '  summary: ' + json.dumps(new, ensure_ascii=False) + '\n', 'Keep the sidecar from retaining the broader held-out wording.', 'Same p.9 firing-rate prediction passage.')
old = """- **Private motor noise alone:** with a constant central command, independent motor-neuron fluctuations produce limited, saturating displacement variance. Figure 3 compares this contribution with the larger continued drift in the recordings.
- **Noisy integrator before the muscles:** Figure 4 measures the simulated internal command. At sufficiently long lags, its mean squared displacement approaches the linear dependence expected for diffusion.
- **Full pathway:** Figure 5 compares the final eye output with the recordings. Muscle filtering shapes the short-lag behavior, while delayed feedback changes the longer-lag behavior.
- **Measurement procedure applied to simulated signals:** simulated motor spikes and eye motion are passed through the same reconstruction and covariance analysis used for the recordings. This tests whether the analysis can recover the shared contribution under a model where its origin is known.[^simeye-figures]"""
new = """- **Change the noise source:** compare a fixed command with private motor noise (Figure 3), the noisy internal command before muscle filtering (Figure 4), and the complete pathway (Figure 5). The [circuit chapter](ch-eye-circuit.html) explains these comparisons. Keep the measured signal explicit: internal command and final eye angle are different outputs.
- **Check the measurement procedure:** apply the recording reconstruction and covariance analysis to simulated motor spikes and eye motion. This tests recovery of the shared contribution where its origin is known. Muscle filtering and delayed feedback must remain in the complete-pathway comparison.[^simeye-figures]"""
change(p,old,new,'SR2: shorten repeated figure interpretation while preserving control operations and measurement cautions.','Ben-Shushan main Figs.3–5 pp.6–8; existing circuit chapter.')

p='content/chapters/13-simulating-place-fields.md'
old="Mainali et al. (2025) ask whether one statistical model can explain the many firing regions observed in hippocampal place cells across different environments. Their simulation generates a cell's firing-rate map over space and measures the active regions. Position is the independent variable. The generated map is fixed while it is analyzed, so this simulation addresses spatial coding rather than how a neural circuit retains a position over time."
new="To reproduce Mainali et al.'s (2025) place-field comparisons, a random map and a recorded map must be generated, fitted, and measured with compatible rules. The [spatial-model chapter](ch-place-fields.html) explains the statistical assumptions, and the [tests chapter](ch-place-tests.html) interprets the evidence. Here the additional detail is the Python map-generation procedure, filter and boundary conventions, fitted summaries, field detectors, and access to code and recordings. Position is the independent variable; each generated map is fixed during analysis, so these computations do not simulate a remembered position changing over time."
change(p,old,new,'SR2: lead with implementation and measurement content while retaining the static-map distinction.','Mainali main STAR Methods pp.13–15; inspected source code; existing Chapters10–12.')
purpose('content/chapters/13-simulating-place-fields.yaml',new)

p='content/chapters/14-simulation-tools.md'
old="A simulated eye trace can look convincing while answering the wrong question. It may use different spike statistics, a different muscle response, or a different definition of displacement from the experiment. Reproducing a result requires matching those choices before comparing curves. This chapter collects the practical decisions shared by the three papers and identifies tools for making those decisions visible."
new="A simulated eye trace can look convincing while answering the wrong question. It may use different spike statistics, a different muscle response, or a different definition of displacement from the experiment. Beyond the paper-specific methods in the preceding chapters, a reproduction needs checks that its software, resolution, and saved run record preserve the intended comparison. This chapter explains how to choose those checks and distinguish the authors' program from an independent implementation or a smaller teaching model."
change(p,old,new,'SR2: identify the cross-paper numerical checks that this final methods chapter adds.','Guide-derived reproduction guidance; existing chapter explains each check.')
purpose('content/chapters/14-simulation-tools.yaml',new)

record = root/'verification/opus-repairs-20261103/edits-routes-methods.json'
record.write_text(json.dumps(dict(recorded_before_edits_utc=datetime.now(timezone.utc).isoformat(), started_local='2026-11-03T16:32:34.1889505+02:00', edits=edits), ensure_ascii=False, indent=2)+'\n',encoding='utf-8')
# The intended original/replacement/reason record exists before any manuscript mutation.
buffers={}
before={}
for e in edits:
    path=e['path']
    if path not in buffers:
        before[path]=(root/path).read_bytes()
        buffers[path]=before[path].decode('utf-8').replace('\r\n','\n')
    assert buffers[path].count(e['original'])==1, (path, e['original'][:85], buffers[path].count(e['original']))
    buffers[path]=buffers[path].replace(e['original'],e['replacement'],1)
for path,value in buffers.items():
    if b'\r\n' in before[path]:
        value=value.replace('\n','\r\n')
    (root/path).write_bytes(value.encode('utf-8'))
result=dict(completed_utc=datetime.now(timezone.utc).isoformat(),
            awake_time='unverified', checks='Exact original passage matched once before each edit; no builds or gates run.',
            files=[dict(path=p,sha256_before=hashlib.sha256(before[p]).hexdigest(),sha256_after=hashlib.sha256((root/p).read_bytes()).hexdigest()) for p in buffers])
(record.parent/'routes-methods-result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,ensure_ascii=False,indent=2))
