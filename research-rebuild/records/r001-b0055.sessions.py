# -*- coding: utf-8 -*-
"""批次 r001-b0055 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0055.sessions.py            # 写 out/r001-b0055.out.jsonl
  python3 records/r001-b0055.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0055"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0055.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "3341745d": {
  "analysis": {
   "question_context": "提问者问“为什么有人会想出卖自己的国家和民族?”（Q001，属提问者）。作者没有直接解释动机，而是先针对一种流行说法——“你只是个老百姓，你没能力/轮不到你出卖国家民族”——展开事实层面的反驳：举出普通人参与卖国行为的反例，给出“卖国”的定义，区分事实定性与道德批判、是否追究，最后把重点从“卖国”转到识别身边“会卖你”的人。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "树起将被反驳的流行说法并反问其是否经思考。", "role": "context"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005", "P006", "P007", "P008"], "summary": "以转发谣言换绿卡者、作假见证混庇护者、连登仔、王立强等反例，反驳“平头老百姓卖不了国”。", "role": "rebuttal"},
    {"unit_id": "U003", "paragraph_refs": ["P009", "P010"], "summary": "自我限定：只作事实判断层面的反驳，不含对卖国行为的道德批判。", "role": "qualification"},
    {"unit_id": "U004", "paragraph_refs": ["P011", "P012", "P013", "P014"], "summary": "给出“卖国”定义，并主张伦理定性只看性质、与追究与否无关。", "role": "definition"},
    {"unit_id": "U005", "paragraph_refs": ["P015", "P016", "P017", "P018", "P019"], "summary": "让步划界：可主张不予追究或论证其正当，但不能因额度小否认其符合定义；以细菌为类比。", "role": "qualification"},
    {"unit_id": "U006", "paragraph_refs": ["P020", "P021", "P022", "P023", "P024"], "summary": "回应本题：人可出卖的对象远不止国家民族，且都不少见。", "role": "claim"},
    {"unit_id": "U007", "paragraph_refs": ["P025", "P026", "P027", "P028"], "summary": "自省式限定：什么都不出卖者极少，作者不排除自己在自欺。", "role": "qualification"},
    {"unit_id": "U008", "paragraph_refs": ["P029", "P030", "P031", "P032"], "summary": "指出多数人靠抬高“出卖”的认证线自我豁免，并以“小”的系数讽刺。", "role": "reason"},
    {"unit_id": "U009", "paragraph_refs": ["P033", "P034"], "summary": "行动建议：见微知著识别这类人，在社会生态中悄悄末位淘汰并持续降低特征指数。", "role": "action_advice"},
    {"unit_id": "U010", "paragraph_refs": ["P035", "P036", "P037", "P038", "P039"], "summary": "结论：真正要害是“会卖你”的人，须将其排除出自己的社会生态系统。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "opponent_view", "attribution": "opponent", "modality": "asserted", "statement": "被作者反驳的流行说法：普通人只是老百姓，没有能力、也轮不到出卖国家民族。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "该说法经不起推敲：转发境外谣言换绿卡、作假见证混庇护、挥舞殖民旗闹事、王立强等反例，都不需要特殊文凭或职位。", "evidence": ["E2", "E3"]},
    {"claim_id": "C003", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "作者声明其反驳仅限于事实判断层面，不含对卖国行为的道德批判；卖国是各人自己决定并承担后果的现实选择。", "evidence": ["E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者给“卖国”的定义：在尝试获得个人利益的过程中有意无视对国家利益的损害；伦理上只看性质，不计金额大小与情节轻重。", "evidence": ["E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "按此定义，为自爽在公共论坛转发削弱社会契约总体信用的谣言，性质上已是不折不扣的出卖国家利益。", "evidence": ["E6", "E7"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "他人是否也这样做、实际损害多大、该不该或能不能追究，都与事实定性无关；可以主张按成本效率不予追究，甚至论证该行为正当，但不能因额度小就否认它符合定义。", "evidence": ["E8", "E9"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人类能出卖的不止国家民族，卖兄弟、同志、组织、客户、恩人、朋友、父母乃至自己都不少见。", "evidence": ["E10"]},
    {"claim_id": "C008", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "在“真的懂行、洞察本质”的前提下，幸运或勇敢到什么都不出卖的人是极其少数；作者不敢自称属于该少数，因为可能潜在地把出卖朋友解释为“正当”而自欺成功。", "evidence": ["E11", "E12"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "多数人只是抬高“出卖”的认证线来自我豁免（小偷不算偷、小骂不算骂等），所谓“小”是随通胀年年上涨的神秘系数。", "evidence": ["E13", "E14"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "应做的不是感叹，而是见微知著地识别这类人并悄无声息地末位淘汰；做不到完全清除，因为人是有限生物，但可以持续降低个人社会生态环境中的特征指数水平。", "evidence": ["E15", "E16", "E17"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "出卖国家民族自有系统的力量去对抗，真正要害的是“会卖你”的人；对这类人出卖已是无法觉察、已被自行justify的潜意识习惯。", "evidence": ["E18", "E19"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "学会觉察迹象并把这类危险分子排除出自己的社会生态系统，是有效实现人生追求至关重要的技能之一。", "evidence": ["E20"]}
   ],
   "argument_steps": [
    "先引述并质疑流行说法“老百姓没能力/轮不到卖国”（P001-P002）。",
    "以若干普通人反例反问该说法，指出这些行为不需要特殊文凭或职位（P003-P005）。",
    "反问“谁说平头老百姓卖不了国”，并判定该俏皮话根本经不起推敲、说者与点赞者未经思考（P006-P008）。",
    "自我限定：仅作事实判断上的反驳，不构成道德批判（P009-P010）。",
    "给出“卖国”定义，并说明伦理只考虑性质不考虑金额与情节（P011）。",
    "据此把转发损害社会契约信用的谣言定性为出卖国家利益；说明买家是自己、被削弱的是全体国民共同利益（P012-P013）。",
    "把“他人是否也做、损害多大、该不该/能不能追究”划出事实定性之外（P014）。",
    "让步：可以主张低于限度不予追究（公共政策博弈），甚至论证该行为正当，但不能因额度小否认其符合定义；类比“细菌很小，不算生物”（P015-P019）。",
    "回到本题：人可出卖的对象极广，都不少见（P020-P024）。",
    "自省让步：什么都不出卖者极少，作者不能凭自查无碍断言自己没有，甚至“既然我是人，我肯定有”（P025-P028）。",
    "归因：多数人抬高认证线来自我豁免，“小”是神秘系数；很多人为更小的利卖掉更重的东西（P029-P032）。",
    "行动建议：识别并末位淘汰、持续降低特征指数；承认做不到完全清除（P033-P034）。",
    "结论：卖国自有系统对抗，真正关键是会卖你的人，须排除出社会生态（P035-P039）。"
   ],
   "concept_usage": [
    {"term": "卖国/出卖", "meaning": "本文给出明确界定：在尝试获得个人利益的过程中有意无视对国家利益的损害（P011）；并强调伦理定性只看性质（P011）。", "evidence": "P011", "ambiguity": "作者自称给出的是清晰定义，但“国家利益”的判断主体与边界未说明；文中“出卖”还被扩展到朋友、组织、父母、自己等对象（P023）。"},
    {"term": "事实判断/道德批判", "meaning": "作者区分二者：其反驳只在事实层面，不包含对卖国行为的道德批判（P009）。", "evidence": "P009", "ambiguity": "作者同时说卖国是每个人都得自己决定并承担后续影响的现实选择，事实判断与伦理评价的界线在文中未完全展开（P009）。"},
    {"term": "社会契约的总体信用", "meaning": "被视为无可置疑的全体国民共同利益，转发谣言削弱它即构成对国家利益的损害（P012-P013）。", "evidence": "P013", "ambiguity": "该信用的构成、可观测与可衡量方式本文未说明。"},
    {"term": "事实定性", "meaning": "指行为是否落入“卖国”定义，作者主张它与是否追究、损害大小无关（P014）。", "evidence": "P014", "ambiguity": "与“该不该追究”的公共政策讨论如何衔接，本文只作划界，未给判准。"},
    {"term": "特征指数", "meaning": "个人社会生态环境中可用于识别“会出卖”倾向的某种指标，作者建议持续降低其水平（P033-P034）。", "evidence": "P034", "ambiguity": "本文未定义该指数的内容、如何观测与计算。"},
    {"term": "见微知著/末位淘汰", "meaning": "从细微迹象识别这类人并在自己的社会生态中悄然淘汰（P033）。", "evidence": "P033", "ambiguity": "“末位淘汰”的具体做法与适用场景未说明。"}
   ],
   "examples_and_targets": [
    "“你只是个老百姓，你没能力/轮不到你出卖国家民族”——被反驳的流行说法（P001）。",
    "疫情期间系统往国内转发境外系统编造的谣言以换绿卡的flg——作者举的反例（P003）；指称与事实断言需外部核查。",
    "公开作假见证、自称回国会被迫害以混庇护者——作者举的反例（P003）。",
    "挥舞殖民旗、砸店铺、发谣言、害死老人、烧活人的连登仔——作者举的反例（P004）；事实需外部核查。",
    "“澳洲共谍”王立强——作者举的反例，以反问其并非位高权重（P005）；身份与事件需外部核查。",
    "“细菌很小，不算生物”——归谬类比（P018）。",
    "“小偷不算偷，小骂不算骂，小抢不算抢，小卖不算卖”——排比式修辞与讽刺（P030）。",
    "“见神卖神，见佛卖佛，见你卖你”——修辞性排比（P037）。"
   ],
   "conditions": [
    "作者自设限定：其反驳只针对事实判断，不含道德批判（P009）。",
    "讨论以“卖国”被清晰定义出来为前提：“只要你把‘卖国’清晰的定义出来”（P011）。",
    "伦理认定不考虑金额大小与情节轻重，仅考虑性质（P011）。",
    "允许主张低于一定限度或特定情节按成本效率原则不予追究，此为公共政策博弈问题（P015）。",
    "允许论证该行为本身正当、被污名化，但不允许因额度小否认其符合定义（P016、P017）。",
    "关于“什么都不出卖者极少”的判断以“如果你真的懂行/真的洞察本质”为条件（P025）。",
    "作者承认完全清除做不到，因为人是有限生物（P033）。",
    "作者的自省带假设语气：可能只是潜意识为自己脱罪、自欺成功（P027）。"
   ],
   "rhetoric_and_tone": "驳论与训诫混合的冷峻语调。连续使用反问（P002、P003、P004、P006），把对方说法称为“俏皮话”“根本经不起推敲”，以“细菌很小，不算生物”作归谬类比，以“小偷不算偷……”四连排比讽刺自我豁免，以“见神卖神，见佛卖佛，见你卖你”三连排比收束。用词口语化且带挖苦（“心里爽一爽”“没有二两猪肉重”）。末段从反驳转为对读者的行动训诫（P033-P038）。文中夹用英文词“justify”（P036）。",
   "unresolved_questions": [
    "flg 的指称与“转发境外谣言换绿卡”的具体事实需外部核查（P003）。",
    "王立强“澳洲共谍”的身份与相关事件需外部核查（P005）。",
    "“社会契约的总体信用”如何界定与衡量，本文未说明（P013）。",
    "“特征指数”如何量化、观察与降低，本文未说明（P033-P034）。",
    "“末位淘汰”在个人社会生态中具体指什么做法，本文未说明（P033）。",
    "“国家利益”由谁判断、边界何在，本文未说明。",
    "“人性本可如此”的作者断言（P028）属其个人判断，未给论证。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "我发现很多人喜欢说这句话——“你只是个老百姓，你没能力/轮不到你出卖国家民族”。", "relation": "context"},
    {"key": "E2", "paragraph_id": "P003", "quote": "那些公开作假见证好自称回国会被迫害混庇护的，需要什么特殊文凭或者职位？", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P005", "quote": "那位“澳洲共谍”王立强是什么位高权重之人？", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P009", "quote": "我这只是做一种事实判断上的反驳。上面这段话并不包含对卖国行为的道德批判", "relation": "qualifies"},
    {"key": "E5", "paragraph_id": "P011", "quote": "在尝试获得个人利益的过程中有意无视对国家利益的损害", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P012", "quote": "这就已经从性质上属于不折不扣的出卖国家利益了。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P013", "quote": "社会契约的总体信用被削弱是无可置疑的全体国民共同利益。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P014", "quote": "这些都跟这个事实定性没有关系。", "relation": "qualifies"},
    {"key": "E9", "paragraph_id": "P017", "quote": "但你不能主张符合这个定义的行为因为额度小、尺寸小就不算符合这个定义。", "relation": "qualifies"},
    {"key": "E10", "paragraph_id": "P023", "quote": "卖兄弟、卖同志、卖组织、卖客户、卖恩人、卖朋友、卖父母、卖自己。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P025", "quote": "幸运到或者勇敢到能过什么都不出卖的生活的人，是极其极其的少数。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P027", "quote": "因为我自己也可能是潜意识里为了给自己脱罪而巧妙的将一些出卖朋友的行为解释为“正当的”而已。", "relation": "qualifies"},
    {"key": "E13", "paragraph_id": "P029", "quote": "绝大部分人只是把“出卖”的认证线抬高，从而把自己的行为不看做出卖罢了。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P031", "quote": "你问啥叫“小”？这个是根据通胀情况年年会涨的一个神秘系数。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P033", "quote": "而是要学会见微知著的识别出这样的人，悄无声息的末位淘汰。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P033", "quote": "完全一点都没有是做不到的，因为人是有限生物，根本做不到完美。", "relation": "qualifies"},
    {"key": "E17", "paragraph_id": "P034", "quote": "但你可以持续降低个人社会生态环境中的特征指数水平。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P035", "quote": "出卖国家民族这种行为，自然有系统的力量去对抗。真正要害的是，真正关键的是会卖你。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P036", "quote": "出卖是一种他们自己已经无法觉察的潜意识习惯了，已经被他们完全的自行justify了。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P038", "quote": "学会觉察这样的迹象，从自己的社会生态系系统排除这类危险分子，是你有效实现人生追求的至关重要的技能之一。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["政治伦理", "社会评论", "国家认同与忠诚", "公共政策"],
   "issue_candidates": ["普通人是否有能力卖国", "卖国的定义与事实定性", "小恶是否算恶/认证线自我豁免", "如何识别与规避会出卖他人者"],
   "text_function_candidates": ["驳论", "答疑", "训诫", "经验总结"],
   "object_candidates": ["中国", "flg", "连登仔", "王立强", "疫情期间"],
   "working_keywords": ["出卖", "卖国", "事实定性", "道德批判", "社会契约的总体信用", "认证线", "特征指数", "见微知著", "末位淘汰"]
  },
  "notes": "提问（Q001：为什么有人会想出卖自己的国家和民族?）归提问者；作者未直接回答动机，而是先反驳“老百姓没能力卖国”的流行说法并重述“卖国”定义，末段将重点转为识别“会卖你”的人。本篇无图片。文中的 flg、连登仔、王立强及其行为断言属作者举出的反例，需外部核查，本记录不作事实裁决。正文与 lexical 结构一致（39 段），无版本/取代信息。",
 },
 "5d1800e5": {
  "analysis": {
   "question_context": "提问者问：很多人买入后拿不住股票，怎样才能拿得住；并追问作者“从何时能做到的？从最初交易经历了多久？哪些关键事改变了你？”（Q001，属提问者）。作者没有回答个人交易史，而是先界定“拿不住”的实质是没有确切理由、只是怀疑自己看得不准，再论证以“避免损失”为目的就不可能拿得住，最后给出自己的立场——“投资”不是为盈利而是为花得值得，并声明若不接受这个定义，作者的投资经验就等于0、答案不必参考。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "界定“拿不住”：并非算好了该抛，而是没有确切理由、只是信不足。", "role": "definition"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005"], "summary": "论证情报永远不够、威胁概率算不出，没发现威胁不等于没威胁。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007", "P008", "P009"], "summary": "以夸张形象描写持仓处境，提出自问“怎么能做到怀疑而不害怕”。", "role": "context"},
    {"unit_id": "U004", "paragraph_refs": ["P010"], "summary": "主张：以规避损失为目的者不可能不害怕、不可能拿得住。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P011", "P012"], "summary": "否弃山顶卖出者的经验，称之为六合彩的经验。", "role": "rebuttal"},
    {"unit_id": "U006", "paragraph_refs": ["P013", "P014"], "summary": "指出唯一能拿得住的立场，并以作者投“某甲”的动机为例。", "role": "claim"},
    {"unit_id": "U007", "paragraph_refs": ["P015", "P016", "P017"], "summary": "以“帮助中国拥有芯片”为例，说明亏掉也心甘情愿。", "role": "example"},
    {"unit_id": "U008", "paragraph_refs": ["P018", "P019", "P020"], "summary": "说明何时才会去看“小猪扑满”；“投资”是拿来花钱的。", "role": "claim"},
    {"unit_id": "U009", "paragraph_refs": ["P021", "P022", "P023", "P024"], "summary": "行动建议：寻找“失而无憾的选择”，考察对方为何做事，增值只是添头。", "role": "action_advice"},
    {"unit_id": "U010", "paragraph_refs": ["P025", "P026", "P027", "P028"], "summary": "结论：值得即已保本，“值得”救赎损失的风险，故拿得住。", "role": "conclusion"},
    {"unit_id": "U011", "paragraph_refs": ["P029", "P030", "P031", "P032"], "summary": "信念与对举：想做事的人会有运气和勇气；已放开者不存在拿不拿得住，不能接受失去者永远拿不住。", "role": "conclusion"},
    {"unit_id": "U012", "paragraph_refs": ["P033", "P034", "P035", "P036", "P037"], "summary": "训诫式收束与适用边界声明；末段疑为平台话题句。", "role": "transition"}
   ],
   "main_claims": [
    {"claim_id": "C000", "claim_type": "open_question", "attribution": "questioner", "modality": "questioned", "statement": "提问者的问题：买入后拿不住股票怎样才能拿得住，作者从何时做到、最初交易经历多久、哪些关键事改变了作者。", "evidence": []},
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“拿不住”不是算好了该抛，而是没有任何确切理由、仅仅怀疑自己看得不准，也就是信不足。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "情报永远不够，威胁发生的概率算不出来；没发现威胁并不等于真的没有威胁。", "evidence": ["E3", "E4"]},
    {"claim_id": "C003", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "若投资的目的是避免损失，投资者就不可能不害怕，也不可能拿得住。", "evidence": ["E5"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "不应听成功在山顶卖出者的经验，那都是六合彩的经验。", "evidence": ["E6", "E7"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只有一种立场可以让人真的“拿得住”：投资不是为了盈利，是为了花得值得。", "evidence": ["E8"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者自述其“投资”某甲的动机不是求回报，而是因为对方做的事是对的、结果为其乐见、需要这笔帮助。", "evidence": ["E9"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“投资”不是拿来赚钱的，而是拿来花钱的；聪明应用于寻找“失而无憾的选择”，察觉对方为何做事，选“想做点事”的人而非“一切围绕为股东赚取最多利润”的人。", "evidence": ["E10", "E11"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只要值得，花掉了也已经保本；这种“值得”救赎了一切损失的风险，作者因此拿得住，不在乎市场风险与国际局势变幻。", "evidence": ["E12", "E13", "E14"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者相信世界的规则里已写定这样的好意：那些“想做事”而不是“想赚钱”的人，总会有足够的运气和勇气。", "evidence": ["E15"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者投资的是想好了不准备再拥有的东西，已经放开，故不存在“拿不拿得住”；而不能接受失去的人永远也拿不住。", "evidence": ["E16", "E17"]},
    {"claim_id": "C011", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "若不认可作者对“投资”的定义，则作者的投资经验为0，其答案不必参考。", "evidence": ["E18", "E19"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "劝诫式预测：几点想明白就几点睡，想不明白只能继续睁眼想，从此再无睡眠可言，只有晕倒。", "evidence": ["E20"]}
   ],
   "argument_steps": [
    "以对照句界定“拿不住”：若算好了该抛自然会抛，拿不住指没有确切理由、只是怀疑自己看得不准（P001-P002）。",
    "论证理由查过也无解：不能断言有威胁也不能断言没有；概率算不出，情报永远不够，并反问“什么叫情报够”（P003-P004）。",
    "反问：没发现威胁是否等于没威胁；若如此则市场企业都归自己（P005）。",
    "以夸张比喻描述可见与不可见威胁，落到自问“我怎么能做到怀疑而不害怕”（P006-P009）。",
    "给出条件判断：以规避损失为目的者不可能不害怕、不可能拿得住（P010）。",
    "否弃成功卖出者的经验（六合彩的经验）（P011-P012）。",
    "提出唯一能拿得住的立场：投资为了花得值得，而非盈利（P013）。",
    "以作者投“某甲”的动机作例证：因为事对、结果乐见、对方需要（P014）。",
    "举例“帮助中国拥有芯片”，说明亏掉也心甘情愿，因为一开始就当捐掉（P015-P017）。",
    "把“花钱”与“赚钱”对置，给出选人标准与“增值只是添头”的定位（P018-P024）。",
    "推论：值得即保本，“值得”救赎损失风险，所以拿得住，不在乎市场与局势（P025-P028）。",
    "以信念收束：世界规则里写定了这样的好意；已放开者不存在拿不拿得住的问题（P029-P032）。",
    "训诫式收尾并声明适用边界：不认可该定义则其经验为0（P033-P036）。"
   ],
   "concept_usage": [
    {"term": "拿不住", "meaning": "本文界定为没有任何确切理由、仅仅怀疑自己看得不准，等于“信不足”；与“算好了该抛”相对（P001-P002）。", "evidence": "P001", "ambiguity": "作者未讨论“算好了该抛却仍不抛”的情形。"},
    {"term": "情报够", "meaning": "作者以反问质疑该标准的存在，认为情报永远不够（P004）。", "evidence": "P004", "ambiguity": "作者只质疑而未给出“够”的替代判准。"},
    {"term": "投资", "meaning": "作者的私有定义：不是为盈利，是为花得值得；不是拿来赚钱的，而是拿来花钱的（P013、P020）。", "evidence": "P020", "ambiguity": "作者明说若不认可该定义则其投资经验为0（P035），故该词在本文与通常财务含义不同。"},
    {"term": "失而无憾的选择", "meaning": "即便失去也不遗憾的投资标的，作者要求把聪明放在寻找它上（P021）。", "evidence": "P021", "ambiguity": "如何判定“无憾”未给标准。"},
    {"term": "值得/救赎", "meaning": "作者用“值得”救赎一切“损失的风险”，作为能拿得住的心理机制（P025-P027）。", "evidence": "P026", "ambiguity": "“值得”由谁判定、可否被证伪，本文未说明。"},
    {"term": "保本", "meaning": "作者用法：只要值得，花掉了也已保本（P025），与通常的财务保本不同。", "evidence": "P025", "ambiguity": "该用法与常规财务含义冲突，属作者个人界定。"}
   ],
   "examples_and_targets": [
    "“某甲”——作者自述的投资对象（泛称），作为个人动机的例证（P014）。",
    "帮助中国拥有芯片：作者自述挑了若干家真想做这事、有理想、有决心、有希望的企业投钱——作者例证（P015）。",
    "“小猪扑满”——作者对可花资金的比喻（P018）。",
    "成功的山顶卖出的人及其经验——被否弃的对象，被称为六合彩的经验（P011-P012）。",
    "“黄金圣斗士”“天马流星拳”——动漫化调侃修辞，用于形容接连而来的威胁（P007-P008）。",
    "“如何树立正确的财富观？”——正文末段出现的话题性短句，疑为平台话题标签混入正文（P037）。"
   ],
   "conditions": [
    "界定“拿不住”以“如果你算好了该抛”为对照条件（P001）。",
    "若投资目的是避免损失，则不可能不害怕、不可能拿得住（P010）。",
    "只有“投资不是为了盈利，是为了花得值得”这一立场才能真拿得住（P013）。",
    "作者自述其做法以“钱一开始就是准备捐掉的”为前提（P016）。",
    "只有当出现比“让中国拥有芯片”更重要的事（如作者治病、所爱者开心）时才会去动小猪扑满（P018）。",
    "若不认可作者对“投资”的定义，其投资经验为0、答案不必参考（P035-P036）。",
    "作者关于“想做事的人总有运气和勇气”的说法依赖“世界的规则里已经写定了这样的好意”这一信念前提（P029）。"
   ],
   "rhetoric_and_tone": "第一人称经验自述夹劝诫。大量网络化口语与调侃（“看不到的威胁在我背后开足了小宇宙天马流星拳”“cnm黄金圣斗士啊你是”），以夸张身体意象写持仓焦虑（悬崖边、谷底、气泡膜式压迫）。用“吹嘘”“六合彩的经验”贬抑对立经验，以“我就是这么傻，所以我才这么幸福”自嘲反讽；结尾用“你几点想明白，你就可以几点睡”一类短句训诫，并以“我的答案你不需要参考了”划定适用边界。",
   "unresolved_questions": [
    "提问者追问的“你从何时能做到的？从最初交易经历了多久？哪些关键事改变了你？”作者未作回答，正文无对应内容。",
    "“某甲”与所投芯片企业均未具名，无法核对其具体情形（P014、P015）。",
    "“世界的规则里已经写定了这样的好意”属信念式断言，作者未给论证（P029）。",
    "正文末段“如何树立正确的财富观？”与上下文不相衔接，疑为平台话题标签混入正文，且 lexical 未覆盖该片段，需核对（P037）。",
    "作者自述的“投资”做法能否被他人复制，作者本人以 P035-P036 声明不适用于不接受该定义者，未给出判准。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "所谓的“拿不住”，一定是指你其实没有任何确切的理由，仅仅只是怀疑自己看得不准。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "没有理由，就是不相信了，信不足了。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "情报永远不够——话说，什么叫“情报够”？", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P005", "quote": "难道我没发现威胁就是真的没威胁了？", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P010", "quote": "如果你的投资的目的是为了避免损失，你是不可能不害怕的。你也是不可能拿得住的。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P011", "quote": "不要听那些成功的山顶卖出的人吹嘘什么经验。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P012", "quote": "那都是六合彩的经验。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P013", "quote": "只有一种立场可以让你真的“拿得住”——投资不是为了盈利，是为了花得值得。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P014", "quote": "而是因为某甲做的事情是对的，结果是我乐见的", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P020", "quote": "“投资”不是拿来赚钱的，而是拿来花钱的。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P021", "quote": "你的聪明，要放在寻找那个“失而无憾的选择”上。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P025", "quote": "只要值得，那么花掉了我也已经保本。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P026", "quote": "这种“值得”，救赎了一切“损失的风险”。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P028", "quote": "所以我根本不在乎什么市场风险国际局势变幻。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P029", "quote": "我相信世界的规则里已经写定了这样的好意", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P031", "quote": "我投资的东西，是我想好了不准备再拥有的东西。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P032", "quote": "你投资的东西，是你不能接受失去的东西", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P035", "quote": "如果你不认可这个“投资”的定义，那么我的“投资经验”就是0。", "relation": "qualifies"},
    {"key": "E19", "paragraph_id": "P036", "quote": "我的答案你不需要参考了。", "relation": "qualifies"},
    {"key": "E20", "paragraph_id": "P034", "quote": "你从此再无睡眠可言，只有晕倒。", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["投资与财富观", "个人经验自述", "风险与心理"],
   "issue_candidates": ["拿不住股票的成因", "以规避损失为目的的投资心态", "投资定义的私人化", "选人与选企业的标准"],
   "text_function_candidates": ["答疑", "经验总结", "劝诫", "自述"],
   "object_candidates": ["中国芯片企业", "某甲", "山顶卖出的成功投资者"],
   "working_keywords": ["拿不住", "情报", "失而无憾的选择", "花得值得", "小猪扑满", "保本", "六合彩的经验", "财富观"]
  },
  "notes": "本篇 lexical 存在未覆盖片段（divergence）：正文末段“如何树立正确的财富观？”未被 lexical 覆盖，已按 body 保留（P037），疑为平台话题标签混入正文，需人工核对。作者在 P013/P020/P035 对“投资”给出私人定义并声明不接受者不必参考其经验；其“保本”“盈利”用法与通常财务含义不同，本记录按原文保留，不作统一。提问者所问个人交易史（何时做到、经历多久、哪些关键事）作者未回答。本篇无图片。",
 },
 "291b5b7d": {
  "analysis": {
   "question_context": "提问者问“为什么越长大越觉得交不到那种可以交心的朋友？”（Q001，属提问者）。作者先定义小孩子的“无罪体认”，说明它如何支撑起儿童之间对友谊美好前景的信心；再推演进入社会后两个前提被击溃——无罪体认破损、可更换朋友的高选择余地消失——从而解释“丰富友谊”为何消失。文章以“（未完，待续）”结束，作者未给出如何重建交心关系的正面回答。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004", "P005"], "summary": "提出并定义“无罪体认”：没有“我犯过xx罪”的自我体认、自觉无道德亏欠。", "role": "definition"},
    {"unit_id": "U002", "paragraph_refs": ["P006", "P007", "P008", "P009", "P010"], "summary": "无罪体认带来对自身与他人道德水准的信心，构成儿童友谊的安全感基础。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P011", "P012"], "summary": "儿童友谊虽易因小事破裂，但青少年聚居、换友余地大，故影响有限。", "role": "qualification"},
    {"unit_id": "U004", "paragraph_refs": ["P013", "P014", "P015", "P016", "P017", "P018"], "summary": "进入社会：需独撑门户、失去庇佑与宽容，处境压抑而理由不被接受。", "role": "context"},
    {"unit_id": "U005", "paragraph_refs": ["P019", "P020", "P021"], "summary": "指出“正正当当的竞争”似为有靠山资本的头部企业特权，普通人没有。", "role": "claim"},
    {"unit_id": "U006", "paragraph_refs": ["P022", "P023", "P024", "P025"], "summary": "他人多以“上不得台盘的事”解决问题，不做就赚不到钱、处在最底层。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P026", "P027"], "summary": "两条道路都导致无罪体认破损或对他人无罪的信任动摇。", "role": "reason"},
    {"unit_id": "U008", "paragraph_refs": ["P028", "P029"], "summary": "失去无罪体认即无法排除被出卖/被辜负的怀疑，投入随之减少并被对方感知。", "role": "reason"},
    {"unit_id": "U009", "paragraph_refs": ["P030", "P031", "P032"], "summary": "第二前提崩塌：成年后日常接触者不过个位数，不喜欢就剧终、无从更换。", "role": "reason"},
    {"unit_id": "U010", "paragraph_refs": ["P033", "P034"], "summary": "结论：两个前提被击溃，建立在完美信心与“不行就换”上的丰富友谊如肥皂泡消失；文末标注未完待续。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C000", "claim_type": "open_question", "attribution": "questioner", "modality": "questioned", "statement": "提问者的问题：为什么越长大越觉得交不到可以交心的朋友。", "evidence": []},
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "小孩子有一个天然“优势”——“无罪体认”：因人生经历短、受父母师长庇佑与社会宽容，没有“我犯过xx罪”的自我体认，自我感受中没有道德亏欠。", "evidence": ["E1", "E2", "E3"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "由此小孩容易对自己能永远保持接近完美的道德水准怀有理所当然的信心，并对同龄人抱类似期待。", "evidence": ["E4"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对自身与对他人的无罪体认，构成儿童对彼此关系美好前景的自然信心，使其能充满安全感地互动——至少一开始如此。", "evidence": ["E5", "E6"]},
    {"claim_id": "C004", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "儿童友谊也容易因鸡毛蒜皮的小事破裂：小损失触发“对方可能很坏”的怀疑，而怀疑总有一定几率被本能的报复心盖章认证为事实。", "evidence": ["E7"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "青少年生活高度聚居，更换新朋友的选择余地很大，故友谊破裂的代价有限。", "evidence": ["E8"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "进入社会后要独撑门户：父母不再能支持反而依赖你，再没人（主要是老师）对你的安危成长负责，也没人再以“小孩不懂事”为宽容理由。", "evidence": ["E9", "E10"]},
    {"claim_id": "C007", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者称“正正当当的竞争”似乎是某些头部企业的特权——它们有靠山、资本、权势甚至能影响政策，所以不怕；普通人没有。", "evidence": ["E11", "E12"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "别人解决问题很大一部分靠上不得台盘的事；不做就没ta们赚钱，处在最底下。", "evidence": ["E13", "E14"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "结果两条路都通向信任崩塌：要么自己开始效仿而致无罪体认破损，要么艰苦熬着并因知道很多人熬不住而无法相信别人真的无罪。", "evidence": ["E15", "E16"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "失去无罪体认意味着无法排除在关系中被出卖或至少被辜负的怀疑；人不可能向自己怀疑的项目投入太多，投入不多对方也有感觉。", "evidence": ["E17", "E18"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "成年后常年同屋、天天见面说话的人不过个位数，不喜欢就剧终，没有更换余地。", "evidence": ["E19", "E20"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "高无罪体认与高选择余地两个前提都被击溃，建立在完美信心和“不行就换”规则上的“丰富友谊”自然如肥皂泡一样消失。", "evidence": ["E21"]}
   ],
   "argument_steps": [
    "提出小孩子的天然“优势”——“无罪体认”（P001）。",
    "设问并给出定义：因经历短、受庇佑与宽容，没有“我犯过xx罪”的自我体认，自觉无道德亏欠（P002-P005）。",
    "说明该体认同时适用于自身与身边朋友，带来对完美道德水准的信心与对同龄人的期待（P006-P007）。",
    "以儿童内心独白式引语呈现这种信心（P008）。",
    "推出：对己对人的无罪体认构成儿童对友谊美好前景的自然信心与安全感（P009-P010）。",
    "让步：儿童友谊也易因小事破裂，怀疑可能被报复心认证为事实（P011）。",
    "补足：但青少年聚居、换友余地大，故可承受（P012）。",
    "转折：进入社会后失去庇佑与宽容，处境压抑而理由不被接受（P013-P018）。",
    "指出竞争条件的差异：正当竞争似为头部企业特权，普通人无靠山资本权势（P019-P021）。",
    "指认他人多以“上不得台盘的事”解决问题，不做就赚不到钱（P022-P025）。",
    "推演后果：效仿则无罪体认破损，硬熬则无法相信他人无罪（P026-P027）。",
    "失去无罪体认即无法排除被出卖/被辜负的怀疑，投入减少并被对方感知（P028-P029）。",
    "提出第二前提的崩塌：成年后日常接触者不过个位数，无从更换（P030-P032）。",
    "结论：两个前提均被击溃，丰富友谊如肥皂泡消失；文末标注未完待续（P033-P034）。"
   ],
   "concept_usage": [
    {"term": "无罪体认", "meaning": "本文核心用法：因人生经历短、受庇佑和社会宽容，而没有“我犯过xx罪”的自我体认，自我感受中不存在道德亏欠（P003-P004）；既可指对自身的体认，也可指对他人的体认（P009）。", "evidence": "P003", "ambiguity": "作者将其称为小孩子的“优势”（带引号），但对成年人是否可能重建、破损是否可逆均未说明。"},
    {"term": "正正当当的竞争", "meaning": "作者称其“似乎是某些头部企业的特权”（P019），用于指资源与政策影响力不对称下的竞争条件。", "evidence": "P019", "ambiguity": "作者用了“似乎”，且未界定何为正当竞争、未给出证据。"},
    {"term": "高选择余地", "meaning": "指青少年高度聚居的集体生活带来的更换朋友的空间（P012）；成年后消失（P030-P032）。", "evidence": "P012", "ambiguity": "本文未量化“余地”或讨论线上社交是否改变该前提。"},
    {"term": "头部企业", "meaning": "文中指有靠山、有资本、有权势、甚至能影响政策因而“不怕”的企业（P020）。", "evidence": "P020", "ambiguity": "未具名、未界定规模标准。"},
    {"term": "丰富友谊", "meaning": "指建立在“完美信心”和“不行就换”规则上的儿童/青少年友谊（P033）。", "evidence": "P033", "ambiguity": "作者未正面界定“交心的朋友”，只用“丰富友谊”作对照。"}
   ],
   "examples_and_targets": [
    "小孩子与青少年群体——主要分析对象，用其“无罪体认”解释友谊基础（P001-P012）。",
    "“人活到非要靠偷、抢、瞒、骗、赖才能撑的地步，得有多差啊。我绝不会这样。”——作者以引号呈现的儿童内心话，属作者构造的示例性引语，非引用具体人物（P008）。",
    "头部企业（有靠山、资本、权势、能影响政策）——作者举出的对照与批评对象（P019-P020）。",
    "“上不得台盘的事”——作者对他人解决方式的概括性说法（P023）。",
    "“高阔蔚蓝的天”塌成“蓝色的气泡膜”——修辞性比喻，写成年处境的压迫（P016）。"
   ],
   "conditions": [
    "儿童的安全感互动被限定为“至少在一开始是这样”（P010）。",
    "怀疑被报复心认证为事实带概率限定：“总有一定几率”（P011）。",
    "对头部企业的判断带不确定限定：“似乎是某些头部企业的特权”（P019）。",
    "对他人手段的判断是概称而非全称：“很大一部分就是靠一些上不得台盘的事”（P023）。",
    "结论只在“无罪体认”与“高选择余地”两个前提同时成立时用于解释过去，两前提被击溃后结论随之改变（P033）。",
    "全文以“（未完，待续）”结束，论述未完成，结论为阶段性（P034）。"
   ],
   "rhetoric_and_tone": "解释—推演式语调，先下定义再逐步推演，结构上以“等ta们踏上社会之后呢？”（P013）作转折。大量使用第二人称“你”把读者带入成年处境，用“高阔蔚蓝的天，塌下来了……蓝色的气泡膜”一类身体化比喻写压抑；以“不喜欢，就剧终了”“哪有得换？”等短句作冷峭收束；P008 以引号呈现儿童内心独白。对现实的描述带批评意味（头部企业特权、上不得台盘的事），但不作对策建议。",
   "unresolved_questions": [
    "正文以“（未完，待续）”收尾，论述未完成；是否存在后续内容，本文未说明（P034）。",
    "提问者所问“交心的朋友”作者未给出界定，只讨论“丰富友谊”消失的机制。",
    "作者未回答成年人是否可能重建无罪体认或建立交心关系，正面答案缺失。",
    "“无罪体认”破损是否可逆、能否修复，本文未说明（P026）。",
    "关于“头部企业”享有正当竞争特权的说法未给证据，需外部核查（P019-P020）。",
    "P008 引语未标明说话者身份，仅可判断为作者所呈现的儿童视角示例。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "小孩子有一个天然的“优势”，就是“无罪体认”。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P003", "quote": "ta没有“我犯过xx罪”的自我体认。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "在ta的自我感受里，自己是没有过道德亏欠的。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P007", "quote": "于是ta们很容易的会对自己可以永远保持一个接近完美的道德水准有很理所当然的信心", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P009", "quote": "对自身的无罪体认和对他人的无罪体认，构成小孩子们对彼此关系会有美好前景的非常自然的信心。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P010", "quote": "所以，ta们能充满安全感的互动——至少在一开始是这样。", "relation": "qualifies"},
    {"key": "E7", "paragraph_id": "P011", "quote": "虽然ta们的友谊容易因为非常鸡毛蒜皮的小事而破裂", "relation": "qualifies"},
    {"key": "E8", "paragraph_id": "P012", "quote": "但好在青少年的生活是高度聚居的集体生活，更换新朋友的选择余地是很大的。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P014", "quote": "自己要独撑门户了；父母不但不再能支持你什么，反而还要依赖你", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P015", "quote": "所有的人都不会再以“小孩不懂事”为合理的宽容的理由了。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P019", "quote": "你开始发现“正正当当的竞争”，似乎是某些头部企业的特权。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P021", "quote": "你没有，你没有办法。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P023", "quote": "很大一部分就是靠一些上不得台盘的事。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P025", "quote": "你在最底下。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P026", "quote": "要么自己就已经开始效仿了，于是你自己的无罪体认破损了", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P026", "quote": "这样你还怎么相信别人真的是无罪的呢？", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P028", "quote": "就意味着无法排除即将在关系中被出卖——或至少被辜负——的怀疑。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P029", "quote": "人是不可能向自己怀疑的项目投入太多的。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P030", "quote": "常年和自己在一间屋里，天天见面、天天能说得上话的人，不过个位数而已。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P032", "quote": "哪有得换？", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P033", "quote": "自然就如肥皂泡一样没了。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["社会心理", "人际关系", "道德心理", "社会批评"],
   "issue_candidates": ["成年后交心朋友减少的原因", "无罪体认与信任的关系", "社会竞争条件与道德妥协", "可更换交往对象的余地"],
   "text_function_candidates": ["答疑", "解释", "推演", "未完稿"],
   "object_candidates": ["小孩子/青少年", "成年人", "头部企业", "父母师长"],
   "working_keywords": ["无罪体认", "道德亏欠", "安全感", "头部企业", "上不得台盘的事", "高选择余地", "丰富友谊"]
  },
  "notes": "正文以“（未完，待续）”结束（P034），属未完成文本，结论仅为阶段性；已读部分完整（34 段）。P008 带引号的句子是作者呈现的儿童内心话（示例性引语），未标注具体说话者，故未归属给任何被引用者。文中关于“头部企业享有正当竞争特权”“他人多靠上不得台盘的事”的判断为作者概括，无数据佐证，需外部核查。本篇无图片。",
 },
 "4cbed42c": {
  "status": "needs_reread",
  "image_checked": False,
  "full_text_checked": False,
  "analysis": {
   "question_context": "提问者问“有什么推荐高中生看的书？”（Q001，属提问者）。作者的回答是：建议先从科学经典、也就是自然史与自然史学读起，并称下面要推荐的系列就是自然史学的经典；他同时强调这是理解世界必须兼容的出发点之一，但不要把它视为真理。正文以“下面这个推荐的系列”指向推荐清单，而清单本身未出现在正文中，很可能是文末的图片（IMG001）；该图片本记录未核验。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "提出建议：高中生乃至所有人先从科学经典、自然史学读起；下面推荐的系列即其经典。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004"], "summary": "说明理由：这是对世界质量相当好的描述，是必须兼容的逻辑出发点；客观世界及其规律是各种意识形态的 common ground。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P005", "P006"], "summary": "提出条件与次序：若对人类有爱的指望就必须由此出发；先了解已明了的世界，再进行哲学与价值观探索。", "role": "action_advice"},
    {"unit_id": "U004", "paragraph_refs": ["P007", "P008", "P009"], "summary": "告诫与限定：不要把这些视为真理，因为人类能达到的极限不过是“有质量的错误”。", "role": "qualification"},
    {"unit_id": "U005", "paragraph_refs": ["P010"], "summary": "正文末尾的图片来源说明“图侵删”，提示推荐清单以图片形式给出。", "role": "other"}
   ],
   "main_claims": [
    {"claim_id": "C000", "claim_type": "open_question", "attribution": "questioner", "modality": "questioned", "statement": "提问者的问题：有什么推荐高中生看的书。", "evidence": []},
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "建议高中生——更泛化地说所有人——先从科学经典读起，也就是从自然史、自然史学读起。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者称下面推荐的系列就是自然史学的经典（清单本身未见于正文，可能位于图片 IMG001）。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "无论将来采取什么意识形态立场、持什么价值观，都要把这一系列当作对世界质量相当好的描述、必须兼容的逻辑出发点和立足点之一。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不得不服从的客观世界及其规律，是所有意识形态能够相互理解、交流、定约的 common ground。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "若对人类有爱的指望，就非从这里出发、非在此立足不可。", "evidence": ["E5"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "应先知道这个世界里已经比较明了的一部分是如何的，再决定什么是与这世界兼容的，即进行哲学和价值观的探索。", "evidence": ["E6"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "不要将这些（科学经典）视为真理。", "evidence": ["E7"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "因为人类能达到的极限不过是“有质量的错误”，这些只是质量比较好的错误。", "evidence": ["E8", "E9"]}
   ],
   "argument_steps": [
    "给出建议：先从科学经典、自然史学读起，对象是高中生乃至所有人（P001）。",
    "指明“下面这个推荐的系列”即自然史学的经典（P002）。",
    "说明理由：这是对世界质量相当好的描述，是将来无论持何意识形态都必须兼容的逻辑出发点之一（P003）。",
    "给出更普遍的理由：客观世界及其规律是所有意识形态相互理解、交流、定约的 common ground（P004）。",
    "加条件：若对人类有爱的指望，非从这里出发、非在此立足不可（P005）。",
    "给出次序建议：先了解世界已明了的部分，再进行哲学与价值观探索（P006）。",
    "转折告诫：不要把这些东西视为真理（P007）。",
    "给出理由：人类能达到的极限不过是“有质量的错误”，它们只是质量比较好的错误（P008-P009）。",
    "以“图侵删”交代图片来源，提示推荐清单为图片形式（P010）。"
   ],
   "concept_usage": [
    {"term": "科学经典/自然史、自然史学", "meaning": "作者推荐给高中生及所有人的阅读起点，称所推荐的系列即自然史学的经典（P001-P002）。", "evidence": "P001", "ambiguity": "作者未界定“科学经典”或“自然史学”的范围与选书标准；具体书目很可能在未核验的图片中。"},
    {"term": "客观世界及其规律", "meaning": "被作者称为所有意识形态能够相互理解、交流、定约的 common ground（P004）。", "evidence": "P004", "ambiguity": "如何认定某条规律属于“不得不服从”，本文未给判准。"},
    {"term": "有质量的错误", "meaning": "作者对人类认识极限的表述：人类所能达到的只是质量比较好的错误（P008-P009）。", "evidence": "P008", "ambiguity": "“质量”如何衡量、与真理的差别何在，本文未展开。"},
    {"term": "逻辑出发点和立足点", "meaning": "指把自然史学作为将来任何立场都必须兼容的出发点之一（P003）。", "evidence": "P003", "ambiguity": "作者说“之一”，但未说明其他出发点是什么。"}
   ],
   "examples_and_targets": [
    "自然史学的经典系列——作者推荐的例证；正文未列出书目，很可能是图片 IMG001 的内容，未核验（P002）。",
    "“图侵删”——作者对图片版权的说明，提示推荐清单以图片形式呈现（P010）。",
    "意识形态与价值观——泛指读者将来的立场，作者以此说明兼容性要求（P003）。"
   ],
   "conditions": [
    "建议对象为高中生，并泛化为“所有人”（P001）。",
    "让步条件：“将来你无论采取什么意识形态立场、有什么样的价值观”（P003）。",
    "条件句：“你若对人类有爱的指望”（P005）。",
    "作者自设告诫条件：即使推崇也不要将这些东西视为真理（P007）。",
    "推荐清单的实际内容依赖图片 IMG001，本记录未核验，故本文在此处的完整内容待补。"
   ],
   "rhetoric_and_tone": "短篇建议体，语气直接、带教导与告诫色彩（“我建议”“你都要记住”“你若……非……不可”“但是注意”）。中英混用（common ground）。对科学经典评价很高（“质量相当好的描述”），但紧接着以“不要将这些东西视为真理”自我限定，并用“有质量的错误”作降温，呈推崇与警惕并存的语气。全文无修辞性攻击，未涉及论敌。",
   "unresolved_questions": [
    "图片 IMG001 未核验（本记录无读图能力），作者推荐的具体书目清单很可能在该图中，需图像核验后再补（P002、P010）。",
    "正文“下面这个推荐的系列”所指的内容未在文本中出现，无法确认清单内容（P002）。",
    "“自然史学的经典”包含哪些书、以何标准选定，本文未说明。",
    "P003 说自然史学是“必须兼容的逻辑出发点和立足点之一”，其他出发点为何，本文未说明。",
    "“图侵删”表明该图片非作者原创，图片来源与版权状态不明（P010）。",
    "本篇按图片文章处理：status=needs_reread、image_checked=false、full_text_checked=false，正文 10 段已读但全文理解未完成。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "我建议高中生——或者更泛化的说，所有人——先从科学经典读起，也就是从自然史、自然史学读起。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "下面这个推荐的系列，就是自然史学的经典。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "这是你要总结和理解的世界的一个质量相当好的描述，是你必须兼容的逻辑出发点和立足点之一。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "不得不服从的客观世界及其规律，是所有意识形态能够相互理解、交流、定约的common ground。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "你若对人类有爱的指望，你非从这里出发、也非在此立足不可。", "relation": "qualifies"},
    {"key": "E6", "paragraph_id": "P006", "quote": "再决定什么是与这世界兼容的——也就是进行哲学和价值观的探索。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "但是注意——不要将这些东西视为真理。", "relation": "qualifies"},
    {"key": "E8", "paragraph_id": "P008", "quote": "因为人类能达到的极限，不过是“有质量的错误”。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P009", "quote": "这些只是质量比较好的错误。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["阅读推荐", "科学教育", "知识论与价值观"],
   "issue_candidates": ["高中生应读什么书", "科学经典/自然史学的优先性", "客观世界与意识形态的关系", "不把科学结论当真理"],
   "text_function_candidates": ["推荐", "建议", "告诫"],
   "object_candidates": ["高中生", "自然史学经典", "意识形态"],
   "working_keywords": ["科学经典", "自然史", "自然史学", "common ground", "有质量的错误", "图侵删"]
  },
  "notes": "本篇含 1 个图片节点（IMG001，src=//asset.sooon.ai/p/2020-06/27/8f097221ecdbcd8f9ea0dcc7b9396183.jpg），本记录无读图能力，图片内容未经核验，故 status=needs_reread、image_checked=false、full_text_checked=false；正文 10 段已完整读取，但作者推荐的“系列”书目很可能在图片中，未核验前不得声称全文理解完成，需人工/多模态复核。P010“图侵删”提示图片非作者原创。本篇无版本/取代信息。",
 },
 "7a64391d": {
  "analysis": {
   "question_context": "提问者问“什么是大格局？大格局的人有哪些表现和思维模式？”（Q001，属提问者）。作者没有逐条列举表现，而是给出一个判别方式：大格局不看资金规模、建筑面积或人员总量，而看“考量的历史感”；并给出衡量方法——是否具有历史使命感以及与之匹配的历史修养，最后强调这与身份职位无关。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "提出判别方式：不是资金规模、建筑面积、人员总量，而是考量的历史感。", "role": "definition"},
    {"unit_id": "U002", "paragraph_refs": ["P004"], "summary": "解释该判别方式的含义：不为一地一事一时而谋，立足过去经验、面向未来可能。", "role": "definition"},
    {"unit_id": "U003", "paragraph_refs": ["P005"], "summary": "列出这类人的三项特征：历史认识、对现状清醒不乡愿、对未来的愿景与安排。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P006", "P007"], "summary": "说明其方案当下常被视为迂腐累赘、有无谓风险，日后才显出先见之明。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P008", "P009"], "summary": "排除空间与数量：帝王将相可器量狭小，穷富人可一掷万金；从无能谋后世的小人。", "role": "rebuttal"},
    {"unit_id": "U006", "paragraph_refs": ["P010", "P011"], "summary": "给出衡量方法（历史使命感与匹配的历史修养），并强调与身份职位无关。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C000", "claim_type": "open_question", "attribution": "questioner", "modality": "questioned", "statement": "提问者的问题：什么是大格局，大格局的人有哪些表现和思维模式。", "evidence": []},
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "大格局的判别方式不是资金规模、建筑面积或人员总量，而是“考量的历史感”。", "evidence": ["E1", "E2", "E3"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "历史感指：不仅仅为一时、一地、一事而谋，而且时时处处既充分面对现实挑战，也站在一切过去的经验之上、面向一切未来的可能。", "evidence": ["E4"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这类人必定对历史有相当深入的心得和认识，对现状有清醒而毫不乡愿的认识，对未来有超出常人的愿景和安排。", "evidence": ["E5"]},
    {"claim_id": "C004", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "这些人常常选择旁人觉得“莫名其妙”的奇怪方案，这些方案在实施当下常被看作迂腐、累赘、没有必要，甚至有无谓风险和多余成本。", "evidence": ["E6", "E7"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "但将来等那些事情到来，人们才会看到这些铺垫是多么的有先见之明。", "evidence": ["E8"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "格局与空间和数量没有关系：历史上有器量狭小、人格猥琐的帝王将相，也有一掷万金的穷富人。", "evidence": ["E9"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "从来没有能谋后世的小人。", "evidence": ["E10"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "格局的衡量方法是看一个人有没有历史使命感，有没有和这个历史使命感匹配的历史修养。", "evidence": ["E11"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "该衡量与身份职位无关：哪怕只是图书管理员、炮兵少尉，甚至只是在市场到处找人聊天的。", "evidence": ["E12"]}
   ],
   "argument_steps": [
    "先声明大格局有很简单的判别方式（P001）。",
    "用三个“不是”排除常见误解：资金规模、建筑面积、人员总量（P002）。",
    "给出正面判别项：考量的历史感（P003）。",
    "展开历史感的含义：不为一地一事一时而谋，立足过去经验、面向未来可能（P004）。",
    "列出这类人的三项特征：历史认识、对现状清醒不乡愿、对未来的愿景与安排（P005）。",
    "说明其方案的当下处境：被当作迂腐、累赘、没必要、有无谓风险与多余成本（P006）。",
    "给出时间性判准：等事情到来，才能看到铺垫的先见之明（P007）。",
    "以历史反例排除空间与数量：器量狭小的帝王将相、一掷万金的穷富人（P008）。",
    "以“从来没有能谋后世的小人”作反衬式断言（P009）。",
    "收束为衡量方法：历史使命感 + 与之匹配的历史修养（P010）。",
    "以身份递降的方式收尾，强调与职位无关（P011）。"
   ],
   "concept_usage": [
    {"term": "大格局/格局", "meaning": "本文界定为“考量的历史感”，与空间、数量无关；衡量方法是看有无历史使命感及匹配的历史修养（P003、P008、P010）。", "evidence": "P003", "ambiguity": "作者未给出可操作判准，也未直接列举提问者所问的“表现和思维模式”。"},
    {"term": "考量的历史感", "meaning": "不仅为一时一地一事而谋，既面对现实挑战，又站在一切过去经验之上、面向一切未来可能（P004）。", "evidence": "P004", "ambiguity": "“历史感”如何观察与衡量，本文未说明。"},
    {"term": "历史使命感", "meaning": "作者用作衡量格局的标准之一（P010）。", "evidence": "P010", "ambiguity": "未定义，亦未说明如何判定某人是否具有。"},
    {"term": "历史修养", "meaning": "作者要求与历史使命感相匹配的修养（P010）。", "evidence": "P010", "ambiguity": "未说明其内容与检验方式。"},
    {"term": "乡愿", "meaning": "用于修饰对现状的认识：“清醒而毫不乡愿的认识”（P005），指不迎合世俗、不取媚于人。", "evidence": "P005", "ambiguity": "作者未展开该词在本文的具体所指。"},
    {"term": "穷富人", "meaning": "P008 中与“帝王将相”并举的例子，指可以一掷万金却未必有格局的富人。", "evidence": "P008", "ambiguity": "“穷富人”的字面组合有歧义（“穷”修饰何者不明），需回原文核对作者用法。"}
   ],
   "examples_and_targets": [
    "“资金规模”“建筑面积”“人员总量”——被作者排除的三种判别标准（P002）。",
    "器量狭小、人格猥琐的帝王将相——泛称历史例证，用来说明格局与地位数量无关（P008）。",
    "一掷万金的穷富人——泛称例证（P008）。",
    "能谋后世的小人——作者断言其不存在，作反衬（P009）。",
    "图书管理员、炮兵少尉、在市场到处找人聊天的——泛称身份形象，用来说明格局与职位无关（P011）；作者未指名，是否影射特定历史人物本文未说明。"
   ],
   "conditions": [
    "判别标准被限定为“考量的历史感”，排除资金规模、建筑面积、人员总量（P002-P003）。",
    "历史感的时间条件：“不仅仅为一时、一地、一事而谋”，要站在一切过去经验之上、面向一切未来可能（P004）。",
    "这类人的方案在当下多被负面评价（迂腐、累赘、没必要、有无谓风险与多余成本），其价值须待“将来等那些事情到来”才显现（P006-P007）。",
    "使用“必定”“从来没有”等全称式断言，未附加例外条件（P005、P009）。",
    "身份不设门槛：“哪怕ta只是个……甚至只是……”（P011）。"
   ],
   "rhetoric_and_tone": "定义—判别式短论，断言语气强（“有一个很简单的判别方式”“必定”“从来没有”）。以三个“不是”排比排除流俗标准，以“哪怕ta只是个图书管理员，或者炮兵少尉，甚至只是个在市场到处找人聊天的”递降排比收束，强调格局与身份无关。对“小人”用贬义措辞（“从来没有能谋后世的小人”），带褒贬与训诫色彩。全篇无引号引文、无对话。",
   "unresolved_questions": [
    "“历史感”“历史使命感”“历史修养”均未给出定义或可操作判准（P003、P010）。",
    "P011 的“图书管理员”“炮兵少尉”“在市场到处找人聊天的”是否为特定历史人物影射，本文未说明，本记录不作推断。",
    "“穷富人”一词的具体含义有歧义（P008）。",
    "“从来没有能谋后世的小人”是作者的全称断言，未给论证（P009）。",
    "作者未正面回答提问的第二部分（大格局的人有哪些表现和思维模式），只给出判别方式与若干特征。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "大格局有一个很简单的判别方式。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "既不是“资金规模”，也不是“建筑面积”，也不是“人员总量”。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "而是考量的历史感。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "不仅仅为一时、一地、一事而谋，而且时时处处既充分的面对现实的挑战，也站在一切过去的经验之上，面向一切未来的可能。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "必定对历史有相当深入的心得和认识，对现状有清醒而毫不乡愿的认识", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "这些人常常选择旁人觉得“莫名其妙”的奇怪方案。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P006", "quote": "甚至“有无谓风险和多余成本”。", "relation": "qualifies"},
    {"key": "E8", "paragraph_id": "P007", "quote": "但是将来等那些事情到来，人们才会看到这些铺垫是多么的有先见之明。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P008", "quote": "格局，和空间和数量没有关系", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P009", "quote": "但却从来没有能谋后世的小人。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P010", "quote": "看一个人有没有历史使命感，有没有和这个历史使命感匹配的历史修养。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P011", "quote": "哪怕ta只是个图书管理员，或者炮兵少尉，甚至只是个在市场到处找人聊天的。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["人物评价", "历史观", "领导力与管理"],
   "issue_candidates": ["什么是大格局", "格局与规模/数量的区别", "历史感与历史使命感", "格局与身份职位的关系"],
   "text_function_candidates": ["答疑", "定义", "评论"],
   "object_candidates": ["帝王将相", "图书管理员", "炮兵少尉", "在市场找人聊天的人", "小人"],
   "working_keywords": ["大格局", "考量的历史感", "历史使命感", "历史修养", "乡愿", "谋后世", "先见之明"]
  },
  "notes": "本篇无图片，正文 11 段已完整读取。P011 的三种身份（图书管理员、炮兵少尉、在市场到处找人聊天的）为作者列举的泛称形象，作者未指名，本记录不推断其影射对象。作者未正面列举提问者所问的“表现和思维模式”，仅给出判别方式与若干特征。无版本/取代信息。",
 },
 "ace386a1": {
  "analysis": {
   "question_context": "提问者问“‘声言具备恰证明其不具备’类的概念有什么共性？”（Q001，属提问者）。作者先把题设翻译为“声言自己不诚实/不客观的人，反而更令旁人觉得诚实/客观”，列出具有该效应的概念清单，给出答案——共性即皆属美德，并用“人的绝对有限性”与“逻辑上的客观事实”论证为何无人能宣称拥有无可置疑的美德。随后作者回应评论区提问（带限定词的夸奖可否接受），再针对题主修正题设后加入的“恶德”概念作反驳，指出非美德并未享受同样的“自悖效应认证”，并以勇敢与怯懦为例说明德性之间只是对比关系而非反义关系。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004", "P005"], "summary": "把题设翻译为“声言不具备反而更像具备”，并列出有此“自悖效应”的概念清单。", "role": "context"},
    {"unit_id": "U002", "paragraph_refs": ["P006", "P007"], "summary": "给出答案：共性是皆属美德；凡无可置疑的美德皆有自悖效应。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P008", "P009", "P010", "P011"], "summary": "论证理由：人的有限性使“宣称拥有无可置疑的美德”不成立，且无逻辑路线可证行为与美德的对应。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P012", "P013", "P014"], "summary": "以诗句与“第一神偷悖论”类比，论证道德判定手段的两难（外人不知心、自查不可靠）。", "role": "example"},
    {"unit_id": "U005", "paragraph_refs": ["P015", "P016"], "summary": "“自知”也属有自悖效应的美德；该困境客观且不可反驳。", "role": "claim"},
    {"unit_id": "U006", "paragraph_refs": ["P017", "P018", "P019"], "summary": "唯一例外指向“无限者”：绝对自知者、无限他知者、无限能动者。", "role": "qualification"},
    {"unit_id": "U007", "paragraph_refs": ["P020", "P021", "P022", "P023"], "summary": "论证逻辑事实刚度高于自然规律；不承认逻辑事实即失去有效理性与自我声称的基础。", "role": "reason"},
    {"unit_id": "U008", "paragraph_refs": ["P024", "P025", "P026", "P027"], "summary": "通俗推论：宣称肯定足够公平者反而缺少接近公平的能力；自我宣称证明其缺少基本逻辑判断力。", "role": "conclusion"},
    {"unit_id": "U009", "paragraph_refs": ["P028", "P029", "P030", "P031"], "summary": "给出“谦卑”的含义，并强调它不是怕遭嫉恨的假装；提出“自我宣称即实际抛弃追求”。", "role": "action_advice"},
    {"unit_id": "U010", "paragraph_refs": ["P032", "P033", "P034", "P035", "P036", "P037", "P038"], "summary": "回答评论区提问：带限定词的夸奖可接受，不加限定词的美德表述人当不起。", "role": "action_advice"},
    {"unit_id": "U011", "paragraph_refs": ["P039", "P040", "P041", "P042", "P043"], "summary": "转述题主修正后的题设，并按该公式套出“承认虚伪即不虚伪”等表述。", "role": "context"},
    {"unit_id": "U012", "paragraph_refs": ["P044", "P045", "P046", "P047", "P048", "P049", "P050", "P051", "P052"], "summary": "反驳：承认恶德并不绝对证明不恶德；自称公正可绝对证明不公正，反之不然；非美德未获同样认证。", "role": "rebuttal"},
    {"unit_id": "U013", "paragraph_refs": ["P053", "P054", "P055", "P056", "P057", "P058", "P059"], "summary": "主张德性间多是对比关系而非反义关系，并以勇敢与怯懦为例展开。", "role": "claim"},
    {"unit_id": "U014", "paragraph_refs": ["P060", "P061", "P062", "P063", "P064", "P065", "P066"], "summary": "勇敢实为对“不勇敢”的怯懦；非出于此的冒险应称鲁莽甚至愚蠢。", "role": "reason"},
    {"unit_id": "U015", "paragraph_refs": ["P067", "P068", "P069"], "summary": "结论：勇敢即怯懦；伦理问题高度复杂由此可见一斑。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C000", "claim_type": "open_question", "attribution": "questioner", "modality": "questioned", "statement": "提问者的问题：“声言具备恰证明其不具备”类的概念有什么共性。", "evidence": []},
    {"claim_id": "C001", "claim_type": "author_reported", "attribution": "questioner", "modality": "asserted", "statement": "作者把题设翻译为：一个声言自己不诚实/不客观的人，反而往往比坚定地认为自己够诚实/够客观的人更令旁人觉得诚实/客观。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "诚实、客观、公正、真实、精确、勇敢、豁达、聪明、理智、谦虚、自信、审慎、深刻、开放、好、有品味、有道德等概念都有这个“自悖效应”。", "evidence": ["E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这类概念的共性就是皆属美德；凡属无可置疑的美德的，皆有“自悖效应”。", "evidence": ["E4", "E5"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "其原因在于“人作为有限的存在永无充分立场宣称自己拥有无可置疑的美德”是一个逻辑上的客观事实。", "evidence": ["E6", "E7"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "根本不存在一条逻辑路线，能证明一个人的任何行为组合与某项美德之间有无可置疑的对应关系。", "evidence": ["E8"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人类设计不出既足够有效而自己又不能绕过的道德判定手段：外人不能觉察人心，当事人自查也无法排除自欺欺人或有意欺骗。", "evidence": ["E9", "E10"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“自知”本身也是有“自悖效应”的“无可置疑的美德”之一：人若宣称自知，则一定没有“知道自己不自知的”自知。", "evidence": ["E11"]},
    {"claim_id": "C008", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "这种困境是客观的、与人的绝对有限性绑死、没得反驳——除非人不成其为人，而成为一个无限者。", "evidence": ["E12", "E13"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只有一个绝对自知者才有能力做自我保证人，一个无限他知者才能有效背书该保证；也只有无限能动者才能真正名副其实地承受无限苛刻的美德鉴定标准。", "evidence": ["E14", "E15"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "逻辑上的客观事实的刚度甚至高于自然规律：由基本逻辑保证的结论“无法崩溃”，因为那意味着逻辑律动摇、将整个地消灭理性本身的有效性。", "evidence": ["E16"]},
    {"claim_id": "C011", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "逻辑上的客观事实是人类（一切依靠逻辑律支撑的理性存在）绝无可能撼动的绝对有效事实；作者自注“绝对有效不等于绝对客观”。", "evidence": ["E17"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "若不承认逻辑上的事实，就不具有有效的理性，一切自我声称因此尽皆失去可靠性的基础。", "evidence": ["E18"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“宣称自己无可置疑地拥有某项美德”（包括“够用的美德”）这一行为，已经证明此人绝对地缺少真的接近这项美德的能力——基本的逻辑判断力。", "evidence": ["E19"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "谦卑就是认识到自身的绝对有限性，不再宣称拥有某项无可置疑的美德或宣称拥有而拒绝质疑；这不是怕遭嫉恨而假装的推辞，而是因为这些话逻辑上就不成立。", "evidence": ["E20", "E21", "E22"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "若确实想尽可能拥有美德，就要记住——自我宣称即实际抛弃追求。", "evidence": ["E23"]},
    {"claim_id": "C016", "claim_type": "author_reported", "attribution": "questioner", "modality": "questioned", "statement": "作者引述的评论区提问：别人夸我这些，我应该接受，还是推辞“我不是我没有”？", "evidence": ["E24"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对夸奖的判准在限定词：夸“学习成绩好”“比较聪明”没问题，说“聪明”则拒绝；不加限定词的美德表述不是人所能当得起的。", "evidence": ["E25", "E26", "E27"]},
    {"claim_id": "C018", "claim_type": "author_reported", "attribution": "questioner", "modality": "asserted", "statement": "题主修正题设，加入虚伪、主观、偏见、怯懦等与美德对立的概念，按题设公式可套出“一个人承认自己虚伪，这使得ta不虚伪”“承认自己怯懦，这使得ta不怯懦”。", "evidence": ["E28", "E29", "E30"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "题设的扩展看似对美德分析构成挑战，其实并非如此：承认自己虚伪并没有使得此人（绝对地被证明）不虚伪，承认怯懦亦然。", "evidence": ["E31", "E32"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "存在不对称性：自称公正这一行为可以绝对地证明此人不公正；但自称不公正并不能绝对证明此人公正，只是让听者对其公正有更正面的期待，而这种期待几乎没有重量。", "evidence": ["E33", "E34", "E35"]},
    {"claim_id": "C021", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "当“美德的对立面”被放入该命题时命题并不同样成立；非美德并没有真的享受到美德所享受的“自悖效应认证”。", "evidence": ["E36", "E37"]},
    {"claim_id": "C022", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "很多常被认为互相对称对立的德性，其实只是对比关系，并不是反义关系；勇敢和怯懦即非反义关系。", "evidence": ["E38", "E39"]},
    {"claim_id": "C023", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "真正的勇敢是对“不勇敢”的怯懦：因为真切看见、摸到甚至尝到选择不勇敢的惨痛与折磨，才形成“宁可面对风险和代价也不退半步”的勇气；所以“不是我勇敢，而恰恰是我怯懦”。", "evidence": ["E40", "E41", "E42"]},
    {"claim_id": "C024", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "并非出于对不勇敢后果的怯懦而挑战风险的行为，不称其为勇敢，而称其为鲁莽，甚至是愚蠢。", "evidence": ["E43", "E44"]},
    {"claim_id": "C025", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "结论：勇敢即怯懦；伦理问题是高度复杂的，由此可见一斑。", "evidence": ["E45", "E46"]},
    {"claim_id": "C026", "claim_type": "quoted_or_cited", "attribution": "unknown", "modality": "asserted", "statement": "文中引语“如果我们什么都不做，华为六个月内就会倒闭。”——用以说明变革者预见的是不作为的可怕后果；说话者本文未标明。", "evidence": ["E47"]}
   ],
   "argument_steps": [
    "把题设翻译为对照句：声言自己不诚实/不客观者反而更令旁人觉得诚实/客观（P001-P003）。",
    "列出具有“自悖效应”的概念清单，并把问题重述为“这类概念有何共性”（P004-P005）。",
    "给出答案：共性即皆属美德；凡无可置疑的美德皆有此效应（P006-P007）。",
    "给出理由：人作为有限存在永无充分立场宣称拥有无可置疑的美德，这是逻辑上的客观事实（P008-P010）。",
    "论证：不存在证明任何行为组合与某项美德有无可置疑对应关系的逻辑路线（P011）。",
    "引“周公恐惧流言日，王莽谦恭未篡时”与“第一神偷悖论”作类比，说明道德判定手段的两难（P012-P014）。",
    "补足：“自知”也属有自悖效应的美德；困境客观且没得反驳（P015-P016）。",
    "指出唯一例外条件：除非人成为无限者；并推及绝对自知者、无限他知者、无限能动者（P017-P019）。",
    "论证逻辑事实的刚度高于自然规律，否认它即失去有效理性与自我声称的基础（P020-P023）。",
    "用通俗版重述：宣称肯定足够公平者恰缺少接近公平的能力；自我宣称证明缺少基本逻辑判断力（P024-P027）。",
    "给出“谦卑”的定义与“自我宣称即实际抛弃追求”的要求，并排除“怕遭嫉恨而假装”的误读（P028-P031）。",
    "回答评论区提问，给出限定词判准：带限定的夸奖可接受，无限制的美德表述当不起（P032-P038）。",
    "转述题主修正题设后加入的恶德清单及公式套用结果（P039-P043）。",
    "反驳该扩展：承认恶德并不绝对证明不恶德；自称公正可绝对证明不公正，反向不成立；非美德未获同样认证（P044-P052）。",
    "提出德性间只是对比关系而非反义关系，并以勇敢与怯懦为例（P053-P059）。",
    "推出勇敢实为对“不勇敢”的怯懦；非出于此的冒险是鲁莽甚至愚蠢（P060-P066）。",
    "结论：勇敢即怯懦；伦理问题高度复杂由此可见一斑（P067-P069）。"
   ],
   "concept_usage": [
    {"term": "自悖效应", "meaning": "本文核心术语：声言具备某概念反而证明或令人觉得不具备的效应；作者称凡属无可置疑的美德者皆有此效应（P004-P007）。", "evidence": "P004", "ambiguity": "作者未说明该术语是否为自造或有无既有来源，也未给出统一的形式化表述。"},
    {"term": "美德/无可置疑的美德", "meaning": "作者以“无可置疑”作限定，指不容置疑地拥有某项德性；P027 把“够用的美德”也纳入被否定的宣称对象（P007、P027）。", "evidence": "P007", "ambiguity": "P004 的概念清单是作者列举，未讨论其间是否同质或是否穷尽。"},
    {"term": "逻辑上的客观事实", "meaning": "作者用指由基本逻辑保证、刚度高于自然规律、无法崩溃的结论（P008、P020）；并注明“绝对有效不等于绝对客观”（P021）。", "evidence": "P020", "ambiguity": "“绝对有效”与“绝对客观”的区分作者只作提示，未展开论证。"},
    {"term": "绝对有限性", "meaning": "人作为有限存在的属性，是“永无立场宣称拥有无可置疑美德”的根源（P016、P028）。", "evidence": "P016", "ambiguity": "作者未界定“有限”的具体含义与边界。"},
    {"term": "无限者/绝对自知者/无限他知者/无限能动者", "meaning": "P017-P019 提出作为唯一例外：只有无限者能做自我保证、背书保证并承受无限苛刻的美德鉴定标准。", "evidence": "P018", "ambiguity": "作者未点名任何具体宗教或哲学对象，本记录不作推断。"},
    {"term": "谦卑", "meaning": "作者定义为认识到自身的绝对有限性，不再宣称拥有无可置疑的美德或宣称拥有而拒绝质疑；并明确它不是怕遭嫉恨的假装（P028-P030）。", "evidence": "P028", "ambiguity": "与日常“谦虚”用法的差别作者未逐条比较。"},
    {"term": "自悖效应认证", "meaning": "指美德所享有的那种认证；作者称非美德没有真的享受到它（P052）。", "evidence": "P052", "ambiguity": "“认证”的机制与判定者本文未说明。"},
    {"term": "对比关系/反义关系", "meaning": "作者区分德性之间的两种关系：很多被视为对称对立的德性其实只是对比关系（P053-P054）。", "evidence": "P053", "ambiguity": "作者只给出勇敢/怯懦一例，未说明该区分的适用范围。"},
    {"term": "勇敢/怯懦", "meaning": "作者用法：真正的勇敢是对“不勇敢”的怯懦，故“勇敢即怯懦”（P057-P061、P068）。", "evidence": "P057", "ambiguity": "该用法与日常语义差异极大，作者以企业家为例支撑，未给其他例证。"}
   ],
   "examples_and_targets": [
    "“周公恐惧流言日，王莽谦恭未篡时”——作者引诗，用来说明行为与美德无必然对应；出处本文未标注（P012）。",
    "“第一神偷悖论”：第一神偷设计不出自己能打开而又足够安全的锁——类比（P013）。",
    "道德判定手段的两难（外人不能觉察人心、当事人自查不可靠）——论证材料（P014）。",
    "评论区提问（别人夸我这些应接受还是推辞）——作者引述的第三方提问，属提问者一侧（P032）。",
    "“学习成绩好”“比较聪明”“聪明”——作者用于说明限定词判准的三个例子（P034-P036）。",
    "题主修正题设后加入的虚伪、主观、偏见、怯懦等恶德清单——作者转述的提问者修正（P039）。",
    "在反对声中投入极大赌注做深刻变革的企业家——作者例证（P062-P063）。",
    "“如果我们什么都不做，华为六个月内就会倒闭。”——引语，说话者未标明；华为为文中唯一具名机构（P064）。",
    "“枪林弹雨、刀山火海、千难万阻”“虽千万人而吾往矣”——修辞性铺陈（P058）。"
   ],
   "conditions": [
    "作者以“无可置疑的”限定所讨论的美德，P027 扩展到“够用的美德”（P007、P027）。",
    "唯一例外条件：“除非人不成其为人，而成为一个无限者”（P017）。",
    "作者自注限定：“注意，绝对有效不等于绝对客观”（P021）。",
    "逻辑事实刚度的论证以“对自然规律的认知还有可能因为发现新的现象而改变”为对照（P020）。",
    "夸奖可否接受的判准在有无限定词：成绩好、比较聪明可接受，无限制的“聪明”应拒绝（P034-P036、P038）。",
    "勇敢的界定条件：必须出于对“不勇敢”后果的怯懦；否则称鲁莽甚至愚蠢（P065-P066）。",
    "作者排除一种误读：谦卑不是因为怕遭嫉恨、被人攻击而憋着不说、脸上假装（P029-P030）。",
    "题设经题主修正，P039-P043 的推论以修正后的题设为前提（P039）。"
   ],
   "rhetoric_and_tone": "论辩—推论式长文，语气自信且带训诫与反讽。用“尤其绝妙的是”“仔细咀嚼这两句话”“看到了吗？”等引导性、反问性措辞推进；以“第一神偷悖论”作类比，以“人类将全体疯狂”作夸张推论，以“通俗点说——”切换论述层级。多次直接对读者称“你”，并把评论区提问与题主修正题设纳入行文，形成对话式结构。结尾以“勇敢即怯懦。”的短句下断语，再用“伦理问题是高度复杂的，由此可见一斑”收束，语气由断言转为提示复杂性。",
   "unresolved_questions": [
    "P064 引语“如果我们什么都不做，华为六个月内就会倒闭。”的说话者与出处本文未标明，需外部核查，本记录不代为认定。",
    "P012 诗句的出处本文未标注，需外部核查。",
    "P017-P019 的“绝对自知者”“无限他知者”“无限能动者”是否指特定宗教或哲学对象，本文未点名，不作推断。",
    "“自悖效应”是否为作者自造术语、有无既有来源，本文未说明。",
    "P004 概念清单是否穷尽、各概念是否同质，本文未讨论。",
    "P014 关于“外人不能觉察人心”“当事人自查不可靠”的断言是论证前提，作者未给独立论证。",
    "题主前后两版题设（原题与 P039 修正版）以何为准，本文未说明。",
    "作者对“美德”本身的界定（哪些德性属“无可置疑”）未给出判准。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P002", "quote": "一个声言自己不诚实的人，反而往往比坚定地认为自己够诚实的人更令旁人觉得诚实。", "relation": "context"},
    {"key": "E2", "paragraph_id": "P003", "quote": "一个声言自己不客观的人，反而往往比坚定地认为自己肯定够客观的人更令旁人觉得客观。", "relation": "context"},
    {"key": "E3", "paragraph_id": "P004", "quote": "等等等等概念都有这个“自悖效应”。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P006", "quote": "其实答案已经一目了然了——它们的共性就是皆属美德。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P007", "quote": "凡属无可置疑的美德的，皆有“自悖效应”。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P008", "quote": "这是因为“人作为有限的存在永无充分立场宣称自己拥有无可置疑的美德”是一个逻辑上的客观事实。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P009", "quote": "重复一遍，人永无立场宣称自己拥有无可置疑的美德。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P011", "quote": "你会发现根本不存在一条逻辑路线，能证明一个人的任何行为组合与某项美德之间有无可置疑的对应关系。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P014", "quote": "人类也设计不出既足够有效而自己又不能绕过的道德判定手段。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P014", "quote": "而依靠当事人自查，又无法知道ta不是在自欺欺人或者干脆是有意欺骗。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P015", "quote": "人若宣称自知，则ta一定没有“知道自己不自知的”自知。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P016", "quote": "这种困境是客观的，在逻辑上是和人的绝对有限性绑死的、没得反驳的。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P017", "quote": "除非人不成其为人，而成为一个无限者。", "relation": "qualifies"},
    {"key": "E14", "paragraph_id": "P018", "quote": "只有一个绝对自知者，才有能力做这个自我保证人。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P019", "quote": "事实上，也只有一个无限能动者才能真正名副其实地承受无限苛刻的美德鉴定标准。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P020", "quote": "而由基本逻辑所保证的结论是“无法崩溃”的", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P021", "quote": "逻辑上的客观事实，已经是人类（或者说一切依靠逻辑律支撑的理性的存在）所绝无可能撼动的绝对有效事实（注意，绝对有效不等于绝对客观）。", "relation": "qualifies"},
    {"key": "E18", "paragraph_id": "P023", "quote": "你不具有有效的理性，你的一切自我声称因此尽皆失去了可靠性的基础。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P027", "quote": "这一行为，已经证明了此人绝对地缺少真的接近这项美德的能力——基本的逻辑判断力。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P028", "quote": "谦卑就是认识到了自身的绝对有限性，从此再也不会说我有某项无可置疑的美德，或宣称自己拥有某项美德而拒绝质疑。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P029", "quote": "这一丁点都不是心里明明如此认为，只是因为怕这样说了遭人嫉恨、被人攻击憋着不说", "relation": "qualifies"},
    {"key": "E22", "paragraph_id": "P030", "quote": "而是因为这些话的确逻辑上就不成立。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P031", "quote": "自我宣称即实际抛弃追求。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P032", "quote": "“那别人夸我这些，我应该接受呢？还是推辞‘我不是我没有’？”", "relation": "context"},
    {"key": "E25", "paragraph_id": "P034", "quote": "夸你“学习成绩好”，如果你分数确实很高，那么没问题。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P036", "quote": "说你“聪明”，拒绝。", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P038", "quote": "不加限定词的美德表述，不是人所能当得起的。", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P039", "quote": "题主修正了自己的题设", "relation": "context"},
    {"key": "E29", "paragraph_id": "P041", "quote": "一个人承认自己虚伪，这使得ta不虚伪。", "relation": "context"},
    {"key": "E30", "paragraph_id": "P042", "quote": "一个人承认自己怯懦，这使得ta不怯懦。", "relation": "context"},
    {"key": "E31", "paragraph_id": "P044", "quote": "这看起来似乎对我上面的美德的分析构成了一种挑战，但其实并非如此。", "relation": "contradicts"},
    {"key": "E32", "paragraph_id": "P045", "quote": "因为一个人承认自己虚伪，并没有使得此人（绝对地被证明）不虚伪。", "relation": "contradicts"},
    {"key": "E33", "paragraph_id": "P048", "quote": "一个人自称公正，这个行为可以绝对地证明此人不公正。", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P049", "quote": "但是一个人自称不公正，这个行为并不能绝对地证明此人公正，而只是让听到这话的人对这个人的公正有了更正面的期待。", "relation": "supports"},
    {"key": "E35", "paragraph_id": "P050", "quote": "“更正面的期待”几乎是没有重量的。", "relation": "supports"},
    {"key": "E36", "paragraph_id": "P051", "quote": "当“美德的对立面”被放入这个命题时，这个命题并没有同样的成立。", "relation": "supports"},
    {"key": "E37", "paragraph_id": "P052", "quote": "非美德并没有真的享受到美德所享受的“自悖效应认证”。", "relation": "supports"},
    {"key": "E38", "paragraph_id": "P053", "quote": "很多我们常认为互相对称对立的德性，其实它们的关系只是对比关系，并不是反义关系。", "relation": "supports"},
    {"key": "E39", "paragraph_id": "P054", "quote": "我举个典型的例子——勇敢和怯懦，其实并不是反义关系。", "relation": "supports"},
    {"key": "E40", "paragraph_id": "P057", "quote": "实际上，真正的勇敢，是对“不勇敢”的怯懦。", "relation": "supports"},
    {"key": "E41", "paragraph_id": "P059", "quote": "才构成了这种“宁可面对风险和代价也不退半步”的勇气。", "relation": "supports"},
    {"key": "E42", "paragraph_id": "P061", "quote": "不是我勇敢，而恰恰是我怯懦。", "relation": "supports"},
    {"key": "E43", "paragraph_id": "P065", "quote": "我们并不称其为勇敢，我们称其为鲁莽。", "relation": "supports"},
    {"key": "E44", "paragraph_id": "P066", "quote": "甚至是愚蠢。", "relation": "supports"},
    {"key": "E45", "paragraph_id": "P068", "quote": "勇敢即怯懦。", "relation": "supports"},
    {"key": "E46", "paragraph_id": "P069", "quote": "伦理问题是高度复杂的，由此可见一斑。", "relation": "supports"},
    {"key": "E47", "paragraph_id": "P064", "quote": "“如果我们什么都不做，华为六个月内就会倒闭。”", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["伦理学/道德哲学", "逻辑与认识论", "概念分析"],
   "issue_candidates": ["声言具备即证明不具备的自悖效应", "美德与自我宣称", "人的有限性与道德判定", "德性之间是对比还是反义关系", "勇敢与怯懦的关系"],
   "text_function_candidates": ["答疑", "论辩", "概念分析", "回复评论"],
   "object_candidates": ["题主", "评论区提问者", "人类", "第一神偷", "周公", "王莽", "企业家", "华为"],
   "working_keywords": ["自悖效应", "无可置疑的美德", "绝对有限性", "逻辑上的客观事实", "无限者", "谦卑", "自我宣称即实际抛弃追求", "对比关系", "反义关系", "勇敢即怯懦"]
  },
  "notes": "本篇无图片，69 段正文已完整读取。P032 为作者引述的评论区提问、P039-P043 为作者转述的题主修正题设及其公式套用，均属提问者/评论者一侧，已按 attribution=questioner 标注。P064 引语（“如果我们什么都不做，华为六个月内就会倒闭。”）未标明说话者，记录为 quoted_or_cited + attribution=unknown，需外部核查，本记录不代为认定。P012 诗句出处未标注。无版本/取代信息。",
 },
 "754f6925": {
  "analysis": {
   "question_context": "提问者问“在A股买低估值的股票有什么意义？”（Q001，属提问者）。作者不讨论长期估值投资，而是从上市资格（壳）的角度作答：在政策制定者极端忌讳退市的前提下上市门槛高，低估值上市企业的“座位”因此值钱；但买壳消息一旦泄露会引来投机、真买壳者取消交易，于是给出两条观察指标（退市机制改革、并购消息的真假）与撤离劝告，并声明不构成投资建议。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "提出前提并推出“座位”价值：退市被忌讳导致上市门槛高，低估值企业的上市资格值钱，股价越低越值钱。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005", "P006"], "summary": "买壳博弈：消息泄露引来投机、股价冲天，真买壳者取消交易；若无取消消息则是假买壳、割韭菜。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P007", "P008", "P009"], "summary": "第一条观察指标：盯住上市退市机制改革，门槛降低或退市完善即预示亏损，此为两级警报。", "role": "action_advice"},
    {"unit_id": "U004", "paragraph_refs": ["P010", "P011", "P012"], "summary": "第二条观察指标：并购消息迟迟不取消、反而辟谣或不予置评且股价攀升时，应尽快离场。", "role": "action_advice"},
    {"unit_id": "U005", "paragraph_refs": ["P013"], "summary": "免责声明：以上全部不构成投资建议。", "role": "qualification"}
   ],
   "main_claims": [
    {"claim_id": "C000", "claim_type": "open_question", "attribution": "questioner", "modality": "questioned", "statement": "提问者的问题：在A股买低估值的股票有什么意义。", "evidence": []},
    {"claim_id": "C001", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "在政策制定者极端忌讳股票退市的逻辑前提下，自然会导致上市门槛高。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这意味着凡是低估值的上市企业都至少有一个“座位”值钱；股价越低，“座位”的可交易性越好、这项资产的价值越高。", "evidence": ["E2", "E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "收购者不是傻瓜：并购买壳谈判消息一旦泄露就会有大量人挤进来投机、股价冲天，此时真买壳的收购者必定取消交易。", "evidence": ["E4", "E5"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "如果买壳谈判没有传出取消的消息，那这就是假买壳、割韭菜无疑——放消息的一方在趁外界跟风高位抛售。", "evidence": ["E6"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "第一条警报：盯住上市退市机制改革——上市门槛降低就会亏，退市机制完善预示着要亏；这已是两级警报，再被割怪不得谁。", "evidence": ["E7", "E8"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "第二条警报：已传出并购消息却迟迟不宣布“取消交易”，反而“辟谣”或“不予置评”且股价攀升时，劝此时快走，“铡刀随时落下”。", "evidence": ["E9", "E10", "E11"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者声明：以上全部不构成投资建议。", "evidence": ["E12"]}
   ],
   "argument_steps": [
    "设定前提：政策制定者极端忌讳股票退市，故上市门槛高（P001）。",
    "推出结论：低估值上市企业至少有一个“座位”值钱，股价越低该资产价值越高（P002-P003）。",
    "引入博弈方：消息泄露引来大量投机者，股价冲天（P004）。",
    "推出真买壳者的反应：必定取消交易（P005）。",
    "给出识别规则：若无取消消息，即为假买壳、割韭菜，放消息方在高位抛售（P006）。",
    "转入操作建议，先设“你要玩这种游戏的话”这一适用限定（P007）。",
    "第一条指标：盯上市退市机制改革，门槛降低或退市完善都是亏损信号，构成两级警报（P008-P009）。",
    "第二条指标：盯潜伏低价股的并购消息，出现不取消、反而辟谣或不予置评且股价攀升的组合即应撤离（P010-P011）。",
    "以“铡刀随时落下”强调风险（P012）。",
    "以“以上全部不构成投资建议”作免责收束（P013）。"
   ],
   "concept_usage": [
    {"term": "低估值", "meaning": "本文用于指股价低的上市企业，并把它与“座位”（上市资格/壳）价值挂钩（P002-P003）。", "evidence": "P002", "ambiguity": "作者未给出估值指标（如市盈率、市净率）或低估的判定标准。"},
    {"term": "“座位”", "meaning": "作者对上市资格的比喻：低估值上市企业至少有一个“座位”值钱，股价越低其可交易性与价值越高（P002-P003）。", "evidence": "P003", "ambiguity": "“座位”如何估值、如何交易，本文未说明。"},
    {"term": "买壳/并购买壳", "meaning": "收购方取得上市资格的交易；作者讨论其消息泄露后的投机与取消（P004-P006）。", "evidence": "P004", "ambiguity": "作者未区分借壳上市与一般并购。"},
    {"term": "割韭菜", "meaning": "本文指放消息的一方趁外界跟风在高位抛售（P006）。", "evidence": "P006", "ambiguity": "作者未说明如何事先区分真买壳与假买壳。"},
    {"term": "两级警报", "meaning": "指上市门槛降低与退市机制完善两项政策变化（P008-P009）。", "evidence": "P009", "ambiguity": "作者未给出警报触发后的具体应对措施。"}
   ],
   "examples_and_targets": [
    "政策制定者极端忌讳股票退市——作者论证所依赖的前提（P001），其事实状态需外部核查。",
    "收购者、投机者、放消息的一方——作者分析的博弈主体（P004-P006）。",
    "“铡刀随时落下”——风险比喻（P012）。",
    "“以上全部不构成投资建议”——作者自设免责声明（P013）。"
   ],
   "conditions": [
    "论证以“政策制定者极端忌讳股票退市”为前提（P001）。",
    "投机与取消交易的连锁反应以“消息一旦被泄露”为条件（P004）。",
    "假买壳的判断条件：“如果买壳谈判没有传出取消的消息”（P006）。",
    "操作建议的适用限定：“所以你要玩这种游戏的话”（P007）。",
    "亏损条件明说：上市门槛降低、退市机制完善（P008）。",
    "免责限定：作者声明上述内容不构成投资建议（P013）。"
   ],
   "rhetoric_and_tone": "冷峻简短的机制分析加操作提示。用“座位”“割韭菜”“铡刀随时落下”等比喻压缩复杂关系；以序号（1）2））并列两条观察指标，句子短促、结论直下（“这个时候，真买壳的收购者必定会取消交易”“劝你这时候快走”）。带警告与自保意味（“再被割也怪不得谁了”），结尾用免责声明收束。",
   "unresolved_questions": [
    "“低估值”的具体指标与判定标准本文未界定（P002）。",
    "“座位”（上市资格/壳）如何估值与交易，本文未说明（P002-P003）。",
    "作者分析所依赖的前提“政策制定者极端忌讳股票退市”属事实断言，需外部核查（P001）。",
    "“上市退市机制改革”的具体内容与时间表本文未说明（P008）。",
    "作者未回答提问中“买低估值股票有什么意义”在长期投资意义上的部分，仅讨论壳价值博弈。",
    "如何事先区分真买壳与假买壳，作者只给出事后判据（P006、P010）。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "在政策制定者极端忌讳股票退市的逻辑前提下，自然会导致上市门槛高。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "这意味着凡是低估值的上市企业都至少有一个“座位”值钱。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "股价越低，“座位”的可交易性越好，“座位”这项资产的价值就越高。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "并购买壳谈判的消息一旦被泄露，就会有大量的人挤进来投机。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "这个时候，真买壳的收购者必定会取消交易。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "那么这就是假买壳、割韭菜无疑", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P008", "quote": "上市门槛降低，你就亏了。退市机制完善，就预示着你要亏。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P009", "quote": "这已经给了你两级警报，再被割也怪不得谁了。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P010", "quote": "双方却迟迟没有宣布“取消交易”，反而是“辟谣”或者“不予置评”，而且股价在攀升。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P011", "quote": "劝你这时候快走。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P012", "quote": "铡刀随时落下。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P013", "quote": "以上全部不构成投资建议。", "relation": "qualifies"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["证券市场", "投资策略", "政策与监管"],
   "issue_candidates": ["A股买低估值股票的意义", "上市资格（壳）价值", "买壳消息与投机", "退市机制改革对低价股的影响"],
   "text_function_candidates": ["答疑", "机制分析", "操作提示"],
   "object_candidates": ["A股", "政策制定者", "收购者", "投机者", "低估值上市企业"],
   "working_keywords": ["低估值", "座位", "买壳", "割韭菜", "上市门槛", "退市机制", "两级警报", "铡刀"]
  },
  "notes": "本篇无图片，正文 13 段已完整读取。作者论证以“政策制定者极端忌讳股票退市”为前提，属需外部核查的事实断言，本记录不作裁决。P013 为作者自设的免责声明。无版本/取代信息。",
 },
 "b21f0365": {
  "analysis": {
   "question_context": "提问者问“有什么可以给intj的人生建议吗？”（Q001，属提问者）。作者没有逐条给建议，而是整体劝阻采用人格分型框架：先论证“型”只是抽象化的心理构造，只有在主张心理构造不可能显著改变时才能成立；再以木头/石头与水/油、非牛顿流体作比，说明人的心理不可预测、有治愈缺陷的无限可能；随后承认这类测试在大企业风险管理中有有限的工具性用途，但指出其有效性依赖保密与容许误差两个要害，最终把对它的追捧定性为一种偶像崇拜，并以“你是自由的，一切都由你自己决定”作结。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "开篇劝告：少看人格分型理论，不要自误。", "role": "action_advice"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005"], "summary": "论证“型”的成立条件：若型确定且不可转换则缺陷成绝症；型只是抽象化的心理构造。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007", "P008", "P009", "P010"], "summary": "以木头石头与水油、非牛顿流体作比，说明人的心理构造可变、有治愈的无限可能。", "role": "example"},
    {"unit_id": "U004", "paragraph_refs": ["P011", "P012"], "summary": "定性：宣称人有型是贩售安慰剂、换取放弃自我解决；分型理论不尊重人的不可预测性。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P013", "P014", "P015"], "summary": "对读者断言：你什么型也不是；自我归类等于自我放弃与自我戕害。", "role": "claim"},
    {"unit_id": "U006", "paragraph_refs": ["P016", "P017", "P018", "P019", "P020", "P021"], "summary": "附注告诫：不要据星座八字血型等“相合”对人作特殊预料；并预防性地回应追问。", "role": "action_advice"},
    {"unit_id": "U007", "paragraph_refs": ["P022", "P023", "P024"], "summary": "承认分型并非完全无用，但用处是企业风险管理决策而非个人人生规划。", "role": "qualification"},
    {"unit_id": "U008", "paragraph_refs": ["P025", "P026", "P027", "P028", "P029", "P030", "P031"], "summary": "说明其来源与有效性条件：征兵智商测试的企业应用版，测过总好过不测，信度不高但有短期价值。", "role": "reason"},
    {"unit_id": "U009", "paragraph_refs": ["P032", "P033", "P034", "P035", "P036"], "summary": "提出两个要害：必须保密（题库泄露即失效）、一开始就容许误差（要求低得惊人）。", "role": "qualification"},
    {"unit_id": "U010", "paragraph_refs": ["P037", "P038", "P039", "P040"], "summary": "指出追捧的成因与性质：军队与企业用过即被追捧，实为偶像崇拜，并反问是否值得。", "role": "rebuttal"},
    {"unit_id": "U011", "paragraph_refs": ["P041", "P042", "P043", "P044", "P045", "P046"], "summary": "强调偶像崇拜从无善果；当代企业实践只是寻求“新神谕”的仪式，与古时求吉凶无本质区别。", "role": "reason"},
    {"unit_id": "U012", "paragraph_refs": ["P047", "P048", "P049", "P050", "P051"], "summary": "结论：它们的迷信不足以定义你，人是自由的、一切由自己决定。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C000", "claim_type": "open_question", "attribution": "questioner", "modality": "questioned", "statement": "提问者的问题：有什么可以给 intj 的人生建议。", "evidence": []},
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "劝告：少看这些“人格分型”理论，不要自误。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "如果人存在被确定的“型”且不能转换，那就等于说很多心理疾病和认知缺陷是绝症。", "evidence": ["E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“型”本身不过是抽象化的心理构造；只有在主张“人的心理构造不可能发生显著的改变”的前提下，才有可能主张人有“型”可言。", "evidence": ["E4", "E5"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "比喻论证：木头、石头才有型，水、油没有型；只有固态的、变形过大就会碎裂的东西才有“型”可言。", "evidence": ["E6", "E7"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人类的心理构造像非牛顿流体——骤然加之坚如钢铁，缓缓揉捏软如稀泥；正因如此，人类才有治愈一切认知缺陷和心灵创伤的无限可能性。", "evidence": ["E8", "E9"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "宣称人有型只是贩售自我认知感的安慰剂，换取了人对自己解决自身心灵缺陷的放弃。", "evidence": ["E10"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "星座性格、称骨法、九型人格等都是对人类最本质的高贵性——不可预测性——的不尊重。", "evidence": ["E11"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "你什么型也不是；你“属于”某种型只会是你自己放弃的结果。", "evidence": ["E12", "E13"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "说“我就是xx样的人”等于放弃极大段生命可能，相关缺陷成为无法改变的绝症，并叫别人放弃对你是别样的人的一切期待；或迟或早你会意识到这是自我戕害。", "evidence": ["E14", "E15"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "不要因为星座、属相、八字、血型、九型人格“相合”而对特定人给予任何特殊预料，作者称其极度危险。", "evidence": ["E16"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者对读者的预防性回应：不要猜答主是哪型，并自称“五毒俱全，多重人格”，警告“勿谓言之不预”。", "evidence": ["E17", "E18", "E19"]},
    {"claim_id": "C012", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "人格分型并非完全没用，但其用处绝不是帮助个人规划人生，而是帮助大企业在接受一定错误率的基础上做管理风险决策。", "evidence": ["E20"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这套东西是美国大规模征兵时搞出来的“智商测试”的企业应用版。", "evidence": ["E21"]},
    {"claim_id": "C014", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "其“有效性”以待测样本未被污染（题库未泄露）为前提，是一次误差可以容忍（测过总好过不测）的测量；及格线就是“测过总好过不测”。", "evidence": ["E22", "E23"]},
    {"claim_id": "C015", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "在此基准上，智商测试、能力测试、性格类型测试在题库未泄露的前提下有短期的、信度虽然不高但并非完全没有意义的实用价值。", "evidence": ["E24"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "理由是用错人在关键组织问题上代价无比巨大：战场军官、跨国企业管理人员（甚至一线人员）手一滑就是人命关天、金额巨大的契约责任。", "evidence": ["E25", "E26"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "两个要害：第一，它必须是秘密，题库泄露就会基本失效（做题家能把 intp 做到让人跪地求饶）；第二，它一开始就被允许有测量误差，要求低得惊人——一百个里发现一两个不适格就算立大功。", "evidence": ["E27", "E28", "E29", "E30"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "是大企业与强大的军队曾用过这些“四面漏风”但不失为有价值的工具，导致人们疯狂追捧它们。", "evidence": ["E31"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "说穿了，这是一种以“面试圣经”形式传播的新世纪的偶像崇拜——将获胜的军队、赚钱的企业视作领受了特殊启示的真理代言人。", "evidence": ["E32"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者反问：它们评价人的标准（还是几十年前用过的废弃物）被当成“正确的标准”、值得人按框框重塑自身，真的值得吗？", "evidence": ["E33", "E34"]},
    {"claim_id": "C021", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "偶像崇拜这种事，从无善果（作者要求记住这句话）。", "evidence": ["E35", "E36"]},
    {"claim_id": "C022", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "这件事追根到底是一种偶像崇拜，甚至不是第一波而是早就过去的余波；如今大公司仍在笔试试卷中安排巧妙问题、对关键职位做行为分析与笔迹分析，但那早就不是“九型人格”这类东西了。", "evidence": ["E37", "E38"]},
    {"claim_id": "C023", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "这样做的企业其实只是买个心安——它们也有自己内心的脆弱无法面对，必须寻求“新神谕”——类似科学——的仪式来安慰自己。", "evidence": ["E39"]},
    {"claim_id": "C024", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人类这五千年来几乎没有什么真正的进步：几千年前出征要请法师登坛做法求吉凶，今天面试大区主管要请“心理学家”看真伪，没有本质区别。", "evidence": ["E40"]},
    {"claim_id": "C025", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "别以为它们就真的很真理；它们的迷信根本不足以定义你，无论“它们”是多么伟大的存在都一样。", "evidence": ["E41", "E42", "E43"]},
    {"claim_id": "C026", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "结论：你是自由的，一切都由你自己决定。", "evidence": ["E44"]}
   ],
   "argument_steps": [
    "开篇给出劝告：少看人格分型理论，不要自误（P001-P002）。",
    "以反证法指出：若型确定且不可转换，很多心理疾病与认知缺陷就成绝症（P003）。",
    "指出型只是抽象化的心理构造，其成立以“心理构造不可能显著改变”为前提（P004-P005）。",
    "用木头石头与水油的比喻说明“型”只属于固态物（P006-P007）。",
    "用非牛顿流体比喻人的心理构造，推出治愈缺陷与创伤的无限可能性（P008-P010）。",
    "定性：宣称人有型是安慰剂，换取人放弃自我解决（P011）。",
    "把星座、称骨法、九型人格归为对“不可预测性”的不尊重（P012）。",
    "直接对读者断言“你什么型也不是”，并推演自我归类的后果与自我戕害（P013-P015）。",
    "附注告诫不要据星座八字血型等“相合”对人作预料，并预防性回应追问（P016-P021）。",
    "让步：承认分型并非完全无用，但定位为企业风险管理决策工具（P022-P024）。",
    "追溯来源（征兵智商测试的企业应用版）并界定有效性前提与及格线（P025-P027）。",
    "在限定条件下承认其短期、低信度但非无意义的实用价值（P028）。",
    "给出理由：关键组织问题上用错人代价巨大（P029-P030），且成本不高（P031）。",
    "提出两个要害：必须保密、容许误差（P032-P036）。",
    "指出追捧成因：军队与企业用过；并把它定性为新世纪的偶像崇拜（P037-P038）。",
    "反问标准是否值得遵循，并断言偶像崇拜从无善果（P039-P042）。",
    "指出这是旧余波，当代企业实践只是寻求“新神谕”的仪式（P043-P046）。",
    "结论：它们的迷信不足以定义你，你是自由的（P047-P051）。"
   ],
   "concept_usage": [
    {"term": "人格分型/“型”", "meaning": "本文指把人的心理构造抽象化为固定类型的理论；作者主张只有在“人的心理构造不可能发生显著的改变”的前提下才能主张有“型”（P004-P005）。", "evidence": "P005", "ambiguity": "作者未区分不同分型工具的理论构造，统称为“这些‘人格分型’理论”。"},
    {"term": "不可预测性", "meaning": "作者称其为“人类最本质的高贵性”，被分型理论所不尊重（P012）。", "evidence": "P012", "ambiguity": "作者未说明该属性与随机性或可塑性的关系。"},
    {"term": "非牛顿流体", "meaning": "作者用来比喻人类心理构造：骤然加之坚如钢铁，缓缓揉捏软如稀泥（P009）。", "evidence": "P009", "ambiguity": "比喻与“无限可能性”结论之间的推论作者未给实证依据。"},
    {"term": "偶像崇拜", "meaning": "作者对分型/测评被追捧这一现象的定性：将获胜的军队、赚钱的企业视作领受特殊启示的真理代言人（P038、P041-P043）。", "evidence": "P038", "ambiguity": "作者未界定“偶像崇拜”的判定标准，也未说明工具性使用与崇拜的界线。"},
    {"term": "新神谕", "meaning": "作者讽刺企业寻求“类似科学”的测评仪式以自我安慰的说法（P045）。", "evidence": "P045", "ambiguity": "属修辞性命名，作者未展开。"},
    {"term": "智商测试的企业应用版", "meaning": "作者对人格分型来源的定位：美国大规模征兵时搞出来的智商测试（P025）。", "evidence": "P025", "ambiguity": "该历史来源的说法需外部核查。"}
   ],
   "examples_and_targets": [
    "intj（提问者所问的类型）——提问者话题，作者未按该框架作答（Q001、P001-P002）。",
    "星座性格、称骨法、九型人格——作者批评的对象（P012、P017）。",
    "属相、八字、血型——作者告诫不要据以判断“相合”的对象（P017）。",
    "美国大规模征兵时搞出来的“智商测试”——作者所述来源（P025），需外部核查。",
    "战场上的军官、跨国企业里的管理人员甚至一线人员——作者举例说明用错人的代价（P030）。",
    "“你要intp是吧？信不信做题家们能intp到你跪地求饶？”——调侃式例证，说明题库泄露后失效（P034）。",
    "“面试圣经”——传播形式的比喻（P038）。",
    "行为分析、笔迹分析、面试大区主管请“心理学家”——当代企业实践举例（P044-P046）。",
    "几千年前出征前请法师登坛做法求吉凶——历史类比（P046）。"
   ],
   "conditions": [
    "条件句：如果人存在被确定的“型”而且不能转换（P003）。",
    "前提条件：只有在主张“人的心理构造不可能发生显著的改变”的前提下才能主张有“型”可言（P005）。",
    "有效性的前提：待测样本没有被污染，也就是试卷体系还没有被泄露（P026）。",
    "有效性的及格线：测过总好过不测（P027）。",
    "价值限定：短期、信度虽然不高、结论并非完全没有意义（P028）。",
    "成本条件：只要有所帮助、成本不是太高（P031）。",
    "两个要害构成使用条件：必须保密；被允许有测量误差（P033、P035）。",
    "用途限定：用于大企业在接受一定错误率的基础上做管理风险决策，不用于个人人生规划（P024）。"
   ],
   "rhetoric_and_tone": "训诫与讽刺混合，语气强硬而直接。开篇用命令句（“少看这些‘人格分型’理论”“不要自误”）；以“木头、石头才有型，水、油没有型”“非牛顿流体”作通俗类比；用“贩售自我认知感的安慰剂”“新世纪的偶像崇拜”“新神谕”“面试圣经”作讽刺性命名；以“勿谓言之不预”“真的值得吗？真的吗？”“你是自由的，一切都由你自己决定”等短句作节奏性收束。ps/pps 段落以自我调侃（“五毒俱全，多重人格”）预防读者追问。第二人称“你”贯穿全篇，多处直接对读者下断语。",
   "unresolved_questions": [
    "“人格分型是美国大规模征兵时搞出来的‘智商测试’的企业应用版”属作者的历史断言，需外部核查（P025）。",
    "由“非牛顿流体”比喻推出“治愈一切认知缺陷和心灵创伤的无限可能性”，作者未给实证依据（P009-P010）。",
    "作者一方面承认分型对企业管理决策有实用价值，一方面称其迷信不足以定义个人，工具性使用与偶像崇拜的界线未明确界定（P024、P049）。",
    "“称骨法”等术语本文未作解释（P012）。",
    "提问者所问“给 intj 的人生建议”未被逐条回答，作者改为整体劝阻使用分型框架（Q001 与 P001-P002）。",
    "P020 作者自称“五毒俱全，多重人格”属调侃性回应，不宜作事实陈述，记录中按修辞保留。",
    "P044-P046 关于当代企业测评实践的描述属作者叙述，需外部核查。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "少看这些“人格分型”理论。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "不要自误。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "如果人存在被确定的“型”，而且不能转换，那么这就等于说很多心理疾病和认知缺陷是绝症。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "因为“型”本身不过是抽象化的心理构造。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "只有在主张“人的心理构造不可能发生显著的改变”的前提下，才有可能主张人有“型”可言。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "形象点说——木头、石头才有型，水、油没有型。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "只有固态的东西，如同混凝土那样变形过大就会碎裂的东西，才有“型”可言。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P009", "quote": "像非牛顿流体——骤然加之，坚如钢铁；缓缓揉捏，软如稀泥。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P010", "quote": "正因为如此，人类才有治愈一切认知缺陷和心灵创伤的无限可能性。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P011", "quote": "宣称人有型，只是通过贩售自我认知感的安慰剂，换取了人对自己解决自身的心灵缺陷的放弃。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P012", "quote": "都是对人类最本质的高贵性——不可预测性——的不尊重。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P013", "quote": "你什么型也不是。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P014", "quote": "你“属于”某种型，只会是你自己放弃的结果。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P014", "quote": "与这个构型相关联的缺陷对你就是再也无法改变的绝症。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P015", "quote": "或迟或早，你一定会意识到，这是一种自我戕害。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P017", "quote": "不要因为什么星座、属相、八字、血型、九型人格“相合”而对特定人给予任何特殊预料，极度危险。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P019", "quote": "提前打预防针——不要猜答主是哪型。", "relation": "context"},
    {"key": "E18", "paragraph_id": "P020", "quote": "五毒俱全，多重人格，属于哪种精神病完全取决于几点看医生。", "relation": "context"},
    {"key": "E19", "paragraph_id": "P021", "quote": "勿谓言之不预。", "relation": "context"},
    {"key": "E20", "paragraph_id": "P024", "quote": "但是那个用处绝不是帮助你规划人生的，那个是用来帮助大企业在接受一定错误率的基础上做管理风险决策的。", "relation": "qualifies"},
    {"key": "E21", "paragraph_id": "P025", "quote": "说白了，这个东西是美国大规模征兵时搞出来的“智商测试”的企业应用版。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P026", "quote": "进行一次误差可以容忍（也就是测过总好过不测）的测量。", "relation": "qualifies"},
    {"key": "E23", "paragraph_id": "P027", "quote": "看清楚这东西的有效性的及格线——测过总好过不测。", "relation": "qualifies"},
    {"key": "E24", "paragraph_id": "P028", "quote": "这些智商测试、能力测试、性格类型测试都在题库没有泄露的前提下有短期的、信度虽然不高、但是结论并非完全没有意义的实用价值。", "relation": "qualifies"},
    {"key": "E25", "paragraph_id": "P029", "quote": "因为用错人在关键的组织问题上是一个代价无比巨大的核心问题。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P030", "quote": "手一滑就是人命关天、金额巨大的契约责任。", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P033", "quote": "第一，它必须是秘密，题库泄露就会基本失效。", "relation": "qualifies"},
    {"key": "E28", "paragraph_id": "P034", "quote": "你要intp是吧？信不信做题家们能intp到你跪地求饶？", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P035", "quote": "第二，它一开始就被允许有测量误差——要求低得惊人。", "relation": "qualifies"},
    {"key": "E30", "paragraph_id": "P036", "quote": "一百个里面发现一两个不适格的就算你为公司和国家立下大功了。", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P037", "quote": "是因为有大企业，强大的军队曾经用过这些四面漏风，但不失为有价值的工具，导致人们疯狂的追捧它们。", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P038", "quote": "说穿了，这就是一种以“面试圣经”形式被传播的新世纪的偶像崇拜", "relation": "supports"},
    {"key": "E33", "paragraph_id": "P039", "quote": "它们评价人的标准（还是几十年前曾经用过的废弃物而已），一定是“正确的标准”", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P040", "quote": "真的值得吗？真的吗？", "relation": "supports"},
    {"key": "E35", "paragraph_id": "P041", "quote": "偶像崇拜这种事，从无善果。", "relation": "supports"},
    {"key": "E36", "paragraph_id": "P042", "quote": "记住这句话——偶像崇拜这件事，从无善果。", "relation": "supports"},
    {"key": "E37", "paragraph_id": "P043", "quote": "而这件事，追根到底，其实是一种偶像崇拜——甚至还不是第一波，而是早就过去的余波。", "relation": "supports"},
    {"key": "E38", "paragraph_id": "P044", "quote": "但是那早就不是“九型人格”这类东西了。", "relation": "qualifies"},
    {"key": "E39", "paragraph_id": "P045", "quote": "必须寻求“新神谕”——类似科学——的仪式来安慰自己。", "relation": "supports"},
    {"key": "E40", "paragraph_id": "P046", "quote": "今天面试个大区主管要请“心理学家”看真伪，其实没有什么本质的区别。", "relation": "supports"},
    {"key": "E41", "paragraph_id": "P047", "quote": "别以为它们就真的很真理。", "relation": "supports"},
    {"key": "E42", "paragraph_id": "P049", "quote": "它们的迷信根本不足以定义你。", "relation": "supports"},
    {"key": "E43", "paragraph_id": "P050", "quote": "无论“它们”是多么伟大的存在都一样。", "relation": "supports"},
    {"key": "E44", "paragraph_id": "P051", "quote": "你是自由的，一切都由你自己决定。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["心理学与人格理论", "社会批评", "管理与组织", "自我认知"],
   "issue_candidates": ["人格分型是否成立", "心理构造的可变性", "分型与命运/自我放弃", "心理测评在企业用人中的用途与限度", "对测评工具的偶像崇拜"],
   "text_function_candidates": ["答疑", "论辩", "训诫", "批评"],
   "object_candidates": ["intj/intp", "九型人格", "星座性格", "称骨法", "美国大规模征兵", "大企业", "军队", "做题家", "心理学家"],
   "working_keywords": ["人格分型", "型", "非牛顿流体", "不可预测性", "安慰剂", "偶像崇拜", "新神谕", "面试圣经", "测过总好过不测"]
  },
  "notes": "本篇无图片，51 段正文已完整读取。作者关于“人格分型源于美国大规模征兵时的智商测试”“当代企业用行为分析、笔迹分析”等叙述属其事实断言，需外部核查，本记录不裁决。P019-P021 为作者对读者可能追问的预防性回应，其中“五毒俱全，多重人格”属调侃，不按事实陈述处理。提问者所问的“给 intj 的人生建议”未被逐条回答，作者改为整体劝阻采用分型框架。无版本/取代信息。"
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
