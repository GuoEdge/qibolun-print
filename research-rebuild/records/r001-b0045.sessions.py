# -*- coding: utf-8 -*-
"""批次 r001-b0045 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0045.sessions.py            # 写 out/r001-b0045.out.jsonl
  python3 records/r001-b0045.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0045"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0045.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "1e6499af": {
  "analysis": {
   "question_context": "提问者（Q001）问“如何看待逆全球化？”。作者先自设全球化的定义，再把问题转为“有没有力量能阻止全球化”，提出软极限与两个主要议题（收益的区域内再分配、地缘政治格局承受重压）；P076 起为回应“谈一谈疫情对全球化的影响”这一要求的补充段落。",
   "content_units": [
    { "unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004"], "summary": "立定义：全球化＝采集全球最好的原料、人力、技术，生产最多人需要的产品，卖到一切可卖之处；本质是“商品经济最大化”。", "role": "definition" },
    { "unit_id": "U002", "paragraph_refs": ["P005", "P006", "P007", "P008", "P009", "P010", "P011"], "summary": "问题转为：有没有力量能让商人放弃最极限利润。集体干预须均匀统一，否则被限制者只有战或逃；该规律如万有引力不可抗拒。", "role": "reason" },
    { "unit_id": "U003", "paragraph_refs": ["P012", "P013", "P014", "P015", "P016", "P017", "P018", "P019", "P020", "P021", "P022", "P023"], "summary": "全球化像空气，扩展到能扩展到的极限才止步；极限分物理极限与动态软极限。走向在不同地域行业维度不均匀波动，应按局部议题判断而非全球总趋势。", "role": "claim" },
    { "unit_id": "U004", "paragraph_refs": ["P024", "P025", "P026", "P027", "P028"], "summary": "第一议题：收益的区域内再分配。进出口部门高度受益，部门外的人利益较小即制造问题；政治平衡点迁移消耗社会资本，社会资本无主而商业资本有主。", "role": "claim" },
    { "unit_id": "U005", "paragraph_refs": ["P029", "P030", "P031", "P032"], "summary": "村十一人算例：整体增益被富翁独得大半；普通村民无力承担风险与信息成本，市场竞争失灵，到限度即触发非经济手段的抑制能量。", "role": "example" },
    { "unit_id": "U006", "paragraph_refs": ["P033", "P034", "P035", "P036", "P037"], "summary": "“中美贸易战”本质是美国全球化掉队者与弄潮儿之争，打击成本几乎全由美国富翁承受；不解决利润的区域广泛分配，全球化就不会获得进一步扩大的许可。", "role": "rebuttal" },
    { "unit_id": "U007", "paragraph_refs": ["P038", "P039", "P040", "P041", "P042", "P043", "P044", "P045"], "summary": "富翁不会轻易就范，妥协须足够痛苦且无后患；答案是全民所有制与国有经济主体化，美国以超额贸易税实现该设计，是隐性国有化。", "role": "claim" },
    { "unit_id": "U008", "paragraph_refs": ["P046", "P047", "P048", "P049", "P050", "P051", "P052", "P053"], "summary": "该措施授予政府决定谁被国有化的权力，是政治对经济的霸权，而美国富翁才是最大政治霸权势力（川普如宋江）。中国因全民所有制架构缓和极化、权力与经济脱钩，并以全局投资与“以工代赈”实现均沾；资源国有型国家同理。", "role": "reason" },
    { "unit_id": "U009", "paragraph_refs": ["P054", "P055", "P056", "P057", "P058", "P059", "P060", "P061", "P062", "P063", "P064"], "summary": "第二议题：地缘政治格局承受重压，是美国村问题的重演，但没有第二个地球村可容纳“各得其所”。作者认为只有武力震慑＋主动释放物质利益一途，受益国将团结实行；最终剧情是“生产力之王”先震慑、再以物质倾斜换取秩序调整。", "role": "claim" },
    { "unit_id": "U010", "paragraph_refs": ["P065", "P066", "P067", "P068", "P069", "P070", "P071", "P072", "P073", "P074", "P075"], "summary": "中国已行动：军事现代化、一带一路与“人类命运共同体”，并引《论语》“不患寡而患不均”；还可扩大门户开放（科举制为先例）。归结为：全球化是生产力发展，反全球化是生产关系诉求，生产关系终将自我调整。", "role": "conclusion" },
    { "unit_id": "U011", "paragraph_refs": ["P076", "P077", "P078", "P079", "P080", "P081", "P082", "P083", "P084", "P085", "P086", "P087"], "summary": "回应疫情：回迁产业使成本与价格更高，只有中国肯定不卖更便宜产品时更高成本才成为实际最低成本；担心卡脖子应建战略储备，回迁自产储备是纯粹浪费。", "role": "rebuttal" },
    { "unit_id": "U012", "paragraph_refs": ["P088", "P089", "P090", "P091", "P092", "P093", "P094", "P095", "P096", "P097", "P098", "P099", "P100"], "summary": "再反驳：自产产能平时无法养活，预判疫情过后不到两年呼声即转向“这很愚蠢”，回迁成本完全沉没；该主张要长期获支持，必须有中国无休无止恶意禁运这一绝对必要前提。", "role": "rebuttal" },
   ],
   "main_claims": [
    { "claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者界定全球化：采集全球最好的原料、人力、技术，生产最多人需要的产品，卖到一切可卖之处。", "evidence": ["E1"] },
    { "claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称全球化的本质就是“商品经济最大化”。", "evidence": ["E2"] },
    { "claim_id": "C003", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "作者把问题转为有没有力量能让商人放弃最极限利润，并论证集体主动干预必须均匀统一施加到所有市场玩家身上，否则被限制者只有战（让你下台甚至肉体消灭）或逃（换国家）。", "evidence": ["E4", "E5"] },
    { "claim_id": "C004", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者称这个规律如万有引力定律般不可抗拒，除非消灭商品经济；消费者对质次价高长期不可接受。", "evidence": ["E6"] },
    { "claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者提出全球化像空气，会进展到能扩展到的极限才止步；极限分不可超过的物理极限与超过即被回拉、反复回弹的动态软极限。", "evidence": ["E7", "E8"] },
    { "claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为全球化走向是不均匀波动，按不同口径统计会得不同结论，“全面推进/全面逆转”之说在触碰软极限时很无意义。", "evidence": ["E9"] },
    { "claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张应关注影响各地区各行业局部策略的主要议题及其交叉反应，而非“全球的全球化总趋势”。", "evidence": ["E10"] },
    { "claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者提出第一议题是收益的区域内再分配：全球化高度有利于进出口部门，对该部门之外的人利益较小（不见得是没有利益）就已制造问题。", "evidence": ["E11"] },
    { "claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为政治平衡点迁移痛苦且消耗大量社会资本；社会资本无主、无人能有效捍卫而商业资本有主，全球化因而有没收全民社会资本、倾斜给密切参与全球化的阶层并给予丰厚奖励的效应。", "evidence": ["E12", "E13"] },
    { "claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以村里十一人的算例说明极化（一人独得800、其余各得20），并称风险承担能力和信息准备远非普通村民所能普遍承担，且富翁已抢先占住战略优势位置。", "evidence": ["E14"] },
    { "claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者判断市场竞争失灵、政治经济地位向富翁倾斜而无法靠市场竞争扭转，到一定限度就会触发非经济手段的抑制全球化的能量。", "evidence": ["E15"] },
    { "claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为“中美贸易战”本质上发生在美国的全球化掉队者和弄潮儿之间；中国环节成本与需求刚性，打击成本几乎完全由美国富翁承受。", "evidence": ["E16", "E17"] },
    { "claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为不解决全球化利润的区域内广泛分配问题，全球化就不会获得进一步扩大的许可，这才是受阻的根本原因。", "evidence": ["E18"] },
    { "claim_id": "C014", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者判断富翁不可能轻易就范：即使愿意妥协也必须使过程足够痛苦，否则“闹事有钱拿”没有尽头；没有无制度和伦理后患的妥协逻辑。", "evidence": ["E19"] },
    { "claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者提出真正能解决这个问题的答案是全民所有制以及国有经济主体化：由全民持有最有利润的优势产业，外贸利润用于全民普惠的基础建设，但对资本主义国家太可怕。", "evidence": ["E20"] },
    { "claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为美国正尝试通过征收必然由富翁承担的超额贸易税在本质上实现这个设计，这是一种隐性的国有化。", "evidence": ["E21"] },
    { "claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者警告美国人民不要抱过大乐观：该措施会授予政府决定谁被国有化的巨大权力，是政治对经济的霸权，而美国富翁才是最大的政治霸权势力；川普的确可算是美国村民的宋江，可惜宋江的下场并不美好。", "evidence": ["E22"] },
    { "claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为中国是全球化中最成功的玩家之一：全民所有制和国有经济主体的架构缓和了全球化对中国的极化效应，并实现了政治权力与经济实力的脱钩化。", "evidence": ["E24"] },
    { "claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为中国把“利润公平再分配”难题转化为高铁、全面城市化、军事现代化、公立教育、全民医疗和一带一路等全局性投资，以“以工代赈”实现均沾。", "evidence": ["E25"] },
    { "claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为中国对全球化必然的副作用有更强免疫力，几乎没有任何顾虑，可以大胆展开一切进攻性的策略。", "evidence": ["E26"] },
    { "claim_id": "C021", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者认为资源国有或变相国有的资源型国家如果较好控制住贪污，也会对全球化有更大承受力（卡塔尔、沙特、阿联酋、文莱、新加坡、日本、韩国）。", "evidence": ["E27"] },
    { "claim_id": "C022", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者提出第二议题是地缘政治格局承受重压：各国禀赋与获益能力不同，是美国村问题的重演，但在地球村层面并无第二个地球村可以容纳“各得其所”。", "evidence": ["E28"] },
    { "claim_id": "C023", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为只有一种处理手段：一面拥有足够的武力震慑，另一面主动释放物质利益换取社会资本；这两条策略对受益的全体国家整体有效，非如此不可。", "evidence": ["E30"] },
    { "claim_id": "C024", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作者提出历史最终只有一种剧情：新的“生产力之王”先将一切软硬武力威胁震慑住使对方暴力尝试彻底失败，再主动以物质倾斜换取国际关系与秩序调整，而不是无条件施舍；只有这种结果有最大稳定性。", "evidence": ["E32"] },
    { "claim_id": "C025", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为中国已看到这个总趋势并已行动：一方面飞速军事现代化和先进化，另一方面推进一带一路倡议和“人类命运共同体”的新利益分配框架。", "evidence": ["E34"] },
    { "claim_id": "C026", "claim_type": "quoted_or_cited", "attribution": "cited_source", "modality": "asserted", "statement": "作者引《论语·季氏》“不患寡而患不均，不患贫而患不安”为据。", "evidence": ["E35"] },
    { "claim_id": "C027", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者提出受惠国可扩大门户开放和市场准入，让对全球化不满者以个人身份参与利益分享，这是对反全球化集团性势力釜底抽薪的策略；其经典实践是隋唐科举制，令动乱力量失去智力和组织资源。", "evidence": ["E36"] },
    { "claim_id": "C028", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者归结：全球化是生产力的发展，反全球化是生产关系的诉求；生产关系可一时延缓生产力发展速度，但最终总会自我调整到适应新的生产力。", "evidence": ["E38"] },
    { "claim_id": "C029", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者补充限定：除非人类放弃对物质生活的无限追求，否则这是无可逆转的宏观规律。", "evidence": ["E39"] },
    { "claim_id": "C030", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为盯住这两个主要议题在各地区的进程，就能看到全球化低潮和高潮交替的节奏；至于作出什么判断，是各人自己要做的功课。", "evidence": ["E40"] },
    { "claim_id": "C031", "claim_type": "author_reported", "attribution": "unknown", "modality": "asserted", "statement": "作者转述：很多人都在喊疫情会导致各国回迁各种产业、努力提高自给自足的水平，以防再次出现这种突发窘境。", "evidence": ["E41"] },
    { "claim_id": "C032", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者反问回迁产业链预防突发窘境在经济上的逻辑是否成立，并指出产业自由流动是因为效率最好、成本最低，改变状态就会成本更高、产品价格更高。", "evidence": ["E42", "E43"] },
    { "claim_id": "C033", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者认为只有在中国自己因为某种原因肯定不会卖给你更便宜的产品的前提下，这种更高的成本才会变成实际上最低的成本。", "evidence": ["E44"] },
    { "claim_id": "C034", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者反问：就算确信中国会在疫情期间卡脖子要挟，那么非疫情期间呢？中国也会故意在平时就不卖口罩给其他国家吗？", "evidence": ["E45"] },
    { "claim_id": "C035", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者判断若仅仅担心非常时期被卡脖子，回迁生产线显然愚蠢，远不如在和平的非禁运时期建立战略储备。", "evidence": ["E46"] },
    { "claim_id": "C036", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者反问“你怎么可能比中国便宜”，并判断选择回迁生产线来自行生产储备所花费的额外金钱是纯粹的浪费。", "evidence": ["E48"] },
    { "claim_id": "C037", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者指出“储备耗尽时自产”意味着产能要有足够规模应付突发的巨量需求，并反问这个巨大产能规模在没有疫情的漫长时期内怎么养活；一天不发生疫情就要净亏一天。", "evidence": ["E49", "E50"] },
    { "claim_id": "C038", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作者预判头几年大家积极性很高、一致认为“非如此不可”，疫情过去还没满两年就会有呼声表示“这很愚蠢”。", "evidence": ["E51"] },
    { "claim_id": "C039", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作者预判届时算账：回迁生产线的成本完全沉没，只剩过时设备可廉价拍卖，补贴两年买自产高价口罩的成本超过向中国直接购买数倍。", "evidence": ["E52"] },
    { "claim_id": "C040", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为强行回迁只能靠财政收入一直养、强迫本国居民以更高价格购买更差产品，且这还是在疫情过后经济萧条、国债负担沉重、货币信用近崩溃的前提下，并挤占复苏资源。", "evidence": ["E54"] },
    { "claim_id": "C041", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者认为这种主张要长期获得足够支持有一个绝对必要的前提：来自中国的坚决的、无情的、绝不妥协的、显然恶意的、无休无止的禁运；不存在这种禁运，回撤的逻辑就整个失去基本合理性。", "evidence": ["E55"] },
    { "claim_id": "C042", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作者预判这种回迁主张到最后多半亏得一沓糊涂而被迫放弃。", "evidence": ["E56"] },
   ],
   "argument_steps": ["界定全球化并概括其本质为“商品经济最大化”（P001-P003）。", "把问题转为有没有力量能让商人放弃最极限利润（P004-P006）。", "论证集体干预须均匀统一，否则被限制者只有战或逃，且该规律不可抗拒（P007-P011）。", "提出极限论：物理极限与动态软极限，据此说明全球化走向的不均匀与统计口径问题（P012-P019）。", "主张关注局部主要议题而非全球总趋势（P020-P023）。", "展开第一议题：收益区域内再分配、平衡点迁移、社会资本处境（P024-P028）。", "以村十一人算例说明极化与市场竞争失灵（P029-P032）。", "重新解释中美贸易战的性质与成本承担者，指出受阻的根本原因（P033-P037）。", "讨论富翁为何不轻易就范与妥协的两难（P038-P041）。", "给出全民所有制与国有经济主体化的答案，并称美国在做隐性国有化（P042-P045）。", "警告该方案的政治后果并作宋江之喻；说明中国与资源型国有国家的承受力（P046-P053）。", "展开第二议题：地缘政治格局承受重压与最终稳态的剧情（P054-P064）。", "指出中国已行动，引《论语》为据，补充门户开放与科举制原理（P065-P070）。", "归结为生产力与生产关系的宏观规律并给出观察方法（P071-P075）。", "回应疫情：先反驳回迁的经济逻辑，再反驳战略储备与产能维持的理由（P076-P100）。"],
   "concept_usage": [
    { "term": "全球化", "meaning": "作者的操作性界定：采集全球最好的原料、人力、技术，生产最多人需要的产品，卖到一切可卖之处；本质是商品经济最大化。", "evidence": "P002、P003", "ambiguity": "作者自设定义，未说明与常见经济学定义的关系。" },
    { "term": "软极限", "meaning": "多种因素围成的动态边界：超过就被往回拉，回弹到显著低于它后又反弹，如此反复。", "evidence": "P015、P016", "ambiguity": "由哪些因素围成、如何度量，作者未列举。" },
    { "term": "社会资本", "meaning": "全民享有但无主、无人能有效捍卫者；全球化会将其没收并倾斜给密切参与全球化的阶层。", "evidence": "P027、P028", "ambiguity": "作者未下定义，与常见社会学用法是否一致不明。" },
    { "term": "全民所有制、国有经济主体化", "meaning": "作者提出的答案：实质上由全民持有最有利润的优势产业，外贸利润用于全民普惠的基础建设，形成正循环。", "evidence": "P042、P043", "ambiguity": "与既有制度的对应关系和实施路径未说明。" },
    { "term": "隐性国有化", "meaning": "作者用来指美国征收必然由富翁承担的超额贸易税、本质上实现上述设计。", "evidence": "P044、P045", "ambiguity": "属作者判断与命名，非官方表述。" },
    { "term": "生产力之王", "meaning": "历史最终剧情中先震慑住一切软硬武力威胁、再主动重新分配部分利益的新胜出者。", "evidence": "P062", "ambiguity": "所指的具体国家或主体，作者未点名。" },
    { "term": "以工代赈", "meaning": "作者借指中国以大规模全局性投资实现内部按劳分配与底线保障领域均沾的做法。", "evidence": "P051", "ambiguity": "具体财政安排未说明。" },
   ],
   "examples_and_targets": ["村里十一人的算例：10人每月盈余50、一人500，全球化后整体增1000而一人独得800、其余各得20（作者自设说明性算例）", "“中美贸易战”（作者重新解释为美国内部掉队者与弄潮儿之争，非国家间战争）", "把工厂从中国迁到越南（作者举为这种斗争波及的明证）", "土匪绑票要一两千块、远比请保镖便宜，却苦于没有给钱而无后患的方法（类比妥协两难）", "川普被比作美国村民的宋江（引《水浒》人物作比，并称宋江下场并不美好）", "卡塔尔、沙特、阿联酋、文莱、新加坡、日本、韩国（举为资源国有或变相国有而承受力更强的例子）", "《论语·季氏》“不患寡而患不均，不患贫而患不安”（引用）", "隋唐科举制（举为以筛选机制吸纳精英、削弱动乱力量的经典实践）", "疫情下各国回迁产业、储备十亿二十亿口罩、一个体育场、又一个十七年（反驳回迁论的材料）"],
   "conditions": ["“如果这个力量是来自于某种人类的集体主动干预”——均匀统一干预论证的前提。", "“除非消灭商品经济这种现象”——不可抗拒性的例外条件。", "“只有全球化达到并超越了它应有的极限，才有可能向下回归”——回归的前提。", "“除非存在一种‘全球发展指数基金’给你买卖”——讨论总趋势是否有意义的前提。", "“如果较好的控制住贪污问题”——资源型国家承受力结论的附加条件。", "“这只有在中国自己因为某种原因肯定不会卖给你更便宜的产品的前提下”——回迁成本论证的前提。", "“如果仅仅只是担心非常时期会被卡脖子”——判定回迁愚蠢所针对的情形。", "“只要事实证明根本不存在这种恶意禁运”——回撤逻辑成立与否的条件。", "“除非人类放弃对物质生活的无限追求”——宏观规律陈述的限定。", "“有要求要谈一谈疫情对全球化的影响”——P076 起补充部分的写作缘起。"],
   "rhetoric_and_tone": "长篇论说文的推演语气：先立定义再逐层设问（“最根本的问题是……”“那么，问题就转化成了……”）；大量比喻意象（全球化像空气、铜墙铁壁、一锅五颜六色疙瘩汤、篱笆的桩子、动力源关机）与自设算例；夹用口语俚语（疙瘩汤、闹事有钱拿、伊于胡底、亏得一沓糊涂）；反问与设问（“它在经济上的逻辑成立吗？”“而你怎么可能比中国便宜？”）；引《论语》《水浒》与历史类比（隋唐科举制、万有引力定律、RGBA 色彩空间）；以第二人称给出方法与功课。",
   "unresolved_questions": ["“软极限”由哪些因素围成、如何度量，作者未列举；P018 用一维曲线、二维平面、三维几率云、RGBA 四元色作比并逐一判为不足，未给出替代表达。", "“全球发展指数基金”只是作者设想的假设物，现实中有无对应机制未说明。", "“社会资本”未定义；“生产力之王”所指主体未点名。", "各国例子（卡塔尔、沙特、阿联酋、文莱、新加坡、日本、韩国）的资产归属与“控制住贪污”程度均为作者断言，待外部核查。", "“又一个十七年后”暗指某次相隔十七年的疫情，作者未说明所指。", "P076“有要求要谈一谈疫情对全球化的影响”表明该部分为应约补充，成文与发表时间未说明；元数据 updated_at 2025-02-20 晚于 published_at 2020-04-19，是否有后改不明。", "无图片节点，图片状态 not_applicable。"],
   "evidence": [
    { "key": "E1", "paragraph_id": "P002", "quote": "所谓的全球化，一言以蔽之，是指采集全球最好的原料、雇佣全球最好的人力", "relation": "supports" },
    { "key": "E2", "paragraph_id": "P003", "quote": "本质上，所谓的全球化就是“商品经济最大化”。", "relation": "supports" },
    { "key": "E4", "paragraph_id": "P007", "quote": "这种干预必须保证均匀而统一的施加到所有的市场玩家身上。", "relation": "supports" },
    { "key": "E5", "paragraph_id": "P011", "quote": "除非消灭商品经济这种现象，否则它就必须按照这个规则行事", "relation": "supports" },
    { "key": "E6", "paragraph_id": "P012", "quote": "全球化就像空气，一定会进展到它自己能扩展到的极限才会止步。", "relation": "supports" },
    { "key": "E7", "paragraph_id": "P014", "quote": "物理极限是全球化的铜墙铁壁，是不可能超过的。", "relation": "supports" },
    { "key": "E8", "paragraph_id": "P015", "quote": "超过软极限，就会有力量把你往回拉", "relation": "supports" },
    { "key": "E9", "paragraph_id": "P017", "quote": "而是一个在不同的地域、不同的行业、朝着不同方向、不同的维度不均匀的波动着的过程。", "relation": "supports" },
    { "key": "E10", "paragraph_id": "P020", "quote": "比较有意义的，是要去理解影响各地区、各行业的局部全球化策略倾向的几大主要议题", "relation": "supports" },
    { "key": "E11", "paragraph_id": "P025", "quote": "全球化高度有利于进出口部门，但对该部门之外的人利益较小。", "relation": "supports" },
    { "key": "E12", "paragraph_id": "P027", "quote": "但是社会资本是无主的、是没有人能有效捍卫的，而商业资本是有主的", "relation": "supports" },
    { "key": "E13", "paragraph_id": "P028", "quote": "将全民享有的社会资本没收，将其倾斜到部分密切参与全球化的阶层", "relation": "supports" },
    { "key": "E14", "paragraph_id": "P029", "quote": "却是这个人一人独得800，剩下每人各得20", "relation": "supports" },
    { "key": "E15", "paragraph_id": "P032", "quote": "就会触发非经济手段的抑制全球化的能量。", "relation": "supports" },
    { "key": "E16", "paragraph_id": "P033", "quote": "而是发生在美国的全球化掉队者和弄潮儿之间。", "relation": "supports" },
    { "key": "E17", "paragraph_id": "P034", "quote": "几乎完全是在由美国的富翁们承受。", "relation": "supports" },
    { "key": "E18", "paragraph_id": "P036", "quote": "全球化就不会获得进一步扩大的许可。", "relation": "supports" },
    { "key": "E19", "paragraph_id": "P039", "quote": "但却没有无制度和伦理后患的妥协的逻辑。", "relation": "supports" },
    { "key": "E20", "paragraph_id": "P042", "quote": "那就是全民所有制以及国有经济主体化。", "relation": "supports" },
    { "key": "E21", "paragraph_id": "P045", "quote": "这就是一种隐性的国有化。", "relation": "supports" },
    { "key": "E22", "paragraph_id": "P047", "quote": "富翁们才是最大的政治霸权势力。", "relation": "supports" },
    { "key": "E24", "paragraph_id": "P050", "quote": "相当微妙的缓和了全球化对中国的极化效应。", "relation": "supports" },
    { "key": "E25", "paragraph_id": "P051", "quote": "中国战略性的选择了将它转化为高铁、全面城市化、军事现代化", "relation": "supports" },
    { "key": "E26", "paragraph_id": "P052", "quote": "可以大胆的展开一切进攻性的策略。", "relation": "supports" },
    { "key": "E27", "paragraph_id": "P053", "quote": "也会对全球化有更大的承受力。", "relation": "supports" },
    { "key": "E28", "paragraph_id": "P054", "quote": "全球化的第二个议题，就是地缘政治格局承受重压。", "relation": "supports" },
    { "key": "E30", "paragraph_id": "P059", "quote": "一面拥有足够的武力震慑", "relation": "supports" },
    { "key": "E32", "paragraph_id": "P062", "quote": "就是最后新的“生产力之王”首先将一切软硬武力威胁震慑住", "relation": "supports" },
    { "key": "E34", "paragraph_id": "P066", "quote": "另一方面在突飞猛进的推进一带一路倡议和“人类命运共同体”的新利益分配框架。", "relation": "supports" },
    { "key": "E35", "paragraph_id": "P068", "quote": "不患寡而患不均，不患贫而患不安。", "relation": "supports" },
    { "key": "E36", "paragraph_id": "P069", "quote": "也是对反全球化的集团性势力釜底抽薪的一种策略。", "relation": "supports" },
    { "key": "E38", "paragraph_id": "P071", "quote": "全球化是生产力的发展，反全球化是生产关系的诉求。", "relation": "supports" },
    { "key": "E39", "paragraph_id": "P073", "quote": "否则这是无可逆转的宏观规律。", "relation": "supports" },
    { "key": "E40", "paragraph_id": "P074", "quote": "你就能看到全球化低潮和高潮交替的节奏", "relation": "supports" },
    { "key": "E41", "paragraph_id": "P077", "quote": "很多人都在喊疫情会导致各国回迁各种产业", "relation": "supports" },
    { "key": "E42", "paragraph_id": "P078", "quote": "它在经济上的逻辑成立吗？", "relation": "supports" },
    { "key": "E43", "paragraph_id": "P079", "quote": "当然是因为这样效率是最好的、成本是最低的。", "relation": "supports" },
    { "key": "E44", "paragraph_id": "P081", "quote": "这种更高的成本才会变成实际上最低的成本。", "relation": "supports" },
    { "key": "E45", "paragraph_id": "P082", "quote": "中国也会故意在平时就不卖口罩给其他国家吗？", "relation": "supports" },
    { "key": "E46", "paragraph_id": "P083", "quote": "远远不如在和平的非禁运时期建立战略储备。", "relation": "supports" },
    { "key": "E48", "paragraph_id": "P087", "quote": "这是纯粹的浪费。", "relation": "supports" },
    { "key": "E49", "paragraph_id": "P089", "quote": "这个巨大的产能规模，在没有疫情的漫长时期内怎么养活？", "relation": "supports" },
    { "key": "E50", "paragraph_id": "P090", "quote": "一天不发生疫情，就要净亏一天", "relation": "supports" },
    { "key": "E51", "paragraph_id": "P092", "quote": "就会有各种呼声表示“这很愚蠢”", "relation": "supports" },
    { "key": "E52", "paragraph_id": "P093", "quote": "回迁生产线的成本完全沉没", "relation": "supports" },
    { "key": "E54", "paragraph_id": "P096", "quote": "国债负担沉重到利息都快扛不起、货币信用都快崩溃的前提下。", "relation": "supports" },
    { "key": "E55", "paragraph_id": "P098", "quote": "就是来自中国的坚决的、无情的、绝不妥协的、显然恶意的、无休无止的禁运。", "relation": "supports" },
    { "key": "E56", "paragraph_id": "P100", "quote": "而且到最后多半亏得一沓糊涂而被迫放弃。", "relation": "supports" },
   ],
  },
  "provisional_tags": {
   "domain_candidates": ["全球化与国际贸易", "政治经济学", "国际关系", "产业政策", "疫情与供应链"],
   "issue_candidates": ["逆全球化", "全球化收益的区域内再分配", "软极限", "中美贸易战的性质", "全民所有制与国有经济", "地缘政治格局承受重压", "产业链回迁与战略储备"],
   "text_function_candidates": ["答疑", "理论推演", "时评", "论辩"],
   "object_candidates": ["全球化", "中国", "美国", "越南", "川普", "宋江", "卡塔尔", "沙特", "阿联酋", "文莱", "新加坡", "日本", "韩国", "一带一路", "人类命运共同体", "《论语·季氏》", "隋唐科举制"],
   "working_keywords": ["全球化", "商品经济最大化", "物理极限", "软极限", "社会资本", "商业资本", "区域内再分配", "中美贸易战", "全民所有制", "国有经济主体化", "隐性国有化", "以工代赈", "生产力之王", "战略储备", "回迁生产线", "恶意禁运"],
  },
  "notes": "无图片节点（not_applicable）。问答体长文：Q001 问“如何看待逆全球化？”，作者自设定义后推演，提问者立场未归给作者。P068 为《论语·季氏》引文块（field=quote），按 quoted_or_cited/cited_source 记录。P076 起为应约补充，划为 U011、U012。P048 宋江、P039 土匪绑票均为作者比喻，P029 村十一人算例为自设说明性算例，非统计数据。",
 },
 "557cd798": {
  "analysis": {
   "question_context": "提问者（Q001）问“分手后真的能看出一个人的人品吗？”。作者没有直接评论提问者的预设，而是先纠正“相处是因为爱、分开是因为不爱”的流行看法，区分爱与贪，用一套“爱的能力/被爱的能力”与“爱的公式”说明爱在账面上必然亏损、但在人生意义上永不亏损，最后把“人品”归结为是否遵奉这套爱的逻辑，从而回应提问。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004", "P005"], "summary": "立论：相处因为爱、分开因为不爱是错的；分开时觉得不爱乃至生恨者若诚实追问会意识到那从一开始就不是爱。生于非爱的关系走到终点，剩屈辱、不甘、沮丧、狂怒，要公平、要勉强、要补偿，求而不得则要报复。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P006"], "summary": "作者代拟分手双方互相追责的口吻：“你吃亏？当初谁强迫你来？……你还‘报复’我？！”", "role": "example"},
    {"unit_id": "U003", "paragraph_refs": ["P007", "P008", "P009", "P010", "P011", "P012"], "summary": "两个贪鬼以为可以“合作双赢”互补，其打算的本质是以我变成你的奴隶换你变成我的奴隶；作者反问双方是否受过当奴隶与奴隶主的训练，指出这只是赌对方是足够仁慈的奴隶主，而对方也这样想。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P013", "P014", "P015", "P016"], "summary": "期望落空后，贪婪成性的人不可能丢开守了几十年的逻辑，必然把分开变成仇恨；贪婪者找贪婪者互补，除非半道双双醒悟，只要一个不醒悟就必然化身无间地狱；不悔改者觉得都是对方的错，换人只会重蹈覆辙。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P017", "P018", "P019", "P020"], "summary": "从旧牢房换到新牢房不等于出狱；顶多因没有本钱再挣扎而无限委曲求全、相信自己能适应地狱，作者以“地狱可是创意无限的”作讽。", "role": "example"},
    {"unit_id": "U006", "paragraph_refs": ["P021", "P022", "P023", "P024", "P025", "P026"], "summary": "爱是爱，贪是贪。爱遵守的基本逻辑是对方不能因我的存在而受无谓的痛苦，最好比没和我接触过有净收益；这没有“我必须不吃亏／够本／不委屈／有面子”等前提，无论如何都不能让对方还受我的任性贪婪的额外损失。", "role": "definition"},
    {"unit_id": "U007", "paragraph_refs": ["P027", "P028", "P029", "P030", "P031", "P032", "P033", "P034"], "summary": "人必定无能、任性和贪婪，与人交往就必须忍受这些；想要对方得到好处要在接受这些代价的前提下达成。对方得一分而你常付出101分，如何把付出降到91分、10分乃至1.5分是爱的技能问题而非原则问题；把爱的成本控制在可承受范围内、为因自己无能而产生的代价负责，都是自己的责任。", "role": "claim"},
    {"unit_id": "U008", "paragraph_refs": ["P035", "P036", "P037", "P038", "P039", "P040", "P041", "P042", "P043", "P044", "P045", "P046", "P047"], "summary": "爱的能力是有效性的度量、被爱的能力是无效性的度量；作者给出爱的公式 N = P*E − U，E永远低于1、U永远大于0，故N永远小于P。对欠缺能力的两人，甲只得1分而乙付出101分，双方都觉得不公——这是隐藏在亲密关系中的撒旦、逻辑的魔鬼。", "role": "definition"},
    {"unit_id": "U009", "paragraph_refs": ["P048", "P049", "P050"], "summary": "遵循“保本获利”法则的人的爱最终必然在质问下哑口无言；父母教孩子“机灵点，要拎得清”，是因为本能察觉到爱是从账面上看必然亏损的生意。人的无能任性贪婪只有程度问题，故人类无效性长期不可能为0，无效性低于0的只能是全知全能、自有永有、无欲无求的上帝。", "role": "reason"},
    {"unit_id": "U010", "paragraph_refs": ["P051", "P052", "P053", "P054", "P055", "P056"], "summary": "爱的第一个支撑：低无效性、高有效性的两人合作有更强比较竞争优势，能在社会分配中分得更大份额，赢得选举与市场竞争、借助赢家通吃较易获得物质成功——自然之中设计了奖励爱人者的内在逻辑；但物质充裕不足以抵消关系本身的无效性，心伤是无价的。", "role": "reason"},
    {"unit_id": "U011", "paragraph_refs": ["P057", "P058", "P059", "P060", "P061", "P062", "P063"], "summary": "第二个支撑是人生的意义：生命终将逝去，避免损失在终极意义上不成其为收益；人生是以必然损失的一切换取可能幸存的一切的游戏。付出101分换了1分不算吃亏，因为那101分本来就要消失——这就是爱之所以永不亏损的真正逻辑。", "role": "claim"},
    {"unit_id": "U012", "paragraph_refs": ["P064", "P065", "P066", "P067", "P068", "P069", "P070", "P071"], "summary": "明白这个逻辑，若不得不分开就不会成为被激怒的恶魔，因为没有亏损、冤屈与失败就不会惩罚、追讨、报复。人与人最大的障碍是对关系终结时可能遭受的追索、惩罚和报复的畏惧；“但凡爱最后必破产”导致“我不要爱了”，这就是不安全感的根源。", "role": "claim"},
    {"unit_id": "U013", "paragraph_refs": ["P072", "P073", "P074", "P075", "P076", "P077", "P078", "P079", "P080"], "summary": "在遵从爱的逻辑的人看来，那101不是对方欠下而是自己花掉的——买的是把自己的1分生命寄存到对方身上、不再因自己死亡而消失的终极价值；没买到是自己无能，不是对方无义，故没有可报复的理由、只可能有感谢的理由，这样的人每一个都是珍宝。结论：在一起是因为爱，分开是因为更爱；看得懂这个逻辑就是所谓“人品”的本质，否则只是放长线钓大鱼的诡计。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者否定“相处是因为爱、分开是因为不爱”：分开时觉得自己已经不爱乃至开始恨的人，若对自己足够诚实且追问到底，会意识到从一开始那个就不是爱。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为生于非爱的关系走到终点，欲望消散后剩下的是屈辱、不甘、沮丧、狂怒，要公平、要勉强、要补偿；求而不得则要报复。", "evidence": ["E3", "E4"]},
    {"claim_id": "C003", "claim_type": "quoted_or_cited", "attribution": "unknown", "modality": "asserted", "statement": "作者代拟分手双方互相追责的口吻（“你吃亏？当初谁强迫你来？你自愿的，你报复我？……”），以呈现追责逻辑而非陈述事实。", "evidence": ["E5"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者判断两个贪鬼的“合作双赢”互补，本质是想以我变成你的奴隶、换你变成我的奴隶，好让双方各有一个奴隶。", "evidence": ["E6", "E7"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者反问双方是否受过当奴隶与当奴隶主的训练，并指出敢这样赌只是赌对方是足够仁慈的奴隶主，而对方也这样想。", "evidence": ["E8", "E9"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为贪婪的人找贪婪的人互补，除非半道双双醒悟，只要一个不醒悟就必然化身无间地狱；习惯把错误总结在别人身上的人必不能摆脱重蹈覆辙的命运。", "evidence": ["E10", "E11"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者提出爱遵守的基本逻辑是对方不能因我的存在而受无谓的痛苦，尤其是不能受我主动施加的痛苦，最好能做到比没和我接触过有净收益。", "evidence": ["E12"]},
    {"claim_id": "C008", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者强调这个基本原则没有前提：没有“我必须不吃亏／够本／不委屈／有面子”，无论自己多失望、屈辱、无辜、吃亏都不改变；也不能让对方在交往必然的不便与我的无能造成的损失之外，再受我的任性贪婪的额外损失。", "evidence": ["E13", "E14"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为人必定是无能、任性和贪婪的，只要与人交往就必须忍受这些，想要对方得到好处只能在这前提下达成。", "evidence": ["E15"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为事情常常是对方要得到一分而你实际付出101分，不管是否公平世界就是这样安排的；如何只付出91分、10分乃至1.5分就让对方得到1分，是爱的技能问题，与爱的原则无关。", "evidence": ["E16", "E17"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张磨练爱的能力、把爱的成本控制在能承受的范围之内，是选择爱人者必须解决并自己承担的责任；因自己的无能而产生承受不起的代价，是为自己的决策错误承担责任。", "evidence": ["E18", "E19"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者定义：爱的能力是付出多少分就能让对方得到多少分的有效性的度量（与绕过和处理他人无能任性贪婪的能力有关）；被爱的能力是让对方要付出多少自己才能得到一分的无效性的度量（与对自身无能任性贪婪的管理有关）。", "evidence": ["E20", "E21"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者给出爱的公式：被爱者的净所得 N = 爱者的付出P*有效性系数E − 被爱者的无效性U；E永远低于1、U永远大于0，所以N永远小于P。", "evidence": ["E22", "E23"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为对欠缺爱与被爱能力的两人而言，甲只得1分而乙付出101分、双方都觉得不公，这就是隐藏在亲密关系中的撒旦、逻辑的魔鬼。", "evidence": ["E24"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者判断每一个遵循“保本获利”法则的人的爱最终都必然在那质问下哑口无言；父母教孩子“机灵点，要拎得清”，是因为本能察觉到爱是一项从账面上看必然亏损的生意。", "evidence": ["E25"]},
    {"claim_id": "C016", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者认为人的无能、任性和贪婪只有程度问题，因此人类的无效性在长期看不可能为0；无效性低于0的只可能是全知全能、自有永有、无欲无求的上帝。", "evidence": ["E26"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者提出爱的第一个支撑：低无效性、高有效性的两人合作有更强的比较竞争优势，能在社会分配中分得更大份额并获得物质成功——自然之中设计了奖励爱人者的内在逻辑。", "evidence": ["E27"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者指出即使如此，物质的安全乃至充裕并不足以真正抵消关系本身的无效性，心伤是无价的。", "evidence": ["E28"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者提出第二条救赎是人生的意义：生命终将逝去，避免损失在终极意义上不成其为收益；人生是以必然损失的一切换取可能幸存的一切的游戏。", "evidence": ["E29"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为付出101分换了1分并没有吃亏，因为那101分本来就是要消失的；只要换到1分，就比1分都没换到、最后全被没收要强，这就是爱之所以永不亏损的真正逻辑。", "evidence": ["E30", "E31"]},
    {"claim_id": "C021", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为明白这个逻辑的人若不得不分开，就不会成为被激怒的恶魔；既然没有亏损、冤屈和失败，就不会惩罚、追讨、报复。", "evidence": ["E32"]},
    {"claim_id": "C022", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者指出人与人最大的障碍是对将来关系终结时可能遭受的追索、惩罚和报复的畏惧；由“但凡爱最后必破产”推出“我不要爱了”，这就是不安全感的根源。", "evidence": ["E33", "E34"]},
    {"claim_id": "C023", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为在真正懂得并遵从爱的逻辑的人看来，那101不是对方欠下而是自己花掉的——买的是把自己的1分生命寄存到对方身上、不再因自己死亡而消失的终极价值；没买到是自己无能，不是对方无义。", "evidence": ["E35", "E36"]},
    {"claim_id": "C024", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为从始至终没有可报复的理由、只可能有感谢的理由，这样的人每一个都是珍宝；财富、权势、美貌都不足以抵消这个基本认知带来的价值，否则只会变成欠下的债和架在脖子上的刀、套在脚上的锁链。", "evidence": ["E37", "E38"]},
    {"claim_id": "C025", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者结论：对于懂得的人，在一起是因为爱，分开是因为更爱。", "evidence": ["E39"]},
    {"claim_id": "C026", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者回答提问：看得懂这个逻辑就是所谓“人品”的本质；如果不是因为遵奉这个逻辑，那只不过是放长线钓大鱼的诡计罢了。", "evidence": ["E40"]}
   ],
   "argument_steps": [
    "否定“分开是因为不爱”的流行看法，指出那从一开始就不是爱（P001-P003）。",
    "描述非爱关系终点的索偿与报复逻辑（P004-P005），并以代拟的双方互责口吻呈现（P006）。",
    "剖析“贪鬼互补”的打算本质是互为奴隶主与奴隶，并反问其可行性（P007-P012）。",
    "推论期望落空后必然产生仇恨，不悔改者换人也会重蹈覆辙（P013-P016）。",
    "以换牢房、委曲求全、适应地狱的比喻说明这种厄运没得逃（P017-P020）。",
    "给出爱的基本逻辑及其“没有前提”的无条件性（P021-P026）。",
    "以人的无能任性贪婪为前提，说明对方得1分往往要你付出101分，并区分技能问题与原则问题、责任归属（P027-P034）。",
    "定义爱的能力与被爱的能力，给出爱的公式与亏本结构，称之为逻辑的魔鬼（P035-P047）。",
    "说明遵循保本获利者的爱必然哑口无言，并追问无效性能否为0（P048-P050）。",
    "给出爱的两个支撑之一：奖励爱人者的社会竞争逻辑，但物质不足以抵消心伤（P051-P056）。",
    "给出第二个支撑：以必然损失换取可能幸存的人生意义，故爱永不亏损（P057-P063）。",
    "说明懂此逻辑者不会报复，并指出畏惧追索报复是不安全感的根源（P064-P071）。",
    "重述101分是自己花掉的、买的是生命寄存的终极价值，故无可报复只可感谢（P072-P075）。",
    "以格言式短句收束，并把“人品”归结为是否遵奉这套逻辑（P076-P080）。"
   ],
   "concept_usage": [
    {"term": "爱", "meaning": "作者在本文中把爱与贪对举：爱遵守“对方不能因我的存在而受无谓的痛苦、最好有净收益”的逻辑，且没有保本获利之类的前提。", "evidence": "P022、P023", "ambiguity": "作者用“爱”同时指原则、能力与关系，未作术语区分。"},
    {"term": "贪（贪鬼）", "meaning": "以互补为名互相贪求对方天然有而不匮乏之物的关系动机；作者称以贪立身者不可能在分手时丢开这套逻辑。", "evidence": "P007、P013", "ambiguity": "作者未界定贪的边界，与正常需求如何区分不明。"},
    {"term": "爱的能力／被爱的能力", "meaning": "爱的能力＝付出多少分就能让对方得到多少分的有效性度量；被爱的能力＝让对方要付出多少自己才能得到一分的无效性度量。", "evidence": "P037、P038", "ambiguity": "两项能力如何测量、能否训练到何种程度，作者未说明。"},
    {"term": "有效性系数E／无效性U／净所得N", "meaning": "作者自设的公式记号：N = P*E − U，E永远低于1，U永远大于0，故N永远小于P。", "evidence": "P040、P041", "ambiguity": "P、E、U、N均无量纲与测量方法说明，属作者自设的说明性公式。"},
    {"term": "无间地狱／地狱", "meaning": "作者用来比喻贪婪者互补关系的必然结局，以及“相信自己能适应地狱”的状态。", "evidence": "P014、P018、P020", "ambiguity": "佛教用语被移用于亲密关系，作者未说明取义范围。"},
    {"term": "人品", "meaning": "文章结尾把“看得懂这个逻辑”（即遵奉爱的逻辑）称为“人品”的本质，用以回答提问者。", "evidence": "P080", "ambiguity": "作者只给出这一种判定，未讨论识别方法与误判可能。"},
    {"term": "放长线钓大鱼的诡计", "meaning": "作者对不遵奉上述逻辑却看似有“人品”的行为的定性。", "evidence": "P080", "ambiguity": "属修辞性判断，作者未给判定标准。"}
   ],
   "examples_and_targets": [
    "两个贪鬼的“合作双赢”互补（作者对关系动机的刻画，非具体个案）",
    "“两个领钱上班都满腹怨言，不知服从为何物的小朋友”（作者类比）",
    "奴隶与奴隶主、旧牢房换新牢房、无间地狱、吃一口糖断一根手指、架在脖子上的刀与套在脚上的锁链（作者比喻）",
    "父母教导孩子“机灵点，要拎得清”（作者举为社会现象）",
    "选举与市场竞争、赢家通吃、拿走失败关系中的人的配额（作者用来说明奖励爱人者的社会机制）",
    "全知全能、自有永有、无欲无求的上帝（作者举为无效性低于0的唯一可能）",
    "提问者的问题“分手后真的能看出一个人的人品吗？”（本文的回应对象，属提问者）"
   ],
   "conditions": [
    "“除非半道双双醒悟”——贪婪者互补关系可能不恶化成地狱的例外条件。",
    "“如果你们真训练有素，那还说不定真有点希望”——假设性让步条件。",
    "“只要一个不醒悟”——关系必然化身无间地狱的条件。",
    "“最好，能做到比没和我接触过有净收益”——爱的逻辑中的更高要求，非硬性前提。",
    "“将爱的成本控制在你自己能承受的范围之内”——对爱人者的要求。",
    "“人类的无效性在长期看不可能为0”——结论的时间限定。",
    "“如果因为某个原因不得不分开”——不成为恶魔所针对的情形。",
    "“如果没有这个基本认知”——财富、权势、美貌变成债与刀锁的条件。"
   ],
   "rhetoric_and_tone": "训诫与论说混合的语气，全篇以第二人称“你／你们”直接对读者说话；反问与设问密集（“你们受过奴隶的训练吗？”“就等于出狱了吗？”“你怎么会惩罚、追讨、报复？”）；比喻成串（贪鬼、奴隶主、无间地狱、牢房、吃糖断指、刀与锁链）；夹用讽刺（“这可真要祝你好运——地狱可是创意无限的”）；中段引入自设公式作“算账”式论证；结尾用格言式短句分行收束（“在一起，是因为爱。分开，是因为更爱。”），并把全文落到“人品”二字上回应提问。",
   "unresolved_questions": [
    "提问者问的是“能不能看出”一个人的人品，作者只给出人品的判定标准（是否遵奉爱的逻辑），未讨论如何在分手情境中识别、以及误判的可能。",
    "爱的公式中 P、E、U、N 均为作者自设记号，文中未说明如何度量，也未给任何数据。",
    "P050 写“无效性低于0的，只可能是……上帝”，与前文“无效性在长期看不可能为0”并置，用词是否应为“等于0”作者未说明。",
    "文中“很多人”“千千万万的父母”等为概括性表述，没有具体案例、统计或出处。",
    "无图片节点，图片状态 not_applicable；正文与 lexical 结构一致（结构节点统计为 paragraph 80）。",
    "元数据 updated_at（2021-05-23）晚于 published_at（2020-04-27），是否有后改不明。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "很多人以为相处是因为爱，分开是因为不爱。", "relation": "context"},
    {"key": "E2", "paragraph_id": "P003", "quote": "从一开始那个就不是爱。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "要公平、要勉强、要补偿。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P005", "quote": "终于求任一而不得，于是要报复。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P006", "quote": "你吃亏？当初谁强迫你来？", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P007", "quote": "两个贪鬼，以为可以“合作双赢”", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P008", "quote": "是想以我变成你的奴隶，换你变成我的奴隶。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P009", "quote": "你们受过奴隶的训练吗？", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P010", "quote": "无非是在赌对方一定是一个足够仁慈的奴隶主", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P014", "quote": "否则只要一个不醒悟，这关系都必然最终化身无间地狱。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P016", "quote": "必不能摆脱重蹈覆辙的命运。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P022", "quote": "对方不能因我的存在而受无谓的痛苦", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P023", "quote": "这是没有前提的", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P024", "quote": "还受到来自我的任性、我的贪婪的额外的损失。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P027", "quote": "因为人必定是无能、任性和贪婪的。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P030", "quote": "而你实际付出的是101分。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P032", "quote": "这是爱的技能问题，与爱的原则无关。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P033", "quote": "将爱的成本控制在你自己能承受的范围之内", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P034", "quote": "是你要为自己的决策错误而承担的责任。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P037", "quote": "就是付出多少分就能让对方得到多少分的有效性的度量。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P038", "quote": "是无效性的度量。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P040", "quote": "N = 爱者的付出P*爱者的有效性系数E", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P041", "quote": "E永远低于1，U永远大于0。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P047", "quote": "这就是隐藏在亲密关系中的撒旦，逻辑的魔鬼。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P048", "quote": "爱是一项从账面上看必然亏损的生意。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P050", "quote": "无效性低于0的，只可能是全知全能、自有永有、无欲无求的上帝。", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P054", "quote": "自然之中设计了奖励爱人者的内在逻辑。", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P056", "quote": "再衣食无忧，心伤是无价的。", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P060", "quote": "人生是一种以必然损失的一切换取可能幸存的一切的游戏。", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P061", "quote": "因为你那101分本来就是要消失的。", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P063", "quote": "这就是爱之所以永不亏损的真正逻辑。", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P065", "quote": "你怎么会惩罚、追讨、报复？", "relation": "supports"},
    {"key": "E33", "paragraph_id": "P068", "quote": "就是对将来关系因为种种自己不能控制的意外", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P070", "quote": "所以我不要“爱”了，因为我没手指了。", "relation": "supports"},
    {"key": "E35", "paragraph_id": "P072", "quote": "那101不是对方欠下了，而是自己花掉了。", "relation": "supports"},
    {"key": "E36", "paragraph_id": "P073", "quote": "总之是我自己的责任——不是对方无义。", "relation": "supports"},
    {"key": "E37", "paragraph_id": "P074", "quote": "只可能有感谢的理由。", "relation": "supports"},
    {"key": "E38", "paragraph_id": "P075", "quote": "这样的人，在这个世界上每一个都是珍宝。", "relation": "supports"},
    {"key": "E39", "paragraph_id": "P078", "quote": "分开，是因为更爱。", "relation": "supports"},
    {"key": "E40", "paragraph_id": "P080", "quote": "就是所谓的“人品”的本质", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["亲密关系", "情感伦理", "人生哲学"],
   "issue_candidates": ["分手与人品", "爱与贪的区分", "爱的能力与成本", "关系终结时的追索与报复", "不安全感"],
   "text_function_candidates": ["答疑", "论说", "训诫", "格言式总结"],
   "object_candidates": ["提问者（知乎问题）", "父母", "上帝", "奴隶与奴隶主（比喻）"],
   "working_keywords": ["爱", "贪", "爱的能力", "被爱的能力", "有效性系数E", "无效性U", "净所得N", "无间地狱", "人品", "放长线钓大鱼", "不安全感"]
  },
  "notes": "无图片节点（not_applicable），正文非空，status=read。问答体：Q001“分手后真的能看出一个人的人品吗？”属提问者，作者未复述提问者立场，只在 P080 给出自己的判定。全篇为第二人称训诫式论说，P040 的自设公式与 P038“自身的自身的”重复字均按原文保留。P006 为作者代拟的双方口吻，按 quoted_or_cited / unknown 记录。P076-P078 为分行短句段（lexical 仍为 paragraph）。"
 },
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', default=None, help='输出 JSONL 路径（默认 out/<batch>.out.jsonl）')
    args = ap.parse_args()
    rows = load_batch_rows(BATCH)
    records = []
    for row in rows:
        art = row['article']
        uid = UID_BY_ID[art['id']]
        if uid not in ANALYSIS:
            raise SystemExit('ANALYSIS 缺少 %s (%s)' % (uid, art.get('title')))
        p = ANALYSIS[uid]
        records.append(build_record(
            row, row['batch_id'], row['corpus_sha256'],
            p['analysis'], p['provisional_tags'], STARTED, COMPLETED,
            status=p.get('status', 'read'),
            full_text_checked=p.get('full_text_checked', True),
            image_checked=p.get('image_checked', False),
            notes=p.get('notes', '')))
    out = args.out or os.path.join(_HERE, '..', 'out', BATCH + '.out.jsonl')
    write_jsonl(out, records)
    print('ok %s -> %s (%d records)' % (BATCH, out, len(records)))


if __name__ == '__main__':
    main()
