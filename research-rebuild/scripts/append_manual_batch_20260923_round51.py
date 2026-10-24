import csv
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
PATH=ROOT/'research-rebuild/data/print-topic-manual-decisions-v2.csv'
BATCH=ROOT/'research-rebuild/reports/live-manual-short-batch-v2-round51-short50.csv'
D={'爱在珍珠港':('A03','A00;A07'),'强电近地':('A13','A16;A08'),'谁来同情':('A11','A00;A02'),'真人不语':('A07','A02;A03'),'漫堤之日':('A03','A07;A05'),'不锈钢毛巾':('A13','A15;A04'),'邋遢的黄蓉':('A07','A02;A15'),'正义交替':('A09','A07;A00'),'四不值':('A12','A07;A15'),'大法庭':('A12','A07;A11'),'龙穴金':('A05','A02;A00'),'左撇子':('A04','A05;A02'),'学的必要':('A02','A00;A10'),'渗啥透':('A12','A07;A18'),'寡人有疾':('A08','A07;A15'),'ai创新':('A13','A00;A10'),'鼠标垫':('A13','A08;A15'),'听泉':('A02','A07;A11'),'一二三四，二二三四':('A15','A12;A10'),'我娃不适应':('A05','A07;A02'),'问在猜前':('A02','A03;A11'),'男王':('A15','A03;A10'),'异于禽兽者':('A07','A02;A03'),'理解不能':('A02','A05;A11'),'戴珍珠耳环的少女':('A15','A03;A04'),'蛋挞赌王':('A08','A07;A16'),'公平对战':('A13','A07;A10'),'炫耀与展示':('A07','A15;A02'),'不如意金箍棒':('A08','A07;A16'),'加油':('A03','A11;A05'),'欢迎不客气':('A03','A07;A15'),'盗名':('A07','A16;A02'),'青云窄巷':('A05','A18;A00'),'神笔牛良':('A12','A07;A02'),'出力不出钱':('A08','A07;A15'),'无缝':('A03','A11;A07'),'无声惊雷':('A20','A18;A00'),'追悔若及':('A00','A11;A10'),'大包厢':('A15','A10;A08'),'容错率':('A00','A10;A11'),'恐惧游戏':('A05','A07;A11'),'关门大吉':('A05','A07;A02'),'拍佛像':('A18','A07;A11'),'八卦':('A02','A03;A07'),'东美':('A15','A04;A18'),'风评无用':('A07','A00;A10'),'驴和马':('A03','A07;A02'),'国家队':('A15','A12;A10'),'以卵击石':('A04','A15;A07'),'大成至圣':('A05','A02;A10')}
batch=list(csv.DictReader(BATCH.open(encoding='utf-8-sig',newline='')))
assert len(batch)==50 and {r['title'] for r in batch}==set(D)
with PATH.open(encoding='utf-8-sig',newline='') as f:
 rd=csv.DictReader(f); rows=list(rd); fields=rd.fieldnames
by={r['id']:r for r in rows}
for r in batch:
 p,s=D[r['title']]
 by[r['id']]={'id':r['id'],'title':r['title'],'primary_print_topic_code':p,'secondary_print_topic_codes':s,'classification_status':'manual_confirmed','decision_basis':'Round 51 full-text review: '+r['title'],'review_note':'正文中心明确，主副专题按论证中心裁决。','reviewer':'main-thread','reviewed_at':'2026-09-23'}
with PATH.open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(by.values())
print('round51',len(batch),'manual_rows',len(by))
