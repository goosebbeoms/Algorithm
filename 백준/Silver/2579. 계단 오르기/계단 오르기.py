N = int(input())    # 계단의 개수
stairs = [0] + [int(input()) for _ in range(N)]
dp = [[0, 0, 0] for _ in range(N+1)]    # 해당 칸 안 밟는 경우, 이전 칸 안 밟은 경우, 두 번 연속 밟는 경우

for i in range(1, N+1):
    dp[i][0] = max(dp[i-1][1:])
    dp[i][1] = dp[i-1][0] + stairs[i]
    dp[i][2] = dp[i-1][1] + stairs[i]

print(max(dp[-1][1:]))