import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / 'research-rebuild/data/print-topic-manual-decisions-v2.csv'
BATCH = ROOT / 'research-rebuild/reports/live-manual-short-batch-v2-round47-short50.csv'

DECISIONS = {
 '西施':('A18','A04;A11'),'对错了':('A00','A04;A07'),'笨蛋':('A00','A04;A11'),'红A字':('A12','A07;A02'),'颈椎':('A13','A09;A08'),'一辉':('A00','A11;A20'),'非法改装':('A12','A07;A13'),'悲壮':('A12','A18;A02'),'宗教的价值':('A11','A00;A06'),'出于恐惧的仇恨':('A12','A11;A02'),'沙加':('A00','A04'),'核披萨':('A13','A10;A14'),'高差':('A15','A13;A08'),'Black Wallstreet':('A12','A02;A06'),'种族矛盾':('A12','A06;A11'),'具象建筑':('A15','A13;A00'),'正中心':('A14','A10;A20'),'3D打印':('A13','A15;A08'),'可见光通信':('A13','A10;A14'),'戒刀':('A11','A15;A00'),'锄禾日当午':('A15','A09;A11'),'树知道':('A16','A09;A13'),'速写':('A04','A15;A00'),'除胶计':('A08','A05;A13'),'塑料保鲜袋':('A13','A09;A10'),'无关之爱':('A06','A02;A11'),'软鼓':('A08','A07;A04'),'捧土成丘':('A09','A04;A10'),'过拟合':('A11','A04;A13'),'馆阁':('A15','A06;A11'),'无人机武士':('A07','A06;A02'),'逆行超车':('A07','A12;A16'),'性感与女王':('A02','A04;A11'),'生育恐怖主义':('A12','A06;A02'),'不可战胜的手工艺':('A13','A04;A08'),'没有简单':('A04','A13;A14'),'落后时代':('A13','A11;A04'),'AAL IZZ WELL':('A11','A04;A06'),'谁不像':('A15','A20;A11'),'最佳徒手圆':('A04','A13;A00'),'龙的传人':('A18','A09;A00'),'地狱骑士':('A09','A16;A13'),'惩戒的资格':('A05','A06;A11'),'时间轴平移':('A13','A12;A00'),'象牙手镯':('A18','A08;A06'),'房屋管理员':('A08','A13;A18'),'猫':('A15','A18;A09'),'观音快递':('A07','A05;A06'),'No Soup For You':('A07','A08;A04'),'左南右北':('A15','A13;A18')}

batch=list(csv.DictReader(BATCH.open(encoding='utf-8-sig',newline='')))
assert len(batch)==50 and set(r['title'] for r in batch)==set(DECISIONS), 'batch/title mismatch'
with PATH.open(encoding='utf-8-sig',newline='') as f:
    reader=csv.DictReader(f); rows=list(reader); fields=reader.fieldnames
by={r['id']:r for r in rows}
for r in batch:
    primary,secondary=DECISIONS[r['title']]
    by[r['id']]={'id':r['id'],'title':r['title'],'primary_print_topic_code':primary,'secondary_print_topic_codes':secondary,'classification_status':'manual_confirmed','decision_basis':'Round 47 full-text review: '+r['title'],'review_note':'正文中心明确，主副专题按论证中心裁决。','reviewer':'main-thread','reviewed_at':'2026-09-23'}
with PATH.open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(by.values())
print('round47',len(batch),'manual_rows',len(by))
