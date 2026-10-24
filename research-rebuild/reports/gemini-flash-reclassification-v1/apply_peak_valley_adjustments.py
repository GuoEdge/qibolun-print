#!/usr/bin/env python3
"""
执行《岐伯论》分册削峰填谷重构：
1. 削峰：
   - B17 (171篇) -> B17A (86篇, 上册) / B17B (85篇, 下册)
   - B22 (197篇) -> B22A (99篇, 上册) / B22B (98篇, 下册)
   - B23 (164篇) -> B23A (82篇, 上册) / B23B (82篇, 下册)
   - B32 (191篇) -> B32A (96篇, 上册) / B32B (95篇, 下册)

2. 填谷：
   - 卷一：
     B05 (12篇) + B07 (4篇) -> B05 (16篇，戊册·長輩相處與精神解綁)
     原 B06 (111篇) -> B06 (保持己册·成年子女自立與邊界)
     原 B08 (45篇) -> B07 (调整为庚册·手足同胞與家族親戚)
     原 B09 (33篇) + B10 (10篇) -> B08 (43篇，辛册·宗族傳承與喪祭奠儀)
     (卷一原有 B01, B02A/B/C, B03, B04, B05, B06, B07, B08 共 10 本)

   - 卷四：
     原 B18 (16篇) + B19 (68篇) -> B18 (84篇，乙册·知行合一與作息身息)
     B17A (甲册·上), B17B (甲册·下), B18 (乙册) 共 3 本

   - 卷五：
     原 B21 (17篇) 并入 B20C -> B20C (134篇，甲·下册·職場彙報與權責留痕·下册)
     B20A, B20B, B20C, B22A, B22B 共 5 本

   - 卷七：
     原 B36 (21篇) 并入 B33 -> B33 (79篇，丙册·善惡分野與人性幽微)
"""

import json
import shutil
import time
from pathlib import Path

BASE = Path("/storage/Users/currentUser/Documents/岐伯论/research-rebuild/reports/gemini-flash-reclassification-v1")
CAT_V4 = BASE / "workbook-40b-all-catalog-v4.jsonl"
CAT_MAIN = BASE / "workbook-40b-all-catalog.jsonl"

def main():
    # 1. 备份现有编目文件
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    bak_v4 = BASE / f"workbook-40b-all-catalog-v4.jsonl.bak_peakvalley_{timestamp}"
    bak_main = BASE / f"workbook-40b-all-catalog.jsonl.bak_peakvalley_{timestamp}"
    shutil.copy2(CAT_V4, bak_v4)
    shutil.copy2(CAT_MAIN, bak_main)
    print(f"已备份原始编目至:\n  {bak_v4}\n  {bak_main}")

    with open(CAT_V4, "r", encoding="utf-8") as f:
        records = [json.loads(line) for line in f if line.strip()]

    print(f"读取到原始记录总数: {len(records)}")

    # 分卷分册索引
    # 对每种情况进行重命名与重分配
    # 先把 records 按原顺序分组提取或逐条处理
    
    # 统计原册
    b_records = {}
    for r in records:
        b_records.setdefault(r["booklet_code"], []).append(r)

    # 1. 削峰
    # B17 -> B17A, B17B
    b17_list = b_records.get("B17", [])
    mid17 = (len(b17_list) + 1) // 2
    for i, r in enumerate(b17_list):
        if i < mid17:
            r["booklet_code"] = "B17A"
            r["booklet_name"] = "情志平復與容貌自和·上冊"
            r["booklet_stem"] = "甲·上"
            r["booklet_stem_title"] = "甲·上冊 情志平復與容貌自和·上冊"
            r["full_citation"] = "存神調息 · 甲·上冊 情志平復與容貌自和·上冊"
        else:
            r["booklet_code"] = "B17B"
            r["booklet_name"] = "情志平復與容貌自和·下冊"
            r["booklet_stem"] = "甲·下"
            r["booklet_stem_title"] = "甲·下冊 情志平復與容貌自和·下冊"
            r["full_citation"] = "存神調息 · 甲·下冊 情志平復與容貌自和·下冊"

    # B22 -> B22A, B22B
    b22_list = b_records.get("B22", [])
    mid22 = (len(b22_list) + 1) // 2
    for i, r in enumerate(b22_list):
        if i < mid22:
            r["booklet_code"] = "B22A"
            r["booklet_name"] = "商業競爭與資產投資·上冊"
            r["booklet_stem"] = "乙·上"
            r["booklet_stem_title"] = "乙·上冊 商業競爭與資產投資·上冊"
            r["full_citation"] = "度勢居貨 · 乙·上冊 商業競爭與資產投資·上冊"
        else:
            r["booklet_code"] = "B22B"
            r["booklet_name"] = "商業競爭與資產投資·下冊"
            r["booklet_stem"] = "乙·下"
            r["booklet_stem_title"] = "乙·下冊 商業競爭與資產投資·下冊"
            r["full_citation"] = "度勢居貨 · 乙·下冊 商業競爭與資產投资·下冊"

    # B23 -> B23A, B23B
    b23_list = b_records.get("B23", [])
    mid23 = (len(b23_list) + 1) // 2
    for i, r in enumerate(b23_list):
        if i < mid23:
            r["booklet_code"] = "B23A"
            r["booklet_name"] = "公共熱點與事件剖析·上冊"
            r["booklet_stem"] = "甲·上"
            r["booklet_stem_title"] = "甲·上冊 公共熱點與事件剖析·上冊"
            r["full_citation"] = "觀風察變 · 甲·上冊 公共熱點與事件剖析·上冊"
        else:
            r["booklet_code"] = "B23B"
            r["booklet_name"] = "公共熱點與事件剖析·下冊"
            r["booklet_stem"] = "甲·下"
            r["booklet_stem_title"] = "甲·下冊 公共熱點與事件剖析·下冊"
            r["full_citation"] = "觀風察變 · 甲·下冊 公共熱點與事件剖析·下冊"

    # B32 -> B32A, B32B
    b32_list = b_records.get("B32", [])
    mid32 = (len(b32_list) + 1) // 2
    for i, r in enumerate(b32_list):
        if i < mid32:
            r["booklet_code"] = "B32A"
            r["booklet_name"] = "名相辨析與語言牢籠·上冊"
            r["booklet_stem"] = "乙·上"
            r["booklet_stem_title"] = "乙·上冊 名相辨析與語言牢籠·上冊"
            r["full_citation"] = "滌除玄覽 · 乙·上冊 名相辨析與語言牢籠·上冊"
        else:
            r["booklet_code"] = "B32B"
            r["booklet_name"] = "名相辨析與語言牢籠·下冊"
            r["booklet_stem"] = "乙·下"
            r["booklet_stem_title"] = "乙·下冊 名相辨析與語言牢籠·下冊"
            r["full_citation"] = "滌除玄覽 · 乙·下冊 名相辨析與語言牢籠·下冊"

    # 2. 填谷（合并）
    # 卷一：
    # B05 (12) + B07 (4) -> B05 (戊冊·長輩相處與精神解綁)
    for r in b_records.get("B05", []) + b_records.get("B07", []):
        r["booklet_code"] = "B05"
        r["booklet_name"] = "長輩相處與精神解綁"
        r["booklet_stem"] = "戊"
        r["booklet_stem_title"] = "戊冊 長輩相處與精神解綁"
        r["full_citation"] = "本根敦倫 · 戊冊 長輩相處與精神解綁"

    # 原 B08 (45) -> 改为 B07 (庚冊·手足同胞與家族親戚)
    for r in b_records.get("B08", []):
        r["booklet_code"] = "B07"
        r["booklet_name"] = "手足同胞與家族親戚"
        r["booklet_stem"] = "庚"
        r["booklet_stem_title"] = "庚冊 手足同胞與家族親戚"
        r["full_citation"] = "本根敦倫 · 庚冊 手足同胞與家族親戚"

    # 原 B09 (33) + B10 (10) -> 改为 B08 (辛冊·宗族傳承與喪祭奠儀)
    for r in b_records.get("B09", []) + b_records.get("B10", []):
        r["booklet_code"] = "B08"
        r["booklet_name"] = "宗族傳承與喪祭奠儀"
        r["booklet_stem"] = "辛"
        r["booklet_stem_title"] = "辛冊 宗族傳承與喪祭奠儀"
        r["full_citation"] = "本根敦倫 · 辛冊 宗族傳承與喪祭奠儀"

    # 卷四：
    # 原 B18 (16) + B19 (68) -> B18 (乙冊·知行合一與作息身息)
    for r in b_records.get("B18", []) + b_records.get("B19", []):
        r["booklet_code"] = "B18"
        r["booklet_name"] = "知行合一與作息身息"
        r["booklet_stem"] = "乙"
        r["booklet_stem_title"] = "乙冊 知行合一與作息身息"
        r["full_citation"] = "存神調息 · 乙冊 知行合一與作息身息"

    # 卷五：
    # 原 B21 (17) 并入 B20C (甲·下冊·職場彙報與權責留痕·下冊)
    for r in b_records.get("B21", []):
        r["booklet_code"] = "B20C"
        r["booklet_name"] = "職場彙報與權責留痕·下冊"
        r["booklet_stem"] = "甲·下"
        r["booklet_stem_title"] = "甲·下冊 職場彙報與權責留痕·下冊"
        r["full_citation"] = "度勢居貨 · 甲·下冊 職場彙報與權責留痕·下冊"

    # 卷七：
    # 原 B36 (21) 并入 B33 (丙冊·善惡分野與人性幽微)
    for r in b_records.get("B36", []):
        r["booklet_code"] = "B33"
        r["booklet_name"] = "善惡分野與人性幽微"
        r["booklet_stem"] = "丙"
        r["booklet_stem_title"] = "丙冊 善惡分野與人性幽微"
        r["full_citation"] = "滌除玄覽 · 丙冊 善惡分野與人性幽微"

    # 原 B33 的旧文章名也统一升级为 善惡分野與人性幽微
    for r in b_records.get("B33", []):
        r["booklet_name"] = "善惡分野與人性幽微"
        r["booklet_stem_title"] = "丙冊 善惡分野與人性幽微"
        r["full_citation"] = "滌除玄覽 · 丙冊 善惡分野與人性幽微"

    # 重新输出并刷新 ordinal
    with open(CAT_V4, "w", encoding="utf-8") as f1, open(CAT_MAIN, "w", encoding="utf-8") as f2:
        for r in records:
            line = json.dumps(r, ensure_ascii=False)
            f1.write(line + "\n")
            f2.write(line + "\n")

    print("已成功写入新编目文件!")

if __name__ == "__main__":
    main()
