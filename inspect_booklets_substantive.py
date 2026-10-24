#!/usr/bin/env python3
import json

with open('v1_full_reading_corpus.json', 'r', encoding='utf-8') as f:
    corpus = json.load(f)

by_booklet = {}
for c in corpus:
    by_booklet.setdefault(c['booklet_code'], []).append(c)

def inspect_booklet(bc, start=0, count=100):
    items = by_booklet.get(bc, [])
    print(f"=== {bc} ({items[0]['booklet_name'] if items else ''}) Total: {len(items)}, Showing {start} to {start+count} ===")
    for i, it in enumerate(items[start:start+count], start+1):
        q = it['question'].replace('\n', ' ')[:60]
        # first 120 chars of answer
        txt = it['text'].replace('\n', ' ')[:100]
        print(f"{i}. [{it['title']}] (ID: {it['id'][:8]})")
        print(f"   Q: {q}")
        print(f"   A: {txt}\n")

if __name__ == '__main__':
    import sys
    bc = sys.argv[1] if len(sys.argv) > 1 else 'B01'
    start = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    count = int(sys.argv[3]) if len(sys.argv) > 3 else 50
    inspect_booklet(bc, start, count)
