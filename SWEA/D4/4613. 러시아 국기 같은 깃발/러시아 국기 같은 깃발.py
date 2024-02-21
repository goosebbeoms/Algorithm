T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # N: 행, M: 열
    arr = [list(input()) for _ in range(N)]

    count = [[0, 0, 0] for _ in range(N)]   # 흰색, 파란색, 빨간색
    for row in range(N):
        count[row][0] = arr[row].count('W')
        count[row][1] = arr[row].count('B')
        count[row][2] = arr[row].count('R')

    cnt_lst = []
    for l1 in range(1, N-1):
        for l2 in range(l1+1, N):
            # print(l1, l2)
            cnt = 0
            # 0~l1까지 흰색
            for row in range(0, l1):
                cnt += count[row][1]
                cnt += count[row][2]
            # l1~l2까지 파란색
            for row in range(l1, l2):
                cnt += count[row][0]
                cnt += count[row][2]
            # l2~N-1까지 빨간색
            for row in range(l2, N):
                cnt += count[row][0]
                cnt += count[row][1]
            cnt_lst.append(cnt)
    print(f'#{tc}', min(cnt_lst))