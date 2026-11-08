# NC212955 比大小
# 读入两个整数，按大小关系输出 < = >
a, b = map(int, input().split())

if a < b:
    print("<")
elif a == b:
    print("=")
else:
    print(">")
