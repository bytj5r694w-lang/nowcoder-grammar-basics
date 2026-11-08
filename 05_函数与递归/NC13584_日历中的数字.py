# NC13584 日历中的数字
# 把某年某月的所有日期写成 yyyy-mm-dd 的形式，统计数字 x 出现的次数。
import sys


def days_in_month(year, month):
    """返回某年某月的天数（含闰年判断）。"""
    if month == 2:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            return 29
        return 28
    if month in (4, 6, 9, 11):
        return 30
    return 31


data = sys.stdin.read().split()
out = []
for i in range(0, len(data) - 2, 3):
    year = int(data[i])
    month = int(data[i + 1])
    target = data[i + 2]

    count = 0
    for day in range(1, days_in_month(year, month) + 1):
        text = "%04d%02d%02d" % (year, month, day)
        count += text.count(target)
    out.append(str(count))

print("\n".join(out))
