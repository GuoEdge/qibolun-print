#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""批次 r001-b0001 的初读记录（金标准样例）。

本文件只承载逐篇分析内容；段落定位、字符位置、图片与元数据由 authoring.py
从语料机械生成，避免手写定位。
"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0001"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "out", BATCH + ".out.jsonl")
STARTED = "2026-09-19T23:50:00+08:00"
COMPLETED = "2026-09-20T00:05:00+08:00"

A = {}

A["80c38b2d-3c5b-5fe9-913e-b3324a867a58"] = {
    "analysis": {
        "question_context": "提问者问买菜这件事上北方和南方差别多大、为什么（Q001）。作者先复述他人答案中三种常见解释，判定其不准确，再给出自己的通史性解释。",
        "content_units": [
            {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "复述并否定常见解释（生活智慧、严寒、游牧民族风格影响）。", "role": "rebuttal"},
            {"unit_id": "U002", "paragraph_refs": ["P003"], "summary": "以北方地名“x宁/x镇/x屯/x堡/x卫”推断东北长期以军屯军镇为行政形态、坞屯堡寨为聚居方式。", "role": "reason"},
            {"unit_id": "U003", "paragraph_refs": ["P004"], "summary": "提出北方汉族饮食实为军食、伙食，并以“伙”系词汇作为文化遗留证据。", "role": "claim"},
            {"unit_id": "U004", "paragraph_refs": ["P005", "P006", "P007", "P008"], "summary": "由军需供给条件顺推北方饮食的若干特点：大锅大批量加工、饭菜一体、干粮倾向、剩食回收、可囤积食材、调味偏咸。", "role": "reason"},
            {"unit_id": "U005", "paragraph_refs": ["P009", "P010"], "summary": "结论：东北饮食传承古代军食风格，非生活智慧；预测现代供应体系会削弱南北差异；买菜习惯是军队采购习惯的延伸。", "role": "conclusion"},
            {"unit_id": "U006", "paragraph_refs": ["P011"], "summary": "以“欢迎探讨”结束，语气开放。", "role": "transition"},
        ],
        "main_claims": [
            {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为把北方饭食特点归结为“生活智慧”“因为严寒”“游牧民族风格影响”是不准确的。", "evidence": ["E1"]},
            {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以北方“x宁/x镇/x屯/x堡/x卫”地名推断该地区长期以军屯军镇为主要行政形态、以坞屯堡寨为主要聚居方式，军事化生活人口占压倒性优势。", "evidence": ["E2"]},
            {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张北方汉族饮食实为军食、伙食，并以“伙食/伙长/伙伴/伙夫”等词为该基层军事单位的文化遗留。", "evidence": ["E3"]},
            {"claim_id": "C004", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "作者以“依这个假设顺推”为条件，由军需供给条件推出北方饮食的大锅大批量加工、饭菜一体、干粮倾向、剩食回收、可囤积食材、调味偏咸等特点。", "evidence": ["E4"]},
            {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作者预测现代供应体系消除供应限制后，中国北方餐饮会向南方靠拢，以少量多样、精细和质量为主导。", "evidence": ["E5"]},
            {"claim_id": "C006", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "作者以“以我的拙见”限定地认为整个东北地区饮食习惯传承古代军食风格，由军事需要和有限行政能力塑造。", "evidence": ["E6"]},
        ],
        "argument_steps": [
            "先复述并否定既有解释（P001-P002）。",
            "用地名构词指出军屯军镇、坞屯堡寨的长期聚居形态（P003）。",
            "据此提出“北方汉族饮食实为军食”的线索性判断，并用“伙”系词汇佐证（P004）。",
            "以“假设顺推”的方式，把军队大批量加工、燃料与调味品供应限制、储运条件逐项对应到具体饮食习惯（P005-P008）。",
            "由此收束为通史性结论，并对现代供应体系下的变化作预测（P009-P010）。",
        ],
        "concept_usage": [
            {"term": "军食/伙食", "meaning": "由军队基层餐饮单位和军需供给条件塑造的饮食形态；作者用“伙”系词汇说明其来源。", "evidence": "P004", "ambiguity": "“伙”系词汇与军事单位的关系由作者直接断言，本文未给出文献出处。"},
            {"term": "供应限制", "meaning": "燃料收集、调味品供应、储存与运输等条件对烹饪方式的约束。", "evidence": "P005-P008", "ambiguity": "未量化，也未区分不同时期与地区的差异。"},
            {"term": "买菜的习惯", "meaning": "作者称其为军队采购习惯的延伸，并认为这种差别正在消亡。", "evidence": "P010", "ambiguity": "未展开论证采购习惯与军队供给制度的对应关系。"},
        ],
        "examples_and_targets": [
            "反驳对象：把北方饮食归因于生活智慧、严寒、游牧民族风格影响的“大多数答案”（P001）。",
            "证据性材料：北方“x宁/x镇/x屯/x堡/x卫”地名（P003）；“伙”系词汇（P004）；大锅菜、大饼卷大葱、食堂剩菜、盐专卖（P005-P008）。",
            "类比/修辞材料：大饼即餐具、手即食具、一个锅里搅马勺（P005）。",
        ],
        "conditions": [
            "“依这个假设顺推”（P005）明示后续推理依赖前文假设。",
            "作者把军事化聚居状态限定为“几乎贯穿两千年东北文明史——仅以最近的一百年除外”（P003）。",
            "作者以“以我的拙见”限制结论的确定性（P009）。",
            "预测部分以现代供应体系已消除供应限制为前提（P009）。",
        ],
        "rhetoric_and_tone": "答疑式论述，第一人称“我”出现于“以我的拙见”；以反问“有没有注意到”引导读者；夹杂口语化调侃（“人能用啥三件套”）；条目编号自 1）跳至 5）6）7），本文未说明 4）是否存在；末句“欢迎探讨”呈开放讨论姿态。",
        "unresolved_questions": [
            "编号 1）2）3）之后直接跳到 5）6）7），第 4）条在本文缺失，原因未说明。",
            "正文末尾“社科答集”为平台话题标签，出现在 text 中但不在 lexical 结构内，属于编辑/平台附加文本，作者归属待核。",
            "“伙”系词汇源自军事单位的说法需要外部文献核查（待外部核查）。",
            "作者未说明军队供给条件与具体菜式之间是否存在反例。",
        ],
        "evidence": [
            {"key": "E1", "paragraph_id": "P001", "quote": "大多数答案都把北方饭食的特点归结于“生活智慧”“因为严寒”“游牧民族风格影响”", "relation": "supports"},
            {"key": "E2", "paragraph_id": "P003", "quote": "向来是以军屯军镇为主要行政形态、以坞屯堡寨为主要聚居方式的", "relation": "supports"},
            {"key": "E3", "paragraph_id": "P004", "quote": "北方汉族饮食实为军食、伙食", "relation": "supports"},
            {"key": "E4", "paragraph_id": "P005", "quote": "依这个假设顺推，北方饮食的特点也就顺理成章了", "relation": "qualifies"},
            {"key": "E5", "paragraph_id": "P009", "quote": "中国北方的餐饮习惯也会开始向南方靠拢", "relation": "supports"},
            {"key": "E6", "paragraph_id": "P009", "quote": "所以以我的拙见，实际上整个东北地区的饮食习惯，传承着绵延千年的古代军食风格", "relation": "qualifies"},
        ],
    },
    "provisional_tags": {
        "domain_candidates": ["饮食史", "军事史", "区域文化"],
        "issue_candidates": ["南北饮食差异成因", "军屯制度与饮食", "饮食词汇来源"],
        "text_function_candidates": ["答疑", "论辩", "历史解释"],
        "object_candidates": ["东北地区", "北方汉族", "军屯军镇", "坞屯堡寨"],
        "working_keywords": ["军食", "伙食", "军屯军镇", "坞屯堡寨", "大锅菜", "盐专卖"],
    },
}

A["8c4f866e-8ef9-547c-af60-ada5792bb1f3"] = {
    "analysis": {
        "question_context": "提问者问人类是否拥有最强耐力（Q001）。作者针对“上面的评论”所述人类靠奔跑追死猎物的说法，逐条列出误解并给出反证，最后给出自己的结论。",
        "content_units": [
            {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "点出被反驳的说法：人类耐力最强源于在草原上“追死猎物”，并称其中误解很多、前提被遗忘。", "role": "rebuttal"},
            {"unit_id": "U002", "paragraph_refs": ["P003"], "summary": "误解一：人类追逐的是健康动物；作者称人类先打伤动物再“追逐”。", "role": "rebuttal"},
            {"unit_id": "U003", "paragraph_refs": ["P004"], "summary": "误解二：把“追逐”理解为竞速；作者称人类靠足迹与血迹追踪，速度几乎无价值。", "role": "rebuttal"},
            {"unit_id": "U004", "paragraph_refs": ["P005", "P006"], "summary": "误解三：认为人类有充足补给；作者以布须曼人无水具、干粮制作晚于农耕为由反驳。", "role": "rebuttal"},
            {"unit_id": "U005", "paragraph_refs": ["P007"], "summary": "以狩猎采集时代生活优渥、技术停滞为背景，说明水具与干粮不在石器时代画面中。", "role": "reason"},
            {"unit_id": "U006", "paragraph_refs": ["P008", "P009", "P010", "P011"], "summary": "提出“入不敷出”的额外问题：能量投入、失败代价、需结伴、搬运与切割难题、劳动力负担。", "role": "reason"},
            {"unit_id": "U007", "paragraph_refs": ["P012", "P013"], "summary": "回应“绕圈追逐”的反驳，认为在平地绕圈追上猎物不成立。", "role": "rebuttal"},
            {"unit_id": "U008", "paragraph_refs": ["P014", "P015", "P016"], "summary": "强调野生食草动物会对抗甚至主动攻击，人类正面交锋未必占优。", "role": "reason"},
            {"unit_id": "U009", "paragraph_refs": ["P017", "P018"], "summary": "结论：石器时代人类没有超常耐力，生理上不胜过动物，靠伏击与追踪胜过受伤的普通动物。", "role": "conclusion"},
            {"unit_id": "U010", "paragraph_refs": ["P019", "P020", "P021"], "summary": "文末“科学答集”标签与一句延伸评论（“这个很说明问题了，基本全中”）及反问句。", "role": "other"},
        ],
        "main_claims": [
            {"claim_id": "C001", "claim_type": "opponent_view", "attribution": "opponent", "modality": "asserted", "statement": "被反驳的说法：人类耐力最强，因为在草原上可以“追死猎物”，且该战术“战无不胜”。", "evidence": ["E1"]},
            {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称人类几乎从不追逐无伤无损的动物，总是先用石块、骨棒、弓箭、手斧等打伤动物才开始“追逐”。", "evidence": ["E2"]},
            {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称人类很少进行竞速追逐，而是依据足迹、折断枝叶、毛发与血迹追踪，速度在此几乎无价值。", "evidence": ["E3"]},
            {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者举布须曼人没有携带水器具、靠识别与挖掘含水植物块根解决水分代谢，否证“人类靠补给耗死猎物”。", "evidence": ["E4"]},
            {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称“制作干粮”远没有一般想象古老，几乎已是农耕文明之后的产物，距今不过几千年。", "evidence": ["E5"]},
            {"claim_id": "C006", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "作者以“假设这些都不是问题”为让步条件，仍指出成年劳动力稀缺与抚养负担使耐力狩猎难以供养家族。", "evidence": ["E6"]},
            {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者认为“人类追逐羚羊是跑一个大圆圈”的反驳不成立，因为绕圈追逐需在内圈以更快速度跑更长距离。", "evidence": ["E7"]},
            {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称石器时代人类没有超常耐力，因为基本用不着，付出代价维持无用能力意味着竞争劣势。", "evidence": ["E8"]},
            {"claim_id": "C009", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者以“应该”表述：人类在生理上无法胜过动物，甚至不如平庸动物，只是借伏击（尤其投掷和远程射击）与足迹追踪能力胜过受了伤的普通动物。", "evidence": ["E9"]},
            {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者以反问“21世纪了，真的还有非洲部落靠跑死动物狩猎吗？”质疑该说法的现实依据。", "evidence": ["E10"]},
        ],
        "argument_steps": [
            "先复述被反驳的评论观点（P001）。",
            "拆出三个“误解”并逐条反证：追健康动物、竞速追逐、携带补给（P003-P006）。",
            "补充石器时代生活与技术背景，说明水具与干粮不成立（P007）。",
            "再以成本收益（能量投入、失败代价、结伴、搬运、切割、劳动力负担）论证耐力狩猎入不敷出（P008-P011）。",
            "预先回应绕圈追逐的反驳（P012-P013）。",
            "指出食草动物的对抗能力，否定人类正面交锋的优势（P014-P016）。",
            "收束为石器时代人类无超常耐力、靠伏击与追踪的结论（P017-P018）。",
        ],
        "concept_usage": [
            {"term": "追逐/耐力狩猎", "meaning": "被作者区分为“竞速追赶”和“沿踪迹追踪”两件事；作者只承认后者，并称前者几乎不被使用。", "evidence": "P004", "ambiguity": "作者未给出“耐力狩猎”在学术讨论中的通行定义。"},
            {"term": "误解", "meaning": "作者对被反驳评论中若干前提的称呼，共列出三条。", "evidence": "P003-P005", "ambiguity": "误解的提出者被笼统称为“上面的评论”，未指名。"},
            {"term": "入不敷出", "meaning": "作者用来概括耐力狩猎在能量、人力、搬运与加工上的收支失衡。", "evidence": "P008", "ambiguity": "未给出定量估算。"},
        ],
        "examples_and_targets": [
            "反驳对象：认为人类耐力最强、可“追死猎物”的“上面的评论”（P001）。",
            "证据性材料：非洲布须曼人无携水器具（P005）；原始部落就地饱餐并弃置多余猎物（P006）；投掷手斧淘汰耐力捕猎的推论（P010）；成年男子与1.5名成年女子、四名幼童、0.25名老年成员的负担估算（P011）。",
            "类比：狮子追逐羚羊的场面想象（P004）；弓猎射中后等待半小时（P004）。",
            "修辞材料：反问句“你们真的确信羚羊、角马就是这么软弱的善类，由的你们这些废柴随意追逐吗？”（P014）",
        ],
        "conditions": [
            "作者把讨论对象限定为“石器时代的人类”（P017）。",
            "论证中多次使用“几乎”“很少——或者干脆并不——”“大概率”等限定词（P003、P004、P005）。",
            "第 P011 段以“现在我们假设这些都不是问题”设定让步条件再继续论证。",
            "“人类在生理上应该无法胜过动物”用“应该”表示推测（P018）。",
            "关于“习得”与考古证据的限制，本篇未展开。",
        ],
        "rhetoric_and_tone": "辩论式驳论，直接以“误解一/二/三”编号；语气强硬带嘲讽（“蠢到灭绝了”“废柴”）；大量使用反问；夹入具体场景想象与估算数字增强说服力；文末“科学答集”为平台话题标签，其后语句为作者补充评论。",
        "unresolved_questions": [
            "被反驳的“上面的评论”具体文本与作者未在本文中给出。",
            "“误解”三条是否为对方原话的准确概括，无法从本文确认。",
            "“人类几乎从不追逐无伤无损的动物”等断言未给出来源，需外部核查（待外部核查）。",
            "P019“科学答集”属平台标签，出现在 text 中但不在 lexical 结构内；P019、P021 未被 lexical 覆盖，属编辑性拼接，作者归属待核。",
        ],
        "evidence": [
            {"key": "E1", "paragraph_id": "P001", "quote": "上面的评论认为人类耐力最强无非是因为当年误以为人类在草原上可以“追死猎物”", "relation": "context"},
            {"key": "E2", "paragraph_id": "P003", "quote": "人类总是先用石块、骨棒、弓箭、手斧之类先打伤动物才开始“追逐”", "relation": "supports"},
            {"key": "E3", "paragraph_id": "P004", "quote": "而仅仅是根据足迹、折断的枝叶，挂落的毛发，以及滴落的血迹去追踪", "relation": "supports"},
            {"key": "E4", "paragraph_id": "P005", "quote": "至少近现代的非洲布须曼人是没有携带水的器具的", "relation": "supports"},
            {"key": "E5", "paragraph_id": "P006", "quote": "“制作干粮”这一科技成就远没有一般想象的那么古老", "relation": "supports"},
            {"key": "E6", "paragraph_id": "P011", "quote": "现在我们假设这些都不是问题", "relation": "qualifies"},
            {"key": "E7", "paragraph_id": "P013", "quote": "因为追逐者跑的是外圈", "relation": "supports"},
            {"key": "E8", "paragraph_id": "P017", "quote": "石器时代的人类并没有什么大不了的超常耐力", "relation": "supports"},
            {"key": "E9", "paragraph_id": "P018", "quote": "人类在生理上应该无法胜过动物", "relation": "qualifies"},
            {"key": "E10", "paragraph_id": "P021", "quote": "21世纪了，真的还有非洲部落靠跑死动物狩猎吗？", "relation": "supports"},
        ],
    },
    "provisional_tags": {
        "domain_candidates": ["人类学", "进化生物学", "狩猎采集生计"],
        "issue_candidates": ["人类耐力是否最强", "耐力狩猎假说", "石器时代技术与补给"],
        "text_function_candidates": ["答疑", "驳论"],
        "object_candidates": ["非洲布须曼人", "羚羊", "角马", "石器时代人类"],
        "working_keywords": ["耐力狩猎", "追逐", "追踪", "干粮", "布须曼人", "入不敷出"],
    },
}

A["c2e2ed74-762d-565d-92f4-336b0de662bc"] = {
    "analysis": {
        "question_context": "提问者问医学的进步是否阻碍了人类的进化（Q001）。作者直接回答“并非如此”，并提出医学进步实际上加速了人类进化。",
        "content_units": [
            {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "否定提问预设：医学进步大大提速了人类进化，因为提高了人口密度、加剧社会竞争。", "role": "claim"},
            {"unit_id": "U002", "paragraph_refs": ["P002"], "summary": "强调演化动力来自种群密度超标而非规模超标；对比其他动物靠灾难导致的密度超标，人类靠技术不断推高聚集密度与末位淘汰。", "role": "reason"},
            {"unit_id": "U003", "paragraph_refs": ["P003"], "summary": "推论灾害在高密度下的破坏力更大，以黑死病与欧洲人口密度、城镇距离为例。", "role": "example"},
            {"unit_id": "U004", "paragraph_refs": ["P004"], "summary": "总结医学增大了人类的演化压力，并提到文化选择带来的额外动力。", "role": "conclusion"},
        ],
        "main_claims": [
            {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者否定“医学进步阻碍人类进化”，主张医学进步大大提速了人类进化。", "evidence": ["E1"]},
            {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张任何演化都以种群数量爆炸为前提，医学进步通过增加人口密度、加剧社会竞争推动进化。", "evidence": ["E2"]},
            {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者强调演化的动力来自种群密度超标，而不是所谓的规模超标。", "evidence": ["E3"]},
            {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称人类即使无灾害也处于高频甚至连续的末位淘汰，高密度下遇灾害则发生近乎灭绝性的大清洗。", "evidence": ["E4"]},
            {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作者以黑死病为例主张：技术的发展让灾害规模看似受抑制，但一旦压垮应对体系便连环崩塌。", "evidence": ["E5"]},
            {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者总结医学增大了人类的演化压力；并称即使不考虑医学促进的高密度居住带来的文化选择动力，结论依然成立。", "evidence": ["E6"]},
        ],
        "argument_steps": [
            "直接否定提问预设并给出反向结论（P001）。",
            "给出机制性前提：演化以种群数量爆炸为前提，动力来自密度超标（P001-P002）。",
            "对比动物与人类：动物密度超标多由灾难引发且频率不高，人类则由技术持续推高密度（P002）。",
            "推出末位淘汰常态化与灾害的放大效应（P003）。",
            "以黑死病为例说明高密度与防疫技术反而加剧传播后果（P003）。",
            "收束结论并补充文化选择的额外动力（P004）。",
        ],
        "concept_usage": [
            {"term": "种群密度超标", "meaning": "作者设定的演化动力来源，区别于种群规模。", "evidence": "P002", "ambiguity": "“超标”的判定标准本文未说明。"},
            {"term": "末位淘汰", "meaning": "高密度下处于种群下层的个体承受压力而被淘汰。", "evidence": "P002", "ambiguity": "未给出机制细节与经验证据。"},
            {"term": "文化选择", "meaning": "作者提到高密度居住降低沟通成本、触发文化繁荣，从而为人类演化带来来自文化选择的动力。", "evidence": "P004", "ambiguity": "以“哪怕不考虑”作让步，未展开。"},
            {"term": "医学进步", "meaning": "被作者视为提高人口密度、从而增大演化压力的因素。", "evidence": "P001", "ambiguity": "未区分医学的不同分支与历史阶段。"},
        ],
        "examples_and_targets": [
            "例证：狮子十平方公里只能有一两只，努力多生也只会正常死掉（P002）。",
            "例证：台风对发达地区几乎成了休假理由，但一旦压垮应对便连环崩塌（P003）。",
            "例证：黑死病与欧洲人口密度、城镇距离40%的假设推演（P003）。",
            "被否定对象：提问预设“医学的进步阻碍了人类的进化”（Q001）。",
        ],
        "conditions": [
            "以“任何演化都是以种群数量爆炸为前提”作为普遍前提（P001）。",
            "关于黑死病的推演使用“如果欧洲人口密度降低一半，城镇之间的距离拉远40%”的反事实条件（P003）。",
            "结论以“哪怕不考虑……结论也依然成立”的让步结构加强（P004）。",
        ],
        "rhetoric_and_tone": "短篇说理，断言式语气为主（“并非如此”“事实上”）；用“要特别注意”提示关键前提；以反事实推演和具体历史案例支撑；全篇无致谢或讨论式结尾，直接以结论收束。",
        "unresolved_questions": [
            "“演化的动力是来自种群密度超标，而不是来自所谓的规模超标”中的“规模超标”指什么，本文未定义。",
            "黑死病与人口密度、城镇距离之间的因果链条未给出文献依据，需外部核查（待外部核查）。",
            "作者未说明医学进步在降低死亡率方面是否可能同时减弱选择压力，这一可能的反驳未被讨论。",
        ],
        "evidence": [
            {"key": "E1", "paragraph_id": "P001", "quote": "并非如此。事实上医学的进步大大的提速了人类的进化。", "relation": "supports"},
            {"key": "E2", "paragraph_id": "P001", "quote": "因为医学的进步增加了人口密度，加剧了社会竞争，任何演化都是以种群数量爆炸为前提", "relation": "supports"},
            {"key": "E3", "paragraph_id": "P002", "quote": "演化的动力是来自种群密度超标，而不是来自所谓的规模超标", "relation": "supports"},
            {"key": "E4", "paragraph_id": "P003", "quote": "即使完全不发生灾害，人类也是在高频率的——甚至可以说是连续的末位淘汰", "relation": "supports"},
            {"key": "E5", "paragraph_id": "P003", "quote": "一旦真的压垮了人类的重重应对，一场灾难就如同蓄势已久的地震，发生连环崩塌", "relation": "supports"},
            {"key": "E6", "paragraph_id": "P004", "quote": "总之，医学是增大了人类的演化压力。", "relation": "supports"},
        ],
    },
    "provisional_tags": {
        "domain_candidates": ["进化生物学", "人口学", "医学社会史"],
        "issue_candidates": ["医学与人类进化", "种群密度与选择压力", "黑死病传播条件"],
        "text_function_candidates": ["答疑", "论证"],
        "object_candidates": ["人类", "欧洲", "黑死病", "狮子"],
        "working_keywords": ["种群密度超标", "末位淘汰", "文化选择", "黑死病"],
    },
}

A["0af3428a-e550-54a2-97fc-8d907e94afe9"] = {
    "analysis": {
        "question_context": "提问者问运动能力最强的物种是否为猫科动物（Q001）。作者先设定“运动能力评估标准”的概念，再给出自己的评估标度与推测结论。",
        "content_units": [
            {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "提出先设定评估标准，并给出“有效过载”这一标度。", "role": "definition"},
            {"unit_id": "U002", "paragraph_refs": ["P003", "P004"], "summary": "说明该标度来自战斗机机动性衡量方式，可去掉体型影响、直接表达敏捷性与强壮性。", "role": "reason"},
            {"unit_id": "U003", "paragraph_refs": ["P005"], "summary": "以“就我的理解”“大概率”推测微小昆虫会获胜，理由是材料学上尺度缩小后结构有效强度增大。", "role": "claim"},
            {"unit_id": "U004", "paragraph_refs": ["P006"], "summary": "以该标准给出结论：猫的机动能力不如蚊子。", "role": "conclusion"},
        ],
        "main_claims": [
            {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者提出以“有效过载”作为运动能力的评估标度，即把动物等效为单一质心后能自发造成的过载。", "evidence": ["E1", "E2"]},
            {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者认为该数值直接表达动物的敏捷性和强壮性，并可去掉体型本身的影响。", "evidence": ["E3"]},
            {"claim_id": "C003", "claim_type": "author_qualified", "attribution": "author", "modality": "predicted", "statement": "作者以“就我的理解”“大概率”推测在这场比较中胜者会是某种微小的昆虫，因为同等材料下结构越小有效强度越大。", "evidence": ["E4"]},
            {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者给出结论：在这一条件下，猫的机动能力不如蚊子。", "evidence": ["E5"]},
        ],
        "argument_steps": [
            "先声明需要先设定“运动能力评估标准”的概念（P001）。",
            "引入源自战斗机机动性的“有效过载”标度（P002-P003）。",
            "说明该标度去体型化的优点（P004）。",
            "依据材料强度随尺度缩小而增大的理由，推测微小昆虫胜出（P005）。",
            "据此得出猫不如蚊子的结论（P006）。",
        ],
        "concept_usage": [
            {"term": "有效过载", "meaning": "借用战斗机机动性衡量方式，指动物等效为单一质心后能自发造成的过载，用以比较敏捷性与强壮性。", "evidence": "P002-P004", "ambiguity": "未给出计算方式，也未说明如何处置不同体型动物的等效问题。"},
            {"term": "运动能力", "meaning": "本文未给出独立定义，而是通过“有效过载”这一标度间接界定。", "evidence": "P001-P002", "ambiguity": "作者承认这是一个“很有意思的标度”，但未讨论其局限。"},
        ],
        "examples_and_targets": [
            "例证：把老鼠放大到大象那么大，脚会骨折，用以说明材料强度随尺度变化（P005）。",
            "被回应对象：提问中的“猫科动物最强”预设（Q001）。",
        ],
        "conditions": [
            "全篇以“先设定好评估标准”为前提，结论只在该标度下成立（P001）。",
            "预测使用“就我的理解”“大概率”限定（P005）。",
            "结论句以“在这一条件下”限定适用范围（P006）。",
        ],
        "rhetoric_and_tone": "短篇设定式回答，先立标准再作推断；使用“很有意思”的评述口吻；以反直觉结论（猫不如蚊子）收尾；未展开论证细节。",
        "unresolved_questions": [
            "“有效过载”与动物实际运动表现之间的关系本文未论证。",
            "“某种微小的昆虫”未具体到物种。",
            "老鼠放大到大象体型的例子属思想实验，本文未给出来源或数据（待外部核查）。",
        ],
        "evidence": [
            {"key": "E1", "paragraph_id": "P001", "quote": "先设定好“运动能力评估标准”的概念。", "relation": "context"},
            {"key": "E2", "paragraph_id": "P002", "quote": "其实我们可以给出一个很有意思的标度——有效过载。", "relation": "supports"},
            {"key": "E3", "paragraph_id": "P004", "quote": "这个数值直接表达了动物的敏捷性和强壮性，而可以去掉体型本身的影响。", "relation": "supports"},
            {"key": "E4", "paragraph_id": "P005", "quote": "就我的理解，大概率会是某种微小的昆虫会获胜", "relation": "qualifies"},
            {"key": "E5", "paragraph_id": "P006", "quote": "在这一条件下，猫的机动能力不如蚊子。", "relation": "supports"},
        ],
    },
    "provisional_tags": {
        "domain_candidates": ["比较生理学", "生物力学"],
        "issue_candidates": ["运动能力评估标准", "体型与结构强度", "猫科动物机动性"],
        "text_function_candidates": ["答疑", "概念设定"],
        "object_candidates": ["猫科动物", "蚊子", "昆虫", "老鼠", "大象", "战斗机"],
        "working_keywords": ["有效过载", "运动能力", "材料强度", "机动性"],
    },
}

A["cd4c2817-214a-5286-8a93-74d32d2f2748"] = {
    "analysis": {
        "question_context": "提问者问为什么观念里会有猫爱吃鱼、狗爱吃骨头这种想法（Q001）。作者分别就猫、狗给出历史条件解释，并称这类观念源于对人类对现象的粗暴理解。",
        "content_units": [
            {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "解释“猫爱吃鱼”：猫随大型木质船只扩大分布，船上鼠患与猫不能吃咸肉等条件使鱼成为最可行的食物，港口码头又提供低价值杂鱼。", "role": "reason"},
            {"unit_id": "U002", "paragraph_refs": ["P003"], "summary": "解释“狗爱吃骨头”：驯化于狩猎时代，喂肉违背增产初衷、熬煮骨头耗燃料且当时以烤为主，故骨头给犬不构成浪费。", "role": "reason"},
            {"unit_id": "U003", "paragraph_refs": ["P004"], "summary": "结论：两种观念都来自人类对现象的粗暴理解，并非事实。", "role": "conclusion"},
            {"unit_id": "U004", "paragraph_refs": ["P005"], "summary": "以流浪汉吃剩食及回忆录中“最喜欢吐司边”的说法作类比，说明限定比较对象会产出偏差结论。", "role": "example"},
            {"unit_id": "U005", "paragraph_refs": ["P006"], "summary": "文末“科学答集”标签。", "role": "other"},
        ],
        "main_claims": [
            {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称猫是随大型木质船只的兴起扩大分布区域的，几乎所有船只都会养猫以应对鼠患。", "evidence": ["E1"]},
            {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称猫不能吃咸肉（易急性肾衰竭）又无法消化蔬果和干制粮食，于是船上最好的食物是新鲜鱼。", "evidence": ["E2"]},
            {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者认为猫并不“喜欢”鱼肉，鱼刺对猫威胁不小；只是船上别无选择、码头鱼肉优势太大，形成社会记忆。", "evidence": ["E3"]},
            {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称狗作为狩猎助手的合理性首先来自要促成肉产量净增加，整块喂肉违背初衷。", "evidence": ["E4"]},
            {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称当时熬煮骨头耗燃料、烹饪以烤为主，硬咬生骨头易损伤牙齿，故把骨头丢给咬合力远胜人类的犬不构成浪费。", "evidence": ["E5"]},
            {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者认为狗并不“喜欢”吃骨头，如果可以它们更喜欢吃肉；只有骨头缝里的肉和骨髓可吃，于是人类形成社会记忆。", "evidence": ["E6"]},
            {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者总结这两种结论都源于人类对现象的粗暴理解，并非事实。", "evidence": ["E7"]},
        ],
        "argument_steps": [
            "先给出待解释的两个观念（P001-P003 隐含）。",
            "为猫建立历史条件链：船只—鼠患—养猫—咸肉不可食—鱼成为最优解—港口码头—社会记忆（P002）。",
            "为狗建立条件链：狩猎时代—肉产量初衷—燃料昂贵—以烤为主—骨强度不降—丢骨给犬（P003）。",
            "以“并不是喜欢，而是只有这些可吃”否定观念的事实性（P002-P003）。",
            "以流浪汉剩食类比说明限定比较对象导致的误认（P005）。",
        ],
        "concept_usage": [
            {"term": "社会记忆", "meaning": "作者用来指人类因长期条件限制而形成的、被误当作动物偏好的集体印象。", "evidence": "P002", "ambiguity": "本文未说明该概念的其他用法或来源。"},
            {"term": "粗暴理解", "meaning": "作者对这两种观念成因的概括，指忽略条件限制的判断方式。", "evidence": "P004", "ambiguity": "未给出判据。"},
        ],
        "examples_and_targets": [
            "例证：古代大型木质船只的鼠患问题（P002）；猫不能吃咸肉、不能消化蔬果干粮（P002）；港口码头抛弃的低价值杂鱼与鱼内脏（P002）。",
            "数据性说法：人类咬合力约40公斤，犬70-150公斤（P003）；城镇与航海的燃料收集成本（P003）。",
            "类比：流浪汉吃餐馆剩余食物、回忆录中“最喜欢面包店的吐司边”（P005）。",
        ],
        "conditions": [
            "猫的解释限定于大型木质船只与航海贸易的历史阶段（P002）。",
            "狗的解释限定于人类以狩猎为主要食物来源之一的时代（P003）。",
            "类比部分用“作为一种类比”明示其非事实断言（P005）。",
        ],
        "rhetoric_and_tone": "解释性短文，以“先说猫”“再说狗”分段推进；语气平实、带解释性断言；末段用类比与“也不能这么理解”收束；文末“科学答集”为平台话题标签。",
        "unresolved_questions": [
            "人类咬合力约40公斤、犬70-150公斤的数据未给出来源，需外部核查（待外部核查）。",
            "“猫无法消化蔬果和干制粮食”等生理断言未给出依据（待外部核查）。",
            "“科学答集”标签为平台附加内容，作者归属待核。",
        ],
        "evidence": [
            {"key": "E1", "paragraph_id": "P002", "quote": "猫是随着大型木质船只的兴起而开始扩大分布区域的", "relation": "supports"},
            {"key": "E2", "paragraph_id": "P002", "quote": "因为容易导致急性肾衰竭，而猫又无法消化蔬果和干制粮食", "relation": "supports"},
            {"key": "E3", "paragraph_id": "P002", "quote": "其实猫并不“喜欢”鱼肉，因为鱼刺对猫威胁不小", "relation": "supports"},
            {"key": "E4", "paragraph_id": "P003", "quote": "首先来自于要促成肉产量的净增加", "relation": "supports"},
            {"key": "E5", "paragraph_id": "P003", "quote": "当时要获得骨头夹缝里的肉，需要大量的燃料熬煮", "relation": "supports"},
            {"key": "E6", "paragraph_id": "P003", "quote": "并不是狗“喜欢”吃骨头——如果可能，它们当然更喜欢吃肉", "relation": "supports"},
            {"key": "E7", "paragraph_id": "P004", "quote": "这两种结论都是因为人类对现象的粗暴理解，并非事实。", "relation": "supports"},
        ],
    },
    "provisional_tags": {
        "domain_candidates": ["动物驯化史", "航海史", "饮食文化"],
        "issue_candidates": ["猫吃鱼狗吃骨头的观念来源", "动物偏好与社会记忆"],
        "text_function_candidates": ["答疑", "解释"],
        "object_candidates": ["猫", "狗", "大型木质船只", "港口码头", "流浪汉"],
        "working_keywords": ["社会记忆", "咸肉", "鼠患", "咬合力", "粗暴理解"],
    },
}

A["454f018e-f365-558d-b8af-90b36352067c"] = {
    "analysis": {
        "question_context": "提问者问“对人类恐惧的动物”与“对动物恐惧的人类”两者恐惧感是否等同（Q001）。作者先给恐惧感下定义，再论证人类恐惧与动物恐惧有本质不同，并称这一差异是人与动物分界的原因而非结果。",
        "content_units": [
            {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "为讨论设定定义：恐惧感是意识主体对危机发生的强迫性反应，包含注意力强制转移与生理痛苦感。", "role": "definition"},
            {"unit_id": "U002", "paragraph_refs": ["P003", "P004"], "summary": "从机能与自然选择角度论证该定义的两个方面：不能转移注意力或不厌恶恐惧的物种会被淘汰。", "role": "reason"},
            {"unit_id": "U003", "paragraph_refs": ["P005"], "summary": "强调恐惧的强迫性不可由主体自行关闭。", "role": "qualification"},
            {"unit_id": "U004", "paragraph_refs": ["P006", "P007"], "summary": "提出人类恐惧与动物恐惧有本质不同，甚至是人类与动物的分界；所有物种都有恐惧，而唯有人类的恐惧机制强迫性最弱。", "role": "claim"},
            {"unit_id": "U005", "paragraph_refs": ["P008"], "summary": "提出人类独有“挑战恐惧带来的额外快感”机制，并举极速驾驶、跳伞等例，称大量文明成就与之相关。", "role": "reason"},
            {"unit_id": "U006", "paragraph_refs": ["P009"], "summary": "对比动物：动物无法从恐惧中汲取快感，生理恐惧划下的围栏是绝对命令，因此可用种群作为行为模式研究单位。", "role": "reason"},
            {"unit_id": "U007", "paragraph_refs": ["P010", "P011"], "summary": "分别回答问题的两侧：人对动物的恐惧含兴奋感，动物对人的恐惧多出于绝对禁忌本能，未必理解人类是什么。", "role": "conclusion"},
            {"unit_id": "U008", "paragraph_refs": ["P012", "P013"], "summary": "收尾断言：恐惧的差异不是结果，而是原因。", "role": "conclusion"},
        ],
        "main_claims": [
            {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者定义恐惧感为意识主体对危机发生的强迫性反应，至少包含注意力的强制性转移与生理上的痛苦感两个方面。", "evidence": ["E1"]},
            {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称恐惧的强迫性不可由主体厌憎而自行关闭，如同不能命令心跳停止。", "evidence": ["E2"]},
            {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张人类恐惧与动物恐惧有本质不同，这甚至是人类与动物的分界所在。", "evidence": ["E3"]},
            {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称所有物种都有恐惧（草履虫也会不可自控地避开浓盐水），但唯有人类的恐惧机制强迫性最弱。", "evidence": ["E4"]},
            {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者提出人类独有“挑战恐惧带来的额外快感”机制，并称大量文明成就与这一应激机制无法分离。", "evidence": ["E5"]},
            {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称动物无法从恐惧中汲取快感，生理恐惧的围栏对动物是绝对命令，因此可用种群作为行为模式研究单位。", "evidence": ["E6"]},
            {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者对人类对动物的恐惧的回答：除紧张感外还有难以觉察的兴奋感；动物对人的恐惧多半出于绝对禁忌本能。", "evidence": ["E7", "E8"]},
            {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者断言恐惧的差异不是结果，而是原因。", "evidence": ["E9"]},
        ],
        "argument_steps": [
            "先声明以定义为讨论基础，并给出恐惧感的两个构成方面（P001-P002）。",
            "用自然选择的反事实（不能转移注意力、不厌恶恐惧的物种会灭绝）论证定义的必要性（P003-P004）。",
            "补充强迫性不可自行关闭的限定（P005）。",
            "转入对人的分析：人类恐惧机制强迫性最弱，并有从恐惧中榨取快感的机制（P006-P008）。",
            "以动物的绝对禁忌与种群一致性作对照（P009）。",
            "分别回答问题的两侧，并以“差异是原因不是结果”收束（P010-P013）。",
        ],
        "concept_usage": [
            {"term": "恐惧感", "meaning": "意识主体对危机发生的强迫性反应，含注意力强制转移与生理痛苦感。", "evidence": "P002", "ambiguity": "作者承认按此定义连神经结构都不是必备项。"},
            {"term": "强迫性", "meaning": "恐惧不可由主体厌憎自行关闭的属性；作者用它区分人类与动物（人类强迫性最弱）。", "evidence": "P005, P007", "ambiguity": "“最弱”的衡量方式本文未说明。"},
            {"term": "本能围栏", "meaning": "由生理恐惧划下、对动物构成绝对命令的界限。", "evidence": "P009", "ambiguity": "未说明边界如何界定。"},
            {"term": "快感机制", "meaning": "人类独有、从挑战恐惧中获得额外快感的机制。", "evidence": "P008", "ambiguity": "未给出机制层面的证据。"},
        ],
        "examples_and_targets": [
            "例证：看到老虎扑面而来而无法收回思绪的物种将无法活到现在（P003）。",
            "例证：草履虫不可自控地避开浓盐水（P007）。",
            "例证清单：极速驾驶、跳伞、滑雪、走钢丝、舞蛇表演（P008）；并提到“可以在很大程度上解释快手的成功”（P008）。",
            "例证：同种马匹的恐惧回避高度一致，而对人类无法作同样预言，甚至不能对双胞胎下断言（P009）。",
            "引述式内心独白：“这种影影绰绰的体型巨大的未知生物接近到了我的警备距离之内”等（P011）。",
        ],
        "conditions": [
            "以作者自设的恐惧感定义为全部讨论前提（P001-P002）。",
            "对“所有物种都有恐惧”用草履虫为边界案例，并承认定义可扩展到无神经结构者（P007）。",
            "人类与动物的对比以“动物们没有……动物们无法”为总体断言（P009）。",
        ],
        "rhetoric_and_tone": "定义—论证型说理文；使用“我们”拉近读者；以反事实灭绝场景增强说服力；引号内的动物内心独白为拟人化修辞；结尾三句短句递进（“所以我们才成了人”“这恐惧的差异不是结果，而是原因”）带格言式收束。",
        "unresolved_questions": [
            "“唯有人类的恐惧机制强迫性最弱”缺乏比较标准与经验证据，需外部核查（待外部核查）。",
            "“人类独有一种快感机制”的机制描述未给出来源（待外部核查）。",
            "关于“草履虫”例证能否支撑“所有物种都有恐惧”，作者未讨论定义边界争议。",
            "“这可以在很大程度上解释快手的成功”属附带断言，本文未展开。",
        ],
        "evidence": [
            {"key": "E1", "paragraph_id": "P002", "quote": "恐惧感是意识主体对危机发生的强迫性反应", "relation": "supports"},
            {"key": "E2", "paragraph_id": "P005", "quote": "必然是强迫性的，即不可由于主体的厌憎而随意自行关闭的", "relation": "supports"},
            {"key": "E3", "paragraph_id": "P007", "quote": "它与动物的恐惧有本质的不同。这甚至是人类与动物的分界所在。", "relation": "supports"},
            {"key": "E4", "paragraph_id": "P007", "quote": "但唯有人类的恐惧机制强迫性最弱", "relation": "supports"},
            {"key": "E5", "paragraph_id": "P008", "quote": "人类独有一种快感机制，即挑战恐惧带来的额外快感", "relation": "supports"},
            {"key": "E6", "paragraph_id": "P009", "quote": "动物们无法从恐惧中汲取快感", "relation": "supports"},
            {"key": "E7", "paragraph_id": "P010", "quote": "人类对动物的恐惧，除了令人反胃的紧张感，还有你最初几次难以觉察的兴奋感", "relation": "supports"},
            {"key": "E8", "paragraph_id": "P011", "quote": "而动物对人类的恐惧，则多半是出于某大类绝对禁忌本能", "relation": "supports"},
            {"key": "E9", "paragraph_id": "P013", "quote": "这恐惧的差异不是结果，而是原因。", "relation": "supports"},
        ],
    },
    "provisional_tags": {
        "domain_candidates": ["情绪心理学", "进化生物学", "人与动物关系"],
        "issue_candidates": ["恐惧感定义", "人类与动物恐惧的差异", "恐惧与快感"],
        "text_function_candidates": ["答疑", "概念定义", "论证"],
        "object_candidates": ["人类", "动物", "草履虫", "马"],
        "working_keywords": ["恐惧感", "强迫性", "本能围栏", "快感机制"],
    },
}

A["0ae9a668-9583-5f92-946b-3d4c7df46a04"] = {
    "analysis": {
        "question_context": "提问者问长得好看的动物是否知道自己好看（Q001）。作者主张动物没有“好看”的概念，只做“战斗还是逃跑”的决策，并据此给出一种重新表述的答案。",
        "content_units": [
            {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "否定提问预设：动物并没有好看的概念，只不断做“战斗还是逃跑”的决策。", "role": "rebuttal"},
            {"unit_id": "U002", "paragraph_refs": ["P002", "P003"], "summary": "其中一部分会对应战决策反复选择应战；被同性挑战意味着“我很美”，选择应战意味着“知道我很美”。", "role": "reason"},
            {"unit_id": "U003", "paragraph_refs": ["P004"], "summary": "结论：在这个意义上可以说动物知道自己的美貌。", "role": "conclusion"},
        ],
        "main_claims": [
            {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者否定动物有“好看”的概念，主张它们只是不断做出“战斗还是逃跑”的决策。", "evidence": ["E1"]},
            {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称有一部分动物会不断对同性挑战者的挑战做出“应战”决策。", "evidence": ["E2"]},
            {"claim_id": "C003", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "作者以“在这个意义上”限定地主张：动物知道自己的美貌，想不知道也很难。", "evidence": ["E3"]},
        ],
        "argument_steps": [
            "先否定“好看”概念在动物身上的适用性（P001）。",
            "把“美”转译为被同性同类持续挑战这一可观察事件（P003）。",
            "把“知道”转译为持续选择应战而非逃走（P003）。",
            "以“在这个意义上”收束为肯定结论（P004）。",
        ],
        "concept_usage": [
            {"term": "好看/美", "meaning": "作者不承认动物具有该概念，而将其重新表述为“不断被同性同类挑战”。", "evidence": "P001, P003", "ambiguity": "属于重新定义式用法，本文未说明与人类审美概念的关系。"},
            {"term": "知道", "meaning": "作者将其操作化为持续选择应战而不是逃走。", "evidence": "P003", "ambiguity": "未讨论该操作化是否等同于认知意义上的知道。"},
        ],
        "examples_and_targets": [
            "被否定对象：提问中“动物知道自己长得好看吗”的预设（Q001）。",
            "本文未给出具体物种或观察案例，仅以“同性挑战者”作一般化描述（P002-P003）。",
        ],
        "conditions": [
            "结论句以“在这个意义上”作限定，仅在作者给出的转译框架内成立（P004）。",
            "论证对象限定为“会不断被同性挑战并选择应战”的那一部分动物（P002）。",
        ],
        "rhetoric_and_tone": "极短篇回答，语句简短、断言密集；以引号强调“我很美”“我知道我很美”等转译说法；结尾“想不知道也很难”带轻松调侃语气。",
        "unresolved_questions": [
            "“不断被同性同类挑战”是否可作为“美”的判据，本文未论证。",
            "未给出具体物种或行为学观察来源（待外部核查）。",
            "对不选择应战的个体如何解释，本文未说明。",
        ],
        "evidence": [
            {"key": "E1", "paragraph_id": "P001", "quote": "动物并没有好看的概念。它们只是不断的做出“战斗还是逃跑”的决策。", "relation": "supports"},
            {"key": "E2", "paragraph_id": "P002", "quote": "其中有一部分会不断的对同性挑战者的挑战做出“应战”的决策。", "relation": "supports"},
            {"key": "E3", "paragraph_id": "P004", "quote": "在这个意义上，可以说动物知道自己的美貌。", "relation": "qualifies"},
        ],
    },
    "provisional_tags": {
        "domain_candidates": ["动物行为学", "进化生物学", "美学概念"],
        "issue_candidates": ["动物是否具有审美自我认知", "性选择与应战行为"],
        "text_function_candidates": ["答疑", "概念转译"],
        "object_candidates": ["动物", "同性挑战者"],
        "working_keywords": ["战斗还是逃跑", "应战", "美貌", "好看"],
    },
}

A["e4da9868-2b4b-5c7e-b689-898ab4e03e53"] = {
    "analysis": {
        "question_context": "提问者问动物是什么时候开始惧怕人类的（Q001）。作者先为“惧怕”设定可测量的定义（半数回避距离），再讨论该距离的演化意义、人类攻击距离的分级，最后给出“莫须有”式的答案及时间推断。",
        "content_units": [
            {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "为回答问题先定义“惧怕程度”为“半数回避距离”，并给出测量方式。", "role": "definition"},
            {"unit_id": "U002", "paragraph_refs": ["P003"], "summary": "说明该指标可表达动物“胆量”，警戒对象不限于人类。", "role": "qualification"},
            {"unit_id": "U003", "paragraph_refs": ["P004"], "summary": "论证回避距离过大反而不利生存：迁徙中水源不可选择，耐受近距离才能获得补水机会。", "role": "reason"},
            {"unit_id": "U004", "paragraph_refs": ["P005"], "summary": "指出回避距离取决于捕食者何时决定值得一搏，其他动物贴近该边界生存。", "role": "reason"},
            {"unit_id": "U005", "paragraph_refs": ["P006", "P007"], "summary": "把问题转换为人类的三级攻击距离（50%、90%、100%伤害把握），并给出判断动物是否“怕人”的三档标准。", "role": "definition"},
            {"unit_id": "U006", "paragraph_refs": ["P008"], "summary": "按回避距离分档：低于第三攻击距离者多被驯化豢养，介于第二与第三之间者往往被大量捕杀。", "role": "reason"},
            {"unit_id": "U007", "paragraph_refs": ["P009"], "summary": "指出历史上动物学会惧怕人类极难被有效回答：人类狩猎技巧高、隐瞒攻击距离，动物试错机会极少。", "role": "reason"},
            {"unit_id": "U008", "paragraph_refs": ["P010"], "summary": "推论此类适应若存在必定发生在人类有文字记录以前，因此没有文献可依赖，遗址发掘也难以证明。", "role": "reason"},
            {"unit_id": "U009", "paragraph_refs": ["P011", "P012"], "summary": "给出答案“莫须有”，时间应在史前；并列出文末平台话题标签。", "role": "conclusion"},
        ],
        "main_claims": [
            {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "作者设定“惧怕程度”为“半数回避距离”，即随机采样后在标准环境下人类匀速缓步接近时半数动物开始主动回避的距离。", "evidence": ["E1"]},
            {"claim_id": "C002", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "作者认为该指标可较有效表达动物“胆量”，其警戒对象不见得仅包含人类。", "evidence": ["E2"]},
            {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者主张回避距离过大反而使生存空间太小，不利于动物群体生存，并以迁徙中水源不可选择为例。", "evidence": ["E3"]},
            {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称回避距离取决于“狮子们何时决定值得一搏”，其他动物为综合生存率贴近该边界生存。", "evidence": ["E4"]},
            {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者把人类攻击范围分为第一（50%以上几率造成伤害）、第二（90%）、第三（100%伤害把握）三级攻击距离。", "evidence": ["E5"]},
            {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者以回避距离相对三级攻击距离的位置，界定人类如何判断动物是否“不怕”人。", "evidence": ["E6"]},
            {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "作者称回避距离低于第三攻击距离的动物有很大几率被归化为家畜和宠物，介于第二与第三之间者往往遭遇悲惨、成为捕杀主要对象。", "evidence": ["E7"]},
            {"claim_id": "C008", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "作者认为“历史上有什么动物学会惧怕人类”极难被有效回答，因为人类狩猎技巧高、会隐瞒有效攻击距离，动物逃生率极低。", "evidence": ["E8"]},
            {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "作者提出：若曾有动物种群学会适应人类捕猎，那一定发生在人类有文字记录以前，因此没有文献可依赖。", "evidence": ["E9"]},
            {"claim_id": "C010", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者称不能靠遗址里没有某种动物遗骸来判断其是否学会恐惧人类；只能据逻辑推断这样的物种应该存在，但除非有意外考古发现，证实极难。", "evidence": ["E10"]},
            {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "作者的答案是“莫须有”，发生时间应在史前，即人类还无法充分有效传承狩猎经验的年代。", "evidence": ["E11"]},
        ],
        "argument_steps": [
            "先为“惧怕”建立可测定义（半数回避距离）与测量流程（P001-P002）。",
            "说明指标的适用范围不限于人类（P003）。",
            "论证回避距离存在双向权衡：过大不利取水，过小招致捕食（P004-P005）。",
            "把问题转换为人类攻击距离的分级，并据此定义“怕人”的三档阈值（P006-P007）。",
            "按阈值分档说明驯化与捕杀的分布（P008）。",
            "指出经验研究的困难：人类狩猎技巧高、动物试错机会极少（P009）。",
            "推论适应若存在必在史前，文献与遗址证据均不足（P010）。",
            "给出“莫须有”的答案与时间推断（P011）。",
        ],
        "concept_usage": [
            {"term": "半数回避距离", "meaning": "随机采样后，标准环境下半数个体开始主动回避人类时的逼近距离；用于度量“惧怕程度”。", "evidence": "P002", "ambiguity": "标准环境、采样方式等细节由作者自行设定，未说明其效度检验。"},
            {"term": "第一/第二/第三攻击距离", "meaning": "作者按造成伤害几率划分的人类有效攻击范围（约50%、90%、100%）。", "evidence": "P006", "ambiguity": "三档概率由作者直接给出，未给出测量方式。"},
            {"term": "胆量", "meaning": "作者以半数回避距离反指动物的耐受能力。", "evidence": "P003", "ambiguity": "文中既称“胆量”又称“勇气”，未统一。"},
            {"term": "莫须有", "meaning": "作者对“历史上是否有动物学会惧怕人类”的答案表述，指推断上应存在但无实证。", "evidence": "P011", "ambiguity": "词义带歧义，作者随后以“其发生的时间应该是在史前”补充。"},
        ],
        "examples_and_targets": [
            "例证：长途迁徙中食草动物与狮子老虎鳄鱼“同桌喝水”（P004）。",
            "例证：回避距离低于群体水平者屡屡诱惑狮子发起追击，最终输给概率（P004）。",
            "例证：介于第二与第三攻击距离之间的动物在环保主义勃发之前是捕杀主要对象（P008）。",
            "引用性表述：【一定发生在人类有文字记录以前】【没有】某种动物的遗骸【极难】，原文使用方括号强调（P010）。",
        ],
        "conditions": [
            "全部讨论以作者设定的“半数回避距离”定义与测量方式为前提（P002）。",
            "关于攻击距离的分档使用概率式表述（50%、90%、100%），且被作者称为“很简单的解答”（P006）。",
            "对历史问题的结论多次使用“极难”“应该”“除非……否则”等限定（P009-P011）。",
            "答案限定于有文字记录以前的史前时代（P010-P011）。",
        ],
        "rhetoric_and_tone": "以“先定义后推论”的结构展开，兼用设问（“现在问题来了”）；语气自信、带口语化调侃（“犹如在刀锋上跳舞”）；结论用“莫须有”这一带古语色彩的词；文末列出多个平台话题标签（科学答集/社科答集/文艺答集/企管答集）。",
        "unresolved_questions": [
            "“半数回避距离”与“第一/第二/第三攻击距离”均为作者自设指标，缺少外部依据（待外部核查）。",
            "关于“回避距离低于第三攻击距离的动物有很大几率被归化为家畜和宠物”的分档未给出案例或数据。",
            "文末“科学答集/社科答集/文艺答集/企管答集”为平台话题标签，出现在 text 中但不在 lexical 结构内，属编辑/平台附加文本，作者归属待核。",
            "作者未说明该问题在何种意义上可被实证检验。",
        ],
        "evidence": [
            {"key": "E1", "paragraph_id": "P002", "quote": "我们可以将“惧怕程度”设定为“半数回避距离”", "relation": "supports"},
            {"key": "E2", "paragraph_id": "P003", "quote": "这个指标可以比较有效的表达动物的“胆量”", "relation": "qualifies"},
            {"key": "E3", "paragraph_id": "P004", "quote": "这个数字过大，反而会导致动物的生存空间太小，不利于动物群体的生存", "relation": "supports"},
            {"key": "E4", "paragraph_id": "P005", "quote": "取决于狮子们何时决定值得一搏", "relation": "supports"},
            {"key": "E5", "paragraph_id": "P006", "quote": "第一攻击距离——我们有百分之五十以上几率对对方造成伤害的范围", "relation": "supports"},
            {"key": "E6", "paragraph_id": "P007", "quote": "当半数回避距离小于第二攻击距离，人类认为动物“不怕”人类", "relation": "supports"},
            {"key": "E7", "paragraph_id": "P008", "quote": "回避距离低于第三的动物，则有很大几率会被归化为家畜和宠物", "relation": "supports"},
            {"key": "E8", "paragraph_id": "P009", "quote": "事实是这一问题极难被有效的回答", "relation": "supports"},
            {"key": "E9", "paragraph_id": "P010", "quote": "那【一定发生在人类有文字记录以前】", "relation": "supports"},
            {"key": "E10", "paragraph_id": "P010", "quote": "要证实这一点【极难】", "relation": "qualifies"},
            {"key": "E11", "paragraph_id": "P011", "quote": "所以，答案是“莫须有”，且其发生的时间应该是在史前", "relation": "supports"},
        ],
    },
    "provisional_tags": {
        "domain_candidates": ["动物行为学", "进化生物学", "史前考古"],
        "issue_candidates": ["动物惧怕人类的起源时间", "回避距离的测量与演化意义", "驯化与捕杀的阈值"],
        "text_function_candidates": ["答疑", "概念定义", "方法论讨论"],
        "object_candidates": ["人类", "狮子", "羚羊", "布须曼人", "家畜"],
        "working_keywords": ["半数回避距离", "攻击距离", "回避行为", "驯化", "莫须有"],
    },
}

NOTES = {
    "80c38b2d-3c5b-5fe9-913e-b3324a867a58": "text 末尾“社科答集”为平台话题标签，未出现在 lexical 结构中；本篇条目编号自 3）跳至 5），第 4）条缺失，已在未决问题登记。",
    "8c4f866e-8ef9-547c-af60-ada5792bb1f3": "text 中“科学答集”标签插在正文中间（P019），未被 lexical 覆盖；本条不据此改写正文，仅登记为编辑性拼接。",
    "cd4c2817-214a-5286-8a93-74d32d2f2748": "text 末尾“科学答集”为平台话题标签，未被 lexical 覆盖，已登记。",
    "e4da9868-2b4b-5c7e-b689-898ab4e03e53": "text 末尾四个话题标签（科学答集/社科答集/文艺答集/企管答集）未被 lexical 覆盖；本篇为纯文字文章，无图片节点。",
}


def main():
    rows = load_batch_rows(BATCH)
    records = []
    for row in rows:
        art = row["article"]
        aid = art["id"]
        payload = A[aid]
        rec = build_record(
            row,
            row["batch_id"],
            row["corpus_sha256"],
            payload["analysis"],
            payload["provisional_tags"],
            STARTED,
            COMPLETED,
            notes=NOTES.get(aid, ""),
        )
        records.append(rec)
    write_jsonl(OUT, records)
    print("wrote %s (%d records)" % (OUT, len(records)))


if __name__ == "__main__":
    main()
