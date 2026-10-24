import csv
from pathlib import Path
p=Path('research-rebuild/data/print-topic-manual-decisions-v2.csv')
spec=[
('049b2aa6-0752-584f-86bd-0f94acd09569','欲与还休','A06','A03;A01','manual_confirmed','正文中心是亲密关系中赠予、撤回、信任与风险承担的边界','赠予概念和情绪反应为副轴'),
('f52eb7c8-d75f-535f-a115-2d4098b93f1d','等因奉此','A07','A03;A10','manual_confirmed','正文中心是组织传话、责任核实、信息完整性与上下级协作风险','事实核验和权力责任为副轴'),
('466f7b8c-c951-5e93-a7f8-dd9c091f613d','基本颜值','A15','A02;A08','manual_confirmed','正文中心是外貌修饰、体面规范与审美技术的社会义务','身体呈现和消费劳动为副轴'),
('97aed0c8-5326-57a7-a020-b31124698b43','奶婚','A06','A01;A03','manual_provisional','正文中心是亲密关系中以沉没成本和珍惜机制维持婚姻的风险','心理依恋和沉没成本概念为副轴；含明显寓言化推断，暂定'),
('190a0b7a-45d7-50b3-b4e0-d5731b737ded','沉吟至今','A15','A04;A20','manual_confirmed','正文中心是诗歌朗诵、音韵审美和文化传承中的学习实践','教育训练和历史语言文明为副轴'),
('96f118d4-77b3-50fe-8bd1-c407ea8fcd4e','休息处','A11','A01;A19','manual_provisional','正文中心是罪责、悔过、隐私与重新生长的道德宽恕空间','心理恢复和死亡/终极责任为副轴；作者价值承诺较强，暂定'),
('660c2ce5-bb23-5c33-9b63-fdd242332b73','唯一对手','A04','A08;A05','manual_confirmed','正文中心是教育孩子认识愿望实现的全部成本并培养自主解决问题的能力','资源成本和亲子支持为副轴'),
('c05e173c-8c17-57fd-987c-c03275f6ff40','憋','A06','A01;A03','manual_confirmed','正文中心是友谊中表达痛苦、消耗关切与关系资源边界的权衡','情绪体验和频率/尺度判断为副轴'),
]
with p.open(encoding='utf-8-sig',newline='') as f: old=list(csv.DictReader(f)); fields=list(old[0])
by={r['id']:r for r in old}; added=0
for i,t,pri,sec,status,basis,note in spec:
 r={'id':i,'title':t,'primary_print_topic_code':pri,'secondary_print_topic_codes':sec,'classification_status':status,'decision_basis':basis,'review_note':note,'reviewer':'main-thread','reviewed_at':'2026-09-22'}
 if i not in by: old.append(r); by[i]=r; added+=1
 else: by[i].update(r)
with p.open('w',encoding='utf-8-sig',newline='') as f: w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(old)
print('added',added,'rows',len(old))
