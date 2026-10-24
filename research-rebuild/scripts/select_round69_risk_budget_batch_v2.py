#!/usr/bin/env python3
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORTS = ROOT / 'research-rebuild/reports'
QUEUE = REPORTS / 'live-manual-classification-queue-v2.csv'
MANUAL = ROOT / 'research-rebuild/data/print-topic-manual-decisions-v2.csv'
CORPUS = ROOT / 'sooon-q9adg-articles-v2.jsonl'
BATCH = REPORTS / 'live-manual-risk-batch-v2-round69-30k.csv'
FULLTEXT = REPORTS / 'round69-fulltext.json'
TARGET_CHARS = 30_000
MAX_RECORDS = 20

def read_csv(path: Path):
    with path.open(encoding='utf-8-sig', newline='') as fh:
        reader = csv.DictReader(fh)
        return list(reader.fieldnames or []), list(reader)

def collect(node) -> str:
    if not isinstance(node, dict):
        return ''
    if node.get('type') == 'text':
        return str(node.get('text') or '')
    if node.get('type') == 'linebreak':
        return '\n'
    return ''.join(collect(child) for child in node.get('children') or [])

_, queue = read_csv(QUEUE)
_, manual = read_csv(MANUAL)
manual_ids = {row['id'] for row in manual}
with CORPUS.open(encoding='utf-8') as fh:
    corpus = {row['id']: row for row in (json.loads(line) for line in fh if line.strip())}

selected = []
total_chars = 0
for row in queue:
    article = corpus[row['id']]
    lexical = article.get('lexical')
    if isinstance(lexical, str):
        try:
            lexical = json.loads(lexical)
        except json.JSONDecodeError:
            lexical = {}
    body = article.get('text') or collect((lexical or {}).get('root') or {})
    count = len(body)
    if not count or int(row.get('deepseek_image_count') or 0) <= 0:
        continue
    if len(selected) >= MAX_RECORDS or total_chars + count > TARGET_CHARS:
        break
    selected.append({
        'priority': row['priority'],
        'priority_reasons': row['priority_reasons'],
        'source_ordinal': row['source_ordinal'],
        'id': row['id'],
        'title': article.get('title', row.get('title', '')),
        'question': article.get('question', ''),
        'published_date': row.get('published_date', ''),
        'body_char_count': count,
        'candidate_primary': row.get('candidate_primary', ''),
        'candidate_secondary': row.get('candidate_secondary', ''),
        'official_assignment_status': row.get('official_assignment_status', ''),
        'official_category_paths': row.get('official_category_paths', ''),
        'deepseek_reading_status': row.get('deepseek_reading_status', ''),
        'deepseek_image_count': row.get('deepseek_image_count', ''),
    })
    total_chars += count

ids = [row['id'] for row in selected]
assert ids and len(ids) == len(set(ids)) and not set(ids) & manual_ids
with BATCH.open('w', encoding='utf-8-sig', newline='') as fh:
    writer = csv.DictWriter(fh, fieldnames=list(selected[0]))
    writer.writeheader()
    writer.writerows(selected)

fulltext = []
for row in selected:
    article = corpus[row['id']]
    lexical = article.get('lexical')
    if isinstance(lexical, str):
        try:
            lexical = json.loads(lexical)
        except json.JSONDecodeError:
            lexical = {}
    text = article.get('text') or collect((lexical or {}).get('root') or {})
    assert len(text) == int(row['body_char_count'])
    fulltext.append({
        'id': row['id'], 'title': row['title'], 'question': row['question'],
        'text': text, 'image_count': int(row['deepseek_image_count']),
    })
assert len(fulltext) == len(selected)
FULLTEXT.write_text(json.dumps(fulltext, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps({
    'records': len(selected), 'body_chars': total_chars,
    'max_body_chars': max(len(row['text']) for row in fulltext),
    'image_refs': sum(row['image_count'] for row in fulltext),
    'titles': [row['title'] for row in selected],
    'manual_overlap': len(set(ids) & manual_ids),
}, ensure_ascii=False, indent=2))
