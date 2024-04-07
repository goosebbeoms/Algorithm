from collections import deque


def BFS():
    global R, C

    q = deque([(0, 0)])
    visited[0][0] = True
    melt = deque()

    while q:
        r, c = q.popleft()
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc]:
                visited[nr][nc] = True
                if cheese[nr][nc] == 1:
                    melt.append((nr, nc))
                else:
                    q.append((nr, nc))

    for r, c in melt:
        cheese[r][c] = 0
    return len(melt)


R, C = map(int, input().split())
cheese = []
remain = 0
time = 1
for _ in range(R):
    tmp = list(map(int, input().split()))
    remain += sum(tmp)
    cheese.append(tmp)

while True:
    visited = [[False]*C for _ in range(R)]
    melt_cnt = BFS()
    if remain - melt_cnt == 0:
        print(time)
        print(remain)
        break
    else:
        remain -= melt_cnt
        time += 1

