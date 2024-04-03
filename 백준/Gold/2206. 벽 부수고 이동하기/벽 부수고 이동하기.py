from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    q.append(start)
    visited[0][0][0] = 1

    while q:
        r, c, break_cnt = q.popleft()

        if (r, c) == (N-1, M-1):
            return visited[r][c][break_cnt]

        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < N and 0 <= nc < M:
                # 벽인 경우, 벽을 부순다.
                if arr[nr][nc] == 1 and break_cnt == 0:
                    visited[nr][nc][1] = visited[r][c][0] + 1
                    q.append((nr, nc, 1))
                # 이동 가능하며, 해당 break_cnt 층에서 아직 방문하지 않은 경우
                elif arr[nr][nc] == 0 and visited[nr][nc][break_cnt] == 0:
                    visited[nr][nc][break_cnt] = visited[r][c][break_cnt] + 1
                    q.append((nr, nc, break_cnt))

    return -1


# N: row, M: col
N, M = map(int, input().split())
arr = [list(map(int, list(input().strip()))) for _ in range(N)]

# (idx0: 벽을 안 부수고 가는 경로, idx1: 벽을 부수고 가는 경로)
visited = [[[0, 0] for i in range(M)] for j in range(N)]

start = (0, 0, 0)
q = deque()

print(bfs())