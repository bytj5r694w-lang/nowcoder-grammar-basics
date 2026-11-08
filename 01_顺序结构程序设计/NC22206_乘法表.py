# NC22206 乘法表
# 第 i 行输出 i 个式子，每个乘积占 2 个字符宽度，式子之间用 1 个空格分隔。
for i in range(1, 10):
    row = []
    for j in range(1, i + 1):
        row.append("%d*%d=%2d" % (j, i, i * j))
    print(" ".join(row))
