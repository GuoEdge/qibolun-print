#!/usr/bin/env python3
import csv, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BATCH = ROOT / 'research-rebuild/reports/live-manual-short-batch-v2-round62-short50.csv'
CORPUS = ROOT / 'sooon-q9adg-articles-v2.jsonl'
OUT = ROOT / 'research-rebuild/reports/round62-fulltext.json'

def collect(node):
    if not isinstance(node, dict): return ''
    typ = node.get('type')
    if typ == 'text': return str(node.get('text') or '')
    if typ == 'linebreak': return '\n'
    return ''.join(collect(x) for x in node.get('children') or [])

batch = list(csv.DictReader(BATCH.open(encoding='utf-8-sig', newline='')))
want = {r['id']: r for r in batch}
found = {}
for line in CORPUS.open(encoding='utf-8'):
    row = json.loads(line)
    if row.get('id') not in want: continue
    lexical = row.get('lexical')
    if isinstance(lexical, str):
        try: lexical = json.loads(lexical)
        except json.JSONDecodeError: lexical = {}
    text = row.get('text') or collect((lexical or {}).get('root') or {})
    found[row['id']] = {'id': row['id'], 'title': row.get('title',''), 'text': text}
assert len(found) == len(batch) == 50
out = [found[r['id']] for r in batch]
assert [r['id'] for r in out] == [r['id'] for r in batch]
assert all(len(r['text']) <= int(b['body_char_count']) for r,b in zip(out,batch))
OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps({'records':len(out),'text_chars':sum(len(x['text']) for x in out),'max_chars':max(len(x['text']) for x in out)}, ensure_ascii=False))
