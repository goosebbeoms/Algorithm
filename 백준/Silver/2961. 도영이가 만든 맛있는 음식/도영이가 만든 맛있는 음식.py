def recur(idx, dan, sseun):
    if idx == N:
        if sseun == 0:
            return

        result.append(abs(dan - sseun))
        return

    recur(idx+1, dan, sseun)
    recur(idx+1, dan*ingredients[idx][0], sseun+ingredients[idx][1])


N = int(input())    # 재료의 개수
ingredients = [list(map(int, input().split())) for _ in range(N)]   # 재료의 (신맛, 쓴맛)
result = []

recur(0, 1, 0)
print(min(result))