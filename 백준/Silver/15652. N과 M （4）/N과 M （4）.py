def comb(x, pre):
    if x == M:
        print(*nums)
        return

    for i in range(pre, N+1):
        nums.append(i)
        comb(x+1, i)
        nums.pop()


N, M = map(int, input().split())
nums = []

comb(0,1)