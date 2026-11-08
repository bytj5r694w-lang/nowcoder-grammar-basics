# NC21874 好串
# "好串"只能由空串不断插入 "ab" 得到，等价于：把 a 看成左括号、b 看成右括号，
# 任意前缀中 a 的个数不少于 b 的个数，且最终两者数量相等。
text = input().strip()

balance = 0
valid = True
for ch in text:
    if ch == "a":
        balance += 1
    else:
        balance -= 1
    if balance < 0:
        valid = False
        break

if valid and balance == 0:
    print("Good")
else:
    print("Bad")
