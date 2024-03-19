def perm(x, sub):
    global N, result

    if result >= sub:
        return

    if x == N:
        if result < sub:
            result = sub
        return

    for i in range(N):
        if not used[i]:
            lst.append(i)
            used[i] = True
            perm(x+1, sub * (works[x][i] / 100))
            lst.pop()
            used[i] = False


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    works = dict()
    for num in range(N):
        works[num] = list(map(int, input().split()))
    lst = []
    used = [False for _ in range(N)]
    result = 0
    perm(0, 1)

    print(f'#{tc} {result*100:.6f}')