# -*- coding: utf-8 -*-
"""Independent re-verification of on-disk round167/round168 artifacts."""
import json, csv, os, re, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.abspath(os.path.join(BASE, '..', '..', '..'))
REG = {r['code'] for r in csv.DictReader(open(os.path.join(REPO,'research-rebuild','data','print-topic-registry-v2.csv'), encoding='utf-8-sig'))}
QUOTECH = '“”"\'‘’「」『』《》'
WS = re.compile(r'\s+')
def norm(s):
    for ch in QUOTECH: s = (s or '').replace(ch, '')
    return WS.sub('', s)
def lcs(a,b):
    best=0; prev=[0]*(len(b)+1)
    for i in range(1,len(a)+1):
        cur=[0]*(len(b)+1); ai=a[i-1]
        for j in range(1,len(b)+1):
            if ai==b[j-1]:
                cur[j]=prev[j-1]+1
                if cur[j]>best: best=cur[j]
        prev=cur
    return best
BLOCK_OK={'source_empty','source_truncated','body_is_quotation','body_is_pointer','body_question_mismatch','body_too_short_for_center','a00_registry_gap'}

allpass=True
for rnd in ['round167','round168']:
    rdir=os.path.join(BASE,rnd)
    arts={a['id']:a for a in json.load(open(os.path.join(rdir,f'{rnd}-fulltext.json'),encoding='utf-8'))}
    sel=list(csv.DictReader(open(os.path.join(rdir,f'{rnd}-selection.csv'),encoding='utf-8-sig')))
    aud=list(csv.DictReader(open(os.path.join(rdir,f'{rnd}-body-evidence-audit.tsv'),encoding='utf-8-sig'),delimiter='\t'))
    dec=list(csv.DictReader(open(os.path.join(rdir,f'{rnd}-decisions.tsv'),encoding='utf-8-sig'),delimiter='\t'))
    rev=list(csv.DictReader(open(os.path.join(rdir,f'{rnd}-revision-log.csv'),encoding='utf-8-sig')))
    res=[]
    # C1 quote
    f1=[]
    for r in aud:
        q=norm(r['body_evidence_quote']); t=norm(arts[r['id']]['text'])
        ok = len(q)>=12 and q in t and lcs(q,t)>=12
        if not ok: f1.append(r['title'])
    res.append(('C1 body_evidence_quote >=12 连续片段原文命中', not f1, f'{len(aud)-len(f1)}/{len(aud)}'+(' FAIL:'+','.join(f1) if f1 else '')))
    # C2 codes in registry
    f2=[r['title'] for r in aud if r['new_primary'] not in REG or any(c and c not in REG for c in (r['new_secondary'].split(';') if r['new_secondary'] else []))]
    res.append(('C2 primary/secondary 均在 A00-A21 内', not f2, f'{len(aud)-len(f2)}/{len(aud)}'+(' FAIL:'+','.join(f2) if f2 else '')))
    # C3 primary not in secondary
    f3=[r['title'] for r in aud if r['new_primary'] in (r['new_secondary'].split(';') if r['new_secondary'] else [])]
    res.append(('C3 primary 不出现在 secondary', not f3, ('PASS' if not f3 else 'FAIL:'+','.join(f3))))
    # C4 exactly one primary
    f4=[r['title'] for r in aud if len([c for c in r['new_primary'].split(';') if c])!=1]
    res.append(('C4 每篇恰好 1 个 primary', not f4, ('PASS' if not f4 else 'FAIL:'+','.join(f4))))
    # C5 row count + id set
    ids_a={r['id'] for r in aud}; ids_s={r['id'] for r in sel}; ids_d={r['id'] for r in dec}
    ok5 = len(aud)==len(sel)==len(dec) and ids_a==ids_s==ids_d
    res.append(('C5 行数与 ID 集合等于选择清单', ok5, f'audit={len(aud)} decisions={len(dec)} selection={len(sel)} ids_equal={ids_a==ids_s==ids_d}'))
    # C6 provisional blocking
    f6=[r['title'] for r in aud if r['new_status']=='manual_provisional' and r['blocking_reason'] not in BLOCK_OK]
    f6b=[r['title'] for r in aud if r['new_status']=='manual_confirmed' and r['blocking_reason']!='']
    res.append(('C6 暂定行 blocking_reason 合法（确认行为空）', not f6 and not f6b, f'provisional={sum(1 for r in aud if r["new_status"]=="manual_provisional")} violations={f6+f6b}'))
    # C7 consistency decisions vs audit
    dmap={r['id']:r for r in dec}
    f7=[r['title'] for r in aud if dmap[r['id']]['primary']!=r['new_primary'] or dmap[r['id']]['secondary']!=r['new_secondary'] or dmap[r['id']]['status']!=r['new_status']]
    res.append(('C7 decisions.tsv 与 audit 一致', not f7, ('PASS' if not f7 else 'FAIL:'+','.join(f7))))
    # C8 reviewed_at / reviewer
    f8=[r['title'] for r in aud if r['reviewed_at']!='2026-09-26' or r['reviewer']!=f'subagent+{rnd}-body-review']
    res.append(('C8 reviewed_at=2026-09-26 且 reviewer 标签正确', not f8, ('PASS' if not f8 else 'FAIL:'+','.join(f8))))
    # C9 revision-log only changed rows
    f9=[]
    for r in aud:
        ch = (r['old_primary'],r['old_secondary'],r['old_status'])!=(r['new_primary'],r['new_secondary'],r['new_status'])
        inrev = any(x['id']==r['id'] for x in rev)
        if ch!=inrev: f9.append(r['title'])
    res.append(('C9 revision-log 只含发生变化行且无遗漏', not f9, f'{len(rev)} rows'+(' FAIL:'+','.join(f9) if f9 else '')))
    print('='*20, rnd)
    for name, ok, detail in res:
        print(('PASS' if ok else 'FAIL'), '|', name, '|', detail)
        if not ok: allpass=False
print('OVERALL:', 'PASS' if allpass else 'FAIL')
