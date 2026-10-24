#!/bin/sh
# V4 简化版：直接在正确目录执行，不使用 cd
BASE="/storage/Users/currentUser/Documents/岐伯论/research-rebuild/reports/gemini-flash-reclassification-v1"
NODE="/data/service/hnp/bin/node"
LOG="/storage/Users/currentUser/Documents/岐伯论/rebuild_v4_progress.log"

echo "=== 开始重建 20 个分册 ===" | tee "$LOG"

# V1 卷一 (3个)
echo "[1/20] B01..." | tee -a "$LOG"
$NODE "$BASE/build_volume_v1.js" B01 >> "$LOG" 2>&1 && echo "  ✓ B01" | tee -a "$LOG" || echo "  ✗ B01" | tee -a "$LOG"

echo "[2/20] B03..." | tee -a "$LOG"
$NODE "$BASE/build_volume_v1.js" B03 >> "$LOG" 2>&1 && echo "  ✓ B03" | tee -a "$LOG" || echo "  ✗ B03" | tee -a "$LOG"

echo "[3/20] B04..." | tee -a "$LOG"
$NODE "$BASE/build_volume_v1.js" B04 >> "$LOG" 2>&1 && echo "  ✓ B04" | tee -a "$LOG" || echo "  ✗ B04" | tee -a "$LOG"

# V2 卷二 (1个)
echo "[4/20] B12..." | tee -a "$LOG"
$NODE "$BASE/build_volume_v2.js" B12 >> "$LOG" 2>&1 && echo "  ✓ B12" | tee -a "$LOG" || echo "  ✗ B12" | tee -a "$LOG"

# V3 卷三 (1个)
echo "[5/20] B15..." | tee -a "$LOG"
$NODE "$BASE/build_volumes_v4_v8.js" B15 >> "$LOG" 2>&1 && echo "  ✓ B15" | tee -a "$LOG" || echo "  ✗ B15" | tee -a "$LOG"

# V4 卷四 (3个)
echo "[6/20] B17..." | tee -a "$LOG"
$NODE "$BASE/build_volumes_v4_v8.js" B17 >> "$LOG" 2>&1 && echo "  ✓ B17" | tee -a "$LOG" || echo "  ✗ B17" | tee -a "$LOG"

echo "[7/20] B18..." | tee -a "$LOG"
$NODE "$BASE/build_volumes_v4_v8.js" B18 >> "$LOG" 2>&1 && echo "  ✓ B18" | tee -a "$LOG" || echo "  ✗ B18" | tee -a "$LOG"

echo "[8/20] B19..." | tee -a "$LOG"
$NODE "$BASE/build_volumes_v4_v8.js" B19 >> "$LOG" 2>&1 && echo "  ✓ B19" | tee -a "$LOG" || echo "  ✗ B19" | tee -a "$LOG"

# V5 卷五 (2个)
echo "[9/20] B20A..." | tee -a "$LOG"
$NODE "$BASE/build_volumes_v4_v8.js" B20A >> "$LOG" 2>&1 && echo "  ✓ B20A" | tee -a "$LOG" || echo "  ✗ B20A" | tee -a "$LOG"

echo "[10/20] B22..." | tee -a "$LOG"
$NODE "$BASE/build_volumes_v4_v8.js" B22 >> "$LOG" 2>&1 && echo "  ✓ B22" | tee -a "$LOG" || echo "  ✗ B22" | tee -a "$LOG"

# V6 卷六 (7个)
echo "[11/20] B23..." | tee -a "$LOG"
$NODE "$BASE/build_volumes_v4_v8.js" B23 >> "$LOG" 2>&1 && echo "  ✓ B23" | tee -a "$LOG" || echo "  ✗ B23" | tee -a "$LOG"

echo "[12/20] B24..." | tee -a "$LOG"
$NODE "$BASE/build_volumes_v4_v8.js" B24 >> "$LOG" 2>&1 && echo "  ✓ B24" | tee -a "$LOG" || echo "  ✗ B24" | tee -a "$LOG"

echo "[13/20] B26..." | tee -a "$LOG"
$NODE "$BASE/build_volumes_v4_v8.js" B26 >> "$LOG" 2>&1 && echo "  ✓ B26" | tee -a "$LOG" || echo "  ✗ B26" | tee -a "$LOG"

echo "[14/20] B27..." | tee -a "$LOG"
$NODE "$BASE/build_volumes_v4_v8.js" B27 >> "$LOG" 2>&1 && echo "  ✓ B27" | tee -a "$LOG" || echo "  ✗ B27" | tee -a "$LOG"

echo "[15/20] B28..." | tee -a "$LOG"
$NODE "$BASE/build_volumes_v4_v8.js" B28 >> "$LOG" 2>&1 && echo "  ✓ B28" | tee -a "$LOG" || echo "  ✗ B28" | tee -a "$LOG"

echo "[16/20] B29..." | tee -a "$LOG"
$NODE "$BASE/build_volumes_v4_v8.js" B29 >> "$LOG" 2>&1 && echo "  ✓ B29" | tee -a "$LOG" || echo "  ✗ B29" | tee -a "$LOG"

echo "[17/20] B30..." | tee -a "$LOG"
$NODE "$BASE/build_volumes_v4_v8.js" B30 >> "$LOG" 2>&1 && echo "  ✓ B30" | tee -a "$LOG" || echo "  ✗ B30" | tee -a "$LOG"

# V7 卷七 (2个)
echo "[18/20] B32..." | tee -a "$LOG"
$NODE "$BASE/build_volumes_v4_v8.js" B32 >> "$LOG" 2>&1 && echo "  ✓ B32" | tee -a "$LOG" || echo "  ✗ B32" | tee -a "$LOG"

echo "[19/20] B34..." | tee -a "$LOG"
$NODE "$BASE/build_volumes_v4_v8.js" B34 >> "$LOG" 2>&1 && echo "  ✓ B34" | tee -a "$LOG" || echo "  ✗ B34" | tee -a "$LOG"

# V8 卷八 (1个)
echo "[20/20] B39..." | tee -a "$LOG"
$NODE "$BASE/build_volumes_v4_v8.js" B39 >> "$LOG" 2>&1 && echo "  ✓ B39" | tee -a "$LOG" || echo "  ✗ B39" | tee -a "$LOG"

echo "" | tee -a "$LOG"
echo "=== 完成 ===" | tee -a "$LOG"
echo "详细日志: $LOG"
