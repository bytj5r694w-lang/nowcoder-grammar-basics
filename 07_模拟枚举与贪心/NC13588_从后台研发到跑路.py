# NC13588 从后台研发到跑路
# 删除代码中所有 /* */ 注释，但引号内的内容不处理，且引号可能被反斜杠转义。
import sys


def remove_comments(code):
    """逐字符扫描，跳过注释，保留字符串和其余所有字符（含换行、空格）。"""
    result = []
    i = 0
    in_string = False
    while i < len(code):
        ch = code[i]

        if in_string:
            result.append(ch)
            if ch == "\\" and i + 1 < len(code):     # 转义字符：原样保留两个字符
                result.append(code[i + 1])
                i += 2
                continue
            if ch == '"':
                in_string = False
            i += 1
            continue

        if ch == '"':
            in_string = True
            result.append(ch)
            i += 1
            continue

        if ch == "/" and i + 1 < len(code) and code[i + 1] == "*":
            end = code.find("*/", i + 2)
            if end == -1:                              # 不配对的 /* 按普通文本保留
                result.append("/*")
                i += 2
                continue
            i = end + 2
            continue

        result.append(ch)
        i += 1

    return "".join(result)


sys.stdout.write(remove_comments(sys.stdin.read()))
