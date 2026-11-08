# NC204117 牛牛的三角形
# 从 n 个数中任选三个，判断能否组成三角形，输出任意一组解。
n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

answer = None
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            # 排序后只需判断最小的两边之和是否大于最大边
            if numbers[i] + numbers[j] > numbers[k]:
                answer = (numbers[i], numbers[j], numbers[k])
                break
        if answer:
            break
    if answer:
        break

if answer:
    print(answer[0], answer[1], answer[2])
else:
    print("No solution")
