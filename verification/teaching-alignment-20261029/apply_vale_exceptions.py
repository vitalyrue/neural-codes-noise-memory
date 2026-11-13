"""Bind native Vale exceptions to actual reviewed alerts and current lines.

Unmatched errors remain pending. No rule, severity or raw lint result is changed.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from datetime import datetime
import difflib
import hashlib
import json
from pathlib import Path
import re

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[1]


def load(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def line_map(before, after):
    result = {}
    for tag, a, b, c, d in difflib.SequenceMatcher(None, before, after, autojunk=False).get_opcodes():
        if tag == 'equal' or (tag == 'replace' and b - a == d - c):
            result.update({old + 1: new + 1 for old, new in zip(range(a, b), range(c, d))})
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('current_report', type=Path)
    parser.add_argument('--additional', type=Path)
    parser.add_argument('--apply', action='store_true')
    args = parser.parse_args()
    report = load(args.current_report)
    indexed = defaultdict(list)
    records = []
    current_sources = {}
    for group in ('memory', 'eye', 'place'):
        inputs = {row['id']: row for row in load(OUT / f'{group}-vale-input.json')}
        review = load(OUT / f'{group}-stage2.json')
        records.append({'path': str(OUT / f'{group}-stage2.json'),
                        'sha256': sha(OUT / f'{group}-stage2.json'), 'call': review['call']})
        for decision in review['vale_decisions']:
            if decision['decision'] != 'retain_exception':
                continue
            old = inputs[decision['id']]
            source = old['source']
            if source not in current_sources:
                text = (ROOT / source).read_text(encoding='utf-8-sig')
                before = (OUT / 'baseline' / source).read_text(encoding='utf-8-sig')
                current_sources[source] = {'text': text, 'lines': text.splitlines(),
                    'line_map': line_map(before.splitlines(), text.splitlines())}
            number = current_sources[source]['line_map'].get(old['line'])
            if number is not None:
                indexed[(source, number, old['rule'], old['match'])].append({
                    'original_alert': old, 'decision': decision, 'reviewer_call': review['call']['run_id']})
    if args.additional:
        additional = load(args.additional)
        records.append({'path': str(args.additional), 'sha256': sha(args.additional), 'call': additional['call']})
        for decision in additional['decisions']:
            if decision['decision'] != 'retain_exception':
                continue
            source, number = decision['source'], decision['line']
            actual_line = current_sources[source]['lines'][number - 1]
            assert actual_line == decision['source_line'], (source, number, 'additional reviewed passage changed')
            indexed[(source, number, decision['rule'], decision['match'])].append({
                'original_alert': {'source': source, 'line': number, 'rule': decision['rule'], 'match': decision['match']},
                'decision': decision, 'reviewer_call': additional['call']['run_id'],
                'binding_note': 'Exact reviewed line verified; original review source hash remains in the unchanged decision record.'})
    accepted, pending, by_line = [], [], defaultdict(lambda: defaultdict(list))
    for file_name, alerts in report['raw'].items():
        path = Path(file_name).resolve()
        source = path.relative_to(ROOT).as_posix()
        for alert in alerts:
            if alert['Severity'] != 'error':
                continue
            key = (source, alert['Line'], alert['Check'], alert['Match'])
            matches = indexed.get(key, [])
            if not matches:
                pending.append({'source': source, 'alert': alert,
                    'source_line': path.read_text(encoding='utf-8-sig').splitlines()[alert['Line'] - 1]})
                continue
            comment_line = alert['Line']
            location_note = None
            if (source == 'content/chapters/03-memory-information.md' and alert['Line'] == 282
                    and alert['Check'] == 'ai-tells.SemicolonUsage' and alert['Match'] == '; pp.'):
                # The independent memory review explicitly located this native
                # diagnostic's reference separator at 278, not reported line 282.
                assert alert['Match'] in current_sources[source]['lines'][277]
                comment_line = 278
                location_note = 'Native Vale reports line 282; memory-stage2 independently identifies the actual source locator at line 278.'
            item = {'source': source, 'line_before_comments': comment_line,
                'current_alert': alert, 'reviewed_bindings': matches,
                'source_line': current_sources[source]['lines'][comment_line - 1],
                'diagnostic_location_note': location_note}
            accepted.append(item)
            by_line[source][comment_line].append(item)
    if args.apply:
        for source, lines in by_line.items():
            path = ROOT / source
            current = current_sources[source]
            if path.read_text(encoding='utf-8-sig') != current['text']:
                raise RuntimeError(f'Source changed after preparation: {source}')
            output = []
            for number, line in enumerate(current['lines'], 1):
                items = lines.get(number, [])
                rules = sorted({item['current_alert']['Check'] for item in items})
                match = re.match(r'^(\s*)(?:[-+*]|\d+[.)])\s+', line)
                indent = ' ' * len(match.group(0)) if match else ''
                for rule in rules:
                    output.append(f'{indent}<!-- vale {rule} = NO -->')
                output.append(line)
                for rule in reversed(rules):
                    output.append(f'{indent}<!-- vale {rule} = YES -->')
            path.write_text('\n'.join(output) + '\n', encoding='utf-8', newline='\n')
    ledger = {'at': datetime.now().astimezone().isoformat(), 'applied': args.apply,
        'current_report': str(args.current_report), 'current_report_sha256': sha(args.current_report),
        'config_sha256': report['metadata']['config_sha256'], 'review_records': records,
        'scope': 'Only identical rule/match alerts on mapped current lines; other errors remain pending.',
        'accepted_alerts': accepted, 'pending_errors': pending,
        'source_hashes': {source: sha(ROOT / source) for source in by_line}}
    destination = OUT / ('vale-exceptions.json' if args.apply else 'vale-exceptions-preflight.json')
    destination.write_text(json.dumps(ledger, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps({'applied': args.apply, 'bound_alerts': len(accepted), 'pending': len(pending),
                      'lines': sum(len(value) for value in by_line.values()), 'files': len(by_line)}))


if __name__ == '__main__':
    main()
