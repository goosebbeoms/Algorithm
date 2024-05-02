def dfs(r, c):
    global M, N

    stack = [(r, c)]
    visited[r][c] = True

    while stack:
        row, col = stack.pop()
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr = row + dr
            nc = col + dc
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] and not visited[nr][nc]:
                stack.append((nr, nc))
                visited[nr][nc] = True


T = int(input())        # 테스트 케이스 개수
for tc in range(T):
    # M: 배추밭 가로 길이, N: 세로 길이, K: 배추 위치 개수
    M, N, K = map(int, input().split())
    cnt = 0
    arr = list([0] * M for _ in range(N))
    visited = list([False] * M for _ in range(N))
    for _ in range(K):
        X, Y = map(int, input().split())
        arr[Y][X] = 1

    for i in range(N):
        for j in range(M):
            if arr[i][j] and not visited[i][j]:
                cnt += 1
                dfs(i, j)

    print(cnt)