def checker(num):
    if num < 2:  # 1 이하의 숫자는 소수가 아님
        return False
    for j in range(2, int(num ** 0.5) + 1):
        if num % j == 0:  # 🔹 i → num 으로 수정
            return False
    return True  # 모든 검사를 통과하면 소수임

M = int(input())
N = int(input())
lst = []

for i in range(M, N+1):
    if checker(i):
        lst.append(i)

if not lst:
    print(-1)
else:
    print(sum(lst))
    print(min(lst))  # 🔹 sorted(lst)[0] 대신 min(lst) 사용 (효율성 개선)