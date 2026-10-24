#!/usr/bin/env python3
import csv, json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
R = ROOT / 'research-rebuild/reports'
D = ROOT / 'research-rebuild/data'
B = R / 'live-manual-short-batch-v2-round66-short50.csv'
F = R / 'round66-fulltext.json'
T = R / 'round66-decisions.tsv'
M = D / 'print-topic-manual-decisions-v2.csv'

def read_csv(path):
    with path.open(encoding='utf-8-sig', newline='') as fh:
        reader = csv.DictReader(fh)
        return list(reader.fieldnames or []), list(reader)

_, batch = read_csv(B)
fields, manual = read_csv(M)
with T.open(encoding='utf-8-sig', newline='') as fh:
    decisions = list(csv.DictReader(fh, delimiter='\t'))
full = json.loads(F.read_text(encoding='utf-8'))

ids = [r['id'] for r in batch]
assert len(ids) == len(set(ids)) == 50
assert len(decisions) == len(full) == 50
assert ids == [r['id'] for r in full]
assert len({r['title'] for r in decisions}) == 50
assert {r['title'] for r in batch} == {r['title'] for r in decisions}
assert not set(ids) & {r['id'] for r in manual}

by_title = {r['title']: r for r in decisions}
out = []
for row in batch:
    decision = by_title[row['title']]
    secondary = [v for v in decision['secondary'].split(';') if v]
    assert decision['primary'] not in secondary and len(secondary) <= 3
    out.append({
        'id': row['id'],
        'title': row['title'],
        'primary_print_topic_code': decision['primary'],
        'secondary_print_topic_codes': ';'.join(secondary),
        'classification_status': decision['status'],
        'decision_basis': decision['basis'],
        'review_note': f'Round 66 full text; batch={B.name}',
        'reviewer': 'main-thread',
        'reviewed_at': date.today().isoformat(),
    })

with M.open('a', encoding='utf-8-sig', newline='') as fh:
    csv.DictWriter(fh, fieldnames=fields, extrasaction='ignore').writerows(out)
print(f'appended={len(out)} total={len(manual) + len(out)}')
