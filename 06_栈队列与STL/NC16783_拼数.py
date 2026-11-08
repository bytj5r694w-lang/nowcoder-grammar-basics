# NC16783 拼数
# 把 n 个正整数排成一排拼成最大的数。
# 排序规则：若 a + b > b + a，则 a 应排在 b 前面（字典序拼接比较）。
import sys

data = sys.stdin.read().split()
n = int(data[0])
numbers = data[1:1 + n]

for i in range(n):
    for j in range(n - 1 - i):
        if numbers[j] + numbers[j + 1] < numbers[j + 1] + numbers[j]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print("".join(numbers))
