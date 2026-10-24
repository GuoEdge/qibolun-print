#!/bin/sh
# 构建卷三所有分册（B14/B15/B16）

echo "开始构建卷三..."
echo "================================"

for code in B14 B15 B16; do
  echo "[$code] 构建中..."
  node build_volumes_v4_v8.js "$code"
done

echo "================================"
echo "卷三构建完成！"
