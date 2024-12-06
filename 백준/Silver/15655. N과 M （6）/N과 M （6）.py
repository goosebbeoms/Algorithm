def comb(x, n):
    if x == M:
        print(*nums)
        return

    for i in range(n, N):
        if used[i]:
            continue

        nums.append(arr[i])
        used[i] = True

        comb(x+1, i)

        nums.pop()
        used[i] = False


N, M = map(int, input().split())
arr = sorted(map(int, input().split()))
used = [False] * (N+1)
nums = []

comb(0, 0)