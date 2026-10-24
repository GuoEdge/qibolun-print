#!/usr/bin/env python3
"""Prepare Round123 text and fresh-image candidate lists only."""
from __future__ import annotations
import csv, json
from collections import defaultdict
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
REPORTS=ROOT/'research-rebuild/reports'; DATA=ROOT/'research-rebuild/data'
CORPUS=ROOT/'sooon-q9adg-articles-v2.jsonl'; MANUAL=DATA/'print-topic-manual-decisions-v2.csv'
INDEX=REPORTS/'article-classification-v2.csv'; INVENTORY=DATA/'image-inventory.csv'
TEXT_OUT=REPORTS/'round123-text-candidates.csv'; IMAGE_OUT=REPORTS/'round123-image-candidates.csv'

def read(path:Path):
    with path.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def write(path:Path, rows, fields):
    with path.open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');w.writeheader();w.writerows(rows)
def integer(v,default=0):
    try:return int(v or default)
    except (TypeError,ValueError):return default
def prior():
    ids=set();keys=set()
    for p in REPORTS.glob('round*-image-manifest*.csv'):
        for r in read(p):
            if r.get('id'):
                ids.add(r['id']);keys.add((r.get('id',''),r.get('image_index',''),r.get('src','')))
    return ids,keys

def main():
    corpus={}
    with CORPUS.open(encoding='utf-8') as f:
        for line in f:
            if line.strip():
                a=json.loads(line);corpus[str(a['id'])]=a
    manual={r['id']:r for r in read(MANUAL)}; index={r['id']:r for r in read(INDEX)}
    inventory=read(INVENTORY); groups=defaultdict(list)
    for r in inventory:groups[r['id']].append(r)
    prior_ids,prior_keys=prior()

    text=[]
    for aid,m in manual.items():
        if m.get('classification_status')!='manual_provisional':continue
        article=corpus.get(aid,{}); body=str(article.get('text') or '')
        if not body.strip():continue
        imgs=groups.get(aid,[])
        if imgs and any(r.get('status')!='reviewed' for r in imgs):continue
        ix=index.get(aid,{}); score=0; reasons=[]
        if ix.get('reading_status') in {'needs_reread','missing',''}:score+=50;reasons.append('needs_reread_or_missing')
        if integer(ix.get('primary_topic_tie_count'))>1:score+=30;reasons.append('candidate_tie')
        if integer(ix.get('primary_topic_candidate_score'),100)<70:score+=25;reasons.append('low_candidate_score')
        if 'unassigned' in ix.get('native_assignment_status','').lower():score+=15;reasons.append('official_unassigned')
        if not imgs:score+=15;reasons.append('no_image_dependency')
        if len(body)<700:score+=10;reasons.append('short_text')
        text.append({'ordinal':ix.get('ordinal',''),'id':aid,'title':article.get('title',m.get('title','')),
                     'body_char_count':str(len(body)),'image_count':str(len(imgs)),
                     'image_status':'none' if not imgs else 'all_reviewed',
                     'primary_print_topic_code':m.get('primary_print_topic_code',''),
                     'secondary_print_topic_codes':m.get('secondary_print_topic_codes',''),
                     'classification_status':m.get('classification_status',''),
                     'reading_status':ix.get('reading_status',''),'candidate_score':ix.get('primary_topic_candidate_score',''),
                     'selection_score':str(score),'selection_reasons':';'.join(reasons),
                     'selection_basis':'Round123 provisional text audit; text_present; no unreviewed image dependency; needs-reread/boundary risks ranked first.'})
    text.sort(key=lambda r:(-integer(r['selection_score']),integer(r['ordinal'],10**9),r['id']))
    text_eligible_count=len(text)
    text=text[:10];assert len(text)==10 and len({r['id'] for r in text})==10
    assert all(r['classification_status']=='manual_provisional' for r in text)
    write(TEXT_OUT,text,list(text[0]))

    fresh=[]
    for aid,rs in groups.items():
        if not rs or aid in prior_ids or not all(r.get('status')=='unreviewed' for r in rs):continue
        keys={(r.get('id',''),r.get('image_index',''),r.get('src','')) for r in rs}
        if keys & prior_keys:continue
        indices=sorted(integer(r.get('image_index')) for r in rs)
        if indices!=list(range(1,len(rs)+1)):continue
        fresh.append({'ordinal':str(integer(rs[0].get('ordinal'),10**9)),'id':aid,'title':rs[0].get('title',''),
                      'image_count':str(len(rs)),'classification_status':manual.get(aid,{}).get('classification_status',''),
                      'primary_print_topic_code':manual.get(aid,{}).get('primary_print_topic_code',''),
                      'selection_basis':'Round123 fresh complete unreviewed image group; article/image-key overlap with prior manifests excluded; dynamic 40-50 image budget.'})
    fresh.sort(key=lambda r:(-integer(r['image_count']),integer(r['ordinal'],10**9),r['id']))
    selected=[];total=0
    for r in fresh:
        n=integer(r['image_count'])
        if total+n<=50:selected.append(r);total+=n
        if total>=40:break
    assert 40<=total<=50 and len({r['id'] for r in selected})==len(selected)
    write(IMAGE_OUT,selected,list(selected[0]))
    print(json.dumps({'provisional_total':sum(r.get('classification_status')=='manual_provisional' for r in manual.values()),
      'text_pool_eligible':text_eligible_count,'text_selected':len(text),'text_chars':sum(integer(r['body_char_count']) for r in text),
      'fresh_groups':len(fresh),'image_selected':len(selected),'image_total':total,
      'image_status_counts':{s:sum(r['classification_status']==s for r in selected) for s in sorted({r['classification_status'] for r in selected})},
      'text_output':str(TEXT_OUT),'image_output':str(IMAGE_OUT)},ensure_ascii=False,indent=2))
if __name__=='__main__':main()
