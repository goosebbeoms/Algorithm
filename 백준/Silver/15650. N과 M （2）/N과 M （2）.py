def comb(x, start):
    if x == M:
        print(*nums)

    for i in range(start, N+1):
        if used[i]:
            continue

        nums.append(i)
        used[i] = True
        comb(x+1, i+1)
        nums.pop()
        used[i] = False


N, M = map(int, input().split())
used = [False] * (N+1)
nums = []

comb(0, 1)