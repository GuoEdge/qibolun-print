#!/usr/bin/env python3
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
R = ROOT / 'research-rebuild/reports'
ROUND = 70
B = R / f'live-manual-short-batch-v2-round{ROUND}-short50.csv'
F = R / f'round{ROUND}-fulltext.json'
C = ROOT / 'sooon-q9adg-articles-v2.jsonl'

def collect(node):
    if not isinstance(node, dict):
        return ''
    if node.get('type') == 'text':
        return str(node.get('text') or '')
    if node.get('type') == 'linebreak':
        return '\n'
    return ''.join(collect(child) for child in node.get('children') or [])

def main():
    global ROUND, B, F
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('--round', type=int, default=70)
    ap.add_argument('--batch', type=Path, default=None,
                    help='可选：显式指定本轮批次 CSV，以支持预算型批次。')
    args = ap.parse_args()
    ROUND = args.round
    B = args.batch or R / f'live-manual-short-batch-v2-round{ROUND}-short50.csv'
    F = R / f'round{ROUND}-fulltext.json'

    batch = list(csv.DictReader(B.open(encoding='utf-8-sig', newline='')))
    assert 1 <= len(batch) <= 50 and len({r['id'] for r in batch}) == len(batch)
    corpus = {}
    with C.open(encoding='utf-8') as fh:
        for line in fh:
            if line.strip():
                article = json.loads(line)
                corpus[article['id']] = article

    out = []
    for row in batch:
        article = corpus[row['id']]
        lexical = article.get('lexical')
        if isinstance(lexical, str):
            lexical = json.loads(lexical)
        body = article.get('text') or collect((lexical or {}).get('root') or {})
        assert len(body) == int(row['body_char_count'])
        out.append({
            'id': row['id'], 'title': article.get('title', row['title']),
            'question': article.get('question', row.get('question', '')),
            'text': body,
        })
    assert [r['id'] for r in out] == [r['id'] for r in batch]
    F.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps({'records': len(out), 'body_chars': sum(len(r['text']) for r in out),
                      'max_body_chars': max(len(r['text']) for r in out),
                      'output': str(F)}, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
