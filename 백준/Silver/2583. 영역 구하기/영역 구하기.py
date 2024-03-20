from collections import deque


def bfs():
    area = 1
    while q:
        nr, nc = q.popleft()
        for tmp_r, tmp_c in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            if 0 <= nr+tmp_r < M and 0 <= nc+tmp_c < N and not arr[nr+tmp_r][nc+tmp_c] and not visited[nr+tmp_r][nc+tmp_c]:
                q.append((nr+tmp_r, nc+tmp_c))
                visited[nr+tmp_r][nc+tmp_c] = 1
                area += 1
    area_lst.append(area)


M, N, K = map(int, input().split())
arr = [[0]*N for _ in range(M)]
visited = [[0]*N for _ in range(M)]
cnt = 0
area_lst = []

for k in range(K):
    bx, by, tx, ty = map(int, input().split())
    for i in range(bx, tx):
        for j in range(by, ty):
            arr[j][i] += 1

q = deque()
for r in range(M):
    for c in range(N):
        if arr[r][c] == 0 and not visited[r][c]:
            q.append((r, c))
            visited[r][c] = 1
            cnt += 1
            bfs()

area_lst.sort()

print(cnt)
print(*area_lst)