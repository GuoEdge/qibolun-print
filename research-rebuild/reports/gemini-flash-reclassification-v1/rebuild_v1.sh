#!/bin/sh
# 重建卷一所有分册（修复二维码URL）

echo "开始重建卷一所有分册..."
echo "================================"

# B01 甲册（使用独立脚本）
echo "[B01] 甲册构建中..."
node build_booklet_B01_v3.js

# B02 乙册（上中下3册）
for code in B02A B02B B02C; do
  echo "[$code] 构建中..."
  node build_volume_v1.js "$code"
done

# B03-B10（8册）
for code in B03 B04 B05 B06 B07 B08 B09 B10; do
  echo "[$code] 构建中..."
  node build_volume_v1.js "$code"
done

echo "================================"
echo "卷一全部重建完成！"
