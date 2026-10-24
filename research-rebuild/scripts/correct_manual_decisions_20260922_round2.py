import csv
from pathlib import Path

path = Path(__file__).resolve().parents[1] / 'data' / 'print-topic-manual-decisions-v2.csv'
updates = {
    'b7783aac-09f8-5124-bd0f-03efe1ca23aa': {
        'classification_status': 'manual_provisional',
        'review_note': '正文足以支持 A03 主专题；原文含高尔顿钉板图片，图片尚未独立复核，保留 provisional',
    },
}
with path.open(encoding='utf-8-sig', newline='') as f:
    rows = list(csv.DictReader(f))
fields = list(rows[0]) if rows else []
changed = 0
for row in rows:
    if row['id'] in updates:
        before = tuple(row.get(k, '') for k in updates[row['id']])
        for key, value in updates[row['id']].items():
            row[key] = value
        after = tuple(row.get(k, '') for k in updates[row['id']])
        if before != after:
            changed += 1
with path.open('w', encoding='utf-8-sig', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)
print({'rows': len(rows), 'changed': changed})
