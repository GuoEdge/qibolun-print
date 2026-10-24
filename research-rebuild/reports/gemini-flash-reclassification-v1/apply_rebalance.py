#!/usr/bin/env python3
"""
执行《岐伯论》全量分册削峰（4大超巨册分上下）与填谷（薄册内容逻辑合并）
更新 workbook-40b-all-catalog-v4.jsonl 和 workbook-40b-all-catalog.jsonl
"""

import json
import os
import shutil

BASE = "/storage/Users/currentUser/Documents/岐伯论/research-rebuild/reports/gemini-flash-reclassification-v1"
CAT_V4 = os.path.join(BASE, "workbook-40b-all-catalog-v4.jsonl")
CAT_MAIN = os.path.join(BASE, "workbook-40b-all-catalog.jsonl")

with open(CAT_V4, "r", encoding="utf-8") as f:
    records = [json.loads(line) for line in f if line.strip()]

print(f"载入原始记录数: {len(records)}")

# 辅助函数：根据文章原始顺序进行拆半
def split_records_half(recs, code_a, code_b, name_base, stem):
    n = len(recs)
    mid = math.ceil(n / 2)
    part_a = recs[:mid]
    part_b = recs[mid:]
    
    for r in part_a:
        r["booklet_code"] = code_a
        r["booklet_name"] = name_base
        r["booklet_stem"] = stem
        r["booklet_stem_title"] = f"{stem}冊 {name_base}·上冊"
        r["full_citation"] = f"{r.get('volume_prefix', '')} · {stem}冊 {name_base}·上冊"
        
    for r in part_b:
        r["booklet_code"] = code_b
        r["booklet_name"] = name_base
        r["booklet_stem"] = stem
        r["booklet_stem_title"] = f"{stem}冊 {name_base}·下冊"
        r["full_citation"] = f"{r.get('volume_prefix', '')} · {stem}冊 {name_base}·下冊"
        
    return part_a + part_b

import math

# 按原卷组织处理
by_vol = {}
for r in records:
    by_vol.setdefault(r["volume_code"], []).append(r)

new_records = []

# --- 1. 卷一 (V1) ---
v1_recs = by_vol["V1"]
v1_by_b = {}
for r in v1_recs:
    v1_by_b.setdefault(r["booklet_code"], []).append(r)

# B01-B04 保持
for b in ["B01", "B02", "B03", "B04"]:
    new_records.extend(v1_by_b.get(b, []))

# B05 (12篇) + B07 (4篇) -> 新 B05 (戊册·長輩相處與精神解綁)
b05_merged = v1_by_b.get("B05", []) + v1_by_b.get("B07", [])
for r in b05_merged:
    r["booklet_code"] = "B05"
    r["booklet_name"] = "長輩相處與精神解綁"
    r["booklet_stem"] = "戊"
    r["booklet_stem_title"] = "戊冊 長輩相處與精神解綁"
    r["full_citation"] = "本根敦倫 · 戊冊 長輩相處與精神解綁"
new_records.extend(b05_merged)

# B06 保持 (己册·成年子女自立與邊界)
new_records.extend(v1_by_b.get("B06", []))

# 原 B08 (45篇) -> 新 B07 (庚册·手足同胞與家族親戚)
b08_recs = v1_by_b.get("B08", [])
for r in b08_recs:
    r["booklet_code"] = "B07"
    r["booklet_name"] = "手足同胞與家族親戚"
    r["booklet_stem"] = "庚"
    r["booklet_stem_title"] = "庚冊 手足同胞與家族親戚"
    r["full_citation"] = "本根敦倫 · 庚冊 手足同胞與家族親戚"
new_records.extend(b08_recs)

# 原 B09 (33篇) + B10 (10篇) -> 新 B08 (辛册·宗族傳承與喪祭奠儀)
b09_b10_merged = v1_by_b.get("B09", []) + v1_by_b.get("B10", [])
for r in b09_b10_merged:
    r["booklet_code"] = "B08"
    r["booklet_name"] = "宗族傳承與喪祭奠儀"
    r["booklet_stem"] = "辛"
    r["booklet_stem_title"] = "辛冊 宗族傳承與喪祭奠儀"
    r["full_citation"] = "本根敦倫 · 辛冊 宗族傳承與喪祭奠儀"
new_records.extend(b09_b10_merged)

# --- 2. 卷二 (V2) 保持 ---
new_records.extend(by_vol["V2"])

# --- 3. 卷三 (V3) 保持 ---
new_records.extend(by_vol["V3"])

# --- 4. 卷四 (V4) ---
v4_recs = by_vol["V4"]
v4_by_b = {}
for r in v4_recs:
    v4_by_b.setdefault(r["booklet_code"], []).append(r)

# B17 (171篇) 拆为 B17A 和 B17B
b17_split = split_records_half(v4_by_b.get("B17", []), "B17A", "B17B", "情志平復與容貌自和", "甲")
new_records.extend(b17_split)

# 原 B18 (16篇) + B19 (68篇) 合并为 B18 (乙册·知行合一與作息身息)
b18_merged = v4_by_b.get("B18", []) + v4_by_b.get("B19", [])
for r in b18_merged:
    r["booklet_code"] = "B18"
    r["booklet_name"] = "知行合一與作息身息"
    r["booklet_stem"] = "乙"
    r["booklet_stem_title"] = "乙冊 知行合一與作息身息"
    r["full_citation"] = "存神調息 · 乙冊 知行合一與作息身息"
new_records.extend(b18_merged)

# --- 5. 卷五 (V5) ---
v5_recs = by_vol["V5"]
v5_by_b = {}
for r in v5_recs:
    v5_by_b.setdefault(r["booklet_code"], []).append(r)

# B20A, B20B 保持
new_records.extend(v5_by_b.get("B20A", []))
new_records.extend(v5_by_b.get("B20B", []))

# 原 B21 (17篇) 并入 B20C (下册·117篇 -> 134篇)
b20c_merged = v5_by_b.get("B20C", []) + v5_by_b.get("B21", [])
for r in b20c_merged:
    r["booklet_code"] = "B20C"
    r["booklet_name"] = "職場彙報與權責留痕"
    r["booklet_stem"] = "甲"
    r["booklet_stem_title"] = "甲冊 職場彙報與權責留痕·下冊"
    r["full_citation"] = "度勢居貨 · 甲冊 職場彙報與權責留痕·下冊"
new_records.extend(b20c_merged)

# 原 B22 (197篇) 拆为 B22A (上册) 和 B22B (下册) (stem 变更为 乙册)
b22_split = split_records_half(v5_by_b.get("B22", []), "B22A", "B22B", "商業競爭與資產投資", "乙")
new_records.extend(b22_split)

# --- 6. 卷六 (V6) ---
v6_recs = by_vol["V6"]
v6_by_b = {}
for r in v6_recs:
    v6_by_b.setdefault(r["booklet_code"], []).append(r)

# 原 B23 (164篇) 拆为 B23A (上册) 和 B23B (下册)
b23_split = split_records_half(v6_by_b.get("B23", []), "B23A", "B23B", "公共熱點與事件剖析", "甲")
new_records.extend(b23_split)

# 其余 B24-B30 保持不变
for b in ["B24", "B25", "B26", "B27", "B28", "B29", "B30"]:
    new_records.extend(v6_by_b.get(b, []))

# --- 7. 卷七 (V7) ---
v7_recs = by_vol["V7"]
v7_by_b = {}
for r in v7_recs:
    v7_by_b.setdefault(r["booklet_code"], []).append(r)

# B31A, B31B 保持
new_records.extend(v7_by_b.get("B31A", []))
new_records.extend(v7_by_b.get("B31B", []))

# 原 B32 (191篇) 拆为 B32A 和 B32B
b32_split = split_records_half(v7_by_b.get("B32", []), "B32A", "B32B", "名相辨析與語言牢籠", "乙")
new_records.extend(b32_split)

# 原 B36 (21篇) 并入 B33 (丙册·善惡分野與倫理底線 -> 善惡分野與人性幽微, 58+21=79篇)
b33_merged = v7_by_b.get("B33", []) + v7_by_b.get("B36", [])
for r in b33_merged:
    r["booklet_code"] = "B33"
    r["booklet_name"] = "善惡分野與人性幽微"
    r["booklet_stem"] = "丙"
    r["booklet_stem_title"] = "丙冊 善惡分野與人性幽微"
    r["full_citation"] = "滌除玄覽 · 丙冊 善惡分野與人性幽微"
new_records.extend(b33_merged)

# B34, B35, B37 保持
for b in ["B34", "B35", "B37"]:
    new_records.extend(v7_by_b.get(b, []))

# B38A-L 保持
for stem_ch in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]:
    b = f"B38{stem_ch}"
    new_records.extend(v7_by_b.get(b, []))

# --- 8. 卷八 (V8) 保持 ---
new_records.extend(by_vol["V8"])

print(f"转换后输出记录数: {len(new_records)}")
assert len(new_records) == len(records), "文章记录总数不匹配！"

# 写回文件
with open(CAT_V4, "w", encoding="utf-8") as f:
    for r in new_records:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

shutil.copy2(CAT_V4, CAT_MAIN)
print("已成功写回 CAT_V4 与 CAT_MAIN！")

# 统计最终分册分布
counts = collections.Counter(r["booklet_code"] for r in new_records)
print(f"\n最终分册总数: {len(counts)}")
for b, c in sorted(counts.items()):
    print(f"  {b:6s}: {c:3d} 篇")
