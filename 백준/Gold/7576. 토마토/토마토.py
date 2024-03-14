import collections


def bfs():
    cnt = -1
    while q:
        rr, cc = q.popleft()
        for d in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            new_r = rr + d[0]
            new_c = cc + d[1]
            if 0 <= new_r < N and 0 <= new_c < M and not arr[new_r][new_c]:
                arr[new_r][new_c] = arr[rr][cc] + 1
                q.append((new_r, new_c))

    for i in range(N):
        for j in range(M):
            if not arr[i][j]:
                return -1
            cnt = max(cnt, arr[i][j])
    return cnt - 1  # 시작 단계에서의 1을 고려한 계산


M, N = map(int, input().split())    # M: 가로, N: 세로
arr = [list(map(int, input().split())) for _ in range(N)]
used = [[False]*M for _ in range(N)]

q = collections.deque()

# 익은 토마토 찾기 & 없는 토마토 칸 거르기
for r in range(N):
    for c in range(M):
        if arr[r][c] == 1:
            q.append((r, c))

print(bfs())