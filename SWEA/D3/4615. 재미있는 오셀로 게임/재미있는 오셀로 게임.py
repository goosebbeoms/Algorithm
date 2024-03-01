def set_board(N):
    arr = [['']*N for _ in range(N)]
    arr[N//2-1][N//2-1], arr[N//2][N//2] = 'W', 'W'
    arr[N//2-1][N//2], arr[N//2][N//2-1] = 'B', 'B'
    return arr


def find(row, col, color, color_r):
    dr = [-1, -1, 0, 1, 1, 1, 0, -1]
    dc = [0, 1, 1, 1, 0, -1, -1, -1]

    for idx in range(8):
        new_r = row + dr[idx]
        new_c = col + dc[idx]
        while (0<=new_r<N and 0<=new_c<N) and arr[new_r][new_c] == color_r:
            new_r = new_r + dr[idx]
            new_c = new_c + dc[idx]

        if 0<=new_r<N and 0<=new_c<N and arr[new_r][new_c] == color:
            while not (new_r == row and new_c == col):
                new_r -= dr[idx]
                new_c -= dc[idx]
                arr[new_r][new_c] = color



T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # N: 보드 한 변, M: 돌 놓는 횟수
    # 보드 세팅
    arr = set_board(N)

    for _ in range(M):
        col, row, color = map(int, input().split())
        col -= 1
        row -= 1
        if color == 1:
            color = 'B'
            color_r = 'W'
        elif color == 2:
            color = 'W'
            color_r = 'B'
        arr[row][col] = color

        find(row, col, color, color_r)

    result = [0, 0]
    for row in range(N):
        for col in range(N):
            if arr[row][col] == 'B':
                result[0] += 1
            elif arr[row][col] == 'W':
                result[1] += 1

    print(f'#{tc}', result[0], result[1])
