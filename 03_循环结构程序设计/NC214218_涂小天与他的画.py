# NC214218 涂小天与他的画
# 多组测试数据，每组给出一个奇数 n，输出高度为 n 的菱形，行末不能有空格。
import sys

data = sys.stdin.read().split()
t = int(data[0])

for idx in range(1, t + 1):
    n = int(data[idx])
    half = n // 2
    for row in range(n):
        # 距离菱形中心的行数：上半部分为 row，下半部分为 n-1-row
        if row <= half:
            level = row
        else:
            level = n - 1 - row
        spaces = half - level
        print(" " * spaces + "*" * (2 * level + 1))
