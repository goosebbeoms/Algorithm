def length_calc():
    result = 0
    for h_r, h_c in homes:
        temp = []
        for s_r, s_c in picked:
            temp.append(abs(h_r - s_r) + abs(h_c - s_c))
        result += min(temp)
    return result



def comb(x, start):
    global M
    if x == M:
        final.append(length_calc())

    for i in range(start, len(stores)):
        picked.append(stores[i])
        comb(x+1, i+1)
        picked.pop()


# N: 도시 크기, M: 치킨집 최대 개수
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

homes = []
stores = []
picked = []
final = []
for r in range(N):
    for c in range(N):
        if arr[r][c] == 1:      # 집
            homes.append((r, c))
        elif arr[r][c] == 2:    # 치킨집
            stores.append((r, c))
# used = [False]*len(stores)
comb(0, 0)

print(min(final))