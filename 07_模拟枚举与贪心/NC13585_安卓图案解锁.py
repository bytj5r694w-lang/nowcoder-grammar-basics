# NC13585 安卓图案解锁
# 规则：每个数字最多用一次；若两点连线中间隔着另一个数字，
# 则该中间数字必须已经被使用过，否则连线非法。
import sys

# 需要中间点才能直接相连的数字对，value 为中间那个数字
MIDDLE = {
    (1, 3): 2, (3, 1): 2,
    (1, 7): 4, (7, 1): 4,
    (1, 9): 5, (9, 1): 5,
    (2, 8): 5, (8, 2): 5,
    (3, 7): 5, (7, 3): 5,
    (3, 9): 6, (9, 3): 6,
    (4, 6): 5, (6, 4): 5,
    (7, 9): 8, (9, 7): 8,
}

out = []
for pattern in sys.stdin.read().split():
    used = set()
    valid = True
    previous = None
    for ch in pattern:
        digit = int(ch)
        if digit in used:
            valid = False
            break
        if previous is not None and (previous, digit) in MIDDLE:
            if MIDDLE[(previous, digit)] not in used:
                valid = False
                break
        used.add(digit)
        previous = digit
    out.append("YES" if valid else "NO")

print("\n".join(out))
