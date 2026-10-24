import csv
from pathlib import Path
p=Path('research-rebuild/data/print-topic-manual-decisions-v2.csv')
spec=[
('bf9b4eb5-d380-5b55-915c-d000c8f22c27','爱自己','A04','A01;A05','manual_confirmed','正文中心是通过具体任务、反馈和代价训练儿童的自我管理与能力成长','主体自爱和亲子教育为副轴'),
('1ebceeb1-26da-536f-bfcd-d43f91f25b8d','云阶','A01','A08;A05','manual_confirmed','正文中心是主体摆脱阶层羞耻、在当下生活中建立稳定满足和自我价值','财富处境和身边关系经营为副轴'),
('ca3e2033-6991-50e4-84b8-8ca371a16748','我心不满','A06','A01;A03','manual_confirmed','正文中心是亲密关系中表达不满、资源调度与信任义务的冲突','情绪机制和感受表达概念为副轴'),
('48fc9dc7-9e20-5b78-b9b3-c6e14181eaf9','我是你爷爷','A03','A10;A05','manual_confirmed','正文中心是“没教养”等道德评价的管辖权、定义和社会地位含义','审判权/规范边界和家庭教育为副轴'),
('e476717b-2cf7-5a91-adb2-924fbec64dea','援亲','A08','A05;A10','manual_confirmed','正文中心是亲友借款、投资、援助的契约区分与资源边界','亲属救助和法律契约为副轴'),
('bc474d87-a778-54ee-914c-dcdf73138a6d','大题大作','A06','A02;A03','manual_confirmed','正文中心是亲密关系中的命令、承诺、隐私和侵权边界','身体/个人边界与原则定义为副轴'),
('5bcb728b-4a1d-518d-a629-fc27f09df49e','锥子','A04','A01;A07','manual_confirmed','正文中心是通过可观察榜样、具体行动和渐进训练形成能力与志向','主体激励和合作实践为副轴'),
('a306129e-d5b1-544e-beeb-60e87483e02f','小算盘','A07','A04;A08','manual_confirmed','正文中心是个人能力、人脉形成与组织合作的相互依赖','学习能力和资源网络为副轴'),
]
with p.open(encoding='utf-8-sig',newline='') as f: old=list(csv.DictReader(f)); fields=list(old[0])
by={r['id']:r for r in old}; added=0
for i,t,pri,sec,status,basis,note in spec:
 r={'id':i,'title':t,'primary_print_topic_code':pri,'secondary_print_topic_codes':sec,'classification_status':status,'decision_basis':basis,'review_note':note,'reviewer':'main-thread','reviewed_at':'2026-09-22'}
 if i not in by: old.append(r); by[i]=r; added+=1
 else: by[i].update(r)
with p.open('w',encoding='utf-8-sig',newline='') as f: w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(old)
print('added',added,'rows',len(old))
