import csv
from pathlib import Path

p=Path('research-rebuild/data/print-topic-manual-decisions-v2.csv')
spec=[
('ace0aea5-99d9-5110-b9f2-6c83e040005f','大前门','A06','A01;A08','manual_provisional','正文中心是亲密关系中对伴侣能力、投入与合作资格的判断','涉及约会、资源投入和能力评价，作者对关系对象的推断较强，暂定'),
('3a0d174c-f654-5ce2-b2ec-60fb34b0c258','双毕业','A05','A08;A04','manual_confirmed','正文中心是父母与成年子女之间的储蓄、借贷、教育回报和代际经济安排','财富管理和学习习惯为副轴'),
('26639f91-6db3-571c-af59-364e41e1b24e','NPC','A07','A02;A10','manual_confirmed','正文中心是服务行业中的职业人格、工作边界与性骚扰规避','性别身体和法律风险为副轴'),
('abf0a4ce-d142-580e-b306-4616001cb183','西线无战事','A05','A01;A04','manual_confirmed','正文中心是父母/管理者的救火式监护如何损害亲子与下属的信任和自主成长','焦虑机制和教育引导为副轴'),
('b37796ff-6ee1-562d-9cc2-1ce50382c60e','宁静力','A01','A11;A08','manual_confirmed','正文中心是主体摆脱“堪与不堪”评价、以节制和稳定获得内在平静','生活方式的规范伦理和劳动/财富条件为副轴'),
('f48ddf91-2686-5bbb-88d1-3644e94907d7','好美','A15','A04;A08','manual_confirmed','正文中心是从自然物的好坏辨识建立审美判断、消费判断与人生选择能力','审美教育和市场消费实践为副轴'),
('c28d9ed8-eec9-51c4-bf67-4f47e91c6912','屁股朝前','A08','A07;A03','manual_confirmed','正文中心是信用、礼数与交易成本如何影响持续合作和经济收益','组织合作和社会惯例的论证为副轴'),
('be11fc4e-aa10-5562-b303-6cffcea4b6a9','当仁不让','A06','A02;A03','manual_confirmed','正文中心是亲密关系中的尊重、请求与同意边界，反对把合理性变成指挥权','身体/性别权力和“让”概念的定义为副轴'),
('16c0cbf0-7c55-5956-af86-f80923eada77','少点歧视','A17','A10;A11','manual_confirmed','正文中心是对群体株连、歧视和自保伤害的身份伦理反省','反歧视法律和规范伦理为副轴'),
('eb5c8088-f151-5249-a718-4ef7279880d1','救命书','A05','A04;A09','manual_confirmed','正文中心是亲子共同制定安全预案、演习和照料实践','教育训练和健康/安全照料为副轴'),
('f3ef4904-dcb3-5d06-835a-f0177ff33fa4','多余的不开心','A01','A06;A19','manual_provisional','正文中心是主体如何在朋友分担、衰老死亡和自我承受之间管理情绪负担','亲密友谊和死亡边界为副轴，含较强自我规范判断，暂定'),
('63aa195b-6c30-549f-b9d9-0452c144e2f3','稻谷咖啡','A04','A05;A14','manual_confirmed','正文中心是儿童学习动机、父母反馈和长期能力形成','亲子教育和AI时代学习竞争为副轴'),
('0e572114-b072-5bbd-a5bd-fd0b5c2ef31f','蘸醋','A08','A06;A11','manual_confirmed','正文中心是对他人自愿牺牲的利用、回报与价值传递','朋友关系和牺牲伦理为副轴'),
('bdbd1ec1-4516-571a-8e12-db95b0c99a88','环保猎人','A18','A10;A08','manual_provisional','正文中心是合法狩猎、自然保护区融资与环保机制的事实辩护','法律手续和服务收费为副轴；外部链接事实需独立核验，暂定'),
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
