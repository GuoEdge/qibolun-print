#!/usr/bin/env python3
import csv,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; B=ROOT/'research-rebuild/reports/live-manual-short-batch-v2-round64-short50.csv'; C=ROOT/'sooon-q9adg-articles-v2.jsonl'; O=ROOT/'research-rebuild/reports/round64-fulltext.json'
def collect(n):
    if not isinstance(n,dict): return ''
    if n.get('type')=='text': return str(n.get('text') or '')
    if n.get('type')=='linebreak': return '\n'
    return ''.join(collect(c) for c in n.get('children') or [])
b=list(csv.DictReader(B.open(encoding='utf-8-sig',newline=''))); ids={x['id'] for x in b}; found={}
for line in C.open(encoding='utf-8'):
    r=json.loads(line)
    if r.get('id') not in ids: continue
    lex=r.get('lexical')
    if isinstance(lex,str):
        try: lex=json.loads(lex)
        except json.JSONDecodeError: lex={}
    found[r['id']]={'id':r['id'],'title':r.get('title',''),'text':r.get('text') or collect((lex or {}).get('root') or {})}
assert len(found)==50
out=[found[x['id']] for x in b]; assert all(len(x['text'])<=int(y['body_char_count']) for x,y in zip(out,b))
O.write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8'); print(len(out),sum(len(x['text']) for x in out),max(len(x['text']) for x in out))
