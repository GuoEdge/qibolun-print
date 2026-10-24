# -*- coding: utf-8 -*-
"""批次 r001-b0013 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0013.sessions.py            # 写 out/r001-b0013.out.jsonl
  python3 records/r001-b0013.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0013"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0013.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "115363db": {
  "analysis": {
   "question_context": "提问者（Q001）问“为什么部分北方人喜欢生吃蔬菜？”。作者（自称东北人）以历史条件作答：东北现代移民史短、人口密度小、气候寒冷，病菌繁殖慢，因此缺少大疫的社会记忆，并认为生吃习惯来自成本与数量，而非“东北菜好吃”。P010、P025 是评论区他人的反驳（提问者一方），作者在 P011—P024、P026—P032 逐条回应；两段属提问者一方，不得归给作者。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "用反事实设想说明：若祖辈反复经历大疫，后代自然会学会不生吃。", "role": "reason"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005", "P006"], "summary": "反驳“东北菜好吃”说；认为该说低估南方物产，也解释不了南方人不生吃。", "role": "rebuttal"},
    {"unit_id": "U003", "paragraph_refs": ["P007", "P008", "P009"], "summary": "提出习惯形成取决于成本与数量；生吃省燃料，不生吃必有不占便宜的理由。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P010"], "summary": "对手反驳：家中有取暖火可顺带煮熟菜，谈不上节约燃料，且当时东北经济条件更好。", "role": "rebuttal"},
    {"unit_id": "U005", "paragraph_refs": ["P011"], "summary": "回应：对方家非土生土长东北人，与习惯形成关联不大。", "role": "rebuttal"},
    {"unit_id": "U006", "paragraph_refs": ["P012", "P013", "P014", "P015", "P016", "P017", "P018", "P019", "P020"], "summary": "用燃料的稀缺性反驳“顺带煮熟”：冬无蔬菜、砍柴极费力、火炕保温优先于做饭、大锅灶是为省火。", "role": "rebuttal"},
    {"unit_id": "U007", "paragraph_refs": ["P021", "P022", "P023"], "summary": "以海西女真为例说明极度匮乏下的选择；并以亲自过冬的设想要求对方体会。", "role": "example"},
    {"unit_id": "U008", "paragraph_refs": ["P024"], "summary": "称生吃是本土世代常识与文化下意识，新东北人只是继承习惯并自选理由。", "role": "conclusion"},
    {"unit_id": "U009", "paragraph_refs": ["P025"], "summary": "对手再驳：今天东北人不仅生吃而且“喜欢”，不能用吃惯了解释，习惯可被科学与健康观念取代。", "role": "rebuttal"},
    {"unit_id": "U010", "paragraph_refs": ["P026", "P027", "P028"], "summary": "回应称这是学术范式问题，类比北京豆汁；指对方结论与论证无可靠关联。", "role": "rebuttal"},
    {"unit_id": "U011", "paragraph_refs": ["P029", "P030", "P031"], "summary": "以生牛柳鸡蛋、皮蛋为例说明原料可得不等于会吃；称食俗形成机制远比直观想象复杂。", "role": "reason"},
    {"unit_id": "U012", "paragraph_refs": ["P032"], "summary": "收束：有东西在人们之前就决定了口味偏好。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "东北现代移民历史短、人口密度小、气候寒冷使病菌繁殖慢，因而缺少大规模高致死性流行病的社会记忆。", "evidence": ["E001", "E002"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "若祖辈反复目睹整村死亡，其子孙自然会学会不生吃蔬菜。", "evidence": ["E003"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "“东北人生吃菜是因为东北菜好吃”的说法有根本性的逻辑错误。", "evidence": ["E004"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "“北方菜更好吃”解释不了南方人为何不生吃，也解释不了北方人为何愿意生吃。", "evidence": ["E005"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "饮食习惯的形成基本与味道口感无关，只与成本和数量有关。", "evidence": ["E006", "E007"]},
    {"claim_id": "C006", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "只要可以选择，人一定会选择成本上有优势的生吃。", "evidence": ["E008"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "不生吃必然存在让人不敢占这个便宜的理由。", "evidence": ["E009"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "对方的家庭并非土生土长东北人，因而与当地饮食习惯的形成关联不大。", "evidence": ["E010"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "在现代农业技术之前，东北的冬天没有蔬菜。", "evidence": ["E011"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "冬天燃料靠人力砍柴积蓄，聚居点附近的柴早被砍光。", "evidence": ["E012", "E013"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "火车出现之前与城市之外都没有煤可烧。", "evidence": ["E014"]},
    {"claim_id": "C012", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "当时做不到全屋暖洋洋而有过剩燃料做饭；用麻烦的火炕而非壁炉可资证明。", "evidence": ["E015", "E016"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "当时的活法是尽量省着烧、保火炕不灭，炕火不足以随随便便做饭。", "evidence": ["E017"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "当时用大锅加盖、垛笼屉一次做多样饭食，目的就是少费火。", "evidence": ["E018"]},
    {"claim_id": "C015", "claim_type": "author_reported", "attribution": "author", "modality": "asserted", "statement": "海西女真几乎生吃一切，因北至黑龙江后人力已无力同时解决取暖与饮食。", "evidence": ["E019", "E020"]},
    {"claim_id": "C016", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "当地种植所耗热量使产出不足以支撑日常消耗，故只能以人参貂皮换粮或驱奴耕种。", "evidence": ["E021"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "生吃是东北本土人世世代代的常识与文化底层的下意识。", "evidence": ["E022"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "后代新东北人并不明白这些习惯的根源，只是自己选择了最喜欢的理由。", "evidence": ["E023"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对话双方的分歧属于学术范式问题。", "evidence": ["E024"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "对方的结论与其逻辑论证之间不存在可靠关联。", "evidence": ["E025"]},
    {"claim_id": "C021", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "以生牛柳生鸡蛋为例反问：东北不缺原料，为何东北人不爱吃。", "evidence": ["E026"]},
    {"claim_id": "C022", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "以美国人不吃皮蛋反问：当地不缺原料，为何仍不吃。", "evidence": ["E027"]},
    {"claim_id": "C023", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "食俗习惯的形成机制远比直观想象复杂，本地年轻一代自认的原因未必是真的原因。", "evidence": ["E028"]},
    {"claim_id": "C024", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "有东西在人们之前就决定了喜欢什么、不碰什么。", "evidence": ["E029"]},
    {"claim_id": "C025", "claim_type": "opponent_view", "attribution": "opponent", "modality": "asserted", "statement": "对手称：取暖火一直烧着，烧水做饭不过利用现成火力，谈不上节约燃料成本，犯不着吃可能致病的生菜。", "evidence": ["E030", "E031"]},
    {"claim_id": "C026", "claim_type": "opponent_view", "attribution": "opponent", "modality": "asserted", "statement": "对手称：几十年前东北是经济条件最好、支援他省的时候，南方条件不比东北更好。", "evidence": ["E032"]},
    {"claim_id": "C027", "claim_type": "opponent_view", "attribution": "opponent", "modality": "questioned", "statement": "对手追问“喜欢”二字：今天东北人依然喜欢生吃，不能用吃惯了不得不接受来解释，且老一代习惯会被科学与健康观念取代。", "evidence": ["E033", "E034"]},
    {"claim_id": "C028", "claim_type": "opponent_view", "attribution": "opponent", "modality": "qualified", "statement": "对手承认：若指女真、宁古塔流放那个时代，作者的逻辑可能是正确的。", "evidence": ["E035"]}
   ],
   "argument_steps": [
    "反事实前提：若东北祖辈反复经历大规模瘟疫，后代自会学会不生吃（P001—P003）。",
    "排除流行解释：东北菜好吃说低估南方物产，且解释不了南方人不生吃、北方人愿生吃（P004—P006）。",
    "提出替代解释：习惯形成与味道无关，只与成本数量有关；生吃省燃料，不生吃必有不敢占便宜的理由（P007—P009）。",
    "对手反驳：取暖火可顺带煮菜、当时东北经济更好（P010）。",
    "回应：对方非土生土长东北人（P011）→ 冬无蔬菜（P012）→ 砍柴艰难、无煤可烧（P014—P017）→ 火炕设计证明无过剩燃料（P018—P019）→ 大锅灶为省火（P020）。",
    "极端例证与体验要求：海西女真生食、种地不合算、亲自过冬（P021—P023）。",
    "结论：习惯是文化下意识，新东北人只是继承并自选理由（P024）。",
    "对手再驳“喜欢”与时代变化（P025）。",
    "回应：范式问题（P026）→ 豆汁类比（P027）→ 结论与论证无关（P028）→ 反例反问（P029—P030）→ 机制复杂、偏好先于自觉（P031—P032）。"
   ],
   "concept_usage": [
    {"term": "社会记忆", "meaning": "由世代反复经历大疫形成的集体经验，会使后代形成不生吃的习惯", "evidence": "P001", "ambiguity": "作者以反事实设想表达，非实证结论"},
    {"term": "成本", "meaning": "获取和处理食物所耗的燃料等代价；作者认为它决定饮食方式", "evidence": "P007", "ambiguity": "未界定除燃料外的成本范围"},
    {"term": "美味", "meaning": "各地人对可获得食物发展出的味觉审美，而非绝对普遍标准", "evidence": "P006", "ambiguity": "作者否定存在绝对美味标准"},
    {"term": "火炕", "meaning": "费工但省燃料的取暖设计，被作者用作燃料不宽裕的证据", "evidence": "P018", "ambiguity": "未给出具体耗柴数据"},
    {"term": "学术范式", "meaning": "作者用于指称双方分歧属于研究范式层面的差异", "evidence": "P026", "ambiguity": "仅一句话，未展开何为范式差异"},
    {"term": "文化意识底层", "meaning": "烙进文化、被后代无意识继承的习惯层面", "evidence": "P024", "ambiguity": "属比喻性表述"}
   ],
   "examples_and_targets": [
    "四十年前中国人不会因味道不好就不吃（作者论据，P007）",
    "对方的多条评论（P010、P025）：被反驳对象，非作者立场",
    "东北冬天的蔬菜与燃料（作者论据，P012—P019）",
    "海西女真几乎生吃一切（作者引用的历史例证，P021）",
    "高丽参、貂皮换粮食与驱奴耕种（作者论据，P022）",
    "生鸡蛋拌腌生牛柳与意大利人（作者设问的反例，P029）",
    "美国人不吃皮蛋（作者设问的反例，P030）",
    "北京人爱喝豆汁（作者类比，用于质疑对方论证方式，P027）"
   ],
   "conditions": [
    "以“东北现代移民历史太短、人口密度小、气候寒冷”为前提（P001）",
    "“即使假设北方蔬菜比南方好吃”的让步假设（P006）",
    "“只要可以选择，一定会选择”的条件限定（P008）",
    "以“在现代农业技术之前”限定冬天没有蔬菜（P012）",
    "以“火车没出现之前”“城市之外”限定无煤可烧（P016）",
    "以对手提出的条件推演“如果东北蔬菜不能生吃，就着取暖的火烧锅开水把菜扔里煮熟就行了”为反驳对象（P010）",
    "以“如果是那样”假设全壁炉的推论（P018）",
    "用“那时候的供应水平”限定活法（P019）",
    "以自身家庭经历（爷爷迁来东北、父亲出生城里）为前提的对手论证（P010）"
   ],
   "rhetoric_and_tone": "论战式、训诫式语气，夹杂“你就并不是”“你算算看”等第二人称质问与反问；用砍柴、火炕、大锅灶等具体场景增强说服力；对手在 P010 开头先行致歉，作者回应时仍称其家庭属于“新东北人”、并把双方分歧称为“学术范式问题”，带明显贬抑；结尾以两组反问（生牛柳鸡蛋、美国人吃皮蛋）与 heading 收束。",
   "unresolved_questions": [
    "“全村人死掉三分之一”“村村燃起焚烧尸骨的黑烟经月不灭”等具体描述属史料还是修辞夸张，需外部核查（P002）",
    "海西女真“几乎生吃一切”、驱奴耕种“等效于吃人”等历史叙述需外部核查（P021、P022）",
    "P010、P025 来自评论区的对手发言，其身份与发言完整性仅由转录决定，无法独立核验",
    "作者称对方“并不是土生土长东北人”的依据仅来自对方自述，未进一步核实（P011）",
    "文章 updated_at 为 2025-05-10，晚于发表时间，是否存在增补或删改，本文未说明",
    "brief 与正文前段文字重合，brief 后续内容未在正文出现，差异原因未说明"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P001", "quote": "因为东北现代移民历史太短，历史上人口密度太小而且气候寒冷，病菌繁殖分裂缓慢", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P001", "quote": "因此缺少大规模高致死性流行病的社会记忆", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P003", "quote": "他们的子孙自然会学会不生吃蔬菜", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P004", "quote": "这个说法有根本性的逻辑错误", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P006", "quote": "解释不了“为什么南方人不生吃”", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P007", "quote": "饮食习惯的形成，基本与味道口感无关，只与成本和数量有关", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P007", "quote": "只要能吃，哪有“不好吃”一说？", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P008", "quote": "在成本上明显有优势。只要可以选择，一定会选择。", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P009", "quote": "自然是有肯定不敢占这便宜的理由", "relation": "supports"},
    {"key": "E010", "paragraph_id": "P011", "quote": "那么你们家就并不是土生土长东北人，对形成饮食习惯并没有多少关联", "relation": "supports"},
    {"key": "E011", "paragraph_id": "P012", "quote": "在现代农业技术之前，东北的冬天没有蔬菜", "relation": "supports"},
    {"key": "E012", "paragraph_id": "P014", "quote": "冬天的燃料全靠人力砍柴来积蓄", "relation": "supports"},
    {"key": "E013", "paragraph_id": "P014", "quote": "能砍的十年前就让本村的人砍光了", "relation": "supports"},
    {"key": "E014", "paragraph_id": "P016", "quote": "火车没出现之前，哪有人烧煤？城市之外，哪有人烧煤？", "relation": "supports"},
    {"key": "E015", "paragraph_id": "P018", "quote": "那时候根本就做不到全屋暖洋洋以至于有过剩的燃料拿来做饭", "relation": "supports"},
    {"key": "E016", "paragraph_id": "P018", "quote": "舍弃壁炉这种明显低技术的手段却用火炕这么麻烦的设计，为什么？", "relation": "supports"},
    {"key": "E017", "paragraph_id": "P019", "quote": "尽可能省着烧，维持火炕不灭", "relation": "supports"},
    {"key": "E018", "paragraph_id": "P020", "quote": "一口气做好？为什么这样做饭？为了少费火。", "relation": "supports"},
    {"key": "E019", "paragraph_id": "P021", "quote": "茹毛饮血的海西女真干脆几乎生吃一切", "relation": "supports"},
    {"key": "E020", "paragraph_id": "P021", "quote": "靠人力已经无力同时解决取暖问题和饮食问题了", "relation": "supports"},
    {"key": "E021", "paragraph_id": "P022", "quote": "那点输入都不够他们日常消耗", "relation": "supports"},
    {"key": "E022", "paragraph_id": "P024", "quote": "那是东北本土人世世代代的常识，是烙进文化意识底层的下意识", "relation": "supports"},
    {"key": "E023", "paragraph_id": "P024", "quote": "于是自己选择了自己最喜欢的理由而已", "relation": "supports"},
    {"key": "E024", "paragraph_id": "P026", "quote": "你这就是学术范式问题了", "relation": "supports"},
    {"key": "E025", "paragraph_id": "P028", "quote": "你的结论和你的逻辑论证之间不存在可靠关联", "relation": "supports"},
    {"key": "E026", "paragraph_id": "P029", "quote": "东北不产牛还是不产鸡蛋？还是这两样难吃？还是这两样稀有？东北人为什么不爱吃？", "relation": "supports"},
    {"key": "E027", "paragraph_id": "P030", "quote": "他们当地要生产这个是缺什么原料？他们为什么不吃？", "relation": "supports"},
    {"key": "E028", "paragraph_id": "P031", "quote": "食俗习惯的形成机制远远复杂过你的直观想象", "relation": "supports"},
    {"key": "E029", "paragraph_id": "P032", "quote": "有东西在你之前决定了你喜欢什么不喜欢什么", "relation": "supports"},
    {"key": "E030", "paragraph_id": "P010", "quote": "我认为谈不上节约燃料成本", "relation": "context"},
    {"key": "E031", "paragraph_id": "P010", "quote": "犯不着一边烤着火炉取暖一边吃口感味道不好还可能导致生病的生菜", "relation": "context"},
    {"key": "E032", "paragraph_id": "P010", "quote": "我不觉得南方条件会比东北更好", "relation": "context"},
    {"key": "E033", "paragraph_id": "P025", "quote": "看到“喜欢”二字了吗？", "relation": "context"},
    {"key": "E034", "paragraph_id": "P025", "quote": "老一代人坚持的坐月子方法，在我们这一代被科学坐月子所取代", "relation": "context"},
    {"key": "E035", "paragraph_id": "P025", "quote": "如果是那个时代，我承认你说的可能是正确的", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["饮食文化", "东北地方史", "公共卫生史", "文化解释"],
   "issue_candidates": ["生吃蔬菜的习惯成因", "饮食习惯与成本/味道的关系", "地域刻板印象的解释方式", "评论区的争论与范式分歧"],
   "text_function_candidates": ["答疑", "论辩", "反驳回应", "经验总结"],
   "object_candidates": ["东北", "南方", "海西女真", "黑龙江", "意大利", "美国", "北京", "四十年前的中国"],
   "working_keywords": ["生吃", "社会记忆", "成本和数量", "火炕", "壁炉", "大锅灶", "学术范式"]
  },
  "notes": "P010、P025 为评论区他人（提问者一方）发言，已按 opponent/context 处理，未归给作者；P010、P025 因单段超过 300 字被生成器截断转录（sample_truncated），本记录短引均取自截断前片段。brief 的末句被截断（“不生吃蔬”），正文前两段与 brief 重合但 brief 更长，差异原因本文未说明。"
 },
 "ec826fb4": {
  "analysis": {
   "question_context": "提问者（Q001）问“用‘能力不足’为人与人之间的矛盾归因，正确吗？”。作者开头即答“这个归因是正确的”，并用层层假设（他人无限满足我的愿望、我无需他人、我能原谅）说明矛盾源于能力不足；末句“是尼采错了”把结论指向对尼采的回应，但正文未说明尼采的哪一说法，也未引用原文。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "谢邀并直接给出判断：该归因正确，是万能归因法。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005", "P006", "P007"], "summary": "用摘星、月亮、太阳、银河的递进假设说明：若对方有无限满足愿望的能力，就永远没有矛盾；可惜人没有这种能力。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P008", "P009", "P010", "P011", "P012", "P013"], "summary": "反过来假设“我不要”：能不要、能自己打赢、有无限财富、对一切人无所求都无矛盾；可惜人没有无欲无求的能力。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P014", "P015", "P016", "P017", "P018", "P019", "P020", "P021", "P022"], "summary": "再假设“我原谅”：对父母、朋友、教师的欠缺都原谅；但对方是否也原谅我？不原谅的不原谅能否被原谅？可惜人也缺少原谅的能力。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P023", "P024"], "summary": "归纳三种能力不足（不需求、满足需求、原谅），称一切人类矛盾的根源都来自这三种不足。", "role": "conclusion"},
    {"unit_id": "U006", "paragraph_refs": ["P025", "P026"], "summary": "收尾：所以提问者没有说错，是尼采错了。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "用“能力不足”为矛盾归因是正确的，这是一种万能归因法。", "evidence": ["E001"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "若对方有无限达成自己愿望的能力，双方就不会有矛盾。", "evidence": ["E002", "E003"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "人没有无限的达成他人愿望的能力。", "evidence": ["E004"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "若自己没有需求、能自己解决或对一切人无所求，他人不满足自己也不会构成矛盾。", "evidence": ["E005", "E006"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "人没有无欲无求的能力。", "evidence": ["E007"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "若我能体谅原谅对方的不能满足，就不会有矛盾。", "evidence": ["E008"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "以反问指出原谅的单向性：我原谅你，你却不原谅我，我能否原谅你的不原谅。", "evidence": ["E009", "E010"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "人类也缺少原谅的能力。", "evidence": ["E011"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "一切人类矛盾的根源都是来自不需求、满足需求、原谅这三种能力的不足。", "evidence": ["E012", "E013"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "提问者没有说错，是尼采错了。", "evidence": ["E014"]}
   ],
   "argument_steps": [
    "先给结论：能力不足是正确且万能的归因（P002）。",
    "第一组假设：他人无限满足我的愿望则无矛盾（P003—P006）。",
    "否定该假设：人没有无限达成他人愿望的能力（P007）。",
    "第二组假设：我若无所需、能自立、有无限财富则无矛盾（P008—P012）。",
    "否定该假设：人没有无欲无求的能力（P013）。",
    "第三组假设：我能原谅则无矛盾，并举父母、朋友、教师（P014—P018）。",
    "追问原谅的相互性（P019—P021）。",
    "否定该假设：人类缺少原谅的能力（P022）。",
    "归纳三种能力不足并推出矛盾根源（P023—P024）。",
    "收束：提问者没说错，是尼采错了（P025—P026）。"
   ],
   "concept_usage": [
    {"term": "能力不足", "meaning": "缺少达成他人愿望、无所需求或原谅他人的能力；作者称其为一切矛盾的根源", "evidence": "P024", "ambiguity": "未区分能力不足与意愿、资源、制度等其他成因"},
    {"term": "万能归因法", "meaning": "可套用于任何矛盾的解释方式，作者因此称其“当然一定是对的”", "evidence": "P002", "ambiguity": "作者未说明“万能”是否也意味着不可证伪"},
    {"term": "原谅", "meaning": "对被满足的期待落空不予追究；作者强调它必须相互才有意义", "evidence": "P015", "ambiguity": "未界定原谅与体谅的区别"},
    {"term": "矛盾", "meaning": "他人的不满足与自己需求之间的冲突", "evidence": "P012", "ambiguity": "未区分人际冲突与逻辑矛盾"},
    {"term": "无欲无求", "meaning": "对一切人不产生任何所需的状态", "evidence": "P013", "ambiguity": "作者以“可惜”否定其现实性"}
   ],
   "examples_and_targets": [
    "摘天上星、月亮、太阳、银河（作者的假设性例证，P003—P005）",
    "他人叛逃而我若自己能打赢（作者的假设例证，P010）",
    "父母与温饱、朋友与理解、教师与答案（作者举的三种关系，P016—P018）",
    "尼采（被作者指为“错了”的对象，P026，但未引其原文）"
   ],
   "conditions": [
    "以“如果你能有这样的能力”为条件的假设（P006）",
    "以“我如果有能力不要”“我如果有无限的财富”为条件的假设（P009、P011）",
    "以“我如果对一切人无任何所需”为条件（P012）",
    "以父母、朋友、教师三种关系为场景（P016—P018）",
    "以“如果我不原谅你的不原谅”为条件的追问（P021）"
   ],
   "rhetoric_and_tone": "短句排比与递进设问为主：“我要……我又要……我若要……”层层加码，再以“很可惜”“可惜”转折否定；第二组改用“我如果有能力……”排比，第三组改用“你是我的……我原谅”句式并转为反问链；结尾两句话锋一转，把结论落到“是尼采错了”，带调侃与论断色彩。",
   "unresolved_questions": [
    "“是尼采错了”所指尼采的哪一具体主张、出自何书，本文未说明，需外部核查",
    "“万能归因法，当然一定是对的”是否含反讽，正文未明示",
    "作者对“矛盾”的定义仅由用例体现，未给出明确定义",
    "标题“能力不足”与正文三种能力的对应关系未明说"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P002", "quote": "这个归因是正确的。这是个万能归因法，当然一定是对的。", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P003", "quote": "我要天上星，你能摘给我，我们之间自然没有矛盾了", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P006", "quote": "如果你能有这样的能力，我们将可以永远没有矛盾可言", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P007", "quote": "很可惜，人没有无限的达成他人愿望的能力", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P009", "quote": "我如果有能力不要你帮我摘星，我们就没有矛盾", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P012", "quote": "我如果对一切人无任何所需，那么任何人不满足我任何所需都不会构成我与任何人的矛盾", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P013", "quote": "可惜，人没有无欲无求的能力", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P015", "quote": "我需要，你却不能给我，我体谅，我原谅，那么也就不会有矛盾了吧", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P020", "quote": "我原谅你，你却不原谅我，我能原谅你的不原谅吗？", "relation": "supports"},
    {"key": "E010", "paragraph_id": "P021", "quote": "如果我不原谅你的不原谅，你还能原谅我对不原谅的不原谅吗？", "relation": "supports"},
    {"key": "E011", "paragraph_id": "P022", "quote": "可惜，人类也缺少原谅的能力", "relation": "supports"},
    {"key": "E012", "paragraph_id": "P023", "quote": "我们没有不需求的能力、没有满足需求的能力、也没有原谅的能力", "relation": "supports"},
    {"key": "E013", "paragraph_id": "P024", "quote": "一切人类矛盾的根源都是来自这三个能力的不足", "relation": "supports"},
    {"key": "E014", "paragraph_id": "P026", "quote": "是尼采错了", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["人际关系", "冲突归因", "哲学随笔"],
   "issue_candidates": ["矛盾的归因方式", "能力与需求的关系", "原谅的相互性"],
   "text_function_candidates": ["答疑", "论辩", "思辨短文"],
   "object_candidates": ["尼采（仅末句提及）"],
   "working_keywords": ["能力不足", "万能归因法", "无欲无求", "原谅", "矛盾"]
  },
  "notes": "全文未点出尼采的具体主张，“是尼采错了”所需的外部文本本文未提供；brief 与正文前七段基本重合但 brief 末尾被截断（“人没有无限”）。"
 },
 "d55a5274": {
  "analysis": {
   "question_context": "提问者（Q001）问“古代的武器真的有穿越小说那么不堪吗？”。作者不直接评判小说，而是从古代冶炼炉温与提纯手段的限制出发，说明古兵器为何达不到现代优良金属制品的性能，并用糖块挑沙的类比加以说明。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "给出技术前提：古代炉温不足以熔炼钢铁，只能靠折叠锻打“敲脱”杂质，即百炼钢。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P003", "P004", "P005", "P006", "P007"], "summary": "以糖块混沙类比两种除杂方式：可溶解过滤者得洁白如象牙，只能拉条挑沙者反复折叠仍远不及，且漏沙处即成缺陷。", "role": "example"},
    {"unit_id": "U003", "paragraph_refs": ["P008", "P009", "P010", "P011", "P012", "P013"], "summary": "由缺陷推出形制后果：怕断只能做粗，人手只能灵活挥舞约两公斤，故同重则更短、同长则更重或易断；结论是古人都用长矛。", "role": "conclusion"},
    {"unit_id": "U004", "paragraph_refs": ["P014"], "summary": "补充热处理与表面处理的限制，并给出总结论：化学成分相同，现代优良金属制品的性能也远高于古代产品。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "古代冶炼炉温很低，不足以熔炼钢铁，只能达到碳化铁熔融物的水平。", "evidence": ["E001"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "很多提纯步骤做不了，主要依靠折叠锻打时的机械性能差异敲脱杂质渣块，即所谓百炼钢。", "evidence": ["E002"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只能挑沙式除杂的一方即便挑一百次也远达不到溶解过滤的水准，挑一千次只能做到略带灰色。", "evidence": ["E003", "E004"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "挑漏的沙粒即成为缺陷，重击可能断裂。", "evidence": ["E005"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "为怕断裂，只能把兵器做得更粗。", "evidence": ["E006"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "人手只能灵活挥舞大概2公斤重的武器。", "evidence": ["E007"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "同样三斤重的刀，杂质多者要短一尺多，够不着对方。", "evidence": ["E008"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "若做成一样长，杂质多者会重到抡不动、举不起，对方砍一刀自己可砍三刀。", "evidence": ["E009"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "若一样长又一样轻，可照其刀身招呼，两下就能砍断，获得“削铁如泥”的效果。", "evidence": ["E010"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "所以古人都用长矛。", "evidence": ["E011"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "古代没有温度计与合成溶剂，不能精细进行淬火、退火、回火等冷却操作，也不能准确做渗碳等表面处理。", "evidence": ["E012", "E013"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "综合下来，即使化学成分完全相同，现代优良金属制品的性能也要远高于古代产品。", "evidence": ["E014"]}
   ],
   "argument_steps": [
    "技术前提：炉温低→提纯步骤缺失→只能靠锻打排渣（P001）。",
    "类比：糖块混沙；两者工艺对比（P002—P006）。",
    "由残留杂质推出缺陷与断裂风险（P007）。",
    "由断裂风险推出加粗（P008）。",
    "加入人力上限：只能挥舞约2公斤（P009）。",
    "分三种情形推出长短与轻重、断与不断的实战后果（P010—P012）。",
    "结论：古人都用长矛（P013）。",
    "补充热处理与表面处理的限制，得出总性能结论（P014）。"
   ],
   "concept_usage": [
    {"term": "碳化铁熔融物", "meaning": "作者称古代炉温所能达到的极限状态，不足以熔炼钢铁", "evidence": "P001", "ambiguity": "未给出温度数值或金相依据"},
    {"term": "百炼钢", "meaning": "靠折叠锻打的机械性能差异敲脱杂质渣块的工艺", "evidence": "P001", "ambiguity": "作者以“所谓”引出，未讨论该词的通常含义"},
    {"term": "削铁如泥", "meaning": "被作者加引号用作砍断对方刀身的比喻性“成就”", "evidence": "P012", "ambiguity": "属修辞用法，非作者认可的技术表述"},
    {"term": "金相结构", "meaning": "需要通过精细冷却操作控制的金属内部组织", "evidence": "P014", "ambiguity": "未展开具体金相学说明"},
    {"term": "渗碳", "meaning": "需要合成溶剂与精准成分控制的表面处理", "evidence": "P014", "ambiguity": "未说明古代是否存在其他渗碳方式"}
   ],
   "examples_and_targets": [
    "大麦芽糖糖块混沙（作者的类比，P002）",
    "用布过滤、蒸发重结晶（作者类比中“你”的做法，P003）",
    "拉成长条用镊子挑沙、反复对折（作者类比中“另一个人”的做法，P004）",
    "三斤重的刀、长矛（作者用于推演形制后果的设定，P010、P013）"
   ],
   "conditions": [
    "以“古代冶炼炉温很低”为技术前提（P001）",
    "以糖块混沙的类比为说明条件（P002—P005）",
    "以“人手只能灵活挥舞大概2公斤重的武器”为人力上限（P009）",
    "以“同样三斤重”“如果一样长”“如果一样长又一样轻”为三种假设情形（P010—P012）",
    "以“即使化学成分完全相同”为让步条件（P014）"
   ],
   "rhetoric_and_tone": "教学式、类比式说明，用第二人称“你”与“另一个人”构造对照实验，让读者自比现代工艺；“而你的洁白如象牙”“你可以获得‘削铁如泥’成就”带有轻微调侃与游戏化措辞（“成就”）；结尾以“综合下来”作冷静总结，通篇无对提问者或小说的直接贬斥。",
   "unresolved_questions": [
    "“古代冶炼炉温很低，不足以熔炼钢铁，事实上只能达到碳化铁熔融物的水平”属技术断言，需冶金史外部核查（P001）",
    "“人手只能灵活挥舞大概2公斤重的武器”未给出依据或适用范围（P009）",
    "“两下他的就断了”等实战推演为设想，未提供实测或史料支持（P012）",
    "古代是否完全不存在精细淬火与渗碳，需外部核查（P014）",
    "文章 updated_at 为 2025-12-27，晚于发表时间，是否有增补未说明"
   ],
   "evidence": [
    {"key": "E001", "paragraph_id": "P001", "quote": "古代冶炼炉温很低，不足以熔炼钢铁，事实上只能达到碳化铁熔融物的水平", "relation": "supports"},
    {"key": "E002", "paragraph_id": "P001", "quote": "主要依靠折叠锻打时的机械性能差异“敲脱”杂质渣块，也就是所谓的百炼钢", "relation": "supports"},
    {"key": "E003", "paragraph_id": "P005", "quote": "他就是挑一百次，也还远远没有到你的水准", "relation": "supports"},
    {"key": "E004", "paragraph_id": "P005", "quote": "挑一千次，大概可以做到略带灰色，但肉眼已看不见可见的沙粒", "relation": "supports"},
    {"key": "E005", "paragraph_id": "P007", "quote": "他挑漏了两三颗沙，那里就是缺陷。重击就可能会断。", "relation": "supports"},
    {"key": "E006", "paragraph_id": "P008", "quote": "为了怕断，他只好做粗一点", "relation": "supports"},
    {"key": "E007", "paragraph_id": "P009", "quote": "人手只能灵活挥舞大概2公斤重的武器", "relation": "supports"},
    {"key": "E008", "paragraph_id": "P010", "quote": "同样三斤重的刀，你的刀比他长一尺多。他够不着你。", "relation": "supports"},
    {"key": "E009", "paragraph_id": "P011", "quote": "如果一样长，他的会重到抡不动、举不起。他砍你一刀，你可以砍他三刀。", "relation": "supports"},
    {"key": "E010", "paragraph_id": "P012", "quote": "如果一样长又一样轻，你可以照着他的刀身招呼。两下他的就断了。", "relation": "supports"},
    {"key": "E011", "paragraph_id": "P013", "quote": "所以古人都用长矛", "relation": "supports"},
    {"key": "E012", "paragraph_id": "P014", "quote": "不能进行精细的淬火、退火、回火等冷却操作，不能精细的控制金相结构", "relation": "supports"},
    {"key": "E013", "paragraph_id": "P014", "quote": "没有合成溶剂和精准的成分控制，于是也就不能做太准确的渗碳等表面处理", "relation": "supports"},
    {"key": "E014", "paragraph_id": "P014", "quote": "即使化学成分完全相同，现代优良金属制品的性能也要远远高过古代产品", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["冶金史", "古代兵器", "材料工艺"],
   "issue_candidates": ["古代武器的实际性能", "古代冶炼与提纯手段的限制", "百炼钢与折叠锻打"],
   "text_function_candidates": ["答疑", "解释", "类比说明"],
   "object_candidates": ["古代中国", "穿越小说（仅提问语境）"],
   "working_keywords": ["百炼钢", "折叠锻打", "杂质", "淬火", "渗碳", "长矛"]
  },
  "notes": "brief 与正文前段重合但被截断（止于“再蒸发水分把糖块重新凝结出来”）。正文未直接评论“穿越小说”的设定，仅从工艺限制回答。文中技术断言均需冶金史外部核查，本记录不代为裁决。"
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
