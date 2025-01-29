N = int(input())
P = [0] + list(map(int, input().split()))
dp = [[0] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):         # 카드 종류
    for j in range(1, N+1):     # 카드 개수
        if j >= i:
            dp[i][j] = max(dp[i-1][j], dp[i][j-i] + P[i])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][N])
