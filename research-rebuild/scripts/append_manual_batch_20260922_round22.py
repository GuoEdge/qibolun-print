import csv
from pathlib import Path
p=Path('research-rebuild/data/print-topic-manual-decisions-v2.csv')
spec=[
('04cf4d96-fc58-54bc-9545-f1a09748d1d7','负十八','A04','A01;A05','manual_provisional','正文中心是对低谷期学生的教育理解、发展可能与长期能力形成','心理痛苦和师生/亲子责任为副轴；历史规律判断偏推测，暂定'),
('9a42c70d-c6f8-57cc-813b-058eff9c1a65','哭奶','A07','A08;A01','manual_confirmed','正文中心是组织中以长期信任、能力和不可替代性取得资源谈判资格','预算资源和情绪策略为副轴'),
('c590e1e8-6daa-556d-928f-94a34d25a184','鬼话连篇','A10','A01;A07','manual_confirmed','正文中心是识别威胁、拒绝合作和防御性沟通的安全策略','恐惧反应和合作边界为副轴'),
('38b7d4d0-539b-521c-8ef6-d42b988c6be1','酸友情','A08','A01;A06','manual_confirmed','正文中心是独立创造价值的劳动能力如何决定资源依赖与关系焦虑','主体自卑和友谊依赖为副轴'),
('1cfec0b4-fb45-5f40-95be-420000cda248','如蒙不弃','A06','A01;A03','manual_confirmed','正文中心是亲密关系中清醒认识缺点、接纳平凡与爱的定义','心理迷恋机制和爱之概念辨析为副轴'),
('607caf96-19f4-5d98-9829-9e70c706877f','四海为家','A17','A07;A20','manual_confirmed','正文中心是移居者通过地方认同、公共生活和关系网络形成身份归属','社会合作和地方历史文明为副轴'),
('cbf06b16-bd70-5662-a798-111ae72eeafa','不插电','A05','A11;A01','manual_confirmed','正文中心是成年子女通过经济和居住独立完成亲子关系断奶','自然法论证和主体自由为副轴'),
('e74bc219-6ba4-54e7-8dd3-33cf205c3009','尊重的前提','A05','A01;A03','manual_confirmed','正文中心是父母监护、子女尊重要求与可操作方案之间的代际关系条件','主体不满和尊重概念逻辑为副轴'),
]
with p.open(encoding='utf-8-sig',newline='') as f: old=list(csv.DictReader(f)); fields=list(old[0])
by={r['id']:r for r in old}; added=0
for i,t,pri,sec,status,basis,note in spec:
 r={'id':i,'title':t,'primary_print_topic_code':pri,'secondary_print_topic_codes':sec,'classification_status':status,'decision_basis':basis,'review_note':note,'reviewer':'main-thread','reviewed_at':'2026-09-22'}
 if i not in by: old.append(r); by[i]=r; added+=1
 else: by[i].update(r)
with p.open('w',encoding='utf-8-sig',newline='') as f: w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(old)
print('added',added,'rows',len(old))
