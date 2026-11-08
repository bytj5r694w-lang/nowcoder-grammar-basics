# NC13814 Captcha Cracker
# 从验证码中按出现顺序提取 0、2、4、6、9 以及它们对应的英文单词。
import sys

WORDS = {
    "zero": "0",
    "two": "2",
    "four": "4",
    "six": "6",
    "nine": "9",
}
DIGITS = set("02469")

data = sys.stdin.read().split()
case_count = int(data[0])
out = []

for case in range(1, case_count + 1):
    captcha = data[case]
    result = []
    i = 0
    while i < len(captcha):
        matched_word = None
        for word, digit in WORDS.items():
            if captcha.startswith(word, i):
                matched_word = (word, digit)
                break
        if matched_word:
            result.append(matched_word[1])
            i += len(matched_word[0])
        elif captcha[i] in DIGITS:
            result.append(captcha[i])
            i += 1
        else:
            i += 1
    out.append("".join(result))

print("\n".join(out))
