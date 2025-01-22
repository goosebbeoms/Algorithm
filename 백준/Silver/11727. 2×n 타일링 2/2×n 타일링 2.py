# 2 * N 크기의 직사각형 채우기
N = int(input())
dp = [0] * (N+2)
dp[0], dp[1] = 1, 1

for i in range(2, N+1):
    dp[i] = dp[i-1] + (dp[i-2] * 2)

print(dp[N] % 10007)
