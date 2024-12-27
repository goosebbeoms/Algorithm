import sys
sys.setrecursionlimit(9999)

def recur(x, y):
    global M, N

    if x == N-1 and y == M-1:
        return 1

    if dp[y][x] != -1:
        return dp[y][x]

    route = 0
    for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < N and 0 <= ny < M:
            if graph[y][x] > graph[ny][nx]:
                route += recur(nx, ny)

    dp[y][x] = route

    return dp[y][x]


M, N = map(int, input().split())    # M: 세로, N: 가로
graph = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1 for _ in range(N)] for _ in range(M)]

print(recur(0, 0))