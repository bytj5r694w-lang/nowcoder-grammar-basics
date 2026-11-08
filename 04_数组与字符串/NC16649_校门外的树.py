# NC16649 校门外的树
# 用差分数组标记被施工覆盖的区间，最后统计仍未被覆盖的点。
L, M = map(int, input().split())

diff = [0] * (L + 2)
for _ in range(M):
    left, right = map(int, input().split())
    diff[left] += 1
    diff[right + 1] -= 1

remain = 0
cover = 0
for i in range(L + 1):
    cover += diff[i]
    if cover == 0:
        remain += 1
print(remain)
