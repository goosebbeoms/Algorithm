import sys
input = sys.stdin.readline

# 1: 가로, 2: 세로, 3: 대각선
def dfs(r, c, flag):
    global N, result
    if (r, c) == (N-1, N-1):
        result += 1
        return

    if flag == 1:
        if 0 <= c+1 < N and arr[r][c+1] == 0:
            dfs(r, c+1, 1)
        if 0 <= r+1 < N and 0 <= c+1 < N:
            if arr[r][c+1] == 0 and arr[r+1][c] == 0 and arr[r+1][c+1] == 0:
                dfs(r+1, c+1, 3)

    elif flag == 2:
        if 0 <= r+1 < N and arr[r+1][c] == 0:
            dfs(r+1, c, 2)
        if 0 <= r + 1 < N and 0 <= c + 1 < N:
            if arr[r][c + 1] == 0 and arr[r + 1][c] == 0 and arr[r + 1][c + 1] == 0:
                dfs(r + 1, c + 1, 3)

    elif flag == 3:
        if 0 <= c+1 < N and arr[r][c+1] == 0:
            dfs(r, c+1, 1)
        if 0 <= r+1 < N and arr[r+1][c] == 0:
            dfs(r+1, c, 2)
        if 0 <= r + 1 < N and 0 <= c + 1 < N:
            if arr[r][c + 1] == 0 and arr[r + 1][c] == 0 and arr[r + 1][c + 1] == 0:
                dfs(r + 1, c + 1, 3)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
result = 0
dfs(0, 1, 1)

print(result)