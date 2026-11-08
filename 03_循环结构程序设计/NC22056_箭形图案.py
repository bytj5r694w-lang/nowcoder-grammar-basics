# NC22056 箭形图案
# 多组输入，每组一个整数 n，输出 2n+1 行的箭头：
# 星号数 1,2,...,n+1,...,2,1，前面的空格数为 2*(n+1-星号数)。
import sys

for token in sys.stdin.read().split():
    n = int(token)
    for i in range(1, n + 2):                       # 上半部分（含最长一行）
        print(" " * (2 * (n + 1 - i)) + "*" * i)
    for i in range(n, 0, -1):                       # 下半部分
        print(" " * (2 * (n + 1 - i)) + "*" * i)
