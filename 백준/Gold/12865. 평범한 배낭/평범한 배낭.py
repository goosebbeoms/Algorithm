def recur(idx, w):
    global K

    if w > K:
        return -9999

    if idx == N:
        return 0

    if dp[idx][w] != -1:
        return dp[idx][w]

    dp[idx][w] = max(recur(idx+1, w+candidates[idx][0]) + candidates[idx][1], recur(idx+1, w))

    return dp[idx][w]


N, K = map(int, input().split())    # N: 물건 개수, K: 배낭에 최대 무게
candidates = [list(map(int, input().split())) for _ in range(N)]    # 물건 목록(무게 W, 가치 V)

dp = [[-1 for _ in range(100_001)] for _ in range(N)]

answer = recur(0, 0)
print(answer)