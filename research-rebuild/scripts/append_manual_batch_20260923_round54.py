import csv
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; PATH=ROOT/'research-rebuild/data/print-topic-manual-decisions-v2.csv'; BATCH=ROOT/'research-rebuild/reports/live-manual-short-batch-v2-round54-short50.csv'
D={
'饶人魔法':('A10','A07;A12'),'爱无侥幸':('A06','A01;A02'),'非常突然':('A06','A01;A07'),'帮助明星':('A16','A08;A06'),'隐瞒债务':('A10','A06;A08'),'绕道而行':('A06','A07;A01'),'无能信仰':('A05','A08;A01'),'洁癖':('A02','A07;A08;A06'),'无需强大':('A06','A16;A12;A01'),'自由的实现':('A01','A10;A12;A18'),'少年沉迷':('A01','A04;A09'),'暗怕':('A01','A08;A06;A07'),'器官的组合':('A02','A06;A07'),'搬到加沙':('A05','A07;A10;A08'),'由华入美':('A12','A17;A03;A06'),'哈尔佛':('A11','A01;A10'),'温柔的魔鬼':('A07','A12;A06'),'the F grade':('A06','A01;A08'),'炼血成丹':('A06','A01;A10'),'纯手搓':('A06','A01;A15'),'重量级棋王':('A03','A15;A12'),'大棒pro':('A07','A04;A10'),'失恋的意义':('A06','A01;A03'),'地动仪':('A03','A13;A18;A20'),'六根雪糕':('A07','A08;A06'),'好照片':('A15','A03;A13;A18'),'一万粉':('A16','A15;A08'),'序号':('A18','A03;A11;A20'),'勉强无益':('A06','A07;A08'),'解决问题的态度':('A07','A10;A01'),'老无聊':('A05','A13;A09;A06'),'火鸡狂欢节':('A06','A01;A15'),'挣钱的知识':('A04','A08;A15'),'最佳事业':('A08','A07;A11;A16'),'今日无大事':('A01','A14;A06;A15'),'来者犹可鉴':('A10','A03;A07;A06'),'浅水区':('A06','A07;A15;A01'),'音频防弹衣':('A07','A04;A01;A06'),'不配得':('A08','A01;A07;A10'),'舒适禁区':('A01','A04;A15'),'傻强':('A07','A04;A10'),'对事的差距':('A07','A08;A04;A01'),'认真':('A01','A07;A04'),'最亲与最好':('A06','A07;A01'),'绸缪忧天':('A03','A16;A01;A18'),'强权和公义':('A12','A10;A17'),'值得付费':('A08','A07;A03;A16'),'表黑':('A06','A07;A15'),'两小无猜':('A06','A07;A01;A10'),'自尊者自信':('A01','A07;A04')}
batch=list(csv.DictReader(BATCH.open(encoding='utf-8-sig',newline=''))); assert len(batch)==50 and {r['title'] for r in batch}==set(D)
with PATH.open(encoding='utf-8-sig',newline='') as f: rd=csv.DictReader(f); rows=list(rd); fields=rd.fieldnames
by={r['id']:r for r in rows}
for r in batch:
 p,s=D[r['title']]; by[r['id']]={'id':r['id'],'title':r['title'],'primary_print_topic_code':p,'secondary_print_topic_codes':s,'classification_status':'manual_confirmed','decision_basis':'Round 54 full-text review: '+r['title'],'review_note':'按lexical正文论证中心裁决；主副专题不重复。','reviewer':'main-thread','reviewed_at':'2026-09-23'}
with PATH.open('w',encoding='utf-8-sig',newline='') as f: w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(by.values())
print('round54',len(batch),'manual_rows',len(by))
