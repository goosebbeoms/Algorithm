import sys

N, K = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for _ in range(N)]

INF = float('inf')
dp = [INF] * (K + 1)
dp[0] = 0

for coin in coins:
    for j in range(coin, K + 1):
        if dp[j - coin] + 1 < dp[j]:
            dp[j] = dp[j - coin] + 1

if dp[K] == INF:
    print(-1)
else:
    print(dp[K])