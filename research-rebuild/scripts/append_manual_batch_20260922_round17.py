import csv
from pathlib import Path
p=Path('research-rebuild/data/print-topic-manual-decisions-v2.csv')
spec=[
('ca0b2dd4-e67a-5243-a150-98c3b33953c1','赤手空拳','A07','A08;A10','manual_confirmed','正文中心是责任承担如何换取组织中的权力、资源与授权','财富和法律责任为副轴'),
('b12ffdac-091e-519b-947b-a20d33f76e44','鲍鱼之肆','A03','A01;A18','manual_confirmed','正文中心是感知分类、经验塑造与香臭评价的认识论机制','情绪经验和物种自然科学例证为副轴'),
('c1f65e27-5be0-5388-aeb8-aae0f0e78b8e','困兽','A06','A01;A05','manual_provisional','正文中心是亲密关系中压力分担、关心与情绪责任','大量内容是不可验证的心理重建，家庭场景为副轴，暂定'),
('4acdd38f-59cb-51e5-a4af-56dc3112c805','弟子服其劳','A07','A04;A03','manual_confirmed','正文中心是组织领导、公共服务激励与公平边界','学校教育是场景，教育训练和规则论证为副轴'),
('561bb73f-d62d-5b2c-9af1-279bffea330d','阻住地球的人','A10','A05;A01','manual_confirmed','正文中心是霸凌处置失灵、社会责任与保护机制','家庭支持和受害者自责的心理后果为副轴'),
('118b1ce8-3d30-51f5-82eb-af8a008d0c04','快乐的信心','A05','A01;A08','manual_confirmed','正文中心是家庭劳动、代际情感支持与传承信心','主体心理和财富选择为副轴'),
('86b2eba8-396f-5abb-a558-6da486f552f9','饱汉饥','A11','A08;A01','manual_confirmed','正文中心是以自然法解释资源过剩后的分享、保护与领导义务','财富占有和幸福奖励变化为副轴'),
('4605e04c-70c0-5b06-bfff-54b358fa6cc4','防事墙','A04','A08;A01','manual_confirmed','正文中心是培养可产出价值的技能并从做事中形成动机','劳动交换价值和主体心理为副轴'),
('6997b10c-8fe5-573f-b41f-312a70f53490','老实大喇叭','A10','A08;A01','manual_confirmed','正文中心是灰色交易、违法风险及责任归因','财富投机和愤怒扩散为副轴'),
('4a78f2bf-1338-55f6-b9ce-7a6707d61805','阿宝悄悄话','A04','A05;A01','manual_confirmed','正文中心是亲子共读、提问记录与认知和社会性发育','家庭关系和情绪支持为副轴，AI只是记录工具'),
]
with p.open(encoding='utf-8-sig',newline='') as f: old=list(csv.DictReader(f)); fields=list(old[0])
by={r['id']:r for r in old}; added=0
for i,t,pri,sec,status,basis,note in spec:
 r={'id':i,'title':t,'primary_print_topic_code':pri,'secondary_print_topic_codes':sec,'classification_status':status,'decision_basis':basis,'review_note':note,'reviewer':'main-thread','reviewed_at':'2026-09-22'}
 if i not in by: old.append(r); by[i]=r; added+=1
 else: by[i].update(r)
with p.open('w',encoding='utf-8-sig',newline='') as f: w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(old)
print('added',added,'rows',len(old))
