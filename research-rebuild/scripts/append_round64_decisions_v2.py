#!/usr/bin/env python3
import csv, json
from datetime import date
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
R=ROOT/'research-rebuild/reports'; D=ROOT/'research-rebuild/data'
B=R/'live-manual-short-batch-v2-round64-short50.csv'; F=R/'round64-fulltext.json'; T=R/'round64-decisions.tsv'; M=D/'print-topic-manual-decisions-v2.csv'
def read(path):
    with path.open(encoding='utf-8-sig',newline='') as f:
        x=csv.DictReader(f); return list(x.fieldnames or []),list(x)
_,batch=read(B); fields,manual=read(M)
dec=list(csv.DictReader(T.open(encoding='utf-8-sig',newline=''),delimiter='\t'))
full=json.loads(F.read_text(encoding='utf-8'))
assert len(batch)==len(dec)==len(full)==50
assert [x['id'] for x in batch]==[x['id'] for x in full]
assert not ({x['id'] for x in batch}&{x['id'] for x in manual})
by={x['title']:x for x in dec}; out=[]
for x in batch:
    d=by[x['title']]; sec=[v for v in d['secondary'].split(';') if v]
    assert d['primary'] not in sec and len(sec)<=3
    out.append({'id':x['id'],'title':x['title'],'primary_print_topic_code':d['primary'],
      'secondary_print_topic_codes':';'.join(sec),'classification_status':d['status'],
      'decision_basis':d['basis'],'review_note':f'Round 64 full text; batch={B.name}',
      'reviewer':'main-thread','reviewed_at':date.today().isoformat()})
with M.open('a',encoding='utf-8-sig',newline='') as f:
    csv.DictWriter(f,fieldnames=fields,extrasaction='ignore').writerows(out)
print(f'appended={len(out)} total={len(manual)+len(out)}')
