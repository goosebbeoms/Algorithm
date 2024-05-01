T = int(input())
for tc in range(T):
    N = int(input())
    cnt_zero = 1
    cnt_one = 0

    for i in range(N):
        cnt_zero, cnt_one = cnt_one, cnt_zero+cnt_one

    print(cnt_zero, cnt_one)
