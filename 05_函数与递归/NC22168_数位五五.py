# NC22168 数位五五
# 统计 [x, y] 中有多少个数，其各位数字之和是 5 的倍数。
x, y = map(int, input().split())
if x > y:
    x, y = y, x

# digit_sum[i] = i 的各位数字之和，用递推一次算出所有值
digit_sum = [0] * (y + 1)
answer = 0
for i in range(y + 1):
    digit_sum[i] = digit_sum[i // 10] + i % 10
    if i >= x and digit_sum[i] % 5 == 0:
        answer += 1
print(answer)
