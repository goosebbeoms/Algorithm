def dfs():
    global N, M, r, c, d, cnt
    if arr[r][c] == 0:  # 현재 위치 청소
        arr[r][c] = 2  # 청소한 위치는 2로 표시
        cnt += 1
    for _ in range(4):  # 4방향 모두 탐색
        nd = (d - 1) % 4  # 왼쪽 방향으로 회전
        nr, nc = r + delta[nd][0], c + delta[nd][1]
        if arr[nr][nc] == 0:  # 왼쪽 방향에 청소하지 않은 공간이 있다면
            r, c, d = nr, nc, nd  # 전진하고 방향 전환
            dfs()  # 재귀 호출
            return
        d = nd  # 청소할 공간이 없다면 회전만 수행
    # 네 방향 모두 청소가 되어 있거나 벽인 경우
    nr, nc = r - delta[d][0], c - delta[d][1]  # 후진
    if arr[nr][nc] == 1:  # 뒤쪽이 벽이라 후진할 수 없는 경우
        return
    r, c = nr, nc
    dfs()  # 후진한 위치에서 다시 탐색 진행

N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
cnt = 0

dfs()

print(cnt)