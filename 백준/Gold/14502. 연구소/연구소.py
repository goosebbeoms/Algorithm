from collections import deque
import copy
import sys
input = sys.stdin.readline


def bfs():
    global N, M, max_space
    tmp_arr = copy.deepcopy(arr)
    # 바이러스 찾기
    q = deque()
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2:
                q.append((i, j))

    # 바이러스 전파
    while q:
        r, c = q.popleft()
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < N and 0 <= nc < M and not tmp_arr[nr][nc]:
                q.append((nr, nc))
                tmp_arr[nr][nc] = 2

    # 안전 영역 카운트
    cnt = 0
    for r in range(N):
        for c in range(M):
            if tmp_arr[r][c] == 0:
                cnt += 1

    # 최대 여부 확인
    if max_space < cnt:
        max_space = cnt


def wall(count):
    global N, M
    if count == 3:
        bfs()
        return

    for r in range(N):
        for c in range(M):
            if arr[r][c] == 0:
                arr[r][c] = 1
                wall(count+1)
                arr[r][c] = 0


# N: 세로, M: 가로
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
max_space = -111

wall(0)

print(max_space)