# NC16538 记数问题
# 统计 1~n 中数字 x 出现的次数。用递推避免每个数都转字符串：
# cnt[i] = cnt[i // 10] + (i % 10 == x)，整体 O(n)。
n, x = map(int, input().split())

cnt = [0] * (n + 1)
total = 0
for i in range(1, n + 1):
    cnt[i] = cnt[i // 10] + (1 if i % 10 == x else 0)
    total += cnt[i]

print(total)
