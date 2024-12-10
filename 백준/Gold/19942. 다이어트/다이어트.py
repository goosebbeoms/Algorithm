def recur(idx, p, f, s, v, c):
    if idx == N:
        if (mp > p) or (mf > f) or (ms > s) or (mv > v):
            return

        result.append([p, f, s, v, c, used[:]])
        return

    recur(idx+1, p, f, s, v, c)

    used.append(idx+1)
    recur(idx+1, p+ingredients[idx][0], f+ingredients[idx][1], s+ingredients[idx][2], v+ingredients[idx][3], c+ingredients[idx][4])
    used.pop()


N = int(input())
mp, mf, ms, mv = map(int, input().split())  # 영양소의 최소 조건
# 단백질(p), 지방(f), 탄수화물(s), 비타민(v), 가격(c)
ingredients = [list(map(int, input().split())) for _ in range(N)]
used = []
result = []

recur(0, 0, 0, 0, 0, 0)

if not len(result):
    print(-1)
else:
    result.sort(key=lambda x: (x[4], x[5]))
    print(result[0][4])
    print(*result[0][5])
