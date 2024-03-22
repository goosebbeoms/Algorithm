from collections import deque


def bfs(row, col):
    global cnt
    q.append((row, col))
    while q:
        r, c = q.popleft()
        for dr, dc in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            new_r = r + dr
            new_c = c + dc
            if 0<=new_r<N and 0<=new_c<N and arr[new_r][new_c] - arr[r][c] == 1:
                q.append((new_r, new_c))
                cnt += 1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_v = -1
    result = []

    # 전체 출발지점에 대한 완전 탐색
    for row in range(N):
        for col in range(N):
            q = deque()
            cnt = 1
            bfs(row, col)
            if max_v == cnt:
                result.append(arr[row][col])
            elif max(max_v, cnt) == cnt:
                result.clear()
                result.append(arr[row][col])
                max_v = cnt

    print(f'#{tc}', min(result), max_v)