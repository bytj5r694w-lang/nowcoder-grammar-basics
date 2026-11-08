# NC212226 回文数
# 给出 0~9 每个数码的个数，用全部数码拼出最小的回文数，不允许前导 0。
counts = list(map(int, input().split()))

odd_digits = [d for d in range(10) if counts[d] % 2 == 1]
if len(odd_digits) > 1:
    print(-1)                                      # 奇数个数的数码超过一个，无法构成回文
else:
    half = "".join(str(d) * (counts[d] // 2) for d in range(10))
    center = str(odd_digits[0]) if odd_digits else ""

    if half == "":
        print(center)                              # 只剩下一位，直接输出
    else:
        digits = sorted(half)
        first = 0
        while first < len(digits) and digits[first] == "0":
            first += 1
        if first == len(digits):
            print(-1)                              # 全是 0，必然出现前导 0
        else:
            # 最小的非零数字放最前面，其余数字升序排列
            half = digits[first] + "".join(digits[:first]) + "".join(digits[first + 1:])
            print(half + center + half[::-1])
