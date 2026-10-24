# -*- coding: utf-8 -*-
"""批次 r001-b0016 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0016.sessions.py            # 写 out/r001-b0016.out.jsonl
  python3 records/r001-b0016.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0016"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0016.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "b34ad449": {
  "analysis": {
   "question_context": "提问者（Q001）问“永生是否是一种酷刑？”，讨论预设是“永生＝不死＝漫长的存在”，并追问这种存在是否构成酷刑。作者先纠正概念：永生不等于不死，永生可以技术地实现，但人仍会死于意外、被杀或自杀；随后给出肯定性回答——永生会带来两重无限恐惧（失去永生、失去永福），并随寿命延长放大选择焦虑与不幸打击，最终只能靠不可动摇的乐观来源（信仰）支撑，否则永生即地狱。提问者的“永生是否酷刑”被改写为“永生如何成为酷刑”的机制论证。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "纠正概念：永生不等于不死；永生可通过类似忒修斯之船的替换实现，技术虽复杂但逻辑通；被杀、车祸、滑雪冻死、冲浪淹死等仍会致死，脑袋中枪也无救；生理性永生大概只是寿命延长一两倍，最终人人死于意外或自杀。", "role": "definition"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005", "P006", "P007", "P008"], "summary": "第一重恐惧：得到永生首先得到对失去永生的无限恐惧；盔甲、堡垒、二十四层轨道炮都防不住超新星辐射、太阳红巨星化、流浪黑洞；未来英年早逝者失去的是100-200年甚至无限年寿命预期；并以百年前后“是否愿意押上永生抗争不公”与同志数量作对比，给出断语“永生指向坚不可摧的奴隶制”。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P009", "P010", "P011", "P012", "P013"], "summary": "第二重恐惧：对失去永福的无限恐惧；以父母对幼儿教育态度的百年变化为例（从天生天养到学区房、双语幼儿园、国际学校），说明幼儿教育不良的代价随人均寿命从30岁到75岁而成倍放大。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P014", "P015", "P016", "P017", "P018", "P019", "P020"], "summary": "以复利模型说明经验净有效性累进：同样技能20岁与30岁掌握的收益差，在40岁、60岁、200岁退休时分别为1229.28、3261.6、4918503；提醒基数只有100元、时间单位是月收入。", "role": "example"},
    {"unit_id": "U005", "paragraph_refs": ["P021", "P022", "P023", "P024"], "summary": "推论：医学永生将使智力与出身的微小优势被绝对放大（“高在云霄”）；任何长远影响未来的重大选择都会引发焦虑，寿命越长焦虑越大，入错行耽误三四年无法一笑置之；遭遇打击时潜在损失更难承受，且“多活二十年就能东山再起”是错误推算，因为竞争对手同样没有少活。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P025", "P026", "P027"], "summary": "诅咒已经收紧：百年前飞机撞楼不会引发如此广泛的恐惧；地球越安宁、人类越长寿，诅咒越呈几何级数上升，恐惧将超出安全手段与一般治疗手段；核能源、空间开发、基因编辑本身就是可怕威胁，终有一天一个错误将释放兆亿的烈焰；没有乐观预期就无法在漫长人生中保持乐观。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P028", "P029", "P030"], "summary": "出路与断语：除非能超理性且不可动摇地拥有某种乐观来源——信仰；无论有神无神都必须有不为负面事实动摇的乐观源泉，人类也必须有为避免沦为奴隶制世界；否则，永生即地狱。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "永生并不意味着不死：永生是永生，不死是不死，脑袋中枪一样没救。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "永生有一天可以做到，譬如改造成某种忒修斯之船、哪里坏了换哪里；技术上非常复杂和困难，但至少逻辑是通的。", "evidence": ["E3"]},
    {"claim_id": "C003", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "生理性的永生大概只意味着人的寿命延长个一两倍，然后人人死于意外或者自杀。", "evidence": ["E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者以连续反问指出：盔甲、堡垒、二十四层轨道炮防不住超新星爆炸的辐射冲击、太阳的红巨星化与流浪的黑洞。", "evidence": ["E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "得到永生首先得到的是对于失去永生的无限恐惧：现在英年早逝失去的是三四十年的寿命预期，未来英年早逝失去的是100-200年甚至无限年的寿命预期。", "evidence": ["E6", "E7"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者以反问提出：当预期寿命是永生而世界同样不义时，人是否愿意押上十拿九稳的【永生】去抗争不公；即使愿意，也很难有多少同志。", "evidence": ["E8"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "永生指向坚不可摧的奴隶制。", "evidence": ["E9"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "第二，永生带来的是对失去永福的无限的恐惧。", "evidence": ["E10"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "幼儿时代的教育不良的代价扩大了好几倍：人均寿命从30岁延长到75岁，人15岁后的寿命就从15年延长到55年，延长了两三倍。", "evidence": ["E11", "E12"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人的经验的净有效性是按复利累进的；按同一技能20岁与30岁掌握、月收入100元且每年提升5%计算，40岁退休时月收入差为1229.28，60岁退休时为3261.6，200岁时为4918503。", "evidence": ["E13", "E14", "E15"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "如果医学的永生得以实现，意味着一个人智力稍微优胜一点、出身稍微幸运一点，将绝对的凌驾于稍微不那么聪明、不那么幸运的同类之上，不是高一层楼，而是高在云霄。", "evidence": ["E16"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "任何会长远影响到未来的重大选择都会造成当事人的焦虑；寿命越长焦虑越大，永生时入错了行、耽误三四年将无法一笑置之，选择焦虑会呈几何级数上升。", "evidence": ["E17"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "遭遇不幸的打击时，人均寿命长意味着潜在损失更加难以承受；“如果我可以多活二十年就不会这么在意”是错误的推算，因为没有遭遇这个打击的竞争对手们也没有少活这二十年。", "evidence": ["E18"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "随着人类平均寿命的延长，永生诅咒已经开始收紧：地球越安宁、人类越长寿，诅咒越呈几何级数上升；安全手段本身同时是可怕的威胁（核能源、空间开发、基因编辑），终有一天一个错误将能释放兆亿的烈焰。", "evidence": ["E19", "E20"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者以反问追问“一般治疗手段”是心理治疗、心灵培训班还是毒品。", "evidence": ["E21"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "没有任何东西能保证乐观预期；没有乐观预期，人将无法在漫长的人生中保持乐观，这人生漫长到即使极尽坚持也会有好几十年要深入黑暗。", "evidence": ["E22"]},
    {"claim_id": "C017", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "除非人能够超理性地、不可动摇地拥有某种乐观来源——信仰。", "evidence": ["E23"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "无论有神还是无神，人必须要有一种任何负面事实都不可动摇的乐观源泉；不但个人必须有，人类也必须要有，以避免沦为奴隶制世界。", "evidence": ["E24"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "否则，永生即地狱。", "evidence": ["E25"]}
   ],
   "argument_steps": [
    "指出讨论缺项：谁说永生意味着不死（P001）。",
    "承认永生可实现：忒修斯之船式替换，技术困难但逻辑通（P002）。",
    "区分永生与不死：意外、被杀、自杀仍可致死；生理性永生约等于寿命延长一两倍（P003）。",
    "提出问题：盔甲、堡垒、轨道炮能否防住超新星、红巨星、黑洞（P004）。",
    "给出第一重恐惧：对失去永生的无限恐惧，且失去的量随寿命预期放大（P005、P006）。",
    "以百年前后抗争不公的赌注与同志数量作对比（P007）。",
    "断语：永生指向坚不可摧的奴隶制（P008）。",
    "给出第二重恐惧：对失去永福的无限恐惧（P009）。",
    "以父母教育投入的百年变化说明早期教育代价放大（P010-P013）。",
    "以复利模型计算经验收益差，说明寿命延长如何放大先发优势（P014-P020）。",
    "推论永生下的选择焦虑、不幸打击与“多活二十年”的算法错误（P021-P024）。",
    "说明诅咒已随寿命延长而收紧，安全手段同时是威胁（P025）。",
    "排除一般治疗手段（P026）。",
    "指出没有乐观预期便无法支撑漫长人生（P027）。",
    "给出唯一出路：超理性、不可动摇的乐观来源——信仰（P028、P029）。",
    "结论：否则永生即地狱（P030）。"
   ],
   "concept_usage": [
    {"term": "永生", "meaning": "本文中不等于不死，而指寿命可被大幅延长或可替换修复；作者称其技术可实现，但仍会死于意外、被杀或自杀。", "evidence": "P003", "ambiguity": "与“不死”“长生”的界线由作者自设，未给技术定义。"},
    {"term": "不死", "meaning": "作者用以指无论如何都不会死的状态，并明确否定永生等于不死。", "evidence": "P003", "ambiguity": "无。"},
    {"term": "忒修斯之船", "meaning": "作者用作永生技术路径的类比：哪里坏了换哪里。", "evidence": "P002", "ambiguity": "类比未涉及同一性问题。"},
    {"term": "永福", "meaning": "与永生对应的、可被失去的永久福乐状态；对失去它的恐惧是第二重无限恐惧。", "evidence": "P009", "ambiguity": "未界定其内容与来源。"},
    {"term": "乐观来源／信仰", "meaning": "作者指任何负面事实都不可动摇的乐观源泉，并称之为信仰，无论有神无神。", "evidence": "P029", "ambiguity": "“超理性的”与“信仰”的关系未展开。"}
   ],
   "examples_and_targets": [
    "忒修斯之船：作者的技术类比（P002）。",
    "超新星爆炸辐射、太阳红巨星化、流浪黑洞：作者用以说明无法防御的风险（P004）。",
    "“不自由，毋宁死”“引刀成一快，不负少年头”“去留肝胆两昆仑”：作者引用的历史口号，用以说明百年前抗争的赌注（P007），属引语材料。",
    "学区房、双语幼儿园、国际学校：作者用作当代父母教育竞争的例证（P011）。",
    "月收入100元、年增5%的复利计算（40/60/200岁）：作者自设的示范性数据（P014-P019）。",
    "飞机撞毁两栋楼房：作者用以说明恐惧随寿命延长而深化（P025）。",
    "核能源、空间开发、基因编辑：作者列举的“安全手段同时是威胁”（P025）。",
    "心理治疗、心灵培训班、毒品：作者对“一般治疗手段”的反问对象（P026）。"
   ],
   "conditions": [
    "P002：永生技术“虽然技术上非常复杂和困难，但是至少逻辑是通的”为可行性限定。",
    "P003：“没被人砍死、没被车撞死……的话”为不死成立的条件；括号内以“大概”限定生理性永生。",
    "P004：三重反问均为条件性设问，未断言这些灾难必然发生。",
    "P007：“即使你愿意”为让步条件。",
    "P021：“如果医学的永生得以实现”为推论前提。",
    "P025：“终有一天”为时间性预测。",
    "P028：“除非”引出唯一例外条件。"
   ],
   "rhetoric_and_tone": "说理与危言并用：以“你”直呼读者施压，多处连续反问（P001、P004、P007、P026）；用短句断语作标题式判断（P008“永生指向坚不可摧的奴隶制。”、P030“否则，永生即地狱。”）；插入复利算式与括号补充，并使用“兆亿的烈焰”“高在云霄”等夸张表述；语气冷峻、警告性强。",
   "unresolved_questions": [
    "引语“不自由，毋宁死”“引刀成一快，不负少年头”“去留肝胆两昆仑”未注明出处与说话者（属历史口号），引用归属需外部核查。",
    "“忒修斯之船”仅作类比，作者未讨论替换后的同一性问题。",
    "复利模型（月收入100元、年增5%、40/60/200岁退休）为示例设定，未说明数据来源；P019“如果是200岁呢？4918503。”未给算式，无法复核。",
    "“二十四层轨道炮”“兆亿的烈焰”属修辞性表述，具体所指未说明。",
    "brief 与正文前三段基本重合但被截断（止于“没有冲浪淹死……的话，你不会死。”），不能据以补全。",
    "作者未回答“永生是否是一种酷刑”的伦理讨论中“酷刑”的界定，只给出机制性论证。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "你们的讨论中缺了一件事——谁说永生意味着不死？", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P003", "quote": "你再“永生”，有人冲脑袋来一枪也没救了。所以，永生是永生，不死是不死。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P002", "quote": "永生有一天是可以做到的——譬如改造成某种忒修斯之船，哪里坏了换哪里。虽然技术上非常复杂和困难，但是至少逻辑是通的。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P003", "quote": "其实生理性的永生大概只意味着人的寿命延长个一两倍，然后人人死于意外或者自杀。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P004", "quote": "穿一层盔甲、建一重堡垒、给地球装上二十四层轨道炮，你能防住超新星爆炸的辐射冲击吗？", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P005", "quote": "你如果得到永生，首先得到的只是对于失去永生的无限恐惧。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P006", "quote": "未来你三四十岁英年早逝，失去的是100-200年甚至无限年的寿命预期。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P007", "quote": "你愿意押上你十拿九稳的【永生】去抗争不公吗？即使你愿意，你觉得你能有多少同志？", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P008", "quote": "永生指向坚不可摧的奴隶制。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P009", "quote": "第二，永生带来的是对失去永福的无限的恐惧。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P012", "quote": "为什么？因为幼儿时代的教育不良的代价扩大了好几倍。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P013", "quote": "人均寿命从30岁延长到75岁，人15岁后的寿命就从15年延长到了55年，延长了两三倍。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P014", "quote": "人的经验的净有效性是按复利累进的。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P016", "quote": "100*12*( 1.05^20 - 1.05^10 ) = 1229.28", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P018", "quote": "100*12*( 1.05^40 - 1.05^30 ) = 3261.6", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P021", "quote": "将绝对的凌驾于ta稍微不那么聪明、稍微不那么幸运的同类之上，不是高一层楼，而是高在云霄。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P023", "quote": "要是永生呢？那时候入错了行，耽误了三四年，你还能一笑置之吗？", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P024", "quote": "因为没有遭遇这个打击的，你的竞争对手们也没有少活这二十年啊。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P025", "quote": "地球越“安宁”、人类越长寿，这诅咒越呈几何级数上升。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P025", "quote": "终有一天，一个错误将能释放兆亿的烈焰。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P026", "quote": "而“一般治疗手段”是心理治疗还是心灵培训班？还是毒品？", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P027", "quote": "没有任何东西能向你保证乐观预期。没有乐观预期，你将无法在漫长的人生中保持乐观。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P028", "quote": "除非，你能超理性的、而且是不可动摇的拥有某种乐观来源——信仰。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P029", "quote": "无论有神还是无神，你必须要有一种任何负面事实都不可动摇的乐观源泉，你必须有。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P030", "quote": "否则，永生即地狱。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["生命伦理", "社会心理", "未来学"],
   "issue_candidates": ["永生是否酷刑", "永生与不死的区分", "寿命延长与选择焦虑", "信仰与乐观来源"],
   "text_function_candidates": ["答疑", "论辩", "推演"],
   "object_candidates": ["提问者", "未来人类", "父母", "信仰者"],
   "working_keywords": ["永生", "不死", "忒修斯之船", "永福", "奴隶制", "复利", "乐观预期", "信仰"]
  },
  "notes": "全文 30 段已读完，无图片节点，status=read。要点：①作者明确区分永生与不死，属定义性纠正，非提问者立场；②文中的历史口号与“飞机撞毁两栋楼房”等均为作者引用的例证材料；③复利算式为作者自设示范数据，P019 未给算式；④brief 被截断，已以 text 为准。"
 },
 "c936feb4": {
  "analysis": {
   "question_context": "提问者（Q001）问“如何选择一本好书？”，寻求选书的可操作标准。作者给出四条可观察的外部代理标准（再版年限、多语种译本、多个中文译本、全球化院校稳定沿用的教科书），并为每条说明理由；未给“好书”的定义，也未给具体书名。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "标准一：初版发行时间在十年以上、仍在不断再版的书；理由是若无价值很难再版超过十年，出版社在用自己的投资替读者做筛选。", "role": "action_advice"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005"], "summary": "标准二：同时拥有多个语种译本的书；理由是翻译是极大的精力投入，多个语种不同国家不约而同认为有市场，意味着该书要义拥有某种跨文化的普适性。", "role": "action_advice"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007"], "summary": "标准三：拥有不止一个中文译本的书；一般是重要的基础性著作，国内不同观点与风格者希望有自己派别的翻译版本；若为文学著作，则因该文学意象对本文化异常新鲜而有价值，值得不断寻求更好的表达。", "role": "action_advice"},
    {"unit_id": "U004", "paragraph_refs": ["P008", "P009", "P010"], "summary": "标准四：全球化院校的历史悠久、版本稳定的教科书；作者界定“全球化院校”为具有鲜明多样化学生结构、明确种族/信仰/国籍多样化招生政策、毕业生面向全球人力资源市场的院校，并称这类院校选教科书高度审慎，稳定沿用多年的教科书往往具有深远影响与现实意义。", "role": "action_advice"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "初版发行时间在十年以上、仍然在不断再版的书值得重点考虑。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "如果该书没有价值，将很难不断再版超过十年；出版社是在用自己的投资帮读者做筛选。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "同时拥有多个语种译本的书值得重点考虑：翻译是极大的精力投入，多个语种不同的国家不约而同认为翻译这本书会有市场，意味着这本书的要义拥有某种跨文化的普适性。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "拥有不止一个中文译本的书值得重点考虑：这一般是重要的基础性著作，以至于国内不同观点和风格者会希望有自己派别的翻译版本；如果为文学著作，则必定是因为这个文学意象对本文化而言异常新鲜而又有价值。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "全球化院校的历史悠久、版本稳定的教科书值得重点考虑。", "evidence": ["E5"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者对“全球化院校”的界定是：具有鲜明的多样化学生结构，有明确的种族/信仰/国籍多样化招生政策，其毕业生也是面向全球人力资源市场。", "evidence": ["E6"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "这样的院校在选择教科书时会有高度审慎的态度；经他们选择而稳定沿用多年的教科书往往具有深远的影响和值得重视的现实意义。", "evidence": ["E7"]}
   ],
   "argument_steps": [
    "给出总纲：符合以下几个标准的书值得重点考虑（P001）。",
    "标准一及其理由：再版十年以上反映价值，出版社投资即筛选（P002、P003）。",
    "标准二及其理由：多语种译本反映跨文化普适性（P004、P005）。",
    "标准三及其理由：多个中文译本反映基础性地位或文学意象的新鲜价值（P006、P007）。",
    "标准四及其理由：全球化院校稳定沿用的教科书具有审慎选择与长期影响（P008-P010）。"
   ],
   "concept_usage": [
    {"term": "好书", "meaning": "本文未直接定义，只以四条外部特征（再版年限、多语种译本、多个中文译本、全球化院校教科书）作为可考虑的判据。", "evidence": "P001", "ambiguity": "“好书”本身未界定，四条标准是代理指标。"},
    {"term": "全球化院校", "meaning": "作者自设标准：学生结构鲜明多样化、有明确的种族/信仰/国籍多样化招生政策、毕业生面向全球人力资源市场。", "evidence": "P009", "ambiguity": "该界定为作者自定，未给具体院校名单。"},
    {"term": "普适性", "meaning": "作者用以指一本书的要义能跨越文化被多个语种市场接受。", "evidence": "P005", "ambiguity": "未说明如何判断普适性的程度。"}
   ],
   "examples_and_targets": [
    "出版社的再版投资：作者用作筛选机制的例证（P003）。",
    "多个语种译本与不同国家的翻译市场：作者用作跨文化普适性的证据（P005）。",
    "不同派别的翻译版本、文学意象：作者用作多个中文译本的成因（P007）。",
    "全球化院校的招生政策与毕业生去向：作者用作教科书审慎选择的依据（P009、P010）。"
   ],
   "conditions": [
    "P003：“如果该书没有价值”为条件句。",
    "P007：“如果为文学著作”为分支条件。",
    "P006、P008：标准均以“值得你重点考虑”表述，属建议而非绝对判据。"
   ],
   "rhetoric_and_tone": "条目式建议文体，四条标准各配简短理由，语气平实、务实，无论辩与修辞夸张；以“你”称呼读者；标准顺序从市场筛选到学术机构筛选，逐步提高门槛。",
   "unresolved_questions": [
    "brief 在“多个语种不同的国家不约而同认为翻译这本书会有市场，”处截断，不能据以补全。",
    "四条标准均为外部代理指标，本文未说明各标准的权重、冲突时如何取舍，以及是否穷尽。",
    "本文未给出任何具体书名作为示例，也未说明“好书”的定义。",
    "“全球化院校”为作者自设界定，标准中的“多样化”程度无可操作判据。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P002", "quote": "1）初版发行时间在十年以上，仍然在不断再版的书。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P003", "quote": "如果该书没有价值，将很难不断再版超过十年。出版社在用自己的投资帮你做筛选。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P005", "quote": "多个语种不同的国家不约而同认为翻译这本书会有市场，意味着这本书的要义拥有某种跨文化的普适性。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P007", "quote": "这一般是重要的基础性著作，以至于国内不同观点和风格者会希望有自己派别的翻译版本。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P008", "quote": "4）全球化院校的历史悠久、版本稳定的教科书。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P009", "quote": "“全球化院校”的标准，是具有鲜明的多样化学生结构，有明确的种族/信仰/国籍多样化的招生政策，其毕业生也是面向全球人力资源市场。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P010", "quote": "经他们选择而稳定沿用多年的教科书往往具有深远的影响和值得重视的现实意义。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["阅读方法", "出版与知识传播", "教育"],
   "issue_candidates": ["如何选择好书", "选书判据", "译本与再版"],
   "text_function_candidates": ["答疑", "操作建议"],
   "object_candidates": ["出版社", "全球化院校", "翻译者", "读者"],
   "working_keywords": ["再版", "多个语种译本", "中文译本", "全球化院校", "教科书"]
  },
  "notes": "全文 10 段已读完，无图片节点，status=read。四条标准均为外部代理指标，未给“好书”定义与具体书名；brief 在“认为翻译这本书会有市场，”处截断，已以 text 为准。"
 },
 "64f30b14": {
  "analysis": {
   "question_context": "提问者（Q001）问“你为什么不喜欢孔子？”，把作者当作不喜欢孔子的人并要求说明理由。作者先限定讨论对象：所谈是作为文化符号的“孔子”（事迹真假参半、围绕某种理念被塑造和堆积），而非“真实的孔子”（后者没人可知）；随后以杀少正卯、删改诗经、篡改历史三件事列举不喜欢该文化符号的理由，最后让步：孔子本人不该负全责，历代的“书生”才是首恶元凶，问题在于遗憾之后是否会改。提问者的“你为什么不喜欢”属提问者的提问框架，作者的回答以文化符号为对象。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "限定讨论对象：孔子已不是一个人而是一个形象，类似阿凡提、拉斯普丁，事迹真假参半、围绕某种理念被塑造和堆积；作者谈的是作为文化符号的“孔子”，而不是没人可知的“真实的孔子”；作者不喜欢这个文化符号。", "role": "definition"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005", "P006", "P007", "P008"], "summary": "第一件事：杀少正卯。罪名是“心達而險、行辟而堅、言偽而辯、記醜而博、順非而澤”，是“惑众”“乱政”；作者解读为政见不同、博闻强识辩才无碍者被理屈词穷者视为特别危险，于是不但敢杀人还理直气壮自居正义；并称不与孔子一条心就要闭嘴，越优秀越该死；结论是理屈词穷起杀心不奇怪，到以为理所当然的正义罕见，这个想象中的孔子难脱干系。", "role": "example"},
    {"unit_id": "U003", "paragraph_refs": ["P009", "P010", "P011", "P012"], "summary": "第二件事：删改诗经。作者痛恨删改原始古文献的人，不管出于什么自以为正义的理由；若批判就应批判，让后人看到批判对象与是否合理，这才是正常学术规范；一扫光的做法成为垂范，毁灭了中国几千年的文明积累，此后每代徒子徒孙焚书都要为此负责，有效的积累传承从未超过三百年；这个想象中的孔子难辞其咎。", "role": "example"},
    {"unit_id": "U004", "paragraph_refs": ["P013", "P014", "P015"], "summary": "第三件事：篡改历史、借历史搞微言大义，堵塞了历史学科对文明的救赎之路；代代统治者学会这一套，名为“史实记录”的东西成了谎言汇编，历史书都写成了政治书；这个想象中的孔子难辞其咎。", "role": "example"},
    {"unit_id": "U005", "paragraph_refs": ["P016", "P017", "P018", "P019"], "summary": "让步与归责：作者并不认为“孔子”该付全责——孔子也是有缺陷有局限的人，所选择的想象的民族无非是有缺陷的人的总和；一代代闭眼奉圣、为高官厚禄蒙眼昧心的“书生”们才是首恶元凶，但他们也不过是受软弱驱使的人类；民族命定要如此走过，关键在于遗憾之后我们是不是会改。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "孔子已不是一个真实的人，而是一个真假参半、围绕某种理念被塑造和堆积的文化符号形象；作者谈的是这个作为文化符号的“孔子”，而不是没人可知的“真实的孔子”。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者不喜欢这个文化符号。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "第一件事是杀少正卯，罪名是“心達而險、行辟而堅、言偽而辯、記醜而博、順非而澤”，是“惑众”、是“乱政”；作者解读为一个人与他政见不同、政治理想矛盾，却博闻强识、辩才无碍、有强大说服力，于是被他理屈词穷地视为特别危险，不但敢于杀人，而且敢于理直气壮地自居正义。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "在作者所描述的这套逻辑下：你最好跟他一条心，或者要懂得闭嘴，否则你越优秀，你越是该死。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "理屈词穷起杀心不奇怪，到以为理所当然的正义，罕见；这件事，这个想象中的孔子，难脱干系。", "evidence": ["E5", "E6"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者痛恨删改原始古文献的人，不管他出于什么自以为正义的理由；要批判就应批判，让后人看到批判对象并判断是否合理，这才是正常的学术规范，而生怕后人不能认同就一扫光则不是。", "evidence": ["E7"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "删改的垂范毁灭了中国几千年的文明积累：此后每一代徒子徒孙焚书都要为之负责，每一代前朝的思想成就都被新朝视为需要“无邪化”，中华文明被一把又一把火清零；文明虽传承三千多年，事实上有效的积累传承从未超过三百年，短的甚至不过两百年、一百年。", "evidence": ["E8"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "第三件事是篡改历史、借历史搞微言大义，堵塞了历史学科对文明的救赎之路；代代统治者都学会了这一套，名为“史实记录”的东西成了精心编纂、遮遮掩掩、无所不用其极的谎言汇编，历史书全都写成了政治书。", "evidence": ["E9"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者并不认为“孔子”该付这个全责：谁都是有缺陷、有局限的人，孔子也是个人，他所选择的想象的民族也无非是有缺陷的人的总和，有很大问题也只不过是平常事。", "evidence": ["E10"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "一代代闭着眼睛奉他为圣、为了高官厚禄而蒙眼昧心的“书生”们才是首恶元凶，但他们也不过是受软弱驱使的人类。", "evidence": ["E11"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "民族命定要如此走过；问题不在于走过的过程很遗憾，而在于遗憾之后我们是不是会改。", "evidence": ["E12"]}
   ],
   "argument_steps": [
    "提出讨论对象问题：当我们谈论孔子时，谈的是什么（P001）。",
    "限定对象：孔子已是文化符号而非真人；“真实的孔子”没人可知（P002）。",
    "表明立场：不喜欢这个文化符号（P003）。",
    "第一件事：杀少正卯及其罪名与作者解读（P004、P005）。",
    "引申：不与他一条心就要闭嘴，越优秀越该死（P006）。",
    "评断：起杀心不奇怪，自居正义罕见；想象中的孔子难脱干系（P007、P008）。",
    "第二件事：删改诗经，作者反对删改古文献并给出学术规范理由（P009、P010）。",
    "后果指控：垂范毁灭文明积累，历代焚书归责，有效传承从未超过三百年（P011）。",
    "归责：想象中的孔子难辞其咎（P012）。",
    "第三件事：篡改历史搞微言大义，历史写成政治书（P013、P014）。",
    "归责：想象中的孔子难辞其咎（P015）。",
    "让步：孔子不该负全责，因为他也是有缺陷的人（P016）。",
    "转移归责：历代蒙眼昧心的“书生”才是首恶元凶，但也是受软弱驱使的人类（P017）。",
    "收束：民族命定如此走过，关键在于之后是否会改（P018、P019）。"
   ],
   "concept_usage": [
    {"term": "孔子（文化符号）", "meaning": "本文的讨论对象，指真假参半、围绕某种理念被塑造和堆积起来的形象，而非历史上的真人。", "evidence": "P002", "ambiguity": "作者明确区分符号与真人，但“某种理念”具体所指未说明。"},
    {"term": "无邪化", "meaning": "作者用以指新朝把前朝思想成就视为需要清除的对象并加以焚毁的做法，源自“思无邪”。", "evidence": "P011", "ambiguity": "带引号的自创说法。"},
    {"term": "微言大义", "meaning": "作者用以指借历史书写寄托政治褒贬的做法，并称其堵塞历史学科对文明的救赎之路。", "evidence": "P013", "ambiguity": "未举例说明具体史书。"},
    {"term": "书生", "meaning": "作者加引号使用，指一代代为高官厚禄而蒙眼昧心、奉孔子为圣的读书人。", "evidence": "P017", "ambiguity": "群体指称，未指名具体人物。"}
   ],
   "examples_and_targets": [
    "少正卯之诛及罪名“心達而險、行辟而堅、言偽而辯、記醜而博、順非而澤”：作者的核心指控材料（P004、P005）。",
    "删改诗经与“思无邪”：作者的指控材料（P009、P010）。",
    "历代焚书与新朝对前朝思想的“无邪化”：作者的历史叙述（P011）。",
    "阿凡提、拉斯普丁：作者用作文化符号形象的类比（P002）。",
    "“史实记录”与政治书：作者的指控材料（P014）。",
    "历代“书生”：作者的归责对象，同时也被作者称为受软弱驱使的人类（P017）。"
   ],
   "conditions": [
    "P002：讨论范围限定为文化符号的“孔子”，而非“真实的孔子”。",
    "P010：“不管他出于什么自以为正义的理由”为让步式全称限定。",
    "P016-P017：归责被两次让步削弱（孔子不该负全责；“书生”也是受软弱驱使的人类）。",
    "P009：“第二，删改诗经。”与 P013“第三，篡改历史”构成分条结构，第一条为 P004 的杀少正卯。"
   ],
   "rhetoric_and_tone": "驳论与控诉式列举：以“第一件事”“第二”“第三”分条历数，两次以“这个想象中的孔子，难辞其咎”形成排比；直接指称“你”并下断语（“你越优秀，你越是该死”）；引用罪名原文（繁体）与“思无邪”；末段以让步与“民族命定要如此走过”的宿命式表述收束，语气峻急但结尾留出“是否会改”的追问。",
   "unresolved_questions": [
    "少正卯之诛的史实争议与所引罪名的出处未注明，需外部核查。",
    "“事实上有效的积累传承从未超过三百年”无数据来源，需外部核查。",
    "“民族命定要如此走过”是修辞性表述还是作者的因果判断，正文未明说。",
    "brief 在“而这个文化符号，我是不”处截断，不能据以补全。",
    "作者未说明“某种理念”具体指什么，也未讨论《论语》等其他材料。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P002", "quote": "我现在谈的，是这个作为文化符号的“孔子”，而不是“真实的孔子”——后者没人可知。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P003", "quote": "而这个文化符号，我是不喜欢的。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P005", "quote": "一个人与他政见不同、政治理想矛盾，而博闻强识、辩才无碍，有强大的说服力，他理屈词穷，于是觉得人家特别危险，不但敢于杀人，而且敢于理直气壮的自居正义。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P006", "quote": "你最好跟他一条心，或者要懂得闭嘴，否则你越优秀，你越是该死。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P007", "quote": "理屈词穷起杀心，不奇怪；到以为理所当然的正义，罕见。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P008", "quote": "这件事，这个想象中的孔子，难脱干系。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P010", "quote": "我痛恨删改原始古文献的人，不管他出于什么自以为正义的理由。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P011", "quote": "事实上有效的积累传承从未超过三百年。短的甚至不过两百年、一百年。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P014", "quote": "名为“史实记录”的东西，成了精心编纂的、遮遮掩掩的、无所不用其极的谎言汇编。历史书全都写成了政治书。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P016", "quote": "不过，我却并不认为“孔子”该付这个全责——谁不是有缺陷、有局限的人？", "relation": "qualifies"},
    {"key": "E11", "paragraph_id": "P017", "quote": "一代代闭着眼睛奉他为圣，为了高官厚禄而蒙眼昧心的“书生”们才是首恶元凶，但他们也不过是受软弱驱使的人类。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P019", "quote": "问题不在于走过的过程很遗憾，而在于遗憾之后我们是不是会改。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["中国思想史", "文化批评", "历史学"],
   "issue_candidates": ["对孔子的评价", "文化符号与历史人物之别", "删改文献与焚书", "历史书写与政治"],
   "text_function_candidates": ["答疑", "批评", "论辩"],
   "object_candidates": ["孔子", "少正卯", "诗经", "历代“书生”", "历代统治者"],
   "working_keywords": ["文化符号", "杀少正卯", "删改诗经", "思无邪", "无邪化", "微言大义", "史实记录"]
  },
  "notes": "全文 19 段已读完，无图片节点，status=read。要点：①作者把讨论对象限定为文化符号的“孔子”，非历史真人；②“书生”一段为作者的归责判断，同时也被作者以“受软弱驱使”作让步；③少正卯罪名原文为繁体引文；④brief 被截断；史实与数据均登记为待外部核查。"
 },
 "96522ec0": {
  "analysis": {
   "question_context": "提问者（Q001）问“你最苦的时候是什么时候，是怎么熬过来的？”，要求叙述个人最苦的经历与熬过的方式。作者没有叙述具体时间与经历，而是重新界定“苦”：凡是“只需要熬就能熬过去”的苦都只是后味回甘的乌龙茶，真正的苦是失去希望本身；并称处于这种苦的人没有力气上知乎答题。回答把提问者的自述请求转为对“真正的苦”的定义与描述。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "重新界定“能熬过去的苦”：只是需要熬就能熬过去的苦，其实只是后味回甘的乌龙茶；之所以能熬，前提是还有希望，而且希望很强。", "role": "definition"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004"], "summary": "真正的苦不是困境本身难熬（癌症、艾滋病、断手断脚、坐牢判刑、欠巨债时间久了也会适应），而是没了希望本身——不知道还该指望什么，即使有所指望也完全没有它能实现的信心。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P005", "P006", "P007", "P008"], "summary": "描述这种苦的形态：每一分煎熬都是毫无意义、毫无积淀的痛苦的延长；只是有某些原因让自己死不成、死不得、不敢死；当事人如同被活埋，进了坟墓但未气绝，只恨自己牵绊太多、缺少勇气不能早死；这样的人哪里有力气来知乎答题换赞——这才是最苦。", "role": "conclusion"},
    {"unit_id": "U004", "paragraph_refs": ["P009"], "summary": "正文末尾出现平台话题标签“悲观的人如何能变得乐观？”，lexical 未覆盖该片段，属平台字段混入正文。", "role": "context"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只是需要熬就能熬过去的苦，其实后味回甘的乌龙茶而已。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人之所以能熬，前提是他还有希望，而且希望还很强。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "真正的苦不是困境本身难熬：困境本身哪怕是癌症、艾滋病、断手断脚、坐牢判刑、欠巨债，时间久了也会适应。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "真正的苦是没了希望本身——不知道还该指望什么、也不知道还能指望什么，即使有所指望，也完全没有它能实现的信心。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "在这种苦中，每一分煎熬都是毫无意义、毫无积淀的痛苦的延长，只是有某些原因让自己死不成、死不得、不敢死。", "evidence": ["E5"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "当事人如同被活埋——进了坟墓但未气绝，只恨自己太多牵绊、缺少勇气，不能早死。", "evidence": ["E6"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者以反问指出：处于这种苦的人哪里有力气来知乎答题换赞。", "evidence": ["E7"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这才是最苦。", "evidence": ["E8"]}
   ],
   "argument_steps": [
    "以比喻重定义“能熬的苦”：后味回甘的乌龙茶（P001）。",
    "给出前提：能熬意味着还有很强的希望（P002）。",
    "排除困境本身：癌症、艾滋病、断手断脚、坐牢判刑、欠巨债时间久了也会适应（P003）。",
    "给出真正的苦：失去希望本身与对希望实现毫无信心（P004）。",
    "描述其形态：煎熬毫无意义与积淀，死不成、死不得、不敢死（P005）。",
    "以“被活埋”作意象，说明牵绊与缺少勇气（P006）。",
    "以“哪里有力气来知乎答题换赞”反讽收束（P007）。",
    "结论：这才是最苦（P008）。"
   ],
   "concept_usage": [
    {"term": "苦", "meaning": "本文区分两种：能靠“熬”度过的苦（乌龙茶）与失去希望本身的苦（真正的苦）。", "evidence": "P001", "ambiguity": "未给出区分两者的可操作判据。"},
    {"term": "希望", "meaning": "作者指人还能指望什么、且相信它能实现；希望的丧失即真正的苦。", "evidence": "P004", "ambiguity": "未说明希望的对象与来源。"},
    {"term": "被活埋", "meaning": "作者用以比喻处于真正苦中的状态：进了坟墓但未气绝。", "evidence": "P006", "ambiguity": "比喻性表述。"}
   ],
   "examples_and_targets": [
    "乌龙茶：作者用作“能熬过去的苦”的比喻（P001）。",
    "癌症、艾滋病、断手断脚、坐牢判刑、欠巨债：作者列举的可适应的困境（P003）。",
    "“被活埋——进了坟墓，但未气绝”：作者用以描写失去希望者的处境（P006）。",
    "知乎答题换赞：作者用作反讽材料，说明真正的苦者无力作答（P007）。"
   ],
   "conditions": [
    "P002：“前提是你还有希望，而且希望还很强”为能熬的条件。",
    "P003：“哪怕是……时间久了也会适应”为让步条件。",
    "P004：“即使有所指望，也完全没有任何它能实现的信心”为递进限定。",
    "P005：“只是有某些原因”指原因未明说。"
   ],
   "rhetoric_and_tone": "短文，先以比喻（乌龙茶）与排除法重定义“苦”，再以“被活埋”意象与排比描写绝境；末尾以“哪里有力气来知乎答题换赞”反讽作结；语气沉郁、克制，无劝慰与励志成分，也未叙述个人经历。",
   "unresolved_questions": [
    "提问者问“最苦的时候是什么时候、怎么熬过来”，正文未回答具体时间与经历，而是重定义“苦”。",
    "“哪里有力气来知乎答题换赞”是否指作者自身状态、抑或泛指，无法确定。",
    "P009 混入平台话题标签“悲观的人如何能变得乐观？”，lexical 未覆盖该片段，是否为正文需人工确认。",
    "brief 在“不知道还该指望什么、也不知道还能指望什么”处截断。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "只是需要熬就能熬过去的苦，其实后味回甘的乌龙茶而已。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "你之所以能熬，前提是你还有希望，而且希望还很强。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "真正的苦，不是困境本身难熬。困境本身——哪怕是癌症艾滋病断手断脚坐牢判刑欠巨债——时间久了也会适应。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "真正的苦，是没了希望本身——不知道还该指望什么、也不知道还能指望什么，即使有所指望，也完全没有任何它能实现的信心。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "每一分煎熬，都是毫无意义、毫无积淀的痛苦的延长。只是有某些原因让自己死不成、死不得、不敢死。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "当事人如同被活埋——进了坟墓，但未气绝，只恨自己太多牵绊、缺少勇气，不能早死。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "哪里有力气来知乎答题换赞。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P008", "quote": "这才是最苦。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["心理与情绪", "人生经验"],
   "issue_candidates": ["何为真正的苦", "希望与绝望", "苦难的适应"],
   "text_function_candidates": ["答疑", "界定", "抒情"],
   "object_candidates": ["提问者", "处于绝望中的人"],
   "working_keywords": ["乌龙茶", "希望", "绝望", "被活埋", "知乎答题换赞"]
  },
  "notes": "全文 9 段已读完，无图片节点，status=read。要点：①末段 P009 为平台话题标签“悲观的人如何能变得乐观？”，lexical 未覆盖（属平台字段混入）；②正文未回答提问者的具体时间与经历，而是重定义“苦”；③brief 被截断。"
 },
 "24e7b3ef": {
  "analysis": {
   "question_context": "提问者（Q001）问“文明这款游戏表达了唯物史观吗？”，询问该游戏的历史观归属。作者不评断唯物史观，而直接给出自己的判断：游戏表达的是一种劣化了的“神”导史观；并进一步论证任何诚实的史观都承认无法凭计划和计算“赢”得历史游戏，社会规则不可彻底测度，任何战略长期看必败，因此历史模拟游戏的“可赢性”恰恰说明它不真实。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "给出判断：文明游戏表达了一种劣化了的“神”导史观；任何诚实的史观都会承认不可能凭计划和计算“赢”得历史游戏，任何战略长期看都是必败的，因为社会规则不可彻底测度；被彻底掌握运转规律的社会里，全体成员将成永世不能超生的奴隶并因失去能动性而丧失人性，本质上不再是“社会”。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005"], "summary": "推论与收束：人性与可测可控的历史在原则上矛盾，因此任何历史模拟游戏都不可能真正反映真实的历史法则，于是才具有“可赢性”；“你能赢，就是假的”。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "文明这个游戏表达了一种劣化了的“神”导史观。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "任何诚实的史观都会承认：你不可能凭计划和计算“赢”得了“历史游戏”。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "任何一种战略，长期看都是必败的，因为社会的规则是不可彻底测度的。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "被彻底掌握运转规律的社会里，全体成员都将成为永世不能超生的奴隶，并因为失去能动性而丧失人性，本质上变成由大量碳基自走机所呈现的一种复杂的自然现象，而不再能称为“社会”。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人性与可测可控的历史是原则上矛盾的。", "evidence": ["E5"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "任何历史模拟游戏都不可能真正反映真实的历史法则，于是才具有“可赢性”；你能赢，就是假的。", "evidence": ["E6", "E7"]}
   ],
   "argument_steps": [
    "给出判断：文明游戏表达的是一种劣化了的“神”导史观（P001）。",
    "提出原则：诚实的史观承认无法凭计划与计算赢得历史游戏（P002）。",
    "给出理由：社会规则不可彻底测度，任何战略长期必败（P003）。",
    "推演彻底可控社会的后果：成员成奴隶、失去人性、不再是社会（P003）。",
    "提出矛盾命题：人性与可测可控的历史原则上矛盾（P004）。",
    "推出结论：历史模拟游戏不能反映真实历史法则，其“可赢性”即不真实的标志（P004、P005）。"
   ],
   "concept_usage": [
    {"term": "“神”导史观", "meaning": "作者自创术语（加引号），用以指文明游戏所表达的历史观，并与提问者所问的唯物史观相对。", "evidence": "P001", "ambiguity": "未给出定义，仅以“劣化了的”修饰。"},
    {"term": "历史游戏", "meaning": "作者指历史进程本身，并强调不可能凭计划和计算“赢”得它。", "evidence": "P002", "ambiguity": "与“历史模拟游戏”区分使用，但未明说界限。"},
    {"term": "可赢性", "meaning": "作者指历史模拟游戏可被玩家取胜的属性，并称这正说明它不反映真实历史法则。", "evidence": "P004", "ambiguity": "无。"},
    {"term": "碳基自走机", "meaning": "作者用以贬称在彻底可控社会中失去能动性的人。", "evidence": "P003", "ambiguity": "自创比喻性说法。"}
   ],
   "examples_and_targets": [
    "《文明》游戏：提问者提供的评断对象，作者称其表达劣化的“神”导史观（P001）。",
    "“碳基自走机”：作者自创的比喻材料（P003）。"
   ],
   "conditions": [
    "P002：“任何诚实的史观都会承认”为全称限定。",
    "P003：“长期看”为时间尺度限定；“被彻底掌握运转规律的社会里”为假设条件。",
    "P004：“原则上”为限定词。"
   ],
   "rhetoric_and_tone": "五段短论，断言密集：以“你能赢，就是假的。”作结，语气斩截；使用加引号的“神”导史观、可赢性等自创说法；不答提问者的唯物史观归属问题，而以替换框架的方式回应。",
   "unresolved_questions": [
    "提问者问的是游戏是否表达唯物史观，作者未直接评断唯物史观，只给出“劣化的‘神’导史观”这一判断。",
    "“神”导史观未作定义，也未说明“劣化”的具体所指。",
    "“社会的规则是不可彻底测度的”未给论证与依据。",
    "brief 在“并因为失去能动性而丧失人性。本”处截断。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "文明这个游戏表达了一种劣化了的“神”导史观。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "任何诚实的史观都会承认——你不可能凭计划和计算“赢”得了“历史游戏”。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "任何一种战略，长期看都是必败的。因为社会的规则是不可彻底测度的。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P003", "quote": "被彻底掌握运转规律的社会里，全体成员都将成为永世不能超生的奴隶，并因为失去能动性而丧失人性。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P004", "quote": "人性与可测可控的历史是原则上矛盾的。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P004", "quote": "因此任何历史模拟游戏都不可能真正反映真实的历史法则，于是才具有“可赢性”。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P005", "quote": "你能赢，就是假的。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["历史哲学", "游戏评论"],
   "issue_candidates": ["《文明》游戏的历史观", "唯物史观与神导史观", "历史可测度性"],
   "text_function_candidates": ["答疑", "评论", "论辩"],
   "object_candidates": ["《文明》游戏", "提问者"],
   "working_keywords": ["文明", "唯物史观", "“神”导史观", "可赢性", "碳基自走机", "可测度"]
  },
  "notes": "全文 5 段已读完，无图片节点，status=read。作者未直接回答“是否表达唯物史观”，而给出“劣化了的‘神’导史观”这一替换性判断；brief 被截断。"
 },
 "0343f198": {
  "analysis": {
   "question_context": "提问者（Q001）问“思想陷入极端循环怎么办？”，要求给出摆脱极端循环的办法。作者没有直接处理“极端循环”，而是重述问题为价值依托问题：先判定提问者的问题在于仍追求自己的满足（即便那满足被社会认定为“高尚”），再论证人生必然长期走向下坡、必在离死亡尚远时看到追求永远无法满足，故与自身绝望共处是人生必修课；战胜绝望的唯一途径是把人生价值寄托在他人将永远于精神上得益的事业上，并给出可操作的遗产形式与边界（必须是不特定的他人）。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "开篇命题：活得踏实、宁静的根本要害不是技能，也不是高尚趣味，而是将价值归依于他人。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P003"], "summary": "对提问者的诊断：其追求仍是自己的满足，被社会认定为“高尚”也本质无别；因无法得满足并认识到得满足的绝望，人生失去价值依托乃至想自杀，是彻底自私自利在逻辑上必然附带的后果，躲过此劫也还有别的劫难。", "role": "rebuttal"},
    {"unit_id": "U003", "paragraph_refs": ["P004"], "summary": "理由：人生必然长期看走向下坡，人必在尚离真正死亡有距离时看到追求永远没机会满足，剩余时间都须在绝望中度过。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P005"], "summary": "否定性限定：哄骗绝望本身没有用，绝望的产生无需能量而抵抗绝望需要能量，如人举石终将力竭。", "role": "qualification"},
    {"unit_id": "U005", "paragraph_refs": ["P006", "P007"], "summary": "出路：唯一途径是把人生价值寄托在他人将永远于精神上得益的事业上；所创造的东西随他人生存而继承，便不必忧虑自己的死亡或绝望。", "role": "action_advice"},
    {"unit_id": "U006", "paragraph_refs": ["P008", "P009"], "summary": "前提：人终有一死，寄于自身的一切都将灰飞烟灭；人的意义由有意或无意的遗产定义，而非由自身满足定义。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P010", "P011", "P012", "P013", "P014"], "summary": "作者第一人称自述：何时死去都可安心，因遗产已有人切实领受且会被加增赠与后人；每多活一天都在加增它；凭着喜乐可超脱自身损失与不满足；留下精神遗产是胜过死亡与绝望的方式，故早已死而无憾。", "role": "example"},
    {"unit_id": "U008", "paragraph_refs": ["P015", "P016", "P017"], "summary": "大解脱的两点：不再执着于争夺；施予者最大——不求得到便不受任何人管辖、最终自由自在，身边只剩能按此规则相处的人。", "role": "action_advice"},
    {"unit_id": "U009", "paragraph_refs": ["P018", "P019", "P020", "P021"], "summary": "具体化：“可以流传的精神上的收益”不必伟大，只需真实地让他人活得更心灵安稳、良知平静；可以是新发明、新知识（教程、诚实的书）、世代传承的慈善组织、诚实记录失败的自传、被教育好准备献身于人类的子女或学生，甚至只是扎实可参考的失败教训。", "role": "action_advice"},
    {"unit_id": "U010", "paragraph_refs": ["P022", "P023"], "summary": "边界条件：不要只利于特定个人（例如自己的子女），否则必为其可能遭受的意外毁灭提心吊胆；必须是不特定的他人。", "role": "qualification"},
    {"unit_id": "U011", "paragraph_refs": ["P024", "P025"], "summary": "例证与物质遗产安排：牛顿定律即使牛顿的仇敌也无法抗拒无法回避地受益，故最好是精神遗产；若为物质遗产，不妨以遗嘱尽量捐给衷心认可的对人类最有价值的公共机构（如留存财富发诺贝尔奖）。", "role": "example"},
    {"unit_id": "U012", "paragraph_refs": ["P026", "P027", "P028", "P029"], "summary": "结语：选择你的死法，然后你就好活；该惶恐不安的是现在死去留下的是不是一场空，若是则要抓紧。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人活着要活得踏实、宁静，最根本的要害既不是掌握技能，也不是追求高尚趣味，而是将价值归依于他人。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者判定提问者的问题首先在于追求的仍是自己的满足；即便所追求的是被社会认定为“高尚”的趣味，本质上也没什么不同。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "因自己无法得满足并进一步认识到得满足的绝望，人生失去价值依托乃至想“自杀”，从根上说是彻底的自私自利在逻辑上必然附带的后果；即便躲过这一劫，之后还会有别的劫难。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人生必然是一个长期看走向下坡的过程，人必然在离真正死亡尚有距离时看到自己的追求永远没机会满足；因此如何与自身的绝望共处本来就是人生的必修课。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "不要想办法去哄骗绝望本身，那是没有用的，因为绝望的产生无需能量，而抵抗绝望却是需要能量的。", "evidence": ["E5"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "战胜这绝望的唯一途径，就是将自己的人生价值寄托在某种他人将永远于精神上得益的事业上。", "evidence": ["E6"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人的意义是由他或有意或无意的遗产定义的，而非由他自身的满足定义。", "evidence": ["E7"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以第一人称自述：我于何时死去都可以安心，留下精神的遗产是我胜过死亡与绝望的方式，我心甚安、早已死而无憾。", "evidence": ["E8", "E9", "E10"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "施予者最大：不求得到就不受任何人管辖，最终自由自在；在我不求获取的前提下，任何事情都可以随心所欲。", "evidence": ["E11"]},
    {"claim_id": "C010", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "可以流传的精神上的收益并不需要多么伟大，只需要有真实的、能让他人活得更心灵安稳、良知平静的价值，哪怕极其轻微也无所谓。", "evidence": ["E12"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不要只是有利于特别的个人（比如自己的子女），否则必然会为他们可能遭受的意外毁灭提心吊胆；必须是不特定的他人。", "evidence": ["E13", "E14"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "如牛顿定律，即使是牛顿的仇敌也会无法抗拒无法回避地受益，故最好是精神遗产；若为物质遗产，不妨以遗嘱形式尽可能多地捐献给自己衷心认可的对人类最有价值的公共机构。", "evidence": ["E15", "E16"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者以反问提出：该惶恐不安的是你现在死去、留下的是不是一场空。", "evidence": ["E17"]}
   ],
   "argument_steps": [
    "定义式开篇（P001）：把“活得踏实宁静”的要害定在“将价值归依于他人”。",
    "诊断提问者（P002-P003）：追求自身满足（即使被社会判为高尚）→ 无法得满足 → 认识到得满足的绝望 → 失去价值依托、想自杀，并称此为自私自利逻辑上必然的后果。",
    "给出普遍前提（P004）：人生长期看必然下坡，追求终将永无满足之机，且此时离死亡尚远，故与绝望共处是必修课。",
    "排除无效方案（P005）：哄骗绝望无用，因绝望产生无需能量而抵抗需要能量。",
    "提出唯一途径（P006-P007）：把价值寄托于他人将永远于精神上得益的事业，创造物随他人继承。",
    "补充前提（P008-P009）：寄于自身者皆灰飞烟灭；意义由遗产而非自身满足定义。",
    "以身作证（P010-P014）：作者自述安心、喜乐、死而无憾。",
    "给出操作与收益（P015-P017）：不再执着争夺；施予者最大，不求获取则不受管辖。",
    "具体化对象（P018-P021）：收益不必伟大，可轻至一份失败教训。",
    "限定边界（P022-P023）：不得只利于特定个人，必须是不特定的他人。",
    "举例（P024-P025）：牛顿定律与公共机构捐赠、诺贝尔奖。",
    "格言式收束（P026-P029）：选择你的死法，然后你就好活；若是空，你要抓紧。"
   ],
   "concept_usage": [
    {"term": "价值归依于他人", "meaning": "本文开篇提出的根本命题：人生踏实宁静的要害所在；全文未对其作进一步定义。", "evidence": "P001", "ambiguity": "“他人”是否包含特定亲属，与P022-P023“必须是不特定的他人”之间的界限由作者后文限定。"},
    {"term": "绝望", "meaning": "追求永远没机会满足、且离真正死亡尚有距离时的状态；作者称其产生无需能量，抵抗它却需要能量。", "evidence": "P004", "ambiguity": "未与临床意义上的抑郁作区分。"},
    {"term": "精神遗产 / 遗产", "meaning": "他人将永远于精神上得益、可随他人生存而继承的东西；作者用它定义人的意义。", "evidence": "P009", "ambiguity": "P010“接受这一条款是法则性的前提”中的“这一条款”指代不明。"},
    {"term": "自私自利", "meaning": "作者对“追求自己的满足”的定性用语，被视为自杀念头的根源。", "evidence": "P003", "ambiguity": "属作者的判定而非心理学诊断。"},
    {"term": "施予者最大", "meaning": "因不求获取而不受任何人管辖、得以随心所欲。", "evidence": "P017", "ambiguity": "“最大”的含义未定义。"},
    {"term": "法则性的前提", "meaning": "作者称领受其遗产者须接受某一条款。", "evidence": "P010", "ambiguity": "条款内容与效力来源均未说明。"}
   ],
   "examples_and_targets": [
    "提问者（第二人称“你”，P002-P003）：作者的诊断与劝诫对象，其“追求自身满足”被作为反面路径。",
    "自杀（P003）：作者对提问者处境的判断用语，非事实陈述。",
    "“如人举石，终将力竭”（P005）：作者的比喻。",
    "牛顿定律与牛顿的仇敌（P024）：作者例证（精神遗产不可回避地被人受益）。",
    "诺贝尔奖与公共机构（P025）：作者举的物质遗产处置范例。",
    "新发明、教程、诚实的书、世代传承的慈善组织、诚实记录失败的自传、献身人类的子女或学生（P020）：作者列举的可接受遗产形式。",
    "扎实可参考的失败教训（P021）：作者列举的底线形式。"
   ],
   "conditions": [
    "前提：人生必然是一个长期看走向下坡的过程（P004）。",
    "排他性条件句：“战胜这绝望的唯一途径”（P006）。",
    "否定性条件：哄骗绝望没有用（P005）。",
    "门槛条件：哪怕极其轻微也无所谓（P019）。",
    "范围条件：必须是不特定的他人（P023）。",
    "条件句：如果是物质遗产，则不妨以遗嘱形式捐献（P025）。",
    "前提限定：在我不求获取的前提下（P017）。",
    "作者自称的接受条件：要领受我的遗产，接受这一条款是法则性的前提（P010）。"
   ],
   "rhetoric_and_tone": "训诫—劝谕式第二人称，直接点名“你的问题首先在于”；大量绝对化措辞（“没有用的”“唯一途径”“必须”“就是”）；比喻“如人举石，终将力竭”；P010-P014 转为作者第一人称的平静自述与喜乐告白；结尾为格言体短句（“选择你的死法，然后你就好活。”“以上。”），并以“——这也会给你带来大解脱”引出两点建议。",
   "unresolved_questions": [
    "提问者问“思想陷入极端循环怎么办”，作者未直接处理“极端循环”这一说法，而重述为价值依托问题，二者关系未说明。",
    "P010“接受这一条款是法则性的前提”中“这一条款”指代不明。",
    "P017“施予者最大”的“最大”含义未定义。",
    "“他人将永远于精神上得益”中“永远”如何成立（P006/P013）未论证。",
    "P010-P014 的喜乐、安心属作者自述（自我报告），无法外部核验。",
    "brief 在“并且进一步认识到得满足”处截断，正文续为“的绝望”，已以 text 为准。",
    "本文无图片节点，图片状态不适用。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "而是将价值归依于他人。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "你的问题首先在于你追求的仍然是自己的满足。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "只是彻底的自私自利在逻辑上必然附带的后果罢了。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "这意味着如何与自身的绝望共处，本来就是人生的必修课。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "绝望的产生无需能量，而抵抗绝望却是需要能量的。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "就是将自己的人生价值寄托在某种他人将永远于精神上得益的事业上。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P009", "quote": "人的意义是由他或有意或无意的遗产定义的，而非由他自身的满足定义。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P010", "quote": "我于何时死去都可以安心", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P013", "quote": "留下精神的遗产，是我胜过死亡与绝望的方式。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P014", "quote": "我心甚安，早已死而无憾。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P017", "quote": "我不求得到，就不受任何人管辖，最终自由自在。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P019", "quote": "哪怕极其轻微，也无所谓。", "relation": "qualifies"},
    {"key": "E13", "paragraph_id": "P022", "quote": "因为你必然会为他们可能遭受的意外毁灭提心吊胆", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P023", "quote": "必须是不特定的他人。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P024", "quote": "所以我说最好是精神遗产。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P025", "quote": "则不妨以遗嘱的形式尽可能多的捐献给你衷心认可的对人类最有价值的公共机构。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P027", "quote": "你该惶恐不安的，是你现在死去，你留下的是不是一场空？", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["人生哲学", "伦理学", "价值论"],
   "issue_candidates": ["价值的归依对象", "绝望与死亡焦虑", "精神遗产", "自杀念头", "遗产与意义"],
   "text_function_candidates": ["答疑", "劝谕", "论辩"],
   "object_candidates": ["提问者", "牛顿", "诺贝尔奖", "公共机构"],
   "working_keywords": ["价值归依于他人", "绝望", "精神遗产", "施予者最大", "不特定的他人", "自私自利", "死而无憾"]
  },
  "notes": "全文 29 段已读完，无图片节点，status=read。要点：①作者未直接回答“极端循环”，而重述为“价值归依于他人”；②P010-P014 为作者第一人称自述，非对读者的普遍断言；③“自杀”“劫难”为作者对提问者处境的判断，非事实陈述；④brief 被截断（“并且进一步认识到得满足”）；⑤“法则性的前提”“施予者最大”含混已登记；⑥无图片节点，image_checked 不适用。"
 },
 "d2e1d859": {
  "analysis": {
   "question_context": "提问者（Q001）问“什么是现代极简装修风格？装修成本大不大？”，含定义与成本两问。作者只对成本给出简答（“极简主义本身并不贵”），主要篇幅用于论证“奢华的极简”是对极简主义的背叛：极简规则本身已包含对“不必要”的判断，尺度由人自定；把“不必要”的尺度本身设在【不必要】的限度上，就得到“一万一平米的极简”；其推动力是知识分子阶层的炫耀与对复杂性的恐惧；作者由此主张极简主义只宜在公共建筑上深度应用，私宅只能量力而行。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004"], "summary": "命题与推理起点：极简主义本身并不贵；“去掉不必要的装饰”这一规则已包含对“不必要”的观点；把“不必要”的尺度定在哪里，“极简”的尺度就落在哪里。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P005"], "summary": "标题句给出核心判断：各种“奢华的极简”是把“不必要”的尺度本身设定在【不必要】的限度上。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007", "P008"], "summary": "解释豪奢化成因：极简主义因遭深刻背叛而呈豪奢色彩；其“不必要”判断依赖高度智力活动与阅历水平，主要追求者几乎仍是知识分子阶层，故只是“知识分子暴发户化”的外露；把炫耀视为“简”不掉的“必要”，才有一万一平米的极简，“这不是极简的错，是你们的错”。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P009"], "summary": "评价：奢华的“极简”在明白人眼里不是值得惊叹的创作，而是割舍不了的虚荣心。", "role": "rebuttal"},
    {"unit_id": "U005", "paragraph_refs": ["P010"], "summary": "第二重推动力：对深陷复杂性的恐惧——简得越极端，映照的恐惧越深越不理性；现代社会的复杂性确令人望而生畏，这是极简主义引起广泛共鸣的社会心理根基；极简主义象征一种控制、对复杂性说不的权力，是一面“反抗军旗”，理念本身积极，直到有人把旗帜改用镜面不锈钢加激光蚀刻。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P011", "P012", "P013", "P014"], "summary": "勇者/弱者对照：勇者追求重归平衡与共处，弱者追求抄家灭门、斩草除根、永绝后患；作者以反问追询这面消光不锈钢旗帜属于谁的旗，并称能举旗者获得了这么多仍解脱不了执着。", "role": "rebuttal"},
    {"unit_id": "U007", "paragraph_refs": ["P015", "P016", "P017"], "summary": "结论与适用边界：极简主义在精神原则上只能合法地在公共建筑上做深度应用，私宅只能量力而行；私宅运用时要时刻注意是否在玩“不必要的不必要”，那是深刻的虚伪。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "极简主义本身并不贵。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "极简主义的规则“去掉不必要的装饰”已包含对“不必要”的观点；把“不必要”的尺度定在哪里，“极简”的尺度就落在哪里。", "evidence": ["E2", "E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "各种“奢华的极简”，是把这“不必要”的尺度本身设定在了【不必要】的限度上。", "evidence": ["E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "极简主义因遭到深刻的背叛而呈现豪奢色彩；其“不必要”判断依赖高度的智力活动和阅历水平，主要追求者几乎仍是知识分子阶层，故这种豪奢化只是“知识分子暴发户化”的外露。", "evidence": ["E5", "E6"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "把炫耀视为“简”不掉的“必要”才出现“一万一平米的极简”；这不是极简的错，是“你们”的错。", "evidence": ["E7"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "奢华的“极简”在明白人眼里不是什么值得惊叹的创作，而是割舍不了的虚荣心。", "evidence": ["E8"]},
    {"claim_id": "C007", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "“奢华的极简”的另一重推动力是对深陷复杂性的恐惧；简得有多极端，就映照出这恐惧有多深、有多不理性。", "evidence": ["E9"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "极简主义象征了一种控制、一种对复杂性说不的权力，是一面“反抗军旗”；这个理念毫无疑问是积极的——直到有人把旗帜改用镜面不锈钢制成再激光蚀刻掉光泽。", "evidence": ["E10"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "勇者的追求是重归平衡与共处，弱者的追求是抄家灭门、斩草除根、“永绝后患”；前者可敬可佩，后者可悲可怜。", "evidence": ["E11"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者以反问提出归属疑问：这面立体构成的消光不锈钢旗帜，是勇者的旗还是弱者的旗。", "evidence": ["E12"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为极简主义在精神原则上只能合法地在公共建筑上做深度应用，而在私宅上只能量力而行。", "evidence": ["E13"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "在私宅运用极简主义时要时刻注意是否在玩“不必要的不必要”，那是一种深刻的虚伪。", "evidence": ["E14"]}
   ],
   "argument_steps": [
    "先答成本之问（P001）：极简主义本身并不贵。",
    "拆解规则（P002-P003）：规则已含“不必要”的判断，尺度由人自定。",
    "给出核心判断（P005 heading）：奢华的极简把“不必要”的尺度本身设在【不必要】的限度上。",
    "解释成因之一（P006-P008）：依赖智力与阅历的知识分子阶层把炫耀当成简不掉的必要，故是“知识分子暴发户化”的外露，并归责于“你们”而非极简主义。",
    "价值评判（P009）：只是割舍不了的虚荣心。",
    "解释成因之二（P010）：对复杂性的恐惧；先承认极简理念积极与现代社会的复杂性令人望而生畏，再以旗帜被改用镜面不锈钢作转折。",
    "勇者/弱者对照与反问（P011-P014）。",
    "给出适用边界（P015-P017）：公共建筑可深度应用，私宅须量力而行，否则是深刻的虚伪。"
   ],
   "concept_usage": [
    {"term": "极简主义", "meaning": "本文中首先是一条规则“去掉不必要的装饰”，其成本本身不高；作者又指它象征对复杂性说不的控制。", "evidence": "P002", "ambiguity": "提问者问的是“现代极简装修风格”，作者未给风格定义，只讨论其尺度与豪奢化。"},
    {"term": "不必要", "meaning": "由个人智力与阅历自行设定的尺度；尺度定在哪里，极简就落在哪里。", "evidence": "P003", "ambiguity": "尺度标准未给出可操作判据。"},
    {"term": "不必要的不必要", "meaning": "作者用以指私宅中对“不必要”尺度本身的再消费，被判定为深刻的虚伪。", "evidence": "P016", "ambiguity": "与P005【不必要】的限度是否同一含义，作者未明说。"},
    {"term": "奢华的极简 / 极简主义的豪奢化", "meaning": "被作者判定为对极简主义的背叛与虚荣心外露的装修现象。", "evidence": "P006", "ambiguity": "未举具体案例或品牌。"},
    {"term": "复杂性", "meaning": "现代社会的复杂性令人望而生畏，被视为极简主义广泛共鸣的社会心理根基。", "evidence": "P010", "ambiguity": "未界定复杂性的范围。"},
    {"term": "公共性", "meaning": "作者称可以救赎上述一切精神上的失败。", "evidence": "P016", "ambiguity": "救赎机制未展开。"},
    {"term": "反抗军旗", "meaning": "作者对极简主义象征意义的比喻。", "evidence": "P010", "ambiguity": "属修辞用语。"}
   ],
   "examples_and_targets": [
    "提问者（“你们”，P007-P008）：被作者直接归责与劝诫的对象。",
    "“一万一平米的极简”（P008）：作者引为被批评的现象。",
    "镜面不锈钢制成、激光蚀刻去掉光泽的旗帜（P010）：作者的比喻材料。",
    "抄家灭门、斩草除根、“永绝后患”（P011）：作者对“弱者追求”的修辞性描述。",
    "知识分子阶层与“知识分子暴发户”（P006）：作者批评的对象群体。",
    "公共建筑与私宅（P015-P016）：作者区分适用场景的对照。"
   ],
   "conditions": [
    "尺度条件：你把“不必要”的尺度定在哪里，你的“极简”的尺度就落在哪里（P003）。",
    "依赖条件：极简主义的“不必要”判断依赖于高度的智力活动和阅历水平（P006）。",
    "让步—转折条件：这个理念毫无疑问是积极的，直到有人将旗帜改用镜面不锈钢制成（P010）。",
    "适用边界：在精神原则上只能合法地在公共建筑上做深度应用，而在私宅上只能量力而行（P015）。",
    "私宅条件：运用时要时刻注意是不是在玩“不必要的不必要”（P016）。",
    "救赎条件：上面所批评的一切精神上的失败，都可以被公共性救赎（P016）。"
   ],
   "rhetoric_and_tone": "论辩兼批评，语气强硬直白：第二人称“你们”直接归责（“这不是极简的错，是你们的错”）；用引号与方头括号标注被批评对象（“奢华的极简”、【不必要】）；比喻密集（反抗军旗、镜面不锈钢、激光蚀刻）；以反问作结（P013）；并用“前者可敬可佩，后者可悲可怜”的对仗句作价值对照；P005 为 heading 结构，承担核心断语。",
   "unresolved_questions": [
    "提问包含“什么是现代极简装修风格”，作者未给出该风格的定义，只讨论“不必要”的尺度问题。",
    "提问问“装修成本大不大”，作者仅以“极简主义本身并不贵”一句作答，未给任何成本数据、预算或量级。",
    "P015“只能合法的在公共建筑上做深度应用”中“合法的”是指“合乎法理”还是“合理地”，语义不明。",
    "P018（“家装中，为什么说极简=极奢？”）为平台话题标签混入正文，lexical 未覆盖；该等式作者未在正文展开。",
    "“一万一平米的极简”“知识分子暴发户化”均未给出可核验的实例或数据，属待外部核查的现象描述。",
    "brief 在“是将这‘不必要’的尺度本身设定在了【不必要】的限度上。”处结束，正文续有P006以下内容，已以 text 为准。",
    "本文无图片节点，图片状态不适用。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "极简主义本身并不贵。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "显然已经包含了对“不必要”的观点。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "你把“不必要”的尺度定在哪里，你的“极简”的尺度就落在哪里。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P005", "quote": "是将这“不必要”的尺度本身设定在了【不必要】的限度上。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P006", "quote": "极简主义是因为遭到了深刻的背叛而呈现出豪奢的色彩。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "只是一种“知识分子暴发户化”的外露。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P008", "quote": "这不是极简的错，是你们的错。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P009", "quote": "而是割舍不了的虚荣心而已。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P010", "quote": "简得有多极端，就映照出这恐惧有多深，有多不理性。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P010", "quote": "极简主义象征了一种控制，一种对复杂性说不的权力，是一面“反抗军旗”。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P011", "quote": "弱者的追求是抄家灭门、斩草除根、“永绝后患”。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P013", "quote": "这面立体构成的消光不锈钢旗帜，是勇者的旗还是弱者的旗？", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P015", "quote": "就只能合法的在公共建筑上做深度应用，而只能在私宅上量力而行。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P016", "quote": "运用极简主义时就要时刻注意你是不是在玩“不必要的不必要”。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P014", "quote": "能举这面旗的人，获得了这么多，还是解脱不了这种执着。", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["室内设计批评", "美学", "社会心理评论"],
   "issue_candidates": ["极简主义的豪奢化", "装修成本", "炫耀性消费", "对复杂性的恐惧"],
   "text_function_candidates": ["答疑", "批评", "论辩"],
   "object_candidates": ["提问者", "知识分子阶层", "公共建筑", "私宅"],
   "working_keywords": ["极简主义", "不必要", "奢华的极简", "知识分子暴发户化", "反抗军旗", "公共性", "复杂性"]
  },
  "notes": "全文 18 段已读完，无图片节点，status=read。要点：①作者只以一句回应“成本大不大”，主体是对“奢华的极简”的批评；②“这不是极简的错，是你们的错”为直接归责于提问者一方；③P005 为 heading 结构；④P018 为平台话题标签“家装中，为什么说极简=极奢？”混入正文（lexical 未覆盖），已在未决问题登记；⑤brief 被截断；⑥无图片节点，image_checked 不适用。"
 },
 "a5309387": {
  "analysis": {
   "question_context": "提问者（Q001）问“如何摆脱原生家庭造成的人格缺陷？”，其中已预设“人格缺陷由原生家庭造成”。作者不接受该预设，也不给摆脱方法：先指出“原生家庭”一词已被“微信心理学”用烂，再以讽刺笔法复述提问者的推理链（焦虑→归咎无能→归咎原生家庭→收工），指责这类话语在利用人们急于推卸个人成长责任的心理缺陷、贩卖“福寿膏”换流量，最后以“世上无完美的父母”和“伤害具有普遍性”两条断言收束，并把差别落在“不是只有你受了伤害”。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "开篇断言：“原生家庭”四个字已经快被“微信心理学”用烂了。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P003", "P004"], "summary": "以讽刺口吻复述提问者一方的推理链：你有一种焦虑，归咎于一种无能，再将这无能归咎于原生家庭，打完收工；随后以“都是爹妈害的。都怪ta们呀～”与单字“唉。”作反讽。", "role": "rebuttal"},
    {"unit_id": "U003", "paragraph_refs": ["P005"], "summary": "反问指责：这类说法在利用人们急于推卸个人成长责任的心理缺陷，贩卖“福寿膏”换流量。", "role": "rebuttal"},
    {"unit_id": "U004", "paragraph_refs": ["P006"], "summary": "命令式断言：别挑了，世上无完美的父母，句号。", "role": "conclusion"},
    {"unit_id": "U005", "paragraph_refs": ["P007", "P008", "P009"], "summary": "以普遍性收束：没有人是不受“原生家庭伤害”的，任何伟人、任何所羡慕的人、任何“完人”都与你们一样深受其害，其中恐有大部分所受伤害比提问者更深；你与所羡慕者的差别根本不是“你受了伤害而他们就没有”。", "role": "reason"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“原生家庭”四个字已经快被“微信心理学”用烂了。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者刻画提问者一方的推理链：有一种焦虑，把它归咎于一种无能，再将这无能归咎于原生家庭，打完收工。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "opponent_view", "attribution": "opponent", "modality": "asserted", "statement": "被作者以反讽口吻复述并反驳的说法：自己的问题都是父母（原生家庭）害的。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者以反问指责：这类说法是在利用人们急于推卸个人成长责任的心理缺陷，贩卖“福寿膏”换流量。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "世上无完美的父母。", "evidence": ["E5"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "没有人是不受“原生家庭伤害”的；任何一个伟人、任何一个所羡慕的人、任何一个“完人”，都与你们一样“深受原生家庭伤害”。", "evidence": ["E6"]},
    {"claim_id": "C007", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "其中恐怕有大部分人所受的“伤害”比提问者还深得多。", "evidence": ["E7"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "你和你所羡慕的人的差别根本就不是你受了伤害而他们就没有。", "evidence": ["E8"]}
   ],
   "argument_steps": [
    "起手贬抑话题词（P001）：“原生家庭”已被“微信心理学”用烂。",
    "复述并反讽提问方的归因链（P002-P003）：焦虑→无能→原生家庭→打完收工；以“都怪ta们呀～”与“唉。”加重讽刺。",
    "给出指责性反问（P005）：这是利用推卸责任的心理缺陷做流量生意（“福寿膏”）。",
    "以命令句切断挑剔（P006）：世上无完美的父母。",
    "以普遍性反驳差别论（P007-P009）：人人深受原生家庭伤害，区别不在有无伤害。"
   ],
   "concept_usage": [
    {"term": "原生家庭", "meaning": "本文中是被作者指为遭“微信心理学”滥用的流行词，并作为提问者归因链的终点。", "evidence": "P002", "ambiguity": "作者未定义该词，也未否认家庭影响存在。"},
    {"term": "微信心理学", "meaning": "作者对流行心理自助话语的贬称。", "evidence": "P001", "ambiguity": "未指明具体账号、文章或机构。"},
    {"term": "福寿膏", "meaning": "作者比喻这类话语是精神鸦片式的流量贩卖。", "evidence": "P005", "ambiguity": "属修辞用语，非事实指控的具体对象。"},
    {"term": "个人成长责任", "meaning": "作者认为读者急于推卸的东西。", "evidence": "P005", "ambiguity": "其内涵与承担方式本文未说明。"},
    {"term": "“原生家庭伤害”", "meaning": "作者称其具有普遍性，人人难免；该词在原文中带引号。", "evidence": "P007", "ambiguity": "引号是否表示作者对“伤害”一词的保留，未明说。"},
    {"term": "“完人”", "meaning": "作者以引号标示并否认其存在。", "evidence": "P007", "ambiguity": "未给出判据。"}
   ],
   "examples_and_targets": [
    "提问者（第二人称“你/你们”，P002/P005/P009）：作者的批评与劝诫对象。",
    "父母（“爹妈”“ta们”，P003）：作者反讽性转述中被归咎的一方。",
    "“微信心理学”（P001）：被批评对象，未具体指明。",
    "伟人、所羡慕的人、“完人”（P007）：作者的对比例证，均为泛指，未举具体人物。",
    "“福寿膏”（P005）：修辞比喻材料。"
   ],
   "conditions": [
    "提问预设“人格缺陷由原生家庭造成”，作者未接受该预设，也未讨论人格缺陷本身。",
    "命令式终止条件：别挑了（P006）。",
    "隐含前提：原生家庭伤害具有普遍性（P007）。",
    "概率限定：其中恐怕有大部分所受的“伤害”比你还深得多（P008）。",
    "本文未给出任何“如何摆脱”的条件、步骤或方法。"
   ],
   "rhetoric_and_tone": "讽刺、反讽与调侃为主：以“都是爹妈害的。都怪ta们呀～”摹拟并嘲弄提问方口吻，以单字“唉。”作情绪插入；用格言式短句下断语（“别挑了，世上无完美的父母，句号。”）；以反问施压（P005）；第二人称直接对话。全文为短篇断言式，未展开论证；引号被用来标示作者对“原生家庭伤害”“完人”等词的保留态度。",
   "unresolved_questions": [
    "提问者问“如何摆脱”，作者未给任何方法、步骤或替代路径，仅作批评与断言。",
    "作者未讨论“人格缺陷”是否存在或如何界定，也未接受提问的这一预设。",
    "“微信心理学”“福寿膏”无具体指涉，无法核验所指对象。",
    "P007 提到的伟人、所羡慕的人、“完人”均为泛指，无具体人物与证据。",
    "作者把“原生家庭伤害”普遍化（P007-P009）但未给经验依据，属待外部核查的断言。",
    "brief 末尾为“别挑了，世上无完美”，正文作“别挑了，世上无完美的父母，句号。”，已以 text 为准。",
    "本文无图片节点，图片状态不适用。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "“原生家庭”四个字已经快被“微信心理学”用烂了。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "你将这无能归咎于原生家庭，打完收工。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "都是爹妈害的。都怪ta们呀～", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P005", "quote": "在利用你们急于推卸个人成长责任的心理缺陷，在贩卖福寿膏换你们的流量吗？", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P006", "quote": "世上无完美的父母，句号。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P007", "quote": "没有人是不受“原生家庭伤害”的。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P008", "quote": "其中恐怕有大部分所受的“伤害”比你还深得多呢。", "relation": "qualifies"},
    {"key": "E8", "paragraph_id": "P009", "quote": "你和你所羡慕的人的差别根本就不是你受了伤害而他们就没有。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["社会心理评论", "家庭教育", "大众话语批评"],
   "issue_candidates": ["原生家庭归因", "个人成长责任", "流行心理学话语", "责任推卸"],
   "text_function_candidates": ["答疑", "批评", "反讽"],
   "object_candidates": ["提问者", "父母", "“微信心理学”写作者", "伟人与“完人”"],
   "working_keywords": ["原生家庭", "微信心理学", "福寿膏", "个人成长责任", "原生家庭伤害", "完人"]
  },
  "notes": "全文 9 段已读完，无图片节点，status=read。要点：①作者不接受提问预设，未回答“如何摆脱”，也未讨论“人格缺陷”本身，已在未决问题登记；②P003 为作者反讽性复述提问方口吻，其“都是爹妈害的”归入 opponent_view；③“微信心理学”“福寿膏”无具体指涉，属待核对象；④P007-P009 的普遍性断言无经验依据，登记为待外部核查；⑤brief 被截断；⑥无图片节点，image_checked 不适用。"
 }
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
