import csv
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; PATH=ROOT/'research-rebuild/data/print-topic-manual-decisions-v2.csv'; BATCH=ROOT/'research-rebuild/reports/live-manual-short-batch-v2-round52-short50.csv'
D={'人传人':('A05','A02;A10'),'内举不避亲':('A08','A10;A07'),'敬我自己一杯':('A08','A07;A03'),'因大失小':('A08','A10;A07'),'逝者如斯夫':('A00','A15;A11'),'噤':('A07','A11;A02'),'赏金猎猪':('A20','A16;A13'),'长期合规':('A09','A16;A08'),'双人票':('A03','A11;A05'),'防偷拍':('A16','A13;A08'),'雷峰夕照':('A07','A03;A12'),'赏赏罚罚':('A08','A07;A10'),'垃圾食品':('A20','A09;A13'),'双语教学':('A05','A02;A04'),'失败福寿膏':('A11','A02;A05'),'祛恶视':('A16','A07;A02'),'不盈利组织':('A08','A15;A10'),'恐惧的疫苗':('A02','A03;A11'),'实际产品':('A13','A10;A08'),'看上去很美':('A12','A18;A07'),'老师的同学':('A05','A02;A10'),'恶人磨':('A07','A02;A16'),'真心祝福':('A03','A07;A00'),'pupil':('A02','A04;A00'),'天眼查':('A13','A16;A08'),'吸引力法则':('A02','A00;A11'),'先吃亏':('A03','A07;A11'),'饭难吃':('A02','A07;A15'),'避玄如避嫌':('A02','A00;A11'),'向后看':('A11','A00;A02'),'监守者难辞其咎':('A08','A16;A07'),'参北斗':('A02','A13;A04'),'鬼故事':('A03','A07;A11'),'厌物':('A02','A07;A11'),'以和为贵':('A13','A15;A08'),'李四闭嘴':('A07','A02;A11'),'现实问题':('A09','A00;A07'),'出头鸟':('A10','A08;A07'),'完整规定':('A07','A03;A00'),'一招制敌':('A16','A09;A13'),'礼貌的意义':('A07','A16;A03'),'数学启蒙':('A04','A02;A05'),'气质的配方':('A04','A05;A00'),'儿童阅读':('A05','A02;A10'),'花呗仙人':('A18','A07;A00'),'馅饼云':('A11','A00;A02'),'房产税之外':('A12','A15;A08'),'帮亲':('A07','A09;A03'),'真想要':('A11','A02;A03'),'反着卖':('A08','A15;A13')}
batch=list(csv.DictReader(BATCH.open(encoding='utf-8-sig',newline='')))
assert len(batch)==50 and {r['title'] for r in batch}==set(D)
with PATH.open(encoding='utf-8-sig',newline='') as f:
 rd=csv.DictReader(f); rows=list(rd); fields=rd.fieldnames
by={r['id']:r for r in rows}
for r in batch:
 p,s=D[r['title']]
 by[r['id']]={'id':r['id'],'title':r['title'],'primary_print_topic_code':p,'secondary_print_topic_codes':s,'classification_status':'manual_confirmed','decision_basis':'Round 52 full-text review: '+r['title'],'review_note':'正文中心明确，主副专题按论证中心裁决。','reviewer':'main-thread','reviewed_at':'2026-09-23'}
with PATH.open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(by.values())
print('round52',len(batch),'manual_rows',len(by))
