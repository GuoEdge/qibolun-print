#!/usr/bin/env python3
"""
重新构建《岐伯论》各卷 Word (.docx) 文档管线。
支持单卷、多卷或全量串行构建，并带有详尽的进度打印与错误拦截。
"""

import os
import sys
import subprocess
import time
from pathlib import Path

ROOT = Path('/storage/Users/currentUser/Documents/岐伯论')
BASE = ROOT / 'research-rebuild/reports/gemini-flash-reclassification-v1'

TASKS = [
    # 卷一 (11 册)
    ('v1', 'B01', '卷一·甲册·幼兒啟蒙與性情習慣'),
    ('v1', 'B02A', '卷一·乙册·上·學業功課與學校日常'),
    ('v1', 'B02B', '卷一·乙册·中·學業功課與學校日常'),
    ('v1', 'B02C', '卷一·乙册·下·學業功課與學校日常'),
    ('v1', 'B03', '卷一·丙册·言傳身教與獎懲邊界'),
    ('v1', 'B04', '卷一·丁册·親子溝通與青春叛逆'),
    ('v1', 'B05', '卷一·戊册·長輩相處與精神解綁'),
    ('v1', 'B06', '卷一·己册·成年子女自立與邊界'),
    ('v1', 'B07', '卷一·庚册·手足同胞與家族親戚'),
    ('v1', 'B08', '卷一·辛册·宗族傳承與喪祭奠儀'),
    ('v1', 'B38F', '卷一·壬册·庭訓教化與親恩相報'),

    # 卷二 (4 册)
    ('v2', 'B11', '卷二·甲册·擇偶標準與兩性吸引'),
    ('v2', 'B12', '卷二·乙册·婚姻存續與夫妻日常'),
    ('v2', 'B13', '卷二·丙册·親密背叛與離異止損'),
    ('v2', 'B38E', '卷二·丁册·情義本真與兩性名理'),

    # 卷三 (5 册)
    ('v4_v8', 'B14', '卷三·甲册·人情往來與禮數分寸'),
    ('v4_v8', 'B15', '卷三·乙册·社交距離與孤立自處'),
    ('v4_v8', 'B16', '卷三·丙册·危機識人與權義守界'),
    ('v4_v8', 'B38C', '卷三·丁册·上·處世分寸與人我進退'),
    ('v4_v8', 'B38D', '卷三·丁册·下·處世分寸與人我進退'),

    # 卷四 (3 册)
    ('v4_v8', 'B17A', '卷四·甲册·上·情志平復與容貌自和'),
    ('v4_v8', 'B17B', '卷四·甲册·下·情志平復與容貌自和'),
    ('v4_v8', 'B18', '卷四·乙册·知行合一與作息身息'),

    # 卷五 (5 册)
    ('v4_v8', 'B20A', '卷五·甲册·上·職場彙報與權責留痕'),
    ('v4_v8', 'B20B', '卷五·甲册·中·職場彙報與權責留痕'),
    ('v4_v8', 'B20C', '卷五·甲册·下·職場彙報與權責留痕'),
    ('v4_v8', 'B22A', '卷五·乙册·上·商業競爭與資產投資'),
    ('v4_v8', 'B22B', '卷五·乙册·下·商業競爭與資產投資'),

    # 卷六 (11 册)
    ('v4_v8', 'B23A', '卷六·甲册·上·公共熱點與事件剖析'),
    ('v4_v8', 'B23B', '卷六·甲册·下·公共熱點與事件剖析'),
    ('v4_v8', 'B24', '卷六·乙册·青年心境與躺平反思'),
    ('v4_v8', 'B25', '卷六·丙册·網絡生態與群體極化'),
    ('v4_v8', 'B26', '卷六·丁册·性別議題與兩性輿論'),
    ('v4_v8', 'B27', '卷六·戊册·教育體制與社會流動'),
    ('v4_v8', 'B28', '卷六·己册·消費主義與生活觀念'),
    ('v4_v8', 'B29', '卷六·庚册·現代科技與工具反思'),
    ('v4_v8', 'B30', '卷六·辛册·文明演進與社會秩序'),
    ('v4_v8', 'B36A', '卷六·壬册·上·時局經緯與家國論衡'),
    ('v4_v8', 'B36B', '卷六·壬册·下·時局經緯與家國論衡'),

    # 卷七 (12 册)
    ('v4_v8', 'B31A', '卷七·甲册·上·存在本質與生命意義'),
    ('v4_v8', 'B31B', '卷七·甲册·下·存在本質與生命意義'),
    ('v4_v8', 'B32A', '卷七·乙册·上·名相辨析與語言牢籠'),
    ('v4_v8', 'B32B', '卷七·乙册·下·名相辨析與語言牢籠'),
    ('v4_v8', 'B33', '卷七·丙册·善惡分野與人性幽微'),
    ('v4_v8', 'B34', '卷七·丁册·認識局限與心智模型'),
    ('v4_v8', 'B35', '卷七·戊册·命途因果與得失隨緣'),
    ('v4_v8', 'B37', '卷七·己册·神聖敬畏與信仰維度'),
    ('v4_v8', 'B38A', '卷七·庚册·子·心性自持與精神獨立'),
    ('v4_v8', 'B38B', '卷七·庚册·丑·心性自持與精神獨立'),
    ('v4_v8', 'B38I', '卷七·庚册·寅·世情人性與義理雜談'),
    ('v4_v8', 'B38J', '卷七·庚册·卯·世情人性與義理雜談'),

    # 卷八 (4 册)
    ('v4_v8', 'B38G', '卷八·丙册·格物致知與機巧萬類'),
    ('v4_v8', 'B38H', '卷八·丁册·治家器術與聲藝百工'),
    ('v4_v8', 'B39', '卷八·甲册·藝能創作與生活美學'),
    ('v4_v8', 'B40', '卷八·乙册·治亂興亡與國家工程')
]

SCRIPT_MAP = {
    'v1': 'build_volume_v1.js',
    'v2': 'build_volume_v2.js',
    'v4_v8': 'build_volumes_v4_v8.js'
}

def run_booklet(builder_type, code, title, idx, total):
    script_name = SCRIPT_MAP[builder_type]
    cmd = ['node', script_name, code]
    print(f"[{idx}/{total}] 正在构建: {title} ({code})...")
    start_t = time.time()
    res = subprocess.run(cmd, cwd=str(BASE), capture_output=True, text=True)
    cost = time.time() - start_t
    if res.returncode == 0:
        # 提取关键输出行
        out_lines = [l.strip() for l in res.stdout.split('\n') if l.strip()]
        summary = ''
        for l in out_lines:
            if '预计物理总页' in l or '大小' in l or '通过' in l:
                summary += ' | ' + l
        print(f"  ✓ 成功 ({cost:.1f}s){summary}")
        return True, cost, ""
    else:
        err_msg = res.stderr.strip() or res.stdout.strip()
        print(f"  ✗ 失败 ({cost:.1f}s):\n{err_msg}")
        return False, cost, err_msg

def main():
    target_pattern = sys.argv[1].upper() if len(sys.argv) > 1 else 'ALL'
    
    selected = []
    for item in TASKS:
        builder, code, desc = item
        if target_pattern == 'ALL':
            selected.append(item)
        elif target_pattern in code or target_pattern in desc:
            selected.append(item)
        elif target_pattern.startswith('V') and desc.startswith(f"卷{target_pattern[1:]}"):
            selected.append(item)
            
    print(f"==================================================")
    print(f"《岐伯论》DOCX 重新生成流水线")
    print(f"目标范围: {target_pattern} | 待生成分册数: {len(selected)}")
    print(f"==================================================")
    
    passed = 0
    failed = []
    total_cost = 0.0
    
    for i, (builder, code, desc) in enumerate(selected, 1):
        ok, c, err = run_booklet(builder, code, desc, i, len(selected))
        total_cost += c
        if ok:
            passed += 1
        else:
            failed.append((code, desc, err))
        # 稳健间隔，防止高频调用引发内存毛刺
        time.sleep(0.3)
        
    print(f"==================================================")
    print(f"构建完成: 成功 {passed}/{len(selected)} 册，耗时 {total_cost:.1f}s")
    if failed:
        print(f"失败分册 ({len(failed)}):")
        for f_code, f_desc, f_err in failed:
            print(f" - {f_code} ({f_desc}): {f_err[:120]}")
    print(f"==================================================")

if __name__ == '__main__':
    main()
