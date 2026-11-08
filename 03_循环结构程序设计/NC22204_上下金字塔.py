# NC22204 上下金字塔
# 多组输入，每组输出一个菱形：上半部分逐行加宽，下半部分逐行收窄。
import sys

for token in sys.stdin.read().split():
    n = int(token)
    for i in range(1, n + 1):                 # 上半部分（含中线）
        print(" " * (n - i) + "*" * (2 * i - 1))
    for i in range(n - 1, 0, -1):             # 下半部分
        print(" " * (n - i) + "*" * (2 * i - 1))
