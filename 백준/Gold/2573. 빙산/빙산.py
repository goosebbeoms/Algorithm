from collections import deque


def BFS(i, j):
    global N, M
    q = deque([(i, j)])
    visited[i][j] = True

    while q:
        r, c = q.popleft()
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                if arr[nr][nc] > 0:
                    q.append((nr, nc))
                    visited[nr][nc] = True
                elif arr[r][c] > 0:
                    arr[r][c] -= 1


N, M = map(int, input().split())    # N: 행, M: 열
arr = [list(map(int, input().split())) for _ in range(N)]
year = -1

while True:
    visited = [[False] * M for _ in range(N)]
    group = 0

    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] > 0:
                cnt += 1

    if cnt > 0:
        for i in range(N):
            for j in range(M):
                if arr[i][j] > 0 and not visited[i][j]:
                    BFS(i, j)
                    group += 1
        year += 1
        if group >= 2:
            print(year)
            break
    else:
        print(0)
        break
