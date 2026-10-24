#!/usr/bin/env python3
"""v6 增量（2026-10-16 抓取 16 篇）：合并语料、按主旨归册、追加三份编目（序号 4408 起）。"""
import json, shutil, time
from pathlib import Path

ROOT = Path("/storage/Users/currentUser/Documents/岐伯论")
BASE = ROOT / "research-rebuild/reports/gemini-flash-reclassification-v1"
INC = ROOT / "research/online-increment/sooon-increment-20261016-154937.jsonl"
V5 = ROOT / "sooon-q9adg-articles-v5.jsonl"
V6 = ROOT / "sooon-q9adg-articles-v6.jsonl"
BUILD_CORPUS = BASE / "sooon-q9adg-articles-v4.jsonl"   # all-articles-merged-v3.jsonl 指向此文件
CATS = [BASE / f for f in ("workbook-40b-all-catalog.jsonl", "workbook-40b-all-catalog-v4.jsonl", "workbook-40b-all-catalog-v5.jsonl")]

# 逐篇通读主旨后的归册
ASSIGN = {
    "寸步可行": "B18",       # 先想清楚再行动 vs 边干边调 -> 知行合一
    "荒": "B25",             # 短剧与屏幕后看不到人 -> 网络生态
    "一人食": "B15",         # 熟店老板搭话就不想去 -> 社交距离
    "鳞甲": "B16",           # 网暴躲不过、如何自保 -> 危机识人与权义守界
    "粉红泡泡": "B11",       # 如何戒掉喜欢一个人 -> 两性吸引
    "工中禅": "B39",         # 无人要求仍做到极致（制箭）-> 艺能与生活美学
    "一狼犬坐": "B40",       # 骑兵下马步战 -> 治乱兴亡（军事史）
    "非标义人": "B30",       # 武侠与骑士/武士/牛仔 -> 文明演进与社会秩序
    "千面真人": "B33",       # 何为真实的自己 -> 人性幽微
    "笑死": "B35",           # 努力能否抹平天赋出身 -> 命途因果
    "搜神": "B29",           # 信息可搜，人还需记住什么 -> 科技与工具反思
    "蜂拥而至的孤独": "B25", # 大水/薄肌理论等网络热梗 -> 网络生态
    "过分要求": "B04",       # 想让儿子贴心是否过分 -> 亲子沟通
    "同乡异人": "B39",       # 王小波为何不再流行 -> 艺文
    "逐流而为": "B32B",      # 顺势而为与随波逐流之辨 -> 名相辨析
    "无可用": "B06",         # 父母总占据我的时间 -> 成年子女自立与边界
}
META_KEYS = ("volume_code", "booklet_name", "volume_prefix", "volume_full_title",
             "booklet_stem", "booklet_stem_title", "full_citation")

ts = time.strftime("%Y%m%d_%H%M%S")
inc = [json.loads(l) for l in INC.open(encoding="utf-8") if l.strip()]
assert len(inc) == 16 and set(r["title"] for r in inc) == set(ASSIGN)

# 1) 语料 v6
corpus = {str(r["id"]): r for r in (json.loads(l) for l in V5.open(encoding="utf-8") if l.strip())}
n0 = len(corpus)
for r in inc:
    corpus[str(r["id"])] = r
items = sorted(corpus.values(), key=lambda x: x["publishedAt"], reverse=True)
with V6.open("w", encoding="utf-8") as f:
    for it in items:
        f.write(json.dumps(it, ensure_ascii=False, separators=(",", ":")) + "\n")
shutil.copy2(BUILD_CORPUS, str(BUILD_CORPUS) + ".bak_before_v6_" + ts)
shutil.copy2(V6, BUILD_CORPUS)
print(f"语料：{n0} -> {len(items)}")

# 2) 编目
recs = [json.loads(l) for l in CATS[0].open(encoding="utf-8") if l.strip()]
ids = {r["original_id"] for r in recs}
# 每册取出现最多的元数据组合作为模板（避免繁简混杂的少数派）
from collections import Counter
tmpl = {}
for code in set(ASSIGN.values()):
    c = Counter(tuple(r[k] for k in META_KEYS) for r in recs if r["booklet_code"] == code)
    tmpl[code] = dict(zip(META_KEYS, c.most_common(1)[0][0]))

ordn = max(r["workbook_ordinal"] for r in recs) + 1
assert ordn == 4408
new = []
for r in sorted(inc, key=lambda x: x["publishedAt"]):
    assert r["id"] not in ids
    code = ASSIGN[r["title"]]
    rec = {"workbook_ordinal": ordn, "original_id": r["id"], "title": r["title"],
           "published_at": r["publishedAt"], "question": r.get("question") or "",
           "booklet_code": code, "text_len": len(r.get("text") or ""),
           "text_preview": (r.get("text") or "")[:150], "url": r["url"], "article_url": r["url"]}
    rec.update(tmpl[code])
    new.append(rec)
    print(ordn, r["title"], "->", code, tmpl[code]["booklet_name"])
    ordn += 1

final = recs + new
for p in CATS:
    shutil.copy2(p, str(p) + ".bak_before_v6_" + ts)
    with p.open("w", encoding="utf-8") as f:
        for r in final:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
print("编目总篇数：", len(final))
