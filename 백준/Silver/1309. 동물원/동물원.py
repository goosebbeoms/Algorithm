N = int(input())
dp = [1, 1, 1]

for i in range(2, N+1):
    x_x = sum(dp)
    x_o = dp[0] + dp[2]
    o_x = dp[0] + dp[1]
    dp = [x_x, x_o, o_x]

print(sum(dp) % 9901)
