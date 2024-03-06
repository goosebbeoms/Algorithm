dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]


def dfs(r, c):
    if dp[r][c] != (r, c):
        return dp[r][c]
    dp[r][c] = r, c
    tmp_v = 30000000
    for i in range(8):
        tr, tc = r + dr[i], c + dc[i]
        if 0 <= tr < R and 0 <= tc < C and board[tr][tc] < board[r][c]:
            if tmp_v > board[tr][tc]:
                tmp_v = board[tr][tc]
                dp[r][c] = dfs(tr, tc)
    return dp[r][c]


R, C = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
dp = [[(i, j) for j in range(C)] for i in range(R)]
ball_cnt = [[0]*C for _ in range(R)]

for i in range(R):
    for j in range(C):
        nr, nc = dfs(i, j)
        ball_cnt[nr][nc] += 1

for row in ball_cnt:
    print(*row)
