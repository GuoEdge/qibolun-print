# -*- coding: utf-8 -*-
"""批次 r001-b0053 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0053.sessions.py            # 写 out/r001-b0053.out.jsonl
  python3 records/r001-b0053.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0053"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0053.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "a464d0ff": {
  "analysis": {
   "question_context": "提问者问“中国现在有哪些做得不好的地方？”（提问字段属提问者，非作者主张）。作者以“宏观组织的有效性掩盖的微观组织的无效性”作答，并从国家竞争层面推进到个人伦理框架缺失与意识形态共存问题；文末标“（未完待续）”，本篇属未完结的系列文章。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004", "P005", "P006", "P007", "P008", "P009", "P010"], "summary": "宏观层面：国企舰队、党政一体体制、教育体系与舆论场域带来看似无双的整体竞争力；多数他国是刺激驱动而非战略驱动，其“战略”沦为笑谈；决策质量的关键在认错改错的速度，西方高质量决策源于学术遗产这一存量优势；中国或从更低政策起点出发，但差距不致命。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P011", "P012", "P013", "P014", "P015", "P016", "P017", "P018", "P019", "P020", "P021"], "summary": "微观层面：宏观有效性被微观低效拖后腿；朋友、师生、亲子、同事、上下级、恋人关系失灵，人与不同时间、处境、身份的自己亦不和；缺乏可参考的个人伦理框架。作者称此为中国现在最大的问题，乃至世界目前最大的问题。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P022", "P023"], "summary": "转折：问题本身的要害不在问题，而在“应循何种框架去解决”这一问题本身存在巨大的思想混乱。", "role": "transition"},
    {"unit_id": "U004", "paragraph_refs": ["P024", "P025", "P026", "P027", "P028", "P029", "P030", "P031"], "summary": "障碍分析：普遍接受的“朴素自由主义”（作者称实为虚无主义）预设；把“被影响即被奴役”写入思维底层；被说服即触发红色警报，造成心智上的孤立无援。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P033", "P034", "P035", "P036", "P037", "P038", "P039", "P040", "P041"], "summary": "自问自答：作者声明写作目的不是让人哀叹世风、鄙夷知识分子或归咎体制国情，而是让人意识到这是要害问题，且任何问题都是自己的问题。", "role": "conclusion"},
    {"unit_id": "U006", "paragraph_refs": ["P042", "P043", "P044", "P045", "P046", "P047"], "summary": "责任归属：作者认为微观失灵中国家与知识分子责任小甚至可忽略，困境主要源于个人对自己的不负责任（送饭人迟到与饿肚子的类比）。", "role": "claim"},
    {"unit_id": "U007", "paragraph_refs": ["P048", "P049", "P050", "P051", "P052", "P053", "P054", "P055", "P056", "P057"], "summary": "引述式论断与反驳：“那些只是你的借口”被作者称为“天下的”判断；世界只关心你是否解决了问题；失恋、绝交、丢工作时的求助与“慢慢就好了”“时间会治愈一切”只是重新计时。", "role": "rebuttal"},
    {"unit_id": "U008", "paragraph_refs": ["P058", "P059", "P060", "P061", "P062", "P063"], "summary": "行动建议：想通自己的伦理观是头号问题；人是社会关系的总和，伦理先于“生产力”；作者把困境归为近百年来民族成员自己对伦理的不努力，并呼吁下更大功夫。", "role": "action_advice"},
    {"unit_id": "U009", "paragraph_refs": ["P064", "P065"], "summary": "提出首要关键：这个时代对人的伦理提出了新要求（准确说是以空前严苛性强调的老要求）——共融。", "role": "definition"},
    {"unit_id": "U010", "paragraph_refs": ["P066", "P067", "P068", "P069", "P070", "P071", "P072", "P073", "P074", "P075", "P076", "P077", "P078", "P079", "P080", "P081", "P082", "P083"], "summary": "历史与心理机制：帝国辉煌诱导出“意识形态应定于一尊”的集体潜意识；基于信仰的意识形态互为掘墓人、以真理为名行征服与唯一化；古典伦理缺少与异己共存的诚意，导致个人层面的自我敌对。", "role": "reason"},
    {"unit_id": "U011", "paragraph_refs": ["P084", "P085", "P086", "P087", "P088", "P089", "P090", "P091", "P092", "P093"], "summary": "当代条件：全球化与信息化使意识形态直接交叠，核武器与世贸组织使“慑服一切、唯我独尊”不现实；历史宣布“独尊真理”在实践层面已不再可能，“与敌人们共存”成为一票否决式的必修课。", "role": "claim"},
    {"unit_id": "U012", "paragraph_refs": ["P094", "P095", "P096", "P097", "P098", "P099", "P100"], "summary": "结论与要求：共存不止于忍受、虚与委蛇与避免激化矛盾，须修到“建设性关系”与“和谐共处”，并落到个人友谊、生意伙伴、伴侣以及不同时段的自己；文末“（未完待续）”。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "中国现在最大的问题，是被宏观组织的有效性掩盖的微观组织的无效性；作者进一步称这甚至是世界目前最大的问题。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "央企领航的国企舰队、党政一体的政府体制、一体化教育体系与有效管制的舆论场域，给了中国举世无双的整体竞争力。", "evidence": ["E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "世界上绝大多数国家在国家意志与总体行动力方面落后，其整体动作更多是刺激驱动而非理想、战略驱动，其所谓“战略”已渐渐沦为笑谈。", "evidence": ["E4", "E5"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "幻想对手会下错赌注、认为程序正义的自然博弈更正确，是无根据的自欺欺人，是被集体意识焦虑催生的政治正确。", "evidence": ["E6", "E7"]},
    {"claim_id": "C005", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "重要的不是会不会犯错误，而是会不会承认错误、会不会改错、够不够快；主动决策无论来自少数精英决断还是复杂投票制度，并没有多少本质上的质量区别。", "evidence": ["E8", "E9", "E10"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "西方发达国家能作出相对高质量的决策，事实上与民主制度无关，更多基于传承不断、积累深厚的学术遗产。", "evidence": ["E11"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不同于制度上的优势，遗产造成的优势不是增量的优势，而是存量的优势。", "evidence": ["E12"]},
    {"claim_id": "C008", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "中国也许并不能作出质量更好的决策，甚至因学术积累不足几乎总是从更低的政策起点出发；但差距不致命（兔子需比乌龟多跑十米的类比）。", "evidence": ["E13", "E14"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "中国宏观层面的高度有效性被微观层面的低效严重拖了后腿：朋友、师生、亲子、同事、上下级、恋人关系严重失灵。", "evidence": ["E15", "E16"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人们不知道应如何作为朋友、下属、上司、学生、老师、同事、恋人、男人、女人、父母、子女、成人、孩子生存；失和不只发生在人与人之间，也发生在不同时间、处境与身份的自己之间。", "evidence": ["E17", "E18"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "眼下中国没有显著可见的、足够扎实自洽、可广延、可规模化而自持、同时又与顶层设计兼容的个人伦理框架。", "evidence": ["E19"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "真正的要害是“这个问题应该循着何种框架去解决”这一问题本身存在巨大的思想混乱。", "evidence": ["E20"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "首要障碍是人们普遍接受了一种未经审视的、名为“自由主义”实为虚无主义的思想预设，并下意识认为排除一切影响个人价值观的可能才是获得与保证个人自由的必由之路。", "evidence": ["E21", "E22"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“认同、追随、服务、甚至学习都是被奴役”已被时代写入思维底层的心理本能；仅仅被说服或被觉察到的影响，对绝大多数现代人已是值得动员反抗的红色警报，而这是现代性的核心要素之一。", "evidence": ["E23", "E24", "E25"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "这造成心智上的天然困境：如果你在心理上对被说服都感到厌恶，就必然在心智上处在孤立无援的境地。", "evidence": ["E26"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者声明写这些不是要读者哀叹世风日下、鄙夷知识分子或把责任怪在体制国情上，而是希望读者意识到这是要害问题，并且任何问题都是自己的问题。", "evidence": ["E27", "E28"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "中国社会微观层面的失灵，国家与知识分子承担的责任是小的、甚至可忽略；更多是个人对自己的不负责任造成了自己的困境。", "evidence": ["E29", "E30"]},
    {"claim_id": "C018", "claim_type": "author_reported", "attribution": "author", "modality": "asserted", "statement": "作者称“那些只是你的借口”这一判断不是他下的而是“天下的”，因为世界不关心你没解决的原因，只关心你没有解决好这些问题。", "evidence": ["E31", "E32", "E33"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "“慢慢就好了”“时间会治愈一切”并不成立——只是又开始重新计时了。", "evidence": ["E34", "E35"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "想通自己的伦理观是头号问题，比考好大学、进好公司、结婚、赚大钱、住大房子更重要，而且是一个不容绕过的问题。", "evidence": ["E36", "E37"]},
    {"claim_id": "C021", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人是社会关系的总和；对个人而言总是先有伦理的蛋、再有“生产力”的鸡，且生产力无论多惊人也买不了社会关系。", "evidence": ["E38", "E39"]},
    {"claim_id": "C022", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "目前这个困境是近百年来中华民族的每一个成员自己对伦理的不努力的结果。", "evidence": ["E40"]},
    {"claim_id": "C023", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这个时代对人的伦理提出了一个新要求（准确说，是以前所未有的严苛性强调出了一个老要求）——共融。", "evidence": ["E41"]},
    {"claim_id": "C024", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "二战前各文化圈的帝国辉煌诱导出“意识形态应有至尊、理应最终定于一尊”的集体潜意识，使基于信仰的意识形态对异己抱持“我是你们全体的掘墓人”的心态。", "evidence": ["E42", "E43"]},
    {"claim_id": "C025", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "几乎所有古典主义的价值观、伦理观，都缺少真实地和异己真正和解、真正共存的诚意。", "evidence": ["E44"]},
    {"claim_id": "C026", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "核武器与世界贸易组织的存在使“以绝对正确的理念慑服一切意识形态、达成唯我独尊”越来越不现实乃至不健康；历史已宣布“独尊真理”起码在这个时代、在实践层面上不再可能。", "evidence": ["E45", "E46"]},
    {"claim_id": "C027", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对每一种意识形态而言，“与敌人们共存”已不再是选修课，而是必修课，且是一票否决式的绝对必修课。", "evidence": ["E47"]},
    {"claim_id": "C028", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "共存不止于暂时忍受、虚与委蛇与避免激化矛盾（那只是学前班预科），必须修到“如何与对方建立建设性关系”与“和谐共处”；这同样适用于朋友、生意伙伴、伴侣，本质上也是今天与明天、此处与彼处的自己之间的关系。", "evidence": ["E48", "E49", "E50"]}
   ],
   "argument_steps": [
    "提问（Q001，提问者）：中国现在有哪些做得不好的地方？",
    "定义/前提（P001）：把“最大的问题”限定为宏观组织有效性与微观组织无效性的落差。",
    "理由（P002–P004）：以国企舰队、党政一体、教育体系、舆论场域论证宏观有效性；以水母、海星类比他国的刺激驱动型行动力。",
    "反驳（P005–P006）：把“等对手下错赌注”判为自欺欺人与政治正确。",
    "让步与限定（P007–P010）：承认中国政策起点可能更低，但以存量/增量优势之别与兔子乌龟类比说明不致命。",
    "转折（P011–P021）：由宏观转向微观失灵，并提出缺乏个人伦理框架这一“最大的问题”。",
    "递进（P022–P023）：指出要害是解决问题的框架本身存在思想混乱。",
    "障碍分析（P024–P031）：朴素自由主义、被影响即被奴役的心理本能、心智孤立无援。",
    "自问自答与转折（P033–P041）：声明写作意图，并把问题收归个人。",
    "归责与反驳（P042–P057）：以送饭人比喻归责个人；引“天下的”判断；反驳“时间会治愈一切”。",
    "行动要求（P058–P063）：想通伦理观是头号问题，伦理先于生产力。",
    "提出概念（P064–P065）：时代对伦理的新要求是“共融”。",
    "历史与心理机制（P066–P083）：帝国辉煌→定于一尊的潜意识→互为掘墓人→自我敌对。",
    "条件论证（P084–P093）：全球化交叠与核武器、WTO 使独尊真理不再可能，共存成为必修课。",
    "结论（P094–P100）：共存须修到建设性关系与和谐共处，并要求落到个人关系与不同时段的自己；标明未完待续。"
   ],
   "concept_usage": [
    {"term": "宏观组织的有效性／微观组织的无效性", "meaning": "作者用以概括中国问题的核心张力：国家层面组织动员有效，个人伦理与人际关系层面失效。", "evidence": "P001", "ambiguity": "两个“有效性”均未给出衡量标准或经验数据。"},
    {"term": "存量优势／增量优势", "meaning": "作者把学术遗产造成的优势称为存量优势，区别于制度带来的增量优势（P008）。", "evidence": "P008", "ambiguity": "未说明存量优势能否转化为增量。"},
    {"term": "朴素自由主义", "meaning": "作者称之为“未经审视的、名为自由主义、实为虚无主义的思想预设”。", "evidence": "P024", "ambiguity": "术语为作者自造，未给出与通常自由主义的界定关系。"},
    {"term": "共融", "meaning": "作者称这是时代对人的伦理提出的新要求（实为以前所未有的严苛性强调的老要求）。", "evidence": "P065", "ambiguity": "全文未给出“共融”的操作性定义。"},
    {"term": "独尊真理", "meaning": "作者用指“唯我独尊的永远正确”式意识形态立场，并称其在实践层面已不再可能。", "evidence": "P092", "ambiguity": "属作者概括语，未指明持此立场的具体主体。"},
    {"term": "与敌人们共存", "meaning": "作者称之为一票否决式的绝对必修课，须修到建设性关系与和谐共处。", "evidence": "P093", "ambiguity": "“敌人”的判定标准未说明。"},
    {"term": "天下的", "meaning": "作者借以指称并非由个人作出、而是客观处境给出的裁决。", "evidence": "P049", "ambiguity": "该主体的具体所指未说明。"},
    {"term": "哀鸿遍野", "meaning": "作者在两处（P013、P032）重复使用的叠句，用以形容微观关系失灵与心智孤立的状态。", "evidence": "P013", "ambiguity": "修辞性表达，非可核验描述。"},
    {"term": "摸着石头过长江", "meaning": "作者把“摸着石头过河”改写后用以指缺乏总体方案、只能各自摸索的处境。", "evidence": "P019", "ambiguity": "与官方用语“摸着石头过河”的关系未说明。"}
   ],
   "examples_and_targets": [
    "类比（作者）：中国如睁眼竖耳、四肢健全的脊椎动物；他国如海星，落后者为水母（P003、P004）。",
    "类比（作者）：兔子需比乌龟多跑十米（P010）。",
    "历史例举（作者修辞/证据）：埃及、巴比伦、波斯、希腊马其顿、罗马、阿拉伯、秦汉隋唐元明清、大不列颠、苏联、美帝国（P066、P070）。",
    "例举（作者）：儒容不得释与道、新教容不得旧教、西方容不得东方、蓝容不得红（P074）。",
    "例举（作者）：核武器、世界贸易组织（P085、P087）。",
    "例证（作者）：失恋、绝交、丢工作时问朋友、父母、知乎、心理医生而答案都不满意（P052、P053）。",
    "被反驳的说法（非作者）：流行语“慢慢就好了”“时间会治愈一切”（P056、P057）；“等对手下错赌注”的期待（P005）。",
    "例证（作者）：考好大学、进好公司、结婚、赚大钱、住大房子作为对照项（P059）。",
    "引语（说话者为作者，以引号标出）：作者自引“认同、追随、服务、甚至学习，都是某种意义上的‘被奴役’”（P026）与“我是你们全体的掘墓人”（P068），均被作者当作时代心态的描述而非他人学说。"
   ],
   "conditions": [
    "限定词“也许”“甚至”：中国也许不能作出质量更好的决策，甚至几乎总是从更低的政策起点出发（P009）。",
    "条件：如果在心理上对被说服都感到厌恶，则必然心智孤立无援（P030）。",
    "条件：如果你发生意识形态立场上的犹豫和憧憬，就会因缺少“和解的遗产”而陷入自我敌对；倒向一边就自动继承对其他同类的根本排斥（P079、P080）。",
    "时间范围限定：“起码在这个时代、在实践层面上”独尊真理不再可能（P092）。",
    "历史分期：二战前（P066）与现代化、信息化、全球化之后的当下（P084）。",
    "让步条件：“即使有耳聪目明的精英”，他国也无法凝聚共识与动员资源（P004）。",
    "对象范围：作者以“中华民族的每一个成员”为归责对象（P062），同时把问题扩展为“这个世界目前最大的问题”（P021）。",
    "未设条件处：作者未说明学术遗产如何度量，也未说明“近百年”起止。"
   ],
   "rhetoric_and_tone": "训诫与布道式语气，通篇以第二人称“你”直呼读者；反复使用“哀鸿遍野”作叠句（P013、P032）；密集反问（“与己不和，何处可逃？”“谁能消灭谁？”“谁比谁真的永远优越？”“难道他一天不来，你就一天不吃吗？”）；自问自答的段落（P033–P037 连问后以“并不是”收束）；用动物类比（水母、海星、脊椎动物、兔子与乌龟）与重词（掘墓人、处决、你死我活）加强力度；引号内嵌套引号（P026）；文末以“（未完待续）”表明结构上未完成。",
   "unresolved_questions": [
    "文末标“（未完待续）”，本篇非完整论述，后续篇内容本文未说明。",
    "“朴素自由主义”“共融”等术语本文只以例举与对比说明，未给出系统定义或判定标准。",
    "P007 出现“认得够不够快”，与同句“会不会承认错误、会不会改错”并列，疑为原文笔误或特殊用法；未作改动，需与原件核对。",
    "作者断言西方发达国家高质量决策“事实上与民主制度无关”，属需外部核查的事实性断言。",
    "“近百年来中华民族的每一个成员自己对伦理的不努力”这一归责缺乏经验依据说明。",
    "“天下的”这一裁决主体的具体所指未说明。",
    "P004 提及“四年或者八年一反复”，未点名具体国家或制度。",
    "提问字段属提问者立场（问“有哪些做得不好的地方”），正文未复述该问题，二者关系需研究者复核。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "中国现在最大的问题，是被宏观组织的有效性掩盖的微观组织的无效性。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P021", "quote": "甚至，是这个世界目前最大的问题。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P002", "quote": "给了中国举世无双的整体竞争力", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "他们的整体动作更多的是刺激驱动的，而非理想、战略驱动", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P004", "quote": "已经渐渐沦为笑谈了", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P005", "quote": "他们总是在幻想那些大胆行动的对手一定会下错赌注", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P006", "quote": "这其实是一种无根据的自欺欺人", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P007", "quote": "因为重要的并不是会不会犯错误，而是会不会承认错误、会不会改错", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P007", "quote": "并没有多少本质上的、质量上的客观区别", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P007", "quote": "主动的决策——无论是来自少数精英的决断、还是来自复杂的投票制度", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P007", "quote": "事实上与民主制度无关，而更多的是基于传承不断、积累深厚的学术遗产", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P008", "quote": "遗产造成的优势不是增量的优势，而是存量的优势", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P009", "quote": "中国几乎总是从更低的政策起点出发", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P010", "quote": "兔子需要比乌龟多跑十米，对兔子并不是致命的问题", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P011", "quote": "中国宏观层面的高度有效性，被微观层面的低效性严重的拖了后腿", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P012", "quote": "我们的朋友、师生、亲子、同事、上下级、恋人关系，严重的失灵", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P015", "quote": "人们不知道应该怎么作为一个朋友、一个下属、一个上司", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P016", "quote": "还是今天的自己与昨天的自己不和、明天的自己与今天的自己不和", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P018", "quote": "没有显著可见的足够扎实的、自洽的、可广延的、可以规模化而自持的", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P023", "quote": "真正要害的地方是“这个问题应该循着何种框架去解决”这个问题本身存在着巨大的思想混乱", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P024", "quote": "人们普遍的接受了一种未经审视的、名为“自由主义”，实为虚无主义的思想预设", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P025", "quote": "排除一切关于个人价值观的受影响的可能，是获得和保证个人自由的必由之路", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P026", "quote": "这是已经被这个时代写入了人的思维底层的心理本能", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P027", "quote": "对于绝大多数现代人就已经是足以引起警惕、值得动员反抗的红色警报了", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P028", "quote": "实际上，这就是现代性的核心要素之一。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P030", "quote": "那么你就必然在心智上处在孤立无援的境地", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P038", "quote": "我只是希望你们意识到这是一个要害的问题", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P039", "quote": "而任何问题，都是你的问题", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P047", "quote": "国家、知识分子承担的责任是小的，甚至是可以忽略的", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P043", "quote": "不如说是你个人对自己的不负责任，造成了你自己个人的困境", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P048", "quote": "那些只是你的借口。", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P049", "quote": "这判断其实不是我下的，而是天下的。", "relation": "supports"},
    {"key": "E33", "paragraph_id": "P050", "quote": "它只关心你没有解决好这些问题。", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P057", "quote": "好什么啊……只是又开始重新计时了。", "relation": "contradicts"},
    {"key": "E35", "paragraph_id": "P056", "quote": "“慢慢就好了”，“时间会治愈一切”", "relation": "context"},
    {"key": "E36", "paragraph_id": "P059", "quote": "想通你自己的伦理观，这是你的头号问题", "relation": "supports"},
    {"key": "E37", "paragraph_id": "P059", "quote": "比考好大学、进好公司、结婚、赚大钱、住大房子更重要的问题", "relation": "supports"},
    {"key": "E38", "paragraph_id": "P060", "quote": "人是社会关系的总和。", "relation": "supports"},
    {"key": "E39", "paragraph_id": "P061", "quote": "总是先有伦理的蛋，再有“生产力”的鸡", "relation": "supports"},
    {"key": "E40", "paragraph_id": "P062", "quote": "是近百年来中华民族的每一个成员自己对伦理的不努力的结果", "relation": "supports"},
    {"key": "E41", "paragraph_id": "P065", "quote": "是以前所未有的严苛性强调出了一个老要求", "relation": "supports"},
    {"key": "E42", "paragraph_id": "P066", "quote": "意识形态应该是有至尊的，理应最终要定于一尊的", "relation": "supports"},
    {"key": "E43", "paragraph_id": "P068", "quote": "我是你们全体的掘墓人", "relation": "supports"},
    {"key": "E44", "paragraph_id": "P078", "quote": "都缺少真实的和异己真正和解、真正共存的诚意", "relation": "supports"},
    {"key": "E45", "paragraph_id": "P085", "quote": "已经越来越不现实，乃至于不健康了", "relation": "supports"},
    {"key": "E46", "paragraph_id": "P092", "quote": "“独尊真理”起码在这个时代、在实践层面上已经不再可能了", "relation": "supports"},
    {"key": "E47", "paragraph_id": "P093", "quote": "都已经不再是选修课，而已经成了必修课", "relation": "supports"},
    {"key": "E48", "paragraph_id": "P094", "quote": "这只是学前班预科", "relation": "supports"},
    {"key": "E49", "paragraph_id": "P095", "quote": "你必须要修到“如何与对方建立建设性关系”，修到“和谐共处”", "relation": "supports"},
    {"key": "E50", "paragraph_id": "P098", "quote": "这也是今天的你与明天的你、此处的你与彼处的你自己的建设性关系和和谐共处的问题", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["政治哲学", "社会伦理", "国际政治", "文化批评", "中国社会问题"],
   "issue_candidates": ["宏观组织有效性与微观组织无效性的落差", "个人伦理框架缺失", "朴素自由主义与虚无主义", "意识形态共存与独尊真理", "现代性中的被说服恐惧", "人与自我的不和"],
   "text_function_candidates": ["答疑（回应知乎提问）", "论辩", "批评", "训诫", "系列长文（未完待续）"],
   "object_candidates": ["中国", "西方发达国家", "中华民族", "知识分子", "埃及/巴比伦/波斯/罗马/大不列颠/苏联/美国等帝国", "核武器", "世界贸易组织"],
   "working_keywords": ["宏观组织的有效性", "微观组织的无效性", "朴素自由主义", "共融", "独尊真理", "与敌人们共存", "存量优势", "增量优势", "定于一尊", "摸着石头过长江", "哀鸿遍野"]
  },
  "notes": "无图片节点（骨架 images 为空）。正文 P001–P100 已完整读取；text 与 lexical 无 divergence。文末“（未完待续）”提示系列未完，本篇非完结篇。提问字段 Q001 属提问者，其立场未计入作者主张；正文未复述提问。P007“认得够不够快”疑为原文笔误，保留原样。"
 },
 "12e4a0af": {
  "analysis": {
   "question_context": "提问者问“如何评价‘吃饭时筷子插在饭上不吉’这种封建迷信思想？”（提问字段属提问者）。作者未直接评价该民俗本身，而是设定一个假设情境：若你在饭桌上以“封建迷信思想”斥责提醒你的人，会依次触发甲、乙、丙、丁四类反应，并据此说明移风易俗的条件与代价。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "假设情境的设定：你把筷子插在饭上，某甲介意并提醒，你以“封建迷信思想”斥责对方。", "role": "context"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P003", "P004"], "summary": "三类负面后果：甲视你为不可交往并撤回合作；同样持该忌讳的乙把你列入黑名单；不持该忌讳的丙也因你不懂隐忍处理习惯差异、把小问题弄成丢掉两个社会关系而将你拉黑。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P005", "P006"], "summary": "第四类反应：丁不持该忌讳且觉得痛快，认为断掉这类合作关系是消除隐患；随后丁也会因你的白左/粉红/女权/动保/精日/哈韩等标签同样对待你。", "role": "example"},
    {"unit_id": "U004", "paragraph_refs": ["P007"], "summary": "以麻将术语作结：甲乙丙丁合起来是“推倒胡、放炮大四喜、八十八番、双倍役满”。", "role": "conclusion"},
    {"unit_id": "U005", "paragraph_refs": ["P008"], "summary": "推广判断：受这种效应保护的不是某一种传统，而是所有信仰、风俗、传统。", "role": "claim"},
    {"unit_id": "U006", "paragraph_refs": ["P009", "P010"], "summary": "反驳与预测：移风易俗不能靠毫无德行积累的小孩子“嗤之以鼻”，那是以卵击石；这些吃亏的小孩长大后往往从丁变成丙，也会拉黑新的挑战者。", "role": "rebuttal"},
    {"unit_id": "U007", "paragraph_refs": ["P011", "P012", "P013", "P014", "P015"], "summary": "资格条件：移风易俗是有功于天下苍生的圣贤才有资格做的事；真想移谁的俗，必须先救这人的命，让对方有“命都是你救的”念头；因为移风易俗就是在改人的命。", "role": "qualification"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "在作者设定的假设情境中，以“封建迷信思想”斥责提醒者，会使甲撤回合作、乙把你列入黑名单、丙因你不懂处理习惯差异而把你拉黑。", "evidence": ["E1", "E2", "E3"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "在假设情境中，丁不但不介意，还会认为断掉这类合作关系是消除隐患，并会因你的白左/粉红/女权/动保/精日/哈韩等标签以同样方式对待你。", "evidence": ["E4", "E5"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "受这种效应保护的不是这一种传统，而是所有的信仰、风俗、传统。", "evidence": ["E6"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "移风易俗不是靠毫无德行积累的小孩子“嗤之以鼻”去完成的，这纯属以卵击石、毫无意义的自我葬送。", "evidence": ["E7"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "因这种心态吃了大亏的小孩子长大后，往往会从某丁变成某丙，自己也会成为拉黑新的幼年挑战者的一员。", "evidence": ["E8"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "移风易俗是有功于天下苍生的圣贤才有资格干的事。", "evidence": ["E9"]},
    {"claim_id": "C007", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "真想移谁的风、易谁的俗，必须先救这人的命，让对方有“命都是你救的”的念头，才有资格说这话。", "evidence": ["E10"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "因为移风易俗就是在改人的命。", "evidence": ["E11"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以“你遇到别人来移你的风、易你的俗试试看，你瞬间就明白”点出此事的真正重量。", "evidence": ["E12", "E13"]}
   ],
   "argument_steps": [
    "设定假设前提（P001）：饭桌插筷、被提醒、以“封建迷信思想”斥责。",
    "分情形推演后果（P002–P005）：甲撤回合作、乙拉黑、丙因处事方式拉黑、丁视为消除隐患。",
    "延伸（P006）：同一逻辑可用于你的其他身份标签，故无人安全。",
    "结论式收束（P007）：以麻将“推倒胡、放炮大四喜、八十八番、双倍役满”比喻全输。",
    "由个例推广（P008）：受保护的是所有信仰、风俗、传统。",
    "反驳（P009）：否定“嗤之以鼻”式移风易俗，判为以卵击石。",
    "预测（P010）：吃亏者长大后变成丙，复制同一机制。",
    "提出资格条件（P011–P013）：圣贤才有资格，且须先救命；理由是移风易俗即改命。",
    "以读者处境作验证（P014）：换位体验即可明白。",
    "收束（P015）：这才是这事真正的重量。"
   ],
   "concept_usage": [
    {"term": "封建迷信思想", "meaning": "作者在假设情境中让“你”用来斥责对方的标签；作者未评价该民俗本身，只推演使用该标签的代价。", "evidence": "P001", "ambiguity": "该词出自提问者对民俗的评价语境，作者以引号使用，未表示认同。"},
    {"term": "移风易俗", "meaning": "改变他人的风俗传统；作者称其为“改人的命”，须先救人性命才有资格。", "evidence": "P012", "ambiguity": "未区分移风易俗的公权力行为与私人劝说。"},
    {"term": "德行积累", "meaning": "作者认为小孩子“毫无德行积累”，故无移风易俗的资格。", "evidence": "P009", "ambiguity": "“德行积累”的衡量方式未说明。"},
    {"term": "双倍役满", "meaning": "麻将术语，作者用以比喻上述四类反应叠加导致的彻底失败。", "evidence": "P007", "ambiguity": "比喻的具体番数对应关系非论证内容。"},
    {"term": "社会关系／合作关系", "meaning": "作者把饭桌冲突的后果落到可撤回的合作关系与黑名单上。", "evidence": "P002", "ambiguity": "未给出“社会关系损失”的量化标准。"}
   ],
   "examples_and_targets": [
    "假设人物（作者设定）：某甲（介意并被斥责者）、某乙（同样持忌讳者）、某丙（不持忌讳但重视处事方式者）、某丁（不持忌讳且视断交为消除隐患者）（P002–P005）。",
    "被反驳对象（作者）：以“封建迷信思想”斥责提醒者的“小孩子们”及其“嗤之以鼻”式的移风易俗方式（P001、P009）。",
    "类比/修辞材料（作者）：麻将术语“推倒胡，放炮大四喜，八十八番，双倍役满”（P007）。",
    "标签例举（作者列举的社会身份标签）：白左、粉红、女权、动保、精日、哈韩（P006）。",
    "提问者说法（非作者）：筷子插在饭上不吉属“封建迷信思想”（Q001 属提问者，正文未复述）。"
   ],
   "conditions": [
    "全篇以假设语气展开（P001“你吃饭时把筷子插在饭上……斥责之”），后果均为情境推演而非对具体事件的记述。",
    "条件：乙之所以拉黑你，前提是“如果这人也有‘封建迷信思想’”（P003）。",
    "条件：丙的反应取决于“这人没有‘封建迷信思想’，但这人发现你居然意识不到这样做的现实代价”（P004）。",
    "条件：丁的反应取决于“这人不但没有‘封建迷信思想’，而且深深的觉得这样做真痛快”（P005）。",
    "资格条件：须“先救这人的命，让这人有‘命都是你救的’的念头”才有资格说移风易俗的话（P012）。",
    "程度限定：“有一句‘抱歉’可以解决的问题弄到丢掉两个社会关系”（P004）。",
    "对象范围：作者把结论推广到“所有的信仰、风俗、传统”（P008）。"
   ],
   "rhetoric_and_tone": "冷峻的推演语气，采用编号清单（1）2）3）4））式的分情形枚举；以第二人称“你”把读者放入情境；结尾用麻将番数作戏谑式收束（“恭喜，推倒胡，放炮大四喜，八十八番，双倍役满，赶紧给钱”）；对“小孩子们”使用带贬抑色彩但非辱骂的称呼；P006 末句“因为这就是ta的处世之道，不是吗？”为反问；ta 用作不分性别的第三人称写法。",
   "unresolved_questions": [
    "作者未直接回答提问者对“筷子插在饭上不吉”这一民俗本身的评价请求，只讨论使用“封建迷信思想”这一标签的代价。",
    "甲乙丙丁均为假设人物，非现实事件或可核查案例。",
    "“移风易俗就是在改人的命”属比喻性断言，作者未给出论证或经验依据。",
    "作者把“白左/粉红/女权/动保/精日/哈韩”等标签并置，未说明其相互关系与判定标准。",
    "提问字段属提问者立场，正文未复述该问题。",
    "P010 原文作“成为因此而讲新的幼年挑战者拉黑的一员”，“讲”疑为“将”之笔误；保留原文未改，证据 E8 按原文逐字引用。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P002", "quote": "某甲显然会视你为不可交往的对象，撤回一切与你合作的企图。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P003", "quote": "你也要上这人的黑名单", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "这人也要把你拉进黑名单", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P005", "quote": "甚至认为断掉这类有封建迷信思想 / 过度敏感的合作关系还算是消除了隐患", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P006", "quote": "把你“三喜临门”了。因为这就是ta的处世之道", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P008", "quote": "而是所有的信仰、风俗、传统都受到这样的保护", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P009", "quote": "这纯属以卵击石，毫无意义的自我葬送", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P010", "quote": "往往会从某丁变成某丙，自己也会成为因此而讲新的幼年挑战者拉黑的一员", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P011", "quote": "移风易俗是有功于天下苍生的圣贤才有资格干的事。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P012", "quote": "必须先救这人的命，让这人有“命都是你救的”的念头，你才有资格说这话", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P013", "quote": "因为移风易俗就是在改人的命。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P014", "quote": "你遇到别人来移你的风、易你的俗试试看，你瞬间就明白。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P015", "quote": "这才是这事真正的重量。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P009", "quote": "移风易俗不是靠毫无德行积累的小孩子“嗤之以鼻”去完成的", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P007", "quote": "推倒胡，放炮大四喜，八十八番，双倍役满，赶紧给钱。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["社会交往伦理", "风俗与习俗", "冲突处理", "社会心理"],
   "issue_candidates": ["以“封建迷信”标签斥责他人的代价", "移风易俗的资格与条件", "习惯差异的处理方式", "社会关系的撤回与黑名单机制"],
   "text_function_candidates": ["答疑（回应知乎提问）", "假设情境推演", "论辩", "经验总结"],
   "object_candidates": ["某甲", "某乙", "某丙", "某丁", "“小孩子们”（泛指）"],
   "working_keywords": ["封建迷信思想", "移风易俗", "德行积累", "改人的命", "黑名单", "双倍役满", "社会关系"]
  },
  "notes": "无图片节点。正文 P001–P015 已完整读取（共 753 字），text 与 lexical 无 divergence。全篇为作者设定的假设情境推演，未指名现实人物或事件；P007 麻将术语与 P006 的身份标签为修辞材料。提问字段属提问者，其“封建迷信”评价未计入作者主张。"
 },
 "9c035109": {
  "analysis": {
   "question_context": "提问者问“为什么海外华人不团结？”（提问字段属提问者）。作者的回应是：这一提问预设了“华人本性不团结”，而在作者看来，与其说华人本性不团结，不如说在大部分国家华人是不能团结的；原因是华人的祖国太强大，团结组织无法绕过“忠诚证明”这一绝对要求。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "语境转述：一直有人呼吁海外华人团结、用投票权、成立组织、游说立法机构；在美国，年轻一代痛心华人不参政，动员时被族人的冷淡浇凉。作者评：这是他们太年轻了。", "role": "context"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005"], "summary": "核心判断：与其说华人本性不团结，不如说在大部分国家华人是不能团结的，因为华人的祖国太强大了。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007"], "summary": "理由一：具有鲜明种族身份的华人组织会触发“如何保证你不是你祖国的代理人”这一严重问题。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P008", "P009", "P010", "P011"], "summary": "分条件比较：祖国是小国或坚定盟友则无此问题；若祖国是足以争霸的大国且是敌国，则存在自证清白的绝对必要；生存空间由私人、私人企业的自由与投票所体现的个人意志限制，而非仅由成文法律保障。", "role": "qualification"},
    {"unit_id": "U005", "paragraph_refs": ["P012", "P013", "P014", "P015", "P016", "P017", "P018"], "summary": "悖论与逻辑链：真正有效的忠诚证明恰恰是自觉不团结；团结→需证明忠诚→唯一绝对有效的证明是“始终绝对服从安排”→该证明又以“绝对满意现有安排”为有效证明→故主张自身利益必然在绝对忠诚考核中失败。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P019", "P020", "P021"], "summary": "原罪与不可洗刷：华人背着“有一个强大而敌对的祖国”的原罪；任何不满都会被看作“民族苦肉计”；“团结起来”本身就是“叛意的证明”。", "role": "claim"},
    {"unit_id": "U007", "paragraph_refs": ["P022", "P023", "P024"], "summary": "后果与时限：出现能垒——团结反而使华人群体实际福利下降，越团结越恶化；这一情况在华裔人口比例足以影响政治版图之前会一直持续。", "role": "conclusion"},
    {"unit_id": "U008", "paragraph_refs": ["P025"], "summary": "反问式对照：作者以前苏联流亡遗民、俄罗斯移民为例，反问是否存在强大而团结的“美国俄罗斯裔协会”。", "role": "example"},
    {"unit_id": "U009", "paragraph_refs": ["P026", "P027", "P028", "P029"], "summary": "历史例证：吴三桂、耿仲明/耿精忠、尚可喜为清出生入死，武装与地盘足以割据东南西南，团结起来的下场被作者用作历史教训。", "role": "example"},
    {"unit_id": "U010", "paragraph_refs": ["P030"], "summary": "文化解释前提：东亚文明最大的文化优势是深刻理解群体动力学、能敏锐而毫无侥幸地“阅读空气”。", "role": "reason"},
    {"unit_id": "U011", "paragraph_refs": ["P031", "P032"], "summary": "两条路：要么通婚混血直到后裔不能自认华人，要么为保持文化身份以“不试图团结”为必须勇敢承受的代价；选后者恰恰是最华人的表现、对文化身份的最大忠诚。", "role": "claim"},
    {"unit_id": "U012", "paragraph_refs": ["P033", "P034", "P035"], "summary": "对呼声来源的判断与辩白：呼吁团结者多来自丧失充分华人身份认同的二代三代与深受西方文化浸染的新移民；作者不认为华人“懦弱无能”，因为他们更不肯选“团结起来但丢掉华人身份认同”。", "role": "rebuttal"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "与其说是华人本性不团结，不如说在大部分国家，华人是不能团结的。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "华人不能团结的原因，是华人的祖国太强大了。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "既然谈“华人团结”就意味着组织有鲜明的种族身份，就会触发“如何保证你不是你祖国的代理人”这一严重问题。", "evidence": ["E3", "E4"]},
    {"claim_id": "C004", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "若祖国是微不足道的小国或坚定盟友则没有问题；但若祖国是足以争霸的大国且是敌国，就存在自证清白的绝对必要。", "evidence": ["E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "生存空间不是由某部成文法律就能保障的；仅来自私人、私人企业的个人自由、经营自由与投票体现的个人意志，就足以有效限制生存空间。", "evidence": ["E6"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "真正有效的忠诚证明是一个悖论：恰恰是自觉的不团结起来。", "evidence": ["E7"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "逻辑链：团结即需证明忠诚；唯一绝对有效的忠诚证明是“始终绝对服从安排”；而这又以“绝对满意现有安排”为有效证明；故“团结起来主张自己的利益”必然在绝对忠诚的考核中失败。", "evidence": ["E8", "E9", "E10"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“团结起来”本身就是“叛意的证明”，任何其他证据都洗刷不了。", "evidence": ["E11"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "由此产生一个能垒：华人团结起来反而会导致华人群体实际福利下降，并且越团结越恶化。", "evidence": ["E12", "E13"]},
    {"claim_id": "C010", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "这一情况在华裔占到足够人口比例、足以影响政治版图之前，会一直持续。", "evidence": ["E14"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者以前苏联流亡遗民与俄罗斯移民反问：是否存在强大而团结的“美国俄罗斯裔协会”。", "evidence": ["E15"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "吴三桂、耿仲明/耿精忠、尚可喜为清出生入死、武装与地盘足以割据，仍以团结收场惨烈，此历史教训足以说明问题。", "evidence": ["E16", "E17", "E18"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "东亚文明最大的文化优势，是在深刻理解群体动力学上有能敏锐的、毫无侥幸的“阅读空气”的能力。", "evidence": ["E19"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "海外华人无论有意无意都意识到只有两条路：通婚混血直到后裔不能自认华人；或为保持文化身份，以“不试图团结”作为必须勇敢承受的代价。", "evidence": ["E20"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "选择后者恰恰是最华人的表现，是对自己文化身份的最大忠诚。", "evidence": ["E21"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“华人怎么不团结起来”的呼声，反而来自丧失充分华人身份认同的二代三代与不熟悉自身文化传统和历史记忆的新移民，是华人变得不是华人之后的结果。", "evidence": ["E22"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者不认为华人们“懦弱无能”、不勇于选择自己的命运；相反，他们多为保持文化身份而宁可选择代价沉重的“不团结起来”。", "evidence": ["E23"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "因为“团结起来，但丢掉华人身份认同”这个方案他们更不肯选，选也无用。", "evidence": ["E24"]}
   ],
   "argument_steps": [
    "转述语境（P001–P002）：长期以来呼吁海外华人团结参政的声音，以及年轻一代动员受挫的处境。",
    "作者评断（P003–P004）：这是他们太年轻了；不是本性不团结，而是不能团结。",
    "给出原因（P005）：华人的祖国太强大了。",
    "界定前提（P006）：“华人团结”意味着组织具有鲜明种族身份。",
    "提出问题（P007）：如何保证你不是你祖国的代理人。",
    "分条件讨论（P008–P009）：小国/盟友无此问题；争霸大国且为敌国则有自证清白的绝对必要，生存空间取决于证明程度。",
    "补充机制（P010–P011）：限制来自私人与私人企业的自由与投票，而非法律；组织无法绕过忠诚证明。",
    "悖论（P012–P013）：真正有效的忠诚证明是自觉不团结。",
    "逻辑链（P014–P018）：四步推出“主张自身利益必然在忠诚考核中失败”。",
    "加重（P019–P021）：原罪、苦肉计之嫌、“团结即叛意证明”。",
    "结论与时限（P022–P024）：团结反而降低福利且越团结越恶化，直至人口比例足以影响政治版图。",
    "对照例证（P025）：以俄罗斯裔是否存在同类协会反问。",
    "历史例证（P026–P029）：三藩为清效力与割据实力，团结的结局。",
    "文化前提（P030）：东亚文明“阅读空气”的能力。",
    "两条路与评价（P031–P032）：通婚混血，或承受不团结的代价；后者最为“华人”。",
    "反驳指责（P033–P035）：呼声来自身份认同已淡化者；华人非懦弱无能，只是更不肯丢掉身份认同。"
   ],
   "concept_usage": [
    {"term": "华人团结", "meaning": "作者界定为具有鲜明种族身份、以组织与游说争取本族利益的行为，而非加入泛化的少数族裔协会。", "evidence": "P006", "ambiguity": "作者未说明“团结”的组织形式与程度标准。"},
    {"term": "忠诚证明／自证清白", "meaning": "华人组织必须通过的绝对要求；作者称唯一绝对有效的形式是“始终绝对服从安排”。", "evidence": "P009", "ambiguity": "“安排”的发出者未具名。"},
    {"term": "原罪", "meaning": "作者用以指华人背负的“有一个强大而敌对的祖国”这一处境性负担。", "evidence": "P019", "ambiguity": "属修辞性用法，非神学或法律概念。"},
    {"term": "能垒", "meaning": "作者借用（类物理）术语，指团结行为反而压低群体福利的机制。", "evidence": "P022", "ambiguity": "未给出可测量的势垒或实证数据。"},
    {"term": "阅读空气", "meaning": "作者称这是东亚文明在理解群体动力学上的文化优势，指敏锐而无侥幸地把握群体氛围。", "evidence": "P030", "ambiguity": "未说明该能力的界限与失效条件。"},
    {"term": "文化身份认同", "meaning": "作者用以区分“华人”与“变得不是华人”的标准，并与通婚混血相对。", "evidence": "P031", "ambiguity": "血统、文化记忆与自我认同三者的权重未说明。"}
   ],
   "examples_and_targets": [
    "被讨论的呼声（非作者，属作者转述的对象）：呼吁海外华人团结、用投票权、成立组织、游说立法机构（P001）。",
    "被描述群体（作者转述其处境）：在美年轻一代痛心华人无参政传统，动员被族人冷淡浇凉（P002）。",
    "反问式对照（作者）：前苏联流亡遗民、俄罗斯移民，是否存在强大而团结的“美国俄罗斯裔协会”（P025）。",
    "历史例证（作者证据）：吴三桂、耿仲明/耿精忠、尚可喜为清效力、绞死明帝、割据东南西南而终至下场惨烈（P026–P028）。",
    "未点名的主体（作者）：所谓“祖国是足以争霸的大国，而且是敌国”这一假设中的祖国与所在国（P008），文中未具名。",
    "提问者说法（非作者）：海外华人不团结（Q001 属提问者）。"
   ],
   "conditions": [
    "范围限定：“在大部分国家”，作者并未主张所有国家皆如此（P004）。",
    "分条件判断：祖国为小国/坚定盟友则无问题；为争霸大国且为敌国才有自证清白的绝对必要（P008）。",
    "程度条件：“你能在多大程度上证明自己不是你祖国的内部代理人，你才会被许可有多大的生存空间”（P009）。",
    "手段条件：限制来自私人、私人企业的个人自由、经营自由与投票所体现的个人意志（P010）。",
    "时间条件：在华裔人口比例足以影响政治版图之前，该情况一直持续（P024）。",
    "语气限定：“无论是有意或是无意”“明确地意识到了”（P031）；“我不认为”“更多的是选择了”（P034）为作者表态而非绝对断言。",
    "两条路的穷尽性由作者断言，未讨论第三条路（P031）。"
   ],
   "rhetoric_and_tone": "冷静分析的说明语气，通篇以“你”指代华人组织者，把读者置于被审查位置；用“悖论”“逻辑链是这样的——”的编号推理（1）2）3））呈现论证；密集反问（“有强大而团结的‘美国俄罗斯裔协会’吗？”“他们团结起来了，又是个什么下场？”“这样的历史教训还不足够说明问题吗？”）；使用“原罪”“苦肉计”“叛意的证明”“掘墓人”式重词；末段以“我不认为华人们‘懦弱无能’”作辩护性转折，整体为替海外华人的选择作辩解而非指责。",
   "unresolved_questions": [
    "作者对“忠诚证明”机制的描述（唯一绝对有效的证明是“始终绝对服从安排”）未指明其来源：是法律、行政程序还是社会舆论，本文未说明。",
    "“足以争霸的大国，而且是一个敌国”这一假设中的祖国与所在国均未具名，无法据本文定位具体国家。",
    "吴三桂、耿仲明/耿精忠、尚可喜的史事被作者用作历史教训，其具体结局本文未展开，属需外部核查的历史叙述。",
    "“在大部分国家，华人是不能团结的”这一范围断言缺乏国别证据。",
    "“能垒”导致“越团结、越恶化”缺少数额或案例支撑，属预测性判断。",
    "P026 原文作“耿仲明/耿精忠精忠”，其中重复的“精忠”疑为原文笔误或排版残留；未作改动，需与原件核对。",
    "提问字段属提问者立场，正文未复述该问题。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P004", "quote": "不如说在大部分国家，华人是不能团结的", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P005", "quote": "因为华人的祖国太强大了。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P006", "quote": "当然意味着这类组织会有鲜明的种族身份", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P007", "quote": "如何保证你不是你祖国的代理人？", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P008", "quote": "那么你就存在自证清白的绝对必要", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P010", "quote": "不要以为生存空间是由某部成文法律就可以保障的", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P013", "quote": "恰恰就是自觉的不团结起来", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P016", "quote": "而绝对有效的忠诚证明只有一种，“始终绝对服从安排”", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P017", "quote": "“始终绝对服从安排”本身需要以“绝对满意现有安排”为有效证明", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P018", "quote": "于是一定会在“绝对忠诚”的考核中失败", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P021", "quote": "“团结起来”本身就是“叛意的证明”，任何其他证据都洗刷不了。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P022", "quote": "华人团结起来，反而会导致华人的群体的实际福利下降", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P023", "quote": "并且是越团结、越恶化。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P024", "quote": "足以影响政治版图之前，会一直持续", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P025", "quote": "有强大而团结的“美国俄罗斯裔协会”吗？", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P026", "quote": "为了大清帝国出生入死，连明朝皇帝都亲手绞死了", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P027", "quote": "都已经足够割据东南西南", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P028", "quote": "他们团结起来了，又是个什么下场？", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P030", "quote": "就是在深刻的理解群体动力学上有能敏锐的、毫无侥幸的“阅读空气”的能力", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P031", "quote": "要么老老实实与本地人通婚混血，直到后裔无论从自己的血统和文化记忆上都不能自认为是一个华人", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P032", "quote": "恰恰是最华人的表现，是对自己文化身份的最大忠诚", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P033", "quote": "是华人变得不是华人之后的结果", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P034", "quote": "我不认为华人们“懦弱无能”，不勇于选择自己的命运", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P035", "quote": "这个方案他们更不肯选/选也无用", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P020", "quote": "也会被认为是“民族苦肉计”，放长线钓大鱼", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P001", "quote": "一直都有人呼吁海外华人在所在国团结起来，充分利用自己的投票权", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["海外华人研究", "族裔政治", "国际关系", "文化认同", "社会心理学"],
   "issue_candidates": ["海外华人为何不团结", "族裔组织的忠诚审查", "参政与投票权动员", "文化身份认同的维持代价", "同化与通婚"],
   "text_function_candidates": ["答疑（回应知乎提问）", "解释", "论辩", "反驳（反驳“本性不团结”的指责）"],
   "object_candidates": ["海外华人", "美国", "前苏联流亡遗民", "俄罗斯移民", "吴三桂", "耿仲明/耿精忠", "尚可喜", "清朝", "明朝"],
   "working_keywords": ["华人团结", "忠诚证明", "自证清白", "原罪", "民族苦肉计", "能垒", "阅读空气", "文化身份认同", "通婚混血"]
  },
  "notes": "无图片节点。正文 P001–P035 已完整读取（共 1530 字），text 与 lexical 无 divergence。文中 P026 的“耿仲明/耿精忠精忠”疑有重复笔误，保留原文。作者对被反驳说法（“华人本性不团结”）的归属已作区分：该说法源自外部呼吁者，非作者主张。提问字段属提问者，正文未复述该问题。"
 },
 "a6d34ae5": {
  "analysis": {
   "question_context": "提问者问“如何看待「苏轼是一片星河，李白只是一颗流星」这一说法？”（引述该说法并提问，属提问者）。作者以三句短句作答，未作展开论证：苏轼“还算人”，李白“可能不是人”，并称李白写的东西在李白写之前都不是人话。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "作者对苏轼与李白分别给出评价：苏轼“还算人”，李白“可能不是人”。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003"], "summary": "作者给出理由式短句：李白写的东西，在李白写之前都不是人话。", "role": "reason"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "quoted_or_cited", "attribution": "questioner", "modality": "questioned", "statement": "提问者引述“苏轼是一片星河，李白只是一颗流星”这一说法并询问如何看待；该说法出自提问字段，不属作者主张，也无正文段落可作证据定位（提问字段不构成 Pnnn 段落）。", "evidence": []},
    {"claim_id": "C002", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者认为苏轼“还算人”（“还算”为限定语）。", "evidence": ["E1"]},
    {"claim_id": "C003", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者认为李白“可能不是人”（以“可能”表推测）。", "evidence": ["E2"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称李白写的东西，在李白写之前都不是人话。", "evidence": ["E3"]}
   ],
   "argument_steps": [
    "提问（Q001，提问者）：如何看待“苏轼是一片星河，李白只是一颗流星”。",
    "作者评价一（P001）：苏轼还算人。",
    "作者评价二（P002）：李白可能不是人。",
    "作者理由式短句（P003）：李白写的东西在李白写之前都不是人话。"
   ],
   "concept_usage": [
    {"term": "人", "meaning": "作者在本文用“还算人／可能不是人／不是人话”三处连用，指某种常人或可理解性标准，具体含义未界定。", "evidence": "P001", "ambiguity": "“人”在此是字面判断还是修辞性评价，本文未说明；三处用法（人、不是人、不是人话）含义是否一致亦不确定。"},
    {"term": "人话", "meaning": "作者称李白写的东西在其出现之前“都不是人话”，似指其表达前所未有的原创性，但本文未解释。", "evidence": "P003", "ambiguity": "确切含义依赖读者推断，本文未给出定义。"}
   ],
   "examples_and_targets": [
    "被评价对象（作者）：苏轼、李白（P001–P003）。",
    "提问者引述的说法（非作者）：「苏轼是一片星河，李白只是一颗流星」（Q001）。",
    "评价中所用的对照：李白写的东西“在李白写之前”的既有表达（P003）。"
   ],
   "conditions": [
    "全文仅 35 字、3 句，未给出任何前提、条件或适用范围。",
    "P002 以“可能”表推测，未作确定判断（P002）。",
    "P001 以“还算”作程度限定，未说明标准（P001）。"
   ],
   "rhetoric_and_tone": "极简的短句体，一句一行，无连接词、无论证展开；以“人／不是人／不是人话”的递进式谐音与反转制造效果，语气似调侃式的极高评价（将李白抬到非人高度），也可能是字面上的贬抑，本文未给出足够语境判断；未直接回应提问中“星河／流星”的比喻。",
   "unresolved_questions": [
    "本文只有三句，未展开论证，也未直接评价提问所引“苏轼是一片星河，李白只是一颗流星”的说法。",
    "“不是人”“不是人话”是褒义（超越常人）还是贬义，本文未说明，语气归属存疑，需研究者结合其他文章判断。",
    "brief 字段内容与 P001–P003 相同，但按规范 brief 不能单独支持作者主张。",
    "提问字段属提问者立场，正文未复述该问题；提问引述的说法未标注出处。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "苏轼还算人，", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "李白可能不是人。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "李白写的东西，在李白写之前都不是人话。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["文学评价", "古典文学", "人物评价"],
   "issue_candidates": ["苏轼与李白的比较", "李白表达的原创性", "“星河／流星”式比喻的接受"],
   "text_function_candidates": ["答疑（回应知乎提问）", "短评", "调侃式回答"],
   "object_candidates": ["苏轼", "李白"],
   "working_keywords": ["苏轼", "李白", "星河", "流星", "不是人", "不是人话"]
  },
  "notes": "无图片节点。正文仅 3 段 35 字，已完整读取；text 与 lexical 无 divergence（lexical 段落数 3 与正文一致）。本篇为极短回答，作者未展开论证，语气（褒／贬）在文内不足以判定，已在 unresolved_questions 登记。提问字段属提问者，未计入作者主张。"
 },
 "29323cf7": {
  "analysis": {
   "question_context": "提问者问“家装中，为什么说极简=极奢？”（提问字段属提问者，其中已含“极简=极奢”这一待解释的说法）。作者先否证一种流行理解（以为贵在设计与施工），再把“极奢”重新定位为极简所要求的生活方式本身的成本。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "开篇定位：作者认为误解太大所以要说明；极简主义设计的奢侈之处根本不在于设计多贵或施工多奢华，而“极简=极奢因为贵”这种说法本身透着一种穷劲儿。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P004"], "summary": "反驳造价说：自有住宅做得让自己心里舒坦谈不上“奢华”；以一般住宅面积多花几万、可享受几十年，且北上广深房价几百万上千万，多花几万十几万装修成本完全不成比例。", "role": "rebuttal"},
    {"unit_id": "U003", "paragraph_refs": ["P005", "P006"], "summary": "以类比提出替代标准：波音747内装长条凳不叫节约而叫浪费；浪费才是极奢。", "role": "definition"},
    {"unit_id": "U004", "paragraph_refs": ["P007", "P008"], "summary": "转入正题：极简奢华的地方不在这里，而在于与极简设计所用的生活方式是奢华的；作者提出下面几点。", "role": "transition"},
    {"unit_id": "U005", "paragraph_refs": ["P009", "P010", "P011"], "summary": "第一点成本：高度整洁有序非常脆弱，需大量时间维护，几乎必须请素质足够的专职帮佣且每年都要花钱；若想自己或让妻子代劳更便宜，作者建议别勉强，不会算账的人会越来越穷，最终会放弃。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P012", "P013"], "summary": "第二点成本：极简要么靠房子够大（喝茶、喝酒、看书、运动各一间，需求都装下且不拥挤），要么靠功能有社会性外包解决方案（整天不着家，小面积也简得起）。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P014", "P015", "P016", "P017", "P018", "P019"], "summary": "第三点成本（精神断舍离）：若真能一箪食一豆羹而不改其乐，则极简在装修家务上确无成本，隐蔽式开关与无主灯设计都是废话，房间应像配有电饭锅的单人牢房；但这条路要行得通更贵，因为消化欲望与挣扎所需的教育与精神维护贵得可怕，反而是最贵的一条；若是假的，就回到前两条。", "role": "qualification"},
    {"unit_id": "U008", "paragraph_refs": ["P020"], "summary": "结论：是因为这个，极简设计才奢华得很。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "极简主义设计的奢侈之处，根本不在于设计上多贵或者施工上多奢华。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "把极简的奢华归因于设计施工之贵，这种说法本身就透着一种穷劲儿。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "自己拥有的住宅做得让自己心里舒坦，谈不上“奢华”；以现在的一般住宅面积多花几万即可享受几十年，尤其北上广深一套房几百万上千万，多花几万十几万装修成本完全不成比例。", "evidence": ["E3", "E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "波音747内装长条凳不叫节约而叫浪费；浪费才是极奢。", "evidence": ["E5", "E6"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "极简奢华的地方不在于造价，而在于与极简设计所用的生活方式是奢华的。", "evidence": ["E7"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "高度的整洁有序状态非常脆弱，需要花费大量时间维护，几乎必须请一个素质足够的专职帮佣，而且这笔钱每年都要。", "evidence": ["E8"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "若觉得自己或叫妻子来做更便宜，就不如别勉强；不会算账的人会越来越穷，到最后会觉得这事多余而直接放弃，简不了几天。", "evidence": ["E9", "E10"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "极简设计要么靠房子够大（各功能分间而间间不拥挤），要么靠功能有社会性的外包解决方案，从而小面积也简得起。", "evidence": ["E11", "E12"]},
    {"claim_id": "C009", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "如果自称能精神断舍离（一箪食、一豆羹而不改其乐）是真的，那极简在装修与家务上确实一点成本都没有，隐蔽式开关、无主灯设计都是废话，房间应像配有电饭锅的单人牢房。", "evidence": ["E13", "E14", "E15"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "但精神断舍离这条路要想行得通更贵——消化自己的欲望和挣扎所需的教育与精神维护贵得可怕，反而是几条路里最贵的一条。", "evidence": ["E16", "E17"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "如果精神断舍离是假的，那就兜回去了，回到了前两条路。", "evidence": ["E18"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "是因为这个，极简设计才奢华得很。", "evidence": ["E19"]}
   ],
   "argument_steps": [
    "提问（Q001，提问者）：家装中为什么说极简=极奢。",
    "否定流行理解（P002–P003）：奢侈之处不在设计贵或施工奢华，该说法透着穷劲儿。",
    "反驳造价论（P004）：以面积、年限与一线城市房价比例说明装修多花的几万十几万不成比例。",
    "提出标准（P005–P006）：以波音747内装长条凳为例，把“浪费”而非“花钱”定为极奢。",
    "转向正题（P007–P008）：奢侈之处在于极简所要求的生活方式。",
    "成本一（P009–P011）：维护整洁需专职帮佣且年年花钱，自行代劳者最终放弃。",
    "成本二（P012–P013）：房子够大或功能外包，二者之一才简得起。",
    "成本三（P014–P018）：精神断舍离若为真则无成本，但其教育与精神维护更贵，是最贵的一条。",
    "兜底（P019）：若为假，则回到前两条路。",
    "结论（P020）：极简设计因此才奢华得很。"
   ],
   "concept_usage": [
    {"term": "极奢", "meaning": "作者把它从“造价昂贵”改写为“浪费”和“生活方式昂贵”，并以波音747内装长条凳界定浪费。", "evidence": "P006", "ambiguity": "作者未给出“浪费”的判定标准，仅以例证说明。"},
    {"term": "极简设计", "meaning": "本文指家装中的极简主义设计，其奢侈处在于维护、空间或功能外包、精神维护三方面的生活方式成本。", "evidence": "P007", "ambiguity": "文中“与极简设计所用的生活方式”一句表述略显不顺，是否为“与极简设计相配的生活方式”之意，本文未明说。"},
    {"term": "精神断舍离", "meaning": "作者用以指自称能以一箪食、一豆羹自足而不改其乐的态度，并称其教育与精神维护成本最高。", "evidence": "P014", "ambiguity": "作者对该词的可实现性持条件式态度（“如果是真的”“如果是假的”）。"},
    {"term": "社会性的外包解决方案", "meaning": "作者指把喝茶、喝酒等功能放到家外的场所，从而减少家中所需功能面积。", "evidence": "P013", "ambiguity": "未说明外包的长期费用与传统装修成本的比较。"}
   ],
   "examples_and_targets": [
    "类比（作者）：波音747内装长条凳，用以说明“浪费”而非节约（P005）。",
    "例举（作者）：满天的吊顶、无主灯设计、隐蔽式开关（P004、P015）。",
    "例举（作者）：喝茶一间、喝酒一间、看书一间、运动一间（P012）；要喝茶有喝茶的去处、要喝酒有喝酒的去处（P013）。",
    "用典（作者）：一箪食，一豆羹，回也不改其乐（P014，指颜回之乐，文中未点名出处）。",
    "比喻（作者）：房间应看起来像配有电饭锅的单人牢房（P016）。",
    "被反驳的说法（非作者）：极简=极奢是因为设计贵或施工奢华（提问语境与 P002–P003 所指）。"
   ],
   "conditions": [
    "限定词“根本不在于”“谈不上”：作者否定的是把极简之奢归因于造价（P002、P004）。",
    "对象条件：“自己拥有的住宅”为前提（P004）。",
    "规模条件：以“现在的一般住宅面积”“多花个几万”为估算基础；并特别举北上广深房价几百万上千万作比例对照（P004）。",
    "条件句：“如果你觉得这块你自己来或者叫你妻子来更便宜”（P010）；“如果是真的”（P015）；“如果是假的”（P019）。",
    "程度限定：“几乎必须请一个专职的帮佣”（P009）；“贵得可怕”（P017）。",
    "时间条件：“这笔钱每年都要”（P009）；“你要享受几十年”（P004）。",
    "路径穷尽性：作者把可行路径归为三条（大房子、功能外包、精神断舍离），未讨论其他可能（P012–P019）。"
   ],
   "rhetoric_and_tone": "家装答问的口语化点评语气，直接、略带讥讽（“这种说法本身就透着一种穷劲儿”“不会算账的人会越来越穷的”）；连续反问（“哪有什么‘奢华’可言？多做个满天的吊顶就叫奢华了？无主灯就叫奢华了？谈得到什么奢华？”）；用波音747装长条凳、单人牢房等夸张类比；结尾以“是因为这个，极简设计才奢华得很”收束，整体是先破后立的短评结构。",
   "unresolved_questions": [
    "P021 末尾“什么是现代极简装修风格？装修成本大不大？”与正文其余部分不相衔接，被语料标注为 text_tail_not_in_lexical（字符 767 起，lexical 未覆盖），疑为平台附加的相关问题链接，未作为作者正文主张使用。",
    "P007“与极简设计所用的生活方式是奢华的”一句表述不顺，是否为笔误或省略，本文未说明。",
    "作者给出的费用数额（多花几万、十几万、几百万上千万）为概括性估算，未说明数据来源，属待外部核查。",
    "“精神断舍离”的真实可行性被作者置于“如果是真的／如果是假的”两种假设下讨论，作者本人倾向哪一侧未明说（仅称若为真则更贵）。",
    "提问字段属提问者立场，其“极简=极奢”的说法被作者部分反驳（否证造价说），归属已在 claims 中区分。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P002", "quote": "极简主义设计的奢侈之处，根本不在于设计上多贵或者施工上多奢华。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P003", "quote": "这种说法本身就透着一种穷劲儿。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "自己拥有的住宅，做得让自己心里舒坦，哪有什么“奢华”可言？", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "多花几万十几万装修成本完全不成比例", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "波音747，内装长条凳，这不叫节约，这叫浪费。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "浪费才是极奢。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "而是在于与极简设计所用的生活方式是奢华的", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P009", "quote": "高度的整洁有序状态是非常脆弱的，你得花费大量的时间去维护。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P010", "quote": "不会算账的人会越来越穷的", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P011", "quote": "简不了几天。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P012", "quote": "极简的设计要么是房子够大", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P013", "quote": "要么就是这些功能你都有社会性的外包解决方案", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P014", "quote": "有人自称自己可以精神断舍离，一箪食，一豆羹，回也不改其乐。", "relation": "context"},
    {"key": "E14", "paragraph_id": "P015", "quote": "那你极简起来在装修上、家务上真一点成本都没有", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P016", "quote": "你的房间应该看起来像配有电饭锅的单人牢房。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P017", "quote": "这要想行得通，更贵", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P018", "quote": "这反而是这几条路里最贵的一条。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P019", "quote": "如果是假的，那你就兜回去了，回到了前两条。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P020", "quote": "是因为这个，极简设计才奢华得很。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P001", "quote": "误解太大了，说两句。", "relation": "context"},
    {"key": "E21", "paragraph_id": "P004", "quote": "尤其是北上广深，一套房子几百万上千万", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["家装设计", "消费与生活方式", "室内设计", "生活成本"],
   "issue_candidates": ["极简与极奢的关系", "极简的维护成本", "精神断舍离的实际代价", "装修支出的比例合理性"],
   "text_function_candidates": ["答疑（回应知乎提问）", "评论", "反驳流行说法", "经验总结"],
   "object_candidates": ["波音747", "北上广深", "专职帮佣", "颜回（用典未点名）"],
   "working_keywords": ["极简", "极奢", "浪费", "无主灯", "隐蔽式开关", "精神断舍离", "社会性的外包解决方案", "穷劲儿"]
  },
  "notes": "无图片节点。正文 P001–P020 为作者文字，已完整读取；P021 为 text_tail_not_in_lexical（字符 767 起），疑为平台附加的相关问题链接（“什么是现代极简装修风格？装修成本大不大？”），未作为作者主张使用；骨架 divergence=true 即指此处。提问字段属提问者，其中“极简=极奢”的说法已被作者部分反驳，归属已在 main_claims 中区分。"
 },
 "edf11fe5": {
  "status": "needs_reread",
  "image_checked": False,
  "analysis": {
   "question_context": "提问者问“中国是否应该大量制造航母？”（提问字段属提问者）。作者先否证“世界帝国必须是强海权国家”这一前提，主张陆权才是常态、海权只是技术代差下的短暂现象，进而给出对中国航母数量的预测：够用即可、峰值不超过五艘、二十年内停止造新舰。正文含 5 个图片节点与多句图注，图片内容未经核验。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "否证前提并提出主张：很多人被美国、大英帝国、西班牙帝国、葡萄牙、荷兰的成功晃花眼，误以为世界帝国必须是强海权国家；作者称海权国家是历史昙花，最终回到陆权国家统治大陆、海洋重回沿岸和平割据的常态。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005"], "summary": "地理前提与推论：亚欧非三洲是一整块大陆且在未来是人类绝对的人口与文化中心；只要这一点不变，陆权国家作为文明中心的格局不会真正改变；海权国家只能享有短暂技术代差带来的黄金时代，必须提前铺垫退场，否则“硬着陆”退场后果可能难以承受。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007", "P008", "P009"], "summary": "拒止能力论证：陆权大国可在沿岸撑起最宽 1500–3000 公里保护伞，小国则通过军事合作条约、出租基地分享拒止能力；亚欧非海岸外推 3000 公里拒止线可覆盖世界绝大部分资源、人口、航道；进入该区域的敌意舰只抵挡不住陆基导弹与空军饱和攻击，即使航母战斗群也不行。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P010", "P011", "P012"], "summary": "行动建议：航空母舰这类水上兵器历史寿命不长，预计不过百年后水面舰艇的军事用途将走向终结；眼下急用造到足用即可，造得太多没有意义且挤占将来空天部队与太空部队的预算。", "role": "action_advice"},
    {"unit_id": "U005", "paragraph_refs": ["P013", "P014", "P015", "P016", "P017", "P018", "P019"], "summary": "进一步论证：即使美国再过不到三四十年也将裁撤大部分舰队；水面舰艇安全生存区是离所有非盟国海岸均 1500 公里的剩余海域（太平洋会缩到只剩里海大小，二十年后该数字将达 3000 甚至 5000 公里）；任何水面舰队都无法顶住天基星座分米级定位导航下陆基近乎无限量的无人机与反舰导弹饱和攻击；大洋上的舰队只能无人化当作准备弃守的浮岛，派人驻守不人道；作者反问为何要用水面航行这种低效手段派遣无人机。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P020", "P021", "P022", "P023"], "summary": "预测性结论：作者相信中国航母舰队的峰值不会超过五艘（训练舰不算）；应在二十年内结束再造新舰；从 2030（甚至早至 2025 年）开始向载人/无人舰混编舰队转变；航空母舰的意义会迅速消退直至消失。", "role": "conclusion"},
    {"unit_id": "U007", "paragraph_refs": ["P024", "P025", "P026", "P027"], "summary": "图注与附图说明：作者称下面的标尺都是三千公里，请读者看清陆基反舰导弹射程达 3000 与 1500 公里时太平洋上绝对安全区有多大；并注明未计算空射型，随后给出 DF-26（射程 2900 公里，考虑地球曲率）的射程覆盖范围与卫星对航母的光学侦察能力两幅图。此单元与 IMG001–IMG005 对应，图片内容未核验。", "role": "context"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "很多人被美国、大英帝国、西班牙帝国、葡萄牙、荷兰的成功晃花了眼，误以为成就世界帝国必须是强海权国家。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "海权国家将是历史上的昙花一现，只是短时间内的特殊现象；最终历史要回到常态——陆权国家统治大陆，海洋重回沿岸和平割据状态。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只要亚欧非是一整块大陆、且在可预见的未来是人类绝对的人口与文化中心这一点不变，陆权国家作为人类文明中心的基本格局就不会有真正的改变。", "evidence": ["E3", "E4"]},
    {"claim_id": "C004", "claim_type": "author_qualified", "attribution": "author", "modality": "predicted", "statement": "海权国家无论怎么活跃，也只能享有短暂技术代差带来的黄金时代，必须提前铺垫退场；若以“硬着陆”方式退场，后果可能难以承受。", "evidence": ["E5", "E6"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "陆权大国可在自己沿岸撑起最宽 1500–3000 公里的保护伞，将海权国家海军拒止在外；做不到的小国也会倒向临近陆权大国，通过军事合作条约、出租基地分享拒止能力。", "evidence": ["E7"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "亚欧非大陆海岸向外张开 3000 公里拒止线，足以将世界绝大部分资源、人口、航道置于羽翼之下；进入该区域的敌意舰只抵抗不住陆基导弹与空军饱和攻击，即使航母战斗群也不行。", "evidence": ["E8", "E9", "E10"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "航空母舰这类水上兵器并没有太长的历史寿命，预计不过百年之后，水面舰艇的军事用途就会走向终结。", "evidence": ["E11"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "眼下急用，造到足用即可；造得太多没有意义，而且挤占将来空天部队以及太空部队的预算。", "evidence": ["E12", "E13"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "即使美国，再过不到三四十年也将裁撤大部分舰队；在战时派遣载人平台进入对方占据绝对制海、制空、制电磁权的区域，恐怕是违背军事伦理的。", "evidence": ["E14", "E15"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "水面舰艇的安全生存区域是离所有非盟国海岸均 1500 公里的剩余海域，太平洋都会缩到只剩下里海的大小；何况再过二十年，这个数字将是 3000 甚至 5000 公里。", "evidence": ["E16", "E17"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "任何水面舰队都无法顶住由大量天基星座分米级定位导航的、来自陆基的近乎无限量的武装无人机和反舰导弹的饱和攻击；造 1000 枚中程导弹比造一个航母战斗群快太多。", "evidence": ["E18", "E19"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "布设在大洋上的舰队只能无人化后当作准备弃守的无人自动化浮岛；派人驻守，在战争情况下是不人道的。", "evidence": ["E20"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者反问：同样要派遣无人机，为什么要用水面航行这样低效的手段。", "evidence": ["E21"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作者相信中国航母舰队的峰值不会超过五艘（训练舰不算）。", "evidence": ["E22"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "中国应该在二十年内就结束再造新舰；从 2030（甚至早至 2025 年）开始就会向载人/无人舰混编舰队转变；航空母舰的意义会迅速消退，直至消失。", "evidence": ["E23", "E24", "E25"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称所附标尺均为三千公里，用以显示陆基反舰导弹射程达 3000 公里和 1500 公里时太平洋上绝对安全区的范围，并注明这没有计算空射型。", "evidence": ["E26", "E27"]}
   ],
   "argument_steps": [
    "提问（Q001，提问者）：中国是否应该大量制造航母。",
    "否证前提（P001）：被海权帝国成功晃花眼，误以为世界帝国必须强海权。",
    "提出历史判断（P002）：海权是昙花，常态是陆权统治大陆、海洋沿岸割据。",
    "给出地理前提（P003）：亚欧非为一整块大陆且是人类人口与文化中心。",
    "推论（P004–P005）：陆权中心格局不变；海权只能有技术代差下的黄金时代，须预备退场。",
    "技术论证（P006–P009）：沿岸 1500–3000 公里拒止伞与 3000 公里拒止线，航母战斗群亦无法进入。",
    "预测兵器寿命（P010）：百年内水面舰艇军事用途终结。",
    "给出建议（P011–P012）：造到足用即可，过多无意义且挤占空天与太空预算。",
    "外推至美国（P013）：三四十年内裁撤大部分舰队，载人平台进入对方优势区违背军事伦理。",
    "量化生存区（P014–P015）：离非盟国海岸 1500 公里，太平洋缩至里海大小，未来或达 3000–5000 公里。",
    "饱和攻击论证（P016–P017）：陆基无人机与反舰导弹近乎无限量，成本与速度压倒航母战斗群。",
    "出路（P018–P019）：舰队只能无人化当浮岛；反问为何用水面航行派遣无人机。",
    "预测结论（P020–P023）：峰值不超五艘、二十年内停止造新舰、2030 起混编、航母意义消失。",
    "附图说明（P024–P027）：标尺 3000 公里、未计空射型、DF-26 射程覆盖与卫星光学侦察图。"
   ],
   "concept_usage": [
    {"term": "陆权国家／海权国家", "meaning": "作者以国家主要依托陆地还是海洋区分，并主张陆权是历史常态、海权是技术代差期内的短暂现象。", "evidence": "P002", "ambiguity": "作者未给出划分标准（如海军预算占比或战略取向）。"},
    {"term": "拒止", "meaning": "作者用指陆权大国以陆基导弹与空军在沿岸 1500–3000 公里范围排除海权国家海军的能力；小国可通过条约与基地租借分享。", "evidence": "P006", "ambiguity": "未说明拒止能力的技术前提（如侦察、定位、弹药产能）的可靠性。"},
    {"term": "绝对安全区", "meaning": "作者用指水面舰艇可安全生存的海域，即离所有非盟国海岸均 1500 公里的剩余海域。", "evidence": "P014", "ambiguity": "该概念依赖“所有非盟国海岸”这一理想化条件，作者未讨论盟国变动。"},
    {"term": "硬着陆", "meaning": "作者用以指海权国家未提前铺垫退场而被迫退出的方式，并称其后果可能难以承受。", "evidence": "P005", "ambiguity": "未给出“硬着陆”的具体判定指标。"},
    {"term": "军事伦理", "meaning": "作者在 P013 与 P018 两次以此评估派遣载人平台进入对方绝对优势区域及派人驻守浮岛的行为。", "evidence": "P013", "ambiguity": "作者未说明其所依据的军事伦理准则。"}
   ],
   "examples_and_targets": [
    "被否证的说法（非作者）：许多人认为成就世界帝国必须是强海权国家（P001）。",
    "历史例举（作者修辞/论据）：美国、大英帝国、西班牙帝国、葡萄牙、荷兰的成功（P001）。",
    "地理论据（作者）：亚欧非三洲为一整块大陆（P003）；海洋、沙漠、高原等未在本文出现（属他篇）。",
    "技术例举（作者）：陆基反舰导弹射程 3000 与 1500 公里、DF-26 射程 2900 公里（考虑地球曲率）、天基星座分米级定位导航（P024、P026、P016）。",
    "对照对象（作者）：美国海军舰队（P013）；太平洋缩至里海大小（P014）。",
    "图像材料（作者附图，内容未核验）：IMG001–IMG005，分别对应 P024 前后的标尺图、DF-26 射程覆盖图与卫星对航母光学侦察能力图（P024、P026、P027）。",
    "提问者说法（非作者）：中国是否应该大量制造航母（Q001）。"
   ],
   "conditions": [
    "前提条件：“只要这一点不变”（亚欧非为一整块大陆且是人口与文化中心），陆权格局才不会真正改变（P004）。",
    "时间范围：“在可以预见的未来”（P003）；“不过百年之后”（P010）；“再过不到三四十年”（P013）；“再过二十年”（P014）；“二十年内”（P021）；“从2030（甚至早至2025年）开始”（P022）。",
    "距离条件：最宽 1500–3000 公里保护伞（P006）；离所有非盟国海岸均 1500 公里（P014）。",
    "后果条件：“否则，如果发生‘硬着陆’方式的退场”，后果可能难以承受（P005）。",
    "技术条件：进入拒止区的舰只“如果被证实是敌意的”（P007）；依赖天基星座分米级定位导航（P016）。",
    "对象限定：小国需通过军事合作条约、出租基地才能获得分享的拒止能力（P006）。",
    "作者明确标注未计入的项：“这没有计算空射型”（P025）。",
    "预测均以作者信念语标示：“我相信”“预计”“恐怕”“应该”（P020、P010、P013、P021）。"
   ],
   "rhetoric_and_tone": "军事战略推演式的断言语气，使用“毫无悬念”“绝对优势”“一直持续”类强度词；以反问收束段落（“水面舰队拿什么顶？锅吗？”“为什么要用水面航行这样低效的手段？”）；用“太平洋都会缩到只剩下里海的大小”“五洋虽大，却无可立锥处”等直观类比帮助量化；末段转为图注与读图指令（“下面的标尺都是三千公里。看看清楚……”），并以平台附加的问句链接结束（P028）。",
   "unresolved_questions": [
    "本篇含 5 个图片节点（IMG001–IMG005），子代理无读图能力，图片内容、标尺数值与图注对应关系均未核验，需人工或多模态复核后补读。",
    "P028“假如卫星被摧毁，战争会怎样？”被语料标注为 text_tail_not_in_lexical（字符 1394 起，lexical 未覆盖），疑为平台附加的相关问题链接，未作为作者正文主张使用。",
    "文中拒止距离（1500、3000、5000 公里）、导弹射程（DF-26 2900 公里）、舰队规模（五艘）与时间点（2030、2025）均为作者断言或预测，需外部核查。",
    "P012 与 P013 提到的“空天部队以及太空部队”是否为已存在编制，本文未说明，属需外部核查的事实性表述。",
    "P013“违背军事伦理”所依据的准则本文未说明。",
    "提问字段属提问者，作者未直接以“应该／不应该大量制造”作答，而是以“造到足用即可”与峰值预测回应，二者关系需研究者复核。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "误以为成就世界帝国必须要是强海权国家", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "最终历史还是要回到它的常态——陆权国家统治大陆，海洋重回沿岸和平割据状态", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "亚欧非三洲是一整块大陆，而且在可以预见的未来会是人类绝对的人口和文化中心", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "只要这一点不变，陆权国家作为人类文明的中心的基本格局就不会有真正的改变", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P004", "quote": "也只能享有短暂的技术代差带来的黄金时代", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P005", "quote": "对海权国家的后果可能是难以承受的", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P006", "quote": "陆权大国可以在自己的沿岸撑起最宽1500-3000公里的保护伞", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P007", "quote": "足可以将世界绝大部分的资源、人口、航道置于自己不容侵犯的羽翼之下", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P007", "quote": "无论如何也抵抗不住四面聚集而来的陆基导弹和空军的饱和攻击", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P009", "quote": "即使是航母战斗群也不行。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P010", "quote": "预计不过百年之后，水面舰艇的军事用途就会走向终结", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P011", "quote": "眼下急用，造到足用即可。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P012", "quote": "造得太多，没有意义，而且挤占将来空天部队以及太空部队的预算", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P013", "quote": "再过不到三四十年，也将裁撤大部分舰队", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P013", "quote": "恐怕是违背军事伦理的", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P014", "quote": "水面舰艇的安全生存区域是离所有非盟国海岸均1500公里的剩余海域", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P014", "quote": "太平洋都会缩到只剩下里海的大小", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P016", "quote": "任何水面舰队都无法顶住由大量天基星座分米级定位导航的", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P016", "quote": "造1000枚中程导弹比造一个航母战斗群快太多了", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P018", "quote": "只能无人化后当作准备弃守的无人自动化浮岛", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P019", "quote": "为什么要用水面航行这样低效的手段？", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P020", "quote": "我相信中国航母舰队的峰值不会超过五艘（训练舰不算）", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P021", "quote": "而且应该在二十年内就结束再造新舰了。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P022", "quote": "就会开始向载人/无人舰混编舰队转变", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P023", "quote": "航空母舰的意义会迅速消退，直至消失。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P024", "quote": "下面的标尺都是三千公里。", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P025", "quote": "这没有计算空射型。", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P026", "quote": "下面是射程2900公里得DF-26反舰导弹的射程覆盖范围（考虑了地球曲率）", "relation": "context"},
    {"key": "E29", "paragraph_id": "P027", "quote": "卫星对航母的光学侦察能力：", "relation": "context"},
    {"key": "E30", "paragraph_id": "P017", "quote": "水面舰队拿什么顶？锅吗？", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P015", "quote": "五洋虽大，却无可立锥处。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["军事战略", "地缘政治", "海军与航母", "导弹与拒止能力", "国际安全"],
   "issue_candidates": ["中国是否应大量制造航母", "海权与陆权的历史地位", "陆基反舰导弹拒止线", "航母战斗群的生存性", "水面舰艇的未来"],
   "text_function_candidates": ["答疑（回应知乎提问）", "战略预测", "论辩", "图示说明"],
   "object_candidates": ["中国", "美国", "亚欧非大陆", "大英帝国", "西班牙帝国", "葡萄牙", "荷兰", "DF-26", "太平洋", "里海", "空天部队", "太空部队"],
   "working_keywords": ["陆权国家", "海权国家", "拒止", "保护伞", "绝对安全区", "饱和攻击", "硬着陆", "无人自动化浮岛", "载人/无人舰混编", "军事伦理", "载人平台"]
  },
  "notes": "本篇含 5 个图片节点（IMG001..IMG005，源为 asset.sooon.ai 图片链接），子代理无读图能力，图片内容未经核验，故 status=needs_reread、image_checked=false；已读部分为正文文本 P001–P028。骨架 divergence=true 对应 P028“假如卫星被摧毁，战争会怎样？”（text_tail_not_in_lexical，字符 1394 起），疑为平台附加的相关问题链接，未作为作者主张使用。文末 P024、P026、P027 为图注，其对应图像内容须在图像核验后补读。"
 },
 "8d16c884": {
  "analysis": {
   "question_context": "提问者（相亲当事人）说自己在相亲时因不想磨叽而直接说明原则，被对方喊去出家，问是否自己过分（提问字段属提问者）。作者回答：这没有任何原则问题，甚至是优秀的策略；并指出指责者多是在为自己消解性焦虑，真正要确认的是自己是否从理智上确认采用该策略并接受其连带后果。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "总体评价与该策略的利弊：作者认为提问者的做法没有原则问题、甚至是优秀策略；好处是筛出的对象相对值得认真投入，而“坏处”是目前中国能过关的人客观上比例很小。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004"], "summary": "修正建议：若在意成功率，应做的修正不是改变过滤条件，而是扩大筛选面；以“大浪淘沙，沙里淘金”作喻。", "role": "action_advice"},
    {"unit_id": "U003", "paragraph_refs": ["P005", "P006", "P007", "P008"], "summary": "对指责者的动因分析：无数人指责提问者是为消解自己的性焦虑，生怕“引起效仿”恶化自身性困境；他们打着为你考虑的旗号实为自己考虑，并偷换出一个“恨嫁女”；而提问者一开始就挑明了对“找个人结婚”没有特别强迫性的需求，“筛选不到合适人选你肯定不能接受”这一前提是ta们自己加上去的。", "role": "rebuttal"},
    {"unit_id": "U004", "paragraph_refs": ["P009", "P010"], "summary": "风险论证：如果真的是宁缺毋滥，这样做不但没有错误，甚至非常正确；迅速锁定一个过不了关的对象投入时间与资源专一交往，是风险极大、极其不明智的显著错误，其收益之小、风险之大远非“很难找到合适的”可比；很多人是四五年、上十年后拖着被生父实质抛弃的孩子、带着心理创伤与财务、社会关系困境来体会后果，届时批判者没有一个会分担负担。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P011", "P012"], "summary": "作者给出的真正问题与条件：要想清楚自己是否从理智上确认采用该策略并接受其负面连带后果，分清是因懒惰和软弱而选择，还是因主动计划和勇敢承担而这样做；如果是后者，就不必害怕。", "role": "qualification"},
    {"unit_id": "U006", "paragraph_refs": ["P013", "P014"], "summary": "对该原则的评价：本质上其条款原则还是 live and let live，很合情合理，也很健康；这是一种人格健全的人才能看得懂的性感。", "role": "claim"},
    {"unit_id": "U007", "paragraph_refs": ["P015"], "summary": "预期效果：若是主动计划与勇敢承担，即使要求一字不改照念，语气与神态也会自然镇定温柔，这种态度自有一种对真正强大者的吸引力，对方的反应足以让人发自内心惊喜。", "role": "claim"},
    {"unit_id": "U008", "paragraph_refs": ["P016", "P017"], "summary": "以词句作结：“那便是金风玉露一相逢，胜却人间无数。”", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "提问者的做法其实没有任何原则问题，甚至是优秀的策略。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "该策略的好处是筛选过关的对象相对值得认真投入；而“坏处”则是目前中国能过关的人客观上比例很小。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "如果比较在意成功率，需要做的修正不是改变过滤条件，而是扩大筛选面。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "无数人指责提问者，是因为ta们要消解自己的性焦虑，生怕“引起效仿”而进一步恶化自己的性困境。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "指责者说这些话不是为提问者考虑而是为自己考虑，只是打着为提问者考虑的旗号，并把提问者偷换成自己造出的“恨嫁女”。", "evidence": ["E5", "E6"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "提问者一开始就挑明了对“找个人结婚”没有特别强迫性的需求；“筛选不到合适人选你肯定是不能接受的”这一前提是指责者自己悄悄加上去的。", "evidence": ["E7", "E8"]},
    {"claim_id": "C007", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "如果提问者真的是宁缺毋滥，这样做不但没有错误，甚至是非常正确的做法；反之，迅速锁定一个其实过不了关的对象投入时间与资源专一交往，是风险极大、极其不明智的显著错误。", "evidence": ["E9", "E10"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "很多人是四五年、上十年后拖着一个被生父实质抛弃的孩子、带着心理创伤与财务及社会关系困境来体会这个后果；届时嘲弄与批判的人没有一个会分担负担。", "evidence": ["E11", "E12"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "提问者的主要问题是想清楚自己是否从理智上确认要采取这个策略并接受它的负面连带后果，即分清是因懒惰和软弱而选择，还是因主动计划和勇敢承担而这样做。", "evidence": ["E13"]},
    {"claim_id": "C010", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "如果是后者（因主动计划和勇敢承担而选择），就不必害怕。", "evidence": ["E14"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "本质上其条款原则还是 live and let live，是一种很合情合理的原则，也很健康。", "evidence": ["E15"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这是一种人格健全的人才能看得懂的性感。", "evidence": ["E16"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "若是主动计划与勇敢承担，即使要求一个字都不改照念一遍，语气和神态也会自然而然镇定而温柔，这种态度自有一种对真正强大者的吸引力，对方的反应也足以让人发自内心惊喜。", "evidence": ["E17", "E18"]},
    {"claim_id": "C014", "claim_type": "quoted_or_cited", "attribution": "unknown", "modality": "asserted", "statement": "作者以“金风玉露一相逢，胜却人间无数”两句作结，用作对上述理想相遇的形容；文中未标明该句出处，故归属记为 unknown，仅记为引用而非作者论断。", "evidence": ["E19", "E20"]}
   ],
   "argument_steps": [
    "提问（Q001，提问者）：直接说明原则被喊去出家，是否自己过分。",
    "总评（P001）：没有原则问题，甚至是优秀策略。",
    "利弊（P002）：好处是筛出值得投入者；坏处是过关者比例客观上很小。",
    "建议（P003–P004）：修正方向是扩大筛选面而非降低条件；以“大浪淘沙，沙里淘金”作喻。",
    "动因反驳（P005–P006）：指责源于ta们自身的性焦虑与“怕被效仿”，并为提问者偷换出一个“恨嫁女”。",
    "事实澄清（P007–P008）：提问者本无强迫性结婚需求；对方所设“你肯定不能接受”的前提是外加的。",
    "风险对比（P009–P010）：宁缺毋滥者这样做是正确的；草率锁定过不了关的对象风险极大，且批判者不会分担后果。",
    "提出真正的问题（P011–P012）：确认动机是懒惰软弱还是主动承担；若为后者则不必害怕。",
    "原则评价（P013–P014）：live and let live 合情合理且健康，是人格健全者才看得懂的性感。",
    "预期（P015）：态度镇定温柔本身即具吸引力，对方反应会带来惊喜。",
    "以词句收束（P016–P017）：金风玉露一相逢，胜却人间无数。"
   ],
   "concept_usage": [
    {"term": "过滤条件／筛选面", "meaning": "作者把提问者的原则表述为“过滤条件”，主张修正应针对“筛选面”而非条件本身。", "evidence": "P003", "ambiguity": "作者未说明“筛选面”如何扩大（渠道、地域、频次等）。"},
    {"term": "宁缺毋滥", "meaning": "作者用以指提问者所声明的立场，并称若成立则其做法非常正确。", "evidence": "P009", "ambiguity": "作者未给出判定“真的是宁缺毋滥”的标准。"},
    {"term": "性焦虑", "meaning": "作者用以解释指责者动因的心理机制，称其通过打击他人选择来防止“引起效仿”。", "evidence": "P005", "ambiguity": "属作者对他人动机的推断，无经验证据支持。"},
    {"term": "恨嫁女", "meaning": "作者称这是指责者悄悄偷换出来的、代替提问者的一个形象。", "evidence": "P006", "ambiguity": "该词带贬义，作者以引号标出并归为他人所造。"},
    {"term": "live and let live", "meaning": "作者对提问者条款原则性质的概括，评价为合情合理、健康。", "evidence": "P013", "ambiguity": "作者未解释该原则与其所批评的“朴素自由主义”在他篇中的关系。"},
    {"term": "人格健全的人才能看得懂的性感", "meaning": "作者用以形容上述原则与态度所具有的吸引力。", "evidence": "P014", "ambiguity": "“性感”在此为评价性修辞，非本文可界定的概念。"}
   ],
   "examples_and_targets": [
    "被反驳对象（作者）：指责与嘲弄提问者的“无数人”、“这里这些嘲弄你、批判你、鼓吹要你降低标准、‘手段变得温柔些’的人”（P005、P010）。",
    "提问者自身材料（提问字段，非作者）：相亲时直接说明原则、被对方喊去出家（Q001）。",
    "作者举例（预测性情形）：四五年、上十年后拖着被生父实质抛弃的孩子、带着心理创伤与满目疮痍的财务、社会关系困境来体会后果的“很多人”（P010）。",
    "成语/谚语（作者）：大浪淘沙，沙里淘金（P004）。",
    "引语（作者引用、未标出处）：“金风玉露一相逢，胜却人间无数”（P016、P017）。",
    "对比项（作者）：“很难找到合适的”这一通常说法（P009）。"
   ],
   "conditions": [
    "条件句：“如果你比较在意成功率的话”（P003）；“如果你真的是宁缺毋滥的话”（P009）；“如果是后者，你就不用害怕”（P012）；“因为如果是这样”（P015）。",
    "口气限定：作者用“其实”“客观上”“甚至”等词表态（P001、P002、P009）。",
    "分情形讨论：作者把动机分为因懒惰和软弱而选择、与因主动计划和勇敢承担而选择两种，并只对后者给出肯定（P011、P012）。",
    "范围限定：“目前中国能过关的人客观上的确比例很小”把判断限定在当下中国（P002）。",
    "未设条件处：作者未说明“扩大筛选面”的具体办法与成本，也未讨论提问者原则的具体内容。"
   ],
   "rhetoric_and_tone": "劝慰兼鼓励的直白语气，用第二人称“你”直接对提问者说话，把读者与“这里的这些人”（指责者）对立起来；使用带贬抑色彩的判断（“ta们要消解自己的性焦虑”“打着为你考虑的旗号”），ta 为不分性别的第三人称写法；以“大浪淘沙，沙里淘金”与“金风玉露一相逢，胜却人间无数”两句熟语起收束作用；结尾用拆分两行的方式排出词句，形成咏叹式收尾；整体为辩护性而非中立描述。",
   "unresolved_questions": [
    "作者未追问提问者“原则”的具体内容，也未讨论其内容是否合理，只评价“直接说明”这一方式与筛选策略。",
    "把指责者动因归结为“性焦虑”属作者推断，本文未提供依据。",
    "P010 所述“很多人”的后果描述为概括性断言，无数据来源，属待外部核查。",
    "P016–P017 引用的“金风玉露一相逢，胜却人间无数”未标明出处与作者，故按 quoted_or_cited + attribution=unknown 记录。",
    "P002“目前中国能过关的人客观上的确比例很小”中的“客观”缺乏可核验的统计支持。",
    "提问字段属提问者立场（问“是我过分了吗”），作者予以否认，二者归属已区分。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "你这个其实没有任何原则问题，甚至是优秀的策略。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "“坏处”则是目前中国能过关的人客观上的确比例很小", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "需要做的修正不是要改变你的过滤条件，而是要扩大筛选面", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P005", "quote": "是因为ta们要消解自己的性焦虑", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P006", "quote": "不是在为你考虑，而是在为自己考虑", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "是ta们自己悄悄偷换出来的一个“恨嫁女”", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "你其实对“找个人结婚”这事没有什么特别强迫性的需求", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P008", "quote": "其实这个前提是ta们自己悄悄给你加上的", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P009", "quote": "你这样做不但没有什么错误，甚至是非常正确的做法", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P009", "quote": "是风险极大、极其不明智的显著错误", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P010", "quote": "很多人是四五年、上十年后拖着一个被生父实质抛弃的孩子", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P010", "quote": "没有一个会出来分担你一丁点负担", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P011", "quote": "要确认清楚自己是因为懒惰和软弱而这么选择，还是因为主动计划和勇敢承担而这样做", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P012", "quote": "如果是后者，你就不用害怕。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P013", "quote": "本质上你的条款原则还是live and let live", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P014", "quote": "这是一种人格健全的人才能看得懂的性感。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P015", "quote": "也会自然而然就是镇定而温柔的", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P015", "quote": "而对方对你这些话的反应也足以让你发自内心的惊喜", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P016", "quote": "那便是金风玉露一相逢，", "relation": "context"},
    {"key": "E20", "paragraph_id": "P017", "quote": "胜却人间无数。", "relation": "context"},
    {"key": "E21", "paragraph_id": "P004", "quote": "大浪淘沙，沙里淘金。", "relation": "context"},
    {"key": "E22", "paragraph_id": "P005", "quote": "生怕“引起效仿”，进一步恶化ta们自己的性困境", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["婚恋与择偶", "人际交往策略", "社会心理", "性别议题"],
   "issue_candidates": ["相亲中直接说明原则是否过分", "择偶标准的过滤与筛选面", "催婚与指责者的动机", "宁缺毋滥的风险与代价"],
   "text_function_candidates": ["答疑（回应知乎提问）", "劝慰", "论辩", "反驳（反驳指责者）"],
   "object_candidates": ["提问者（相亲当事人）", "相亲对象", "指责提问者的“无数人”", "“恨嫁女”（他人偷换的形象）"],
   "working_keywords": ["过滤条件", "筛选面", "宁缺毋滥", "性焦虑", "恨嫁女", "live and let live", "大浪淘沙", "金风玉露一相逢"]
  },
  "notes": "无图片节点。正文 P001–P017 已完整读取（共 974 字），text 与 lexical 无 divergence。文中 ta 为作者使用的不分性别第三人称写法，引用时保留原样。P013 的 live and let live 为英文字符串，按原文保留。P016–P017 引语未标出处，按 quoted_or_cited + attribution=unknown 记录，未归为作者论断。提问字段属提问者立场，作者予以否认，归属已区分。"
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
