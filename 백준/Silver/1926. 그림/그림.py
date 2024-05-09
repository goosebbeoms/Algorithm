def dfs(row, col):
    global n, m, max_v
    area = 1

    stack.append((row, col))
    visited[row][col] = 1
    while stack:
        r, c = stack.pop()
        for dr, dc in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] and not visited[nr][nc]:
                stack.append((nr, nc))
                visited[nr][nc] = 1
                area += 1
    else:
        max_v = max(max_v, area)
        return


# n: 도화지 세로 크기, m: 도화지 가로 크기
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

cnt = 0
max_v = float('-INF')

stack = []
for i in range(n):
    for j in range(m):
        if arr[i][j] and not visited[i][j]:
            cnt += 1
            dfs(i, j)

if not cnt:
    max_v = 0

print(cnt)
print(max_v)