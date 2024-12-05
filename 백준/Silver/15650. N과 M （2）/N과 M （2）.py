def comb(x, num):
    if x == M:
        print(*nums)

    for i in range(num+1, N+1):
        if used[i]:
            continue

        nums.append(i)
        used[i] = True

        comb(x+1, i)

        nums.pop()
        used[i] = False

N, M = map(int, input().split())
used = [False] * (N+1)
nums = []

comb(0, 0)