#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""批次 r001-b0004 初读记录生成器。

用法： python3 scripts/build_batch.py r001-b0004

段落、字符位置、图片节点、元数据、哈希、证据编号均由 authoring.py 从语料机械生成；
本文件只承载逐篇阅读判断（ANALYSIS）。
"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0004"
STARTED = "2026-09-20T00:20:00+08:00"
COMPLETED = "2026-09-20T00:50:00+08:00"

# ---------------------------------------------------------------------------
# ANALYSIS：每篇文章一条，key = 语料原始 article id
# 所有 evidence 的 quote 均为所引段落原文的连续片段（逐字复制，含中文引号）。
# 本批 8 篇均无图片节点（图片节点 0），正文非空，故 status 均为默认 read。
# ---------------------------------------------------------------------------
ANALYSIS = {
    # =====================================================================
    # 1/8 动物的未来
    # =====================================================================
    "72e97bb7-5f36-581b-885a-ad52843ff29c": {
        "analysis": {
            "question_context": (
                "提问者（Q001）问：如果人类灭绝了除家畜（猪鸭鱼之类用来吃的）之外的动物，人类会怎样。"
                "作者先以“谢邀”回应邀请，随即把提问者的假设情境改述为“正在发生之中”，"
                "并用“接触—理解—管理”三阶段框架重新组织问题，最后给出关于大型动物将“家畜化”的条件性结论。"
                "提问中的假设与“人类会怎样”的关切属于提问者，作者并未照此假设作答，而是替换了问题框架。"
            ),
            "content_units": [
                {"unit_id": "U001", "paragraph_refs": ["P001", "P002"],
                 "summary": "谢邀并指出提问者描述的情境正在发生：作为总体的人类会与越来越多动物建立相当直接的关系。",
                 "role": "context"},
                {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005", "P006", "P007", "P008"],
                 "summary": "以设问引出人类与动物建立关系的三阶段：接触、理解、管理（人类造成影响→意识到影响→管理影响）。",
                 "role": "definition"},
                {"unit_id": "U003", "paragraph_refs": ["P009", "P010", "P011", "P012", "P013"],
                 "summary": "接触阶段：大量动物种群在人类尚未意识到接触时已灭绝，且往往无法被准确认识到；以北极熊、太平洋岛屿两栖物种、远古未命名动物为例，并称认清已实质接触哪些动物是当前动物生态学的核心课题。",
                 "role": "reason"},
                {"unit_id": "U004", "paragraph_refs": ["P014", "P015"],
                 "summary": "理解阶段：目前理解相当肤浅；达成深刻洞见【至少】需要大规模不间断监控（如角马全寿命档案）、低干预监视与信息处理技术进步及巨额资金；在此之前只能靠片面采样和 educated guess，处境比古代天文学家略好但有限。",
                 "role": "reason"},
                {"unit_id": "U005", "paragraph_refs": ["P016"],
                 "summary": "管理阶段：通过管理自身来管理动物（如大坝留鱼类洄游通道、控制排放与工业规模），但人类尚未真正建立对自身的有效管理，以偷猎、炫耀猎物合影、非法宠物为例。",
                 "role": "reason"},
                {"unit_id": "U006", "paragraph_refs": ["P017"],
                 "summary": "坦克比喻：人类像在巨大履带坦克上的原始部落，不知道前进方向与后果，只知道理解在加深、时间是否够不确定。",
                 "role": "qualification"},
                {"unit_id": "U007", "paragraph_refs": ["P018"],
                 "summary": "结论：大型动物能否继续生存首先取决于人类是否愿意且能做到为其保留生存空间；若以此作为最广义“家畜”定义并假设人类在毁灭一切前学会开坦克，则全部或大部分大型动物将家畜化，畜栏网箱不再必要；若人类学不会，则因灭亡失去最终牧养者资格。",
                 "role": "conclusion"},
                {"unit_id": "U008", "paragraph_refs": ["P019"],
                 "summary": "末句断语：如果人类学不会，那是【活该】。",
                 "role": "conclusion"},
            ],
            "main_claims": [
                {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author",
                 "modality": "asserted",
                 "statement": "作者认为提问者所描述的情境正在发生之中：因为自身的发展，作为总体的人类将会与越来越多的动物建立相当直接的关系。",
                 "evidence": ["E1"]},
                {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author",
                 "modality": "asserted",
                 "statement": "作者把人类与动物建立关系分为接触、理解、管理三个阶段：人类先造成（往往无意识的）生存方式层面的影响，继而意识到这种影响，再通过管理这种影响来管理动物的生存。",
                 "evidence": ["E2"]},
                {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author",
                 "modality": "asserted",
                 "statement": "作者认为在接触阶段有大量动物种群在人类尚未意识到已与之发生接触时就已灭绝，而且我们甚至无法准确认识到这一点。",
                 "evidence": ["E3"]},
                {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author",
                 "modality": "asserted",
                 "statement": "作者认为目前对“人类行为如何影响动物生存”这一层理解还相当肤浅，要达成真正令人信服的深刻洞见【至少】需要相当规模的不间断监控。",
                 "evidence": ["E4", "E5"]},
                {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author",
                 "modality": "asserted",
                 "statement": "作者认为人类目前还没真正建立起对自身的有效管理，并以我国偷猎和非法捕杀现象严重、虽有立法仍有人炫耀猎物合影等为例。",
                 "evidence": ["E6"]},
                {"claim_id": "C006", "claim_type": "author_qualified", "attribution": "author",
                 "modality": "hypothetical",
                 "statement": "作者提出条件性判断：如果把“人类愿意而且能做到为其保留生存空间”作为最广义的“家畜”定义，并假设人类能在毁灭一切之前学会开坦克，那么最终所有的动物都会变成“家畜”。",
                 "evidence": ["E7", "E8"]},
                {"claim_id": "C007", "claim_type": "author_qualified", "attribution": "author",
                 "modality": "predicted",
                 "statement": "作者预测：如果人类维持住知识扩张的势头而没有大崩溃甚至毁灭，且那时动物界还有幸免者，最终结局是全部——或至少大部分——大型动物将全部家畜化，且“家畜”包含所看到的所有动物而非仅牛羊鸡鸭猫狗。",
                 "evidence": ["E9", "E10"]},
                {"claim_id": "C008", "claim_type": "author_qualified", "attribution": "author",
                 "modality": "hypothetical",
                 "statement": "作者认为人类对大型动物能否继续生存负首要责任：这首先取决于人类是否愿意以及能否做到为它们保留生存空间，其次才取决于自然界是否存在它们的生存空间。",
                 "evidence": ["E11"]},
                {"claim_id": "C009", "claim_type": "author_qualified", "attribution": "author",
                 "modality": "hypothetical",
                 "statement": "作者提出：如果人类学不会把“属于人类”真正理解为“属于人类”，人类会因灭亡而失去最终牧养者的资格。",
                 "evidence": ["E12"]},
                {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author",
                 "modality": "asserted",
                 "statement": "作者以“活该”评价人类若因学不会这一点而灭亡的结局（末句断语）。",
                 "evidence": ["E13"]},
            ],
            "argument_steps": [
                "以“谢邀”与对邀请题材的调侃开场，随即否定提问的假设框架，改述为“正在发生之中”（P001-P002）。",
                "以设问“什么叫做人类与动物建立关系？”引出三阶段定义：接触、理解、管理（P003-P008）。",
                "逐阶段展开：接触阶段以北极熊、太平洋岛屿两栖物种、远古未命名动物为例说明“未被意识到的接触与灭绝”（P009-P013）。",
                "理解阶段指出当前理解肤浅，并以角马群全寿命档案为例说明所需监控规模，类比古代天文学家处境（P014-P015）。",
                "管理阶段举大坝鱼类洄游通道与排放控制为例，同时用偷猎等反例说明人类尚未有效自管（P016）。",
                "用坦克比喻收束对认识状态的描述，指出不知道时间是否还够（P017）。",
                "给出条件性结论：以最广义“家畜”定义与“学会开坦克”假设推出全部动物家畜化；反面则人类失去牧养者资格（P018）。",
                "以【活该】作结（P019）。",
            ],
            "concept_usage": [
                {"term": "接触、理解、管理", "meaning": "作者自设的三阶段框架，指人类对动物的影响从无意识造成，到意识到影响，再到通过管理自身来管理动物。",
                 "evidence": "P005-P008", "ambiguity": "三阶段是历时顺序还是可并存的层次，本文未说明。"},
                {"term": "家畜", "meaning": "作者给出最广义定义：人类愿意而且能做到为其保留生存空间；因此“家畜”可涵盖所有大型动物而不限于牛羊鸡鸭猫狗。",
                 "evidence": "P018", "ambiguity": "该定义是作者为讨论方便自设的广义用法，与日常或畜牧学用法不同，本文未另作界定。"},
                {"term": "属于人类", "meaning": "作者主张其真正含义不是“等于谁的也不是，先到先得”，而是人类承担保留生存空间的责任。",
                 "evidence": "P018", "ambiguity": "该短语的规范含义由作者直接断言，本文未给出依据或制度含义。"},
                {"term": "educated guess", "meaning": "作者用来指在缺乏大规模监控数据时，凭少量采样与片面观察所作的推测。",
                 "evidence": "P015", "ambiguity": "夹用英文，未给出中文界定。"},
            ],
            "examples_and_targets": [
                "北极熊因人类生活放热引发冰面融化而趋向灭绝（P010）：作者证据，用来说明未被意识到的接触。",
                "河口垃圾经洋流导致太平洋岛屿两栖物种灭绝（P011）：作者证据，措辞为“可能”“很可能”，属推测性举例。",
                "远古时代人类在有效文字语言产生前灭绝若干未命名动物、岩洞壁画难以对应类目亚种（P012）：作者证据/推测。",
                "对角马群进行无差别追踪监视、为每头角马建立全寿命期档案（P014）：作者设想的监控方案，非已实施研究。",
                "古代天文学家只有原始观星台和肉眼、没有天文望远镜（P015）：作者类比材料。",
                "水利工程大坝留鱼类洄游通道、控制排放量和工业规模（P016）：作者举的已有管理尝试。",
                "我国偷猎和非法捕杀、私下贴猎物合影、炫耀非法宠物、询问野生动物喂养方法（P016）：作者举的反例。",
                "巨大履带坦克上的原始部落（P017-P018）：作者贯穿性的比喻材料。",
                "小丑鱼为别的鱼清理鳞片、牧羊犬照料羊群（P018）：作者类比材料，用以说明广义家畜化的情形。",
                "反驳/改述对象：提问者关于“人类灭绝除家畜之外的动物”的假设情境（Q001），作者称其描述的情况正在发生而非未来假设（P002）。",
            ],
            "conditions": [
                "作者以“如果我们将人类愿意而且能做到为其保留生存空间作为最广义的‘家畜’的定义”设定讨论前提（P018）。",
                "“假设人类能在毁灭一切之前学会开坦克”是推出“所有动物都会变成家畜”的必要假设（P018）。",
                "预测部分并列两个条件：“如果最终人类维持住了知识扩张的势头而没有大崩溃甚至毁灭，如果那时动物界还有幸免者”（P018）。",
                "反面条件：“如果人类学不会这一点”（P018）。",
                "规模与技术条件：【至少】需要相当规模的不间断监控、低干预监视手段的极大技术进步、信息处理与挖掘能力的极大进步、极大量资金投入（P014）。",
                "时间性限定：“在不久的将来”“目前”“从长期看”式表述（P016、P018）。",
                "行文中的推测限定：“可能”“很可能”“也许”“是否还够”“大概”等（P011、P012、P017）。",
            ],
            "rhetoric_and_tone": (
                "知乎答疑体。开场“谢邀……不过为什么邀请我的都是演化论问题？”带调侃；"
                "贯穿第二人称“你”与提问者对话。以设问句推进结构（“什么叫做人类与动物建立关系？”）。"
                "用【】强调关键词（【至少】、【活该】）。中段用大段坦克比喻渲染认识上的模糊与无力（P017）。"
                "结尾由长长的条件句收束到两句短促断语，末句“如果是那样，真是【活该】。”语气强烈，带训诫与讽刺色彩。"
                "整体是先替换问题框架、再分层论证、最后给出条件性预言并加道德评价的结构。"
            ),
            "unresolved_questions": [
                "正文末段 P019 以换行符开头（原文字符 1952 处），分段仅有一句；该换行是原文排版还是抓取残留，本文未说明。",
                "P016 称“我国偷猎和非法捕杀的现象非常严重”，本文未点明“我国”所指国名（按平台语境应为中国），主体需外部核查。",
                "角马群全寿命档案、低干预监视等被作者描述为达成洞见的必要条件，但是否已有实际研究案例，本文未说明（待外部核查）。",
                "“家畜”的最广义定义由作者自设且与常识用法不同，本文未说明该定义是否与畜牧学定义冲突。",
                "提问者所问“人类会怎样”并未被正面回答，作者只回答了动物一侧的结局，本文未说明人类自身的结局。",
                "本篇 brief 字段是正文开头约 140 字的截断（且已去除换行），不含独立于正文的内容，不得作为作者主张的单独依据。",
            ],
            "evidence": [
                {"key": "E1", "paragraph_id": "P002", "quote": "你所描述的这种情况正在发生之中", "relation": "supports"},
                {"key": "E2", "paragraph_id": "P008", "quote": "我们将这三阶段分别称为接触、理解与管理", "relation": "supports"},
                {"key": "E3", "paragraph_id": "P009", "quote": "有大量的动物种群在人类甚至还没有意识到自己已经与之发生接触的时候已经灭绝", "relation": "supports"},
                {"key": "E4", "paragraph_id": "P014", "quote": "我们目前的理解还相当肤浅", "relation": "supports"},
                {"key": "E5", "paragraph_id": "P014", "quote": "【至少】也需要能进行相当规模的不间断监控", "relation": "supports"},
                {"key": "E6", "paragraph_id": "P016", "quote": "我们人类目前还没真正建立起对自身的有效管理", "relation": "supports"},
                {"key": "E7", "paragraph_id": "P018", "quote": "作为最广义的“家畜”的定义", "relation": "qualifies"},
                {"key": "E8", "paragraph_id": "P018", "quote": "则最终所有的动物都会变成“家畜”", "relation": "supports"},
                {"key": "E9", "paragraph_id": "P018", "quote": "最终的结局是全部的——或至少是大部分大型的动物——将全部家畜化", "relation": "supports"},
                {"key": "E10", "paragraph_id": "P018", "quote": "家畜并不意味着剩下的就只有牛羊鸡鸭猫狗", "relation": "qualifies"},
                {"key": "E11", "paragraph_id": "P018", "quote": "首先都取决于人类是否愿意以及能否做到为它们保留生存空间", "relation": "supports"},
                {"key": "E12", "paragraph_id": "P018", "quote": "人类自然会因灭亡而失去这最终牧养者的资格", "relation": "supports"},
                {"key": "E13", "paragraph_id": "P019", "quote": "如果是那样，真是【活该】。", "relation": "supports"},
            ],
        },
        "provisional_tags": {
            "domain_candidates": ["动物生态学", "人与自然关系", "未来学", "演化论"],
            "issue_candidates": ["人类活动导致的物种灭绝", "人类对动物的管理责任", "家畜化", "生态数据监控能力"],
            "text_function_candidates": ["答疑", "论辩", "未来预测", "比喻说理"],
            "object_candidates": ["人类", "北极熊", "角马", "小丑鱼", "牧羊犬", "动物生态学", "我国（国家主体未点名）"],
            "working_keywords": ["接触", "理解", "管理", "家畜化", "最广义的“家畜”", "属于人类", "不间断监控", "坦克比喻"],
        },
        "notes": (
            "本篇无图片节点（图片节点 0），正文 19 段全部读完，status=read、full_text_checked=true。"
            "P019 原文以换行符起始（“\\n如果是那样，真是【活该】。”），已按原文转录与引用。"
            "brief 字段为正文前约 140 字的截断，与正文重合，不作为独立证据。"
            "平台为知乎，提问属提问者（Q001），作者改述了提问的假设框架，二者已区分。"
        ),
    },
    # =====================================================================
    # 2/8 逃避伤害
    # =====================================================================
    "1da7d8ed-010d-57fa-bd76-15259ca65678": {
        "analysis": {
            "question_context": (
                "提问者（Q001）问怎么解决“因为害怕被伤害而逃避很多事情”。"
                "作者没有给出分步操作方案，而是先否定“绝不受伤”的策略（称其为死路），"
                "再提出以主动、有控制地接受受伤风险来脱敏，并把牺牲与人生价值、向他人而死联系起来。"
                "提问者“害怕被伤害、逃避很多事”的处境属提问者陈述，不是作者主张。"
            ),
            "content_units": [
                {"unit_id": "U001", "paragraph_refs": ["P001"],
                 "summary": "开篇命题：逃避伤害只是为了尽可能选择值得的牺牲，而不是为了“永远幸福的生活下去”。",
                 "role": "claim"},
                {"unit_id": "U002", "paragraph_refs": ["P002", "P003"],
                 "summary": "论证“绝不受伤”策略无效：越恐惧越敏感，防范手段追不上敏感性的提高，最终只能自绝于人类；结论是“这是条死路”。",
                 "role": "reason"},
                {"unit_id": "U003", "paragraph_refs": ["P004", "P005", "P006", "P007"],
                 "summary": "行动建议：主动接受受伤的可能性，聪明、有控制、有意地受伤，在不断受伤中形成耐受、脱去敏感，并把“于何时在何地为何人接受何种受伤的风险”作为贯穿人生的深思熟虑的选择。",
                 "role": "action_advice"},
                {"unit_id": "U004", "paragraph_refs": ["P008", "P009", "P010", "P011"],
                 "summary": "理由：唯有有效的牺牲是真正幸福的；人终将死去，无法选择“不失去”，只能选择用必然失去的一切换什么遗产；牺牲有技巧与价值最大化的复杂策略，只能学习而不能拒绝。",
                 "role": "reason"},
                {"unit_id": "U005", "paragraph_refs": ["P012", "P013"],
                 "summary": "限定与结论：回避一种伤害只应因不愿虚掷“受伤余额”，绝不是守着余额到死；活着只是选择如何为他人死去，这是唯一出路，除此之外只有无尽的恐惧和痛苦。",
                 "role": "conclusion"},
                {"unit_id": "U006", "paragraph_refs": ["P014", "P015", "P016"],
                 "summary": "接受该选择后的结果：从接受那一刻起“受膏为王”，只要不改初衷便勇气自生、尊严自在，不必苟且逢迎；这是唯一可选择的人生价值（如还有人生价值可言），也是人生捷径。",
                 "role": "conclusion"},
                {"unit_id": "U007", "paragraph_refs": ["P017"],
                 "summary": "收束格言：这个世界不缺聪明人，缺聪明的勇士，主要是缺勇士。",
                 "role": "conclusion"},
            ],
            "main_claims": [
                {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author",
                 "modality": "asserted",
                 "statement": "作者主张逃避伤害的目的只是尽可能选择值得的牺牲，而不是为了“永远幸福的生活下去”。",
                 "evidence": ["E1"]},
                {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author",
                 "modality": "asserted",
                 "statement": "作者认为不断选择“绝不会受伤害的做法”会让“千万不要受伤害”在决策中越来越重要，使人生被浸透在“可能受伤害”的恐惧之中。",
                 "evidence": ["E2"]},
                {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author",
                 "modality": "negated",
                 "statement": "作者断定“一定要避免被伤害”是无效的策略：越恐惧越敏感，防范手段永远追不上敏感性的提高，最后除了自绝于人类没有手段能安抚极端敏感化的恐惧，因而是死路。",
                 "evidence": ["E3", "E4", "E5"]},
                {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author",
                 "modality": "asserted",
                 "statement": "作者建议主动接受受伤的可能性，聪明地、有控制地、有意地受伤，在不断受伤中形成耐受、脱去敏感，从而剥夺“伤害”的威力。",
                 "evidence": ["E6", "E7"]},
                {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author",
                 "modality": "asserted",
                 "statement": "作者认为“于何时在何地为何人接受何种受伤的风险”应是深思熟虑后的选择，并应贯穿整个人生。",
                 "evidence": ["E8"]},
                {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author",
                 "modality": "predicted",
                 "statement": "作者预言与受伤的可能性主动共舞会使人慢慢学会“跳舞”，并得到别人不敢、不肯、不能的优势。",
                 "evidence": ["E9"]},
                {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author",
                 "modality": "asserted",
                 "statement": "作者主张唯有有效的牺牲是真正幸福的，因为人终将死去，所舍不得牺牲的终会化为飞烟，人根本不能选择“不失去”，只能选择用必然失去的一切换到什么样的遗产留给其他人。",
                 "evidence": ["E10", "E11", "E12"]},
                {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author",
                 "modality": "negated",
                 "statement": "作者主张回避一种伤害只该是因为不愿虚掷“受伤余额”，绝不是为了守着这份余额到死。",
                 "evidence": ["E13"]},
                {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author",
                 "modality": "asserted",
                 "statement": "作者把活着定义为选择如何一点点、一步步地为他人死去，并称想通这条路后世界再无恐惧，且这是唯一出路，除此之外只有无尽的恐惧和痛苦。",
                 "evidence": ["E14", "E15"]},
                {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author",
                 "modality": "predicted",
                 "statement": "作者预言：何时接受这一条，从那一刻起就“受膏为王”，只要不改初衷便会勇气自生、尊严自在，不必苟且和逢迎。",
                 "evidence": ["E16", "E17"]},
                {"claim_id": "C011", "claim_type": "author_qualified", "attribution": "author",
                 "modality": "qualified",
                 "statement": "作者称这是唯一可以选择的人生价值，“如果还有人生价值可言的话”。",
                 "evidence": ["E18"]},
                {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author",
                 "modality": "asserted",
                 "statement": "作者认为这也是人生的捷径：路比把全部智慧花在绝对避免吃亏的人直得多，因此最终也走得远得多。",
                 "evidence": ["E19"]},
                {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author",
                 "modality": "asserted",
                 "statement": "作者断言这个世界不缺聪明人，缺聪明的勇士，主要是缺勇士。",
                 "evidence": ["E20"]},
            ],
            "argument_steps": [
                "先给命题：逃避伤害是为了选择值得的牺牲，而非追求永远幸福（P001）。",
                "反面论证：持续规避受伤会使恐惧主导决策，防范手段追不上敏感性增长，最终走向自绝于人类，故为死路（P002-P003）。",
                "转为行动建议：主动接受受伤可能性，以有控制的受伤获得耐受与脱敏（P004-P005）。",
                "把受伤风险的选择上升为贯穿人生的深思熟虑的选择，并描述其收益（P006-P007）。",
                "给出理由：唯有有效的牺牲真正幸福，因为人必死、无法不失去，只能选择换什么遗产（P008-P010）。",
                "指出牺牲需要技巧与策略，拒绝牺牲不是选项，只能学习牺牲的智慧与技术（P011）。",
                "限定回避的正当理由，并推出“活着是为他人死去”的结论（P012-P013）。",
                "以“受膏为王”的意象描述接受后的状态，并以人生捷径与“缺勇士”的格言收束（P014-P017）。",
            ],
            "concept_usage": [
                {"term": "受伤余额", "meaning": "作者用“余额”比喻一个人还可以承受的受伤额度；回避伤害只应因为不愿虚掷这份额度，而不是守着它到死。",
                 "evidence": "P012", "ambiguity": "该词带引号，属作者自造比喻，本文未给出量化或判定标准。"},
                {"term": "有效的牺牲", "meaning": "换得遗产、有价值产出的牺牲，被认为是真正幸福的；与守着自身余额不动的做法相对。",
                 "evidence": "P008、P010", "ambiguity": "“有效”的判定标准（对谁有效、如何衡量）本文未说明。"},
                {"term": "受膏为王", "meaning": "作者借宗教加冕意象指接受“为他人而死”这一选择后获得的心理状态：勇气自生、尊严自在。",
                 "evidence": "P014", "ambiguity": "典故来源本文未注明，作者把它当作比喻使用。"},
                {"term": "共舞", "meaning": "与“受伤的可能性”主动互动的比喻，指在反复接触风险中习得应对能力。",
                 "evidence": "P007", "ambiguity": "比喻的具体所指（具体技能或心理机制）本文未展开。"},
            ],
            "examples_and_targets": [
                "“永远幸福的生活下去”“绝不会受伤害的做法”“千万不要受伤害”“一定要避免被伤害”等被作者加引号并否定的流行说法（P001-P002）：作者的反驳对象（未点明具体说话者）。",
                "把全部智慧都花在怎么绝对避免吃亏的人（P016）：作者用作对比的反面形象。",
                "“受膏为王”（P014）：修辞/宗教意象材料。",
                "“人生马拉松变成四百米越野”式的譬喻未在本篇出现（见同批《宁不畏死》P005），本篇用“跳舞”“捷径”等比喻（P007、P016）。",
                "本文未使用具体人物、机构、事件或数据作为论据。",
            ],
            "conditions": [
                "“在不断受伤之中形成耐受、脱去敏感”是脱敏效果的前提（P005）。",
                "接受风险的时机与对象被限定为“于何时在何地为何人接受何种受伤的风险”，且须“经过深思熟虑”（P006）。",
                "“只要不改初衷”是勇气自生、尊严自在的条件（P014）。",
                "结论带自我限定：“如果还有人生价值可言的话”（P015）。",
                "“你回避一种伤害，只该是因为不愿虚掷你的‘受伤余额’”，给出回避的允许条件（P012）。",
                "末段的“走得远”以“路直”为条件式比较（P016）。",
            ],
            "rhetoric_and_tone": (
                "格言体、训诫体，通篇第二人称“你”，像对提问者直接劝导。"
                "多用短句与斩截判断（“这是条死路。”“节约才是”式的收束在本篇为“这是条死路。”“缺勇士。”）。"
                "排比：“别人不敢的，你敢；别人不肯的，你肯；于是别人不能的，你能”（P007）。"
                "使用宗教/仪式意象“受膏为王”，以及“跳舞”“捷径”等比喻。"
                "语气强烈、以绝对化措辞给人生定调（“唯一出路”“唯一可以选择的人生价值”），同时用“如果还有人生价值可言的话”自我限定。"
                "P014 使用“ta人”这种性别中立写法，与同段“他人”并存（P013 作“他人”）。"
            ),
            "unresolved_questions": [
                "提问者问“怎么解决……逃避”，作者给出的是原则性劝诫，未提供可操作的步骤、练习或判断标准，本文未说明读者应如何具体落实。",
                "“受伤余额”是自造比喻，本文未给出量化或耗尽判定，无法确定其边界。",
                "“有效的牺牲”“真正幸福”的判定标准本文未说明。",
                "“受膏为王”的典故来源（宗教加冕意象）本文未注明（待外部核查其确切出处）。",
                "P014 写作“为ta人而死”，同篇 P013 写作“为他人死去”，两种写法并存，本文未说明是否刻意区分性别。",
                "本篇 brief 为正文开头约 140 字的截断（去换行），与 P001-P002 重合，不构成独立内容。",
            ],
            "evidence": [
                {"key": "E1", "paragraph_id": "P001", "quote": "逃避伤害只是为了尽可能选择值得的牺牲", "relation": "supports"},
                {"key": "E2", "paragraph_id": "P002", "quote": "只会让“千万不要受伤害”在你的决策中变得越来越重要", "relation": "supports"},
                {"key": "E3", "paragraph_id": "P002", "quote": "“一定要避免被伤害”是无效的策略", "relation": "supports"},
                {"key": "E4", "paragraph_id": "P002", "quote": "你最后除了自绝于人类，将没有任何手段能安抚你极端敏感化的恐惧", "relation": "supports"},
                {"key": "E5", "paragraph_id": "P003", "quote": "这是条死路。", "relation": "supports"},
                {"key": "E6", "paragraph_id": "P004", "quote": "你要学会主动接受受伤的可能性。", "relation": "supports"},
                {"key": "E7", "paragraph_id": "P005", "quote": "在不断受伤之中形成耐受、脱去敏感", "relation": "supports"},
                {"key": "E8", "paragraph_id": "P006", "quote": "应该是你在经过深思熟虑后进行的一种选择", "relation": "supports"},
                {"key": "E9", "paragraph_id": "P007", "quote": "别人不敢的，你敢；别人不肯的，你肯；于是别人不能的，你能", "relation": "supports"},
                {"key": "E10", "paragraph_id": "P008", "quote": "唯有有效的牺牲是真正幸福的", "relation": "supports"},
                {"key": "E11", "paragraph_id": "P009", "quote": "你根本就不能选择“不失去”", "relation": "supports"},
                {"key": "E12", "paragraph_id": "P010", "quote": "你只能选择用必然最终失去的一切能换到什么样的遗产去留给其他人", "relation": "supports"},
                {"key": "E13", "paragraph_id": "P012", "quote": "只该是因为不愿虚掷你的“受伤余额”", "relation": "supports"},
                {"key": "E14", "paragraph_id": "P013", "quote": "所谓活着，只是在选择如何一点点、一步步的为他人死去", "relation": "supports"},
                {"key": "E15", "paragraph_id": "P013", "quote": "而且这是唯一出路", "relation": "supports"},
                {"key": "E16", "paragraph_id": "P014", "quote": "从那一刻你就受膏为王", "relation": "supports"},
                {"key": "E17", "paragraph_id": "P014", "quote": "只要不改初衷，你将会发现勇气自生，尊严自在", "relation": "supports"},
                {"key": "E18", "paragraph_id": "P015", "quote": "如果还有人生价值可言的话", "relation": "qualifies"},
                {"key": "E19", "paragraph_id": "P016", "quote": "你的路要比那些把全部智慧都花在怎么绝对避免吃亏的人直的多", "relation": "supports"},
                {"key": "E20", "paragraph_id": "P017", "quote": "缺聪明的勇士，主要是缺勇士", "relation": "supports"},
            ],
        },
        "provisional_tags": {
            "domain_candidates": ["心理调适", "人生哲学", "伦理与牺牲"],
            "issue_candidates": ["回避伤害的心理机制", "受伤与脱敏", "牺牲的意义", "死亡与人生价值"],
            "text_function_candidates": ["答疑", "劝诫", "格言体说理"],
            "object_candidates": ["提问者（未具名）", "“聪明人”与“勇士”（泛指）"],
            "working_keywords": ["逃避伤害", "受伤余额", "有效的牺牲", "脱敏", "受膏为王", "向他人而死"],
        },
        "notes": (
            "本篇无图片节点，正文 17 段全部读完，status=read、full_text_checked=true。"
            "提问者的处境（害怕被伤害而逃避）仅出现在 Q001，已与作者主张区分；"
            "文中加引号的说法（“永远幸福的生活下去”“一定要避免被伤害”等）是作者引述并否定的流行说法，不是作者主张。"
            "brief 为正文前约 140 字截断，与 P001-P002 重合，不作为独立证据。"
        ),
    },
    # =====================================================================
    # 3/8 节水呼吁
    # =====================================================================
    "98debe38-40de-5cf4-a63d-d230bbc7af3d": {
        "analysis": {
            "question_context": (
                "提问者（Q001）问为什么近些年节约用水的呼声不像以前那么高。"
                "作者先指出许多答案犯了把“缺少宣传”等同于“不提倡”等逻辑错误，"
                "再论证节约本身在中国是国民性与文化共识、且“浪费促进经济”不成立，"
                "最后回到提问：宣传份额下降更可能是优先级排序问题，并不意味着不必节水。"
            ),
            "content_units": [
                {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004"],
                 "summary": "指出很多人犯的逻辑错误（缺少宣传＝不提倡＝肯定反向行为、国外没有节水理念等），并讽刺部分答案只是借机秀“知识渊博”；反问这些说法逻辑上是否成立。",
                 "role": "rebuttal"},
                {"unit_id": "U002", "paragraph_refs": ["P005", "P006"],
                 "summary": "以反问“在中国有没有任何东西不必节约？”提出节约是中国人与生俱来的国民性。",
                 "role": "claim"},
                {"unit_id": "U003", "paragraph_refs": ["P007", "P008"],
                 "summary": "反驳“浪费促进经济”：它只是局部短期现象，不是长期普遍真理，更不应成为主张的理念；并以吃鸡的例子与GDP、医疗费的连环反问展开；随后给出条件式让步——若环境承受力与开发能力真的无限则无需节约，但反问“是否意味着我们肯定将来也一定做得到”。",
                 "role": "rebuttal"},
                {"unit_id": "U004", "paragraph_refs": ["P009", "P010"],
                 "summary": "以中国历史经验说明太平盛世不保证长久、粮仓满不保证明年不饿死人，结论是“节约才是”。",
                 "role": "reason"},
                {"unit_id": "U005", "paragraph_refs": ["P011", "P012", "P013", "P014"],
                 "summary": "申明无论贫富、无论缺不缺都要节约；节俭还有超出实际盈余的精神价值，可抵消一部分“由节俭造成的浪费”，这是老一辈“节俭狂情”的本质；节俭是中国人的文化共识、身份认同标志与官方选择的民族性设计之一；并断言这理念是对的，反驳“经济学家”。",
                 "role": "claim"},
                {"unit_id": "U006", "paragraph_refs": ["P015", "P016", "P017"],
                 "summary": "回答提问：宣传份额下降更可能是优先级问题而非理念过时失效，因为中国有太多别的问题缠身、焦点排序改变，且水在需要节约的东西中并不排名靠前；但这不意味着以后不用节约或不应该节水。",
                 "role": "conclusion"},
                {"unit_id": "U007", "paragraph_refs": ["P018"],
                 "summary": "正文末尾出现平台话题标签“社科答集”，非作者论述，且 lexical 结构未覆盖该片段。",
                 "role": "other"},
            ],
            "main_claims": [
                {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author",
                 "modality": "asserted",
                 "statement": "作者认为很多人犯了逻辑错误：把“缺少宣传”误认为等于“不提倡”，甚至等于“肯定反向行为”，并误认为国外没有节约用水的理念或该理念呼声不响亮意味着不用节约用水被普遍认可。",
                 "evidence": ["E1"]},
                {"claim_id": "C002", "claim_type": "opponent_view", "attribution": "opponent",
                 "modality": "asserted",
                 "statement": "被作者反驳的说法：缺少宣传就是不提倡、国外没有节约用水的理念、国外呼声不响意味着“不用节约用水”的理念被普遍认可。",
                 "evidence": ["E2"]},
                {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author",
                 "modality": "questioned",
                 "statement": "作者以反问质疑上述说法：这些说法逻辑上是否成立，是否真的可以在这些说法上加上“因为”两个字。",
                 "evidence": ["E3"]},
                {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author",
                 "modality": "asserted",
                 "statement": "作者主张节约是我们中国人娘胎里带来的国民性。",
                 "evidence": ["E4"]},
                {"claim_id": "C005", "claim_type": "opponent_view", "attribution": "opponent",
                 "modality": "asserted",
                 "statement": "被作者反驳的说法：“浪费促进经济”可以作为理念主张。",
                 "evidence": ["E5"]},
                {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author",
                 "modality": "negated",
                 "statement": "作者认为“浪费促进经济”只是一种可观察到的局部、短期现象，既不是长期普遍真理，更不可以是一种应该主张的理念；实则只是通过扩大对环境的压力和对欲望的挖掘来扩大交易额。",
                 "evidence": ["E5", "E6"]},
                {"claim_id": "C007", "claim_type": "author_qualified", "attribution": "author",
                 "modality": "hypothetical",
                 "statement": "作者作出条件式让步：如果广义的环境对人的欲望的承受力真是无限的、人也绝对可以自信环境开发能力永远能压榨出更大承载力，那么的确什么也用不着节约。",
                 "evidence": ["E7"]},
                {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author",
                 "modality": "questioned",
                 "statement": "作者反问：我们到目前看似做到了，是否意味着肯定将来也一定做得到。",
                 "evidence": ["E8"]},
                {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author",
                 "modality": "asserted",
                 "statement": "作者以中国几千年历史传承为依据，主张太平盛世不意味着战乱不会转眼即来、粮仓满也不见得保证明年不饿死人，“几十年好日子”不是好日子可以永远持续的保证。",
                 "evidence": ["E9"]},
                {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author",
                 "modality": "asserted",
                 "statement": "作者主张无论富贵或贫穷、无论一种东西现在看起来缺不缺，都要节约；并称节俭习惯有超出实际盈余的精神价值，这种精神价值本身可以抵消一部分“由于节俭造成的浪费”。",
                 "evidence": ["E10", "E11"]},
                {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author",
                 "modality": "asserted",
                 "statement": "作者主张节俭是中国人的文化共识、身份认同标志，是中国官方为中国人选择的民族性设计之一，是中国人可以而且打算持有的国民标签。",
                 "evidence": ["E12"]},
                {"claim_id": "C012", "claim_type": "opponent_view", "attribution": "opponent",
                 "modality": "asserted",
                 "statement": "被作者反驳的对象：反对节俭的“经济学家”们的说法。",
                 "evidence": ["E14"]},
                {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author",
                 "modality": "asserted",
                 "statement": "作者断言这理念是对的：哪怕存在各种浪费，节俭也是对的、普遍正确，并让反对的“经济学家”回去再学两年。",
                 "evidence": ["E13", "E14"]},
                {"claim_id": "C014", "claim_type": "author_qualified", "attribution": "author",
                 "modality": "qualified",
                 "statement": "作者提出带条件的普遍命题：人类只要还没学会在宇宙中瞬间移动以及在真空与辐射中自如生活，这个地球上就没有任何东西是不需要节约的。",
                 "evidence": ["E15"]},
                {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author",
                 "modality": "qualified",
                 "statement": "作者回答提问：节水宣传份额下降更可能是优先级问题，而不是理念过时失效；因为中国有太多别的问题缠身、焦点排序改变，且水在一切需要节约的东西中并不排名靠前。",
                 "evidence": ["E16"]},
                {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author",
                 "modality": "negated",
                 "statement": "作者强调这并不意味着“以后不用节约了”或者“不必节水”甚至“不应该节水”。",
                 "evidence": ["E17"]},
            ],
            "argument_steps": [
                "先列他人答案的三类逻辑错误，并讽刺其炫学，继而以反问要求检验其逻辑（P001-P004）。",
                "提出正面命题：节约是中国人的国民性，中国没有东西不必节约（P005-P006）。",
                "反驳“浪费促进经济”，区分局部短期现象与应然理念，并以吃鸡—GDP—医疗费的连续反问与夸张例证展开（P007）。",
                "给出条件式让步并立即反问：只有环境承受力与开发能力无限时才无需节约，但无法保证将来做得到（P008）。",
                "以中国历史经验（太平盛世不长久、粮仓满不保证不饿死人）支撑“节约才是”（P009-P010）。",
                "扩展论证：节俭的精神价值与老一辈“节俭狂情”，并把节俭提升为文化共识、身份认同与官方民族性设计（P011-P012）。",
                "以“这理念是对的”作断言并反驳“经济学家”（P013）。",
                "给出带条件的普遍结论：只要人类还不能瞬间移动、不能在真空与辐射中生活，就没有东西不需要节约（P014）。",
                "回到提问，以优先级解释宣传份额下降，并否定“不必节水”的推论（P015-P017）。",
            ],
            "concept_usage": [
                {"term": "节约/节俭", "meaning": "作者把它当作中国人的国民性、文化共识与身份认同标志，并主张其普遍正确，兼有实际盈余与精神价值两方面。",
                 "evidence": "P006、P011、P012、P013", "ambiguity": "作者未区分“节约用水”与一般“节俭”，回答提问时把两者贯通使用。"},
                {"term": "国民性/民族性设计", "meaning": "作者称节约是“娘胎里带来的国民性”，又是“中国官方为中国人选择的民族性设计之一”。",
                 "evidence": "P006、P012", "ambiguity": "“官方设计”的依据与主体本文未说明，前后“天生”与“被设计”两种表述并存。"},
                {"term": "“浪费促进经济”", "meaning": "作者所反驳的一种说法，被限定为可观察到的局部、短期现象，不能当作应然理念。",
                 "evidence": "P007", "ambiguity": "作者未指明该说法出自哪些具体论者。"},
                {"term": "“节俭狂情”", "meaning": "作者用来描述老一辈可观察到的节俭心理：在乎的不是钱花得起与否，而是丧失节俭适应态带来的安全感价值。",
                 "evidence": "P011", "ambiguity": "带引号的自造描述，未给出经验研究出处。"},
                {"term": "优先级", "meaning": "作者对宣传份额下降给出的解释：焦点排序改变，而非理念失效；水在需要节约之物的排序中不靠前。",
                 "evidence": "P016", "ambiguity": "“优先级”由谁排序、依据何种机制，本文未说明。"},
            ],
            "examples_and_targets": [
                "反驳对象一：“很多人”的逻辑错误与部分借机秀“知识渊博”的答案（P001-P002）。",
                "反驳对象二：“浪费促进经济”论（P007）与反对节俭的“经济学家”（P013）。",
                "假设性例证：人人每餐多吃一只鸡、盖养鸡场屠宰场、创造职位、吃出满大街胖子、国家收吃鸡税、GDP上涨（P007）：作者用夸张链条举例说明增长不等于福利。",
                "反问材料：“每餐多点一只鸡来摆着看看然后倒掉”作为“完美的改进”（P007）。",
                "历史经验材料：中国几千年历史传承中太平盛世与战乱、粮仓与饿死人的关系（P009）。",
                "社会观察材料：老一辈“节俭狂情”（P011）与“由俭入奢”的心理风险（P011）。",
                "本文未引用具体人物、机构、文献或统计数据。",
            ],
            "conditions": [
                "条件式让步：“如果广义的环境对人的欲望的承受力真的是无限的，人也绝对可以自信自己的环境开发能力永远可以保证从环境里压榨出更大的承载力来解决自己造成的危机，那么的确什么也用不着节约”（P008）。",
                "普遍命题的限制条件：“人类只要还没学会在宇宙中瞬间移动以及在真空与辐射中自如生活”（P014）。",
                "对节俭的坚持附带让步：“哪怕因为各种原因存在着各种浪费”（P013）。",
                "对老一辈节俭的解释带观察限定：“这可以说是老一辈里普遍可以观察到的”（P011）。",
                "回答提问时用可能性限定：“这更可能是优先级的问题，而不是这个理念是否过时失效的问题”（P016）。",
                "对节约作用的限定：“节约有助于解决一切问题，但不是解决一切问题的唯一手段”（P016）。",
            ],
            "rhetoric_and_tone": (
                "论辩/驳论语气，攻击性强。开篇即给人扣“逻辑错误”的帽子，并讽刺对方“秀‘知识渊博’”。"
                "大量反问（“逻辑上都成立吗？”“真的可以在这些说法上加上‘因为’两个字吗？”“在中国有没有任何东西不必节约？”“可持续性不计算价值吗？”“将来的医疗费是不是还要看作‘GDP的进一步增长机会’？”）。"
                "用“对不起”转折加强讽刺；“反对的‘经济学家’们自己回去再学两年再出来说话”是直接训斥。"
                "夸张例证（每餐多吃一只鸡、吃出满大街胖子）承担反驳功能。"
                "整体结构是先驳他人、再立己说、最后回到提问给出解释，末句以否定式收束。"
            ),
            "unresolved_questions": [
                "正文末段 P018 为平台话题标签“社科答集”，混入正文且 lexical 结构未覆盖（渲染包标注“⚠lexical未覆盖片段”），属平台/编辑附加文本，作者归属待核，已单独登记。",
                "P001 原文“不用节约用水”的理念杯普遍认可”中“理念杯”疑为“被”字的错别字，与 brief 中同样写作“理念杯”一致，未作改动，属原文文字问题。",
                "“中国官方为中国人选择的民族性设计之一”的依据、提出主体与文献来源本文未说明（待外部核查）。",
                "“老龄一辈‘节俭狂情’”为作者的可观察描述，本文未给出经验数据。",
                "作者反驳的“经济学家”未指名，无法核对具体论点。",
                "“浪费促进经济”与“节约有助于解决一切问题”两处均用全称表述，本文未给出适用边界或反例。",
                "本篇 brief 为正文前约 140 字截断（去换行），与 P001-P002 重合，不作为独立证据。",
                "提问原文“为什么近来年节约用水呼声不像以前那么高了？”中“近来年”疑为“近年来”的笔误，属提问者文字，未作改动。",
            ],
            "evidence": [
                {"key": "E1", "paragraph_id": "P001", "quote": "很多人都犯了这么一个逻辑错误", "relation": "supports"},
                {"key": "E2", "paragraph_id": "P001", "quote": "误认为“缺少宣传”等于“不提倡”", "relation": "supports"},
                {"key": "E3", "paragraph_id": "P003", "quote": "逻辑上都成立吗？", "relation": "supports"},
                {"key": "E4", "paragraph_id": "P006", "quote": "节约是我们中国人娘胎里带来的国民性", "relation": "supports"},
                {"key": "E5", "paragraph_id": "P007", "quote": "“浪费促进经济”只是一种可以观察到的局部、短期现象", "relation": "contradicts"},
                {"key": "E6", "paragraph_id": "P007", "quote": "实则只是在通过扩大对环境的压力和对人类欲望本身的挖掘而去扩大交易额而已", "relation": "supports"},
                {"key": "E7", "paragraph_id": "P008", "quote": "那么的确什么也用不着节约", "relation": "qualifies"},
                {"key": "E8", "paragraph_id": "P008", "quote": "是否意味着我们肯定将来也一定做得到？", "relation": "supports"},
                {"key": "E9", "paragraph_id": "P009", "quote": "太平盛世根本就不意味着战乱不是转眼即来", "relation": "supports"},
                {"key": "E10", "paragraph_id": "P011", "quote": "无论富贵或贫穷，你都要节约", "relation": "supports"},
                {"key": "E11", "paragraph_id": "P011", "quote": "甚至认可这种精神价值本身就可以抵消一部分“由于节俭造成的浪费”", "relation": "supports"},
                {"key": "E12", "paragraph_id": "P012", "quote": "节俭是中国人的文化共识", "relation": "supports"},
                {"key": "E13", "paragraph_id": "P013", "quote": "节俭也是对的，节俭普遍正确", "relation": "supports"},
                {"key": "E14", "paragraph_id": "P013", "quote": "反对的“经济学家”们自己回去再学两年再出来说话", "relation": "contradicts"},
                {"key": "E15", "paragraph_id": "P014", "quote": "这个地球上就没有任何东西是不需要节约的", "relation": "supports"},
                {"key": "E16", "paragraph_id": "P016", "quote": "这更可能是优先级的问题，而不是这个理念是否过时失效的问题", "relation": "supports"},
                {"key": "E17", "paragraph_id": "P017", "quote": "但这并不意味着“以后不用节约了”或者“不必节水”", "relation": "supports"},
            ],
        },
        "provisional_tags": {
            "domain_candidates": ["资源与环境", "经济观念批评", "国民性与文化认同", "节水宣传"],
            "issue_candidates": ["节水呼声下降的原因", "浪费促进经济论", "节俭的正当性", "宣传优先级"],
            "text_function_candidates": ["答疑", "驳论", "评论", "训诫"],
            "object_candidates": ["中国人", "“经济学家”（未指名）", "国外（未指明国家）", "中国官方", "老一辈"],
            "working_keywords": ["节约用水", "节俭", "国民性", "浪费促进经济", "节俭狂情", "优先级", "社科答集（平台标签）"],
        },
        "notes": (
            "本篇无图片节点，正文 18 段全部读完，status=read、full_text_checked=true。"
            "注意：P018 是平台话题标签“社科答集”（text 字符 1378-1382），渲染包标注“⚠lexical未覆盖片段”，"
            "属平台/编辑附加文本而非作者论述，已登记在 unresolved_questions，未作为作者主张。"
            "原文“理念杯普遍认可”中的“杯”疑为“被”的错字，未改写原文。"
            "被作者反驳的说法（缺少宣传＝不提倡、浪费促进经济等）均以 opponent_view + attribution=opponent 记录，未归给作者。"
            "brief 为正文前约 140 字截断，与正文重合，不作为独立证据。"
        ),
    },
    # =====================================================================
    # 4/8 智力
    # =====================================================================
    "465e8f4f-b56b-56bd-b9fb-fb9d65f1abd8": {
        "analysis": {
            "question_context": (
                "提问者（Q001）问是否所有动物的智力都在发展、伴随人类的动物智力发展是否更快。"
                "作者先把问题引向“智力的来源”，拒绝用还原法定义智力，转而给出“对多样环境的应付力”定义，"
                "并区分“适应”与“应对”，再以“基因池长期稳定、亚种分布高度重叠”两条标准判断动物界的进展，"
                "最后对提问的第二问给出否定性判断：人类全球化趋同不利于动物智力发育。"
            ),
            "content_units": [
                {"unit_id": "U001", "paragraph_refs": ["P001"],
                 "summary": "把提问引向“智力的来源”这一思考角度。",
                 "role": "context"},
                {"unit_id": "U002", "paragraph_refs": ["P002"],
                 "summary": "认为智力不能走还原法（给思维一种原理性解释）来定义，但不否决该路线的实践意义：有助于生产力提升。",
                 "role": "claim"},
                {"unit_id": "U003", "paragraph_refs": ["P003"],
                 "summary": "给出智力定义：对多样环境的“应付力”，以在维持全部遗传特征前提下应付环境挑战、维持种群稳定繁衍的能力衡量；并区分“适应”（产生新种，不计入智力）与“应对”（无种群级基因变化，计入智力）。",
                 "role": "definition"},
                {"unit_id": "U004", "paragraph_refs": ["P004"],
                 "summary": "提出“智慧生物”的本质特征：基因池长期稳定、各“亚种”分布高度重叠，并以黑人分布在非洲与北极科考站为例。",
                 "role": "definition"},
                {"unit_id": "U005", "paragraph_refs": ["P005"],
                 "summary": "按两条标准判断：动物界尚无明显的进展，作者了解范围内没有物种呈现基因稳定性增长与亚种分布重叠性提高。",
                 "role": "conclusion"},
                {"unit_id": "U006", "paragraph_refs": ["P006"],
                 "summary": "让步与限定：猫科犬科已是“班上的头两名”，但有大量人类帮助，其亚种分布交叠主要因依附人类社会（指猎食人类活动带来额外猎物的野生种，不含宠物类），作者称这“算作弊”；家畜、宠物需另案考虑。",
                 "role": "qualification"},
                {"unit_id": "U007", "paragraph_refs": ["P007"],
                 "summary": "结论：人类的全球化和趋同性在要求动物适应高度相似的选择压力，从长期看更不利于动物种群的智力发育。",
                 "role": "conclusion"},
            ],
            "main_claims": [
                {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author",
                 "modality": "negated",
                 "statement": "作者认为智力并不能走还原法、从“尝试给思维一种原理性的解释”的路子去进行定义。",
                 "evidence": ["E1"]},
                {"claim_id": "C002", "claim_type": "author_qualified", "attribution": "author",
                 "modality": "asserted",
                 "statement": "作者让步地表示并不否决循还原路线进行探索的实践意义：尽管几乎不可能给出智力的定义，但却有助于生产力提升。",
                 "evidence": ["E2"]},
                {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author",
                 "modality": "asserted",
                 "statement": "作者提出智力的另一种定义：对多样环境的“应付力”——一个物种能在维持其全部遗传特征的前提下应付多复杂的环境挑战、维持种群稳定繁衍，就有多高的智力水准。",
                 "evidence": ["E3", "E4"]},
                {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author",
                 "modality": "asserted",
                 "statement": "作者区分“适应”与“应对”：被逼出长着耐火壳的新种叫“适应”，得分不计在“智力”项上；逼得物种学会看到你就跑或追着你要踩死你、没有造成任何种群级别的基因变化，叫“应对”，得分算在“智力”项下。",
                 "evidence": ["E5", "E6"]},
                {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author",
                 "modality": "asserted",
                 "statement": "作者认为细菌等看似无智力器官的物种并不违反该法则：适应新环境的细菌在逻辑上已是另一个种，两个种之间不能成绩叠加；就各个独立种而言细菌病毒的适应力极差。",
                 "evidence": ["E7"]},
                {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author",
                 "modality": "asserted",
                 "statement": "作者提出“智慧生物”直接关联到本质特征：基因池长期稳定、各个“亚种”分布高度重叠，并以黑人远不止分布在非洲、同样会分布在北极科考站为例。",
                 "evidence": ["E8", "E9"]},
                {"claim_id": "C007", "claim_type": "author_qualified", "attribution": "author",
                 "modality": "negated",
                 "statement": "作者按其两条标准判断：很遗憾，动物界尚无明显的进展；在自己的了解范围内，没有什么物种呈现基因稳定性的增长和亚种分布重叠性的提高。",
                 "evidence": ["E10", "E11"]},
                {"claim_id": "C008", "claim_type": "author_qualified", "attribution": "author",
                 "modality": "asserted",
                 "statement": "作者承认猫科犬科已是“班上的头两名”，但认为它们有大量人类帮助、其亚种分布交叠主要因依附于人类社会（指靠猎食人类活动带来的额外猎物的野生种，不是宠物类），因此“这个算作弊”；家畜、宠物需另案考虑。",
                 "evidence": ["E12", "E13"]},
                {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author",
                 "modality": "predicted",
                 "statement": "作者判断人类的全球化和趋同性在要求动物适应一种高度相似的选择压力，从长期看更加不利于动物种群的智力发育。",
                 "evidence": ["E14"]},
            ],
            "argument_steps": [
                "先把提问转译为“智力的来源”问题（P001）。",
                "排除还原法作为定义路径，但保留其在生产力上的实践意义（P002）。",
                "给出正面定义：智力＝对多样环境的“应付力”，以遗传特征不变前提下的环境应付与种群繁衍稳定来衡量（P003）。",
                "以“适应 vs 应对”的区分处理细菌等反例，说明只有不产生新种的应对才计入智力（P003）。",
                "提出“智慧生物”的两条本质特征，并以人类的分布为例（P004）。",
                "用这两条标准回答提问：动物界尚无明显的进展（P005）。",
                "对猫科犬科的表面反例作让步并排除：其优势来自人类帮助，算作弊，家畜宠物另案（P006）。",
                "给出反向结论：人类的全球化趋同不利于动物智力发育（P007）。",
            ],
            "concept_usage": [
                {"term": "智力", "meaning": "作者定义为对多样环境的“应付力”：在维持全部遗传特征的前提下应付复杂环境挑战、维持种群稳定繁衍的能力，可用天敌数与周期性环境挑战数比较。",
                 "evidence": "P003", "ambiguity": "该定义与常识或心理测量学的智力概念不同，作者未说明二者关系，也未给出量化方法。"},
                {"term": "适应/应对", "meaning": "作者用一对自设术语区分产生新种的基因层面变化（适应，不计智力）与不产生种群级基因变化的行为性应付（应对，计入智力）。",
                 "evidence": "P003", "ambiguity": "“种群级别的基因变化”的判定门槛本文未说明；生物学既有术语中“适应”含义与此不同。"},
                {"term": "智慧生物", "meaning": "作者以其两条标准界定：基因池长期稳定、各“亚种”分布高度重叠。",
                 "evidence": "P004", "ambiguity": "加引号的“亚种”用于人类时与生物学亚种概念的关系未说明。"},
                {"term": "作弊", "meaning": "作者用来评价猫科犬科借助人类帮助取得分布交叠的说法，表示该情形不计入其智力标准下的成绩。",
                 "evidence": "P006", "ambiguity": "口语化评价，非可操作标准。"},
                {"term": "全球化与趋同性", "meaning": "作者认为人类造成的、要求动物适应高度相似选择压力的过程，长期看不利于动物智力发育。",
                 "evidence": "P007", "ambiguity": "未给出时间尺度与作用机制。"},
            ],
            "examples_and_targets": [
                "细菌、病毒（P003）：作者举的反例，用来检验“应付力”定义是否适用于无智力器官的物种。",
                "被火烧出耐火壳的新种（P003）：作者的假设性举例，用来说明“适应”不计入智力。",
                "看到你就跑/追着你要踩死你（P003）：作者的假设性举例，用来说明“应对”计入智力。",
                "黑人远不止分布在非洲、同样会分布在北极科考站（P004）：作者举例说明“亚种分布高度重叠”，涉及人类群体，原文如此表述。",
                "猫科犬科（P006）：作者承认其为“班上的头两名”，但作为被排除的情形（依靠人类帮助、算作弊）。",
                "老鼠（P006）：作者举例说明依附人类社会的野生种所获得的额外猎物。",
                "家畜、宠物（P006）：作者明确列为“另案考虑”的对象。",
                "本文未给出数据、文献或具体研究。",
            ],
            "conditions": [
                "智力定义的限定前提：“在维持其全部遗传特征的前提下”（P003）。",
                "结论带认知范围限定：“在我的了解范围内”（P005）、“按照这两条标准”（P005）。",
                "对细菌例外的限定：以“适应了新环境的细菌，在逻辑上已经是另一个种”为前提，且“两个种之间并不能进行成绩叠加”（P003）。",
                "对猫科犬科情形的范围限定：只指靠猎食人类活动带来额外猎物的野生种，“不是指宠物类”（P006）。",
                "排除项：“家畜，宠物，都需要另案考虑”（P006）。",
                "时间尺度限定：“从长期看”（P007）。",
                "让步限定：“尽管这样几乎不可能给出智力的定义”（P002）。",
            ],
            "rhetoric_and_tone": (
                "定义式、分类式的学术口语混合体。以第一人称“我”出现两处（“但我并不是否决”“在我的了解范围内”）。"
                "使用课堂/班级比喻（“猫科犬科已经是班上的头两名”“这个算作弊”）。"
                "以“很遗憾的说”表达判断的态度色彩；以“换个说法”重述定义以便理解。"
                "整体先立定义、再处理反例、最后给判断，语气理性但夹带口语评价。"
            ),
            "unresolved_questions": [
                "“智力＝应付力”的定义如何量化（天敌数、周期性环境挑战数之外还看什么），本文未说明。",
                "“种群级别的基因变化”与“适应”的判定门槛本文未给出，生物学既有“适应”概念与作者的用法可能不同（待外部核查）。",
                "以“黑人”作为“亚种分布高度重叠”的例子，涉及把人类群体与生物学“亚种”并置，原文未加说明，可能引起歧义。",
                "“猫科犬科已经是班上的头两名”的依据（比较范围、数据来源）本文未给出。",
                "提问的第一问“是否所有动物的智力都在发展”未被逐类讨论，作者只给出“动物界尚无明显的进展”的一般判断。",
                "提问的第二问（伴随人类的动物智力发展是否更快）只由猫科犬科的排除作答，未讨论其他伴随人类的物种。",
                "本篇 brief 为正文前约 140 字截断（去换行），与 P001-P002 重合，不作为独立证据。",
            ],
            "evidence": [
                {"key": "E1", "paragraph_id": "P002", "quote": "智力并不能走还原法从“尝试给思维一种原理性的解释”的路子去进行定义", "relation": "supports"},
                {"key": "E2", "paragraph_id": "P002", "quote": "但我并不是否决循着这路线去进行探索的实践意义", "relation": "qualifies"},
                {"key": "E3", "paragraph_id": "P003", "quote": "即对多样环境的“应付力”", "relation": "supports"},
                {"key": "E4", "paragraph_id": "P003", "quote": "一个物种能够在维持其全部遗传特征的前提下应付多复杂的环境挑战维持种群稳定繁衍", "relation": "supports"},
                {"key": "E5", "paragraph_id": "P003", "quote": "这个叫做“适应”，得分不计在“智力”项上", "relation": "supports"},
                {"key": "E6", "paragraph_id": "P003", "quote": "这个叫“应对”，得分就算在“智力”项下", "relation": "supports"},
                {"key": "E7", "paragraph_id": "P003", "quote": "而就各个独立种而言，细菌病毒这类物种的适应力是极差的", "relation": "qualifies"},
                {"key": "E8", "paragraph_id": "P004", "quote": "基因池长期稳定; 各个“亚种”分布高度重叠", "relation": "supports"},
                {"key": "E9", "paragraph_id": "P004", "quote": "他同样会分布在北极科考站", "relation": "supports"},
                {"key": "E10", "paragraph_id": "P005", "quote": "动物界尚无明显的进展", "relation": "supports"},
                {"key": "E11", "paragraph_id": "P005", "quote": "在我的了解范围内", "relation": "qualifies"},
                {"key": "E12", "paragraph_id": "P006", "quote": "猫科犬科已经是班上的头两名，但是他们有大量的人类帮助", "relation": "qualifies"},
                {"key": "E13", "paragraph_id": "P006", "quote": "这个算作弊", "relation": "supports"},
                {"key": "E14", "paragraph_id": "P007", "quote": "更加不利于动物种群的智力发育", "relation": "supports"},
            ],
        },
        "provisional_tags": {
            "domain_candidates": ["演化生物学", "动物学", "认知科学（智力定义）"],
            "issue_candidates": ["智力的定义", "适应与应对的区分", "动物智力是否在增长", "人类活动对动物演化的影响"],
            "text_function_candidates": ["答疑", "概念界定", "论辩"],
            "object_candidates": ["细菌", "病毒", "猫科", "犬科", "家畜", "宠物", "黑人", "人类"],
            "working_keywords": ["智力", "应付力", "适应", "应对", "智慧生物", "基因池长期稳定", "亚种分布高度重叠", "作弊"],
        },
        "notes": (
            "本篇无图片节点，正文 7 段全部读完，status=read、full_text_checked=true。"
            "P004 原文用半角分号与空格写作“基因池长期稳定; 各个“亚种”分布高度重叠”，引用时按原文逐字复制。"
            "文中“黑人”一词为作者原文，仅作其“亚种分布重叠”举例记录，未作改写或评价。"
            "brief 为正文前约 140 字截断，与正文重合，不作为独立证据。"
        ),
    },
    # =====================================================================
    # 5/8 宁不畏死
    # =====================================================================
    "8a49d412-0d16-53de-8b16-89f95e650b50": {
        "analysis": {
            "question_context": (
                "提问者（Q001）问怎么处理对死亡的焦虑和恐惧。"
                "作者先安抚“慢慢自然会好”，再把死亡恐惧拆为文化心理与乐观期望两层原因，"
                "指出消除恐惧本身有代价（像退掉一份保险），给出“适应/保守治疗”与“向死而生”两种路径，"
                "并以“名正言顺的休息”为死亡问题上的最好样式作结。"
            ),
            "content_units": [
                {"unit_id": "U001", "paragraph_refs": ["P001", "P002"],
                 "summary": "安抚式开场（慢慢自然会好，不要担心），并提出死亡恐惧来自两个层面的原因。",
                 "role": "claim"},
                {"unit_id": "U002", "paragraph_refs": ["P003"],
                 "summary": "第一层文化心理：现存文明曾因人力资源不足而在军事与生产力斗争中失败，故不约而同把死亡恐怖化、负面化（并把生育与生存正面化甚至义务化）；社会化的人类普遍染上文化有意塑造的“恐死病”，恐死多发生在初高中阶段；但不应简单责怪“文明”，这是自然的安排，没有具体人或阶层负责，未设定该属性的文明趋向灭亡。",
                 "role": "reason"},
                {"unit_id": "U003", "paragraph_refs": ["P004"],
                 "summary": "第二层乐观期望：青少年处在“高势能”地位，未来预期之下死亡被识别为风险；在产生“无法完全防止一切死亡风险”的无力感时会产生强烈恐慌。",
                 "role": "reason"},
                {"unit_id": "U004", "paragraph_refs": ["P005"],
                 "summary": "治愈的代价：若失去对死亡的恐惧，容易导致对安全的漠视和对风险的低估；死亡恐惧像为生命买的保险，省掉保险费就接受了风险，并以反问“你确信这对你是净赚的吗？”要求权衡。",
                 "role": "qualification"},
                {"unit_id": "U005", "paragraph_refs": ["P006"],
                 "summary": "第二种治疗方式“适应”（保守治疗）：依靠刺激的边际效用随时间递减，随时间资本削薄与挫折使死亡重量下降、负面情绪处理经验增长，压力会降到管理能力之内，这也是绝大多数人的路径。",
                 "role": "action_advice"},
                {"unit_id": "U006", "paragraph_refs": ["P007", "P008", "P009"],
                 "summary": "另一条少有人走、更艰难也更美好的路：更深入认识死亡，去除对死亡非理性的恐惧、代之以尊重前提上的敬畏，明白人生最好的样式是向死而生；死亡问题上能有的最好样式是被告知必死时松一口气、欣喜于可以名正言顺地休息。",
                 "role": "action_advice"},
            ],
            "main_claims": [
                {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author",
                 "modality": "predicted",
                 "statement": "作者安抚提问者：慢慢自然会好，不要担心。",
                 "evidence": ["E1"]},
                {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author",
                 "modality": "asserted",
                 "statement": "作者认为对死亡的恐惧来自两个层面的原因（文化心理与人的乐观期望）。",
                 "evidence": ["E2"]},
                {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author",
                 "modality": "asserted",
                 "statement": "作者主张：对世界所有现存文明而言，曾经最大的恐惧是因人力资源不足而在军事和生产力斗争中失败，因此它们不约而同极力将死亡恐怖化和负面化（以及将生育和生存正面化甚至义务化），这是所有现代文明曾经的本能冲动。",
                 "evidence": ["E3"]},
                {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author",
                 "modality": "asserted",
                 "statement": "作者认为经过社会化的人类实际上普遍染上了文化有意塑造的“恐死病”，这也是恐死现象往往发生在初高中阶段的原因（该阶段人基本完成初步的社会化）。",
                 "evidence": ["E4", "E5"]},
                {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author",
                 "modality": "negated",
                 "statement": "作者认为不能简单责怪“文明”：这是自然的安排，并没有哪个具体的人或阶层要为此负责，而没有为自己的社会设定这个属性的文明也就趋向于灭亡了。",
                 "evidence": ["E6", "E7"]},
                {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author",
                 "modality": "asserted",
                 "statement": "作者认为死亡恐惧的第二层力量来自人的乐观期望：青少年处在“高势能”地位，未来预期之下死亡被识别为风险；在耳闻目睹意外死亡、产生无法完全防止一切死亡风险的无力感时会产生强烈恐慌。",
                 "evidence": ["E8", "E9"]},
                {"claim_id": "C007", "claim_type": "author_qualified", "attribution": "author",
                 "modality": "hypothetical",
                 "statement": "作者提醒治愈的代价：如果失去对死亡的恐惧，以当事人的阅历很容易导致对安全的漠视和对风险的低估，一个意外足以将人生马拉松变成四百米越野。",
                 "evidence": ["E10", "E11"]},
                {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author",
                 "modality": "asserted",
                 "statement": "作者认为死亡恐惧所造成的负担客观上就像为生命买的一份保险：省掉这笔保险费的同时也就接受了这项风险，并以“你确信这对你是净赚的吗？”要求读者权衡。",
                 "evidence": ["E12", "E13"]},
                {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author",
                 "modality": "predicted",
                 "statement": "作者提出“适应”这一保守治疗路径：依靠“刺激的边际效用随时间递减”，随年龄增长未来预期下滑、处理负面情绪经验增长，死亡造成的精神压力会降低到管理能力之内，并称这差不多也是绝大多数人的路径。",
                 "evidence": ["E14", "E15", "E16"]},
                {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author",
                 "modality": "asserted",
                 "statement": "作者提出还有一条少有人走、更艰难但更美好的路：更加深入认识死亡，去除对死亡非理性的恐惧，代之以尊重前提上的敬畏，明白人生本身最好的样式就是向死而生。",
                 "evidence": ["E17"]},
                {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author",
                 "modality": "asserted",
                 "statement": "作者认为人在死亡问题上能有的最好样式，就是此刻有人告诉你你已必死，你可以长出一口气，欣喜于终于可以名正言顺地休息。",
                 "evidence": ["E18"]},
            ],
            "argument_steps": [
                "以安抚语开场，并给出“两层原因”的分析框架（P001-P002）。",
                "展开第一层：文明的军事与生产力竞争压力→死亡恐怖化、生育与生存正面化→社会化的“恐死病”→恐死高发于初高中阶段（P003）。",
                "补充限定：不应责怪“文明”，这是自然安排且无具体责任主体，未如此设定的文明趋向灭亡（P003）。",
                "展开第二层：青少年的高势能与未来预期使死亡成为风险，意外死亡信息引发无力感与恐慌（P004）。",
                "指出治愈代价：失去恐惧会导致漠视安全、低估风险，恐惧相当于保险；以反问要求权衡（P005）。",
                "给出第一条路径：适应/保守治疗，等待刺激边际效用递减与时间资本变化，多数人走这条路（P006）。",
                "给出第二条路径：深入认识死亡、去除不合理恐惧、以敬畏替代，向死而生（P007-P008）。",
                "以“名正言顺的休息”作为死亡问题上的最好样式收束（P009）。",
            ],
            "concept_usage": [
                {"term": "“恐死病”", "meaning": "作者用来指经过社会化的人类普遍染上的、由文化有意塑造的死亡恐惧，类比为一种疾病。",
                 "evidence": "P003", "ambiguity": "带引号的自造比喻，非医学诊断，本文未给出判定标准。"},
                {"term": "保险", "meaning": "作者把死亡恐惧的负担比作为生命买的保险：省掉保险费也就接受了相应风险。",
                 "evidence": "P005", "ambiguity": "比喻的边界（保险费与保额如何对应）本文未说明。"},
                {"term": "“高势能”", "meaning": "作者用来描述青少年没有历史包袱、可塑性强、时间资本丰厚的人生位置。",
                 "evidence": "P004", "ambiguity": "物理比喻，未给出量化含义。"},
                {"term": "“保守治疗”/适应", "meaning": "作者指不去除症状、依靠对刺激的敏感性随时间递减而等待压力回落的方式。",
                 "evidence": "P006", "ambiguity": "与医学“保守治疗”的关系未说明，属类比用法。"},
                {"term": "向死而生", "meaning": "作者指更深入认识死亡、去除非理性恐惧，以尊重前提上的敬畏取代之，并把它当作人生最好的样式。",
                 "evidence": "P008", "ambiguity": "该表述的出处（常与存在主义哲学关联）本文未注明。"},
            ],
            "examples_and_targets": [
                "“自私的基因”及其遗传最大化策略与癌症的类比（P003）：作者借用的概念与类比材料，未注明出处。",
                "王朝必须人丁兴旺、意识形态必须广泛传承（P003）：作者举的文明层面例证。",
                "初高中阶段完成初步社会化、恐死现象多发（P003）：作者的经验性断言，未给数据。",
                "意外死亡案例与“无法完全防止一切死亡风险”的无力感（P004）：作者描述的情境。",
                "人生马拉松变成四百米越野（P005）：作者的比喻。",
                "刺激的边际效用随时间递减（P006）：作者借用的认知规律表述。",
                "本文未使用具体人物、机构、事件或统计数据。",
            ],
            "conditions": [
                "治愈路径的条件：“如果你失去对死亡的恐惧，以你的阅历很容易导致对安全的漠视和对风险的低估”（P005）。",
                "“适应”路径依赖的前提：“依靠接受‘刺激的边际效用随时间递减’的认知规律”（P006）。",
                "对多数人路径的限定：“这差不多也是绝大多数人的路径”（P006）。",
                "对文化原因的限定：“对世界所有的现存文明而言”“曾经最大的恐惧”“所有现代文明曾经的本能冲动”（P003），均用过去时与全称限定。",
                "恐死高发期的限定：“恐死现象往往发生在初高中阶段”（P003）。",
                "第二条路径的限定：“还有一条少有人走，更为艰难，但更为美好的路”（P007），明示其非普遍且更难。",
            ],
            "rhetoric_and_tone": (
                "安抚—分析—开方三段式，语气温和但在结论处抬高格调。开场白“慢慢自然会好，不要担心”直接安抚。"
                "大量医学隐喻：疾病、治愈、代价、保险、第二种治疗方式、保守治疗、症状稳定。"
                "反问：“你确信这对你是净赚的吗？”（P005）要求读者自省。"
                "引用式借用概念：“自私的基因”“刺激的边际效用随时间递减”“向死而生”，均未注明出处。"
                "结尾从“向死而生”落到“名正言顺的休息”这一具体画面，带有宽慰与解脱意味。整体第二人称“你”贯穿。"
            ),
            "unresolved_questions": [
                "“向死而生”的出处与确切含义本文未注明（常与存在主义哲学关联，待外部核查）。",
                "“自私的基因”为借用概念，本文未注明出处，也未说明其与死亡恐怖化的类推是否严格。",
                "“恐死现象往往发生在初高中阶段”的依据（样本、研究）本文未给出。",
                "对“所有现存文明”“所有现代文明”的概括性断言需要外部核查（本文未给文献）。",
                "两条路径（“适应”与“向死而生”）是否可以并用、先后关系如何，本文未说明。",
                "开场的“慢慢自然会好”与后文“适应/保守治疗”之间的关系本文未明说，读者可能读作同一路径或两种说法。",
                "作者未讨论恐惧程度达到病理水平时的处理方式，也未给出求助或干预建议。",
                "本篇 brief 为正文前约 140 字截断（去换行），与 P001-P003 重合，不作为独立证据。",
            ],
            "evidence": [
                {"key": "E1", "paragraph_id": "P001", "quote": "慢慢自然会好，不要担心。", "relation": "supports"},
                {"key": "E2", "paragraph_id": "P002", "quote": "对死亡的恐惧来自两个层面的原因。", "relation": "supports"},
                {"key": "E3", "paragraph_id": "P003", "quote": "曾经最大的恐惧就是因人力资源不足而在军事和生产力斗争中失败", "relation": "supports"},
                {"key": "E4", "paragraph_id": "P003", "quote": "经过社会化的人类实际上普遍染上了文化有意塑造的“恐死病”", "relation": "supports"},
                {"key": "E5", "paragraph_id": "P003", "quote": "这也是为什么恐死现象往往发生在初高中阶段", "relation": "supports"},
                {"key": "E6", "paragraph_id": "P003", "quote": "但我们并不能简单的去责怪“文明”", "relation": "supports"},
                {"key": "E7", "paragraph_id": "P003", "quote": "没有为自己的社会设定这个属性的文明也就趋向于灭亡了", "relation": "supports"},
                {"key": "E8", "paragraph_id": "P004", "quote": "青少年往往处在一个“高势能”地位", "relation": "supports"},
                {"key": "E9", "paragraph_id": "P004", "quote": "会产生强烈的恐慌", "relation": "supports"},
                {"key": "E10", "paragraph_id": "P005", "quote": "如果你失去对死亡的恐惧，以你的阅历很容易导致对安全的漠视和对风险的低估", "relation": "qualifies"},
                {"key": "E11", "paragraph_id": "P005", "quote": "一个意外足以将你的人生马拉松变成四百米越野", "relation": "supports"},
                {"key": "E12", "paragraph_id": "P005", "quote": "死亡恐惧所造成的负担，客观上就像你为生命买的一份保险", "relation": "supports"},
                {"key": "E13", "paragraph_id": "P005", "quote": "你确信这对你是净赚的吗？", "relation": "supports"},
                {"key": "E14", "paragraph_id": "P006", "quote": "你可以选择“保守治疗”", "relation": "supports"},
                {"key": "E15", "paragraph_id": "P006", "quote": "死亡所造成的精神压力很快会降低到你的管理能力之内", "relation": "supports"},
                {"key": "E16", "paragraph_id": "P006", "quote": "这差不多也是绝大多数人的路径。", "relation": "qualifies"},
                {"key": "E17", "paragraph_id": "P008", "quote": "明白人生本身最好的样式，就是向死而生", "relation": "supports"},
                {"key": "E18", "paragraph_id": "P009", "quote": "欣喜于你终于可以名正言顺的休息了", "relation": "supports"},
            ],
        },
        "provisional_tags": {
            "domain_candidates": ["死亡心理学", "文化批评", "人生哲学"],
            "issue_candidates": ["死亡恐惧的成因", "恐死与文化社会化", "恐惧的功能与代价", "向死而生的态度"],
            "text_function_candidates": ["答疑", "解释", "劝慰", "开方建议"],
            "object_candidates": ["青少年", "初高中阶段人群", "现存文明/现代文明", "社会", "提问者（未具名）"],
            "working_keywords": ["死亡恐惧", "恐死病", "文化心理", "高势能", "保守治疗", "适应", "向死而生", "保险"],
        },
        "notes": (
            "本篇无图片节点，正文 9 段全部读完，status=read、full_text_checked=true。"
            "提问者的焦虑处境仅见 Q001，已与作者主张区分；文中“自私的基因”“向死而生”等为作者借用但未注明出处的表述，已登记待核。"
            "brief 为正文前约 140 字截断，与正文重合，不作为独立证据。"
        ),
    },
    # =====================================================================
    # 6/8 无知的大脑
    # =====================================================================
    "0ff08f69-bf50-58c5-b400-0b38babbbcc6": {
        "analysis": {
            "question_context": (
                "提问者（Q001）问：为什么医学不发达的时候人们会认为人类的情感和认知会出自心脏而不是大脑。"
                "作者以生理感受与朴素归因作答（大脑几乎是无知觉器官，人更容易感受到心脏与情绪的关系），"
                "再补充另一角度：其他器官也曾被分工为思考器官，并指出“古人都认为心负责思考”是一种错误印象，"
                "最后补充魂魄类观点作为例外情形。"
            ),
            "content_units": [
                {"unit_id": "U001", "paragraph_refs": ["P001"],
                 "summary": "第一层回答：大脑几乎是无知觉器官，人感受不到来自大脑的输入信号，却能容易感受到心脏与情绪的关系，按朴素的归因方法很自然会以心脏为与思考直接相关的器官。",
                 "role": "claim"},
                {"unit_id": "U002", "paragraph_refs": ["P002"],
                 "summary": "另一角度：除心之外其他器官也扮演过思考器官的角色，很多文化把思维分类后分工给不同器官，这种思路在语言中留下大量遗迹；并指出“古人都认为心负责思考”是错误印象，因为大量规模较小的文明在殖民浪潮中未被记录就消亡，观点难以一概而论。",
                 "role": "claim"},
                {"unit_id": "U003", "paragraph_refs": ["P003"],
                 "summary": "补充特殊观点：认为思维是魂魄这类精神元素的功能，没有哪个器官负责思考，器官只是维持魂魄所寄居的肉身房屋的良好运转。",
                 "role": "example"},
            ],
            "main_claims": [
                {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author",
                 "modality": "asserted",
                 "statement": "作者认为原因在于大脑几乎是无知觉器官：人类感受不到来自大脑的任何输入信号，却可以很容易感受到心脏与情绪的关系。",
                 "evidence": ["E1"]},
                {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author",
                 "modality": "asserted",
                 "statement": "作者认为按照朴素的归因方法，人很自然会将心脏作为与思考直接相关的器官。",
                 "evidence": ["E2"]},
                {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author",
                 "modality": "asserted",
                 "statement": "作者补充另一角度：除心之外，其他器官并未见得没有扮演过思考器官的角色；很多文化喜欢将思维分类，然后分别分工给各个不同的器官。",
                 "evidence": ["E3"]},
                {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author",
                 "modality": "asserted",
                 "statement": "作者认为这种思路至今在语言里留下了大量的遗迹，并举把勇气归于胆、把怒火忧思归于肝、英美人把直觉归于guts为例。",
                 "evidence": ["E4"]},
                {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author",
                 "modality": "negated",
                 "statement": "作者断言“古人都认为心负责思考”是一种错误的印象。",
                 "evidence": ["E5"]},
                {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author",
                 "modality": "asserted",
                 "statement": "作者认为由于大量规模较小的文明（如美洲、非洲、相当部分的太平洋岛屿文明）在未被详加记录前就淹没在殖民浪潮中，它们的观点很难一概而论。",
                 "evidence": ["E6"]},
                {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author",
                 "modality": "asserted",
                 "statement": "作者补充另一种观点：思维是魂魄这类精神元素的功能，没有哪个器官在负责思考，器官只是负责维持魂魄所寄居的肉身房屋的良好运转。",
                 "evidence": ["E7"]},
            ],
            "argument_steps": [
                "给出直接答案：大脑几乎无知觉，人只能感受到心脏与情绪的关系，故朴素归因指向心脏（P001）。",
                "补充另一角度，把问题从“心 vs 脑”扩展为多器官分工（胆、肝、guts）（P002）。",
                "以语言遗迹为证据支持“思维被分类并分工给器官”的说法（P002）。",
                "反驳“古人都认为心负责思考”这一印象，理由是许多小规模文明未被记录即消亡，观点难以一概而论（P002）。",
                "补充魂魄类特殊观点，说明还存在不把思考归给任何器官的框架（P003）。",
            ],
            "concept_usage": [
                {"term": "无知觉器官", "meaning": "作者称大脑几乎是无知觉器官，指人感受不到来自大脑的输入信号。",
                 "evidence": "P001", "ambiguity": "该表述是作者的通俗说法，与生理学中内脏感觉的界定关系未说明。"},
                {"term": "朴素的归因方法", "meaning": "作者指人依据可直接感受到的身体信号来推断功能归属，因而把情绪与心脏联系起来。",
                 "evidence": "P001", "ambiguity": "未说明该归因是否为普遍心理机制，也未给出依据。"},
                {"term": "语言遗迹", "meaning": "作者指把思维分类并分工给器官的思路至今仍留在语言词汇中（胆—勇气、肝—怒火忧思、guts—直觉）。",
                 "evidence": "P002", "ambiguity": "未给出具体语源学证据或文献。"},
                {"term": "魂魄", "meaning": "作者转述的另一类观点中，思维所依附的精神元素；器官只是维持其寄居的肉身房屋。",
                 "evidence": "P003", "ambiguity": "未说明该观点属于哪些文化或文献，属“另外一些观点”的笼统转述。"},
            ],
            "examples_and_targets": [
                "把勇气归于胆、把怒火忧思归于肝、英美人把直觉归于guts（P002）：作者举的语言遗迹例证，包含一处英文词。",
                "美洲、非洲、相当部分的太平洋岛屿文明被殖民浪潮消灭、未及详加记录（P002）：作者举的历史例证，用于反驳“古人都认为心负责思考”。",
                "反驳对象：“古人都认为心负责思考”这一印象（P002），作者称之为错误的印象。",
                "“魂魄所寄居的肉身房屋”比喻（P003）：作者转述观点时的比喻。",
                "本文未给出数据、文献或具体人物。",
            ],
            "conditions": [
                "提问的前提“医学不发达的时候”属提问者，作者未直接讨论医学发展阶段与该观念的关系（见 unresolved_questions）。",
                "范围的限定：“很多文化”（P002）、“有大量的规模较小的文明”（P002）、“另外一些观点”（P003），均非全称。",
                "判断的限定：“它们的观点很难一概而论”（P002）。",
                "对第二问的补充以“这问题还有另一个角度”引入，属附加论证而非对原问题的替代（P002）。",
            ],
            "rhetoric_and_tone": (
                "简洁答疑体，先直答“因为……”，再以“这问题还有另一个角度”补充，最后以“另外一些观点”补充例外。"
                "用“譬如”连续举例（胆、肝、guts），以中英对照词例增强直观。"
                "以“实际上……是一种错误的印象”直接纠正流行印象，语气肯定但不训斥。"
                "末段语气转为描述性的“比较特殊”，不作评价。整体为解释、补充、例外三段式。"
            ),
            "unresolved_questions": [
                "提问以“医学不发达的时候”为前提，作者未讨论医学发展阶段与该观念的关系，也未说明该观念的时间范围。",
                "“英美人把直觉归于guts”涉及英语词汇，本文未给出语源或文献依据（待外部核查）。",
                "“有大量的规模较小的文明被消灭了……它们的观点很难一概而论”涉及殖民史与文明记录问题，本文未给出规模、地区或资料来源（待外部核查）。",
                "“另外一些观点”指哪些文化或文献，本文未说明，主体不明。",
                "“大脑几乎是无知觉器官”这一表述与头痛等可感知现象的界限，本文未讨论。",
                "本篇 brief 为正文前约 140 字截断（去换行），与 P001-P002 重合，不作为独立证据。",
            ],
            "evidence": [
                {"key": "E1", "paragraph_id": "P001", "quote": "因为大脑几乎是无知觉器官", "relation": "supports"},
                {"key": "E2", "paragraph_id": "P001", "quote": "很自然会将心脏作为与思考直接相关的器官", "relation": "supports"},
                {"key": "E3", "paragraph_id": "P002", "quote": "很多文化都喜欢将思维分类，然后分别分工给各个不同的器官", "relation": "supports"},
                {"key": "E4", "paragraph_id": "P002", "quote": "把勇气归于胆，把怒火忧思归于肝，英美人把直觉归于guts", "relation": "supports"},
                {"key": "E5", "paragraph_id": "P002", "quote": "是一种错误的印象", "relation": "contradicts"},
                {"key": "E6", "paragraph_id": "P002", "quote": "它们的观点很难一概而论", "relation": "qualifies"},
                {"key": "E7", "paragraph_id": "P003", "quote": "器官只是在负责维持魂魄所寄居的肉身房屋的良好运转而已", "relation": "supports"},
            ],
        },
        "provisional_tags": {
            "domain_candidates": ["认知史", "医学史", "语言与文化", "心理归因"],
            "issue_candidates": ["心脏与思考的关联", "思维器官的多元分工", "古人心脑观念的印象", "魂魄论"],
            "text_function_candidates": ["答疑", "解释", "纠误"],
            "object_candidates": ["大脑", "心脏", "胆", "肝", "英美人", "美洲文明", "非洲文明", "太平洋岛屿文明"],
            "working_keywords": ["无知觉器官", "朴素的归因方法", "思维分类", "语言遗迹", "guts", "魂魄", "肉身房屋"],
        },
        "notes": (
            "本篇无图片节点，正文 3 段全部读完，status=read、full_text_checked=true。"
            "文中“英美人把直觉归于guts”“被消灭的规模较小文明”等断言需外部核查，已登记；"
            "“古人都认为心负责思考”是作者引述并反驳的流行印象（opponent 性质的表述已在 examples_and_targets 说明），未归给作者。"
            "brief 为正文前约 140 字截断，与正文重合，不作为独立证据。"
        ),
    },
    # =====================================================================
    # 7/8 兽语
    # =====================================================================
    "d56b4f7f-b78d-5812-b784-a89b8027e4e1": {
        "analysis": {
            "question_context": (
                "提问者（Q001）问人为什么能说话而动物却不行。作者直接判定这是个误解，"
                "把问题转为语言定义的宽窄问题：若以沟通达意即算语言，则群居协作的动物都有语言；"
                "并进一步主张动物缺的不是语言而是文字，语言不能成为文明的基石，文字才能。"
            ),
            "content_units": [
                {"unit_id": "U001", "paragraph_refs": ["P001"],
                 "summary": "直接否定提问的前提（“这是个误解”）。",
                 "role": "rebuttal"},
                {"unit_id": "U002", "paragraph_refs": ["P002"],
                 "summary": "动物有没有语言取决于语言定义放得多宽；如果只以沟通达意即算语言，则所有群居协作的动物都有语言。",
                 "role": "claim"},
                {"unit_id": "U003", "paragraph_refs": ["P003"],
                 "summary": "结论性判断：动物不缺语言，缺的是文字；语言不是稀缺品，文字才是；语言本身不能成为文明的基石，文字才能。",
                 "role": "conclusion"},
            ],
            "main_claims": [
                {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author",
                 "modality": "negated",
                 "statement": "作者认为提问“人为什么能说话，而动物却不行”是个误解。",
                 "evidence": ["E1"]},
                {"claim_id": "C002", "claim_type": "author_qualified", "attribution": "author",
                 "modality": "hypothetical",
                 "statement": "作者认为动物有没有语言取决于把语言的定义放得有多宽：如果只是沟通达意即算语言，则所有的群居协作的动物都有语言。",
                 "evidence": ["E2", "E3"]},
                {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author",
                 "modality": "asserted",
                 "statement": "作者主张动物不缺语言，它们缺的是文字。",
                 "evidence": ["E4"]},
                {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author",
                 "modality": "asserted",
                 "statement": "作者主张语言并不是稀缺品，文字才是。",
                 "evidence": ["E5"]},
                {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author",
                 "modality": "negated",
                 "statement": "作者主张语言本身不能成为文明的基石，文字才能。",
                 "evidence": ["E6"]},
            ],
            "argument_steps": [
                "先否定提问前提，指出这是个误解（P001）。",
                "把问题转化为语言定义的宽窄问题，并给出条件式判断：以沟通达意即算语言则群居协作动物都有语言（P002）。",
                "给出结论性对比：动物缺的是文字；语言不是稀缺品而是文字；文明基石是文字而非语言（P003）。",
            ],
            "concept_usage": [
                {"term": "语言", "meaning": "作者认为其边界取决于定义宽窄；在最宽的定义（沟通达意）下，群居协作的动物都有语言。",
                 "evidence": "P002", "ambiguity": "作者未给出自己采用哪一种定义，也未区分“语言”与提问者所说的“说话”。"},
                {"term": "文字", "meaning": "作者认为文字才是稀缺品，是文明的基石，也是动物所缺的东西。",
                 "evidence": "P003", "ambiguity": "未给出文字的判定标准，也未说明文字与语言的关系。"},
                {"term": "文明的基石", "meaning": "作者用以说明语言与文字在文明形成中的地位：语言不能充当，文字才能。",
                 "evidence": "P003", "ambiguity": "未界定“文明”，也未给出论证。"},
            ],
            "examples_and_targets": [
                "被否定的前提：提问者“动物不行（不能说话）”的说法（Q001、P001）。",
                "“群居协作的动物”（P002）：作者举的泛指对象，未点具体物种。",
                "本文未使用具体例证、数据或文献。",
            ],
            "conditions": [
                "条件句：“如果只是沟通达意即算语言”（P002）。",
                "前提条件：“取决于你把语言的定义放得有多宽”（P002）。",
                "全篇未给出其他限定、时间、规模或风险条件。",
            ],
            "rhetoric_and_tone": (
                "极简答疑体，全文 3 段 110 字。开门一句“这是个误解。”直接否定前提。"
                "以“取决于你把语言的定义放得有多宽”把判断权交给定义选择，语气条件化。"
                "结尾用对偶短句作结（“动物不缺语言，他们缺的是文字。语言并不是稀缺品，文字才是。”），格言化、无例证、无展开。"
            ),
            "unresolved_questions": [
                "正文极短（110 字），作者未举例、未给文献，论证未展开。",
                "作者未说明自己采用何种语言定义，也未说明提问者的“说话”与作者讨论的“语言”是否同一概念。",
                "“文字才能（成为文明的基石）”只作断言，本文未给出理由或反例讨论。",
                "“群居协作的动物都有语言”为泛指，未点明具体物种，也未说明是否存在反例。",
                "本篇 brief（112 字）与正文几乎相同（正文 110 字，去换行后重合），不构成独立内容。",
            ],
            "evidence": [
                {"key": "E1", "paragraph_id": "P001", "quote": "这是个误解。", "relation": "contradicts"},
                {"key": "E2", "paragraph_id": "P002", "quote": "取决于你把语言的定义放得有多宽", "relation": "qualifies"},
                {"key": "E3", "paragraph_id": "P002", "quote": "则所有的群居协作的动物都有语言", "relation": "supports"},
                {"key": "E4", "paragraph_id": "P003", "quote": "动物不缺语言，他们缺的是文字", "relation": "supports"},
                {"key": "E5", "paragraph_id": "P003", "quote": "语言并不是稀缺品，文字才是", "relation": "supports"},
                {"key": "E6", "paragraph_id": "P003", "quote": "语言本身也不能成为文明的基石，文字才能", "relation": "supports"},
            ],
        },
        "provisional_tags": {
            "domain_candidates": ["语言与文字", "动物行为", "文明起源"],
            "issue_candidates": ["动物是否有语言", "语言与文字的稀缺性", "文明的基石"],
            "text_function_candidates": ["答疑", "纠误", "格言式判断"],
            "object_candidates": ["动物（泛指）", "群居协作的动物（泛指）"],
            "working_keywords": ["语言", "文字", "沟通达意", "群居协作", "文明的基石"],
        },
        "notes": (
            "本篇无图片节点，正文 3 段全部读完，status=read、full_text_checked=true。"
            "提问者的前提（动物不行）在 P001 被作者明确否定，未归给作者。"
            "brief（112 字）与正文基本相同，不构成独立内容。"
            "本篇篇幅极短（110 字），未展开论证，已在 unresolved_questions 登记。"
        ),
    },
    # =====================================================================
    # 8/8 自然状态下的雌性权利
    # =====================================================================
    "682f519d-c178-5ca4-a1a9-3da75ba2f1dc": {
        "analysis": {
            "question_context": (
                "提问者（Q001）问为什么动物界雄性不直接强奸雌性。"
                "作者以“动物中的‘女权’天然成立”作答，从雄性难以安全控制雌性、"
                "雌性重伤或感染会导致繁衍失败两条理由推出：以强奸作为普遍繁衍手段的胎生哺乳类等种群会灭绝，"
                "再讨论“强奸”概念在动物界的适用条件，并以海豚“群牧”行为作为近似案例与争议对象收束。"
            ),
            "content_units": [
                {"unit_id": "U001", "paragraph_refs": ["P001"],
                 "summary": "总答：基本上动物中的“女权”是天然成立的。",
                 "role": "claim"},
                {"unit_id": "U002", "paragraph_refs": ["P002", "P003", "P004"],
                 "summary": "两条理由：其一，若雌性不接受或不配合，雄性很少能安全控制雌性，搏斗中雄性出血受伤并感染会致命；其二，若雌性受伤过重或严重感染，即使受孕繁衍也会失败（对卵生自然孵化的动物无效），搏斗与目的自相矛盾。因此对胎生、哺乳类或幼仔成长严重依赖母亲健康与照料的动物，以强奸为普遍繁衍手段的种群很自然会灭绝。",
                 "role": "reason"},
                {"unit_id": "U003", "paragraph_refs": ["P005", "P006"],
                 "summary": "限定：恰恰是这类动物才有足够的社会性，使“强奸”这个概念变得有实际意义；否则很难定性一种在人类看来很暴力的交配礼仪是否算“强奸”。",
                 "role": "qualification"},
                {"unit_id": "U004", "paragraph_refs": ["P007"],
                 "summary": "另一类情形：环节动物、软体动物、昆虫这些类别可能存在暴力交配行为，但一般认为蜗牛、蚯蚓、贝壳不存在智能；既然不存在可被强迫的意志，就不能把它们的性行为看作强奸。",
                 "role": "qualification"},
                {"unit_id": "U005", "paragraph_refs": ["P008"],
                 "summary": "让步与争议：这并不能理解为动物没有近似强奸的行为，海豚存在“群牧”行为（雄海豚在同伴协助下围追堵截雌性发生性行为）；但该行为应定义为特殊交配礼仪还是强奸存在争议；雌性海豚会展现逃避，帮手也未厉害到把它按倒在海床上，而以海豚的游泳技能，若完全不配合，恐怕没有其他海豚能真正做到“强奸”。",
                 "role": "qualification"},
            ],
            "main_claims": [
                {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author",
                 "modality": "asserted",
                 "statement": "作者认为基本上动物中的“女权”是天然成立的。",
                 "evidence": ["E1"]},
                {"claim_id": "C002", "claim_type": "author_qualified", "attribution": "author",
                 "modality": "hypothetical",
                 "statement": "作者提出朴素的道理：如果雌性不接受或者不配合，雄性很少有能力安全地控制雌性；哪怕经过搏斗可能制服雌性，但如果雌性全力抵抗，雄性受到出血伤的可能性很大，如果感染就会致命。",
                 "evidence": ["E2", "E3"]},
                {"claim_id": "C003", "claim_type": "author_qualified", "attribution": "author",
                 "modality": "hypothetical",
                 "statement": "作者提出更深刻的危险：如果雌性受伤过重或者发生严重感染，则即使雌性受孕繁衍也将失败（这一点对卵生自然孵化的动物无效），于是这种搏斗本身就和试图达成的目的自相矛盾。",
                 "evidence": ["E4", "E5"]},
                {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author",
                 "modality": "predicted",
                 "statement": "作者推出：因此对于胎生、哺乳类动物或者幼仔成长严重依赖于母亲的健康和照料的动物，依靠异性间的强奸作为普遍繁衍手段的种群很自然会灭绝。",
                 "evidence": ["E6"]},
                {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author",
                 "modality": "asserted",
                 "statement": "作者认为恰恰往往是这一类动物才有足够的社会性，使得“强奸”这个概念变得有实际意义。",
                 "evidence": ["E7"]},
                {"claim_id": "C006", "claim_type": "author_qualified", "attribution": "author",
                 "modality": "qualified",
                 "statement": "作者认为在环节动物、软体动物、昆虫这些类别里可能存在这种暴力交配行为；但一般来说我们并不认为蜗牛、蚯蚓、贝壳存在什么智能，既然不存在可被强迫的意志，自然也就不能把它们的任何性行为看作强奸。",
                 "evidence": ["E8", "E9"]},
                {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author",
                 "modality": "negated",
                 "statement": "作者强调这并不能理解为动物没有近似强奸的行为，并举海豚“群牧”行为为例（雄海豚在同伴协助下围追堵截雌性海豚发生性行为）。",
                 "evidence": ["E10", "E11"]},
                {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author",
                 "modality": "questioned",
                 "statement": "作者指出：即使如此，海豚“群牧”行为应被定义为特殊的交配礼仪还是一种强奸，是存在争议的。",
                 "evidence": ["E12"]},
                {"claim_id": "C009", "claim_type": "author_qualified", "attribution": "author",
                 "modality": "hypothetical",
                 "statement": "作者以海豚的游泳技能作反推：如果雌海豚完全不配合，恐怕世界上没有其他海豚能做到真正的“强奸”。",
                 "evidence": ["E13"]},
            ],
            "argument_steps": [
                "以“动物中的‘女权’天然成立”作总答（P001）。",
                "理由一：雌性不配合时雄性难以安全控制，搏斗中雄性出血受伤、感染致命（P002）。",
                "理由二：雌性受伤过重或严重感染会使受孕后的繁衍也失败（卵生自然孵化者除外），搏斗与繁衍目的自相矛盾（P003）。",
                "由两条理由推出结论：胎生、哺乳类或幼仔依赖母亲的物种，以强奸为普遍繁衍手段的种群会灭绝（P004）。",
                "限定概念适用条件：只有这类有社会性的动物才使“强奸”有意义，否则难以定性暴力交配礼仪（P005-P006）。",
                "处理无智能类别：环节动物、软体动物、昆虫可能有暴力交配，但无被强迫的意志，不算强奸（P007）。",
                "让步并保留争议：动物存在近似强奸行为（海豚“群牧”），其定性有争议；以海豚游泳技能反推“真正强奸”的可能性（P008）。",
            ],
            "concept_usage": [
                {"term": "“女权”", "meaning": "作者借人类性别权利话语作类比，指动物中雌性在交配选择上实际拥有不接受或不配合的能力与地位。",
                 "evidence": "P001", "ambiguity": "带引号的类比用法，作者未界定其与人类女权概念的关系。"},
                {"term": "“强奸”", "meaning": "作者讨论其在动物界的适用条件：需要有可被强迫的意志与足够的社会性，否则只能算特殊的交配礼仪或暴力交配行为。",
                 "evidence": "P005、P006、P007、P008", "ambiguity": "作者指出其定义在学界/观察者中存在争议，但未给出判定标准。"},
                {"term": "“群牧”", "meaning": "作者描述的海豚行为：雄海豚在一帮其他雄海豚协助下围追堵截雌性海豚发生性行为。",
                 "evidence": "P008", "ambiguity": "术语加引号，本文未说明该名称的来源与行为学定义。"},
                {"term": "意志", "meaning": "作者用来判断能否构成“强奸”的前提：不存在可被强迫的意志，就不能把性行为看作强奸。",
                 "evidence": "P007", "ambiguity": "哪些物种具有“意志”本文未给出判定标准。"},
                {"term": "社会性", "meaning": "作者认为只有具备足够社会性的动物，才使“强奸”概念有实际意义。",
                 "evidence": "P005", "ambiguity": "“足够的社会性”如何衡量本文未说明。"},
            ],
            "examples_and_targets": [
                "海豚“群牧”行为（P008）：作者举的近似强奸的实例，同时作为定性存在争议的对象。",
                "雌性海豚的逃避、帮手未把雌海豚按倒在海床上、海豚的游泳技能（P008）：作者用来说明“真正强奸”难以成立的反推材料。",
                "环节动物、软体动物、昆虫（P007）：作者承认可能存在的暴力交配类别。",
                "蜗牛、蚯蚓、贝壳（P007）：作者举的无智能、无被强迫意志的例子。",
                "胎生、哺乳类动物、幼仔成长严重依赖母亲的动物（P004）：作者结论所限定的对象范围。",
                "卵生自然孵化的动物（P003）：作者明确标注的例外。",
                "被部分质疑的框架：提问者“雄性不直接强奸雌性”的说法（Q001）——作者既未全盘接受该框架，也讨论了其可定义性。",
                "本文未给出数据、文献或具体研究出处。",
            ],
            "conditions": [
                "条件句密集：“如果雌性不接受或者不配合”“哪怕经过一番搏斗可能制服雌性，但如果雌性全力抵抗”“如果感染就会致命”（P002）。",
                "“如果雌性受伤过重或者发生严重感染，则即使雌性受孕，繁衍也将失败”（P003），并以括号明示例外“这一点对于卵生自然孵化的动物无效”。",
                "结论适用范围限定：“对于胎生、哺乳类动物或者幼仔成长严重依赖于母亲的健康和照料的动物”（P004）。",
                "可能性限定：“可能存在这种暴力交配行为”“一般来说”“恐怕”“很自然”等（P004、P007、P008）。",
                "争议限定：“是存在争议的”（P008）。",
                "判断前提：只有存在“可被强迫的意志”与“足够的社会性”才可讨论强奸（P005、P007）。",
            ],
            "rhetoric_and_tone": (
                "因果解释体，开门以“因为……”直答。分层推进：先说“一个很朴素的道理”，再说“更深刻的危险”，形成递进。"
                "使用人类法律/道德词汇（强奸、女权、交配礼仪、意志）讨论动物行为，并反复讨论这些词的适用边界。"
                "以“但请注意”提醒读者不要误读（P008）；结尾用“恐怕”加条件句作反推，语气是或然而非断言。"
                "全篇无情绪化攻击，属于就概念适用性作辨析的说明文。"
            ),
            "unresolved_questions": [
                "“女权”作为类比术语的界定本文未说明，作者只以引号提示其为借用说法。",
                "“强奸”在动物行为学中的判定标准（是否需要“意志”、如何认定强迫）本文未给出文献或定义来源（待外部核查）。",
                "海豚“群牧”行为的名称、观察来源与行为学描述本文未给出出处（待外部核查）。",
                "“这一点对于卵生自然孵化的动物无效”这一例外的理由本文未展开说明。",
                "“足够的社会性”“不存在可被强迫的意志”的判定标准本文未说明，哪些物种适用并不清楚。",
                "提问者以“雄性不直接强奸雌性”为前提（Q001），作者部分接受该问题框架，但也质疑动物界“强奸”是否可被定义，二者的关系本文未明确表态。",
                "本篇 brief 为正文前约 140 字截断（去换行），与 P001-P003 重合，不作为独立证据。",
            ],
            "evidence": [
                {"key": "E1", "paragraph_id": "P001", "quote": "因为基本上动物中的“女权”是天然成立的。", "relation": "supports"},
                {"key": "E2", "paragraph_id": "P002", "quote": "如果雌性不接受或者不配合，雄性很少有能力可以安全的控制雌性", "relation": "supports"},
                {"key": "E3", "paragraph_id": "P002", "quote": "如果感染就会致命", "relation": "supports"},
                {"key": "E4", "paragraph_id": "P003", "quote": "这一点对于卵生自然孵化的动物无效", "relation": "qualifies"},
                {"key": "E5", "paragraph_id": "P003", "quote": "于是这种搏斗本身就是和试图达成的目的自相矛盾的", "relation": "supports"},
                {"key": "E6", "paragraph_id": "P004", "quote": "依靠异性间的强奸作为普遍繁衍手段的种群很自然是会灭绝的", "relation": "supports"},
                {"key": "E7", "paragraph_id": "P005", "quote": "而恰恰往往是这一类动物才有足够的社会性", "relation": "supports"},
                {"key": "E8", "paragraph_id": "P007", "quote": "在环节动物、软体动物、昆虫这些类别里可能存在这种暴力交配行为", "relation": "qualifies"},
                {"key": "E9", "paragraph_id": "P007", "quote": "既然不存在可被强迫的意志，自然也就不能把它们的任何性行为看作强奸了", "relation": "supports"},
                {"key": "E10", "paragraph_id": "P008", "quote": "但这并不能理解为动物没有近似强奸的行为", "relation": "supports"},
                {"key": "E11", "paragraph_id": "P008", "quote": "海豚就存在“群牧”行为", "relation": "supports"},
                {"key": "E12", "paragraph_id": "P008", "quote": "是存在争议的", "relation": "qualifies"},
                {"key": "E13", "paragraph_id": "P008", "quote": "如果完全不配合，恐怕世界上没有其他海豚能做到真正的“强奸”", "relation": "qualifies"},
            ],
        },
        "provisional_tags": {
            "domain_candidates": ["动物行为学", "演化生物学", "性与性别（概念移植）"],
            "issue_candidates": ["动物交配中的强迫", "强奸概念在动物界的适用性", "雌性选择与繁衍策略", "海豚群牧行为"],
            "text_function_candidates": ["答疑", "解释", "概念辨析"],
            "object_candidates": ["雌性/雄性（泛指）", "胎生哺乳类动物", "卵生自然孵化的动物", "环节动物", "软体动物", "昆虫", "蜗牛", "蚯蚓", "贝壳", "海豚"],
            "working_keywords": ["女权", "强奸", "群牧", "交配礼仪", "意志", "社会性", "卵生自然孵化"],
        },
        "notes": (
            "本篇无图片节点，正文 8 段全部读完，status=read、full_text_checked=true。"
            "文中“强奸”“女权”等词均为作者原文用词，用于讨论概念在动物行为上的适用条件，未作改写或评价；"
            "海豚“群牧”等事实性描述需外部核查，已登记。"
            "提问者“雄性不直接强奸雌性”的前提属提问者，已与作者主张区分。"
            "brief 为正文前约 140 字截断（去换行），与正文重合，不作为独立证据。"
        ),
    },
}


def main():
    rows = load_batch_rows(BATCH)
    records = []
    for row in rows:
        art = row["article"]
        aid = art["id"]
        if aid not in ANALYSIS:
            raise SystemExit("ANALYSIS 缺少文章 %s（%s）" % (aid, art.get("title")))
        payload = ANALYSIS[aid]
        records.append(
            build_record(
                row,
                row["batch_id"],
                row["corpus_sha256"],
                payload["analysis"],
                payload["provisional_tags"],
                STARTED,
                COMPLETED,
                status=payload.get("status", "read"),
                full_text_checked=payload.get("full_text_checked", True),
                image_checked=payload.get("image_checked", False),
                notes=payload.get("notes", ""),
            )
        )
    extra = set(ANALYSIS) - {r["article"]["id"] for r in rows}
    if extra:
        raise SystemExit("ANALYSIS 含不属于本批次的 id: %s" % ", ".join(sorted(extra)))
    write_jsonl(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "out", BATCH + ".out.jsonl"),
        records,
    )
    print("ok %s -> out/%s.out.jsonl (%d records)" % (BATCH, BATCH, len(records)))


if __name__ == "__main__":
    main()
