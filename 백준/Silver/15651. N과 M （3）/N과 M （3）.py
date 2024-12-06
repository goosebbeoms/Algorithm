def perm(x):
    if x == M:
        print(*nums)
        return

    for i in range(1, N+1):
        nums.append(i)
        perm(x+1)
        nums.pop()


N, M = map(int, input().split())
nums = []

perm(0)