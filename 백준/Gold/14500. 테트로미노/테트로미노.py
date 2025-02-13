def dfs(cnt, sum_v, lst):
    global N, M, ans

    if cnt == 4:
        ans = max(ans, sum_v)
        return

    for r, c in lst:
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                visited[nr][nc] = True
                dfs(cnt+1, sum_v+arr[nr][nc], lst+[(nr, nc)])
                visited[nr][nc] = False


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
ans = 0

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(1, arr[i][j], [(i, j)])

print(ans)