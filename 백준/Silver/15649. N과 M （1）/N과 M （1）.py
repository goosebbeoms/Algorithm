def perm(x):
    if x == M:
        print(*temp_list)

    for i in range(1, N+1):
        if used[i]:
            continue

        temp_list.append(i)
        used[i] = True
        perm(x+1)
        temp_list.pop()
        used[i] = False

N, M = map(int, input().split())
used = [False] * (N+1)
temp_list = []

perm(0)