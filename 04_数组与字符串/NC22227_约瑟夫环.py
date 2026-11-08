# NC22227 约瑟夫环
# 编号 0~n-1 围成一圈，从 k 开始报数，报到 m 的人出队，求最后剩下的人。
n, k, m = map(int, input().split())

queue = list(range(n))
index = k                                  # 当前开始报数的人的下标
while len(queue) > 1:
    index = (index + m - 1) % len(queue)   # 报数 m 的人出队
    queue.pop(index)
print(queue[0])
