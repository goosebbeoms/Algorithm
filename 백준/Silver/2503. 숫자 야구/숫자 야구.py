N = int(input())

hint = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
for i in range(1, 10):  # 100의 자리
    for j in range(1, 10):  # 10의 자리
        if i == j:
            continue
        for k in range(1, 10):  # 1의 자리
            if (i == k) or (j == k):
                continue

            num = str(100*i + 10*j + k)
            for case in hint:
                case_num = str(case[0])
                temp_strike = 0
                temp_ball = 0
                for x in range(3):
                    if case_num[x] in num:
                        if num[x] == case_num[x]:
                            temp_strike += 1
                            continue
                        temp_ball += 1

                if (case[1] != temp_strike) or (case[2] != temp_ball):
                    break
            else:
                cnt += 1

print(cnt)