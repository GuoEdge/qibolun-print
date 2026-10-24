import csv
from pathlib import Path
p=Path('research-rebuild/data/print-topic-manual-decisions-v2.csv')
spec=[
('b41e4c82-7300-5dc8-9146-e3de86d16674','如己','A06','A01;A02','manual_provisional','正文中心是亲密关系中对伴侣身体气味的接纳、适应与视同己身','心理去敏感和身体/性边界为副轴；涉及性与体味的推断较强，暂定'),
('d8dd2ec7-b290-5931-8702-c8109d8545ca','勿自疑','A06','A01;A09','manual_provisional','正文中心是亲密关系中面对疾病、负担与承诺时的爱与行动不确定性','心理软弱和疾病照料为副轴；“爱会自然赐予勇气”属推测，暂定'),
('6fb08d39-0a3e-5fa9-b572-0e6ae9791bb9','圆滑2','A07','A01;A04','manual_confirmed','正文中心是组织合作中体谅成员软弱、调和使命与人情并保留执行边界','心理理解和能力训练为副轴'),
('4614c6c1-d48d-5eaf-9add-6c6ad70aa42d','以正视听','A04','A03;A01','manual_confirmed','正文中心是教育中如何使用榜样、分析经验并训练可持续的判断方法','认识论审计和主体价值形成为副轴'),
('0214ec45-35a8-58ed-96d5-cd726149d10f','傻辉的爱','A08','A07;A06','manual_confirmed','正文中心是交易沟通中回报、机会成本与对方响应动力','组织合作和关系中的爱与信任为副轴'),
('05560f89-6f4c-5dd9-bbad-08cdeb4e07ba','延历寺','A07','A10;A20','manual_confirmed','正文中心是高层组织决策中威望、战绩、利益分配与论证的相对作用','权力制度和历史案例为副轴'),
('2f4296c0-b9be-5bde-93fe-28743198c351','色之为性也','A02','A20;A11','manual_provisional','正文中心是性观念、性需求与身体/文化规范的历史变迁及同意边界','文明历史和规范伦理为副轴；历史事实论断需谨慎，暂定'),
('5cee0244-616f-5e86-af29-a2dde5a6a224','错信','A03','A01;A07','manual_confirmed','正文中心是不信任、自我能力与他人可信性的概念分析','主体心理和咨询/合作实践为副轴'),
]
with p.open(encoding='utf-8-sig',newline='') as f: old=list(csv.DictReader(f)); fields=list(old[0])
by={r['id']:r for r in old}; added=0
for i,t,pri,sec,status,basis,note in spec:
 r={'id':i,'title':t,'primary_print_topic_code':pri,'secondary_print_topic_codes':sec,'classification_status':status,'decision_basis':basis,'review_note':note,'reviewer':'main-thread','reviewed_at':'2026-09-22'}
 if i not in by: old.append(r); by[i]=r; added+=1
 else: by[i].update(r)
with p.open('w',encoding='utf-8-sig',newline='') as f: w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(old)
print('added',added,'rows',len(old))
