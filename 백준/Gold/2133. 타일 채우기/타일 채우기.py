N = int(input())
dp = [0] * (N+1)
dp[0] = 1

if N > 1:
    dp[2] = 3

for i in range(4, N+1, 2):
    if i % 2 == 0:
        dp[i] = dp[i-2] * 3
        for j in range(4, i+1, 2):
            dp[i] += dp[i-j] * 2

print(dp[N])