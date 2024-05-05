from collections import deque


def bfs():
    global H, N, M, last_cnt

    while q:
        height, r, c, cnt = q.popleft()
        for dh, dr, dc in [(-1, 0, 0), (1, 0, 0), (0, 0, -1), (0, 0, 1), (0, -1, 0), (0, 1, 0)]:
            nh = height + dh
            nr = r + dr
            nc = c + dc
            if (0 <= nh < H) and (0 <= nr < N) and (0 <= nc < M) and arr[nh][nr][nc] == 0:
                q.append((nh, nr, nc, cnt+1))
                last_cnt = cnt+1
                arr[nh][nr][nc] = 1


# M: 상자의 가로, N: 상자의 세로, H: 상자의 높이
M, N, H = map(int, input().split())
arr = []
for h in range(H):
    h_tmp = []
    for n in range(N):
        h_tmp.append(list(map(int, input().split())))
    arr.append(h_tmp)

q = deque()
for h in range(H):
    for n in range(N):
        for m in range(M):
            if arr[h][n][m] == 1:
                q.append((h, n, m, 0))

last_cnt = 0
bfs()

for h in range(H):
    for n in range(N):
        for m in range(M):
            if not arr[h][n][m]:
                print(-1)
                exit()

print(last_cnt)