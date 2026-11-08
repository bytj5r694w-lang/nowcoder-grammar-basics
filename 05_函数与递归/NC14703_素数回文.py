# NC14703 素数回文
# 把 t 拼成回文数，再判断该回文数是否仍是素数。
# 回文数最大可达 17 位，试除法会超时，因此用 Miller-Rabin 判素。
def is_prime(number):
    """确定性 Miller-Rabin 判素，适用于 64 位整数范围。"""
    if number < 2:
        return False
    small_primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for p in small_primes:
        if number % p == 0:
            return number == p

    odd_part = number - 1
    power = 0
    while odd_part % 2 == 0:
        odd_part //= 2
        power += 1

    for base in small_primes:
        value = pow(base, odd_part, number)
        if value == 1 or value == number - 1:
            continue
        for _ in range(power - 1):
            value = value * value % number
            if value == number - 1:
                break
        else:
            return False
    return True


t = int(input())
text = str(t)
palindrome = int(text + text[-2::-1])      # 例如 13 -> 131，127 -> 12721
print("prime" if is_prime(palindrome) else "noprime")
