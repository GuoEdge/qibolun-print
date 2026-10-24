import csv
from pathlib import Path

p=Path('research-rebuild/data/print-topic-manual-decisions-v2.csv')
spec=[
('a16da506-5c08-5099-816e-25262f8afb82','小炮仗','A01','A04;A06','manual_confirmed','正文中心是主体自由、反抗共识与重大选择中的自我调节','教育和亲密关系是情境副轴'),
('101192ad-8c18-5d1a-abfe-c6d8e7727c38','砼','A01','A09;A03','manual_confirmed','正文中心是挫折后的焦虑、无能认同与心理机制','健康和进化论证为副轴'),
('6587f538-6d67-5561-99dd-2eaf61719621','眠种','A13','A18;A20','manual_confirmed','正文中心是手工技术作为文明备份与技术遗产保存','生态韧性和文明演变为副轴'),
('b4af6921-69d1-5962-ab5f-f7f86f20a794','守在门外的人','A02','A05;A09','manual_confirmed','正文中心是性健康教育、性隐私与性自主权','家庭教养和健康照料为副轴'),
('446ed510-22ee-5cc9-ab46-f5ef8d851fa7','清静无为','A20','A11;A12','manual_provisional','正文中心是庄子思想的历史解释及其政治秩序含义','宗教自然法与政治秩序均有重要比重，暂定'),
('15e6750c-c146-58ea-b925-3a495204a3ef','三分一又三分一','A04','A01;A03','manual_confirmed','正文中心是把大问题拆解为可学习、可验收的任务规划能力','心理状态和方法论为副轴'),
('17108618-47db-56ee-93c1-b25db0d50aa1','火','A06','A01;A05','manual_confirmed','正文中心是亲密关系中的人格尊重、失望与分离判断','主体心理和家庭背景为副轴'),
('c9e76d20-ad76-500f-95eb-be07ade6e9f1','满分70','A10','A11;A12','manual_confirmed','正文中心是社会正义、司法政策与自由秩序的制度论证','世俗伦理和和平秩序为副轴'),
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
