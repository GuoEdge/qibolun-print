import csv
from pathlib import Path

p=Path('research-rebuild/data/print-topic-manual-decisions-v2.csv')
spec=[
('6610b6b8-873e-550d-a483-2a31a6bf54ca','走投无路','A10','A03;A08','manual_confirmed','正文中心是以走投无路为由为偷骗抢等犯罪行为免责的法律与责任边界','对“走投无路”定义和免责论证的认识论、以及生计场景为副轴'),
('cd1c5049-d5d4-58cf-9a91-ef620e5f1f02','超英','A15','A17;A20','manual_confirmed','正文中心是电影文本中的中国英雄形象、文化审美与君子传统','民族身份和文明历史为副轴'),
('ec7ef3e1-ccbc-5708-91c4-a63686c9d61f','素约','A06','A08;A03','manual_confirmed','正文中心是婚礼誓词、婚约约定与亲密关系的公共见证','反对铺张礼金的财富实践和爱的定义/誓词的概念论证为副轴'),
('dd926b00-b9ae-5d70-9552-61f9b7a9203f','一人之上','A14','A08;A07','manual_confirmed','正文中心是人工智能时代的一人公司、产权基础与创业路径','市场资源和组织/客户关系为副轴'),
('f1907b91-2872-5dc4-a6c0-2f835567014b','战龙于野','A04','A05;A10','manual_confirmed','正文中心是按儿童认知能力教授社会风险案例并形成可检验的应对能力','亲子教育责任和欺骗、威胁、合法自卫案例为副轴'),
('d9171979-347e-52be-9db8-e4b4199ce706','山丘背后','A10','A04;A08','manual_confirmed','正文中心是优绩主义、公权力托付与社会资源分配的制度正义','教育竞争和资源分配为副轴'),
('ba2a38af-1016-5306-8be5-3b6a0c38d154','炀','A07','A10;A20','manual_confirmed','正文中心是高层管理中信任、协商、关系安置和组织合作的实际机制','国家治理背景和历史模拟语境为副轴'),
('f9f5cb55-a8a1-5437-88fd-43929f90d6d5','冠军病','A01','A09;A03','manual_provisional','正文中心是痛苦身份、超常自我与心理恢复/强大的主体选择','疾病标签和正常/病态/治愈概念界定为副轴；临床判断不可直接核验，暂定'),
]
with p.open(encoding='utf-8-sig',newline='') as f:
    old=list(csv.DictReader(f)); fields=list(old[0])
by={r['id']:r for r in old}; added=0
for i,t,pri,sec,status,basis,note in spec:
    r={'id':i,'title':t,'primary_print_topic_code':pri,'secondary_print_topic_codes':sec,'classification_status':status,'decision_basis':basis,'review_note':note,'reviewer':'main-thread','reviewed_at':'2026-09-22'}
    if i not in by: old.append(r); by[i]=r; added+=1
    else: by[i].update(r)
with p.open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(old)
print('added',added,'rows',len(old))
