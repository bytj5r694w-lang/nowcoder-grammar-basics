# NC16599 数字统计
# 统计区间 [L, R] 中数字 2 出现的次数。
def count_two(number):
    """返回整数 number 中数字 2 出现的次数。"""
    count = 0
    while number > 0:
        if number % 10 == 2:
            count += 1
        number //= 10
    return count


L, R = map(int, input().split())
total = 0
for i in range(L, R + 1):
    total += count_two(i)
print(total)
