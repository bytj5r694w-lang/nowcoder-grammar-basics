# NC15128 老子的全排列呢
# 输出 1~8 的全排列，按字典序，每行一组，行末无空格。
from itertools import permutations

out = []
for item in permutations("12345678"):
    out.append(" ".join(item))
print("\n".join(out))
