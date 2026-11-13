"""Check source identity and coverage targets; does not accept teaching content."""
from pathlib import Path
import collections
import csv
import datetime
import hashlib
import json
import re
import yaml

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
inventory = list(csv.DictReader((ROOT / 'source-maps/source-inventory.csv').open(encoding='utf-8-sig')))
coverage = list(csv.DictReader((ROOT / 'source-maps/source-coverage.csv').open(encoding='utf-8-sig')))
manifest = yaml.safe_load((ROOT / 'sources/source-manifest.yaml').read_text())
anchors = set()
for path in (ROOT / 'content/chapters').glob('*.md'):
    anchors.update(re.findall(r'\{#((?:ch|sec):[^}\s]+)\}', path.read_text(encoding='utf-8')))

def missing_loci(rows, known):
    return [{'source_unit_id': row['source_unit_id'], 'target': value}
            for row in rows
            for value in re.findall(r'(?:ch|sec):[A-Z0-9_-]+', row['guide_locus'])
            if value not in known]

assert missing_loci([{'source_unit_id': 'planted', 'guide_locus': 'sec:MISSING'}], set()), 'negative-control failed'
identities = {}
for source in manifest['sources']:
    digest = hashlib.sha256((ROOT / source['path']).read_bytes()).hexdigest()
    identities[source['source_id']] = {'path': source['path'], 'sha256': digest, 'matches': digest == source['sha256']}
missing = missing_loci(coverage, anchors)
ids_match = collections.Counter(r['source_unit_id'] for r in inventory) == collections.Counter(r['source_unit_id'] for r in coverage)
report = {'checked_at': datetime.datetime.now().astimezone().isoformat(),
          'inventory_rows': len(inventory), 'coverage_rows': len(coverage), 'source_ids_match': ids_match,
          'dispositions': dict(collections.Counter(r['disposition'] for r in coverage)),
          'missing_targets': missing, 'sources': identities,
          'negative_control': 'missing guide target detected',
          'scope': 'Identity and target existence only. Reviewer source/claim judgments establish teaching adequacy.'}
report['status'] = 'pass' if ids_match and not missing and all(s['matches'] for s in identities.values()) else 'fail'
(OUT / 'source-identity-and-targets.json').write_text(json.dumps(report, indent=2), encoding='utf-8')
print(json.dumps({key: value for key, value in report.items() if key != 'sources'}, indent=2))
