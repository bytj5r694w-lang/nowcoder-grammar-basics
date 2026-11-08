# NC215089 默契
# 两数相等输出 "Tacit！"，否则输出 "No Tacit!"。
# 注意：题目样例中相等时的感叹号是全角"！"，与不相等的半角"!"不同，
# 这是本题的坑点，输出必须与样例逐字符一致。
x, y = map(int, input().split())

if x == y:
    print("Tacit！")
else:
    print("No Tacit!")
