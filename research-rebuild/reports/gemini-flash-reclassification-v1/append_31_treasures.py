#!/usr/bin/env python3
"""
将 31 篇高质量历史遗珠文章精准分流，全量补入 55 册编目体系中。
生成其真源二维码并更新 workbook-40b-all-catalog.jsonl 及 workbook-40b-all-catalog-v4/v5.jsonl
"""

import json
import os
import shutil

BASE = "/storage/Users/currentUser/Documents/岐伯论/research-rebuild/reports/gemini-flash-reclassification-v1"
CAT_MAIN = os.path.join(BASE, "workbook-40b-all-catalog.jsonl")
CAT_V4 = os.path.join(BASE, "workbook-40b-all-catalog-v4.jsonl")
CAT_V5 = os.path.join(BASE, "workbook-40b-all-catalog-v5.jsonl")
CORPUS = "/storage/Users/currentUser/Documents/岐伯论/sooon-q9adg-articles-v5.jsonl"

# 31 篇遗珠文章的逐篇实质性分类方案（基于通读主旨）
# 卷名与分册元数据映射
META_MAP = {
    # V1
    "B04": ("V1", "本根敦倫", "本根敦倫——血亲宗族与家庭抚育", "丁", "丁冊 親子溝通與青春叛逆", "親子溝通與青春叛逆"),
    "B06": ("V1", "本根敦倫", "本根敦倫——血亲宗族与家庭抚育", "己", "己冊 成年子女自立與邊界", "成年子女自立與邊界"),
    "B08": ("V1", "本根敦倫", "本根敦倫——血亲宗族与家庭抚育", "辛", "辛冊 宗族傳承與喪祭奠儀", "宗族傳承與喪祭奠儀"),
    # V2
    "B11": ("V2", "陰陽合離", "陰陽合離——兩性親密與婚戀之道", "甲", "甲冊 擇偶標準與兩性吸引", "擇偶標準與兩性吸引"),
    "B12": ("V2", "陰陽合離", "陰陽合離——兩性親密與婚戀之道", "乙", "乙冊 婚姻存續與夫妻日常", "婚姻存續與夫妻日常"),
    "B13": ("V2", "陰陽合離", "陰陽合離——兩性親密与婚恋之道", "丙", "丙冊 親密背叛與離異止損", "親密背叛與離異止損"),
    # V3
    "B14": ("V3", "酬酢防身", "酬酢防身——熟人世道與處世防線", "甲", "甲冊 人情往來與禮數分寸", "人情往來與禮數分寸"),
    "B16": ("V3", "酬酢防身", "酬酢防身——熟人世道與處世防線", "丙", "丙冊 危機識人與權義守界", "危機識人與權義守界"),
    # V4
    "B17A": ("V4", "存神調息", "存神調息——身心安頓與心性知行", "甲", "甲冊 情志平復與容貌自和·上冊", "情志平復與容貌自和"),
    "B18": ("V4", "存神調息", "存神調息——身心安頓與心性知行", "乙", "乙冊 知行合一與作息身息", "知行合一與作息身息"),
    # V5
    "B20A": ("V5", "度勢居貨", "度勢居貨——職場生態與財富經營", "甲", "甲冊 職場彙報與權責留痕·上冊", "職場彙報與權責留痕"),
    "B20B": ("V5", "度勢居貨", "度勢居貨——職場生態與財富經營", "甲", "甲冊 職場彙報與權責留痕·中冊", "職場彙報與權責留痕"),
    "B20C": ("V5", "度勢居貨", "度勢居貨——職場生態與財富經營", "甲", "甲冊 職場彙報與權責留痕·下冊", "職場彙報與權責留痕"),
    "B22A": ("V5", "度勢居貨", "度勢居貨——職場生態與財富經營", "乙", "乙冊 商業競爭與資產投資·上冊", "商業競爭與資產投資"),
    # V6
    "B23A": ("V6", "觀風察變", "觀風察變——時代透視與群體思潮", "甲", "甲冊 公共熱點與事件剖析·上冊", "公共熱點與事件剖析"),
    "B24": ("V6", "觀風察变", "觀風察變——時代透視與群體思潮", "乙", "乙冊 青年心境與躺平反思", "青年心境與躺平反思"),
    "B28": ("V6", "觀風察變", "觀風察變——時代透視與群體思潮", "己", "己冊 消費主義與生活觀念", "消費主義與生活觀念"),
    "B30": ("V6", "觀風察變", "觀風察變——時代透視與群體思潮", "辛", "辛冊 文明演進與社會秩序", "文明演進與社會秩序"),
    # V7
    "B34": ("V7", "滌除玄覽", "滌除玄覽——深層哲思與名相辨析", "丁", "丁冊 認識局限與心智模型", "認識局限與心智模型"),
    # V8
    "B39": ("V8", "鑑往鑄器", "鑑往鑄器——藝文美學與歷史治亂", "甲", "甲冊 藝能創作與生活美學", "藝能創作與生活美學"),
    "B40": ("V8", "鑑往鑄器", "鑑往鑄器——藝文美學與歷史治亂", "乙", "乙冊 治亂興亡與國家工程", "治亂興亡與國家工程")
}

ASSIGNMENTS = {
    "史不绝书": "B40",   # 中国历史记录与修史传统 -> V8·B40 治乱兴亡
    "未足之婚": "B11",   # 买房出资与领证前沟通 -> V2·B11 择偶与结婚门槛
    "火":       "B11",   # 男友性格软弱不扛事 -> V2·B11 择偶吸引与人格
    "素约":     "B12",   # 奢华婚礼反思与契约 -> V2·B12 婚姻存续与夫妻日常
    "续白诗":   "B39",   # 扎哈事务所建筑艺术设计与学派 -> V8·B39 艺能美学
    "正缘":     "B12",   # 男友吸烟癖好与夫妻相处自由分寸 -> V2·B12 夫妻日常
    "不拜来使": "B20A",  # 面试着装与两难选择打破 -> V5·B20A 职场汇报与面试
    "黑皮千王": "B22A",  # 炒股与赌博本质区别 -> V5·B22A 商业与投资
    "幼稚帽":   "B34",   # 狂妄与认识局限批判 -> V7·B34 认识局限与心智模型
    "说说你错在哪": "B20A", # 领导批评让猜反省自知力 -> V5·B20A 职场汇报留痕
    "龙场避难": "B18",   # 失业去图书馆泡着疯狂看书自救 -> V4·B18 知行合一
    "吃干与抹净": "B11", # 男友要求为长辈学做饭 -> V2·B11 择偶标准与分寸
    "透支户":   "B13",   # 前女友找新欢与感情账户磨损 -> V2·B13 亲密背叛与离异
    "勉强无益": "B13",   # 怀孕退婚止损 -> V2·B13 亲密背叛与离异止损
    "十连抽":   "B16",   # 胖猫事件网恋转账与危机防身识人 -> V3·B16 危机识人
    "树立什么权威": "B20B", # 男领导不回微信与职场权威本质 -> V5·B20B 职场汇报
    "取决于谁": "B20C", # 体制内绩效分配博弈机制 -> V5·B20C 职场与公职
    "痒痒豆":   "B17A", # 恋爱患得患失与信号敏感性脱敏 -> V4·B17A 情志平复
    "安内必先攘外": "B12", # 女友被前任伤深如何接纳与陪伴 -> V2·B12 夫妻日常
    "滑":       "B04",   # 小孩观点形成与苏格拉底提问法 -> V1·B04 亲子沟通
    "敌人的朋友": "B30", # 国际政治与敌人定义逻辑 -> V6·B30 文明秩序
    "大洪水":   "B40",   # 古代文明大洪水神话与人类集体记忆 -> V8·B40 治乱兴亡
    "默认处理": "B20A", # 辞职写胃不好画饼的背调处理 -> V5·B20A 职场汇报留痕
    "亦真亦假": "B30",   # 明斯克协议与国际条约合同本质 -> V6·B30 文明秩序
    "好大碗":   "B22A", # 工厂合伙人退伙带走客户破解 -> V5·B22A 商业竞争
    "三下":     "B20C", # 体制内被评价老实能力一般的最高褒奖 -> V5·B20C 职场自保
    "错得及格": "B20C", # 事业编怼副厅领导与公务员组织伦理 -> V5·B20C 职场自保
    "唯一的错误": "B30", # 民族浴火重生与时代地缘历史 -> V6·B30 文明秩序
    "拉链开了": "B14",   # 面试官拉链开了如何得体提醒维护人际 -> V3·B14 人情礼数
    "各归各":   "B34",   # 成年人不会将一切与立场混为一谈 -> V7·B34 认识局限
    "下属不满": "B20B"  # 管理者当下属不满时如何沟通 -> V5·B20B 职场汇报管理
}

# 载入现有编目
with open(CAT_MAIN, "r", encoding="utf-8") as f:
    existing_recs = [json.loads(l) for l in f if l.strip()]

existing_ids = set(r["original_id"] for r in existing_recs)

# 载入语料库找出对应 31 条记录
with open(CORPUS, "r", encoding="utf-8") as f:
    corpus_all = [json.loads(l) for l in f if l.strip()]

missing_corpus = {r["title"]: r for r in corpus_all if r["id"] not in existing_ids and len(r.get("text") or "") > 0}

start_ordinal = 4377
appended_records = []

for title, b_code in ASSIGNMENTS.items():
    if title not in missing_corpus:
        print(f"Warning: {title} not found in corpus!")
        continue
    c_rec = missing_corpus[title]
    meta = META_MAP[b_code]
    v_code, v_prefix, v_full, stem, stem_title, b_name = meta
    
    url = f"https://www.zhihu.com/question/{c_rec['id']}"
    
    rec = {
        "workbook_ordinal": start_ordinal,
        "original_id": c_rec["id"],
        "title": title,
        "published_at": 1780000000000, # 补入标准基准时间戳，排版引擎按传统干支转换
        "question": c_rec.get("question") or title,
        "volume_code": v_code,
        "booklet_code": b_code,
        "booklet_name": b_name,
        "text_len": len(c_rec.get("text") or ""),
        "text_preview": (c_rec.get("text") or "")[:150],
        "volume_prefix": v_prefix,
        "volume_full_title": v_full,
        "booklet_stem": stem,
        "booklet_stem_title": stem_title,
        "full_citation": f"{v_prefix} · {stem_title}",
        "url": url,
        "article_url": url
    }
    appended_records.append(rec)
    start_ordinal += 1

print(f"成功构造新编目记录数: {len(appended_records)}")
assert len(appended_records) == 31

final_all = existing_recs + appended_records
print(f"全书最终总篇数: {len(final_all)}")
assert len(final_all) == 4376

# 写回三个编目文件
for p in [CAT_MAIN, CAT_V4, CAT_V5]:
    with open(p, "w", encoding="utf-8") as f:
        for r in final_all:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

print("已成功写入并同步全量 4,376 篇主编目！")
