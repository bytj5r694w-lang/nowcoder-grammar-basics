# NC22208 数字三角形
# 第 i 行输出 i 个数，数字从 1 开始连续递增，每个数占 4 个字符宽度（右对齐）。
n = int(input())

number = 1
for i in range(1, n + 1):
    row = []
    for _ in range(i):
        row.append("%4d" % number)
        number += 1
    print("".join(row))
