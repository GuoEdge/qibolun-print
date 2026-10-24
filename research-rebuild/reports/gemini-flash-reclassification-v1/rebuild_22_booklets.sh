#!/bin/sh
# 批量重建22个受影响分册的DOCX
# 这些分册包含了37篇新增文章，需要更新二维码

set -e

echo "================================================================"
echo "批量重建22个受影响分册"
echo "================================================================"
echo ""

TOTAL_COUNT=0
SUCCESS_COUNT=0
FAIL_COUNT=0

# 函数：构建单个分册
build_booklet() {
    local code="$1"
    local script="$2"
    
    echo "----------------------------------------"
    echo "构建 $code (使用 $script) ..."
    echo "----------------------------------------"
    
    if node "$script" "$code"; then
        SUCCESS_COUNT=$((SUCCESS_COUNT + 1))
        echo "✓ $code 构建成功"
    else
        FAIL_COUNT=$((FAIL_COUNT + 1))
        echo "✗ $code 构建失败"
    fi
    
    TOTAL_COUNT=$((TOTAL_COUNT + 1))
    echo ""
}

# 批次1: B01 (特殊脚本)
echo "========================================"
echo "批次1: B01 (卷一·甲册)"
echo "========================================"
build_booklet "B01" "build_booklet_B01_v3.js"

# 批次2: V1其他分册 (6册，包括B02的3个子册)
echo "========================================"
echo "批次2: 卷一其他分册 (6册)"
echo "========================================"
build_booklet "B02A" "build_volume_v1.js"
build_booklet "B02B" "build_volume_v1.js"
build_booklet "B02C" "build_volume_v1.js"
build_booklet "B06" "build_volume_v1.js"
build_booklet "B08" "build_volume_v1.js"

# 批次3: V2 (3册)
echo "========================================"
echo "批次3: 卷二 (3册)"
echo "========================================"
build_booklet "B11" "build_volume_v2.js"
build_booklet "B12" "build_volume_v2.js"
build_booklet "B13" "build_volume_v2.js"

# 批次4: V3-V8使用统一脚本 (15册)
echo "========================================"
echo "批次4: 卷三至卷八 (15册)"
echo "========================================"
# V3
build_booklet "B15" "build_volumes_v4_v8.js"

# V4
build_booklet "B17" "build_volumes_v4_v8.js"
build_booklet "B18" "build_volumes_v4_v8.js"
build_booklet "B19" "build_volumes_v4_v8.js"

# V5
build_booklet "B20C" "build_volumes_v4_v8.js"
build_booklet "B22" "build_volumes_v4_v8.js"

# V6
build_booklet "B24" "build_volumes_v4_v8.js"
build_booklet "B26" "build_volumes_v4_v8.js"
build_booklet "B28" "build_volumes_v4_v8.js"
build_booklet "B29" "build_volumes_v4_v8.js"

# V7
build_booklet "B32" "build_volumes_v4_v8.js"
build_booklet "B35" "build_volumes_v4_v8.js"
build_booklet "B37" "build_volumes_v4_v8.js"
build_booklet "B38L" "build_volumes_v4_v8.js"

# V8
build_booklet "B40" "build_volumes_v4_v8.js"

# 总结
echo ""
echo "================================================================"
echo "批量重建完成"
echo "================================================================"
echo "总计: $TOTAL_COUNT 册"
echo "成功: $SUCCESS_COUNT 册"
echo "失败: $FAIL_COUNT 册"
echo "================================================================"
echo ""
echo "注意: B02需要手动指定B02A/B02B/B02C子册分别构建"

if [ $FAIL_COUNT -gt 0 ]; then
    exit 1
else
    exit 0
fi
