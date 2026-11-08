# NC14721 装进肚子
# 选 K 个巧克力早上吃、其余晚上吃，使总甜蜜值最大。
# 先假设全部晚上吃，再挑 K 个"早上吃更划算"（Ai - Bi 最大）的改到早上。
import sys

data = sys.stdin.read().split()
n = int(data[0])
k = int(data[1])
morning = list(map(int, data[2:2 + n]))
evening = list(map(int, data[2 + n:2 + 2 * n]))

order = sorted(range(n), key=lambda i: morning[i] - evening[i], reverse=True)
total = sum(evening)
for i in order[:k]:
    total += morning[i] - evening[i]
print(total)
