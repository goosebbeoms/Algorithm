def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return (gcd, x, y)

def crt(congruences):
    x, mod = 0, 1
    for a, m in congruences:
        gcd, p, q = extended_gcd(mod, m)
        if (a - x) % gcd != 0:
            return -1  # 해가 없음을 의미
        lcm = mod * m // gcd
        tmp = (a - x) // gcd * p % (m // gcd)
        x = (x + tmp * mod) % lcm
        mod = lcm
    return x if x != 0 else mod

E, S, M = map(int, input().split())

# 문제에서 주어진 주기는 각각 15, 28, 19입니다.
# 하지만 문제의 값은 1부터 시작하므로, 모듈러 연산을 위해 15, 28, 19로 나머지를 설정합니다.
congruences = [
    (E % 15, 15),
    (S % 28, 28),
    (M % 19, 19)
]

result = crt(congruences)
print(result if result != -1 else "No solution")
