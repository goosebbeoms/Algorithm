def check(lev, start, N, M, sum_v):
    if sum_v > M:
        return
    
    if lev == 3:
        if sum_v <= M:
            lst.append(sum_v)
            return

    for i in range(start, N):
        sum_v += arr[i]
        check(lev+1, i+1, N, M, sum_v)
        sum_v -= arr[i]


N, M = map(int, input().split())    # N: 카드의 개수, M: 카드 조건
arr = list(map(int, input().split()))
lst = []
check(0, 0, N, M, 0)
print(max(lst))