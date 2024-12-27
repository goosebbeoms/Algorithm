import sys

sys.setrecursionlimit(9999)

def recur(x, y):
    if dp[y][x] != -1:
        return dp[y][x]

    for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < n and 0 <= ny < n:
            if graph[y][x] < graph[ny][nx]:
                dp[y][x] = max(dp[y][x], recur(nx, ny) + 1)

    return dp[y][x]


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1 for _ in range(n)] for _ in range(n)]

for y in range(n):
    for x in range(n):
        recur(x, y)

print(max(map(max, dp)) + 2)