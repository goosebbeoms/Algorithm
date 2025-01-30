N = int(input())
dp = [i for i in range(N+1)]

for i in range(1, int(N**0.5) + 1):
    for j in range(i**2, N+1):
        dp[j] = min(dp[j], dp[j-(i**2)]+1)

print(dp[N])
