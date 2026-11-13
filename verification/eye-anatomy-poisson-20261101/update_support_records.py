"""Add only the support records for the requested eye/Poisson revision."""
from pathlib import Path
import csv
import re

ROOT = Path(__file__).resolve().parents[2]
glossary = ROOT / 'content/chapters/glossary.md'
text = glossary.read_text(encoding='utf-8')
terms = {
    'elasticity': 'The tendency of stretched muscles and surrounding tissues to exert restoring forces.',
    'extraocular muscles': 'The six muscles attached to the outside of each eyeball that control its orientation.',
    'inertia': 'Resistance to a change in motion. Rotational inertia relates torque to angular acceleration; it does not supply a stationary holding torque.',
    'plasticity': 'A lasting, experience-dependent change in neural responses or connections. In gaze control it can change how well the holding circuit is calibrated.',
    'saccade': 'A rapid eye movement that changes gaze direction.',
    'tonic firing': 'Sustained neural firing during a holding period; the spike times need not be perfectly periodic.',
    'torque': 'The turning effect of a force.',
    'viscosity': 'Mechanical resistance to motion that dissipates energy. It damps movement but supplies no holding torque at zero velocity.',
}
for term, definition in sorted(terms.items()):
    if f'**{term}:**' in text:
        continue
    entry = f'- [[**{term}:**]{{.definition-term custom-style="Definition Term"}} {definition}]{{.definition-explanation}}\n'
    candidates = list(re.finditer(r'^- \[\[\*\*([^:]+):\*\*', text, re.M))
    after = next((m for m in candidates if m.group(1).lower() > term), None)
    if after:
        text = text[:after.start()] + entry + text[after.start():]
    else:
        text = text.rstrip() + '\n' + entry
glossary.write_text(text, encoding='utf-8')

refs = ROOT / 'content/chapters/references.md'
text = refs.read_text(encoding='utf-8')
if 'MITRES_6_012S18_L22.pdf' not in text:
    text = re.sub(r'^(\d+)\.', lambda m: f'{int(m[1])+5}.' if int(m[1]) >= 7 else m[0], text, flags=re.M)
    text = re.sub(r'entry (\d+)', lambda m: f'entry {int(m[1])+5}' if int(m[1]) >= 7 else m[0], text)
    new = r'''7. Massachusetts Institute of Technology, OpenCourseWare. (2018). *Introduction to probability: Lecture 22 notes, the Poisson process*. [Notes, pp. 3–5](https://ocw.mit.edu/courses/res-6-012-introduction-to-probability-spring-2018/d92a00a2bc9d20d84ad11d43be0e7ae0_MITRES_6_012S18_L22.pdf#page=3). The guide uses $r$ for rate and $\lambda=r\Delta t$ for expected count.

8. Dragoi, V. (2026, July 7, last review). *Ocular motor control*. In *Neuroscience Online*, Section 3, Chapter 8. McGovern Medical School, UTHealth Houston. [Sections 8.2–8.3](https://nba.uth.tmc.edu/neuroscience/m/s3/chapter08.html). Anatomy and visual/vestibular control background.

9. Anderson, S. R.; Porrill, J.; Sklavos, S.; Gandhi, N. J.; Sparks, D. L.; Dean, P. (2009). *Dynamics of primate oculomotor plant revealed by effects of abducens microstimulation*. Journal of Neurophysiology, 101(6), 2907–2923. [DOI](https://doi.org/10.1152/jn.91045.2008). Mechanical filtering and the limits of simple linear models.

10. Major, G.; Baker, R.; Aksay, E.; Mensh, B.; Seung, H. S.; Tank, D. W. (2004). *Plasticity and tuning by visual feedback of the stability of a neural integrator*. Proceedings of the National Academy of Sciences, 101(20), 7739–7744. [DOI](https://doi.org/10.1073/pnas.0401970101). Fig. 1 for movement and holding signals; Figs. 2–4 for training in goldfish.

11. Cannon, S. C.; Robinson, D. A. (1987). *Loss of the neural integrator of the oculomotor system from brain stem lesions in monkey*. Journal of Neurophysiology, 57(5), 1383–1409. [DOI](https://doi.org/10.1152/jn.1987.57.5.1383). Reversible disruption and its effect on gaze persistence in darkness.

'''
    # Keep the existing Vale scope attached to the Seung entry.
    pos = text.index('   <!-- vale ai-tells.EmDashUsage = NO -->\n12. Seung')
    text = text[:pos] + new + text[pos:]
    refs.write_text(text, encoding='utf-8')

sources = [
    ('BG-POISSON-MIT', 'MIT OpenCourseWare (2018), Lecture 22: the Poisson process', 'https://ocw.mit.edu/courses/res-6-012-introduction-to-probability-spring-2018/d92a00a2bc9d20d84ad11d43be0e7ae0_MITRES_6_012S18_L22.pdf', '2018', 'PDF pp. 3–5', 'sec:FOUNDATIONS-POISSON', 'Independent short time bins give the Poisson count law; guide notation distinguishes rate from expected count.', 'poisson-stage3.json'),
    ('BG-EYE-ANATOMY', 'Dragoi, Ocular motor control', 'https://nba.uth.tmc.edu/neuroscience/m/s3/chapter08.html', '2026-07-07 (last review)', 'Sections 8.2–8.3; Fig. 8.1', 'sec:PERSISTENCE-EYE-MECHANICS', 'Six extraocular muscles, cranial nerves III IV VI, and visual/vestibular contributions to eye control.', 'eye-stage3.json'),
    ('BG-EYE-MECHANICS', 'Anderson et al. (2009), Dynamics of primate oculomotor plant', 'https://doi.org/10.1152/jn.91045.2008', '2009', 'Introduction p. 2907; stimulation and relaxation results', 'sec:PERSISTENCE-EYE-MECHANICS', 'Viscous and elastic effects dominate inertia; muscle activation has lasting and nonlinear effects. The linear torque equation is a guide approximation.', 'eye-stage3.json'),
    ('BG-EYE-PLASTICITY', 'Major et al. (2004), Plasticity and tuning by visual feedback', 'https://doi.org/10.1073/pnas.0401970101', '2004', 'Fig. 1; Figs. 2–4; Discussion', 'sec:PERSISTENCE-EYE-MECHANICS', 'Pulse and sustained holding drive; altered visual feedback trains goldfish gaze holding over tens of minutes to hours, without identifying the cellular learning rule.', 'eye-stage3.json'),
    ('BG-EYE-INTEGRATOR', 'Cannon and Robinson (1987), Loss of the neural integrator', 'https://doi.org/10.1152/jn.1987.57.5.1383', '1987', 'Abstract, points 1–2', 'sec:PERSISTENCE-EYE-MECHANICS', 'After reversible brainstem disruption in monkeys, horizontal gaze-holding time constants fall from over 20 s to about 0.2 s in darkness.', 'eye-stage3.json'),
]
for filename in ('source-inventory.csv', 'source-coverage.csv', 'research-ledger.csv'):
    path = ROOT / 'source-maps' / filename
    with path.open(encoding='utf-8-sig', newline='') as stream:
        reader = csv.DictReader(stream)
        fields, rows = reader.fieldnames, list(reader)
    for order, (sid, title, url, date, locator, locus, claim, review) in enumerate(sources, 1):
        key = 'claim_id' if filename == 'research-ledger.csv' else 'source_unit_id'
        if any(row[key] == sid for row in rows):
            continue
        row = dict.fromkeys(fields, '')
        row.update({k:v for k,v in {
            'source_unit_id': sid, 'source_id': sid, 'source_path': url,
            'unit_locator': locator, 'presentation_order': str(order),
            'unit_type': 'background teaching source' if order <= 2 else 'primary research excerpt',
            'title': title, 'text_preview': claim, 'disposition': 'covered',
            'guide_locus': locus, 'rationale': claim,
            'writer_evidence': 'verification/eye-anatomy-poisson-20261101/RESULTS.md',
            'review_status': 'pending final scoped review', 'week': 'self-paced',
            'teaching_value': claim, 'reason': 'Requested background for the eye mechanism and Poisson derivation',
            'reviewer': '/root/poisson_review' if order == 1 else '/root/eye_mechanics_sources',
            'review_evidence': 'verification/eye-anatomy-poisson-20261101/' + review,
            'claim_id': sid, 'claim': claim, 'source_title': title, 'source_url': url,
            'publication_or_version_date': date, 'access_date': '2026-11-01',
            'guide_location': locus, 'status': 'truth reviewed; remaining stages pending',
            'notes': locator + '; only this source unit is newly assessed, not the whole publication',
        }.items() if k in fields})
        rows.append(row)
    with path.open('w', encoding='utf-8', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    print(f'{filename}: {len(rows)} rows')
print('Added eight glossary terms and five reference entries; existing references retained.')
