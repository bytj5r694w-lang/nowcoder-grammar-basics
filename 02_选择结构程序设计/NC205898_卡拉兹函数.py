# NC205898 卡拉兹函数
# n 为奇数时 f(n) = 3n + 1，n 为偶数时 f(n) = n / 2。
n = int(input())

if n % 2 == 1:
    print(3 * n + 1)
else:
    print(n // 2)
