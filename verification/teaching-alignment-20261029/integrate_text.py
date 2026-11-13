"""Apply exact independently proposed edits after coordinator inspection.

This checks identity and overlap. It makes no editorial or acceptance judgments.
"""
from __future__ import annotations

import argparse
from datetime import datetime
import difflib
import hashlib
import json
from pathlib import Path
import yaml

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[1]


def digest(text: str) -> str:
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def yaml_scalar_nodes(node):
    if isinstance(node, yaml.ScalarNode):
        yield node
    elif isinstance(node, yaml.SequenceNode):
        for child in node.value:
            yield from yaml_scalar_nodes(child)
    elif isinstance(node, yaml.MappingNode):
        for _key, child in node.value:
            yield from yaml_scalar_nodes(child)


def prepare(report_paths: list[Path]):
    files, failures, sources = {}, [], []
    for report_path in report_paths:
        report = json.loads(report_path.read_text(encoding='utf-8-sig'))
        sources.append({'path': str(report_path), 'sha256': hashlib.sha256(report_path.read_bytes()).hexdigest()})
        for edit in report['proposed_edits']:
            relative = edit['source'].replace('\\', '/')
            path = (ROOT / relative).resolve()
            if not path.is_relative_to(ROOT) or not path.is_file():
                failures.append(f"{edit['id']}: invalid source {relative}")
                continue
            entry = files.setdefault(path, {'before': path.read_text(encoding='utf-8-sig'),
                                           'before_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
                                           'edits': []})
            original = edit['original']
            scalar_matches = []
            if path.suffix in ('.yaml', '.yml'):
                scalar_matches = [node for node in yaml_scalar_nodes(yaml.compose(entry['before']))
                                  if node.value == original]
            count = entry['before'].count(original) if original else 0
            if len(scalar_matches) == 1:
                node = scalar_matches[0]
                start, end = node.start_mark.index, node.end_mark.index
                replacement_raw = json.dumps(edit['replacement'], ensure_ascii=False)
            elif count == 1:
                start = entry['before'].index(original)
                end = start + len(original)
                replacement_raw = edit['replacement']
            else:
                failures.append(f"{edit['id']}: expected one exact original, found {count}")
                continue
            if any(start < existing['end'] and existing['start'] < end for existing in entry['edits']):
                failures.append(f"{edit['id']}: overlaps another proposed edit")
                continue
            entry['edits'].append({**edit, 'start': start, 'end': end,
                                  'replacement_raw': replacement_raw, 'report': str(report_path)})
    for path, entry in files.items():
        text = entry['before']
        for edit in sorted(entry['edits'], key=lambda value: value['start'], reverse=True):
            text = text[:edit['start']] + edit['replacement_raw'] + text[edit['end']:]
        entry['after'] = text
        entry['source'] = path.relative_to(ROOT).as_posix()
        entry['before_normalized_text_sha256'] = digest(entry['before'])
        entry['after_sha256'] = digest(text)
    return files, failures, sources


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('reports', nargs='+', type=Path)
    parser.add_argument('--apply', action='store_true')
    args = parser.parse_args()
    files, failures, sources = prepare(args.reports)
    record = {'at': datetime.now().astimezone().isoformat(), 'applied': False,
              'source_reports': sources, 'failures': failures,
              'changes': [{key: value for key, value in entry.items() if key not in ('before', 'after')}
                          for entry in files.values()]}
    diff = ''.join(''.join(difflib.unified_diff(entry['before'].splitlines(True),
                        entry['after'].splitlines(True), fromfile=entry['source'], tofile=entry['source']))
                   for entry in files.values())
    (OUT / 'proposed-text.diff').write_text(diff, encoding='utf-8')
    if args.apply and not failures:
        # Every file is validated before the first write. Keep baseline untouched.
        for path, entry in files.items():
            path.write_text(entry['after'], encoding='utf-8', newline='\n')
        record['applied'] = True
        record['applied_at'] = datetime.now().astimezone().isoformat()
    destination = OUT / ('integration.json' if record['applied'] else 'integration-preflight.json')
    destination.write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps({'applied': record['applied'], 'files': len(files),
                      'edits': sum(len(entry['edits']) for entry in files.values()), 'failures': failures}))
    return 1 if failures else 0


if __name__ == '__main__':
    raise SystemExit(main())
