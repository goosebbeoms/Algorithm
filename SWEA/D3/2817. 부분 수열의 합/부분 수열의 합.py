def comb(x, s, sub_sum):
    global cnt, K

    if sub_sum >= K:
        if sub_sum == K:
            cnt += 1
        return

    if x == N:
        return

    for i in range(s, N):
        if not used[i]:
            used[i] = 1
            comb(x+1, i, sub_sum + A[i])
            used[i] = 0



T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    cnt = 0
    sum_v = 0
    used = [0] * N

    comb(0, 0, 0)
    print(f'#{tc}', cnt)