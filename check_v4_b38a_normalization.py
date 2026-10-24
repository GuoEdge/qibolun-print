import json
from pathlib import Path

BASE = Path('research-rebuild/reports/gemini-flash-reclassification-v1')
CAT_FILE = BASE / 'workbook-40b-all-catalog-v4.jsonl'

v4_b38a_titles = []
with open(CAT_FILE) as f:
    for line in f:
        if not line.strip(): continue
        x = json.loads(line)
        if x.get('volume_code') == 'V4' and x.get('booklet_code') == 'B38A':
            v4_b38a_titles.append(x['title'])

print(f"Total V4 with booklet_code B38A: {len(v4_b38a_titles)}")
print(v4_b38a_titles)
