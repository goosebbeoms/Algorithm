# n: 동전의 종류, k: 가치의 합 목표
N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

# DP 테이블 초기화
dp = [0] * (K + 1)
dp[0] = 1  # 가치가 0인 경우의 방법의 수는 1

# 동전 종류를 하나씩 순회
for coin in coins:
    for value in range(coin, K + 1):
        dp[value] += dp[value - coin]

# 결과 출력
print(dp[K])