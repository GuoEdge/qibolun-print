#!/usr/bin/env python3
import csv
import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
R = ROOT / 'research-rebuild/reports'
D = ROOT / 'research-rebuild/data'
B = R / 'live-manual-short-batch-v2-round71-short50.csv'
F = R / 'round71-fulltext.json'
T = R / 'round71-decisions.tsv'
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
ids = [r['id'] for r in batch]
assert len(batch) == len(decisions) == len(full) == 50
assert len(ids) == len(set(ids)) == 50
assert ids == [r['id'] for r in full]
assert [r['title'] for r in batch] == [r['title'] for r in full] == [r['title'] for r in decisions]
assert not set(ids) & {r['id'] for r in manual}

out = []
for b, d in zip(batch, decisions):
    secondary = [x for x in d['secondary'].split(';') if x]
    assert d['primary'] in VALID and all(x in VALID for x in secondary)
    assert d['primary'] not in secondary and len(secondary) <= 3
    assert d['status'] in {'manual_confirmed', 'manual_provisional'} and d['basis'].strip()
    if int(b.get('deepseek_image_count') or 0):
        assert d['status'] == 'manual_provisional'
    out.append({
        'id': b['id'], 'title': b['title'],
        'primary_print_topic_code': d['primary'],
        'secondary_print_topic_codes': ';'.join(secondary),
        'classification_status': d['status'], 'decision_basis': d['basis'],
        'review_note': f'Round 71 full text; body_chars={b["body_char_count"]}; batch={B.name}',
        'reviewer': 'main-thread', 'reviewed_at': date.today().isoformat(),
    })
with M.open('a', encoding='utf-8-sig', newline='') as fh:
    csv.DictWriter(fh, fieldnames=fields, extrasaction='ignore').writerows(out)
print(json.dumps({
    'appended': len(out),
    'confirmed': sum(r['classification_status'] == 'manual_confirmed' for r in out),
    'provisional': sum(r['classification_status'] == 'manual_provisional' for r in out),
    'manual_total': len(manual) + len(out),
    'body_chars': sum(int(r['body_char_count']) for r in batch),
}, ensure_ascii=False, indent=2))
