arr = [[0] * 101 for _ in range(101)]
for _ in range(4):
    ld_x, ld_y, ru_x, ru_y = map(int, input().split())  # 좌측하단 x, y좌표와 우측상단 x, y좌표값 (1이상 100이하 정수)
    for i in range(ld_y, ru_y):
        for j in range(ld_x, ru_x):
            if arr[i][j] == 0:
                arr[i][j] += 1

cnt = 0
for i in range(101):
    for j in range(101):
        cnt += arr[i][j]

print(cnt)