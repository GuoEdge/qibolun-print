import csv
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
PATH=ROOT/'research-rebuild/data/print-topic-manual-decisions-v2.csv'
BATCH=ROOT/'research-rebuild/reports/live-manual-short-batch-v2-round53-short50.csv'
D={
'预警':('A07','A09;A01'),'好木匠':('A08','A16;A10'),'无效教育':('A05','A04;A19'),'反黑组':('A10','A16;A07'),'半纹龙':('A04','A03;A10'),'10000-10000':('A06','A02;A03'),'乃告父母':('A05','A02;A06'),'凡尔赛':('A07','A03;A16'),'未保护动物':('A18','A10;A08'),'多余的刺头':('A07','A10;A09'),'戒慎恐惧':('A03','A07;A01'),'魂不附体':('A06','A01;A03'),'牢骚':('A15','A16;A03'),'大砍刀':('A18','A16;A14'),'有钱要花':('A08','A04;A01'),'一意孤行的慈善':('A08','A15;A03'),'考军校':('A04','A12;A10'),'事业为重':('A07','A06;A08'),'强者道歉':('A07','A03;A06'),'高贵和优越':('A03','A01;A17'),'废寝忘食':('A01','A04;A09'),'过得好好':('A01','A06;A08'),'谈钱伤感情':('A06','A07;A16'),'威慑与威胁':('A03','A07;A10'),'透支户':('A06','A01;A02'),'前途上限':('A08','A04;A10'),'永垂不朽':('A20','A15;A12'),'客户、服务员和导师':('A07','A10;A03'),'老实板凳':('A07','A06;A03'),'自我中心':('A01','A03;A06'),'走钢丝的食神':('A04','A16;A07'),'不受采访':('A16','A17;A02'),'智慧的价值':('A03','A01;A07'),'世界越来越难':('A13','A04;A08'),'盗火线':('A07','A09;A10'),'变态':('A03','A06;A11'),'割地求和':('A03','A07;A06'),'我是学生':('A09','A01;A08'),'美式基础教育':('A04','A12;A17'),'完美航空':('A13','A07;A03'),'红拂夜奔':('A06','A08;A05'),'少年立志':('A04','A08;A01'),'染色之前':('A06','A08;A03'),'除了睡觉':('A01','A09;A11'),'有重量的自由':('A05','A08;A06'),'四门功课':('A04','A13;A01'),'身边的深刻':('A03','A16;A06'),'该死的张三':('A02','A06;A03'),'一纵一枉':('A16','A03;A07'),'高级回怼':('A07','A03;A06')}
batch=list(csv.DictReader(BATCH.open(encoding='utf-8-sig',newline='')))
assert len(batch)==50 and {r['title'] for r in batch}==set(D)
with PATH.open(encoding='utf-8-sig',newline='') as f:
 rd=csv.DictReader(f); rows=list(rd); fields=rd.fieldnames
by={r['id']:r for r in rows}
for r in batch:
 p,s=D[r['title']]
 by[r['id']]={'id':r['id'],'title':r['title'],'primary_print_topic_code':p,'secondary_print_topic_codes':s,'classification_status':'manual_confirmed','decision_basis':'Round 53 full-text review: '+r['title'],'review_note':'按lexical正文论证中心裁决；主副专题不重复。','reviewer':'main-thread','reviewed_at':'2026-09-23'}
with PATH.open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(by.values())
print('round53',len(batch),'manual_rows',len(by))
