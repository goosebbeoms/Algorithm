def perm(x):
    if x == M:
        print(*nums)
        return

    for i in range(N):
        if used[i]:
            continue

        nums.append(arr[i])
        used[i] = True

        perm(x+1)

        nums.pop()
        used[i] = False


N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
used = [False] * (N+1)
nums = []

perm(0)
