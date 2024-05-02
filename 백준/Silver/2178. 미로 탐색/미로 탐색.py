from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, list(input()))) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

q = deque([(0, 0)])
visited[0][0] = 1

while q:
    r, c = q.popleft()

    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] and not visited[nr][nc]:
            q.append((nr, nc))
            visited[nr][nc] = visited[r][c] + 1

            if (nr, nc) == (N - 1, M - 1):
                print(visited[r][c] + 1)
                exit()