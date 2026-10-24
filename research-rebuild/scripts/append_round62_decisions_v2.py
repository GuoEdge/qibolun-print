#!/usr/bin/env python3
import csv, json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
R = ROOT / 'research-rebuild/reports'
D = ROOT / 'research-rebuild/data'
B = R / 'live-manual-short-batch-v2-round62-short50.csv'
F = R / 'round62-fulltext.json'
T = R / 'round62-decisions.tsv'
M = D / 'print-topic-manual-decisions-v2.csv'

def read(p):
    with p.open(encoding='utf-8-sig', newline='') as f:
        x = csv.DictReader(f)
        return list(x.fieldnames or []), list(x)

bf, batch = read(B)
mf, manual = read(M)
decisions = list(csv.DictReader(T.open(encoding='utf-8-sig', newline=''), delimiter='\t'))
full = json.loads(F.read_text(encoding='utf-8'))
assert len(batch) == len(decisions) == len(full) == 50
assert [x['id'] for x in batch] == [x['id'] for x in full]
assert not ({x['id'] for x in batch} & {x['id'] for x in manual})
by_title = {x['title']: x for x in decisions}
out = []
for item in batch:
    d = by_title[item['title']]
    secondary = [z for z in d['secondary'].split(';') if z]
    assert d['primary'] not in secondary and len(secondary) <= 3
    out.append({
        'id': item['id'], 'title': item['title'],
        'primary_print_topic_code': d['primary'],
        'secondary_print_topic_codes': ';'.join(secondary),
        'classification_status': d['status'],
        'decision_basis': d['basis'],
        'review_note': f"Round 62 full text; batch={B.name}",
        'reviewer': 'main-thread', 'reviewed_at': date.today().isoformat(),
    })
with M.open('a', encoding='utf-8-sig', newline='') as f:
    csv.DictWriter(f, fieldnames=mf, extrasaction='ignore').writerows(out)
print(f'appended={len(out)} total={len(manual)+len(out)}')
