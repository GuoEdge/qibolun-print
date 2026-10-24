#!/bin/sh
# 批量重建剩余 15 个分册（卷三至卷八）

cd /storage/Users/currentUser/Documents/岐伯论/research-rebuild/reports/gemini-flash-reclassification-v1

NODE=/data/service/hnp/bin/node

# 需要重建的分册列表（从 v4 新增报告中提取）
BOOKLETS="B15 B17 B18 B19 B22 B23 B24 B26 B27 B28 B29 B30 B32 B34 B39"

echo "开始批量重建 15 个分册..."
SUCCESS=0
FAILED=0

for CODE in $BOOKLETS; do
    echo ""
    echo "=== 正在生成 $CODE ==="
    if $NODE build_volumes_v4_v8.js $CODE; then
        SUCCESS=$((SUCCESS + 1))
        echo "✓ $CODE 完成"
    else
        FAILED=$((FAILED + 1))
        echo "✗ $CODE 失败"
    fi
done

echo ""
echo "====================="
echo "总计: $((SUCCESS + FAILED)) 个分册"
echo "成功: $SUCCESS"
echo "失败: $FAILED"
