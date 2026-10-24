import csv
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; PATH=ROOT/'research-rebuild/data/print-topic-manual-decisions-v2.csv'; BATCH=ROOT/'research-rebuild/reports/live-manual-short-batch-v2-round58-short50.csv'
D={
'一般轨迹':('A06','A11'),'撞死羊':('A11','A10;A12'),'慧极型必伤':('A01','A03'),'知足常胜':('A01','A08'),'同意无效':('A01','A11;A03'),'ai轻应用':('A14','A15'),'事实黑':('A03','A06'),'热爱的福利':('A04','A07;A15'),'接班第一':('A07','A20'),'隐秘的雄心':('A01','A07;A16'),'恐艾':('A06','A09;A02'),'取决于谁':('A07','A08'),'最多辞职':('A07','A01;A10'),'均衡操作':('A01',''),'痒痒豆':('A06','A01'),'和氏传奇':('A12','A08;A13'),'自来水上瘾':('A16','A01'),'具体的典狱长':('A11','A05;A07'),'安内必先攘外':('A06','A08'),'gap':('A07','A04'),'亚里士多德':('A20','A03;A15'),'见好就收':('A08','A16;A12'),'错上错':('A07','A04;A03'),'第二十五':('A01','A03;A06'),'草台班子':('A07','A20'),'历史笑柄':('A01','A16;A20'),'境界起点':('A15','A20'),'无利可图':('A08','A13;A12'),'以少胜多':('A02','A06;A08;A16'),'苍蝇切':('A03','A18'),'可维之权':('A10','A07'),'情理难融':('A06','A17'),'接受加班':('A10','A07'),'关于问题的问题':('A03','A16'),'以盾为剑':('A07','A11'),'鬼佬':('A20','A17;A12'),'丧气话':('A17','A16;A01'),'不绝望的功夫':('A01','A04'),'神性':('A11','A03;A02'),'诽谤斗争':('A03','A16'),'饿死':('A09','A18'),'妖道':('A11','A18'),'效率之王':('A07','A08'),'手刹':('A01','A03;A07'),'吹哨人':('A07','A01;A03'),'知见咒':('A04','A20;A01'),'十年太守':('A06','A10'),'帝王蟹':('A04','A08'),'老而不语':('A08','A03;A20'),'三秘卷':('A08','A06;A11')}
batch=list(csv.DictReader(BATCH.open(encoding='utf-8-sig',newline=''))); assert len(batch)==50 and {r['title'] for r in batch}==set(D)
with PATH.open(encoding='utf-8-sig',newline='') as f: rd=csv.DictReader(f); rows=list(rd); fields=rd.fieldnames
by={r['id']:r for r in rows}
for r in batch:
 p,s=D[r['title']]; by[r['id']]={'id':r['id'],'title':r['title'],'primary_print_topic_code':p,'secondary_print_topic_codes':s,'classification_status':'manual_confirmed','decision_basis':'Round 58 full-text review: '+r['title'],'review_note':'按 lexical 正文论证中心裁决；副专题仅记录正文支持的交叉议题。','reviewer':'main-thread','reviewed_at':'2026-09-23'}
with PATH.open('w',encoding='utf-8-sig',newline='') as f: w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(by.values())
print('round58',len(batch),'manual_rows',len(by))
