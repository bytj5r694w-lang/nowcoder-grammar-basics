# NC18929 排列式
# 枚举较小的乘数 a 与较大的乘数 b，令 c = a * b，
# 若 a、b、c 拼起来恰好是 1~9 各出现一次，则是一个合法式子。
results = []

a = 1
while a <= 98:
    b = a + 1
    while b <= 9999:
        c = a * b
        if c > 9999:
            break                      # b 再增大 c 只会更大，直接换下一个 a
        if c >= 1000:
            digits = str(a) + str(b) + str(c)
            if len(digits) == 9 and sorted(digits) == list("123456789"):
                results.append((c, a, b))
        b += 1
    a += 1

# 结果小的先输出；结果相同时，较小的乘数小的先输出
results.sort()
for c, a, b in results:
    print("%d = %d x %d" % (c, a, b))
