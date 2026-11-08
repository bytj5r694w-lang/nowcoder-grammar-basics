# NC200369 四舍五入
# 最多做 t 次四舍五入，求能得到的最大分数。
# 贪心：每次都从"最靠左的、大于等于 5 的小数位"处四舍五入，收益最大。
import sys

data = sys.stdin.read().split()
length = int(data[0])
times = int(data[1])
text = data[2]

if "." in text:
    integer_part, fraction_part = text.split(".")
else:
    integer_part, fraction_part = text, ""

scale = len(fraction_part)
# 把整个数压缩成一个整数：value = 整数部分 * 10^scale + 小数部分
value = int(integer_part) * (10 ** scale) + int(fraction_part or "0")

while times > 0 and scale > 0:
    # 找到最靠左的 >= 5 的小数位
    position = -1
    for i in range(scale):
        digit = (value // (10 ** (scale - 1 - i))) % 10
        if digit >= 5:
            position = i
            break
    if position == -1:
        break

    # 四舍五入到 position 位小数（half-up，等价于加 5 后截断）
    unit = 10 ** (scale - position)
    value = (value + unit // 2) // unit
    scale = position
    times -= 1

if scale == 0:
    print(value)
else:
    frac_text = str(value % (10 ** scale)).rjust(scale, "0").rstrip("0")
    if frac_text:
        print("%d.%s" % (value // (10 ** scale), frac_text))
    else:
        print(value // (10 ** scale))
