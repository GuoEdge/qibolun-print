# -*- coding: utf-8 -*-
"""生成 round169 / round170 复核产出文件（仅写本轮新文件）。"""
import csv, json, os, re

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAVEAT = "本确认只覆盖现有可见正文，不追认未发表部分。"
IMGSEP = "图片审计与主题分类是两个独立决定，本轮不声称图片已全部审完，图片保留决定另记。"

R169 = [
 dict(id="4b4e3d38-7985-5823-aafd-9f44c2d3d20b", title="移星换斗", ord="2524", chars=3610,
   old_p="A12", old_s="A13;A18", new_p="A12", new_s="A13",
   basis="正文以北斗卫星在21500–35786公里轨道上的可发现性、可打击性与天基目标生存为案例，评估反卫星作战的技术可行性与战略含义，中心属太空军事目标与大国军事能力评估。",
   reason="保留A12：正文中心是美国能否发现并击落北斗、以及由此推出的战略判断。保留A13：轨道高度、传感器分辨率、火箭与导弹规模、燃料需求构成连续的工程可行性论证。删除A18：正文的轨道与探测内容服务于军事可打击性论证，未以生态、自然资源或自然科学认识为独立论述域，属机器候选带来的邻近领域联想（“太空”词面命中）。",
   quote="简单来说，根据这些估计，这个目标虽然并非物理上不可能做到，但至少在经济上、工程上难度非常大。",
   risk="轨道高度、传感器分辨率、导弹规模与拦截可行性等技术军事断言均未外部核验，属作者陈述；" + IMGSEP + CAVEAT),
 dict(id="3f6a6867-71a7-57fa-9071-39d374b1621b", title="人所不能者", ord="739", chars=3748,
   old_p="A09", old_s="A04;A01", new_p="A01", new_s="A04;A05",
   basis="正文从教师、家长、同学与当事人四个角度说明“从这事里面获得什么经验教训”，其中占篇幅最大的是当事人与同学的心理调适、自救义务与自我修复，中心属心理主体与情绪劳动。",
   reason="主专题由A09改为A01：正文未以疾病治疗、医护或照料关系为论述对象，肠易激综合征只作为霸凌事件的前提设定，作者的连续处理是受害者的自我修复与主体重建。副专题：删除A09（与主专题同理，正文无治疗/照料论述）；保留A04（教师必须干预、班级日志记录、学校处置与声誉构成教育场景论述）；新增A05（“从家长的角度出发”一节以父母对子女行为的约束与家庭代际后果为中心）；A01升为主专题后不再列入副专题。",
   quote="骤然临之而不惊，无故加之而不怒，这是一个强健的、值得托付和信靠的人该有的气魄。",
   risk="作者关于“不幸是祝福”“自救义务”“自然法”等主张属作者陈述，不得当作研究结论或现实建议；未成年人安全优先，遭遇霸凌应先脱离危险、联系监护人与学校及专业机构；事件事实、疾病与霸凌责任、社会扶助效果未外部核验；" + IMGSEP + CAVEAT),
 dict(id="26b2f5a9-d4ee-5d46-87e2-b4be7a55b9b7", title="服从领导", ord="3665", chars=4139,
   old_p="A07", old_s="A10", new_p="A07", new_s="A10",
   basis="正文区分“屈服”与“服从”，以自愿契约与授权边界说明组织中的服从义务，并讨论命令有效性、书面留痕与领导关系，中心属职场组织与合作。",
   reason="保留A07：正文中心是组织中的服从、契约授权与上下级协作。保留A10：“命令无效/授权范围/起诉留证/公民服从法律”构成连续的合法性论证，副轴成立。未新增副专题。",
   quote="你在企业的领导，是基于你在应聘企业岗位时签署的契约，出于岗位合作的自然安排而产生的协作者。",
   risk="正文末尾标注“（未完，待续），" + CAVEAT + "关于劳动契约、合法命令与违法指令的法律表述未经外部核验，属作者主张，不构成劳动法律意见或反报复保护建议。"),
 dict(id="90c3f6e6-064e-5ebd-bff0-e828bd50e15e", title="组织生鲜供应", ord="3846", chars=4354,
   old_p="A07", old_s="A08", new_p="A07", new_s="A08",
   basis="正文是一份疫情期小区生鲜团购的组织方案：物业—商超规模化供应流程、团购基本规则、团队分工与心理建设、订单与交接范本，中心是社区协作的组织与责任执行。",
   reason="保留A07：正文中心是采购、配送、志愿者分工与服务规则的组织设计和执行。保留A08：套餐定价、服务费、退款、捐赠、供应商订单分配比例与采购成本风险构成连续的市场交换内容。未新增副专题。",
   quote="物业向小区居民发布极尽简单的套装标准，每户按人口构成定量供应，只能选择要或者不要，不能选择内容。",
   risk="正文在商品套餐清单处结束，历史轮次标注“正文未完”，" + CAVEAT + "食品采购、抽检、配送与疫情防护方案具时效性，须遵循当地现行卫生要求；涉及糖尿病患者套餐与“降低透析压力”的表述有医疗风险，不能替代医生或营养师建议；退款、不可撤单与收费规则应核对消费者及合同规范。"),
 dict(id="95a97047-46ae-561c-b462-1c903c2c3ebd", title="尊师", ord="3906", chars=4713,
   old_p="A04", old_s="A11;A03", new_p="A04", new_s="A11;A03",
   basis="正文以“天、地、君、亲、师”推演师生关系的成立，讨论为师的资格（“我教的注定全是错的”自觉）、择师标准与“尊敬”的定义，中心属教育、学习与能力形成中的师生伦理与择师。",
   reason="保留A04：正文中心是教师资格、择师与师生的教受关系。保留A11：“敬天/敬地/天意/自然规律/信仰的礼物”构成连续的自然法与敬畏论证。保留A03：关于人无绝对真相认知、表达与理解的有限性、语言模糊性与“补强/补弱”的定义与论证分析构成连续的认识论述。未新增副专题。",
   quote="知者不足为师、能者也不足为师，只有觉者可以为师。",
   risk="作者关于“学生必须尊敬老师”“为徒资格”“尊敬即对可能性敬畏”的规范主张属作者陈述，不得写成研究结论或现实建议；不得把“尊敬”用作要求学生服从虐待、不当或违法行为的理由，具体教师责任与学生权利须按事实与适用规则核实；正文标注“（未完，待续）”，" + CAVEAT),
 dict(id="c4bab8ec-36c8-546c-84b2-a9fa20cd813d", title="前途", ord="3628", chars=4747,
   old_p="A04", old_s="A13;A07", new_p="A04", new_s="A13",
   basis="正文以强基计划为引，比较从众、先知、稳健三种前途选择策略，论证本科阶段应选基础学科、把确切专业定位推迟到研究生或换第二份工作，并联系国家科研体系与产业攻关需求，中心属教育、学习与能力形成。",
   reason="保留A04：正文中心是教育策略与专业/能力形成。保留A13：芯片制造、生物科技、航空航天、材料科学、科研体系改革与全产业链研发投入构成连续的产业路径论证。删除A07：正文只在“就业前景、换第二份工作时做专业定位”层面提到职业，未展开职场共事、上下级、管理、契约与退出等组织关系，属机器候选带来的邻近领域联想。",
   quote="对于本科生，选择基础学科专业远比选择应用学科专业更有意义。",
   risk="强基计划政策、就业趋势、科研投入与年龄/职业选择等预测性判断未外部核验，属作者主张；该篇1张图片状态为pending，" + IMGSEP + CAVEAT),
 dict(id="87c24ce9-61ee-534e-8417-fe0b89090e3b", title="SOP", ord="3434", chars=5951,
   old_p="A13", old_s="A15;A08", new_p="A13", new_s="",
   basis="正文是一份以质量要求、难点分析、工具选型、配比与加热参数记录、数据采集计划构成的鸡蛋羹制作工艺文件，中心是低门槛高可靠的工艺流程设计与参数化。",
   reason="保留A13：正文中心是工艺开发、设备选型与参数记录。删除A15：正文对“品相”的要求是成品质量规格，未以艺术创作、文化生产或价值评价为论述域。删除A08：“硬件投资成本尽可能低廉”只是设计约束之一，未展开财富、消费、借贷或市场交换论述。A15、A08均系机器候选且正文不支持，副专题清空为0个。",
   quote="因为整个搅拌头深陷液面下，只有一根光滑细幼的不锈钢主轴穿越气液交界，因此，在完成蛋液搅拌的整个过程中将不会产生任何气泡。",
   risk="烹饪温度、材料比例、器具安全与食品卫生参数未经现场复现实验，属作者经验陈述；正文含18张图片，历史轮次（round140，18/18）已作图片复核且未改变专题，" + IMGSEP + "正文标注“（未完，待续）”，" + CAVEAT),
]

R170 = [
 dict(id="f3283eb3-ae1f-5946-9995-2f7f18d3da32", title="反欺凌", ord="3896", chars=5985,
   old_p="A05", old_s="A04;A10", new_p="A05", new_s="A04;A10",
   basis="正文以“孩子受了欺凌，父母应该如何教导”为中心，先论证“教孩子打回去”为何错误（法律后果、升级循环、被贴标签），再给出家长引导子女建立互助团体与提供公共服务的长期策略，中心属父母对子女的教养与代际支持。",
   reason="保留A05：正文通篇对家长说话，中心是亲子教养策略。保留A04：“这是培养未来的领袖的最好的家庭教育”与补习/球队/美术等能力培养内容构成连续的教育论述。保留A10：故意伤害罪、人体轻伤鉴定标准、三年以下有期徒刑与未成年人责任的连续法律风险论证构成副轴。未新增副专题。",
   quote="孩子受了欺凌，父母应该如何教导？",
   risk="作者“不还击”“以提供公共服务换取安全”等主张属作者陈述，不得写成研究结论或现实建议；儿童即时安全优先，实际处置应先脱离危险、联系监护人与学校及专业机构，不得把“不还击”当作绝对规则而忽略紧急自卫；故意伤害量刑、未成年人责任、警方处置与霸凌者心理等断言未外部核验；正文标注“（未完，待续）”，" + CAVEAT),
 dict(id="05a4a9b4-4c5b-5dd4-bcc5-986e293d4955", title="复盘", ord="3369", chars=6350,
   old_p="A07", old_s="A03;A10", new_p="A07", new_s="A03",
   basis="正文给出复盘的完整流程（提出问题、案情重建、方案探讨），并把“解决方案”定义为组织规则的更新，另规定任务小组、会议纪律与主持人职责，中心属职场组织与合作。",
   reason="保留A07：正文中心是组织规则修订与会议/主持人制度的组织流程（“组织的本质，是组织的规则”）。保留A03：问题命名、标本采集、案情重建、排除不可能叙事与“逻辑地狱”构成连续的事实与论证方法论述。删除A10：正文中的奖惩、“执法”与赔偿是组织对内部规则违反的处理，作者明确将其划归复盘之外的专责小组（“关于复盘的讨论，不涉及个人的奖惩判决”），未以国家制度、犯罪、刑罚或司法程序为论述对象，属机器候选带来的邻近领域联想。",
   quote="所谓的解决方案，指且仅指组织规则的更新。",
   risk="会议违规赔偿、职业记录、人事处分与“司法实践”的主张未经外部核验，属作者主张，不能作为现行组织规范或法律程序直接采用；正文标注“（未完，待续）”，" + CAVEAT),
 dict(id="f62a367a-978f-5c01-8471-170daaa2eea8", title="疗愈艺术", ord="3299", chars=7506,
   old_p="A09", old_s="A15;A01", new_p="A01", new_s="A15;A09",
   basis="正文先否定“发泄情绪式治疗”，再以徒手画直线为例说明疗愈是“在方寸之间提供安全的犯错、检查错误、排除错误执念”的自我修复过程，并附十五条关于方法可靠性、能力衡量与坚持的练习笔记，中心是情绪调节与自我修复。",
   reason="主专题由A09改为A01：正文不处理疾病诊治、医护或照料关系，其中心是情绪发泄机制的批判与当事人的自我修复，与官方对象路径“与自己/与情绪/调节”同向，A09的“治疗关系”内容退为副轴。副专题：删除A01（升为主专题）；保留A15（徒手画直线、30度定位、明暗冷暖等艺术实践与审美判断构成连续论述）；A09改为副专题，以保留作者对发泄疗法及患者—治疗师—亲属合谋的持续批判。",
   quote="就是借着某种实践，在方寸之间提供一个安全的犯错、检查错误、排除错误执念、寻求正确可行的方式的过程。",
   risk="艺术疗愈、抑郁疫苗、治疗关系与心理病理解释均属作者主张，未经临床与外部核验，不构成治疗建议，也不得写成研究结论；正文含7张图片，历史轮次（round141，7/7）已作图片复核且未改变专题，" + IMGSEP + "正文标注“（未完，待续）”，" + CAVEAT),
 dict(id="bd497e81-413b-5e4c-b1df-001d0efbd369", title="可控核聚变", ord="4038", chars=8966,
   old_p="A18", old_s="A13;A12", new_p="A18", new_s="A13;A12",
   basis="正文中心是可控核聚变商用后大规模放热对地球热平衡与生态宜居性的威胁，并据此要求先建立国际管制共识，中心属生态、能源与自然科学。",
   reason="保留A18：正文中心是聚变放热的气候与生态后果及地球热平衡（“热也可以是一种污染”）。保留A13：聚变工程、喷管材料、金属氢与星际推进的技术路线分析构成连续工程论述。保留A12：国际条约框架、违约反制、核战争与功率份额竞争构成连续的大国秩序论证。未新增副专题。",
   quote="地球的温度其实是对热收入上升绝对敏感的——热收入增加，地球一定会升温。",
   risk="热力学、全球温度与生态连锁、聚变工程、星际推进及国际安全判断均未外部核验，属作者主张；正文含1张图片，历史轮次（round114，1/1）已作图片复核且图文一致且未改变专题，" + IMGSEP + CAVEAT),
]

ROUNDS = [("round169", R169, "subagent+round169-body-review"), ("round170", R170, "subagent+round170-body-review")]
REVIEWED_AT = "2026-09-26"

def clean(s):
    return re.sub(r"[\t\r\n]+", " ", s).strip()

def norm(s):
    return re.sub(r"[\s\"'“”‘’「」『』]", "", s)

for rname, rows, reviewer in ROUNDS:
    d = os.path.join(BASE, rname)
    texts = {}
    with open(os.path.join(d, f"{rname}-fulltext.json"), encoding="utf-8") as f:
        for i, e in enumerate(json.load(f), 1):
            texts[i] = e["text"]
    order = [e["title"] for e in json.load(open(os.path.join(d, f"{rname}-fulltext.json"), encoding="utf-8"))]

    # sanity: quote hit check before writing
    for i, r in enumerate(rows, 1):
        nq = norm(r["quote"]); nt = norm(texts[i])
        assert len(nq) >= 12, (rname, i, len(nq))
        assert nq in nt, ("QUOTE MISS", rname, i, r["title"])

    with open(os.path.join(d, f"{rname}-decisions.tsv"), "w", encoding="utf-8", newline="") as f:
        f.write("id\ttitle\tprimary\tsecondary\tstatus\tbasis\trisk_note\n")
        for r in rows:
            f.write("\t".join([r["id"], clean(r["title"]), r["new_p"], r["new_s"], "manual_confirmed",
                               clean(r["basis"]), clean(r["risk"])]) + "\n")

    with open(os.path.join(d, f"{rname}-body-evidence-audit.tsv"), "w", encoding="utf-8", newline="") as f:
        f.write("id\ttitle\tsource_ordinal\tbody_char_count\told_primary\told_secondary\told_status\t"
                "new_primary\tnew_secondary\tnew_status\tblocking_reason\tbody_evidence_quote\tdecision_reason\treviewer\treviewed_at\n")
        for r in rows:
            f.write("\t".join([r["id"], clean(r["title"]), r["ord"], str(r["chars"]), r["old_p"], r["old_s"],
                               "manual_provisional", r["new_p"], r["new_s"], "manual_confirmed", "",
                               clean(r["quote"]), clean(r["reason"]), reviewer, REVIEWED_AT]) + "\n")

    with open(os.path.join(d, f"{rname}-revision-log.csv"), "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["id", "title", "old_primary", "old_secondary", "old_status", "new_primary", "new_secondary",
                    "new_status", "basis", "risk_note", "revision_source", "revised_at"])
        for r in rows:
            changed = (r["old_p"] != r["new_p"]) or (r["old_s"] != r["new_s"]) or True  # old_status -> manual_confirmed 均变化
            if changed:
                w.writerow([r["id"], clean(r["title"]), r["old_p"], r["old_s"], "manual_provisional",
                            r["new_p"], r["new_s"], "manual_confirmed", clean(r["basis"]), clean(r["risk"]),
                            f"{rname}-fulltext-body-review", REVIEWED_AT])

    prows = []
    for i, r in enumerate(rows, 1):
        nr = clean(r["quote"])
        hit = norm(r["quote"]) in norm(texts[i])
        prows.append((r, i, hit))
    total = sum(r["chars"] for r in rows)
    n_prim_chg = sum(1 for r in rows if r["old_p"] != r["new_p"])
    n_sec_chg = sum(1 for r in rows if r["old_s"] != r["new_s"])
    print(rname, "rows=%d" % len(rows), "chars=%d" % total, "primary_changed=%d" % n_prim_chg,
          "secondary_changed=%d" % n_sec_chg, "quote_all_hit=%s" % all(p[2] for p in prows))
    for r, i, hit in prows:
        print("   ", i, r["title"], "quote_hit=", hit, "prim", r["old_p"], "->", r["new_p"],
              "sec", repr(r["old_s"]), "->", repr(r["new_s"]))
