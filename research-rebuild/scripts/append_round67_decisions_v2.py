#!/usr/bin/env python3
import csv, json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
R = ROOT / 'research-rebuild/reports'
D = ROOT / 'research-rebuild/data'
B = R / 'live-manual-short-batch-v2-round67-short50.csv'
F = R / 'round67-fulltext.json'
T = R / 'round67-decisions.tsv'
M = D / 'print-topic-manual-decisions-v2.csv'
VALID = {f'A{i:02d}' for i in range(21)} | {'A00'}

def read_csv(path):
    with path.open(encoding='utf-8-sig', newline='') as fh:
        reader = csv.DictReader(fh)
        return list(reader.fieldnames or []), list(reader)

_, batch = read_csv(B)
fields, manual = read_csv(M)
with T.open(encoding='utf-8-sig', newline='') as fh:
    decisions = list(csv.DictReader(fh, delimiter='\t'))
full = json.loads(F.read_text(encoding='utf-8'))

batch_ids = [row['id'] for row in batch]
assert len(batch_ids) == len(set(batch_ids)) == 50
assert len(decisions) == len(full) == 50
assert batch_ids == [row['id'] for row in full]
assert len({row['title'] for row in decisions}) == 50
assert {row['title'] for row in batch} == {row['title'] for row in decisions}
assert not (set(batch_ids) & {row['id'] for row in manual})
by_title = {row['title']: row for row in decisions}
out = []
for row in batch:
    d = by_title[row['title']]
    secondary = [x for x in d['secondary'].split(';') if x]
    assert d['primary'] in VALID
    assert all(x in VALID for x in secondary)
    assert d['primary'] not in secondary and len(secondary) <= 3
    assert d['status'] in {'manual_confirmed', 'manual_provisional'}
    assert d['basis'].strip()
    out.append({
        'id': row['id'],
        'title': row['title'],
        'primary_print_topic_code': d['primary'],
        'secondary_print_topic_codes': ';'.join(secondary),
        'classification_status': d['status'],
        'decision_basis': d['basis'],
        'review_note': f'Round 67 full text; batch={B.name}',
        'reviewer': 'main-thread',
        'reviewed_at': date.today().isoformat(),
    })

with M.open('a', encoding='utf-8-sig', newline='') as fh:
    csv.DictWriter(fh, fieldnames=fields, extrasaction='ignore').writerows(out)
print(f'appended={len(out)} confirmed={sum(r["classification_status"] == "manual_confirmed" for r in out)} provisional={sum(r["classification_status"] == "manual_provisional" for r in out)} total={len(manual) + len(out)}')
