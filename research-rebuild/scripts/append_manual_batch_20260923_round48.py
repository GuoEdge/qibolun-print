import csv
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
PATH=ROOT/'research-rebuild/data/print-topic-manual-decisions-v2.csv'
BATCH=ROOT/'research-rebuild/reports/live-manual-short-batch-v2-round48-short50.csv'
D={
'赌神':('A02','A00;A07'),'硅胶干燥剂':('A13','A08;A15'),'淡定的许褚':('A16','A15;A08'),'七天无理由':('A03','A07;A05'),'苦中苦':('A00','A11;A04'),'极简悄悄话':('A15','A08;A04'),'分明的灰':('A15','A00;A04'),'小灵通':('A15','A13;A08'),'钓鱼背心':('A08','A15;A13'),'龟虽寿':('A20','A14;A00'),'Litttle Bang theory':('A13','A16;A00'),'大好人':('A07','A02;A16'),'黑粉菌':('A20','A14;A15'),'水豚君':('A11','A07;A00'),'修行实践':('A00','A07;A11'),'卵生大猩猩':('A12','A18;A07'),'劈柴':('A13','A08;A16'),'扩建医院':('A12','A16;A08'),'谣止于勤':('A16','A12;A09'),'渐行渐远':('A03','A11;A07'),'张艺谋想你':('A03','A07;A11'),'拍蒜':('A13','A16;A08'),'礼敬':('A07','A08;A05'),'独立调查':('A09','A12;A05'),'工程师路线':('A13','A08;A02'),'橡皮擦':('A00','A11;A07'),'头顶那个洞':('A13','A15;A08'),'摞你命3000':('A00','A11;A07'),'正当防卫门槛':('A09','A07;A16'),'伊斯兰女性':('A18','A07;A03'),'锄奸':('A12','A07;A18'),'写实':('A15','A04;A13'),'渔隐':('A18','A16;A00'),'MINECRAFT':('A00','A11;A07'),'雨伞':('A13','A08;A16'),'俄罗斯':('A18','A12;A00'),'悲欣交集':('A11','A00;A03'),'印刷信息量':('A13','A15;A08'),'浮桥':('A12','A13;A16'),'还魂丹':('A16','A20;A14'),'高粘液体':('A02','A07;A00'),'艺术文凭':('A04','A00;A15'),'防不胜防':('A16','A09;A07'),'小县城的未来':('A12','A08;A13'),'齐齐整整':('A13','A08;A00'),'FURY':('A00','A11;A07'),'不原谅的诅咒':('A05','A11;A07'),'不卑不亢':('A00','A15;A07'),'合谁的理':('A02','A00;A07'),'新手':('A16','A13;A09')}
batch=list(csv.DictReader(BATCH.open(encoding='utf-8-sig',newline='')))
assert len(batch)==50 and {r['title'] for r in batch}==set(D)
with PATH.open(encoding='utf-8-sig',newline='') as f:
 r=csv.DictReader(f); rows=list(r); fields=r.fieldnames
by={x['id']:x for x in rows}
for x in batch:
 p,s=D[x['title']]; by[x['id']]={'id':x['id'],'title':x['title'],'primary_print_topic_code':p,'secondary_print_topic_codes':s,'classification_status':'manual_confirmed','decision_basis':'Round 48 full-text review: '+x['title'],'review_note':'正文中心明确，主副专题按论证中心裁决。','reviewer':'main-thread','reviewed_at':'2026-09-23'}
with PATH.open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(by.values())
print('round48',len(batch),'manual_rows',len(by))
