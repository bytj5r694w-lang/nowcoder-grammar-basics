# NC214223 整除判断
# 判断 m 能否被 n 整除。
m, n = map(int, input().split())

if m % n == 0:
    print("YES")
else:
    print("NO")
