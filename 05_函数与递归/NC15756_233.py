# NC15756 233
# 每组给出两个只由 2 和 3 组成的串，输出它们的乘积。
# 串长可达 50 位，Python 的大整数可以直接相乘。
import sys

data = sys.stdin.read().split()
t = int(data[0])
out = []
for i in range(t):
    first = int(data[1 + 2 * i])
    second = int(data[2 + 2 * i])
    out.append(str(first * second))
print("\n".join(out))
