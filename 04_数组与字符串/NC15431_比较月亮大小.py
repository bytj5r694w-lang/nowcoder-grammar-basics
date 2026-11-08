# NC15431 比较月亮大小
# 月亮大小按 0..15..1 的周期变化，判断记录最后一天的"下一天"是变大还是变小。
n = int(input())
moon = list(map(int, input().split()))

last = moon[-1]
if last == 15:                 # 满月之后必然变小
    print("DOWN")
elif last == 0:                # 新月之后必然变大
    print("UP")
elif n == 1:                   # 只有一个数据且不是 0/15，无法判断
    print("-1")
elif moon[-1] > moon[-2]:
    print("UP")
else:
    print("DOWN")
