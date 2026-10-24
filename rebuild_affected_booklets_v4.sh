#!/bin/sh
# V4 新增 29 篇文章影响的 20 个分册批量重建脚本
# 2026-10-09

BASE="/storage/Users/currentUser/Documents/岐伯论/research-rebuild/reports/gemini-flash-reclassification-v1"
NODE="/data/service/hnp/bin/node"

echo "=== 开始重建受 v4 新增文章影响的 20 个分册 ==="
echo ""

# V1 卷一 (5 篇新增)
echo ">>> 卷一 B01..."
$NODE "$BASE/build_volume_v1.js" B01 || exit 1

echo ">>> 卷一 B03..."
$NODE "$BASE/build_volume_v1.js" B03 || exit 1

echo ">>> 卷一 B04..."
$NODE "$BASE/build_volume_v1.js" B04 || exit 1

# V2 卷二 (1 篇新增)
echo ">>> 卷二 B12..."
$NODE "$BASE/build_volume_v2.js" B12 || exit 1

# V3 卷三 (3 篇新增)
echo ">>> 卷三 B15..."
$NODE "$BASE/build_volumes_v4_v8.js" B15 || exit 1

# V4 卷四 (5 篇新增)
echo ">>> 卷四 B17..."
$NODE "$BASE/build_volumes_v4_v8.js" B17 || exit 1

echo ">>> 卷四 B18..."
$NODE "$BASE/build_volumes_v4_v8.js" B18 || exit 1

echo ">>> 卷四 B19..."
$NODE "$BASE/build_volumes_v4_v8.js" B19 || exit 1

# V5 卷五 (2 篇新增)
echo ">>> 卷五 B20A..."
$NODE "$BASE/build_volumes_v4_v8.js" B20A || exit 1

echo ">>> 卷五 B22..."
$NODE "$BASE/build_volumes_v4_v8.js" B22 || exit 1

# V6 卷六 (9 篇新增)
echo ">>> 卷六 B23..."
$NODE "$BASE/build_volumes_v4_v8.js" B23 || exit 1

echo ">>> 卷六 B24..."
$NODE "$BASE/build_volumes_v4_v8.js" B24 || exit 1

echo ">>> 卷六 B26..."
$NODE "$BASE/build_volumes_v4_v8.js" B26 || exit 1

echo ">>> 卷六 B27..."
$NODE "$BASE/build_volumes_v4_v8.js" B27 || exit 1

echo ">>> 卷六 B28..."
$NODE "$BASE/build_volumes_v4_v8.js" B28 || exit 1

echo ">>> 卷六 B29..."
$NODE "$BASE/build_volumes_v4_v8.js" B29 || exit 1

echo ">>> 卷六 B30..."
$NODE "$BASE/build_volumes_v4_v8.js" B30 || exit 1

# V7 卷七 (3 篇新增)
echo ">>> 卷七 B32..."
$NODE "$BASE/build_volumes_v4_v8.js" B32 || exit 1

echo ">>> 卷七 B34..."
$NODE "$BASE/build_volumes_v4_v8.js" B34 || exit 1

# V8 卷八 (1 篇新增)
echo ">>> 卷八 B39..."
$NODE "$BASE/build_volumes_v4_v8.js" B39 || exit 1

echo ""
echo "=== 全部 20 个分册重建完成 ==="
