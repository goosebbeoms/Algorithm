from collections import deque


def BFS():
    global N, M, cnt
    while q:
        r, c, hour = q.popleft()
        if hour > L:
            break

        cnt += 1

        for i in book[arr[r][c]]:
            nr = r + delta[i][0]
            nc = c + delta[i][1]
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] and (arr[nr][nc] in available[i]) and not visited[nr][nc]:
                q.append((nr, nc, hour+1))
                visited[nr][nc] = True


T = int(input())
for tc in range(1, T+1):
    # N: 지도의 세로 크기, M: 지도의 가로 크기, R: 맨홀 세로 위치, C: 맨홀 가로 위치, L: 탈출 후 소요된 시간
    N, M, R, C, L = map(int, input().split())
    cnt = 0
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False]*M for _ in range(N)]
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상, 하, 좌, 우
    book = {
        1: [0, 1, 2, 3],  # 상, 하, 좌, 우
        2: [0, 1],                   # 상, 하
        3: [2, 3],                   # 좌, 우
        4: [0, 3],                   # 상, 우
        5: [1, 3],                    # 하, 우
        6: [1, 2],                   # 하, 좌
        7: [0, 2],                  # 상, 좌
    }

    available = {
        0: [1, 2, 5, 6],
        1: [1, 2, 4, 7],
        2: [1, 3, 4, 5],
        3: [1, 3, 6, 7],
    }

    start = (R, C, 1)
    q = deque([start])
    visited[R][C] = True
    BFS()
    print(f'#{tc}', cnt)
