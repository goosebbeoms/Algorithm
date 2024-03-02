N, M = map(int, input().split())
arr = [input() for _ in range(N)]
cnt_lst = []
# (0, 0)칸의 색이 'W'인 경우
for i in range(N-7):
    for j in range(M-7):
        cnt_w = 0
        for row in range(8):
            for col in range(8):
                if (row+col)%2 == 0 and arr[i+row][j+col] == 'B':
                    cnt_w += 1
                elif (row+col)%2 == 1 and arr[i+row][j+col] == 'W':
                    cnt_w += 1

        # (0, 0)칸의 색이 'B'인 경우
        cnt_b = 0
        for row in range(8):
            for col in range(8):
                if (row+col)%2 == 0 and arr[i+row][j+col] == 'W':
                    cnt_b += 1
                elif (row+col)%2 == 1 and arr[i+row][j+col] == 'B':
                    cnt_b += 1

        cnt_lst.append(min(cnt_w, cnt_b))

print(min(cnt_lst))