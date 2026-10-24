# -*- coding: utf-8 -*-
"""批次 r001-b0145 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0145.sessions.py            # 写 out/r001-b0145.out.jsonl
  python3 records/r001-b0145.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0145"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0145.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "070114cf": {
  "analysis": {
   "question_context": "知乎提问者问“领导说有困难可以跟他说，是什么意思？”（Q001，立场属提问者，提问者未表态）。作者以答主身份先给出这句话的实际判定规则（不能用早已知情却未上报的困难作为失败理由），再补充领导说这话的两种可能（被坑怕后的口头禅／专门说给你听），后半转向职场新人应掌握的团队伦理：困难观、上报机制、有错与有罪之别。正文不追问领导本人的真实动机证据，而是给出下属的行为规则。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001","P002","P003","P004","P005","P006","P007"], "summary": "用“你先前是否知道／是否说过／交付结果是否合格／是否拿未说的困难当理由”的组合，界定“有困难就说”的实际含义：不能把早知道而未说过的困难当作失败理由。", "role": "definition"},
    {"unit_id": "U002", "paragraph_refs": ["P008","P009","P010"], "summary": "把这句话定性为给下属免责、保命的机会；劝读者不要听网上阴阳怪气的话。", "role": "action_advice"},
    {"unit_id": "U003", "paragraph_refs": ["P011","P012","P013","P014"], "summary": "补充说明领导说这话的第一种可能：被坑怕之后形成、对谁都会下意识说的口头禅。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P015","P016","P017","P018","P019","P020","P021"], "summary": "描述中下层领导带新人、换人极快的情形；批评新人听信网上“防领导”“压榨员工”的叙事，并断言被压榨者必因走投无路而无能、进而没有效能。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P022","P023","P024","P025","P026","P027","P028"], "summary": "以公司须达到社会平均生产率为前提，论证“公司能生存的效率”与“员工全是走投无路接受压榨的垫底劳动力”逻辑不相容，故老板不靠压榨，说这话不是为了挤兑、为难、考验你。", "role": "rebuttal"},
    {"unit_id": "U006", "paragraph_refs": ["P029","P030","P031","P032","P033","P034","P035","P036"], "summary": "老板关注的是完成业务、让客户付款；被瞒出来的雷炸怕后养成加一句“有困难一定要跟我说”的习惯，重音“一定”表示诚意十足。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P037","P038","P039","P040","P041","P042"], "summary": "第二种可能：这话专门说给你听，因为你还没与团队领袖建立默契和信任，需要额外提醒你存在这个试炼；老员工早已知道规则，用不着提醒。", "role": "claim"},
    {"unit_id": "U008", "paragraph_refs": ["P043","P044","P045","P046","P047","P048","P049","P050","P051","P052","P053","P054"], "summary": "把回应这句话界定为极其困难的试炼：承认困难与不承认困难都难；憋住不说或把一切都当困难都会被前辈看破；像横杆只有一个平衡点，正确的一毫米难以捉摸。", "role": "claim"},
    {"unit_id": "U009", "paragraph_refs": ["P055","P056","P057","P058"], "summary": "提出回应方式取决于团队意识；指出职场纯新人有一段“超级免责”的见习期，最大任务是适应团队文化，而困难观是团队文化最核心的内容之一。", "role": "claim"},
    {"unit_id": "U010", "paragraph_refs": ["P059","P060"], "summary": "定义困难观：团队如何定义需要投入资源的困难、困难的责任、恰当上报途径、处理机制和合法表达；任何困难都可提，关键在姿态、立场、方式。", "role": "definition"},
    {"unit_id": "U011", "paragraph_refs": ["P061","P062","P063","P064","P065","P066"], "summary": "以情侣吵架影响白天工作为例：须表述为团队可应对的客观影响才成合法困难；团队干预手段有限；成本应由本人承担；告知本身即对团队的贡献。", "role": "example"},
    {"unit_id": "U012", "paragraph_refs": ["P067","P068","P069","P070","P071","P072","P073","P074","P075","P076"], "summary": "讲上报纪律：循轨上报并书面留痕，不能因怕没人作证而擅自绕过机制公开乱报；不同性质信息有不同规定渠道（如举报上司贪污）；若规定一切只能报顶头上司，则你加入的是上司的私人团队。", "role": "action_advice"},
    {"unit_id": "U013", "paragraph_refs": ["P077","P078","P079","P080","P081","P082","P083","P084","P085","P086"], "summary": "划分团队与个人责任：团队（听汇报的上司）须教你困难如何表述与处理，你须记住并适应；不接受该义务就不算团队成员，建议及早另寻归宿或辞职，但不能不辞职又不接受。", "role": "claim"},
    {"unit_id": "U014", "paragraph_refs": ["P087","P088","P089","P090","P091","P092","P093","P094"], "summary": "区分有错与有罪：不适格上司会出现“是ta叫你告诉，你告诉了ta却又说你有罪”；合格上司须给出可说不可说的法则并赦免无知之错；有错是中性的，罪指故意选择违约。", "role": "definition"},
    {"unit_id": "U015", "paragraph_refs": ["P095","P096","P097","P098","P099","P100","P101","P102","P103","P104"], "summary": "解释新人被指错时的屈辱痛苦来自“错误-恐惧”心理反射，以及家庭和学校教育对团队伦理的教育近乎为零；团队规则属自然规律，不了解是个人无知的责任。", "role": "reason"},
    {"unit_id": "U016", "paragraph_refs": ["P105","P106","P107","P108","P109","P110","P111","P112","P113","P114"], "summary": "判断上司不适格及其根源；提出当领袖须承受无限制的精神压力，说这句话就要准备看到大堆失格的困难，否则是自己先没把自己的话当回事。", "role": "claim"},
    {"unit_id": "U017", "paragraph_refs": ["P115","P116","P117","P118","P119","P120"], "summary": "总结：没有不可说的困难，关键是在新人期学会所投身团队的困难观；领导出尔反尔属领导不适格，可考虑跳槽；能适应不适格上司是很值钱的能力，此类成员反而比不适格领导更核心。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“有困难就说”的实际含义是：事后列出的原因里，不该有任何一条是你之前就知道而上司却没听你说过的。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这句话是给下属免责、保命的机会，不懂得用怪不了别人。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只要是阴阳怪气说的话，不管说的是什么，都不要听。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "领导说这话有两种可能：一是被坑怕后对谁都说的口头禅，二是专门说给你听的提醒。", "evidence": ["E4","E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "除可作人身威胁的地方豪强一类例外，没有几个老板能靠“压榨员工”行走江湖。", "evidence": ["E29"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“公司有能生存的生产效率”与“公司员工都是走投无路不能不接受压榨的垫底劳动力”这两者逻辑不相容，所以公司不可能靠压榨垫底劳动力存活。", "evidence": ["E6"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "老板说这话不是为了挤兑、为难、考验你；老板眼里根本没有你，只想顺利稳妥迅速地完成任务。", "evidence": ["E7"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "专门对你说这话，是因为你还没像老员工一样与团队领袖建立起默契和信任，需要额外提醒你存在这个试炼。", "evidence": ["E8"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这是一个极其困难的试炼：承认困难与不承认困难都很难，且只有一个精确的平衡点。", "evidence": ["E9"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "困难观指团队如何定义需要投入资源的困难、困难的责任、恰当上报途径、恰当处理机制与合法表达。", "evidence": ["E10"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "任何困难都是可以提的，问题在于你以什么姿态、立场、方式去提。", "evidence": ["E11"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "个人私事须表述为对团队工作的客观影响（如“因个人原因无法保证白天的工作效率”），才成为团队的合法困难。", "evidence": ["E12"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "会去“搞定你女朋友”的团队显然不成熟，远期前途不乐观。", "evidence": ["E13"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "知道困难存在对团队是收益，只要是告知，就是一种贡献。", "evidence": ["E14"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "上报要把报告记录在案（书面或内部邮件），以确保是在向组织报告而非向上司个人报告。", "evidence": ["E15"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "为自保而擅自绕过上报机制公开乱报困难，仅此一条就会被团队打上“死人”的标记。", "evidence": ["E16"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "若一个组织规定一切报告只能向顶头上司报告，本质上你加入的是这个上司的私人团队，而非总公司。", "evidence": ["E17"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不接受适应团队解决方案与处事原则的义务，无论有无员工证和劳动合同，你都不是这团队的一员。", "evidence": ["E18","E25"]},
    {"claim_id": "C019", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "如果上司做到给出可说不可说的法则、赦免你因无知而有的误操作，那只是正确的过程，你要接受其中的情绪波动。", "evidence": ["E19"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "别人说你有错是中性的定性，有错不是有罪，绝大多数错误根本没有罪可言。", "evidence": ["E20"]},
    {"claim_id": "C021", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "罪不是指有错，而是指在可以不违约的前提下故意选择违约。", "evidence": ["E21"]},
    {"claim_id": "C022", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "了解和适应自然规律是人自己的义务，没有人教而不会，倒霉也是活该。", "evidence": ["E22"]},
    {"claim_id": "C023", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "领导出尔反尔是领导不适格，可以考虑跳槽，也可以把“能适应不适格的上司”当作额外的个人能力来追求。", "evidence": ["E23"]},
    {"claim_id": "C024", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "在明智而有前途的企业里，能让平庸领导正常履职的成员比不适格领导更核心，裁员会先裁这些中层领导。", "evidence": ["E24"]},
    {"claim_id": "C025", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "说“有困难告诉我”就意味着你必须放弃只会看到合格困难的妄想，做好看到大堆失格困难的准备。", "evidence": ["E27"]}
   ],
   "argument_steps": [
    "先由“最后期限结果不合格时列原因”的场景定义规则：早知道而未说过的困难不能事后当理由（P002）。",
    "用四种情形逐一定性：先前不知道没问题；知道没说但结果好没问题；说了但上司没解决则问题不大；知道没说又拿它当理由则不行（P003-P007）。",
    "把这句话定性为免责保命的机会，并先排除网上阴阳怪气言论的可信度（P008-P010）。",
    "补充领导说这话的两种可能，先展开第一种：被坑怕形成的口头禅（P012-P014）。",
    "以中下层领导带新人、换人快、生瓜蛋子听信“防领导”叙事为背景说明爆雷的来源（P015-P018）。",
    "反驳“压榨员工”传说：能忍受压榨者必因别无选择而无能、无效能，与公司须达社会平均生产率不相容（P019-P024）。",
    "由老板关注业务与客户付款、考虑从员工身上挤利润的时间极少，推出老板说这话不是为了整你（P025-P029）。",
    "由被瞒出的雷炸怕，解释“有困难一定要跟我说”加“一定”重音是诚意与绝望的挣扎（P030-P036）。",
    "转入第二种可能：单独对你说，因你尚未建立默契信任，需额外提醒这个试炼（P037-P042）。",
    "说明这一试炼极难：承认与不承认困难都难，憋住与全抛出都会被看破，正确的一毫米难以捉摸（P043-P054）。",
    "提出解法在于团队意识，并界定团队文化与困难观（P055-P060）。",
    "以情侣吵架为例说明私人困难须转为团队可应对的表述，并指出告知即贡献（P061-P066）。",
    "规定上报纪律：循轨、留痕、不绕过机制；区分不同性质信息的不同渠道（P067-P076）。",
    "划分团队教你与个人记住并适应的双向责任，并给出辞职或及早另寻归宿的选项（P077-P086）。",
    "纠正“你告诉了我却说你有罪”的误判，区分有错与有罪（P087-P094）。",
    "把被指错时的痛苦归因于心理反射与教育缺憾，并以自然规律论证个人无知的责任（P095-P104）。",
    "指出不适格上司的根源与其应承受的压力，收束到“自己先没把自己的话当回事”（P105-P114）。",
    "总结：没有不可说的困难，关键是学会团队困难观；把适应不适格上司列为可变现能力（P115-P120）。"
   ],
   "concept_usage": [
    {"term": "困难观", "meaning": "团队文化最核心的内容之一，指团队如何定义需要投入资源的困难、困难的责任、恰当上报途径、处理机制与合法表达。", "evidence": "P059", "ambiguity": "各团队具体内容未在本文给出，只有一般性定义。"},
    {"term": "免责、保命", "meaning": "把“有困难就说”理解为下属事后免除追责的机会。", "evidence": "P008", "ambiguity": "作者口语化表达，未给出制度含义。"},
    {"term": "试炼", "meaning": "作者用来指回应“有困难就说”这件事，称其极其困难、只有一个精确平衡点。", "evidence": "P043", "ambiguity": "未说明试炼的评判者与合格标准。"},
    {"term": "有错／有罪", "meaning": "有错是中性定性；罪指在可以不违约的前提下故意选择违约。", "evidence": "P091", "ambiguity": "作者用此区分个人道德/契约责任，未与法律意义的有罪作区分说明。"},
    {"term": "团队精神、团队意识", "meaning": "接受适应团队解决方案与处事原则这一义务的直接体现。", "evidence": "P081", "ambiguity": "未说明团队原则本身是否可能不合法或不合理。"},
    {"term": "extra mile", "meaning": "作者以此英文短语指团队超出本职的额外帮助。", "evidence": "P065", "ambiguity": "夹用英文，未作中文界定。"},
    {"term": "生瓜蛋子", "meaning": "作者对缺乏经验、心里没数的新人的称呼。", "evidence": "P016", "ambiguity": "口语贬称，无严格定义。"},
    {"term": "上报机制", "meaning": "预先规定好的困难报告渠道与留痕要求，可区别于向上司个人上报。", "evidence": "P067", "ambiguity": "具体形态取决于组织，文中只举了留痕与不同信息不同渠道的例子。"}
   ],
   "examples_and_targets": [
    "班长排长带新兵蛋子、换人极快、补充兵都是生瓜蛋子（类比，P015）。",
    "网上“压榨员工”“防领导”的传说与声音最大者（作者的反驳对象，P016-P019）。",
    "把上司想象成吃人肉才能消化的妖怪、自认唐僧转世（作者转述并嘲讽的新人想象，P017）。",
    "女朋友/男朋友吵架导致白天没精神（举例，P061-P062）；小王的女朋友闹分手（举例，P108）。",
    "举报上司贪污的官方上报渠道（举例，P073）。",
    "海盗联盟（类比，P075）；初次杀人不会因初犯免刑（类比，P076）。",
    "蝉蜕皮必须承受的痛苦（类比，P099）；摔伤者不能埋怨没人告诉自己万有引力（类比，P102）。",
    "Quit whining!（英文训诫语，P111）。"
   ],
   "conditions": [
    "“这不行”只在“你知道、你没说、你交的东西有问题、你又拿那没说的困难当理由”这一组合下成立（P007）；其余组合作者判为没问题或问题不大（P003-P006）。",
    "“能干下去的老板不靠压榨”的论证前提是员工来去自由（P020），并排除有黑恶势力可作人身威胁的地方豪强这类例外（P019）。",
    "团队承担教你困难表述与定性的责任，前提是你严格遵循正常程序（P077）。",
    "只有在对方做到给出可说不可说的法则并赦免无知之错之后，你才应接受过程中的情绪波动（P089）。",
    "若组织规定一切报告只能向顶头上司报告，则该组织被判定为上司的私人团队（P074）。",
    "只要团队组织能力正常，不接受团队义务者最终不会享有前途与决策权（P082）。",
    "说“有困难告诉我”就意味着必须准备看到大堆失格的困难（P113）。",
    "关于企业先裁中层领导的判断限定在“明智而有前途的企业”这一条件下（P120）。"
   ],
   "rhetoric_and_tone": "第二人称“你”的对话式训诫贯穿全文，兼有调侃与嘲讽（生瓜蛋子、小祖宗、唐僧转世、炸麻了）。多处反问加强语气（“你有腿会走好吗”“为什么ta还在这一层苦熬呢”）；夹用英文（extra mile、Quit whining！）；用分点1）2）3）4）与“总结——”组织后半篇；前半用a）b）并列两种可能。语气强硬、直白，同时以“免责保命”“及早另寻归宿”等形式给读者保护性建议。",
   "unresolved_questions": [
    "P041 明说“什么叫‘恰当的方式’，我们回头再说”，本文未给出“恰当方式”的具体内容，是否另有续文未在本篇说明。",
    "关于老板不靠压榨员工的一般性断言（P019、P024）无数据或来源，属作者经验判断，待外部核查。",
    "“适格的领导极为稀缺，企业对能适应不适格的领导的成员的需求是无限的”（P119）为无限定量化修辞，缺依据。",
    "“不要听阴阳怪气的话”未指明所指对象与判断标准（P009-P010）。",
    "正文以“ta”指代领导、老板、上司，未说明性别与具体身份，主体为一般化角色。",
    "语料 updated_at（2025-06-11）晚于 published_at（2021-07-23），provenance 与 superseded 均为 null，无版本差异说明，无法确认正文是否为后续编辑版本。",
    "阅读包结构统计为 124 个 paragraph 节点，正文分段输出 P001–P120；差额疑为空段落未进入 text 分段，未见正文缺失迹象，但未能完全排除段落被合并或丢弃。",
    "brief 与正文开头一致，未提供正文之外的独立信息。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P002", "quote": "这ABCDEFG里面不该有任何一条是你之前就知道而ta却没听你说过的。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P008", "quote": "这是给你免责、保命的机会，不懂得用怪不了别人。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P010", "quote": "事实上，只要是阴阳怪气说的话，不管说的是什么，都不要听。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P014", "quote": "ta被坑怕了，所以养成了这种口头禅的习惯，对谁都会下意识的说一说。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P037", "quote": "这话不是一种习惯，一般不说，是专门说给你听的。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P024", "quote": "“公司有能生存的生产效率”和“公司的员工都是走投无路不能不接受压榨的垫底劳动力”，这两者是逻辑不相容的。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P029", "quote": "说直接点，老板眼里根本没有你。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P042", "quote": "单独说给你听，就是因为你还没有像老员工一样与团队领袖建立起默契和信任，所以需要额外的提醒你存在这个试炼。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P043", "quote": "不错，这是一个试炼——极其困难的试炼。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P059", "quote": "这是指一个团队如何定义一个需要投入资源的困难、如何定义困难的责任、如何定义困难的恰当上报途径、如何定义困难的恰当处理机制、如何定义困难的合法表达。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P060", "quote": "任何困难都是可以提的，问题不在于困难本身可不可以提，而在于你以什么姿态、什么立场、什么方式去提。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P062", "quote": "你的困难不是“我女朋友跟我吵架”，而是“我出于个人原因，没有办法保证白天完全的工作效率”。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P064", "quote": "会这么干的团队显然不成熟，远期前途不乐观。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P066", "quote": "因而，只要是告知，就是一种贡献。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P068", "quote": "你最好是将你的报告记录在案，例如通过书面方式，或者内部的邮件系统。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P070", "quote": "你直接绕过这个机制，为了自保而不顾及对团队的负面影响，只这一条，你就被打上了死人的标记。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P074", "quote": "意味着你根本没有加入这个总公司，本质上你加入的是这个上司的私人团队。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P082", "quote": "不接受这种义务，无论你是不是有员工证、劳动合同，你都不是这团队的一员", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P089", "quote": "如果ta做到了这两条，对你界定何谓可说、何谓不可说，也赦免了你因为无知而有的误操作，那么这只是正确的过程，你要接受这之中的情绪波动。", "relation": "qualifies"},
    {"key": "E20", "paragraph_id": "P091", "quote": "有错不是有罪，绝大多数错误都根本没有罪可言。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P093", "quote": "罪不是指“有错”，而是指故意选择违约，是指你在可以不违约的前提下，有意的选择违约。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P101", "quote": "了解和适应自然规律是人自己的义务，就是没有任何人教，你不会，你倒霉也是活该。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P117", "quote": "领导出尔反尔，那是领导不适格，你可以考虑跳槽", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P120", "quote": "这种“能让平庸的领导也能正常履职的团队成员”是比这不适格的领导更核心的资产", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P080", "quote": "团队没有义务按照你自己希望的解决方式去应对困难", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P041", "quote": "什么叫“恰当的方式”，我们回头再说。", "relation": "context"},
    {"key": "E27", "paragraph_id": "P113", "quote": "“有困难告诉我”这句话一说，就意味着你必须同时放弃只会看到“合格的困难”的妄想", "relation": "qualifies"},
    {"key": "E28", "paragraph_id": "P020", "quote": "如果一个员工在来去自由的前提下会没有选择到连这种压榨都不能不忍受，那一定是因为ta除了这个工作根本找不到别的工作", "relation": "qualifies"},
    {"key": "E29", "paragraph_id": "P019", "quote": "除了有黑恶势力可以直接做人身威胁的地方豪强这一类之外，根本没有几个老板能靠“压榨员工”来行走江湖的。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["职场关系", "组织伦理", "管理学（工作性标签）"],
   "issue_candidates": ["上下级沟通", "困难上报机制", "新人的团队社会化", "有错与有罪的区分", "职场流言的辨识"],
   "text_function_candidates": ["答疑", "经验总结", "训诫", "论辩（反驳“压榨员工”叙事）"],
   "object_candidates": ["提问者（知乎）", "领导/老板/上司（泛称）", "职场新人", "团队/组织"],
   "working_keywords": ["有困难就说", "困难观", "上报机制", "免责", "试炼", "有错", "有罪", "团队意识"]
  },
  "notes": "平台为知乎；正文未见平台话题标签混入。无图片节点。正文完整覆盖 P001–P120；阅读包结构统计为 124 个 paragraph 节点而分段输出为 120 段，差额疑为空段落未进入 text 分段，已记入未决问题。语料 updated_at 晚于 published_at 且无 provenance/superseded 说明。"
 },
 "9b6db870": {
  "analysis": {
   "question_context": "知乎提问者问“怎么才能达到不羡慕别人的境界?”（Q001，立场属提问者）。作者的回答只有一句断言，未展开论证，也未给出达到该境界的方法或路径。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "以单句给出结论：怜悯者从不羡慕。", "role": "claim"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "怜悯者从不羡慕（处于怜悯状态的人不会羡慕别人）。", "evidence": ["E1"]}
   ],
   "argument_steps": [
    "全文仅一句断言，未给出定义、前提、理由、例证、让步或结论推进，也未说明如何达到不羡慕别人的境界。"
   ],
   "concept_usage": [
    {"term": "怜悯者", "meaning": "本文把不羡慕的主体指认为怜悯者，即处于怜悯状态的人。", "evidence": "P001", "ambiguity": "未界定怜悯的对象、来源与判定标准。"},
    {"term": "羡慕", "meaning": "本文中被否定的状态，只出现在“怜悯者从不羡慕”这一否定句中。", "evidence": "P001", "ambiguity": "未界定羡慕的对象与层次，也未区分对物、对人、对地位等不同情形。"}
   ],
   "examples_and_targets": [
    "本文未使用例子、人物、事件、机构或数据。"
   ],
   "conditions": [
    "本文未说明任何条件；句子以“从不”作全称否定，未附适用对象、场景或例外。"
   ],
   "rhetoric_and_tone": "单句格言式断言，无称呼、无论证、无例子；“从不”为全称否定，语气斩钉截铁。",
   "unresolved_questions": [
    "正文仅 8 个字符，未说明“怜悯”的含义、怜悯者为何不羡慕，也未回答提问所问的“怎么才能达到”这一路径问题。",
    "无法判断是否属于未写完或只保留结论的回答：provenance 与 superseded 均为 null，brief 与正文完全相同，不含额外信息。",
    "“从不”为全称判断，未给出反例、限定条件或适用范围。",
    "语料 updated_at（2022-01-30）晚于 published_at（2021-07-23），无版本差异说明，未能确认是否有修订。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "怜悯者从不羡慕。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["心理（工作性标签）", "伦理（工作性标签）"],
   "issue_candidates": ["羡慕情绪的克服", "怜悯与羡慕的关系"],
   "text_function_candidates": ["答疑（极简回答）", "格言式断言"],
   "object_candidates": [],
   "working_keywords": ["怜悯", "羡慕", "怜悯者从不羡慕"]
  },
  "notes": "正文极短（8 字符），brief 与正文完全相同，无图片节点；本记录只覆盖现有文本，未据标题或提问补写未出现的内容。"
 },
 "6dfcec2b": {
  "analysis": {
   "question_context": "知乎提问者问“东京奥运会将 8 万吨电子废品提炼的金属制成奖牌，如何评价这一尝试？”（Q001，属提问者，提问者本身未表态）。作者先评价该尝试的创意，再对其实现方式提出保留估计，随后把话题扩展到奥运会的非体育意义。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001","P002","P003"], "summary": "评价该尝试：创意很好；但作者估计只是购买回收企业的最终产品并按生产效率反推数据公布，恐怕谈不上“专项回收，专门提炼”；宣传意义还是可以的。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P004","P005","P006","P007"], "summary": "扩展到一般判断：每届奥运奖牌作为设计焦点都有意义且有启发性；奥运会更是设计美学、建筑艺术、直播媒体技术、运动科技的盛会；这些“周边”才是影响更实质的部分。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "用电子废品提炼金属制奖牌是个很好的创意。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者估计该做法只是购买一家回收企业的最终产品，再请对方按生产效率反推并公布数据，恐怕谈不上“专项回收，专门提炼”。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "该尝试的宣传意义还是可以的。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "每一届奥运奖牌作为设计焦点都很自然地有某种意义，在设计上都很有启发性。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "每一届奥运会不单是运动盛会，在更深刻的意义上更是一次设计美学、建筑艺术、直播媒体技术、运动科技的盛会。", "evidence": ["E5"]},
    {"claim_id": "C006", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "后者对人类的总体意义可能还超过体育比赛本身带来的胜负荣辱。", "evidence": ["E6"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这些看似“周边”的东西其实才是奥运会影响更实质的部分，因为它们是“硬”的、全球同步触达的、正面单向进展的、有划时代启示意义的，往往更长久存在。", "evidence": ["E7"]}
   ],
   "argument_steps": [
    "先肯定提问所指的尝试为很好的创意（P001）。",
    "对该尝试的实现方式提出保留估计：可能只是采购回收企业成品并反推数据，谈不上专项回收专门提炼（P002）。",
    "让步承认其宣传意义还是可以的（P003）。",
    "转入一般判断：每届奥运奖牌作为设计焦点自然有意义且有启发性（P004）。",
    "提升论点：奥运会更是设计美学、建筑艺术、直播媒体技术、运动科技的盛会（P005）。",
    "以“甚至”“可能”提出后者对人类的总体意义可能超过体育比赛本身的胜负荣辱（P006）。",
    "收束到结论：这些“周边”才是奥运会影响更实质的部分，并给出“硬”、全球同步触达、正面单向进展、更长久等理由（P007）。"
   ],
   "concept_usage": [
    {"term": "“专项回收，专门提炼”", "meaning": "作者转述并质疑的说法，指专为奖牌从电子废品中回收、提炼金属的做法。", "evidence": "P002", "ambiguity": "作者称“恐怕谈不上”，属估计而非核实结论。"},
    {"term": "“周边”", "meaning": "作者用来指设计美学、建筑艺术、直播媒体技术、运动科技等非竞技内容，并称其反而更实质。", "evidence": "P007", "ambiguity": "引号表示这是他人眼中的“周边”，作者未给出界定标准。"},
    {"term": "“硬”", "meaning": "作者形容上述非体育部分的性质，与全球同步触达、正面单向进展、更长久存在并列。", "evidence": "P007", "ambiguity": "未逐项定义“硬”具体指什么。"},
    {"term": "非体育意义", "meaning": "仅见于标题；正文以“更深刻的意义”“周边”等表述展开，未作为术语定义。", "evidence": "P005", "ambiguity": "标题用语与正文用语不完全一致。"},
    {"term": "设计焦点", "meaning": "指每届奥运奖牌作为设计关注点，作者称其自然地带有某种意义。", "evidence": "P004", "ambiguity": "未说明具体意义如何产生。"}
   ],
   "examples_and_targets": [
    "东京奥运会用 8 万吨电子废品提炼金属制奖牌（被评价的尝试，P001-P003；该数字由提问者给出，正文未引用）。",
    "回收企业及其生产效率、反推数据并公布（作者的估计，P002）。",
    "历届奥运奖牌设计（例证，P004）。",
    "设计美学、建筑艺术、直播媒体技术、运动科技（非体育意义的具体列举，P005）。"
   ],
   "conditions": [
    "对奖牌金属来源的判断带“我估计”“恐怕谈不上”的限定，非确证事实（P002）。",
    "“后者对人类的总体意义可能还超过……”用“甚至”“可能”弱化（P006）。",
    "“往往更长久存在”以“往往”限定，非全称判断（P007）。",
    "标题限定论述范围为“奥运会的非体育意义”，正文未讨论该届奖牌回收的实际环境效益。"
   ],
   "rhetoric_and_tone": "先扬后抑再转：以“这是个很好的创意呀”肯定，以“不过我估计”“恐怕谈不上”加保留，以“当然宣传意义还是可以的”部分认可；随后用“其实”“更深刻地说”转入一般性议论。语气为评价式、审美鉴赏式，无讽刺与训诫。",
   "unresolved_questions": [
    "作者关于奖牌金属系购买回收企业成品并反推数据的判断属“我估计”，未给出信息来源，待外部核查东京奥组委的实际回收与采购流程。",
    "“8 万吨电子废品”为提问者转述的数字，正文未引用或核实。",
    "标题为“奥运会的非体育意义”，但正文对非体育意义只作列举性断言，未给论证与具体案例。",
    "“每一届奥运会……”“往往更长久存在”等为概括判断，未指明具体届次、技术或数据。",
    "brief 为正文的截断前缀，未提供正文之外的独立信息。",
    "语料 updated_at（2025-12-22）远晚于 published_at（2021-07-25），provenance 与 superseded 为 null，无法确认是否有后续修订。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "这是个很好的创意呀。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "不过我估计这只是购买了一家回收企业的最终产品，然后请ta们根据自己的生产效率反推一下数据、公布一下而已。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "当然宣传意义还是可以的。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "其实每一届的奥运奖牌作为一个设计焦点都很自然地有某种意义，在设计上都很有启发性。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "每一届奥运会不单是运动盛会，实际上在更深刻的意义上更是一次设计美学、建筑艺术、直播媒体技术、运动科技的盛会。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "甚至后者对人类的总体意义可能还超过体育比赛本身带来的胜负荣辱。", "relation": "qualifies"},
    {"key": "E7", "paragraph_id": "P007", "quote": "这些看似“周边”的东西，其实反而才是奥运会影响更实质的部分", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["体育（工作性标签）", "设计／美学（工作性标签）", "媒介技术（工作性标签）"],
   "issue_candidates": ["奥运奖牌的材料来源", "奥运会的非体育影响", "设计美学与技术展示的意义"],
   "text_function_candidates": ["答疑", "评价", "评论"],
   "object_candidates": ["东京奥运会", "回收企业（泛称）"],
   "working_keywords": ["奥运奖牌", "电子废品", "专项回收，专门提炼", "设计美学", "直播媒体技术", "运动科技", "周边"]
  },
  "notes": "平台为知乎；正文未见平台话题标签混入；无图片节点。brief 为正文前缀（截断处与 P002、P004 边界吻合），未提供额外信息。正文完整覆盖 P001–P007。"
 },
 "a4a9a8da": {
  "analysis": {
   "question_context": "知乎提问者引述德媒“郑州洪水，没有任何排水系统能应对”的说法，问这反映了哪些问题（Q001，引述内容与提问立场均属提问者）。作者没有直接评价德媒说法或郑州排水系统，而是把这次洪水放入“气候异常时代”的框架，先提出气候异常是最严峻的挑战，再列出基础设施、救灾机制、全球化、国际秩序四类挑战。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001","P002","P003","P004","P005"], "summary": "总起：气候异常是人类即将面对的最严峻挑战；新冠很可能是生态圈灾难性转变的开始；列举一系列异常事件为警讯，河南极端气候是又一例；引出几个基本挑战。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P006","P007","P008","P009","P010","P011","P012","P013","P014","P015","P016","P017","P018"], "summary": "挑战一（基础设施）：过去水利设施以“保证灾害不发生”为目标并仰赖气候稳定和稳定的灾害“前线”；未来极端气候可能不再遵从该逻辑，灾害可能出现在无法预想、不可能普遍设防处；提高全国建筑防灾等级会改变城市规划原则，需要从单纯抵御转向就地限制与缓冲、增强容灾率；基建能力是考试资格，其要害在土地所有制，土地私有制国家将面临严峻挑战。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P019","P020","P021","P022","P023","P024","P025","P026","P027"], "summary": "挑战二（救灾应急机制）：各国都需按新标准重新思考；突破规划的灾害一旦发生，快速反应与大规模物资人力援助是硬指标；强调沙袋、专业人员、车辆、直升机、帐篷等物理性要素，钱不能替代；这些准备与常态维护是治理能力的硬挑战，对基于个人主义的选票民主制不利，政要会赌任内不出事而侥幸概率越来越小。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P028","P029","P030","P031","P032","P033","P034","P035","P036","P037","P038","P039","P040"], "summary": "挑战三（全球化）：产业链局部因灾停摆属不可抗力且难预测；过去只需考虑政治稳定性、军事与经济影响力，现在物理灾害可直接中断生产；各国须考虑产业链分散化与布局优化，包括中国自身；分散化要求异地备灾，但不必然导致工厂回迁，反而可能促成生产管理企业的全球扩张；再布局会偏向基建更强、恢复更快的“更安全的国家”。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P041","P042","P043","P044","P045","P046","P047","P048","P049","P050"], "summary": "挑战四（国际秩序）：需要建立国际性灾害援助的长效机制；富裕国家尚可一搏，未完成现代化的第三世界国家没有外部帮助近乎不可能完成；以美国唯一有实力主导战后经济重建解释其战后秩序地位，并称苏联贡献比例逊色是其落败根本原因；未来主题是难民与灾民问题，唯一办法是帮助非洲拉美建立现代化国家，而如何不干预内政而做到，是未来全球领袖的面试考题。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "气候异常是人类即将要面对的最严峻的挑战。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "新冠很大概率是生态圈开始走向灾难性转变的开始。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "德州大雪、澳洲大火、北极圈异常高温、欧洲酷暑、美国山火、西伯利亚冻土融解、北极圈消退、海平面上升，以及河南的极端气候，都是气候异常的警讯或例证。", "evidence": ["E3","E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "未来全球所有国家的基础设施都要面临难以想象的新挑战。", "evidence": ["E5"]},
    {"claim_id": "C005", "claim_type": "author_reported", "attribution": "cited_source", "modality": "asserted", "statement": "作者称与台湾李鸿源看法一致：以前的水利设施主要考虑保证灾害不发生，这完全仰赖气候稳定，从而有稳定的灾害“前线”可言。", "evidence": ["E6"]},
    {"claim_id": "C006", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "未来的极端气候可能不再遵从旧有逻辑：水灾、风灾、火灾、雪灾都未必发生在传统地带，可能出现在任何无法预想且不可能普遍设防的地方。", "evidence": ["E7","E8","E9"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "提高全国建筑防灾等级会深刻改变城市规划原则，新的设计思想不但要抵御灾害，还要让无从抵御的灾难能就地被限制和缓冲，即同时增强防灾力、抗灾力和容灾率。", "evidence": ["E10","E11","E12"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "任何基础建设新要求都以一份强大的基建能力为最基本的考试资格。", "evidence": ["E13"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "基建能力的要害不在工程机械和劳动力，而在土地所有制；土地私有制国家在全球天气异常的新常态下面临严峻挑战，包括传统发达国家。", "evidence": ["E14","E15"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "所有国家都需要对救灾应急机制做新标准下的重新思考。", "evidence": ["E16"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "突破一切规划标准的灾害一旦发生，救灾需求即成定局，快速反应与大规模物资、人力援助是必须做到的硬指标；这种灾害可能发生在任何国家。", "evidence": ["E17","E18"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "钱不能替代沙袋、救灾专业人员、卡车、直升机、帐篷等可以直接与自然对话的物理性要素；这些要素的准备和常态维护是各国政府必须面对的治理能力硬挑战。", "evidence": ["E19","E20"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这类挑战不是来自意识形态对手的挑衅，而是直接来自“上帝的要求”，没有人可以免试过关或拒不参考。", "evidence": ["E21"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这种挑战对基于个人主义的选票民主制客观上非常不利，“救灾不力”与“破坏民主传统”将是各国政要未来面对的两大逻辑难题。", "evidence": ["E22"]},
    {"claim_id": "C015", "claim_type": "author_qualified", "attribution": "author", "modality": "predicted", "statement": "所有人都会宁可赌“在我任内不会出事”，也不愿在没事的前提下挑战民主传统；而ta们没有预想的幸运的概率会越来越大。", "evidence": ["E23","E24"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "全球化要面对气候新常态的新挑战：全球产业链随时可能因某个局部的重大灾害完全停摆，这属经典的不可抗力问题，损失不可弥补且似乎无法预测。", "evidence": ["E25","E26"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "以前全球化只需考虑政治稳定性、军事强大与经济影响力，风险可以管理；现在物理灾害会直接中断生产与交通。", "evidence": ["E27","E28"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这意味着所有国家都必然要考虑产业链的分散化和布局优化，甚至包括中国自身。", "evidence": ["E29","E30"]},
    {"claim_id": "C019", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "分散化要求同一零组件有异地备灾来源；但这不见得导致“工厂回迁”，反而可能导致生产管理企业的全球扩张（如促使宁德时代全球设厂），且后一种样式很有可能占优。", "evidence": ["E31","E32","E33","E34"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "再布局会把主要赌注放在“更安全的国家”，即最不易出事、出事后最快恢复生产，也就是基建更强、社会救助机制更敏捷有效的国家。", "evidence": ["E35","E36"]},
    {"claim_id": "C021", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "国际秩序本身面临新挑战，指国际性灾害援助长效机制的建立。", "evidence": ["E37","E38"]},
    {"claim_id": "C022", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "这些挑战对富裕国家尚可一搏，且有很大概率能凭内在理性积淀完成必要的转变；但对尚未完成基本现代化的第三世界国家和另外五十亿人，没有外部帮助近乎不可能完成。", "evidence": ["E39","E40"]},
    {"claim_id": "C023", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "美国能主宰战后国际秩序的根本原因是它是唯一拥有足够经济实力领导完成战后经济重建的国家，苏联贡献比例大为逊色，这甚至是苏联最终落败的根本原因。", "evidence": ["E41"]},
    {"claim_id": "C024", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "未来一大全球主题会是越来越严重的难民与灾民问题，非洲拉美作为“天然的难民工厂”会成为越来越大的现实问题，届时欧洲和美国的意识形态故事都会讲不下去。", "evidence": ["E42","E43"]},
    {"claim_id": "C025", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "阻止非洲人拉美人涌入的唯一办法是真正帮助非洲和拉美建立现代化国家，既提供硬件生产力也提供文化启示与理论参考；如何在不直接干预内政而陷入泥潭的前提下做到，是未来全球领袖的面试考题，谁能解决，被困扰的国家就只能团结在谁周围。", "evidence": ["E44","E45","E46"]}
   ],
   "argument_steps": [
    "先立总论断：气候异常是最严峻挑战，新冠很可能是生态圈灾难性转变的开始（P001-P002）。",
    "列举全球异常事件作为警讯，并把河南极端气候列为又一例子（P003-P004）。",
    "以“几个基本挑战”分四点组织全文（P005）。",
    "挑战一：由李鸿源式判断说明过去防灾仰赖气候稳定与固定“前线”，故可用十年一遇、百年一遇等标准投入巨型工程（P006-P008）。",
    "转折：未来极端气候可能不再遵从该逻辑，灾害可能出现在任何无法预想、不可能普遍设防处（P009-P011）。",
    "推出规划层面的后果：提高防灾等级会改变城市规划原则与城市群规划，需要新增就地的限制与缓冲能力，即容灾率（P012-P014）。",
    "再推出基建能力是考试资格，并把要害落在土地所有制，进而判断土地私有制国家将遇严峻挑战（P015-P018）。",
    "挑战二：各国须重新思考救灾机制；用“钱不能替代物理要素”反驳以资金为救灾核心的思路，落点为治理能力的硬挑战（P019-P023）。",
    "以“上帝的要求”强调不可豁免，并指出选票民主制下“救灾不力”与“破坏民主传统”的两难及政客赌任内的倾向（P024-P027）。",
    "挑战三：产业链局部停摆属不可抗力，说明旧全球化的风险管理方式失灵（P028-P031）。",
    "由此推出产业链分散化与布局优化，并用“不见得回迁、反而促全球扩张”修正直觉预期（P032-P036）。",
    "再推出“更安全的国家”标准：基建强、救助快的国家更受青睐（P037-P040）。",
    "挑战四：国际秩序需要灾害援助长效机制；以美苏战后重建贡献对比解释美国地位（P041-P045）。",
    "以难民灾民问题收束：唯一办法是帮助非洲拉美现代化，难点在于不干预内政，最终以“谁能解决谁获团结”作结（P046-P050）。"
   ],
   "concept_usage": [
    {"term": "容灾率", "meaning": "与防灾力、抗灾力并列的新要求，指让无从抵御的灾难就地被限制和缓冲的能力。", "evidence": "P014", "ambiguity": "未给出度量方式或具体工程含义。"},
    {"term": "“前线”", "meaning": "指过去因气候稳定而形成的灾害典型多发地带（地震多发带、自然河道、季节性台风多发地）。", "evidence": "P007", "ambiguity": "作者以引号表示比喻用法，未作严格定义。"},
    {"term": "土地所有制", "meaning": "被作者指为基建能力要害的制度条件，并据此判断土地私有制国家将遇严峻挑战。", "evidence": "P016", "ambiguity": "未说明具体机制、案例或例外。"},
    {"term": "“更安全的国家”", "meaning": "最不易出事、出事后能最快控制与恢复生产的国家，即基建更强、社会救助机制更敏捷有效的国家。", "evidence": "P037", "ambiguity": "标准为作者自定，未给量化指标。"},
    {"term": "“上帝的要求”", "meaning": "作者的修辞，指这类挑战不由任何意识形态对手发起、无人可以豁免。", "evidence": "P024", "ambiguity": "宗教化修辞，非字面神学主张。"},
    {"term": "“天然的难民工厂”", "meaning": "作者对非洲、拉美的整体化称呼，指其在新气候常态下持续产生难民与灾民。", "evidence": "P046", "ambiguity": "整体化概括，未区分国家差异。"},
    {"term": "面试考题", "meaning": "比喻，指未来全球领袖必须回答的问题（如何不干预内政而帮助他国现代化）。", "evidence": "P049", "ambiguity": "比喻性表述，未说明评判者。"},
    {"term": "意识形态故事", "meaning": "指欧洲、美国用于自我说明的对外叙事，作者预测其在难民灾民问题上讲不下去。", "evidence": "P047", "ambiguity": "未具体指明是哪些叙事内容。"}
   ],
   "examples_and_targets": [
    "郑州／河南洪水（提问者引德媒说法；作者称其为极端异常气候的又一例，P004、P020，未评述德媒说法本身）。",
    "德州大雪、澳洲大火、北极圈异常高温、欧洲酷暑、美国大型山火、西伯利亚冻土融解软化、北极圈消退、太平洋岛国海平面上升（作者列举的警讯，P003）。",
    "台湾李鸿源（作者称与其看法一致的引用对象，P007；未给出原文出处）。",
    "地震多发带、自然河道、季节性台风典型多发地（过去灾害“前线”的例子，P007）。",
    "十年一遇、百年一遇乃至千年一遇（既往设防标准的表达，P008）。",
    "沙袋、救灾专业人员、卡车、直升机、帐篷（物理性要素的举例，P022）。",
    "“在我任内不会出事”与“挑战民主传统”（政要两难的表述，P026）。",
    "电动车企业与电池企业、德国／越南／日本、宁德时代全球设厂（产业链分散化的举例，P034-P035）。",
    "美国与苏联在战后经济重建中的贡献对比（历史因果断言，P045，未给史料来源）。",
    "非洲、拉美（“天然的难民工厂”，P046、P048）；马来西亚、印度、日本、法国（灾害可能发生地，P020）。",
    "赵日天（“任你赵日天如何不服都没用”，P031，网络梗式调侃）。"
   ],
   "conditions": [
    "“如果我们将全国的建筑的防灾等级提高一个等级”为条件句，作者据此推出城市规划原则会改变（P012）。",
    "灾害分布以“未必”“可能”表述：水灾未必在传统河道、风灾未必在沿海等，可能出现在无法预想、不可能普遍设防的地方（P010-P011）。",
    "政客侥幸的判断以概率表达：“没有预想的幸运的概率会越来越大”（P027）。",
    "产业链判断带限定：“并不见得会导致所谓的‘工厂回迁’”“很有可能后一种样式反而会占优”（P034、P036）。",
    "对第三世界的判断限定在“没有外部帮助”的条件下（P044）；富裕国家的判断为“还算尚可一搏”并“有很大的概率”（P043）。",
    "帮助非洲拉美的方案以“不直接干预内政而陷入泥潭”为前提（P049）。",
    "“非洲拉美作为天然的难民工厂”为整体化概括，未区分国家（P046）。",
    "全文以“我和台湾的李鸿源看法一致”作为引述前提（P007）。"
   ],
   "rhetoric_and_tone": "论断式长文，以1）2）3）4）分列四类挑战，多用“必然”“完全”“唯一”“没有人可以”等强断言，同时用“可能”“很大概率”“不见得”“很有可能”保留概率判断。夹用口语与比喻（“这是一场新考试。你如果没带笔，你考都没法考”“任你赵日天如何不服都没用”“面试考题”）以及宗教修辞（“直接来自上帝的要求”）。批评对象是“基于个人主义的选票民主制”与发达国家政要的一般化行为，未点名具体人物。",
   "unresolved_questions": [
    "提问所引德媒“郑州洪水，没有任何排水系统能应对”的说法未被作者直接评价或核实，正文未讨论郑州排水系统与德媒报道，回答与提问之间是话题转移关系。",
    "作者称与台湾李鸿源看法一致，但未给出李鸿源的原话、文章或出处，待外部核查。",
    "“新冠很大概率是生态圈开始走向灾难性转变的开始”为无来源的概率断言（P002）。",
    "“土地私有制国家……会面临严峻挑战”未给案例与机制说明（P017）。",
    "“美国是唯一拥有足够的经济实力领导完成战后经济重建的国家”“这甚至是苏联最终落败的根本原因”属历史因果断言，未给史料依据，待外部核查（P045）。",
    "“非洲拉美作为天然的难民工厂”为整体化概括，未区分国家差异（P046）。",
    "正文称产业链分散化“甚至包括中国自身”（P033），但未展开中国的具体情况。",
    "阅读包结构统计为 52 个 paragraph 节点，正文分段输出 P001–P050，差额疑为空段落未进入 text 分段。",
    "语料 updated_at（2024-11-29）晚于 published_at（2021-07-25），provenance 与 superseded 为 null，无法确认是否有后续修订。",
    "brief 为正文前缀的截断（对应 P001–P003），未提供正文之外的独立信息。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "气候异常是人类即将要面对的最严峻的挑战。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "新冠很大概率是生态圈开始走向灾难性转变的开始。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "加上西伯利亚的冻土融解软化、北极圈的消退、太平洋岛国面对的海平面的上升，都是非常明确的警讯。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "河南这次的极端异常气候现象则是另一个例子。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P006", "quote": "未来全球所有国家的基础设施都要面临难以想象的新挑战。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P007", "quote": "这一点我和台湾的李鸿源看法一致——我们以前的水利设施主要是在考虑保证灾害不发生，这完全仰赖于气候稳定", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P009", "quote": "但未来的极端气候可能不再遵从这个逻辑。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P010", "quote": "水灾未必发生在传统的危险河道，风灾未必在沿海，火灾未必在低纬度地区，雪灾未必在高纬度地区。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P011", "quote": "它们可能出现在任何你无法预想，而且不可能普遍设防的地方。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P012", "quote": "如果我们将全国的建筑的防灾等级提高一个等级，仅此一条就足以深刻的改变城市规划的基本原则", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P013", "quote": "不但要考虑将灾害直接抵御住，还要考虑那些无从抵御的灾难必须能就地被限制和缓冲。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P014", "quote": "也就是不但要加强防灾力、抗灾力，还要增强容灾率。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P015", "quote": "不管是什么样的基础建设的新要求，都必然要求一份强大的基建能力来作为最基本的考试资格。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P016", "quote": "而这份基建能力的要害，不在于工程机械和劳动力，而在于土地所有制。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P017", "quote": "土地私有制国家在全球天气异常的新常态下会面临严峻挑战，这甚至包含了传统的发达国家。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P019", "quote": "所有的国家都需要对救灾应急机制做新标准下的重新思考。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P020", "quote": "河南水灾今天发生在中国，明天完全可能发生在马来西亚、印度或者日本、法国。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P021", "quote": "快速反应和大规模物资、人力的援助是一个必须做到的硬指标。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P022", "quote": "钱不能替代沙袋、不能替代救灾专业人员、不能替代卡车和直升机、不能替代帐篷。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P023", "quote": "这些物理性的要素的准备和常态维护，会是世界各国政府都必须面对的治理能力上的硬挑战。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P024", "quote": "这不是来自什么意识形态对手的挑衅，而是直接来自上帝的要求。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P025", "quote": "这种挑战对基于个人主义的选票民主制客观上会非常的不利。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P026", "quote": "所有人都会宁可赌“在我任内不会出事”，也不愿意在没有事的前提下“挑战民主传统”。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P027", "quote": "而ta们没有预想的幸运的概率会越来越大。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P028", "quote": "全球化要面对气候新常态的新挑战。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P029", "quote": "全球产业链随时会有某个局部因为重大灾害而完全停摆。这威胁既现实、又绝对，属于经典的不可抗力问题", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P030", "quote": "以前全球化几乎只需要考虑政治稳定性、只要靠军事强大、经济影响力深，这种风险是可以管理的。", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P031", "quote": "现在是人家的屋顶直接吹不见了、城市断电失联了、工厂道路整个被洪水阻断了。", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P032", "quote": "这意味着所有所有国家都必然要考虑产业链的分散化和布局优化。", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P033", "quote": "这甚至包括中国自身。", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P034", "quote": "同一种零组件，我必须要有异地备灾策略，需要两个不同地区——最好是不同纬度、不同水系、不同地质板块、不同交通圈的供应来源。", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P034", "quote": "这并不见得会导致所谓的“工厂回迁”，而是会导致生产管理企业的全球扩张。", "relation": "qualifies"},
    {"key": "E33", "paragraph_id": "P035", "quote": "也会在另一方面促使宁德时代全球设厂。", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P036", "quote": "所以很有可能后一种样式反而会占优。", "relation": "qualifies"},
    {"key": "E35", "paragraph_id": "P037", "quote": "而再布局则受到另一种要素的影响——我要把我的主要赌注放在“更安全的国家”。", "relation": "supports"},
    {"key": "E36", "paragraph_id": "P039", "quote": "也就是基建能力更强、基建更完善、社会救助机制更敏捷和有效的国家。", "relation": "supports"},
    {"key": "E37", "paragraph_id": "P041", "quote": "4）国际秩序本身面临新挑战。", "relation": "supports"},
    {"key": "E38", "paragraph_id": "P042", "quote": "这是指国际性灾害援助的长效机制的建立。", "relation": "supports"},
    {"key": "E39", "paragraph_id": "P043", "quote": "刚才谈到的这些挑战，对于富裕国家而言固然是困难，但还算尚可一搏的困难。", "relation": "qualifies"},
    {"key": "E40", "paragraph_id": "P044", "quote": "但是对于目前尚未完成基本现代化的第三世界国家、对这个的地球上的另外五十亿人，这可能是一个没有外部帮助近乎不可能完成的任务。", "relation": "qualifies"},
    {"key": "E41", "paragraph_id": "P045", "quote": "根本的原因是美国是唯一拥有足够的经济实力领导完成战后经济重建的国家。", "relation": "supports"},
    {"key": "E42", "paragraph_id": "P046", "quote": "未来的一大全球主题，会是越来越严重的难民问题和灾民问题。", "relation": "supports"},
    {"key": "E43", "paragraph_id": "P047", "quote": "到时候无论是欧洲还是美国的意识形态故事都会面临讲不下去的问题。", "relation": "supports"},
    {"key": "E44", "paragraph_id": "P048", "quote": "唯一的办法就是真正地帮助非洲和拉美建立起自己的现代化国家", "relation": "supports"},
    {"key": "E45", "paragraph_id": "P049", "quote": "如何在不直接干预内政而陷入泥潭的前提下做到这一点，是未来的全球领袖的面试考题。", "relation": "supports"},
    {"key": "E46", "paragraph_id": "P050", "quote": "谁能解决这个问题，被这问题所困扰的国家就只能团结在谁周围，别无选择。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["气候／环境（工作性标签）", "基础设施与城市规划（工作性标签）", "国际政治经济（工作性标签）", "应急管理（工作性标签）"],
   "issue_candidates": ["气候异常的警讯", "基础设施防灾标准与容灾", "土地所有制与基建能力", "救灾应急机制与国家治理能力", "选票民主制下的救灾困境", "产业链分散化与全球布局", "国际灾害援助长效机制", "难民与灾民问题"],
   "text_function_candidates": ["答疑", "评论", "预测性论断", "宏观形势分析"],
   "object_candidates": ["中国（含河南、郑州）", "台湾李鸿源", "美国", "苏联", "欧洲", "非洲", "拉美", "马来西亚、印度、日本、法国", "宁德时代"],
   "working_keywords": ["气候异常", "极端气候", "容灾率", "土地所有制", "救灾应急机制", "选票民主制", "产业链分散化", "工厂回迁", "更安全的国家", "国际性灾害援助"]
  },
  "notes": "平台为知乎；提问者引述德媒说法，属提问者的材料，作者未直接回应德媒报道，而是转入气候异常时代的四类挑战（已记入未决问题）。无图片节点。正文完整覆盖 P001–P050；结构统计 52 个 paragraph 节点与分段输出的差额疑为空段落。语料 updated_at 晚于 published_at，且无 provenance/superseded 说明。"
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
