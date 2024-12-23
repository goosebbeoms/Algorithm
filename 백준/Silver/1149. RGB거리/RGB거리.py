N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(3)] for _ in range(2)]

for k in range(3):
    dp[0][k] = arr[0][k]

for i in range(1, N):
    for j in range(3):
        if j == 0:
            dp[1][j] = min(dp[0][1] + arr[i][j], dp[0][2] + arr[i][j])
        if j == 1:
            dp[1][j] = min(dp[0][0] + arr[i][j], dp[0][2] + arr[i][j])
        if j == 2:
            dp[1][j] = min(dp[0][1] + arr[i][j], dp[0][0] + arr[i][j])
    for f in range(3):
        dp[0][f] = dp[1][f]

print(min(dp[-1]))
