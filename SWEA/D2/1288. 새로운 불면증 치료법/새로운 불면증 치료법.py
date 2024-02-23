T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 양 마릿수
    new_N = N
    tmp = []
    cnt = 1
    while len(tmp) < 10:
        new_N = N * cnt
        N_str = str(new_N)
        for num in N_str:
            if num not in tmp:
                tmp.append(num)
        cnt += 1

    print(f'#{tc}', (cnt-1) * N)