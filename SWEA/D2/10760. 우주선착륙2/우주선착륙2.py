T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # N: row, M: col
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for row in range(N):
        for col in range(M):
            center = arr[row][col]
            cnt = 0
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]:
                new_r = row + dr
                new_c = col + dc
                if 0 <= new_r < N and 0 <= new_c < M and center > arr[new_r][new_c]:
                    cnt += 1
                    if cnt == 4:
                        result += 1
                        break

    print(f'#{tc}', result)