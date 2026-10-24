#!/bin/sh
# V4 新增 29 篇文章影响的 20 个分册批量重建脚本（逐个执行）
# 2026-10-09

BASE="/storage/Users/currentUser/Documents/岐伯论/research-rebuild/reports/gemini-flash-reclassification-v1"
NODE="/data/service/hnp/bin/node"
LOG="/storage/Users/currentUser/Documents/岐伯论/rebuild_v4_detailed.log"

echo "=== 开始重建受 v4 新增文章影响的 20 个分册 ===" | tee "$LOG"
echo "" | tee -a "$LOG"

# V1 卷一 (5 篇新增: B01/B03/B04)
echo ">>> [1/20] 卷一 B01..." | tee -a "$LOG"
cd "$BASE" && $NODE build_volume_v1.js B01 >> "$LOG" 2>&1
if [ $? -eq 0 ]; then echo "    ✓ B01 完成" | tee -a "$LOG"; else echo "    ✗ B01 失败" | tee -a "$LOG"; exit 1; fi

echo ">>> [2/20] 卷一 B03..." | tee -a "$LOG"
cd "$BASE" && $NODE build_volume_v1.js B03 >> "$LOG" 2>&1
if [ $? -eq 0 ]; then echo "    ✓ B03 完成" | tee -a "$LOG"; else echo "    ✗ B03 失败" | tee -a "$LOG"; exit 1; fi

echo ">>> [3/20] 卷一 B04..." | tee -a "$LOG"
cd "$BASE" && $NODE build_volume_v1.js B04 >> "$LOG" 2>&1
if [ $? -eq 0 ]; then echo "    ✓ B04 完成" | tee -a "$LOG"; else echo "    ✗ B04 失败" | tee -a "$LOG"; exit 1; fi

# V2 卷二 (1 篇新增: B12)
echo ">>> [4/20] 卷二 B12..." | tee -a "$LOG"
cd "$BASE" && $NODE build_volume_v2.js B12 >> "$LOG" 2>&1
if [ $? -eq 0 ]; then echo "    ✓ B12 完成" | tee -a "$LOG"; else echo "    ✗ B12 失败" | tee -a "$LOG"; exit 1; fi

# V3 卷三 (3 篇新增: B15)
echo ">>> [5/20] 卷三 B15..." | tee -a "$LOG"
cd "$BASE" && $NODE build_volumes_v4_v8.js B15 >> "$LOG" 2>&1
if [ $? -eq 0 ]; then echo "    ✓ B15 完成" | tee -a "$LOG"; else echo "    ✗ B15 失败" | tee -a "$LOG"; exit 1; fi

# V4 卷四 (5 篇新增: B17/B18/B19)
echo ">>> [6/20] 卷四 B17..." | tee -a "$LOG"
cd "$BASE" && $NODE build_volumes_v4_v8.js B17 >> "$LOG" 2>&1
if [ $? -eq 0 ]; then echo "    ✓ B17 完成" | tee -a "$LOG"; else echo "    ✗ B17 失败" | tee -a "$LOG"; exit 1; fi

echo ">>> [7/20] 卷四 B18..." | tee -a "$LOG"
cd "$BASE" && $NODE build_volumes_v4_v8.js B18 >> "$LOG" 2>&1
if [ $? -eq 0 ]; then echo "    ✓ B18 完成" | tee -a "$LOG"; else echo "    ✗ B18 失败" | tee -a "$LOG"; exit 1; fi

echo ">>> [8/20] 卷四 B19..." | tee -a "$LOG"
cd "$BASE" && $NODE build_volumes_v4_v8.js B19 >> "$LOG" 2>&1
if [ $? -eq 0 ]; then echo "    ✓ B19 完成" | tee -a "$LOG"; else echo "    ✗ B19 失败" | tee -a "$LOG"; exit 1; fi

# V5 卷五 (2 篇新增: B20A/B22)
echo ">>> [9/20] 卷五 B20A..." | tee -a "$LOG"
cd "$BASE" && $NODE build_volumes_v4_v8.js B20A >> "$LOG" 2>&1
if [ $? -eq 0 ]; then echo "    ✓ B20A 完成" | tee -a "$LOG"; else echo "    ✗ B20A 失败" | tee -a "$LOG"; exit 1; fi

echo ">>> [10/20] 卷五 B22..." | tee -a "$LOG"
cd "$BASE" && $NODE build_volumes_v4_v8.js B22 >> "$LOG" 2>&1
if [ $? -eq 0 ]; then echo "    ✓ B22 完成" | tee -a "$LOG"; else echo "    ✗ B22 失败" | tee -a "$LOG"; exit 1; fi

# V6 卷六 (9 篇新增: B23/B24/B26/B27/B28/B29/B30)
echo ">>> [11/20] 卷六 B23..." | tee -a "$LOG"
cd "$BASE" && $NODE build_volumes_v4_v8.js B23 >> "$LOG" 2>&1
if [ $? -eq 0 ]; then echo "    ✓ B23 完成" | tee -a "$LOG"; else echo "    ✗ B23 失败" | tee -a "$LOG"; exit 1; fi

echo ">>> [12/20] 卷六 B24..." | tee -a "$LOG"
cd "$BASE" && $NODE build_volumes_v4_v8.js B24 >> "$LOG" 2>&1
if [ $? -eq 0 ]; then echo "    ✓ B24 完成" | tee -a "$LOG"; else echo "    ✗ B24 失败" | tee -a "$LOG"; exit 1; fi

echo ">>> [13/20] 卷六 B26..." | tee -a "$LOG"
cd "$BASE" && $NODE build_volumes_v4_v8.js B26 >> "$LOG" 2>&1
if [ $? -eq 0 ]; then echo "    ✓ B26 完成" | tee -a "$LOG"; else echo "    ✗ B26 失败" | tee -a "$LOG"; exit 1; fi

echo ">>> [14/20] 卷六 B27..." | tee -a "$LOG"
cd "$BASE" && $NODE build_volumes_v4_v8.js B27 >> "$LOG" 2>&1
if [ $? -eq 0 ]; then echo "    ✓ B27 完成" | tee -a "$LOG"; else echo "    ✗ B27 失败" | tee -a "$LOG"; exit 1; fi

echo ">>> [15/20] 卷六 B28..." | tee -a "$LOG"
cd "$BASE" && $NODE build_volumes_v4_v8.js B28 >> "$LOG" 2>&1
if [ $? -eq 0 ]; then echo "    ✓ B28 完成" | tee -a "$LOG"; else echo "    ✗ B28 失败" | tee -a "$LOG"; exit 1; fi

echo ">>> [16/20] 卷六 B29..." | tee -a "$LOG"
cd "$BASE" && $NODE build_volumes_v4_v8.js B29 >> "$LOG" 2>&1
if [ $? -eq 0 ]; then echo "    ✓ B29 完成" | tee -a "$LOG"; else echo "    ✗ B29 失败" | tee -a "$LOG"; exit 1; fi

echo ">>> [17/20] 卷六 B30..." | tee -a "$LOG"
cd "$BASE" && $NODE build_volumes_v4_v8.js B30 >> "$LOG" 2>&1
if [ $? -eq 0 ]; then echo "    ✓ B30 完成" | tee -a "$LOG"; else echo "    ✗ B30 失败" | tee -a "$LOG"; exit 1; fi

# V7 卷七 (3 篇新增: B32/B34)
echo ">>> [18/20] 卷七 B32..." | tee -a "$LOG"
cd "$BASE" && $NODE build_volumes_v4_v8.js B32 >> "$LOG" 2>&1
if [ $? -eq 0 ]; then echo "    ✓ B32 完成" | tee -a "$LOG"; else echo "    ✗ B32 失败" | tee -a "$LOG"; exit 1; fi

echo ">>> [19/20] 卷七 B34..." | tee -a "$LOG"
cd "$BASE" && $NODE build_volumes_v4_v8.js B34 >> "$LOG" 2>&1
if [ $? -eq 0 ]; then echo "    ✓ B34 完成" | tee -a "$LOG"; else echo "    ✗ B34 失败" | tee -a "$LOG"; exit 1; fi

# V8 卷八 (1 篇新增: B39)
echo ">>> [20/20] 卷八 B39..." | tee -a "$LOG"
cd "$BASE" && $NODE build_volumes_v4_v8.js B39 >> "$LOG" 2>&1
if [ $? -eq 0 ]; then echo "    ✓ B39 完成" | tee -a "$LOG"; else echo "    ✗ B39 失败" | tee -a "$LOG"; exit 1; fi

echo "" | tee -a "$LOG"
echo "=== 全部 20 个分册重建完成 ===" | tee -a "$LOG"
echo "详细日志: $LOG"
