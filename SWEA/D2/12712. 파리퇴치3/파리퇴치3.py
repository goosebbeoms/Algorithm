T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # N: 배열, M: 스프레이 세기
    arr = [list(map(int, input().split())) for _ in range(N)]
    plus_lst = []
    x_lst = []
    for i in range(1, M):
        plus_lst.extend([(-i, 0), (i, 0), (0, -i), (0, i)])
        x_lst.extend([(-i, -i), (i, i), (-i, i), (i, -i)])

    tmp_lst = []
    for row in range(N):
        for col in range(N):
            sum_plus, sum_x = arr[row][col], arr[row][col]
            for dr, dc in plus_lst:
                new_r = row + dr
                new_c = col + dc
                if 0 <= new_r < N and 0 <= new_c < N:
                    sum_plus += arr[new_r][new_c]
            for dr, dc in x_lst:
                new_r = row + dr
                new_c = col + dc
                if 0 <= new_r < N and 0 <= new_c < N:
                    sum_x += arr[new_r][new_c]
            tmp_lst.append(max(sum_x, sum_plus))

    print(f'#{tc}', max(tmp_lst))
