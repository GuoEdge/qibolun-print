# -*- coding: utf-8 -*-
"""批次 r001-b0089 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0089.sessions.py            # 写 out/r001-b0089.out.jsonl
  python3 records/r001-b0089.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0089"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0089.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "8ac10e4e": {
  "analysis": {
   "question_context": "知乎提问问「流浪的蛤蟆是否真的骚扰过微博用户“交易子”？」（Q001）。提问者要的是对具体当事人、具体事件的事实裁断；作者没有替提问者认定事实，而是把问题移到一般层面：这件事「被扭曲了」。作者在 P045 明说「这件事到底当事人有没有这样的意思，外人无从评判」。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "提出总判断：此事被扭曲；扭曲点在于中美一样有道德主义极端化倾向，把「道德完善无污点」当作及格线，于是任何轻微道德不完善一经证明即被判为不及格、卑劣、不可救药。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004"], "summary": "补充：公开说辞里的「不可以偏概全」被作者断定为骗人的政治正确话；内心刻薄，仅「可被合理怀疑」有道德缺陷就足以判人道德极刑。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P005", "P006"], "summary": "结果：伦理定性被迫带上「额度限制」。本来「知其有主，不告而取谓之偷」与额度无关，偷五毛与偷一百万同属偷，情节轻重属另一性质的问题。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P007", "P008", "P009", "P010", "P011", "P012", "P013"], "summary": "连续反问举例：盗用头像、盗图、盗版、拷贝粘贴文章；若严格按与额度无关的标准，几乎人人都偷过，并反问这算不算偷过、该不该被定性为有过偷盗行为。", "role": "example"},
    {"unit_id": "U005", "paragraph_refs": ["P014", "P015", "P016", "P017"], "summary": "假想两种自我判决被客观第三人听到：律己严者成了偷东西的人，自奉甚宽者洁白无瑕；作者称这冤，并反问凭什么吃这个亏。", "role": "rebuttal"},
    {"unit_id": "U006", "paragraph_refs": ["P018", "P019"], "summary": "结论：道德主义社会要实际运转，非得配上道德相对主义（给伦理判定加「定罪金额」）甚至道德虚无主义（等于废除任何伦理原则）；道德主义必然导致虚伪和荒诞。", "role": "conclusion"},
    {"unit_id": "U007", "paragraph_refs": ["P020", "P021"], "summary": "另一负效应：认罪与忏悔极其罕见而艰难，遇事先想否认；作者称这就是「这件事被扭曲」的原因。", "role": "claim"},
    {"unit_id": "U008", "paragraph_refs": ["P022", "P023", "P024"], "summary": "让步与限定：承认「这话」严格说的确有性骚扰的可能成分，但性骚扰不是罕见、必然罪大恶极的罪恶，而是与贪婪、欺骗、逃避同类的人性固有问题，深究必为普遍现象。", "role": "qualification"},
    {"unit_id": "U009", "paragraph_refs": ["P025", "P026", "P027"], "summary": "理由：「恰当的性尊重」是深不可测、连有没有「底」都难断言的课题；据此要求人类普遍做到是妄想，说「没做到就是不及格」或「我就做到了」都是没摸清问题规模的愚蠢和狂妄。", "role": "reason"},
    {"unit_id": "U010", "paragraph_refs": ["P028", "P029", "P030", "P031"], "summary": "由人及己：不必因喜爱一个人就为其辩护到绝对白璧无瑕；没有人白璧无瑕，作者自称是勉强透光的墨玉。", "role": "claim"},
    {"unit_id": "U011", "paragraph_refs": ["P032", "P033", "P034", "P035"], "summary": "作者称为「真相」的判断：没有人凭完美无瑕的德行赢得人人必须给予的基本尊重；那只是周围人不愿太残忍、不愿为宽容邀功而让人轻易持有的幻觉。", "role": "claim"},
    {"unit_id": "U012", "paragraph_refs": ["P036"], "summary": "行动建议：不要怯于用真正完善的伦理法则自我审视，不要因害怕结果而给本来完美、简洁、分明的伦理原则打补丁、拉帮结派。", "role": "action_advice"},
    {"unit_id": "U013", "paragraph_refs": ["P037", "P038"], "summary": "两条路的后果对比：打补丁一路通向满脑子浆糊、丧失基本是非观与判断力；自我审视一路抑制虚伪、增长同情理解、使宽容容易。", "role": "rebuttal"},
    {"unit_id": "U014", "paragraph_refs": ["P039", "P040", "P041", "P042", "P043", "P044"], "summary": "以「你若……那么……」的对照收束：自证圣人者过的是被亏欠、绝望怨愤的日子；认识自己有罪与恶者过的是充满幸运与爱的日子；作者称两者绝对逻辑绑定，只有后者有乐观平安。", "role": "conclusion"},
    {"unit_id": "U015", "paragraph_refs": ["P045", "P046", "P047"], "summary": "收尾：当事人有无此意外人无从评判，但律己从严者得福更大；凡真正重视道德者都必须抛弃道德主义立场，二者逻辑不兼容。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这件事被扭曲了，扭曲点在于中国和美国一样有道德主义的极端化倾向，把「道德完善无污点」当作一个人的及格水平，进而把任何轻微的道德不完善都视为不及格、卑劣、不可救药。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "被问到的人都口称「不可以偏概全」，但作者断定绝大部分人是在说政治正确的假话；其内心刻薄，仅仅「可被合理怀疑」有道德缺陷就足以判人道德极刑。", "evidence": ["E3", "E4"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "一个道德主义的社会要实际运转，就非得配上道德相对主义甚至道德虚无主义（等于废除任何伦理原则）；道德主义必然导致虚伪和荒诞。", "evidence": ["E5", "E6"]},
    {"claim_id": "C004", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "「这话」严格说的确有性骚扰的可能成分；但性骚扰本身并非罕见、必然罪大恶极的罪恶，而是与贪婪、欺骗、逃避同类的、人类极难自我根除的人性固有问题，深究下去必为普遍现象。", "evidence": ["E7", "E8"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "「恰当的性尊重」是深不可测、连有没有「底」都难以断言的课题，因此要求人类普遍做到是妄想；宣称「没做到就是不及格」或「我就做到了」都只是没摸清问题规模的愚蠢和狂妄。", "evidence": ["E9", "E10"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "没有人是凭着自己完美无瑕的德行当之无愧地赢得人人必须给予的基本尊重的；那只是一种幻觉，是周围的人不愿对你太残忍、也不愿为自己的宽容邀功而让你轻易持有的。", "evidence": ["E11", "E12"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "自我认证为圣人与认识自己有罪与恶这两个结果是绝对逻辑绑定的，前者通向活地狱，只有后者才有乐观和平安可言。", "evidence": ["E13", "E14", "E15"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "任何一个真正重视道德的人都必须抛弃道德主义的立场，二者逻辑不兼容。", "evidence": ["E16"]},
    {"claim_id": "C009", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "这件事当事人到底有没有这样的意思，外人无从评判；但律己从严的人得到的祝福更大。", "evidence": ["E17", "E18"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不要怯于用真正完善的伦理法则自我审视，也不要因害怕审视结果而给本来完美、简洁、分明的伦理原则打各种补丁。", "evidence": ["E19"]}
   ],
   "argument_steps": [
    "定义起点判断：此事被扭曲（P001）。",
    "归因：道德主义的极端化倾向，把道德无污点当作及格线，于是轻微道德不完善=人格全盘不及格（P002）。",
    "指认公共说辞虚伪：口称不偏概全，实则对「可被合理怀疑」即判道德极刑（P003–P004）。",
    "推导制度性后果：伦理定性被迫加「额度限制」；而伦理法则本与额度无关（P005–P006）。",
    "举例反问：头像、图片、盗版、文章拷贝——严格标准下人人皆偷（P007–P013）。",
    "假想第三人视角，说明严格律己者反受惩罚，追问公平（P014–P017）。",
    "结论：道德主义社会必配道德相对主义乃至虚无主义，故道德主义必然虚伪和荒诞（P018–P019）。",
    "补充负效应：认罪与忏悔因此极难，遇事先否认（P020–P021）。",
    "让步：承认「这话」有性骚扰的可能成分（P022）。",
    "转折立论：性骚扰是人性的普遍固有问题，因「恰当的性尊重」是无底的课题（P023–P027）。",
    "推及自身与他人：没有人白璧无瑕，基本尊重并非德行挣得（P028–P035）。",
    "行动要求：用完善伦理法则自我审视，不打补丁（P036）。",
    "两条路后果对比（P037–P038）。",
    "条件式收束：自证圣人与承认罪恶的结果逻辑绑定（P039–P044）。",
    "限定并收尾：当事人意图外人无从评判；真正重视道德者必须抛弃道德主义（P045–P047）。"
   ],
   "concept_usage": [
    {"term": "道德主义", "meaning": "把「道德完善无污点」当作人的及格水平，并据此对他人作全盘人格判决的立场；作者在结尾把它与「真正重视道德」对立起来。", "evidence": "P002", "ambiguity": "正文未系统界定道德主义的边界，只说二者「逻辑不兼容」（P047）。"},
    {"term": "道德相对主义", "meaning": "给伦理判定加「定罪金额」的补丁，即让定性取决于情节额度。", "evidence": "P018", "ambiguity": "作者称之为「丑陋的补丁」，未讨论其学理形态。"},
    {"term": "道德虚无主义", "meaning": "定罪金额无法达成普遍共识，于是「每个人都有权利自己定义自己的金额」，本质等于废除任何伦理原则。", "evidence": "P018", "ambiguity": "本文未说明。"},
    {"term": "额度限制／定罪金额", "meaning": "对伦理问题定性时附加的数量门槛；作者认为它与「知其有主，不告而取谓之偷」这种与额度无关的法则相冲突。", "evidence": "P005", "ambiguity": "两个说法在文中并用于同一含义。"},
    {"term": "恰当的性尊重", "meaning": "被作者称为深不可测、十几代博士一两百年也摸不到底、甚至无法断言有无「底」的课题。", "evidence": "P026", "ambiguity": "作者未给出该课题的具体内容或标准。"},
    {"term": "白璧无瑕／墨玉", "meaning": "道德上毫无瑕疵的自我或他人形象；作者以「整块墨玉，对着太阳勉强透点光」自指不完美。", "evidence": "P029", "ambiguity": "属作者自评，无外部依据。"}
   ],
   "examples_and_targets": [
    "提问所指的具体事件（流浪的蛤蟆是否骚扰微博用户“交易子”）——提问者的问题对象；作者未作事实认定，只在 P022 说「这话」确有性骚扰的可能成分，「这话」所指未明。",
    "「知其有主，不告而取谓之偷」——作者引用的伦理法则（P006），未注明出处。",
    "「不可以偏概全，不能全盘否定」——作者引为虚伪套话的公共说辞（P003）。",
    "中国和美国——作者称两者同样存在道德主义极端化倾向（P002）。",
    "盗头像、盗网络图片、用盗版、拷贝粘贴文章——作者用来自我审视的反问式举例（P008–P011）。",
    "偷五毛/偷一百万/偷一分钱、「没超过一千万都不能叫偷」——作者假设的额度对照（P006、P014）。",
    "「老夫圣明，你真该死」——修辞性引语，用以形容打补丁后的道德判断（P037）。"
   ],
   "conditions": [
    "「这话严格说的确有性骚扰的可能成分」是对特定一句话的限定承认，作者未指明是哪句话、谁的（P022）。",
    "道德主义的后果论证以「一个道德主义的社会，想要实际运转」为前提（P018）。",
    "普遍性判断带条件：「如果深究下去的话必然发现是普遍现象」（P024）。",
    "自我审视与自证圣人的两条路以「你若……」的条件句式提出（P039、P040）。",
    "全文只处理外人如何评判当事人，不涉及当事人自认，作者明说意图「外人无从评判」（P045）。"
   ],
   "rhetoric_and_tone": "问答体议论，语气强断言且训诫性（「你们要记住一个真相——」）；密集反问（「干过没？」「我凭啥吃这个亏？」「难道你们没读过历史？」式追问）；口语与夸张并用（「乖乖龙地咚」「道德变成大大口香糖，能撑到绕地球二十圈」）；使用网络化用词（ta们、zz正确、f*ck 类粗口未见于此篇但语气直白）；先让步后转折，结尾以「逻辑绑定」「逻辑不兼容」的强决定论口吻收束。",
   "unresolved_questions": [
    "P022「这话」具体指哪一句话、说话者是谁，正文未说明；作者对提问所指事实（是否骚扰）未作认定。",
    "作者未解释「道德主义」与「真正重视道德」的判定标准，只断言二者逻辑不兼容。",
    "「知其有主，不告而取谓之偷」的出处与语境未注明，需外部核查。",
    "作者自述「我整个一块墨玉」属自评，无法核验。",
    "提问者的追问立场在正文中未被正面回应，也未复述其指控内容。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P002", "quote": "扭曲的点主要在于中国和美国一样，有道德主义的极端化倾向", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "都意味着一个人不及格、卑劣、不可救药", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "但是其实绝大部分人都是在骗人——说些zz正确的鬼话罢了。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "仅仅是可以被“合理怀疑”有道德缺陷，都已经够绝大部分人去判处道德极刑了。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P018", "quote": "一个道德主义的社会，想要实际运转，非得配上道德相对主义", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P019", "quote": "道德主义，必然导致虚伪和荒诞。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P022", "quote": "这话严格说的确有性骚扰的可能成分。", "relation": "qualifies"},
    {"key": "E8", "paragraph_id": "P024", "quote": "而是如果深究下去的话必然发现是普遍现象。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P026", "quote": "因为“恰当的性尊重”这个课题，是一个深不可测的、靠十几代博士、一两百年的时间根本连底都摸不到的课题", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P027", "quote": "只有可能是一种连问题的规模都没摸清楚的愚蠢和狂妄", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P033", "quote": "我们没有人是凭着自己完美无瑕的德行，当之无愧地赢得了所有人必须给予的基本尊重的。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P035", "quote": "那是周围的人不希望对你太残忍", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P041", "quote": "这两个结果是绝对的逻辑绑定的，根本没有留下任何可能。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P043", "quote": "你选前者，就是在选活地狱。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P044", "quote": "只有选后者你才有乐观和平安可言。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P047", "quote": "任何一个真正重视道德的人，都必须抛弃道德主义的立场，这是逻辑不兼容的。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P045", "quote": "这件事到底当事人有没有这样的意思，外人无从评判。", "relation": "qualifies"},
    {"key": "E18", "paragraph_id": "P046", "quote": "但其实是律己从严的人得到的祝福更大。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P036", "quote": "不要怯于用真正完善的伦理法则自我审视", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["伦理学／道德哲学", "网络舆论与公共评判", "人格与自我认识"],
   "issue_candidates": ["道德主义与道德相对主义", "性骚扰的定性与普遍性", "公共舆论中的道德审判", "自我审视与忏悔"],
   "text_function_candidates": ["答疑", "论辩", "评论", "训诫"],
   "object_candidates": ["流浪的蛤蟆（提问所指当事人）", "微博用户“交易子”（提问所指）", "中国", "美国"],
   "working_keywords": ["道德主义", "道德相对主义", "道德虚无主义", "定罪金额", "恰当的性尊重", "白璧无瑕", "墨玉", "律己从严"]
  },
  "notes": "brief 与 P001–P003 内容基本重合（导航字段，未单独支持主张）。提问是知乎上对具体当事人是否骚扰的追问，作者未作事实认定，只在 P022 有限承认「这话」有性骚扰的可能成分，且「这话」指代不明——已在 unresolved_questions 登记。"
 },
 "1fbdeed7": {
  "analysis": {
   "question_context": "知乎提问（Q001）问：10 岁男孩经常情绪失控，是受爸爸脾气的影响还是环境影响导致的？应该如何正确地引导？提问者要的是原因归属与引导方法；作者开篇说「让我们来梳理一下你的问题」（P001），随即将问题重构为提问者自身的状态问题——真正的困境不是找不到办法，而是没有力气（P006–P008）。全文以第二人称「你／你们」直接对提问者（父母）进言，未对提问者的归因选项作事实裁断。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004", "P005"], "summary": "复述提问者的处境：孩子表现带来忧虑失望与痛苦，为痛苦想定位原因；定位在自己身上不知如何总结、且已尽全力而无余力，定位在父亲、祖父母或环境身上同样沉重且难以改变。", "role": "context"},
    {"unit_id": "U002", "paragraph_refs": ["P006", "P007", "P008"], "summary": "作者给出诊断：真正的困境不是有害因素无法解决，而是就算有办法也担忧没有力气解决；无力为子女争取理想中最低限度生活的绝望感才是真正的问题，即「你累了」。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P009", "P010", "P011", "P012", "P013"], "summary": "指出提问者处在想讨到好办法再挤出一份力气再搏一搏的状态：心平气和是竭力克制的结果，光克制已精疲力竭；在此重压下再给妙计无用，勉强扛更多责任会无以为继、半途而废并陷入更深忧虑。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P014"], "summary": "以断言收束此段推理：这个恶性循环迟早教会你「此路不通」。", "role": "conclusion"},
    {"unit_id": "U005", "paragraph_refs": ["P015", "P016"], "summary": "行动建议：必须先卸下心头重担才有心力做改善；进一步称卸掉后精气神会有良性改变，同样的话以不同精神状态去说效力截然不同，且很大概率不改原有策略节奏就产生不同走向。", "role": "action_advice"},
    {"unit_id": "U006", "paragraph_refs": ["P017", "P018"], "summary": "自问自答界定「千斤重担」：把子女「不正常」的人生轨迹趋势看作绝对要想办法避免的坏事，并把避免不了它看成绝对失职和失败。", "role": "definition"},
    {"unit_id": "U007", "paragraph_refs": ["P019", "P020"], "summary": "理由：真正在教育人、决定人的命运的是世界而非父母，父母为子女设计命运从一开始就受诅咒；自认为只要绝大多数人自然拥有的最基本东西，本身是傲慢且根本性的错误。", "role": "reason"},
    {"unit_id": "U008", "paragraph_refs": ["P021", "P022", "P023", "P024", "P025"], "summary": "指认「逻辑断裂」：这些安排是否孵化为坏结局并不确定；少年时的极大困境真正决定的是非常规的一生而非失败可悲的一生；而「非常规」还包括了伟大。", "role": "rebuttal"},
    {"unit_id": "U009", "paragraph_refs": ["P026", "P027", "P028", "P029", "P030", "P031"], "summary": "以青史留名者常有超常成长历程作例证与反问；把不可阻止的痛苦命运称为「被选中」，并称其发育为憎恨世界的恶魔还是拯救人类的天使，极大程度上取决于父母对待这被选本身的态度。", "role": "example"},
    {"unit_id": "U010", "paragraph_refs": ["P032", "P033"], "summary": "两种态度的后果对照：视其为诅咒、超越正义伦理边界谋求逃避并在失败后怨毒诅咒者，其焦虑沮丧怨恨与无能会浸透子女命运；视其为 blessing in disguise 者不惊慌失措，应对能发乎于情、止乎于理。", "role": "reason"},
    {"unit_id": "U011", "paragraph_refs": ["P034", "P035"], "summary": "限定与再定义：痛苦并不需要全部避免；痛苦对人的真正伤害是靠造成不择手段的逃避、引诱人连环犯错，那些二次三次四次更大的错误决定才是最大杀伤所在。", "role": "qualification"},
    {"unit_id": "U012", "paragraph_refs": ["P036", "P037", "P038"], "summary": "行动建议与结论：父母是子女面对痛苦和艰难的第一个老师，该教的第一课是从容淡定地接受并相信它是财富；那会使子女永远免疫于灾难和困境，这也是父母唯一真正需要做的教育。", "role": "action_advice"},
    {"unit_id": "U013", "paragraph_refs": ["P039", "P040", "P041", "P042"], "summary": "强化可行性：这份教育只需一个人就能完成，他人的不配合恰成反向对照组；只要下定决心没有因素能阻止、没有事情能让你失败，作者称爱足以支撑取胜。", "role": "claim"},
    {"unit_id": "U014", "paragraph_refs": ["P043", "P044", "P045", "P046", "P047", "P048"], "summary": "回到「不同寻常」的判定：其好坏首先取决于父母如何认定；把偏离计划全判为坏等于自居全知、全能、全善的上帝，而这一心态决定一切「妙计」只是苟延残喘，终把「不寻常」推向恶。", "role": "rebuttal"},
    {"unit_id": "U015", "paragraph_refs": ["P049", "P050", "P051", "P052", "P053", "P054", "P055"], "summary": "反问转向提问者自身：孩子对失败的不接受恐怕是大家联手教的，他可能没看到真正坦然接受挫折的示范；他需要看到真正乐观、运转良好的例子，而这不需要整个团队配合，若必须如此则示范的是乐观的不可能。", "role": "rebuttal"},
    {"unit_id": "U016", "paragraph_refs": ["P056", "P057", "P058"], "summary": "收尾：每个子女都面临与众不同的痛苦与困难，所问只是细节不同；世上没有「一般的命运」，没有被选中的人不存在。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "提问者真正的困境不是有害因素存在且无法解决，而是就算有办法也担忧没有力气解决；没有力气为子女争取理想中最低限度生活的绝望感、即「你累了」，才是真正的问题。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "提问者看似心平气和、温言细语，其实是竭尽全力控制才压住的；光是这份克制已经让人精疲力竭。", "evidence": ["E3", "E4"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "在这份重压下再给更多妙计对提问者没什么用，因为没有力气再负担；勉强扛更多责任很快会无以为继，而半途而废的努力只会让人陷入更深的忧虑。", "evidence": ["E5"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "必须先有某种方法把心头重担卸下，先让自己有心力可以拿来做改善；不先卸掉担子，任何妙计都没有燃料、也难有好结果。", "evidence": ["E6"]},
    {"claim_id": "C005", "claim_type": "author_qualified", "attribution": "author", "modality": "predicted", "statement": "真的把担子卸掉后，精气神会直接有良性改变，同样的话用不同精神状态去说效力截然不同；有很大的概率，卸下重担者没有改变任何原有策略和节奏，就已把事情引向别的方向。", "evidence": ["E7"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这个「千斤重担」就是把子女「不正常」的人生轨迹趋势看作一件绝对要想办法避免的坏事，并且把避免不了它看成一种绝对失职和失败。", "evidence": ["E8"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "真正在教育人、决定人的命运的不是父母而是世界；父母为子女设计命运，无论自认为多么保守、打了多少余量，都从一开始是受诅咒的。", "evidence": ["E9"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "自认为要得不多、只要绝大多数人都自然拥有的最基本东西，这本身就是一种傲慢，而且是一种根本性的错误。", "evidence": ["E10"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "这些安排最后是否孵化为坏的结局并不确定；少年时遇到的极大困境、折磨、伤害和痛苦真正决定的，是子女必将拥有非常规的一生，而不是必定失败、可悲的一生。", "evidence": ["E11", "E12"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "「非常规」还包括了伟大；那些青史留名、照耀人类文明的名字，常常有着超乎常人的成长历程。", "evidence": ["E13", "E14"]},
    {"claim_id": "C011", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "当竭尽全力仍不能阻止的痛苦命运降临时，意味着孩子「被选中了」；这种天意的选择会发育成憎恨世界的恶魔还是拯救人类的天使，极大程度上取决于父母自己对待这被选本身的态度。", "evidence": ["E15", "E16"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "父母视其为诅咒、超越正义与伦理边界谋求逃避并在失败后怨毒诅咒，其焦虑、沮丧、怨恨和无能会一滴滴浸透子女的命运；视其为 blessing in disguise 则不会惊慌失措，应对能发乎于情、止乎于理。", "evidence": ["E17", "E18"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "痛苦并不需要全部避免；痛苦对人的真正伤害是靠造成不择手段的逃避、引诱人连环犯错，那些二次、三次、四次在试图逃避中做出的更大错误决定，才是痛苦最大的杀伤所在。", "evidence": ["E19", "E20"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "父母是子女面对痛苦和艰难的第一个老师，该教的第一课是从容、淡定地接受它并相信它是一份财富；那会永远让子女免疫于一切灾难和困境，这其实是父母唯一真正需要做的教育。", "evidence": ["E21", "E22", "E23"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这份教育只需要一个人就能完成；其他人的不配合、反其道而行，恰恰能形成反向对照组。", "evidence": ["E24"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只要下定决心，没有任何其他因素能阻止、也没有任何事情能让你失败；作者并对提问者断言「你已经不会失败了」，因为你对孩子有多少爱，你离失败就有多远。", "evidence": ["E25", "E26"]},
    {"claim_id": "C017", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "「不同寻常」是指不同寻常的坏还是不同寻常的好，首先取决于父母觉得孩子遭遇的这件事本身是不同寻常的坏还是好。", "evidence": ["E27"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "当父母认定偏离自己计划安排全是不同寻常的坏时，就是在自居为全知、全能、全善的上帝；这个心态本身决定一切「妙计」必定不过是苟延残喘，它一定会把「不寻常」推向恶。", "evidence": ["E28", "E29"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者以反问质疑提问者的归因：孩子对失败的不接受真的只是从父亲身上学来的吗；他那样的反应恐怕是大家联手教的，他可能就没有看到任何一个真正可以坦然接受挫折的示范。", "evidence": ["E30", "E31"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者要求提问者重读自己的问题，并以反问指出：问题本身就是对失败的不接受；提问者自己也是「道理都懂……但一遇到还是放不下」。", "evidence": ["E32", "E33"]},
    {"claim_id": "C021", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "孩子需要看到一个真正乐观的、运转良好的例子，而这并不需要「一整个团队的全部队友互相配合来创造」；如果必须要这样的条件才能保持乐观，那与其说示范乐观的可能，不如说示范乐观的不可能。", "evidence": ["E34", "E35"]},
    {"claim_id": "C022", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "提问者的子女并非特例：每个子女都面临与众不同的痛苦和困难，所问只是细节不同；世上没有「一般的命运」，没有被选中的人不存在。", "evidence": ["E36", "E37"]}
   ],
   "argument_steps": [
    "复述提问者的两难：归因于己则无从总结且已无余力，归因于他人与环境则同样沉重难改（P002–P005）。",
    "重新诊断：真正的困境是无力气而非无办法；「你累了」才是真正的问题（P006–P008）。",
    "说明当下给方法无效：克制已耗尽精力，勉强加责必半途而废并加重忧虑（P009–P013）。",
    "断言此路不通（P014）。",
    "行动要求：先卸下心头重担，才谈得上改善；并预期卸下后状态与效果的改变（P015–P016）。",
    "界定重担之内涵（P017–P018）。",
    "给出理由：决定命运的是世界而非父母，为子女设计命运自始受诅咒；自认要求最低是傲慢（P019–P020）。",
    "指认逻辑断裂：坏结局不确定；苦难决定的是「非常规」的一生，而非常规包含伟大（P021–P025）。",
    "例证与反问：青史留名者常有超常成长历程（P026–P027）。",
    "提出「被选中」，并说明其走向取决于父母的态度（P028–P031）。",
    "两种态度的后果对照（P032–P033）。",
    "限定：痛苦不必全部避免；真正杀伤来自逃避引发的连环错误（P034–P035）。",
    "行动要求与结论：第一课是坦然接受，这是唯一真正需要的教育（P036–P038）。",
    "强化：一人即可完成，他人不配合成反向对照组；下定决心即不会失败（P039–P042）。",
    "重申「不同寻常」取决于父母认定，自居上帝者必把不寻常推向恶（P043–P048）。",
    "反问转向提问者自身，指出其问题即是对失败的不接受（P049–P055）。",
    "普遍化收尾：没有「一般的命运」（P056–P058）。"
   ],
   "concept_usage": [
    {"term": "妙计", "meaning": "提问者所期待的具体办法；作者在其「没有力气再负担」的判断下判定此类方法无效，后又用以指一切试图规避「不寻常」的方案。", "evidence": "P013", "ambiguity": "文中未列举任何具体妙计的内容。"},
    {"term": "千斤重担", "meaning": "把子女「不正常」的人生轨迹趋势看作绝对要想办法避免的坏事，并把避免不了它看成绝对失职和失败的心态。", "evidence": "P018", "ambiguity": "本文未界定「正常／不正常」的判定标准。"},
    {"term": "非常规／不同寻常", "meaning": "与「失败的、可悲的一生」相区别的命运描述，作者称其「还包括了伟大」；其好坏取决于父母如何认定。", "evidence": "P022", "ambiguity": "「正常」的标准与「非常规」的具体范围本文未说明。"},
    {"term": "被选中／天意的选择", "meaning": "把不可阻止的痛苦命运解释为一种选择；作者称其会发育为憎恨世界的恶魔或拯救人类的天使。", "evidence": "P029", "ambiguity": "属作者的宿命／宗教式表述，未给出可检验标准或出处。"},
    {"term": "blessing in disguise", "meaning": "英文短语，指把苦难视为伪装的赐福；作者以此描述父母应持的态度。", "evidence": "P033", "ambiguity": "本文未展开该词的内涵。"},
    {"term": "痛苦", "meaning": "作者区分痛苦本身与其伤害：痛苦本身不必全部避免，伤害来自为逃避痛苦而连环犯错所做的更大错误决定。", "evidence": "P035", "ambiguity": "未区分身体痛苦与心理痛苦。"},
    {"term": "反向对照组", "meaning": "他人的不配合、反其道而行，恰能反衬出面对苦难、失败、困难时应该有的样子。", "evidence": "P039", "ambiguity": "本文未说明该机制的作用条件。"}
   ],
   "examples_and_targets": [
    "提问所指的 10 岁男孩及其父亲、祖父母、环境——提问者列出的归因选项（P005）；作者未认定其中任一为真正原因，而把问题移到提问者自身状态（P006–P008）。",
    "「妙计」（P013、P048）——作者对提问者所求方法的代称，非具体例证。",
    "「那些青史留名、照耀人类文明的名字」（P026）——作者的例证，未指名任何具体人物。",
    "「一整个团队的全部队友互相配合来创造」（P054）——作者引述并反驳的说法，引号内说话者未标明。",
    "「很多人跛行已久，已经觉得这是正常的了」（P045）——作者的比喻性修辞，指逻辑断裂已被视为常态。",
    "「你已经对你说了这话……你已经不会失败了」（P041）与「你对ta有多少爱，你离失败就有多远」（P042）——作者对提问者的直接保证式断言，非外部事实。"
   ],
   "conditions": [
    "全文诊断以提问者的具体处境为前提（10 岁男孩、经常情绪失控、提问者已尽全力）。",
    "效果判断带概率限定：「有很大的概率」卸下重担者不改策略也能改变走向（P016）。",
    "「无论父母们自己自认为多么的保守、打了多少余量」——作者称受诅咒无例外（P019）。",
    "「是否最后会孵化为坏的结局、并不是确定的」——对恶果的必然性作否定（P021）。",
    "恶魔／天使之分「极大程度上取决于」父母态度，为程度限定而非全称决定（P031）。",
    "「痛苦并不需要全部避免」为限定，非主张应当追求痛苦（P034）。",
    "「只要下定决心，没有任何其他因素能阻止」——作者给出的无条件保证（P040）。",
    "「如果必须要这样的条件才能保持乐观」——对乐观之前提的假设性反驳（P054）。",
    "全篇针对父母的教养心态，未讨论该儿童是否另有医学或心理诊断。"
   ],
   "rhetoric_and_tone": "第二人称「你／你们」直接进言，先共情式复述提问者的痛苦与克制，再转入诊断式断言；密集反问（「不是吗？」「明白吗？」「看到没有？」「你们看到逻辑断裂的地方了吗？」）；训诫与布道式语气（「父母们，好好想想吧」「你们的孩子，被选中了」）；宗教化措辞（「天意的选择」「blessing in disguise」「折断痛苦的毒针」）；对子女使用「ta们」等网络化代词；结尾以普遍化反问收束。",
   "unresolved_questions": [
    "提问者所问的「是受爸爸脾气的影响还是环境影响」在正文中未被直接回答：作者把问题重构为提问者自身的状态问题（P006–P008），未对两种归因作事实裁断。",
    "「被选中」「天意的选择」属作者的宿命式表述，本文未给出可检验标准或思想出处，归属层面需研究者复核。",
    "P026「那些青史留名、照耀人类文明的名字」未指名任何具体人物，无法核验其为历史事实还是修辞。",
    "P032「怨毒、罥骂、诅咒」中「罥骂」疑为「咒骂」的笔误；原文保留未改写，需外部核查。",
    "P054 引号内「一整个团队的全部队友互相配合来创造」的说话者未标明，是否为提问者原话或作者概括的常见说法不明。",
    "作者未界定「情绪失控」，也未考虑 10 岁儿童情绪失控是否存在医学／心理诊断因素。",
    "作者称「你的爱支撑你取胜，是绰绰有余的」（P042）为对提问者的保证式断言，无文中依据可核验。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P006", "quote": "其实，你真正的困境并不是看到有各种有害的因素存在，没有办法去解决，而是就算有办法，你担忧没有力气解决。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P008", "quote": "你累了，这才是真正的问题。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P010", "quote": "但其实是竭尽全力的控制着才压住的，不是吗？", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P012", "quote": "光是这份克制，已经让人精疲力竭了，不是吗？", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P013", "quote": "再给你更多的妙计，其实对你是没什么用的。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P015", "quote": "你必须有某种方法，先把心头的重担卸下。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P016", "quote": "有很大的概率，那个卸下了重担的你，没有改变任何原有的策略和节奏，就已经把事情引向了别的方向。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P018", "quote": "看作一件绝对要想办法避免的坏事，并且把避免不了它看成一种绝对失职和失败", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P019", "quote": "父母为子女设计命运，无论父母们自己自认为多么的保守、打了多少余量，都从一开始是受诅咒的。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P020", "quote": "这本身就是一种傲慢，而且是一种根本性的错误。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P021", "quote": "是否最后会孵化为坏的结局、并不是确定的，明白吗？", "relation": "qualifies"},
    {"key": "E12", "paragraph_id": "P022", "quote": "而是必将拥有非常规的一生。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P025", "quote": "“非常规”，还包括了伟大啊。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P026", "quote": "那些青史留名、照耀人类文明的名字，常常有着超乎常人的成长历程吗？", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P029", "quote": "你们的孩子，被选中了。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P031", "quote": "极大程度上取决于你们自己对待这被选本身的态度。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P032", "quote": "你们视其为诅咒，无所不用其极的、乃至于超越正义、伦理边界的谋求逃避", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P033", "quote": "你们视其为blessing in disguise", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P034", "quote": "痛苦并不需要全部避免。", "relation": "qualifies"},
    {"key": "E20", "paragraph_id": "P035", "quote": "是那些二次、三次、四次在试图逃避中做出的更大的错误决定，才是痛苦最大的杀伤所在。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P036", "quote": "而是从容、淡定的接受它，相信它只是一份处理工艺复杂、兑换过程漫长的财富的信心。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P037", "quote": "那会永远的让ta们免疫于一切灾难和困境。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P038", "quote": "这其实是父母们唯一真正需要做的教育。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P039", "quote": "而且这份教育，只需要一个人就能完成。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P040", "quote": "只要下定决心，没有任何其他因素能阻止，也没有任何事情能让你失败。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P042", "quote": "你的爱支撑你取胜，是绰绰有余的。", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P046", "quote": "首先取决于你们觉得ta遭遇的这件事本身是不同寻常的坏，还是不同寻常的好。", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P047", "quote": "你们是在自居为全知、全能、全善的上帝", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P048", "quote": "决定了一切“妙计”必定不过是苟延残喘，勉强拖延", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P049", "quote": "你的孩子对失败的不接受，真的只是从父亲身上学来的吗？", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P052", "quote": "他其实可能就没有看到任何一个真正的可以坦然接受挫折的示范。", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P050", "quote": "难道你的问题本身，不正是对失败的不接受吗？", "relation": "supports"},
    {"key": "E33", "paragraph_id": "P051", "quote": "你又何尝不是“道理都懂，也都知道失败没什么大不了，但一遇到还是放不下”吗？", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P053", "quote": "他需要看到一个真正乐观的、运转良好的例子。", "relation": "supports"},
    {"key": "E35", "paragraph_id": "P054", "quote": "与其说是在示范乐观的可能，不如说是在示范乐观的不可能。", "relation": "supports"},
    {"key": "E36", "paragraph_id": "P057", "quote": "其实你们的子女，谁没有面临与众不同的痛苦和困难？", "relation": "supports"},
    {"key": "E37", "paragraph_id": "P058", "quote": "世上哪有“一般的命运”？谁真的没有被选中呢？", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["家庭教育／亲子关系", "心理与情绪", "人生哲学／苦难观"],
   "issue_candidates": ["儿童情绪失控的成因与引导", "父母的无力感与焦虑", "为子女设计命运的正当性", "苦难的意义与应对态度"],
   "text_function_candidates": ["答疑", "劝解／疏导", "训诫", "论辩"],
   "object_candidates": ["提问者（10 岁男孩的家长）", "10 岁男孩", "孩子的父亲", "祖父母", "青史留名者（未指名）"],
   "working_keywords": ["情绪失控", "妙计", "千斤重担", "非常规", "不同寻常", "被选中", "天意的选择", "blessing in disguise", "反向对照组"]
  },
  "notes": "本篇无图片节点（图片节点 0），正文 58 段全部读完，按默认 status=read、full_text_checked=true 处理。brief 字段在句中被截断（止于「所」），仅作导航，未用于支持任何主张。提问者给出的两个归因选项（爸爸脾气／环境）在正文中未被正面裁断：作者把问题重构为提问者「没有力气」的状态问题（P006–P008），已在 unresolved_questions 登记。P032「罥骂」疑为笔误，原文保留未改写。P054 引号内说法未标明说话者。P026 的青史留名者未指名，无法外部核验。"
 },
 "f9d288d4": {
  "analysis": {
   "question_context": "知乎提问（Q001）问：怎样才能让自己不胆怯，敢在大众面前说话，并且有话说，不脸红，怎么克服？提问者要的是克服怯场的技巧。作者开篇称「这个问题啊，原因很繁杂，我们先条分缕析」（P001），随后不直接给技巧，而是先论证中国文化本就排斥「对公众讲话」的能力、再指出怯场的根子不在修辞而在事实／逻辑／义理不扎实、最后把动机定性为求崇拜，并结论式地回答「这份害怕……是不该被消除、也是消除不了的」（P030）。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "宣告方法：问题原因繁杂，先条分缕析。", "role": "transition"},
    {"unit_id": "U002", "paragraph_refs": ["P002"], "summary": "第一个原因：中国文化不强调当众演讲能力，甚至抵触「大广场演讲」；对传统中国精英阶层而言，「对公众讲话」的能力是多余的。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P003", "P004"], "summary": "对照论证：中国的运行逻辑与希腊—罗马文化的「广场mz」体系不同，强调专家治国、精英治国，在很小的全面知识决策圈内达成共识，并依赖私下坦率交流与「含蓄沟通」这类不立文字、依靠暗示与心照不宣的技术。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P005", "P006"], "summary": "以历史印象与建筑遗存举证：中国历史里领袖对人山人海振臂高呼的场景几乎为零，并请读者去太和殿参观以获直观印象。", "role": "example"},
    {"unit_id": "U005", "paragraph_refs": ["P007", "P008"], "summary": "两条图片说明文字：太和殿（御座前只有几十平米）与军机处值班房，均标「侵删」；对应图片 IMG001、IMG002。", "role": "other"},
    {"unit_id": "U006", "paragraph_refs": ["P009"], "summary": "说明太和殿前广场的设计用途是大型朝会与庆典，靠声音洪亮的内官层层传声，没有「公众讨论」「说服各方」的功能，只是自顶向下公布既定结果。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P010"], "summary": "推论：在中国策略讨论限于精英小圈子，要获得最大政策影响力，主要策略是不断获得更上一层决策圈的注意与认可，而非更广范围的认知度。", "role": "conclusion"},
    {"unit_id": "U008", "paragraph_refs": ["P011"], "summary": "进一步断言：靠大型公开演讲获得曝光度与「民意」在根子上被中国治理文化排斥，因为不可避免会媚俗，会导致前瞻性不足、过于情绪化、不必承担全部个人责任的政策，基本被视为品格缺陷。", "role": "claim"},
    {"unit_id": "U009", "paragraph_refs": ["P012", "P013"], "summary": "重新解释「虽千万人吾往矣」：不是杀敌，而是即使裹挟了巨大盲目共识、反对会被孤立也要正面对抗；有数据、逻辑、大义可以说服我，诉诸人数与赞数则被拒绝。", "role": "definition"},
    {"unit_id": "U010", "paragraph_refs": ["P014"], "summary": "条件式推论：论据、逻辑、大义每一样都深不可测，若真诚地以三者为此唯一正确的说服之道，就不应还有很多精力去磨练鼓动大众情绪的技巧与积累经验。", "role": "reason"},
    {"unit_id": "U011", "paragraph_refs": ["P015", "P016", "P017", "P018", "P019"], "summary": "以文言格言连续陈述君子应然：学而时习之、不耻下问、喻于义、搞好事实逻辑大义、讷于言。", "role": "reason"},
    {"unit_id": "U012", "paragraph_refs": ["P020"], "summary": "结论式主张：东方意义上的君子不应拥有、尤其不应追求调动群体情绪的能力，而应天然是这种追求的敌人。", "role": "claim"},
    {"unit_id": "U013", "paragraph_refs": ["P021"], "summary": "理由：「群体非理性」是可怕的武器，是任何真正卓有成效的领导体系最大的软肋和噩梦；有人却孜孜不倦地追求并花样百出地使用这种技术。", "role": "reason"},
    {"unit_id": "U014", "paragraph_refs": ["P022"], "summary": "指认该技术在西方被称为「修辞学」，曾被希腊、罗马贵族精英视为最重要的个人技能；在东方伦理视角下走这条路属于毋庸置疑的道德问题，并引「巧言令色，鲜矣仁」佐证。", "role": "rebuttal"},
    {"unit_id": "U015", "paragraph_refs": ["P023"], "summary": "反推提问者的处境：面对大庭广众说不出有情绪的话、发挥不出激情，在东方文化里不构成缺陷、甚至可说是加分，因为这表明没有此意图、没有能力储备且有心理障碍，所说之话可信度反而提高；作者括号声明这里没有评判两种观点设计谁好谁坏。", "role": "rebuttal"},
    {"unit_id": "U016", "paragraph_refs": ["P024"], "summary": "行动要求：要说的话应限于所见的事实、所想的逻辑、所悟的大义，直直摆出来供人参考，而非要人顺从屈服。", "role": "action_advice"},
    {"unit_id": "U017", "paragraph_refs": ["P025"], "summary": "把讲话等同于念实验报告、念科学论文：虽仍有表达技能要求，但根子不在修辞学，而在事实掌握没把握、逻辑不扎实、义理不坚固，即平时满足于似是而非、道听途说、模棱两可。", "role": "claim"},
    {"unit_id": "U018", "paragraph_refs": ["P026"], "summary": "描述状态：自己知道这些经不起追问，论据是听说的、逻辑是糊弄的、义理是凭朴素感情临时站的，故在大庭广众甚至小范围发言都战战兢兢。", "role": "reason"},
    {"unit_id": "U019", "paragraph_refs": ["P027"], "summary": "反问指出出路：不知道就直说不知道，只说知道的、明白的、有把握的，并追问为何没走这条出路。", "role": "action_advice"},
    {"unit_id": "U020", "paragraph_refs": ["P028", "P029"], "summary": "给出动机诊断：因为贪图更高的影响力、不想失去虽不该得到但已得到的机会和地位；说穿了是自立为偶像、想要获得崇拜，所以害怕光鲜假象破裂。", "role": "claim"},
    {"unit_id": "U021", "paragraph_refs": ["P030"], "summary": "结论式回答：若真存在这样的绝技，世界不会是现在这个样子；这份害怕是应该的，是不该被消除、也是消除不了的。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "中国的文化里并不强调当众演讲的能力，甚至干脆抵触「大广场演讲」；这种「对公众讲话」的能力对传统中国的精英阶层而言是多余的。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "中国的运行逻辑与希腊—罗马文化的「广场mz」体系完全不同，它强调专家治国、精英治国，是在一个必然很小的、掌握全面知识的决策圈之内达成共识，并依赖私下坦率交流与「含蓄沟通」这类不立文字、依靠暗示与心照不宣的技术。", "evidence": ["E2", "E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "中国历史里「领袖人物对人山人海振臂高呼、响彻云霄」这种场景几乎是零；太和殿前广场的设计只为大型朝会与庆典的层层传声，完全没有「公众讨论」「说服各方」的功能，只是自顶向下公布既定结果。", "evidence": ["E4", "E5"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "在中国，策略讨论限定在精英小圈子之内；要取得最大限度的政策影响力，主要策略是不断获得更上一层决策圈的注意和认可，而不是获得更多、更广范围的认知度。", "evidence": ["E6"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "通过大型公开演讲获得曝光度与「民意」，在根子上被中国的治理文化排斥，因为不可避免会媚俗，原理上会导致前瞻性不足、过于情绪化、不必承担全部个人责任的政策；这基本上被视为一种品格缺陷。", "evidence": ["E7", "E8"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "「虽千万人吾往矣」指的是即使被巨大的盲目共识裹挟、反对会被孤立，也要挺身而出正面对抗；诉诸人数与赞数而非逻辑的做法被拒绝。", "evidence": ["E9", "E10"]},
    {"claim_id": "C007", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "论据、逻辑、大义每一样都深不可测，可以花费全部时间精力；如果真诚地以讲论据、讲逻辑、讲大义为唯一正确的说服之道，就不应该还有很多精力去磨练鼓动大众情绪的技巧。", "evidence": ["E11"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "一个东方意义上的君子不应该拥有、尤其不应该追求调动群体情绪的能力，而应该天然是这种追求的敌人。", "evidence": ["E12", "E13"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "「群体非理性」是一件可怕的武器，是任何真正卓有成效的领导体系最大的软肋和噩梦；而有人不是偶然使用，而是孜孜不倦地刻苦追求、视如得意技能、无处不用。", "evidence": ["E14", "E15"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "该技术在西方被称为「修辞学」，曾被视为希腊、罗马贵族精英最重要的个人技能；在东方伦理的视角下，选择这种个人发展路线去求荣华富贵属于毋庸置疑的道德问题。", "evidence": ["E16", "E17"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "面对大庭广众说不出有情绪的话、发挥不出激情，在东方文化里并不构成缺陷，甚至可以说是加分的；因为这意味着没有这种意图、没有做能力储备且对这样做有心理障碍，于是所说之话的可信度在很大程度上提高了。作者同时声明这里没有评判两种观点设计谁好谁坏。", "evidence": ["E18", "E19", "E20"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "要说的话应仅限于所见的事实、所想的逻辑、所悟的大义，只需直直摆出来供人参考，而非要人顺从、屈服；那与念一份实验报告、念一篇科学论文应无本质区别。", "evidence": ["E21", "E22"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "胆怯的根子不是口才问题，而是事实掌握没把握、逻辑不扎实、义理不坚固，即平时满足于似是而非、道听途说、模棱两可；因为知道这些经不起追问，所以发言时战战兢兢、害怕虚弱不堪一击。", "evidence": ["E23", "E24"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者以反问提出出路并追问：不知道的直说不知道，只说自己知道的、明白的、有把握的，不就可以了吗？你为什么没走这条出路？", "evidence": ["E25"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "没走这条出路的原因是贪图更高的影响力、不想失去虽不该得到但已经得到的机会和地位：若蒙混过关便觉得会有更好地位，若失手则会遭到反噬。", "evidence": ["E26"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "说穿了，这其实是自立为偶像、想要获得崇拜，所以害怕自己极力营造的光鲜假象无意间破裂。", "evidence": ["E27"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "作者以反事实假设作答：如果真存在这样的绝技，世界会是现在这个样子吗？这份害怕是应该的，是不该被消除、也是消除不了的。", "evidence": ["E28"]}
   ],
   "argument_steps": [
    "宣告条分缕析的方法（P001）。",
    "给出第一条原因：中国文化不强调甚至抵触当众演讲，该能力对传统精英是多余的（P002）。",
    "对照论证中国与希腊—罗马「广场mz」体系的差异：专家／精英治国、小决策圈共识、含蓄沟通（P003–P004）。",
    "以历史印象与太和殿等建筑遗存举证（P005–P006，附图 P007–P008）。",
    "说明太和殿前广场无公众讨论功能，只是自上而下公布结果（P009）。",
    "推出政策影响力的获取路径：向上获取决策圈认可而非扩大认知度（P010）。",
    "断言公开演讲求民意被治理文化排斥，因媚俗而导致劣质政策，被视为品格缺陷（P011）。",
    "重新解释「虽千万人吾往矣」，确立以论据、逻辑、大义为说服之道（P012–P013）。",
    "条件式推论：三者深不可测，真诚奉之者无余力磨练鼓动群体情绪的技巧（P014）。",
    "以文言格言陈君子应然，结论君子应为调动群体情绪之追求的敌人（P015–P020）。",
    "理由：群体非理性是领导体系最大的软肋和噩梦（P021）。",
    "指认该技术在西方即修辞学，在东方伦理下是道德问题，引「巧言令色，鲜矣仁」（P022）。",
    "反推：不善煽情在东方文化中不是缺陷甚至加分，且提高可信度（作者声明不作好坏评判）（P023）。",
    "行动要求：只说事实、逻辑、大义，供人参考而非要人屈服（P024）。",
    "把讲话比作念实验报告／科学论文，指出根子在事实、逻辑、义理而非口才（P025）。",
    "描摹心理状态：明知经不起追问故战战兢兢（P026）。",
    "以反问指出出路：不知道就说不知道（P027）。",
    "诊断动机：贪图影响力，自立为偶像求崇拜（P028–P029）。",
    "结论：绝技不存在，这份害怕是应该的、不该被消除也消除不了（P030）。"
   ],
   "concept_usage": [
    {"term": "修辞学", "meaning": "作者称其在西方被如此称呼，曾被希腊、罗马贵族精英视为最重要的个人技能；本文中作者把它等同于调动群体情绪的技术。", "evidence": "P022", "ambiguity": "作者以该词指「鼓动大众情绪」的技巧，是否等同于西方修辞学的通常含义，本文未讨论。"},
    {"term": "广场mz", "meaning": "「希腊—罗马文化的“广场mz”体系」中的缩略写法，作者借以对照中国的治理逻辑。", "evidence": "P003", "ambiguity": "全称与具体所指本文未说明。"},
    {"term": "群体非理性", "meaning": "被作者称为可怕的武器，是任何真正卓有成效的领导体系最大的软肋和噩梦。", "evidence": "P021", "ambiguity": "本文未界定其机制与边界。"},
    {"term": "含蓄沟通", "meaning": "共同决策时的沟通技术：利用大量小圈子共识，不立文字、不留把柄的微妙表态，依靠暗示和心照不宣。", "evidence": "P004", "ambiguity": "本文未说明其适用层级与失效条件。"},
    {"term": "媚俗", "meaning": "通过大型公开演讲获得曝光度与民意所不可避免的结果，作者称其原理上导致前瞻性不足、过于情绪化、不必承担全部个人责任的政策。", "evidence": "P011", "ambiguity": "本文未给出判定标准。"},
    {"term": "大义／义理", "meaning": "与事实、逻辑并列的说服要素，作者称其「深不可测」，是讲话应当直直摆出的内容之一。", "evidence": "P014", "ambiguity": "「大义」与「义理」在文中近似通用，均未定义。"},
    {"term": "偶像", "meaning": "「自立为偶像，想要获得崇拜」——作者对怯场根因的定性，指营造光鲜假象以求得崇拜。", "evidence": "P029", "ambiguity": "属作者的修辞性定性，无外部依据。"}
   ],
   "examples_and_targets": [
    "太和殿、太和殿前广场、军机处值班房——作者作为直观例证引用的建筑遗存（P006–P009）；其中 P007、P008 为图片说明文字，对应图片 IMG001、IMG002 未经核验。",
    "「虽千万人吾往矣」——作者引用的文言语句并自行解释（P012），未注明出处。",
    "赵子龙（「七进七出」）——作者引以对比的通俗叙事形象，说明该语并非指杀敌（P012）。",
    "希腊—罗马文化的「广场mz」体系、修辞学、希腊与罗马的贵族精英——作者设置的对照对象（P003、P022）。",
    "「靠声音洪亮的内官层层传声」——作者对中国古代朝会传声方式的叙述（P009），未注明来源。",
    "「巧言令色，鲜矣仁」——作者引用的文言语句，未注明出处（P022）。",
    "「君子应该学而时习之」「不耻下问」「喻于义」「讷于言」——作者引用的文言格言（P015–P019），未逐条注明出处。",
    "「念一份实验报告、念一篇科学论文」——作者的类比（P025）。"
   ],
   "conditions": [
    "「如果你们仔细查看」——历史印象的举证以读者自行查看为条件（P005）。",
    "「如果你真诚的以讲论据、讲逻辑、讲大义为唯一正确的说服之道」——对推论主体的资格性限定（P014）。",
    "「在东方伦理的视角下」——道德问题之判断明标视角（P022）。",
    "「注意，这里没有评判这两种观点设计谁好谁坏」——作者对自己跨文化比较的评价边界声明（P023）。",
    "「如果真存在这样的绝技」——结尾结论以反事实假设为前提（P030）。",
    "「你本来要说的话，应该仅限于你所看到的事实……」——对发言内容的范围限定（P024）。",
    "全文针对的是「当众讲话／对公众演讲」场景与提问者的个人处境，未讨论其他沟通场合。"
   ],
   "rhetoric_and_tone": "条分缕析的讲课式结构（「原因很繁杂，我们先条分缕析」「首先」）；大量中西对照的断言句；密集引用文言格言作为论据；粗口式转折（「那对不起，虽千万人，f*ck it，吾往矣」）；括号插注（「（注意，这里没有评判这两种观点设计谁好谁坏）」「（侵删）」）；结尾以反问收束（「如果真存在这样的绝技，世界会是现在这个样子吗？」）；对提问者的动机作直言不讳的定性（「你贪图更高的影响力」「自立为偶像」），带训诫色彩，并以「这份害怕……是不该被消除、也是消除不了的」作结，不提供克服技巧。",
   "unresolved_questions": [
    "本篇含 2 个图片节点（IMG001、IMG002，对应 P007「御座前只有几十平米面积的太和殿（侵删）」与 P008「军机处值班房（侵删）」的说明文字），图片内容未核验，需人工或多模态复核：图片是否确为所标建筑、是否含可读文字均未确认。",
    "P007、P008 为图片说明文字（含「侵删」字样），其正文归属与是否属作者原创表述需研究者确认。",
    "「虽千万人吾往矣」「巧言令色，鲜矣仁」「君子应该学而时习之」等引文出处本文未注明，需外部核查。",
    "作者关于中国古代朝会「靠声音洪亮的内官层层传声」的叙述（P009）未给出来源，待外部核查。",
    "「广场mz」为缩略写法，全称与具体所指本文未说明。",
    "P021 末尾「这种技术，」与 P022 首句跨段续接，引文连续性与段落切分的关系需注意。",
    "提问者所问的「怎么克服」在结尾被转为「这份害怕是应该的，是不该被消除、也是消除不了的」（P030），作者未给出通常意义上的克服技巧。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P002", "quote": "首先，中国的文化里并不强调当众演讲的能力，甚至干脆就是抵触这种“大广场演讲”的。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P003", "quote": "它强调的是专家治国、精英治国，强调是在掌握了全面知识的决策圈（这必然是一个非常小的决策圈）之内达成共识。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "大量依靠暗示和心照不宣", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P005", "quote": "你会发现中国历史里“领袖人物对人山人海振臂高呼、响彻云霄”这种场景几乎是零。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P009", "quote": "完全没有“公众讨论”，“说服各方”的功能，只是在自顶向下层层公布既定的结果。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P010", "quote": "你的主要策略应该是不断的获得更上一层的决策圈的注意和认可，而不是不断的获得更多、更广范围的认知度。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P011", "quote": "在根子上是被中国的治理文化排斥的行为——因为你不可避免会媚俗。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P011", "quote": "这基本上被视为一种品格缺陷。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P012", "quote": "而是指即使你裹挟了巨大的盲目共识，哪怕我反对会被限于孤立，我也要挺身而出正面对抗。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P013", "quote": "你不诉诸逻辑，而是诉诸于你背后站着多少人、有多少赞", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P014", "quote": "如果你真诚的以讲论据、讲逻辑、讲大义为唯一正确的说服之道，你不应该还有很多精力去磨练你鼓动大众情绪的技巧、去积累那些经验。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P020", "quote": "一个东方意义上的君子不应该拥有——尤其是追求拥有——调动群体情绪的能力，而应该天然的是这种追求的敌人。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P019", "quote": "君子应该讷于言。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P021", "quote": "因为“群体非理性”是一件可怕的武器，是任何真正卓有成效的的领导体系最大的软肋和噩梦。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P021", "quote": "孜孜不倦的刻苦追求、视如得意技能的、花样百出的无处不用", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P022", "quote": "在西方被称为“修辞学”——曾经被希腊、罗马的贵族精英视为最重要的个人技能。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P022", "quote": "在东方伦理的视角下，属于毋庸置疑的道德问题。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P023", "quote": "在东方文化里，并不构成一种缺陷。甚至，还可以说是加分的。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P023", "quote": "于是你说的话在很大的程度上可信度提高了。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P023", "quote": "（注意，这里没有评判这两种观点设计谁好谁坏）", "relation": "qualifies"},
    {"key": "E21", "paragraph_id": "P024", "quote": "你所要做的只是直直的摆出来，是供人参考，而非要人顺从、屈服。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P025", "quote": "那和念一份实验报告、念一篇科学论文，应该没有本质区别。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P025", "quote": "那更多的不是口才问题，而是你平时满足于似是而非的东西，满足于道听途说，满足于模棱两可。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P026", "quote": "都难免战战兢兢，汗不敢出，害怕自己的虚弱不堪一击。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P027", "quote": "你不知道的，就直说不知道，只说自己知道的、明白的、有把握的、不就可以了吗？你为什么没走这条出路？", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P028", "quote": "因为你贪图更高的影响力，你不想失去你虽不该得到、但已经得到的机会和地位。", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P029", "quote": "说穿了，这其实是自立为偶像，想要获得崇拜。", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P030", "quote": "这份害怕是应该的，是不该被消除、也是消除不了的。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["文化比较／中西政治文化", "伦理学／君子人格", "修辞与说服", "公共表达与心理"],
   "issue_candidates": ["当众讲话能力在不同文化中的地位", "公开演讲与媚俗／群体非理性", "怯场的真实成因", "说服方式：论据逻辑大义 vs 诉诸人数"],
   "text_function_candidates": ["答疑", "论辩", "文化解释", "训诫"],
   "object_candidates": ["提问者", "中国（治理文化）", "希腊—罗马文化", "传统中国精英阶层", "太和殿", "军机处", "赵子龙（引例）"],
   "working_keywords": ["广场mz", "修辞学", "群体非理性", "含蓄沟通", "媚俗", "虽千万人吾往矣", "讷于言", "巧言令色", "自立为偶像"]
  },
  "status": "needs_reread",
  "image_checked": False,
  "full_text_checked": False,
  "notes": "本篇含 2 个图片节点（IMG001、IMG002，src 见 structure.images），图片内容未经核验，需图像核验：无法确认两图是否即为太和殿与军机处、图内是否含可读文字，故本记录不声称读懂图片，也不据图片补写正文。因图片未核验，本篇 status=needs_reread、image_checked=false、full_text_checked=false（按系统提示词第 5 节「图片文章还要求 image_checked=true 才可 full_text_checked=true」的保守解释）。两图对应的说明文字为 P007「御座前只有几十平米面积的太和殿（侵删）」与 P008「军机处值班房（侵删）」，未核验前不作认定。brief 与 P002–P004 内容基本重合（导航字段），未单独支持主张。P021 末尾「这种技术，」与 P022 首句跨段续接，引文按原段切分处理。P023 括号内「观点设计」字样疑为原文表述，未改写。"
 },
 "4f0d4841": {
  "analysis": {
   "question_context": "知乎提问（Q001）问：打算重组家庭时，父母需要给孩子做什么心理建设？提问者预设了「父母给孩子做心理建设」这一做法。作者开篇即把根子前移：「这个问题的根子很远，远在没有离婚之前」（P001），随后不接受该问法——把「心理建设」解释为「如何圆场」（P006）、把问题定性为给已垮台的承诺打补丁（P028），并在结尾反转受力方：「需要“心理建设”的不是对方，而是你这孽障」（P037）。全文以第二人称「你」直接对父母／恋人进言。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "把问题的根子前移到离婚之前。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P003", "P004"], "summary": "指认现代父母与恋人的「悄没声的狂妄自大」：理所当然地自认为有爱、把正在做的事认定为毫无疑问的爱的表现，并极其轻易地做「永远」的保证，最经典的是「爸爸/妈妈/我永远爱你」。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P005"], "summary": "反问：把这话挂在嘴边，此时能不愁怎么做「心理建设」吗？", "role": "transition"},
    {"unit_id": "U004", "paragraph_refs": ["P006", "P007"], "summary": "给「做心理建设」下判断：本质上就是「如何圆场」，并列举要圆的四类问题（原承诺为何失效、父母间承诺失效为何不等于亲子承诺失效、爱是什么、为何爱我却不能阻止你另娶／嫁）。", "role": "definition"},
    {"unit_id": "U005", "paragraph_refs": ["P008", "P009"], "summary": "预判圆不回来：因为一开始只是无知而无畏、敢于盗用爱的名义；如今已知道当初的承诺基于对爱极为傲慢而粗陋的定义，却不敢跟子女实话实说。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P010"], "summary": "以反证否定「心理建设」的效力：若它可行，世界上还会有「爱」这个概念存在吗？应该只剩下「心理建设大全」了。", "role": "rebuttal"},
    {"unit_id": "U007", "paragraph_refs": ["P011", "P012", "P013", "P014"], "summary": "给出应做的第一步：老实承认自己并不懂爱是什么，只是空有一腔爱欲；只有「永远对ta好」的欲望，却不知其何时会失控消失，也不知经自己简单、不周、有限的实施是否真的对对方有益；作者声明这是实情，没有贬低、没有 sugar coating。", "role": "action_advice"},
    {"unit_id": "U008", "paragraph_refs": ["P015", "P016"], "summary": "把该实情推广到父母与恋人两种身份：深爱子女、深爱对方，爱的实情也不过如此。", "role": "reason"},
    {"unit_id": "U009", "paragraph_refs": ["P017", "P018"], "summary": "由实情推出资格的否定：没有资格「承诺永远」，只能希望做到永远；没有资格自称对人好，只能希望所做的不是全然损失、多少有所帮助。", "role": "conclusion"},
    {"unit_id": "U010", "paragraph_refs": ["P019"], "summary": "行动要求：先承认之前的狂妄，忏悔自己的无知与傲慢，以及无意识的、甚至自欺欺人的、因而本质是明知故犯的欺骗。", "role": "action_advice"},
    {"unit_id": "U011", "paragraph_refs": ["P020", "P021"], "summary": "行动要求：重新表述打算为对方所做的，给对方最坏的、但却是确实的、人可以行的消息；对方会受重击、失望、痛苦，但到最后至少可以踏实。", "role": "action_advice"},
    {"unit_id": "U012", "paragraph_refs": ["P022", "P023", "P024"], "summary": "以反问否定继续修补的可能：靠甜蜜狂言编织的朝不保夕的「幸福感」「安全感」原本就要靠自欺欺人送服，如今已被撕破，不能再指望用「心理建设」让对方继续相信「永远爱」「不会变」；并以反问指其逻辑荒谬。", "role": "rebuttal"},
    {"unit_id": "U013", "paragraph_refs": ["P025"], "summary": "正面主张：爱只有一种可行的做法——深明人的局限和笨拙，只说盼望、只说努力，永远不说那虚假的、人根本没有能力做出的「承诺」。", "role": "claim"},
    {"unit_id": "U014", "paragraph_refs": ["P026", "P027", "P028"], "summary": "指出后果链与归因：没有资格承诺却贪了、选了、承诺了，于是「信用」垮台；再打算帮目击证人做「心理建设」、重新竖起已垮台的谎言并不现实。", "role": "reason"},
    {"unit_id": "U015", "paragraph_refs": ["P029", "P030", "P031", "P032", "P033"], "summary": "以排比方式界定爱：爱不是承诺永远、一定、保证；爱是自知不能、尽力而为；爱是帮助对方不必依赖自己的永远、一定和保证；我不能保证自己永远存在或好意长存，所以要帮助对方无惧于此；爱一个人不是让 ta 相信你会永远爱 ta，而是让 ta 不再害怕你会不爱 ta。", "role": "definition"},
    {"unit_id": "U016", "paragraph_refs": ["P034", "P035", "P036"], "summary": "指出两种做法的关系：想清楚两者区别；做到后一条的人会顺便获得前一条；只做前一条、甚至想避免后一条的人，连前一条也是假的。", "role": "conclusion"},
    {"unit_id": "U017", "paragraph_refs": ["P037"], "summary": "反转受力方：需要「心理建设」的不是对方，而是父母自己（作者用「孽障」指称）。", "role": "claim"},
    {"unit_id": "U018", "paragraph_refs": ["P038", "P039"], "summary": "以条件句收尾：若关系一开始就建立在这一基础认识和实践之上，会发现它牢固、正面得多，不易出现难以挽回的问题；其次即便出现问题，到了所问的关头，子女也并不需要多少「心理建设」。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这个问题的根子很远，远在没有离婚之前。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "现代的父母们、恋人们有一种悄没声的狂妄自大：胆敢理所当然地自认为自己有爱，敢于把现在在做的事情认定为毫无疑问的爱的表现，而且极其轻易地做「永远」的保证。", "evidence": ["E2", "E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "把「爸爸/妈妈/我永远爱你」这类话挂在嘴边，就难免要愁怎么做「心理建设」；而所谓「做心理建设」本质上就是「如何圆场」。", "evidence": ["E4", "E5"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "你将很难把那些问题圆回来，因为一开始你就的确只不过是无知而无畏，敢于盗用爱的名义罢了。", "evidence": ["E6"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "你现在已经知道之前对子女所做的爱的承诺是基于一个对爱极为傲慢而粗陋的定义，却不敢跟孩子实话实说。", "evidence": ["E7"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "用奇妙的「心理建设」来解决问题，如果可行的话，世界上就不会还有「爱」这个概念，应该只剩下「心理建设大全」。", "evidence": ["E8"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "你首先应该做的是老老实实承认自己并不懂爱是什么，只是空有一腔爱欲；你只有「永远对ta好」的欲望，却不清楚这欲望何时会不受控制地消失，也不知道经你头脑简单、思虑不周、能力有限的实施是否真的对ta有益。", "evidence": ["E9", "E10"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作为父母深爱子女、作为爱人深爱对方，其爱的实情也不过就是如此（即只是爱欲与不确定的欲望）。", "evidence": ["E11"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "你没有资格「承诺永远」，只能希望可以做到永远；你没有资格自称对人好，只能希望你所做的对人不是全然的损失、多少有所帮助。", "evidence": ["E12", "E13"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "你首先需要承认你之前的狂妄，要忏悔自己的无知和傲慢，以及无意识的——甚至自欺欺人的、因而本质是明知故犯的欺骗。", "evidence": ["E14"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "你应重新表述打算为对方所做的，给对方最坏的、但却是确实的、人可以行的消息；对方会受重击、失望、痛苦，但到最后至少可以踏实。", "evidence": ["E15", "E16"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "靠甜蜜诱人的狂言大语编织出来的朝不保夕、游移不定的「幸福感」「安全感」，原本就让人每天都要用自欺欺人来送服，如今已被撕破，不能再指望用「心理建设」让对方继续相信「永远爱」「不会变」。", "evidence": ["E17", "E18"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "爱只有一种可行的做法，就是深明人的局限和笨拙，只说盼望、只说努力，永远不说那该死的、虚假的、人根本没有能力做出的「承诺」。", "evidence": ["E19"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "「承诺」了似乎就可以得到这个那个，但人并没有资格「承诺」；那些没有「承诺」就「没有安全感」的人本来就还是饥不择食的小孩子，甚至不应被视为可以选择的选项。", "evidence": ["E20"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "因为你贪了、选了、「承诺」了，然后你的「信用」垮台了；再打算帮目击证人「做好心理建设」、重新竖起已经垮台的谎言，这并不现实。", "evidence": ["E21", "E22"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "爱不是去承诺什么永远、一定、保证；爱是自知不能，尽力而为；爱是帮助对方不必依赖于自己的「永远」「一定」和「保证」。", "evidence": ["E23", "E24", "E25"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "我不能保证我永远存在或者好意长存，所以我要帮助对方无惧于自己可能不再存在或好意不存的影响。", "evidence": ["E26"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "爱一个人，不是要去让这人相信你会永远爱ta，而是要让这人不再害怕你会不爱ta。", "evidence": ["E27"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "做到后一条的人会顺便获得前一条；只做前一条、甚至想避免后一条的人，连前一条也是假的。", "evidence": ["E28", "E29"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "需要「心理建设」的不是对方，而是父母自己。", "evidence": ["E30"]},
    {"claim_id": "C021", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "如果一开始就在这个基础认识和实践之上建立关系，首先会发现那牢固、正面得多，因此不容易出现难以挽回的问题；其次即使出现了问题，到了这个问题所问的关头，子女也并不需要多少「心理建设」。", "evidence": ["E31", "E32"]}
   ],
   "argument_steps": [
    "把问题根子前移到离婚之前（P001）。",
    "指认父母／恋人的狂妄：自认有爱、把当下行为当作爱的表现、轻易做「永远」的保证（P002–P004）。",
    "反问点出「心理建设」之愁的来源（P005）。",
    "定义「做心理建设」＝如何圆场，并列四类需圆的问题（P006–P007）。",
    "预判圆不回来，归因于无知无畏、盗用爱的名义；并指出如今知情却不敢实说（P008–P009）。",
    "反证否定其效力：若可行则「爱」这个概念不会存在（P010）。",
    "给出第一步：承认不懂爱、只有爱欲，且欲望与实施皆不可控（P011–P014）。",
    "推广到父母与恋人两种身份（P015–P016）。",
    "推出资格否定：无资格承诺永远、无资格自称对人好（P017–P018）。",
    "要求承认狂妄并忏悔（P019）。",
    "要求重新表述、给出最坏但确实的消息，使对方至少踏实（P020–P021）。",
    "反问否定修补旧谎言的可能（P022–P024）。",
    "提出正面主张：只说盼望与努力，永不做承诺（P025）。",
    "指出贪、选、承诺导致信用垮台，补做心理建设不现实（P026–P028）。",
    "排比界定爱（P029–P033）。",
    "说明两种做法的关系：做后一条兼得前一条，只做前一条则前一条也是假的（P034–P036）。",
    "反转：需要心理建设的是父母自己（P037）。",
    "以条件句收尾：如此建立关系更牢固，子女也不需要多少心理建设（P038–P039）。"
   ],
   "concept_usage": [
    {"term": "心理建设", "meaning": "提问者所用的说法；作者把它解释为「如何圆场」，即给已失效的「永远」承诺打补丁，并在结尾称真正需要它的是父母自己。", "evidence": "P006", "ambiguity": "作者未讨论心理学意义上「心理建设」的其他含义。"},
    {"term": "「永远」的保证／「承诺」", "meaning": "父母或恋人对子女／对方所做的永远爱、永远好、不会变的保证；作者称人没有资格做出，只能希望与努力。", "evidence": "P017", "ambiguity": "文中「保证」「承诺」与「永远」常连用，边界未细分。"},
    {"term": "爱欲", "meaning": "与「爱」相对的用语：空有一腔爱欲，只有「永远对ta好」的欲望，而不知其何时失控消失、实施是否有益。", "evidence": "P011", "ambiguity": "本文以否定式与排比句谈「爱」，未给正面定义，爱与爱欲的界限未系统说明。"},
    {"term": "sugar coating", "meaning": "英文短语，指粉饰；作者声明所述实情没有一分一毫的贬低，也没有一分一毫的 sugar coating。", "evidence": "P013", "ambiguity": "本文未展开。"},
    {"term": "踏实", "meaning": "给出最坏但确实的消息后对方至少可以获得的状态，与靠狂言大语编织的「安全感」相对。", "evidence": "P021", "ambiguity": "本文未说明「踏实」的判准。"},
    {"term": "饥不择食的小孩子", "meaning": "作者对「没有『承诺』就『没有安全感』」者的定性，称其不应被视为可以选择的选项。", "evidence": "P026", "ambiguity": "属作者的贬抑性修辞，未给出判定标准。"},
    {"term": "孽障", "meaning": "训诫性用语，作者以此指称提问者一类父母，称真正需要「心理建设」的是他们。", "evidence": "P037", "ambiguity": "属修辞性指称，非事实判断。"}
   ],
   "examples_and_targets": [
    "「爸爸/妈妈/我永远爱你」——作者举为最经典的「永远」保证（P004），其说话者为作者概括的一类父母／恋人，未指名。",
    "四类需「圆场」的问题：原承诺为何失效、父母间承诺失效为何不等于亲子承诺失效、爱是什么、为何爱我却不能按我的意愿不另娶／嫁（P007）——作者的概括性列举。",
    "「恨不得能把心掏出来送给对方当卤煮」——作者的夸张比喻（P016）。",
    "「目击证人」——作者对子女的比喻性称呼（P028），所指依赖上下文推断。",
    "「心理建设大全」——作者的讽刺性假设物（P010）。",
    "重组家庭与离婚——提问语境（Q001、P001）；作者未讨论继父母关系、抚养安排、告知时机等具体问题。"
   ],
   "conditions": [
    "「如果你一开始就是在这个基础认识和实践之上建立的关系」——结尾第一个结论的条件（P038）。",
    "「即使出现了问题，到了这个问题所问的关头」——结尾第二个结论的条件（P039）。",
    "「你只能希望可以做到永远」「你只能希望你所做的对人不是全然的损失」——把承诺改写为希望的限定（P017、P018）。",
    "「如果可行的话」——对「心理建设」效力的反证以假设其可行为前提（P010）。",
    "作者自陈语气边界：「没有一分一毫的贬低你，也没有一分一毫的sugar coating」（P013）。",
    "全文以第二人称「你」指向提问者（打算重组家庭的父母／恋人），未区分继子女、生父母等不同关系位置。"
   ],
   "rhetoric_and_tone": "第二人称「你」的训诫式议论，语气严厉直接（结尾称对方为「你这孽障」）；以反问推进（「这个时候能不愁怎么做“心理建设”吗？」「世界上还会有“爱”这个概念存在吗？」「你没感受到这逻辑上是荒谬的吗？」）；用「最坏的、但是却是确实的、人可以行的消息」这类对照句式下定义；口语化夸张（「恨不得能把心掏出来送给对方当卤煮」）；结尾以「爱是……」排比句收束，并声明所述实情没有贬低、没有粉饰。",
   "unresolved_questions": [
    "提问所问的「重组家庭／再婚」情境在正文中未被直接处理：作者把根子移到离婚之前的「永远」承诺（P001），未讨论继父母关系、子女安置、告知时机等具体问题。",
    "「爱」在本文中只以否定式（不是承诺永远、一定、保证）与排比句（自知不能、尽力而为）界定，未给正面定义；「爱」与「爱欲」的界限亦未系统说明。",
    "「爸爸/妈妈/我永远爱你」的说话者未指名，是作者概括的常见说法还是提问者原话不明。",
    "P028「你打算帮目击证人“做好心理建设”」中「目击证人」的所指（子女？）依赖上下文推断，本文未明说。",
    "P037 以「孽障」指称对方属训诫性修辞，不构成事实主张，其归属与语气需研究者复核。",
    "updated_at=2026-04-18 远晚于 published_at=2021-01-15，语料未提供版本差异或修订说明，是否存在后续改动无法判定。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "这个问题的根子很远，远在没有离婚之前。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "有一种悄没声的狂妄自大，就是胆敢理所当然的自认为自己有爱", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "而且极其轻易的做“永远”的保证。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P005", "quote": "说了这话，而且挂在嘴边，这个时候能不愁怎么做“心理建设”吗？", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P006", "quote": "所谓“做心理建设”，本质上不就是“如何圆场”的意思吗？", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P008", "quote": "因为一开始你就的确只不过是无知而无畏，敢于盗用爱的名义罢了。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P009", "quote": "你已经知道之前对子女所做的爱的承诺是基于一个对于爱的极为傲慢而粗陋的定义了，你却不敢跟ta们实话实说。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P010", "quote": "用奇妙的“心理建设”来解决问题，如果可行的话，世界上还会有“爱”这个概念存在吗？", "relation": "contradicts"},
    {"key": "E9", "paragraph_id": "P011", "quote": "是老老实实的承认自己并不懂爱是什么，只是空有一腔爱欲。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P012", "quote": "你只是有“永远对ta好”的欲望，但你不清楚这个欲望何时会不受你控制的消失", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P015", "quote": "你是父母，深爱你的子女，你对ta的爱实情也是如此。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P017", "quote": "你没有资格“承诺永远”。你只能希望可以做到永远。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P018", "quote": "你没有资格自称对人好，你只能希望你所做的对人不是全然的损失，多少有所帮助。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P019", "quote": "你首先需要承认你之前的狂妄，要忏悔自己的无知和傲慢", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P020", "quote": "给对方最坏的、但是却是确实的、人可以行的消息。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P021", "quote": "但是到最后，对方至少可以踏实。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P022", "quote": "原本就让人每天都要用自欺欺人来送服", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P023", "quote": "还能指望用“心理建设”继续让对方继续相信你“永远爱”“不会变”吗？", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P025", "quote": "爱只有一种可行的做法，就是深明人的局限和笨拙，只说盼望、只说努力", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P026", "quote": "本来就还是饥不择食的小孩子而已，你甚至都不应该视其为可以选择的选项。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P027", "quote": "但是你贪了，你选了，你“承诺”了，然后你的“信用”垮台了。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P028", "quote": "重新竖起已经垮台的谎言，你想想，这现实吗？", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P029", "quote": "爱不是去承诺什么永远、一定、保证。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P030", "quote": "爱是自知不能，尽力而为；", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P031", "quote": "爱是帮助对方不必依赖于自己的“永远”“一定”和“保证”。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P032", "quote": "我不能保证我永远存在或者好意长存", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P033", "quote": "而是要让这人不再害怕你会不爱ta。", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P035", "quote": "做到后一条的人，会顺便获得前一条。", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P036", "quote": "只做前一条，甚至想避免后一条的人，连前一条也是假的。", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P037", "quote": "需要“心理建设”的不是对方，而是你这孽障。", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P038", "quote": "首先你会发现那牢固、正面得多，因此不容易出现难以挽回的问题。", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P039", "quote": "子女也并不需要多少“心理建设”。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["家庭伦理／亲子关系", "婚恋与承诺", "伦理学（爱的界定）", "言语与诚实"],
   "issue_candidates": ["重组家庭中的心理建设", "「永远爱你」式承诺的正当性", "父母向子女说实话", "爱与承诺、安全感的关系"],
   "text_function_candidates": ["答疑", "批评／训诫", "论辩", "伦理劝导"],
   "object_candidates": ["提问者（打算重组家庭的父母）", "子女", "现代的父母们与恋人们", "目击证人（喻指子女）"],
   "working_keywords": ["心理建设", "圆场", "永远", "承诺", "爱欲", "实情", "sugar coating", "安全感", "踏实", "孽障"]
  },
  "notes": "本篇无图片节点（图片节点 0），正文 39 段全部读完，按默认 status=read、full_text_checked=true 处理。brief 在句中被截断（止于「说了这话，而」），仅作导航，未用于支持任何主张。提问者要的是「父母需要给孩子做什么心理建设」，作者不接受该问法：把「心理建设」解释为「如何圆场」（P006），并在结尾称真正需要「心理建设」的是父母自己（P037）；提问中的重组家庭／再婚具体情境未被直接处理，已登记未决问题。P028「目击证人」所指依赖上下文推断。updated_at（2026-04-18）远晚于 published_at（2021-01-15），语料未提供版本差异说明。"
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
