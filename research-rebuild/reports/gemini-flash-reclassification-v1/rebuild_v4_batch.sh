#!/bin/sh
# 在生成脚本目录内直接执行的批量重建脚本
# 必须在 research-rebuild/reports/gemini-flash-reclassification-v1 目录内执行

LOG="rebuild_v4_batch.log"
NODE="/data/service/hnp/bin/node"

echo "=== V4 批量重建 20 个分册 ===" | tee "$LOG"
echo "开始时间: $(date)" | tee -a "$LOG"
echo "" | tee -a "$LOG"

# V1 卷一 (2个，B01已完成)
echo "[1/19] B03..." | tee -a "$LOG"
$NODE build_volume_v1.js B03 >> "$LOG" 2>&1 && echo "  ✓" | tee -a "$LOG" || echo "  ✗" | tee -a "$LOG"

echo "[2/19] B04..." | tee -a "$LOG"
$NODE build_volume_v1.js B04 >> "$LOG" 2>&1 && echo "  ✓" | tee -a "$LOG" || echo "  ✗" | tee -a "$LOG"

# V2 卷二 (1个)
echo "[3/19] B12..." | tee -a "$LOG"
$NODE build_volume_v2.js B12 >> "$LOG" 2>&1 && echo "  ✓" | tee -a "$LOG" || echo "  ✗" | tee -a "$LOG"

# V3-V8 (16个)
echo "[4/19] B15..." | tee -a "$LOG"
$NODE build_volumes_v4_v8.js B15 >> "$LOG" 2>&1 && echo "  ✓" | tee -a "$LOG" || echo "  ✗" | tee -a "$LOG"

echo "[5/19] B17..." | tee -a "$LOG"
$NODE build_volumes_v4_v8.js B17 >> "$LOG" 2>&1 && echo "  ✓" | tee -a "$LOG" || echo "  ✗" | tee -a "$LOG"

echo "[6/19] B18..." | tee -a "$LOG"
$NODE build_volumes_v4_v8.js B18 >> "$LOG" 2>&1 && echo "  ✓" | tee -a "$LOG" || echo "  ✗" | tee -a "$LOG"

echo "[7/19] B19..." | tee -a "$LOG"
$NODE build_volumes_v4_v8.js B19 >> "$LOG" 2>&1 && echo "  ✓" | tee -a "$LOG" || echo "  ✗" | tee -a "$LOG"

echo "[8/19] B20A..." | tee -a "$LOG"
$NODE build_volumes_v4_v8.js B20A >> "$LOG" 2>&1 && echo "  ✓" | tee -a "$LOG" || echo "  ✗" | tee -a "$LOG"

echo "[9/19] B22..." | tee -a "$LOG"
$NODE build_volumes_v4_v8.js B22 >> "$LOG" 2>&1 && echo "  ✓" | tee -a "$LOG" || echo "  ✗" | tee -a "$LOG"

echo "[10/19] B23..." | tee -a "$LOG"
$NODE build_volumes_v4_v8.js B23 >> "$LOG" 2>&1 && echo "  ✓" | tee -a "$LOG" || echo "  ✗" | tee -a "$LOG"

echo "[11/19] B24..." | tee -a "$LOG"
$NODE build_volumes_v4_v8.js B24 >> "$LOG" 2>&1 && echo "  ✓" | tee -a "$LOG" || echo "  ✗" | tee -a "$LOG"

echo "[12/19] B26..." | tee -a "$LOG"
$NODE build_volumes_v4_v8.js B26 >> "$LOG" 2>&1 && echo "  ✓" | tee -a "$LOG" || echo "  ✗" | tee -a "$LOG"

echo "[13/19] B27..." | tee -a "$LOG"
$NODE build_volumes_v4_v8.js B27 >> "$LOG" 2>&1 && echo "  ✓" | tee -a "$LOG" || echo "  ✗" | tee -a "$LOG"

echo "[14/19] B28..." | tee -a "$LOG"
$NODE build_volumes_v4_v8.js B28 >> "$LOG" 2>&1 && echo "  ✓" | tee -a "$LOG" || echo "  ✗" | tee -a "$LOG"

echo "[15/19] B29..." | tee -a "$LOG"
$NODE build_volumes_v4_v8.js B29 >> "$LOG" 2>&1 && echo "  ✓" | tee -a "$LOG" || echo "  ✗" | tee -a "$LOG"

echo "[16/19] B30..." | tee -a "$LOG"
$NODE build_volumes_v4_v8.js B30 >> "$LOG" 2>&1 && echo "  ✓" | tee -a "$LOG" || echo "  ✗" | tee -a "$LOG"

echo "[17/19] B32..." | tee -a "$LOG"
$NODE build_volumes_v4_v8.js B32 >> "$LOG" 2>&1 && echo "  ✓" | tee -a "$LOG" || echo "  ✗" | tee -a "$LOG"

echo "[18/19] B34..." | tee -a "$LOG"
$NODE build_volumes_v4_v8.js B34 >> "$LOG" 2>&1 && echo "  ✓" | tee -a "$LOG" || echo "  ✗" | tee -a "$LOG"

echo "[19/19] B39..." | tee -a "$LOG"
$NODE build_volumes_v4_v8.js B39 >> "$LOG" 2>&1 && echo "  ✓" | tee -a "$LOG" || echo "  ✗" | tee -a "$LOG"

echo "" | tee -a "$LOG"
echo "=== 完成 ===" | tee -a "$LOG"
echo "结束时间: $(date)" | tee -a "$LOG"
echo "详细日志: $(pwd)/$LOG"
