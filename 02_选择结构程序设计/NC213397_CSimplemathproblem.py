# NC213397 CSimplemathproblem
# 若 X 是 Y 的因数（即 Y % X == 0），Z = X + Y；否则 Z = Y - X。
x, y = map(int, input().split())

if y % x == 0:
    print(x + y)
else:
    print(y - x)
