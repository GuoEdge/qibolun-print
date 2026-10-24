#!/usr/bin/env python3
import csv, json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
R = ROOT / 'research-rebuild/reports'
D = ROOT / 'research-rebuild/data'
B = R / 'live-manual-short-batch-v2-round63-short50.csv'
F = R / 'round63-fulltext.json'
T = R / 'round63-decisions.tsv'
M = D / 'print-topic-manual-decisions-v2.csv'

def read(p):
    with p.open(encoding='utf-8-sig', newline='') as f:
        q = csv.DictReader(f)
        return list(q.fieldnames or []), list(q)

_, batch = read(B)
fields, manual = read(M)
dec = list(csv.DictReader(T.open(encoding='utf-8-sig', newline=''), delimiter='\t'))
full = json.loads(F.read_text(encoding='utf-8'))
assert len(batch) == len(dec) == len(full) == 50
assert [x['id'] for x in batch] == [x['id'] for x in full]
assert not ({x['id'] for x in batch} & {x['id'] for x in manual})
by_title = {x['title']: x for x in dec}
out = []
for item in batch:
    d = by_title[item['title']]
    sec = [z for z in d['secondary'].split(';') if z]
    assert d['primary'] not in sec and len(sec) <= 3
    out.append({'id': item['id'], 'title': item['title'],
                'primary_print_topic_code': d['primary'],
                'secondary_print_topic_codes': ';'.join(sec),
                'classification_status': d['status'],
                'decision_basis': d['basis'],
                'review_note': f'Round 63 full text; batch={B.name}',
                'reviewer': 'main-thread', 'reviewed_at': date.today().isoformat()})
with M.open('a', encoding='utf-8-sig', newline='') as f:
    csv.DictWriter(f, fieldnames=fields, extrasaction='ignore').writerows(out)
print(f'appended={len(out)} total={len(manual)+len(out)}')
