# -*- coding: utf-8 -*-
import json,csv,re,os
BASE='research-rebuild/reports/rebuild-20260926'; OUT=os.path.join(BASE,'round171')
ft={a['id']:a for a in json.load(open(os.path.join(OUT,'round171-fulltext.json'),encoding='utf-8'))}
reg={r['code'] for r in csv.DictReader(open('research-rebuild/data/print-topic-registry-v2.csv',encoding='utf-8'))}
sel=[r for r in csv.DictReader(open(os.path.join(OUT,'round171-selection.csv'),encoding='utf-8-sig'))]
aud=list(csv.DictReader(open(os.path.join(OUT,'round171-body-evidence-audit.tsv'),encoding='utf-8-sig'),delimiter='\t'))
dec=list(csv.DictReader(open(os.path.join(OUT,'round171-decisions.tsv'),encoding='utf-8-sig'),delimiter='\t'))
rev=list(csv.DictReader(open(os.path.join(OUT,'round171-revision-log.csv'),encoding='utf-8-sig')))
LEGAL={'source_empty','source_truncated','body_is_quotation','body_is_pointer','body_question_mismatch','body_too_short_for_center','a00_registry_gap'}
def norm(s): return re.sub(r'[\s"“”\'‘’]','',s)
ok=True
def rep(l,c,d=''):
    global ok
    if not c: ok=False
    print(('PASS' if c else 'FAIL'),l,d)
rep('audit 行数 == selection 行数',len(aud)==len(sel),f'{len(aud)} vs {len(sel)}')
rep('audit ID 集合 == selection ID 集合',{r['id'] for r in aud}=={r['id'] for r in sel})
rep('decisions ID 集合 == selection ID 集合',{r['id'] for r in dec}=={r['id'] for r in sel})
rep('decisions 与 audit 主副题一致',all(d['primary']==a['new_primary'] and d['secondary']==a['new_secondary'] for d,a in zip(sorted(dec,key=lambda x:x['id']),sorted(aud,key=lambda x:x['id']))))
bad=[]
for a in aud:
    q=norm(a['body_evidence_quote']); t=norm(ft[a['id']]['text']); best=0
    for x in range(len(q)):
        for y in range(len(q),x+best,-1):
            if q[x:y] in t:
                best=max(best,y-x); break
    if best<12: bad.append((a['title'],best))
rep('quote 去引号/空白后最长命中 ≥12 字（含引号/疑问句外观检查）',not bad,str(bad))
rep('quote 均为作者陈述句（不以问号结尾、非题面复述）',all(not a['body_evidence_quote'].rstrip().endswith(('？','?')) and a['body_evidence_quote'].strip() not in ft[a['id']]['question'] for a in aud))
rep('primary/secondary 均在 A00–A21',all(a['new_primary'] in reg and all(c in reg for c in a['new_secondary'].split(';') if c) for a in aud))
rep('primary 不在 secondary',all(a['new_primary'] not in a['new_secondary'].split(';') for a in aud))
rep('每篇恰好 1 个 primary',all(len([x for x in a['new_primary'].split(';') if x])==1 for a in aud))
rep('副专题 ≤3',all(len([c for c in a['new_secondary'].split(';') if c])<=3 for a in aud))
rep('provisional 行均填合法 blocking_reason',all((a['blocking_reason'] in LEGAL) for a in aud if a['new_status']=='manual_provisional'))
rep('confirmed 行 blocking_reason 为空',all(a['blocking_reason']=='' for a in aud if a['new_status']=='manual_confirmed'))
rep('reviewer/reviewed_at 统一',all(a['reviewer']=='subagent+round171-body-review' and a['reviewed_at']=='2026-09-26' for a in aud))
rep('revision-log 只含发生变化行',all(not (r['old_primary']==r['new_primary'] and r['old_secondary']==r['new_secondary'] and r['old_status']==r['new_status']) for r in rev),f'{len(rev)} 行')
rep('body_char_count 与 text 实际长度一致',all(int(a['body_char_count'])==len(ft[a['id']]['text']) for a in aud))
print('TOTAL_CHARS',sum(int(a['body_char_count']) for a in aud))
print('ALL', 'PASS' if ok else 'FAIL')
