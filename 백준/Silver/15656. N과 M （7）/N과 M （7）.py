def perm(x, idx):
    if x == M:
        print(*nums)
        return

    for i in range(N):
        nums.append(arr[i])
        perm(x+1, i)
        nums.pop()


N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
nums = []

perm(0, 0)