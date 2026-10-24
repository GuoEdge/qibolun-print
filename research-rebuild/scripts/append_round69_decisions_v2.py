#!/usr/bin/env python3
import csv, json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
R = ROOT / 'research-rebuild/reports'
D = ROOT / 'research-rebuild/data'
B = R / 'live-manual-risk-batch-v2-round69-30k.csv'
F = R / 'round69-fulltext.json'
T = R / 'round69-decisions.tsv'
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
ids = [row['id'] for row in batch]
assert 1 <= len(ids) <= 20 and len(ids) == len(set(ids))
assert len(decisions) == len(full) == len(ids)
assert ids == [row['id'] for row in full]
assert {row['title'] for row in batch} == {row['title'] for row in decisions}
assert len({row['title'] for row in decisions}) == len(decisions)
assert not set(ids) & {row['id'] for row in manual}
by_title = {row['title']: row for row in decisions}
out = []
for row in batch:
    d = by_title[row['title']]
    secondary = [x for x in d['secondary'].split(';') if x]
    assert d['primary'] in VALID and all(x in VALID for x in secondary)
    assert d['primary'] not in secondary and len(secondary) <= 3
    assert d['status'] == 'manual_provisional'
    assert d['basis'].strip()
    out.append({
        'id': row['id'], 'title': row['title'],
        'primary_print_topic_code': d['primary'],
        'secondary_print_topic_codes': ';'.join(secondary),
        'classification_status': d['status'], 'decision_basis': d['basis'],
        'review_note': f'Round 69 full text; image_count={row["deepseek_image_count"]}; image review pending',
        'reviewer': 'main-thread', 'reviewed_at': date.today().isoformat(),
    })
with M.open('a', encoding='utf-8-sig', newline='') as fh:
    csv.DictWriter(fh, fieldnames=fields, extrasaction='ignore').writerows(out)
print(f'appended={len(out)} provisional={len(out)} total={len(manual) + len(out)}')
