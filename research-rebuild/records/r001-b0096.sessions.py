# -*- coding: utf-8 -*-
"""批次 r001-b0096 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0096.sessions.py            # 写 out/r001-b0096.out.jsonl
  python3 records/r001-b0096.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0096"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0096.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "36cdf517": {
  "analysis": {
   "question_context": "提问者（Q001）问“爱到底是什么？”。作者不按日常情感话题作答，而是宣称要“追本溯源”地考察“爱”这个概念：用拉丁文版、英王钦定本与中文和合本的《哥林多前书》‘爱’段逐词对照，论证东亚现在所谈的“爱”本非东亚原生概念，其源头对应词是 caritas/慈善而不是 Love，并据此给出“爱是什么”的定义式收束。提问者的提问只有一句，未表达立场。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "交代目的与方法：追本溯源谈“爱”；用拉丁文版、英王钦定本、中文和合本三版对照，明示不纠缠三版各自的大量小版本差异，只看“最显然的大局”。", "role": "context"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005", "P006"], "summary": "说明选 Bible 的理由（东亚所谈的“爱”不是东亚原生概念）与选这三个版本的理由（拉丁文版是基督教立为罗马国教后确立的正典版本）；作者声明自己不专精拉丁文、不主张本文答案是标准答案。", "role": "context"},
    {"unit_id": "U003", "paragraph_refs": ["P007", "P008", "P009", "P010", "P011", "P012", "P013", "P014", "P015", "P016", "P017", "P018"], "summary": "逐词对读开头数句：patiens（忍耐痛苦的耐心，非“病人”）、suffereth（受苦）、non aemulatur（不嫉妒）、non agit perperam（不自夸）、non inflatur（不张狂）、non est ambitiosa；作者把后者译作“爱没有野心”，并指出英王钦定本作 doth not behave itself unseemly。", "role": "example"},
    {"unit_id": "U004", "paragraph_refs": ["P019", "P020", "P021"], "summary": "比较两版的制作与读者处境（修士常年祈祷后在羊皮卷上抄写、为座堂镇殿之宝 vs 印刷机大量印给识字不多的民众当报纸读），提出英王钦定本的通俗化导致圣经原意被英语文化语境迁移；以“爱无野心→爱是不做害羞的事”为例，称该转译把解释权从教会大公会议转到国王御案。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P022", "P023", "P024", "P025", "P026", "P027", "P028", "P029", "P030"], "summary": "继续逐词对读：seeketh not her own（不求自己的益处）、non irritatur（作者译“爱不受挑衅”）、non cogitat malum（作者译“爱不思恶／不以恶意揣测人”）。", "role": "example"},
    {"unit_id": "U006", "paragraph_refs": ["P031", "P032", "P033", "P034", "P035", "P036", "P037"], "summary": "解读 iniquity（敌意的、恶意的行为）与 congaudet veritati：爱不喜欢任何对他人含有恶意、冀望人受损的行为；爱以真实为乐，其中根植“事实自身永远是善”的价值观。", "role": "claim"},
    {"unit_id": "U007", "paragraph_refs": ["P038", "P039", "P040", "P041", "P042", "P043", "P044"], "summary": "omnia suffert 应译“凡事忍受”，中文译者因文化心理隔阂转译成“包容、宽容”，而拉丁文原义是“忍饥挨饿”那样性质的忍受。", "role": "claim"},
    {"unit_id": "U008", "paragraph_refs": ["P045", "P046", "P047", "P048", "P049", "P050"], "summary": "称 omnia credit 是“又一个至关重要的迁移”：区分 credit（授信，以真视之，先假定为真、待违信再反应）与 believe（认信为真，含拒绝转为不信的义务，即“对怀疑的免疫力”），主张此句应译“凡事授信”。", "role": "claim"},
    {"unit_id": "U009", "paragraph_refs": ["P051", "P052", "P053", "P054", "P055"], "summary": "omnia sperat 的解读：对一切都寄予希望，因而没有“绝望”；可以以任何其他理由停止投入或停止服务某人，但不能是因为“绝望”，因为人不能预测未来、不能决定历史，没有逻辑上有效的能力做出绝望的结论。", "role": "claim"},
    {"unit_id": "U010", "paragraph_refs": ["P056", "P057", "P058"], "summary": "omnia sustinet 宜译“持续、坚持”（sustainability 同源）；英文 endureth 含“硬挺着直到灾难过去”之意，也适合译“凡事坚持”。", "role": "qualification"},
    {"unit_id": "U011", "paragraph_refs": ["P059", "P060", "P061", "P062", "P063", "P064"], "summary": "Caritas numquam excidit／never fail 直译为“从不失败”；中文由“从不失败”推出“从不认输”，故译成“爱永不止息”。", "role": "claim"},
    {"unit_id": "U012", "paragraph_refs": ["P065", "P066", "P067", "P068", "P069"], "summary": "源头两版都没有把这里的“爱”对应为 Love，而是 caritas／charity；Love 是盎格鲁-撒克逊语原生词，指“快乐的情绪”“使人快乐”；因英国崛起而发生的 Caritas→Love 迁移是“爱”概念的至关重要的异变；“欲使人快乐的东西”并不能使人快乐，是 Caritas 使人平安喜乐，Love 不能替代 caritas。", "role": "claim"},
    {"unit_id": "U013", "paragraph_refs": ["P070", "P071", "P072", "P073", "P074", "P075", "P076", "P077", "P078", "P079"], "summary": "总结定义：爱不是 love，爱是 caritas／慈善；行为若不是慈善则不成其为爱；爱不是男女缠绵之情；慈善不分性别、种族、阶级、意识形态，不自夸、不膨胀、无野心、不想象恶、甘愿受苦、信奉真理、凡事授信、永不绝望、永不认输；爱是人借以战胜罪恶的神性内核，是人所能行最近于神的事。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称现在在东亚所谈的“爱”的概念，不是本来直接存在于东亚文化里的原生概念（故须回到 Bible 的拉丁文与英译本追本溯源）。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者声明自己并不专精拉丁文，也不主张读者以本文答案为标准答案，这些只是其个人理解。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "quoted_or_cited", "attribution": "cited_source", "modality": "asserted", "statement": "本篇逐句并列引用拉丁文版、英王钦定本与中文和合本的《哥林多前书》‘爱’段作为对照材料（引文属被引经文，非作者自撰）。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称 patiens 不是“病人”而是耐心，专指忍耐痛苦的耐心，忍耐病痛的人因此被称为 patient。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称英王钦定本作为印给基本不识字民众当报纸读的通俗读物，带来了一个致命问题：圣经的原意被英语文化的语境迁移了。", "evidence": ["E5"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称“爱无野心”被迁移成“爱是不做害羞的事”，而何谓 unseemly 属“皇家御准事业”，这一转译把原文解释权从教会大公会议转移到国王御案。", "evidence": ["E6"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称 non cogitat malum 应理解为爱不想象恶、不向恶思索、不以恶意揣测人（“爱不思恶”）。", "evidence": ["E7", "E30"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称 iniquity 指敌意的、恶意的行为，中文“不喜欢不义”实际上指不喜欢任何对他人含有恶意、冀望人受损的行为。", "evidence": ["E27", "E8"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称爱之中根植了“事实自身永远是善”的价值观：无论幻觉让人如何享受、事实让人如何折磨，明了事实、摆脱幻觉都值得庆贺。", "evidence": ["E26", "E9"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称 omnia suffert 其实应译“凡事忍受”，在拉丁文中是“忍饥挨饿”那样性质的忍受；中文译成包容、宽容是译者的转身。", "evidence": ["E10", "E11"]},
    {"claim_id": "C011", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者称按个人理解 credit 不是“相信”而是“授信”：credit 是“以真视之”，believe 是“认信为真”并要求拒绝转为不信的义务（“对怀疑的免疫力”），否则只可称为 credit。", "evidence": ["E12", "E13"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称按拉丁文，omnia credit 实际上应译为“凡事授信”，即对一切人的声称首先当作真实的诚实的来对待，直到看到事实与此相悖。", "evidence": ["E14"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称可以以其他任何理由停止投入或停止服务某人，但不可以是因为“绝望”；因为人不能预测未来、不能决定历史，没有逻辑上有效的能力做出“绝望”的结论。", "evidence": ["E24", "E15"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称源头两版都没有把这里的“爱”对应为 Love，而是 caritas／charity；Love 是盎格鲁-撒克逊语原生词，指向“快乐的情绪”、指“使人快乐”。", "evidence": ["E25", "E16"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称从拉丁文 Caritas／慈善向盎格鲁-撒克逊语 Love／使人快乐的迁移，是“爱”这个概念的一次至关重要的异变；令人叹息的是“欲使人快乐的东西”并不能使人快乐，是 Caritas 使人真正的平安喜乐。", "evidence": ["E17", "E31"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称爱不是 love，爱是 caritas／慈善；一种行为若不是慈善，则不成其为爱。", "evidence": ["E18", "E19"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者称爱不是你侬我侬、耳鬓厮磨、缠绵悱恻，更不是寤寐思服、辗转反侧，根本就不是这种东西。", "evidence": ["E20"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称 Caritas／慈善无虑性别、种族、阶级、意识形态，它不自夸、不膨胀、无野心、不想象恶、甘愿受苦、信奉真理、凡事授信、永不绝望、永不认输。", "evidence": ["E21", "E32"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称爱是人类借以穿透一切兽性、消解一切恶念、最终战胜一切罪恶的神性内核，是人所能行最近于神的事。", "evidence": ["E22", "E33"]}
   ],
   "argument_steps": [
    "先定方法与范围：三版对照，声明不打小版本差异的口舌官司，只看大局（P002）。",
    "给出选材理由：东亚所谈的“爱”非东亚原生概念，故须溯至 Bible；三版中拉丁文版是罗马国教确立的正典（P003—P005）。",
    "自我限定：作者不专精拉丁文，答案非标准答案，只是个人理解（P006）。",
    "逐词例证：patiens→耐心、suffereth→受苦、non aemulatur→不嫉妒、non agit perperam→不自夸、non inflatur→不张狂、non est ambitiosa→爱没有野心（P007—P018）。",
    "以版本物质形态与读者差异解释迁移：修士抄本 vs 印刷通俗读物，KJV 使原意被英语语境迁移（P019—P020）。",
    "举例坐实迁移的后果：爱无野心→爱是不做害羞的事，解释权由大公会议转到国王（P021）。",
    "继续逐词：不求自己的益处、爱不受挑衅、爱不思恶（P022—P030）。",
    "由 iniquity 与“只喜欢真理”推出爱以真实为乐、“事实自身永远是善”（P031—P037）。",
    "指出中译的第二处迁移：凡事忍受→凡事包容，并还原拉丁文语义（P038—P044）。",
    "指出第三处“至关重要的迁移”：credit 被译成“相信”，据词义区分授信与认信，主张改译“凡事授信”（P045—P050）。",
    "由 omnia sperat 推出不存在“绝望”，并给出理由：人不能预测未来、不能决定历史（P051—P055）。",
    "由 sustinet 推出“坚持/持续”义（P056—P058）。",
    "由 never fail 到“永不止息”的转译链（P059—P064）。",
    "指出源头用词是 caritas/charity 而非 Love，追溯 Love 的语源与本义，判定 Caritas→Love 是概念的异变（P065—P068）。",
    "结论式定义与排他：爱＝caritas／慈善，不是 love，不是男女之情；并以宗教语汇给出“神性内核”的收束（P069—P079）。"
   ],
   "concept_usage": [
    {"term": "爱（中译词）", "meaning": "本文讨论的核心译词；作者主张它在东亚不是原生概念，其源头对位是 caritas／慈善，而非现代意义的 love、更非男女情爱。", "evidence": "P003、P071、P073", "ambiguity": "中文“爱”同时承载译经用语与现代情爱义，作者明言后者被误当作本文所说的爱。"},
    {"term": "caritas / charity", "meaning": "拉丁文正典与英王钦定本用以对译此段“爱”的词，作者视为“爱”的真正对位表述，义近慈善。", "evidence": "P065、P071、P075", "ambiguity": "作者未交代 caritas 在拉丁文中的其他义项与后世神学用法。"},
    {"term": "love", "meaning": "盎格鲁-撒克逊语原生词，作者称其指“快乐的情绪”、指“使人快乐”，并视之为造成概念异变的译词。", "evidence": "P066、P067、P069", "ambiguity": "作者未区分现代英语 love 的多义用法（亲情、情爱、爱好等）。"},
    {"term": "patiens / patient", "meaning": "忍耐痛苦的耐心；忍耐病痛的人被称为 patient。", "evidence": "P008", "ambiguity": "无。"},
    {"term": "ambitiosa / ambition", "meaning": "野心；作者据此把 non est ambitiosa 译作“爱没有野心”。", "evidence": "P016、P017", "ambiguity": "作者未讨论拉丁文词在经文语境中的其他可能义。"},
    {"term": "credit（授信）vs believe（相信）", "meaning": "credit 是“以真视之”、先假定为真、待违信再反应；believe 是“认信为真”，并含拒绝采纳反证、拒绝转为不信的义务（“对怀疑的免疫力”）。", "evidence": "P047、P049、P050", "ambiguity": "作者明言这是“我个人理解”，属其自设区分。"},
    {"term": "iniquity", "meaning": "敌意的行为、恶意的行为。", "evidence": "P032、P033", "ambiguity": "无。"},
    {"term": "omnia", "meaning": "全向的、全部的（作者以 omni light 全向射灯作比）。", "evidence": "P040", "ambiguity": "无。"},
    {"term": "sustinet / sustainability", "meaning": "持续、坚持；作者据此把“凡事忍耐”读作“凡事坚持”。", "evidence": "P057、P058", "ambiguity": "无。"},
    {"term": "numquam excidit / never fail", "meaning": "从不失败；作者称中文由“从不失败”推出“从不认输”，再译成“永不止息”。", "evidence": "P060、P062、P063", "ambiguity": "作者未说明译者转译是否为有意为之。"},
    {"term": "事实 / 真理", "meaning": "爱所乐于其中的对象；作者称“爱之中根植了‘事实自身永远是善’的价值观”。", "evidence": "P035、P036", "ambiguity": "“事实自身永远是善”是作者的价值命题，本文未加论证。"}
   ],
   "examples_and_targets": [
    "《哥林多前书》‘爱’段的拉丁文版、英王钦定本、中文和合本三语对照——作者的核心材料与引文来源（P002、P007 起）。",
    "拉丁文版：基督教被立为罗马国教后确立的正典版本（P005）；由修士一天祈祷数小时后在羊皮卷上抄写、为各教区座堂镇殿之宝（P019）——作者的历史叙述，需外部核查。",
    "英王钦定本：以印刷机大量印给基本不识字、只会英文白话的老百姓当报纸读的通俗读物（P020）——作者的历史叙述，需外部核查。",
    "“爱无野心”被译成“爱是不做害羞的事”，以及 unseemly 的界定权属“皇家御准事业”——作者的例证与批评对象（P021）。",
    "credit card 信用卡——作者用以类比“授信”：先假定你是真的，等你违信了再作反应（P048）。",
    "omni light 全向射灯——作者用以解释 omnia 的类比（P040）。",
    "你侬我侬、耳鬓厮磨、缠绵悱恻、寤寐思服、辗转反侧——作者用以指认被误当作“爱”的男女之情（P073），属修辞材料。",
    "教会大公会议与国王御案——作者用以说明解释权转移的机构性对象（P021）。",
    "英王钦定本与莎士比亚作品——作者称二者一起奠定现代英语的根基（P020），属作者的文学史断言，需外部核查。"
   ],
   "conditions": [
    "P001：作者称“如果你有英语基础，对深入的理解这个概念会大有好处”——对读者阅读条件的限定。",
    "P002：明示排除三个版本“无数的小版本差异”，只看“最显然的大局”，本文结论不覆盖版本校勘层面。",
    "P006：作者自述不专精拉丁文，也不主张本文答案为标准答案，明确把词义判断限定为个人理解。",
    "P033：“不喜欢不义”的范围被作者限定为“任何对他人含有恶意、冀望人受损的行为”。",
    "P050：“凡事授信”的时限条件——先当作真实诚实的对待“直到看到事实与此相悖”。",
    "P054：停止投入或停止服务某人可以由其他任何理由触发，唯“绝望”不被允许。",
    "P055：禁止“绝望”结论的理由条件是：人不能预测未来、不能决定历史。",
    "P075：Caritas／慈善的适用不因性别、种族、阶级、意识形态而变——无条件的适用声明。",
    "P078—P079：“神性内核”“最近于神的事”属带有宗教前提的评价性断言，其判据本文未给出。"
   ],
   "rhetoric_and_tone": "注疏式教学口吻，第二人称引导（“带着你们一个词一个词的过一过”）；大量极短判断句与重复收束（“爱没有野心。”“爱不思恶。”“爱以真实为乐。”“爱从不失败。”）；以“记住：”引出训诫式总结；对概念异变有明确的价值叹息（“真正令人叹息的”），结尾转为宗教性庄严表述；同时反复声明个人理解的限度，并以反问（“这是‘病人’吗？”）推进词义辨析。",
   "unresolved_questions": [
    "三版“无数的小版本差异”被作者明示排除，本文未说明所据版本（武加大译本的具体校勘本、KJV 是否 1611 年版、和合本版本等）。",
    "作者自述不专精拉丁文，patiens／ambitiosa／credit／sustinet 等词义判断属个人理解，需古典学与圣经学外部核查（P006）。",
    "P019—P020 关于武加大译本抄写方式、英王钦定本读者定位、“与莎士比亚一起奠定现代英语根基”“导致原意被英语文化语境迁移”等历史断言，本文未给依据，需外部核查。",
    "P066 所列 love 词源串（lubo / Liubi / Lieber / lob / lof / liob / lien）未注出处，需词源学核查。",
    "P042 称中文译者“很显然……意识得到”直译会造成信仰障碍，是对译者动机的推测，本文未给证据。",
    "引文未标注具体书卷章节与节号；正文段落前的 5、6、7、8 等数字疑为节号，本文未说明。",
    "三语/双语对照在阅读包中按行合并为单段（如 P007、P012、P013、P015），个别处句读与语种归属依赖原排版，存在歧义。",
    "“爱是神性内核”“最近于神的事”等表述以宗教前提为据，本文未界定其判据，亦未回应非信仰读者的可能质疑。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P003", "quote": "不是一个本来直接存在于东亚文化里的原生概念", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P006", "quote": "我并不专精拉丁文，也并不主张你们以这里的答案为标准答案", "relation": "qualifies"},
    {"key": "E3", "paragraph_id": "P007", "quote": "Caritas patiens est, benigna est.", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P008", "quote": "这是耐心。专指忍耐痛苦的耐心。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P020", "quote": "它导致圣经的原意被英语文化的语境迁移了", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P021", "quote": "将原文的解释权轻轻巧巧的从教会的大公会议上转移到了国王御案上", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P030", "quote": "爱不思恶。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P033", "quote": "实际上是指不喜欢任何对ta人含有恶意、冀望人受损的行为。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P036", "quote": "爱之中根植了“事实自身永远是善”的价值观。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P042", "quote": "这其实应该译作“凡事忍受”。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P043", "quote": "但其实在拉丁文中其实就是“忍饥挨饿”那样性质的忍受。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P047", "quote": "就我个人理解，credit不是“相信”，而是“授信”。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P049", "quote": "没有这种“对怀疑的免疫力”，是不成其为believe的，只可以称为credit。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P050", "quote": "实际上应该译为“凡事授信”", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P055", "quote": "没有逻辑上有效的能力来做出“绝望”的结论。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P066", "quote": "它是指向“快乐的情绪”，指“使人快乐”。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P067", "quote": "是“爱”这个概念的一次至关重要的异变。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P071", "quote": "爱不是“love”，爱是caritas，爱是慈善。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P072", "quote": "一种行为，若不是慈善，则不成其为爱。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P073", "quote": "爱不是你侬我侬，耳鬓厮磨，缠绵悱恻", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P075", "quote": "Caritas / 慈善，无虑性别，无虑种族、无虑阶级、无虑意识形态。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P078", "quote": "爱是人类借以穿透一切兽性、消解一切恶念，最终战胜一切罪恶的神性内核。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P002", "quote": "这三个版本本身有无数的小版本差异，我们这里不去打这个口舌官司，只看最显然的大局。", "relation": "context"},
    {"key": "E24", "paragraph_id": "P054", "quote": "但这不可以是因为“绝望”。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P065", "quote": "都没有将这里的“爱”对应为Love，而是caritas，charity。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P035", "quote": "无论一个幻觉让你如何享受，一个事实让你如何折磨", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P032", "quote": "iniquity 敌意的行为、恶意的行为", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P019", "quote": "拉丁文版是由修士一天祈祷几个小时", "relation": "context"},
    {"key": "E29", "paragraph_id": "P005", "quote": "这个拉丁文版本，是基督教被立为罗马国教后确立的正典版本。", "relation": "context"},
    {"key": "E30", "paragraph_id": "P029", "quote": "爱不想象恶，不向恶思索，爱不以恶意揣测人。", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P068", "quote": "真正令人叹息的，是“欲使人快乐的东西”并不能使人快乐。", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P076", "quote": "它不自夸，不膨胀，无野心，不想象恶，甘愿受苦，信奉真理，凡事授信，永不绝望。", "relation": "supports"},
    {"key": "E33", "paragraph_id": "P079", "quote": "是人所能行最近于神的事。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["宗教文本与翻译", "语义与词源", "伦理学（爱/慈善）", "文化史与概念史"],
   "issue_candidates": ["爱的定义", "caritas 与 love 的对译", "圣经翻译史与英王钦定本", "概念跨语言迁移", "中文译本的意译取向"],
   "text_function_candidates": ["答疑", "词义疏解/注疏", "论辩", "训诫式总结"],
   "object_candidates": ["圣经（拉丁文版、英王钦定本、中文和合本）", "教会大公会议", "英王/詹姆士王", "盎格鲁-撒克逊语", "中文圣经译者"],
   "working_keywords": ["caritas", "charity", "love", "patiens", "ambitiosa", "credit/授信", "believe", "sustinet", "numquam excidit", "慈善", "爱"]
  },
  "notes": "知乎答题（question 444126370）。正文含拉丁文/英文/中文逐词对照与经文引文，均属原文结构；无图片节点，故不涉图像核验。作者在 P006 明确声明不专精拉丁文、不主张标准答案，本记录据此把其词义判断记为作者个人理解（C002、C011 标 author_qualified）而非定论；其历史与词源断言（P019、P020、P066）已登记为待外部核查。无平台话题标签混入正文。"
 },
 "ecfc1be7": {
  "analysis": {
   "question_context": "提问者（Q001）问“穷人怎么才能翻身？”。作者不直接给致富方法，而是把问题改写为“穷人摆脱贫困的最大的困难在哪里”，依次列出并处理三大障碍（学识劣势、心态急功近利、愤世嫉俗），给出应对与禁忌，最后重新界定“穷”本身：财富分层，私产只是撬动公共财富的撬棒，穷的要害首先在观念与知识，而不是账户余额。提问者只有一句提问，未表达立场。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004"], "summary": "改写问题为“最大的困难在哪里”；先说贫穷不一定是劣势：有强烈脱贫动力者在雇主眼里是加分项，但该优势以“其他方面一样”为条件，翻身的关键是找出并处理抵消优势的差异。", "role": "context"},
    {"unit_id": "U002", "paragraph_refs": ["P005", "P006", "P007", "P008", "P009", "P010", "P011"], "summary": "障碍一（学识）：富家子弟教育资源更多但非必然；穷人专注数理化基本功或手艺、保持求知饥渴可抵消知识存量差距；重要的是热爱学习而非现在会多少；穷加上饥渴好学反成优势。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P012", "P013", "P014", "P015", "P016"], "summary": "障碍二（急功近利）：在意报酬可理解，但若影响努力与表现即无可辩解；雇主预先有此顾虑并拿放大镜找迹象，如对富贵子弟预设不努力一样，因敏感注意而加倍容易证实。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P017", "P018", "P019", "P020", "P021", "P022", "P023", "P024"], "summary": "言行建议：不满可用脚投票或辞职，但绝不说“老板画大饼”“我只是想赚钱”之类的话；拱火者可能告密，两人以上听到即“证实即处决”；就算老板真画大饼，抱怨对自己也无正面意义。", "role": "action_advice"},
    {"unit_id": "U005", "paragraph_refs": ["P025", "P026", "P027", "P028", "P029", "P030", "P031"], "summary": "反证“反大饼政策”不可落实：几乎总会不满薪水、几乎无法预判老板；跳槽仍遇到谈前景的老板，换到第三四个就没人愿意伺候你；一起吐槽的“兄弟”早已不在。", "role": "rebuttal"},
    {"unit_id": "U006", "paragraph_refs": ["P032", "P033", "P034", "P035", "P036", "P037", "P038", "P039"], "summary": "障碍三（愤世嫉俗）：定义为对社会秩序不满、仇恨一切既得利益者；作者设“既得利益者是不是贬义词”的闪念测试，并主张该词只是显而易见的中性描述。", "role": "claim"},
    {"unit_id": "U007", "paragraph_refs": ["P040", "P041", "P042", "P043", "P044", "P045", "P046", "P047", "P048", "P049"], "summary": "后果链：不承认现状的正义性 → 对你的服从性没有期待 → 不信你会积极执行 → 认为配合只是屈从、努力只是表演 → 不交有影响的事给你 → 被视为“不够可靠的次要补充人力”，最终成为最优先裁员候选。", "role": "claim"},
    {"unit_id": "U008", "paragraph_refs": ["P050", "P051", "P052", "P053", "P054"], "summary": "补充机制与结局：决策者未必意识到；有意为之太残忍而难以长期承受；可能出现要求提高热情的谈话，多以离职收场并再付沉没成本，但仍好过三十五岁被裁员。", "role": "reason"},
    {"unit_id": "U009", "paragraph_refs": ["P055", "P056", "P057", "P058", "P059", "P060", "P061", "P062"], "summary": "建议：消除“对现实正义的愤怒”——这是富家子弟的特权，越穷后果越重；作者称这是冰冷的规律、zzzq无意义；想得通即超脱，想不通就控制住不表现，控制一分有一分好处。", "role": "action_advice"},
    {"unit_id": "U010", "paragraph_refs": ["P063", "P064", "P065", "P066", "P067", "P068", "P069", "P070", "P071", "P072", "P073", "P074", "P075", "P076"], "summary": "重新界定“穷”：财富分层，私产只是一部分，你还共有军队、司法、治安、教育、健康等公共财产；以中国军费、教育经费、公共总支出与建国七十年的积累为据，称折算后这才是最大份额。", "role": "claim"},
    {"unit_id": "U011", "paragraph_refs": ["P077", "P078", "P079", "P080", "P081", "P082", "P083", "P084"], "summary": "此外还共有人类共有财富（牛顿第一定律、二十四史、空气、地球、太阳），皆为无价之宝，折算价值远胜账户余额那点毛毛雨。", "role": "claim"},
    {"unit_id": "U012", "paragraph_refs": ["P085", "P086", "P087", "P088", "P089", "P090"], "summary": "解释贫困感的来源：私产影响你获取共同财产的实际份额（没钱买高铁票、交不起补贴后的医疗费）；私产的真正作用是撬动公共财富的撬棒与铁锹，而非换酒换火锅。", "role": "claim"},
    {"unit_id": "U013", "paragraph_refs": ["P091", "P092", "P093", "P094", "P095", "P096", "P097", "P098", "P099"], "summary": "收束：被动的公共财富总是自动享有，用得多勤多巧也影响份额；穷的要害不在财富本身或私产多寡，而在基本观念与知识、对社会的认识与利用能力；不知其存在或拿不到，有一个亿也还是穷。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称贫穷不一定是劣势：受过贫苦而有强烈脱贫动力者，在很多雇主眼里是加分项，同薪资对穷人驱动力更强。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "作者把雇主优先雇佣经济状况更差者限定在“如果有可能，而且其他方面一样”的条件下。", "evidence": ["E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称“穷人翻身”的关键是找到妨碍根本优势发挥的“不一样”的地方，明智应对、扬长避短。", "evidence": ["E4", "E5"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "作者称教育资源的差距并非必然；专注数理化基本功或手艺、保持求知饥渴，可在很大程度上抵消富家子弟的知识存量优势。", "evidence": ["E6", "E7"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称重要的是热爱知识与学习而非现在会多少；专业人眼里新人本来都要从头教起，穷加上饥渴好学、刻苦钻研反被视为优势，缺陷都会被忽略。", "evidence": ["E8", "E9", "E10"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称急功近利可以理解，但若影响努力提高的动力与工作表现，则多可理解、多可原谅都无意义。", "evidence": ["E11"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称雇主对穷人预先有急功近利的顾虑并拿放大镜找迹象，如同对富贵子弟预设不努力，因格外敏感而加倍容易证实。", "evidence": ["E12", "E13"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者建议：可以心里想、可以直接辞职，但绝对不要说出“老板只是画大饼骗我们出力”“我只是想赚钱”“给钱最实在”这类话。", "evidence": ["E14"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作者称拱你火、勾引你“共鸣”的人，转眼就可能出卖这些消息给老板。", "evidence": ["E15"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称话被同事听到（尤其两人以上）职业生命就交到对方手里；极少有老板能宽容有此念头的人，“证实即处决”。", "evidence": ["E16", "E17"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称就算老板真在画大饼，指责抱怨也不会让ta改变做法，对自己没有任何正面意义。", "evidence": ["E18"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "作者称你几乎总对薪水不满、几乎无法在入职前判断老板，故“反大饼政策”无法落实；跳槽也换不到不谈前景的老板。", "evidence": ["E19", "E20", "E21"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者把愤世嫉俗定义为对社会秩序不满、仇恨一切既得利益者，并以“既得利益者”是否被第一闪念当作贬义词作自我测试。", "evidence": ["E22", "E23", "E24"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称“既得利益者”只是显而易见的中性描述，不含一丝利益不正当之意；把它当贬义词说明你不承认现状的正义性与基本合理性。", "evidence": ["E25", "E26"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作者推演：这会使看出这一点的人对你的服从性没有期待，不信你会真正积极执行命令，只当你的配合是屈从。", "evidence": ["E27", "E28"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作者称其后果是隐形的诅咒：努力被当成表演，永远被当作“不够可靠的次要补充人力”，最终成为“没啥功劳，只有苦劳”的最优先裁员候选。", "evidence": ["E29", "E30"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "作者称这些并不需要决策者明确意识到，因为带着显意识这样对待一个人显然是残忍的，多数人不能长期承受这种心理压力。", "evidence": ["E31", "E32"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者建议消除“对现实正义的愤怒”，称这是富家子弟的“特权”；越穷苦出身，被认定愤世嫉俗的后果越沉重。", "evidence": ["E33", "E34"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称这是赤裸裸的、冰冷的事实运行规律，zzzq毫无意义；暴露愤恨就基本注定倒霉，换了你自己决策也会一模一样地处理。", "evidence": ["E35", "E36", "E37"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称这是穷人翻身最大的障碍之一；想得通直接超脱是上上之道，想不通就控制住不表现出来，控制一分有一分的好处。", "evidence": ["E38", "E39"]},
    {"claim_id": "C021", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称人的财富是分层的，私产只是一部分；现代军队、司法、治安、教育、健康中有大量古人花钱也买不到的服务和资源，现在免费给你。", "evidence": ["E40", "E41"]},
    {"claim_id": "C022", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以中国军费、教育经费与建国七十年的积累为据，称每个公民都分得这些公共利益，折算成金额是最大的财富份额，约等于一份价值不知多少万一年的会员资格。", "evidence": ["E42", "E43", "E44", "E45"]},
    {"claim_id": "C023", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称还共有人类共有财富（牛顿第一定律、二十四史、空气、地球、太阳），其折算价值远胜银行账户余额那点毛毛雨。", "evidence": ["E46"]},
    {"claim_id": "C024", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称私产会影响你获取共同财产的实际份额（没钱买高铁票、交不起补贴后的医疗费）。", "evidence": ["E47", "E48"]},
    {"claim_id": "C025", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称私产的真正作用是撬动公共财富的撬棒与挖掘公共财富的铁锹，而不是拿来喝酒吃火锅。", "evidence": ["E49", "E50"]},
    {"claim_id": "C026", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称穷真正的要害不在拥有财富本身或私产多寡，而首先在基本观念与知识、对社会的认识能力和利用技巧上：有一个亿而不知其存在或拿不到，还是穷。", "evidence": ["E51", "E52", "E53", "E54"]}
   ],
   "argument_steps": [
    "把提问改写成“最大的困难在哪里”，先立反直觉前提：有脱贫动力的贫穷对雇主是加分项（P001—P003）。",
    "限定该优势的条件“其他方面一样”，据此把翻身的关键定义为处理抵消优势的差异（P004）。",
    "障碍一（学识）：承认富家子弟教育优势但称非必然，给出以基本功、手艺、求知饥渴抵消的对策，并把热爱学习立为决定因素（P005—P011）。",
    "障碍二（急功近利）：承认在意报酬可理解，以“影响努力与表现”为界取消其可原谅性，并用雇主的放大镜机制说明风险（P012—P016）。",
    "给出言行禁忌：可辞职、不可抱怨老板画大饼；以告密风险与“证实即处决”作后果论（P017—P024）。",
    "以反问反驳“反大饼政策”的可落实性：无法预判老板、跳槽同样遇谈前景者、频繁跳槽耗尽职业前十年（P025—P031）。",
    "障碍三（愤世嫉俗）：先定义，再以“既得利益者是不是贬义词”的闪念测试让读者自判（P032—P039）。",
    "由测试结果推出“不承认现状正义性”，再逐级推出服从性无期待、不给重要任务、努力被读成表演、最优先裁员（P040—P049）。",
    "补充机制：该过程多为无意识，有意识的残忍难以长期承受；沟通失败以离职收场，但仍好过三十五岁被裁员（P050—P054）。",
    "规范性建议：消除愤怒是富家子弟的特权，越穷后果越重；称这是冰冷规律，想不通就隐藏（P055—P062）。",
    "转入重新定义“穷”：财富分层，私产之外还有公共财产与人类共有财富，并以财政数字说明其价值（P063—P084）。",
    "解释贫困感来源：私产决定你能撬动多少公共财富，私产的工具意义是撬棒与铁锹（P085—P090）。",
    "收束：决定穷不穷的是观念、知识与利用技巧，不知其存在或拿不到都仍是穷（P091—P099）。"
   ],
   "concept_usage": [
    {"term": "贫穷/穷", "meaning": "兼指两种：有强烈脱贫动力的贫苦处境（对雇主是加分项），与文末界定的“不知道或拿不到本可享有的公共财富”。", "evidence": "P003、P093、P098", "ambiguity": "同一“穷”字兼指经济状况与认知/利用能力，作者未作术语区分。"},
    {"term": "翻身", "meaning": "沿用提问者说法，被具体化为“找到妨碍根本优势发挥的差异并扬长避短”。", "evidence": "P004", "ambiguity": "未界定翻身的目标状态。"},
    {"term": "加分项", "meaning": "雇主评价中的优势项：同薪资对穷人驱动力更强，条件相同时更愿雇佣。", "evidence": "P003", "ambiguity": "以雇主视角立论，未给雇佣数据。"},
    {"term": "急功近利", "meaning": "非常在意报酬，并因此影响努力提高的动力与工作表现。", "evidence": "P013", "ambiguity": "未给出判定“影响工作表现”的标准。"},
    {"term": "画大饼", "meaning": "老板谈成长、谈远景而不兑现的说法（文中引号标出的口语）。", "evidence": "P018、P023", "ambiguity": "作者既承认可能真在画大饼又主张不要说，未区分真假情形。"},
    {"term": "职业死刑/死缓", "meaning": "被老板视为不可宽容者后在该处职业前途终结的口语化比喻。", "evidence": "P020、P023", "ambiguity": "比喻性表述，无制度含义。"},
    {"term": "愤世嫉俗", "meaning": "对社会秩序不满、仇恨一切既得利益者；判定用“既得利益者是否被当作贬义词”的闪念测试。", "evidence": "P033、P037", "ambiguity": "以单次闪念作判据，未讨论误判。"},
    {"term": "既得利益者", "meaning": "作者主张其为“显而易见的中性描述”，不代表所得利益不正当。", "evidence": "P038", "ambiguity": "以语文判断替代词典/语料证据，未讨论实际语用中的贬义化。"},
    {"term": "服从性", "meaning": "被期待的执行意愿：对方是否相信你会真正积极地执行命令。", "evidence": "P042、P043", "ambiguity": "无。"},
    {"term": "私有财产 vs 公共财产/共同财产", "meaning": "财富分层的两类：私产是账户与可变卖实物；公共财产是军队、司法、治安、教育、健康等免费服务；私产是撬动公共财富的工具。", "evidence": "P064、P066、P089", "ambiguity": "未说明公共财富份额的分配机制。"},
    {"term": "撬棒/铁锹", "meaning": "私产的功能性比喻：撬动公共财富、挖掘公共财富矿藏。", "evidence": "P089、P092", "ambiguity": "无。"},
    {"term": "zzzq", "meaning": "按上下文指“政治正确”；作者称其在此毫无意义。", "evidence": "P057", "ambiguity": "正文未展开该缩写，含义依上下文推断。"}
   ],
   "examples_and_targets": [
    "雇主/老板——作者立论的判据来源与读者行为的承受方（P003、P014、P020、P023）。",
    "富贵子弟/富家子弟——对比群体：作者称雇主同样预设他们不努力、不上心，并以“纨绔子弟拿工作当过家家”说明放大镜效应（P015）；又称“对现实正义的愤怒”是富家子弟的特权（P055）。",
    "数理化基本功与基本手艺——作者给出的抵消知识存量差距的对策（P008）。",
    "辞职、用脚投票、跳槽换下一家——作者允许的行为（P018、P024）。",
    "工余聚餐里大谈抱怨、勾引你“共鸣”的人——作者描绘的告密风险角色（P019、P021）。",
    "“三十五岁被忍痛裁员”——作者用作比较基准的职场说法（P054），属修辞材料，未给出数据。",
    "“既得利益者是不是贬义词”的小测试——作者自设的自我诊断工具（P034—P039）。",
    "中国每年2610亿美元军费、每年46000亿人民币教育经费、每年几百亿医疗保障经费、每年二十万亿级别的公共总支出、建国七十年——作者用以证明公共财富份额的数据与历史叙述（P067、P068、P069、P075、P076），需外部核查。",
    "牛顿第一定律、二十四史、空气、地球、太阳——作者列举的人类共有财富（P078—P083），属修辞性枚举。",
    "没钱买高铁票、交不起补贴后的医疗费——作者用以说明私产影响公共财富实际份额的例子（P087、P088）。",
    "“你有一个亿，但是不知道它的存在”——作者用以说明穷的判定不看账户余额的假设例（P098）。"
   ],
   "conditions": [
    "P003：雇主的偏好以“如果有可能，而且其他方面一样”为条件，作者随即承认其他方面常常不一样。",
    "P007：“但这并不是必然的”——学识劣势非必然，为其后的对策留出空间。",
    "P008：抵消作用被限定为“在很大程度上”，非完全消除。",
    "P010：判断主体限定为“在专业人眼里”。",
    "P013：急功近利的可原谅性以“如果影响到你努力提高的动力，影响到你的工作表现”为界。",
    "P018：辞职可行以“在现代劳动制度下”为制度前提。",
    "P019—P020：风险条件为被任何同事听到、尤其两人以上听到；“极少有老板能宽容有这个念头的人”为带限定的概括。",
    "P026：以“几乎总是”“几乎没可能”双重限定薪水不满与入职前判断老板。",
    "P030：以“如果你有五六个可以换的话”为条件。",
    "P037：测试的判定条件为“如果你第一闪念就感到这是贬义词”。",
    "P050：明确限定该机制“并不需要做决策的人明确的意识到自己在这样做”。",
    "P056：后果与贫穷程度成正比——越是穷苦出身，被认定愤世嫉俗的后果越沉重。",
    "P059：以“换了你自己做决策”为假设条件。",
    "P067—P076：财政数字与“建国七十年”均以中国为范围，未给出年份口径；P076 以“就算民国留下的资产不计算”作让步条件。",
    "P087—P088：公共财富份额的减损以“如果你没钱买高铁票”“你如果连补贴后的医疗费也交不起”为条件。",
    "P098：以“你有一个亿”为假设情形说明认知条件优先于持有。"
   ],
   "rhetoric_and_tone": "第二人称全程直呼“你”的劝诫/训诫体，兼有威胁性警告与家长式指导；大量反问连发（P025、P027—P029、P040）；口语乃至粗俗用语（“屁都不会”“鬼话”“拱你的火”“这位爷好不好伺候”）；形象比喻（放大镜、职业死刑/死缓、撬棒与铁锹、画大饼）；自设小测试引导读者自我判定；以“我直白点告诉你”“再说一遍”“我实话实说”“我告诉你的是赤裸裸的、冰冷的事实运行规律”强化断言力度；对读者的愤怒与屈从情绪有明确的规训语气，同时偶作让步（“这可以理解”）；结尾改用列举与算账式的说理口吻。使用“ta/ta们”作中性第三人称。",
   "unresolved_questions": [
    "作者身份与经验来源未在正文说明（以“我直白点告诉你”等口吻作断言），其关于雇主心理的概括缺依据。",
    "P067、P068、P069、P075 的财政数字（军费2610亿美元、教育经费46000亿人民币、医疗经费几百亿、公共总支出二十万亿级）未注明年份、统计口径与出处，需外部核查。",
    "P076“建国七十年”与文末更新时间（2023-09-25）不同步，正文数据可能基于更早年份，本文未说明版本或修订情况。",
    "P030“一般换到第三四个，就没人再有兴趣知道你这位爷好不好伺候了”与 P015 的雇主心理描述均为经验断言，无数据或研究支持。",
    "P038 关于“既得利益者”是中性词的判断是作者的语文主张，未引词典或语料证据，也未讨论该词在公共语用中的贬义化。",
    "P037 以“第一闪念”作愤世嫉俗的判定标准，其效度与误判风险本文未讨论。",
    "P057 的“zzzq”未在正文解释，按上下文推断为“政治正确”的拼音缩写，属推断。",
    "作者把私产的作用归纳为“撬动公共财富”，但未说明公共财富的实际分配机制、可及性差异与地区/身份差别。",
    "P052 称“没有自我知觉的小孩子”对谈话的反应“绝大多数都是要么愤愤不平，要么郁郁寡欢”，属对他人心理的概括，无依据。",
    "本篇为建议性长文，未讨论其建议在劳动关系中的法律与伦理边界（如言论后果、告密行为的评价）。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P003", "quote": "这在很多雇主眼里是一个加分项", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P003", "quote": "这是穷人在经济上一个极大的基本优势。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "如果有可能，而且其他方面一样，雇主当然会想要优先雇佣经济状况更差一些的人", "relation": "qualifies"},
    {"key": "E4", "paragraph_id": "P004", "quote": "而所谓“穷人翻身”的关键就是找到这些妨碍自己的根本优势发挥出来的“不一样”的地方", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P004", "quote": "争取扬长避短。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P007", "quote": "但这并不是必然的。", "relation": "qualifies"},
    {"key": "E7", "paragraph_id": "P008", "quote": "就可以在很大程度上抵消富家子弟拥有的知识存量优势。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P009", "quote": "重要的是你有多热爱知识和学习，不是你现在会多少。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P010", "quote": "其实在专业人眼里你们基本都是屁都不会，都要从头教起。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P011", "quote": "你穷，这是加分项", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P013", "quote": "这可以理解，但这如果影响到你努力提高的动力，影响到你的工作表现，那么有多可理解、多可原谅都是无意义的。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P014", "quote": "因为雇主提前就有这种顾虑，随时随地会拿着放大镜去看你有没有这种通病的迹象。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P015", "quote": "因为格外敏感的注意，于是加倍的容易证实。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P018", "quote": "绝对不要对任何人说出所谓“老板只是画大饼骗我们出力”", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P019", "quote": "勾引你“共鸣“的人，转眼间就可能是出卖这些消息给老板的人。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P020", "quote": "你在这里的职业生命实际上就已经交到对方手里捏着了。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P020", "quote": "证实即处决。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P023", "quote": "对你自己不会有任何正面意义。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P026", "quote": "你几乎总是会对薪水不满的", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P027", "quote": "那么你要怎么落实这种“反大饼政策”？", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P030", "quote": "一般换到第三四个，就没人再有兴趣知道你这位爷好不好伺候了。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P033", "quote": "也就是对社会秩序不满，从心底里仇恨一切既得利益者。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P037", "quote": "如果你第一闪念就感到这是贬义词", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P037", "quote": "你已经有愤世嫉俗的倾向。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P038", "quote": "只是一种显而易见的中性描述", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P041", "quote": "这说明你在总体上不承认现状的正义性，不接受现状的基本合理性。", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P042", "quote": "这会导致看出这一点的人对你的服从性没有期待。", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P043", "quote": "对方在心底里并不相信你会真正积极的执行命令。", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P049", "quote": "永远被下意识的当作“不够可靠的次要补充人力”来使用", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P049", "quote": "最优先裁员候选。", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P050", "quote": "并不需要做决策的人明确的意识到自己在这样做", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P051", "quote": "因为带着显意识这样决策，这样故意的去对待一个人，显然是残忍的。", "relation": "supports"},
    {"key": "E33", "paragraph_id": "P055", "quote": "你最好想办法消除你那“对现实正义的愤怒”", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P056", "quote": "越是穷苦出身，被认定愤世嫉俗的后果越沉重。", "relation": "supports"},
    {"key": "E35", "paragraph_id": "P057", "quote": "我告诉你的是赤裸裸的、冰冷的事实运行规律，zzzq在这里没有一丝一毫的意义。", "relation": "supports"},
    {"key": "E36", "paragraph_id": "P058", "quote": "你暴露你的愤恨，你就基本注定倒霉。", "relation": "supports"},
    {"key": "E37", "paragraph_id": "P059", "quote": "换了你自己做决策，你来决定用人，你会一模一样的处理。", "relation": "supports"},
    {"key": "E38", "paragraph_id": "P060", "quote": "事实上，这是穷人翻身最大的障碍之一。", "relation": "supports"},
    {"key": "E39", "paragraph_id": "P062", "quote": "自己控制住不要表现出来，也一样控制一分就有一分的好处。", "relation": "supports"},
    {"key": "E40", "paragraph_id": "P064", "quote": "人的财富是分层的。", "relation": "supports"},
    {"key": "E41", "paragraph_id": "P066", "quote": "这里面有大量古人花钱也买不到的服务和资源，现在是免费给你的。", "relation": "supports"},
    {"key": "E42", "paragraph_id": "P067", "quote": "中国每年2610亿美元军费", "relation": "supports"},
    {"key": "E43", "paragraph_id": "P068", "quote": "每年46000亿人民币的教育经费，你有一份。", "relation": "supports"},
    {"key": "E44", "paragraph_id": "P074", "quote": "你手里已经有个价值不知多少万一年的会员资格。", "relation": "supports"},
    {"key": "E45", "paragraph_id": "P076", "quote": "一个一分钱都没有的中国公民也一样分得了一份积累了七十年的家底。", "relation": "supports"},
    {"key": "E46", "paragraph_id": "P084", "quote": "其折算价值远远胜过你的银行账户余额所能代表的那点毛毛雨。", "relation": "supports"},
    {"key": "E47", "paragraph_id": "P086", "quote": "因为你的私产会影响到你获取这些共同财产的实际份额。", "relation": "supports"},
    {"key": "E48", "paragraph_id": "P087", "quote": "如果你没钱买高铁票，高铁所蕴含的公共利益分到你手里的直接份额就会减少不少。", "relation": "supports"},
    {"key": "E49", "paragraph_id": "P089", "quote": "你自己的私有财产，真正起到的作用是作为撬动公共财富的撬棒，挖掘公共财富矿藏的铁锹。", "relation": "supports"},
    {"key": "E50", "paragraph_id": "P090", "quote": "而不是拿它可以喝多少瓶酒、吃多少次火锅。", "relation": "supports"},
    {"key": "E51", "paragraph_id": "P093", "quote": "穷真正的要害，其实并不在拥有财富本身上", "relation": "supports"},
    {"key": "E52", "paragraph_id": "P093", "quote": "而首先在于一些基本的观念和知识上——在于对社会的认识能力和利用技巧上。", "relation": "supports"},
    {"key": "E53", "paragraph_id": "P098", "quote": "你有一个亿，但是不知道它的存在，你还是穷；知道但是拿不到，也还是穷。", "relation": "supports"},
    {"key": "E54", "paragraph_id": "P099", "quote": "这才是人穷的真正原因。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["职业发展/劳动市场", "社会分层与财富观", "观念与行为规训", "公共财政与公共品"],
   "issue_candidates": ["贫穷的成因", "穷人的职场处境", "雇主对穷人的刻板印象", "抱怨与告密文化", "愤世嫉俗的代价", "公共财富与私有财产", "阶层流动"],
   "text_function_candidates": ["答疑", "经验总结", "行动建议", "训诫/警告", "论辩（反驳“反大饼政策”）", "说理式算账"],
   "object_candidates": ["穷人/穷苦子弟", "富贵子弟", "雇主/老板", "同事/告密者", "既得利益者", "中国（财政数据）"],
   "working_keywords": ["翻身", "加分项", "画大饼", "证实即处决", "愤世嫉俗", "既得利益者", "服从性", "职业死刑", "撬棒", "公共财产", "zzzq"]
  },
  "notes": "知乎答题（question 444003245）。正文为第二人称建议式长文，含口号式短句与粗俗口语，均属原文风格；文中财政数字（P067—P069、P075）与“建国七十年”未注明年份与出处，已登记为待外部核查，本记录不据此判定其真实性。无图片节点，不涉图像核验；正文未见平台话题标签混入。作者以读者群体（“你们”）为对象、以雇主视角立论，本记录按原文把相关判断记为作者主张。"
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
