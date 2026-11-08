# NC205911 牛牛的数学作业（题单中原名"随机序列"）
# 每组数据求极差与方差，方差保留 3 位小数。
import sys

data = sys.stdin.read().split()
t = int(data[0])
pos = 1
out = []

for _ in range(t):
    n = int(data[pos])
    pos += 1
    arr = list(map(int, data[pos:pos + n]))
    pos += n

    total = sum(arr)
    total_square = sum(x * x for x in arr)
    # 方差 = (n * Σai² - (Σai)²) / n²，用整数运算避免浮点误差
    variance = (n * total_square - total * total) / (n * n)
    out.append("%d %.3f" % (max(arr) - min(arr), variance))

print("\n".join(out))
