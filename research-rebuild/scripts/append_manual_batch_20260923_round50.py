import csv
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
PATH=ROOT/'research-rebuild/data/print-topic-manual-decisions-v2.csv'
BATCH=ROOT/'research-rebuild/reports/live-manual-short-batch-v2-round50-short50.csv'
D={'偏袒陷阱':('A09','A03;A07'),'真爽':('A15','A10;A00'),'情绪大师':('A11','A02;A07'),'心猿':('A02','A00;A20'),'安全的诅咒':('A07','A11;A16'),'照骨镜':('A16','A13;A07'),'正常的歧视':('A03','A10;A07'),'无言以对':('A13','A04;A08'),'白羽毛':('A18','A12;A07'),'卡通表':('A15','A07;A08'),'山丘上的鱼鹰':('A10','A02;A00'),'慧眼识珠':('A08','A16;A10'),'最佳促销':('A03','A05;A09'),'邪魔外道':('A07','A12;A18'),'大教育家':('A05','A10;A02'),'吟诗作对':('A04','A02;A00'),'公什么关':('A07','A10;A08'),'历史的手续费':('A07','A02;A15'),'言不由衷':('A03','A07;A02'),'人的目的':('A00','A03;A07'),'睡前真经':('A02','A10;A04'),'感谢策略':('A03','A07;A05'),'行宫':('A08','A15;A13'),'先后爱':('A03','A00;A07'),'不想生':('A03','A09;A05'),'吃干与抹净':('A03','A05;A07'),'新手村之王':('A03','A00;A07'),'一点傲骨':('A05','A02;A07'),'大而细':('A12','A07;A09'),'不必勉强':('A03','A07;A00'),'偷油贼':('A11','A00;A03'),'大炼钢铁':('A07','A12;A02'),'lowpoly':('A02','A07;A11'),'婚姻底气':('A03','A15;A16'),'冤枉钱':('A15','A00;A02'),'缅北王':('A03','A07;A02'),'穷金':('A15','A00;A10'),'真假客套':('A03','A07;A02'),'肉公基':('A04','A10;A13'),'无要求抑郁':('A11','A05;A02'),'入门弓':('A13','A16;A04'),'从不休假':('A15','A10;A00'),'代客举手':('A02','A07;A11'),'道路以目':('A03','A07;A00'),'纪律抓手':('A08','A10;A07'),'money talks':('A07','A02;A10'),'工作冲突处置原则':('A08','A07;A10'),'小上帝的前女友':('A03','A02;A07'),'A VERY EDUCATED GUESS':('A03','A05;A02'),'私有不公':('A12','A09;A07')}
batch=list(csv.DictReader(BATCH.open(encoding='utf-8-sig',newline='')))
assert len(batch)==50 and {r['title'] for r in batch}==set(D)
with PATH.open(encoding='utf-8-sig',newline='') as f:
 rd=csv.DictReader(f); rows=list(rd); fields=rd.fieldnames
by={r['id']:r for r in rows}
for r in batch:
 p,s=D[r['title']]
 by[r['id']]={'id':r['id'],'title':r['title'],'primary_print_topic_code':p,'secondary_print_topic_codes':s,'classification_status':'manual_confirmed','decision_basis':'Round 50 full-text review: '+r['title'],'review_note':'正文中心明确，主副专题按论证中心裁决。','reviewer':'main-thread','reviewed_at':'2026-09-23'}
with PATH.open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(by.values())
print('round50',len(batch),'manual_rows',len(by))
