#!/bin/sh
# 重建卷二-八所有已存在的分册（修复二维码URL）

echo "开始重建卷二-八所有分册..."
echo "================================"

# 卷二（3册）
for code in B04 B05 B06; do
  echo "[$code] 构建中..."
  node build_volumes_v4_v8.js "$code"
done

# 卷三（暂无，需单独处理）

# 卷四（3册）
for code in B17 B18 B19; do
  echo "[$code] 构建中..."
  node build_volumes_v4_v8.js "$code"
done

# 卷五（5册：B20A/B/C + B21 + B22）
for code in B20A B20B B20C B21 B22; do
  echo "[$code] 构建中..."
  node build_volumes_v4_v8.js "$code"
done

# 卷六（8册）
for code in B23 B24 B25 B26 B27 B28 B29 B30; do
  echo "[$code] 构建中..."
  node build_volumes_v4_v8.js "$code"
done

# 卷七（20册：B31A/B + B32-B37 + B38A-L）
for code in B31A B31B B32 B33 B34 B35 B36 B37 B38A B38B B38C B38D B38E B38F B38G B38H B38I B38J B38K B38L; do
  echo "[$code] 构建中..."
  node build_volumes_v4_v8.js "$code"
done

# 卷八（2册）
for code in B39 B40; do
  echo "[$code] 构建中..."
  node build_volumes_v4_v8.js "$code"
done

echo "================================"
echo "全部重建完成！"
