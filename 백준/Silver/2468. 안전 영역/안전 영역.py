from collections import deque


def bfs(N, h):
    checked = [[False]*N for _ in range(N)]
    q = deque()
    tmp = 0
    for r in range(N):
        for c in range(N):
            if not checked[r][c] and arr[r][c] > h:
                q.append((r, c))
                tmp += 1
                checked[r][c] = True
                while q:
                    rr, cc = q.popleft()
                    for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                        new_r = rr + dr
                        new_c = cc + dc
                        if 0 <= new_r < N and 0 <= new_c < N and arr[new_r][new_c] > h and not checked[new_r][new_c]:
                            q.append((new_r, new_c))
                            checked[new_r][new_c] = True
    return tmp


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# h: 비의 양 (1~높이 최댓값)
max_h = max(map(max, arr)) - 1      # 안전 영역이 존재하는 최대 비의 양
lst = []

for h in range(max_h+1):
    lst.append(bfs(N, h))

print(max(lst))
