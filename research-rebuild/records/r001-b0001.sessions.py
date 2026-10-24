# -*- coding: utf-8 -*-
"""批次 r001-b0001 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0001.sessions.py            # 写 out/r001-b0001.out.jsonl
  python3 records/r001-b0001.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0001"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0001.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "80c38b2d": {
  "analysis": {
   "question_context":"回应南北买菜和饮食差异，作者提出北方饮食受军屯军镇和军需条件塑造的解释。",
   "content_units":[{"unit_id":"U001","paragraph_refs":["P001","P002","P003","P004","P005","P006","P007","P008","P009","P010"],"summary":"从地名和行政聚居形态推断北方饮食具有军食特征，并列举大锅、炖煮、干粮、咸味等结果。","role":"claim"}],
   "main_claims":[{"claim_id":"C001","claim_type":"author_qualified","attribution":"author","modality":"predicted","statement":"北方尤其东北饮食习惯主要由长期军事化生活、军需供应和有限行政能力塑造。","evidence":["E1"]}],
   "argument_steps":["以北方地名和军屯形态作线索。","把军队采购和加工条件对应到饮食形式。","预测供应体系现代化后北方餐饮会向少量多样、精细质量靠拢。"],
   "concept_usage":[{"term":"军食","meaning":"由军队集体供给和加工条件形成的伙食模式","evidence":"P004"}],
   "examples_and_targets":["大锅菜、馒头、干粮、肉食、面食、咸菜和盐。"],"conditions":["论证依赖古代军屯军镇长期占优势的历史假设。","现代供应体系消除限制后差异会逐渐消亡。"],
   "rhetoric_and_tone":"解释性、推断性，使用编号列举和自谦语气。","unresolved_questions":["文中历史因果链未提供外部史料核验。","末段含平台词‘社科答集’。"],
   "evidence":[{"key":"E1","paragraph_id":"P009","quote":"北方汉族饮食实为军食、伙食","relation":"supports"}]},
  "provisional_tags":{"domain_candidates":["饮食史","社会史"],"issue_candidates":["南北饮食差异"],"text_function_candidates":["因果解释"],"object_candidates":["北方饮食","军屯"],"working_keywords":["军食","军需","供应体系"]},"notes":"未将作者推断当作已证实历史结论。"
  },
 "8c4f866e": {
  "analysis": {
   "question_context":"回应人类是否拥有最强耐力，作者反驳把耐力狩猎想象成无伤追逐。","content_units":[{"unit_id":"U001","paragraph_refs":["P001","P002","P003","P004","P005","P006","P007","P008","P009","P010","P011","P012","P013","P014","P015","P016","P017","P018"],"summary":"区分受伤猎物、追踪与竞速，指出补给、收益、风险和劳动力约束，结论是人类靠工具和追踪而非生理耐力胜过动物。","role":"rebuttal"}],"main_claims":[{"claim_id":"C001","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"人类通常先用工具打伤动物，再依靠追踪而非竞速追逐。","evidence":["E1"]},{"claim_id":"C002","claim_type":"author_qualified","attribution":"author","modality":"asserted","statement":"石器时代人类没有超常耐力，主要优势是伏击、投掷、远程射击和足迹追踪。","evidence":["E2"]}],"argument_steps":["列出关于耐力狩猎的多个误解。","分析补给、能量、搬运和群体劳动力成本。","排除圆圈追逐等反驳并给出结论。"],"concept_usage":[{"term":"耐力狩猎","meaning":"以持续运动使猎物过热或脱水的狩猎设想","evidence":"P009"}],"examples_and_targets":["羚羊、角马、布须曼人、石器工具。"],"conditions":["若成功率非百分之百，长距离追逐会带来重大风险。"],"rhetoric_and_tone":"论战式、反讽，连续设问和夸张口语。","unresolved_questions":["文中有关狩猎人类学的事实需外部核查。","末段含平台词和追加问题。"],"evidence":[{"key":"E1","paragraph_id":"P003","quote":"人类总是先用石块、骨棒、弓箭、手斧之类先打伤动物才开始‘追逐’的","relation":"supports"},{"key":"E2","paragraph_id":"P018","quote":"人类只是借着伏击能力（尤其是投掷和远程射击能力）和足迹追踪能力胜过受了伤的普通动物。","relation":"supports"}]},"provisional_tags":{"domain_candidates":["人类学","狩猎"],"issue_candidates":["人类耐力"],"text_function_candidates":["反驳"],"object_candidates":["人类","野生动物"],"working_keywords":["耐力狩猎","追踪","补给"]},"notes":"保留作者的经验性推断，不作外部事实裁决。"
  },
 "c2e2ed74": {
  "analysis": {
   "question_context":"回应医学进步是否阻碍人类进化，作者主张医学提高人口密度和竞争压力，反而加速演化。","content_units":[{"unit_id":"U001","paragraph_refs":["P001","P002","P003","P004"],"summary":"把演化动力归因于种群密度超标，举黑死病和高密度社会说明技术与医学造成持续选择压力。","role":"claim"}],"main_claims":[{"claim_id":"C001","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"医学进步增加人口密度和社会竞争，因此加速而非阻碍人类演化。","evidence":["E1"]}],"argument_steps":["定义演化需要种群数量和密度压力。","比较动物灾害导致的密度与人类技术造成的持续密度。","用黑死病说明高密度和医学条件如何放大选择压力。"],"concept_usage":[{"term":"演化压力","meaning":"人口密度、竞争和灾害对种群末位个体施加的淘汰压力","evidence":"P004"}],"examples_and_targets":["狮子种群、黑死病、欧洲城镇。"],"conditions":["结论依赖将人口密度与演化压力建立因果关系。"],"rhetoric_and_tone":"解释性、断言式，带有机制推演。","unresolved_questions":["文中未区分遗传演化与文化选择的证据强度。"],"evidence":[{"key":"E1","paragraph_id":"P001","quote":"医学的进步大大的提速了人类的进化。","relation":"supports"}]},"provisional_tags":{"domain_candidates":["进化论","社会史"],"issue_candidates":["医学与演化"],"text_function_candidates":["因果论证"],"object_candidates":["人类种群","医学"],"working_keywords":["人口密度","末位淘汰","医学"]},"notes":"‘提速’为作者判断，未作科学验证。"
  },
 "0af3428a": {
  "analysis": {
   "question_context":"回应运动能力最强物种是否为猫科，作者先改变评价标准，再用尺度和材料学推断小型昆虫可能胜出。","content_units":[{"unit_id":"U001","paragraph_refs":["P001","P002","P003","P004","P005","P006"],"summary":"以有效过载作为去除体型影响的敏捷与强壮标度，并指出缩小结构具有材料强度优势。","role":"definition"}],"main_claims":[{"claim_id":"C001","claim_type":"author_qualified","attribution":"author","modality":"predicted","statement":"若以有效过载评价运动能力，微小昆虫可能胜过猫；猫的机动能力不如蚊子。","evidence":["E1"]}],"argument_steps":["设定运动能力评价标准。","引入有效过载并说明体型影响。","用缩小结构的强度优势推导结论。"],"concept_usage":[{"term":"有效过载","meaning":"动物以自身质心为等效对象时可主动造成的过载，用于衡量机动性","evidence":"P002"}],"examples_and_targets":["猫、蚊子、老鼠和大象。"],"conditions":["结论仅适用于作者设定的有效过载指标。"],"rhetoric_and_tone":"概念设定式、简洁推演。","unresolved_questions":["没有讨论不同动物运动方式和测量可比性。"],"evidence":[{"key":"E1","paragraph_id":"P006","quote":"在这一条件下，猫的机动能力不如蚊子。","relation":"supports"}]},"provisional_tags":{"domain_candidates":["生物力学"],"issue_candidates":["运动能力评价"],"text_function_candidates":["概念实验"],"object_candidates":["猫","昆虫"],"working_keywords":["有效过载","体型","机动性"]},"notes":"结论取决于自定义评价标准。"
  },
 "cd4c2817": {
  "analysis": {
   "question_context":"回应为何形成猫爱吃鱼、狗爱吃骨头的观念，作者解释为历史环境和人类观察造成的社会记忆。","content_units":[{"unit_id":"U001","paragraph_refs":["P001","P002","P003","P004","P005"],"summary":"猫因船舶和港口环境常获得鱼，狗因狩猎和烹饪条件获得骨头；两者并非出于偏好。","role":"rebuttal"}],"main_claims":[{"claim_id":"C001","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"猫吃鱼、狗啃骨头的常识主要是生存环境和人类供食方式造成的，并不等于动物偏爱。","evidence":["E1"]}],"argument_steps":["分别说明猫和狗的历史处境。","指出食物可得性与真正偏好的差异。","用流浪汉类比说明受限选择不能推出喜欢。"],"concept_usage":[{"term":"社会记忆","meaning":"人类从反复可见现象形成的概括性观念","evidence":"P002"}],"examples_and_targets":["大型木船、港口杂鱼、狩猎犬、骨髓。"],"conditions":["结论针对受限食物环境，不否认动物在可选择时可能偏好肉。"],"rhetoric_and_tone":"科普解释、纠正常识，带类比。","unresolved_questions":["历史和动物营养细节需外部核查。","末段含平台词。"],"evidence":[{"key":"E1","paragraph_id":"P004","quote":"这两种结论都是因为人类对现象的粗暴理解，并非事实。","relation":"supports"}]},"provisional_tags":{"domain_candidates":["动物行为","饮食史"],"issue_candidates":["动物食物偏好"],"text_function_candidates":["常识纠正"],"object_candidates":["猫","狗"],"working_keywords":["鱼","骨头","社会记忆"]},"notes":"把作者的历史解释与动物真实偏好区分记录。"
  },
 "454f018e": {
  "analysis": {
   "question_context":"回应人类和动物彼此恐惧是否等同，作者先定义恐惧，再区分人类可从恐惧中获得快感与动物的本能回避。","content_units":[{"unit_id":"U001","paragraph_refs":["P001","P002","P003","P004","P005","P006","P007","P008","P009","P010","P011","P012","P013"],"summary":"恐惧包含注意力强制转移和生理痛苦；人类可挑战恐惧并获得快感，动物多受本能围栏约束，因此两者体验和行为功能不同。","role":"definition"}],"main_claims":[{"claim_id":"C001","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"恐惧是意识主体对危机的强迫性反应，至少包括注意力转移和生理痛苦。","evidence":["E1"]},{"claim_id":"C002","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"人类恐惧机制的强迫性较弱，可从挑战恐惧中榨取快感；动物通常不能。","evidence":["E2"]}],"argument_steps":["给恐惧下定义。","说明其生存功能。","比较人类和动物面对恐惧的差异。","结论称差异是人和动物分界的原因。"],"concept_usage":[{"term":"恐惧","meaning":"强制注意力转移并产生生理痛苦的危机反应","evidence":"P002"}],"examples_and_targets":["极速驾驶、跳伞、走钢丝、舞蛇，以及动物回避猛兽。"],"conditions":["人类和动物的差异被作者概括为总体机制差异，不代表每个个体。"],"rhetoric_and_tone":"定义先行、类比和讽刺并用。","unresolved_questions":["动物主观体验无法由本文证实。"],"evidence":[{"key":"E1","paragraph_id":"P002","quote":"恐惧感是意识主体对危机发生的强迫性反应。","relation":"supports"},{"key":"E2","paragraph_id":"P008","quote":"人类独有一种快感机制，即挑战恐惧带来的额外快感。","relation":"supports"}]},"provisional_tags":{"domain_candidates":["动物行为","心理机制"],"issue_candidates":["恐惧的比较"],"text_function_candidates":["概念定义"],"object_candidates":["人类","动物"],"working_keywords":["恐惧","本能围栏","快感"]},"notes":"只记录作者的比较模型，不补入心理学诊断。"
  },
 "0ae9a668": {
  "analysis": {
   "question_context":"回应漂亮动物是否知道自己好看，作者把‘美’改写为动物对同性挑战和应战的行为判断。","content_units":[{"unit_id":"U001","paragraph_refs":["P001","P002","P003","P004"],"summary":"动物没有人类审美概念，但持续被同性挑战并选择应战，意味着其行为上获得了关于自身竞争优势的反馈。","role":"claim"}],"main_claims":[{"claim_id":"C001","claim_type":"author_qualified","attribution":"author","modality":"asserted","statement":"在行为意义上，可以说动物知道自己的美貌，因为同性挑战和应战让其获得了相关信息。","evidence":["E1"]}],"argument_steps":["否认动物拥有抽象的好看概念。","把同性挑战与应战解释为反馈。","据此作行为意义上的‘知道美貌’结论。"],"concept_usage":[{"term":"美貌","meaning":"引发同性竞争并使个体选择应战的外显竞争优势","evidence":"P003"}],"examples_and_targets":["漂亮动物、同性挑战者。"],"conditions":["作者明确限定为行为意义，不等同于人类审美自觉。"],"rhetoric_and_tone":"简短、反转式推理。","unresolved_questions":["未说明不同物种行为是否都能如此解释。"],"evidence":[{"key":"E1","paragraph_id":"P004","quote":"在这个意义上，可以说动物知道自己的美貌。","relation":"supports"}]},"provisional_tags":{"domain_candidates":["动物行为"],"issue_candidates":["动物自我认知"],"text_function_candidates":["概念重述"],"object_candidates":["漂亮动物"],"working_keywords":["美貌","同性挑战","应战"]},"notes":"‘知道’被作者限定为行为反馈意义。"
  },
 "e4da9868": {
  "analysis": {
   "question_context":"回应动物何时开始惧怕人类，作者提出半数回避距离和人类攻击距离的比较框架，并认为可证历史极少。","content_units":[{"unit_id":"U001","paragraph_refs":["P001","P002","P003","P004","P005","P006","P007","P008","P009","P010","P011"],"summary":"用半数回避距离衡量动物胆量，再与人类三种攻击距离比较；文字记录时代的人类狩猎技巧已使动物难以通过试错适应，答案只能暂称莫须有。","role":"definition"}],"main_claims":[{"claim_id":"C001","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"动物惧怕人类可用半数回避距离衡量，并需与人类有效攻击范围比较。","evidence":["E1"]},{"claim_id":"C002","claim_type":"author_qualified","attribution":"author","modality":"asserted","statement":"若动物曾在史前学会适应人类捕猎，其证据极难由文字记录确认。","evidence":["E2"]}],"argument_steps":["定义回避距离。","说明胆量与生存资源的权衡。","建立三种攻击距离。","讨论历史记录和史前证据的限制。"],"concept_usage":[{"term":"半数回避距离","meaning":"随机样本中半数动物开始主动回避人类时的距离","evidence":"P002"}],"examples_and_targets":["狮子、狼、食草动物、人类猎手。"],"conditions":["结论受制于考古证据不足和历史狩猎技巧的高杀伤率。"],"rhetoric_and_tone":"模型化、推演式，夹有生存叙事。","unresolved_questions":["指标和史前推断需要动物行为学与考古资料核验。","末段含平台词。"],"evidence":[{"key":"E1","paragraph_id":"P002","quote":"将动物开始发起主动回避行为的那个距离称为‘回避距离’","relation":"supports"},{"key":"E2","paragraph_id":"P011","quote":"所以，答案是‘莫须有’，且其发生的时间应该是在史前","relation":"supports"}]},"provisional_tags":{"domain_candidates":["动物行为","考古推断"],"issue_candidates":["动物对人类的恐惧"],"text_function_candidates":["指标构造","历史推演"],"object_candidates":["野生动物","人类狩猎"],"working_keywords":["回避距离","攻击距离","史前"]},"notes":"‘莫须有’是作者对可证据状态的表述，不是事实断言。"
  }
}  # noqa: E501


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
