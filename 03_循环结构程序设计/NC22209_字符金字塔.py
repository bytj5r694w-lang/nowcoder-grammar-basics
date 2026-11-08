# NC22209 字符金字塔
# 输入一个大写字母，输出高度为(字母序号)的金字塔，
# 第 i 行形如 A B C ... 去程 + 回程。
letter = input().strip()
height = ord(letter) - ord("A") + 1

for i in range(height):
    left = ""
    for k in range(i + 1):
        left += chr(ord("A") + k)
    right = left[::-1][1:]                     # 回程去掉重复的峰顶字母
    print(" " * (height - 1 - i) + left + right)
