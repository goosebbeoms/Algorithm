import sys
input = sys.stdin.readline
from collections import deque


def BFS(r, c):
    global R, C, result

    q = deque()
    visited = [[-1] * C for _ in range(R)]
    q.append((r, c))
    visited[r][c] = 0

    last_point = (r, c)

    while q:
        row, col = q.popleft()
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr = row + dr
            nc = col + dc
            if 0 <= nr < R and 0 <= nc < C and visited[nr][nc] == -1 and arr[nr][nc] == 'L':
                q.append((nr, nc))
                visited[nr][nc] = visited[row][col] + 1
                last_point = (nr, nc)
    else:
        if result < visited[last_point[0]][last_point[1]]:
            result = visited[last_point[0]][last_point[1]]


R, C = map(int, input().split())
arr = [input() for _ in range(R)]
result = -1

for r in range(R):
    for c in range(C):
        if arr[r][c] == 'L':
            BFS(r, c)

print(result)