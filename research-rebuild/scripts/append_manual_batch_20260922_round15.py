import csv, json
from pathlib import Path
p=Path('research-rebuild/data/print-topic-manual-decisions-v2.csv')
spec=[
('c0ef769d-39f5-5f7b-af45-899250f18786','嫉妒','A01','A06;A03','manual_confirmed','正文中心是嫉妒作为主体情绪、比较机制与关系反应','关系和论证是副轴'),
('e4b84f2f-dd8c-5163-a062-003fd1ec871f','善良程度','A11','A01;A03','manual_confirmed','正文中心是善良规范、道德设防与世俗伦理判断','心理动机和事实论证为副轴'),
('714155ed-3e9b-5722-b3f1-9715741ed39a','咽','A09','A18;A03','manual_confirmed','正文中心是咽喉健康、餐饮风险与身体照料','自然机制和事实判断为副轴'),
('c2038ba6-3f8d-5cb4-9d84-2e5667316198','渣起来','A06','A01;A10','manual_confirmed','正文中心是亲密关系退出、婚恋责任与关系伤害','主体心理和道德法律边界为副轴'),
('be3dedc0-5161-5bd2-b4e0-28cf1ed72b1e','白目人','A07','A03;A06','manual_confirmed','正文中心是职场与社会合作中的命令边界、责任和关系协调','事实判断与亲密关系为副轴'),
('f4cdfc65-3177-52e3-b12c-54859a4db61e','二宝锤','A03','A01;A08','manual_confirmed','正文中心是认知讽刺、贫困经验与知识判断','主体心理和资源处境为副轴'),
('57d4a115-7d26-597e-8fcc-df08c4d41a1f','车速过快','A01','A04;A13','manual_confirmed','正文中心是紧张、能力边界与主体自我调节','学习训练和技术情境为副轴'),
('2a91b754-20fc-55b4-9aa1-185a470dbb01','人走茶凉','A07','A08;A06','manual_confirmed','正文中心是职业伦理、组织关系与离职后的合作秩序','资源交换和亲密关系为副轴'),
('b61be412-94ee-5961-9445-c48786d74925','论同志','A03','A12;A17','manual_confirmed','正文中心是同志概念边界、政治共同体与身份论证','战争政治和族群身份为副轴'),
('0d56a917-8440-5c0e-9c34-92365b831d9a','301的隔壁','A06','A01;A03','manual_confirmed','正文中心是亲密关系、自我暴露与身份互动','主体心理和事实解释为副轴'),
('9bd10f2e-221b-5789-b44c-65732e163960','丑','A15','A02;A17','manual_confirmed','正文中心是审美判断、身体外观与族群身份的文化义务','性别身体和身份秩序为副轴'),
]
with p.open(encoding='utf-8-sig',newline='') as f: old=list(csv.DictReader(f)); fields=list(old[0])
by={r['id']:r for r in old}; added=0
for i,t,pri,sec,status,basis,note in spec:
 r={'id':i,'title':t,'primary_print_topic_code':pri,'secondary_print_topic_codes':sec,'classification_status':status,'decision_basis':basis,'review_note':note,'reviewer':'main-thread','reviewed_at':'2026-09-22'}
 if i not in by: old.append(r); by[i]=r; added+=1
 else: by[i].update(r)
with p.open('w',encoding='utf-8-sig',newline='') as f: w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(old)
print('added',added,'rows',len(old))
