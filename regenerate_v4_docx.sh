#!/bin/sh
# 重新生成 v4 受影响的 20 个分册 DOCX（使用真实二维码）

cd /storage/Users/currentUser/Documents/岐伯论/research-rebuild/reports/gemini-flash-reclassification-v1

echo "=== 开始重新生成 20 个分册 DOCX ==="
echo ""

# 卷一（4个分册）
echo "=== 生成卷一 B01 ===" && node build_volume_v1.js B01
echo "=== 生成卷一 B03 ===" && node build_volume_v1.js B03
echo "=== 生成卷一 B04 ===" && node build_volume_v1.js B04
echo "=== 生成卷一 B06 ===" && node build_volume_v1.js B06

# 卷二（1个分册）
echo "=== 生成卷二 B12 ===" && node build_volume_v2.js B12

# 卷三（1个分册）
echo "=== 生成卷三 B15 ===" && node build_volumes_v4_v8.js B15

# 卷四（3个分册）
echo "=== 生成卷四 B17 ===" && node build_volumes_v4_v8.js B17
echo "=== 生成卷四 B18 ===" && node build_volumes_v4_v8.js B18
echo "=== 生成卷四 B19 ===" && node build_volumes_v4_v8.js B19

# 卷五（2个分册）
echo "=== 生成卷五 B20A ===" && node build_volumes_v4_v8.js B20A
echo "=== 生成卷五 B22 ===" && node build_volumes_v4_v8.js B22

# 卷六（7个分册）
echo "=== 生成卷六 B23 ===" && node build_volumes_v4_v8.js B23
echo "=== 生成卷六 B24 ===" && node build_volumes_v4_v8.js B24
echo "=== 生成卷六 B26 ===" && node build_volumes_v4_v8.js B26
echo "=== 生成卷六 B27 ===" && node build_volumes_v4_v8.js B27
echo "=== 生成卷六 B28 ===" && node build_volumes_v4_v8.js B28
echo "=== 生成卷六 B29 ===" && node build_volumes_v4_v8.js B29
echo "=== 生成卷六 B30 ===" && node build_volumes_v4_v8.js B30

# 卷七（2个分册）
echo "=== 生成卷七 B32 ===" && node build_volumes_v4_v8.js B32
echo "=== 生成卷七 B34 ===" && node build_volumes_v4_v8.js B34

# 卷八（1个分册）
echo "=== 生成卷八 B39 ===" && node build_volumes_v4_v8.js B39

echo ""
echo "=== 全部完成 ==="
