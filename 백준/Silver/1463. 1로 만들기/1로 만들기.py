N = int(input())
dp = [float('inf')] * (N+1)
dp[N] = 0

for i in range(N-1, 0, -1):
    if i*3 <= N and dp[i*3] != float('inf'):
        dp[i] = min(dp[i], dp[i*3] + 1)
    if i*2 <= N and dp[i*2] != float('inf'):
        dp[i] = min(dp[i], dp[i*2] + 1)
    dp[i] = min(dp[i], dp[i+1] + 1)

print(dp[1])