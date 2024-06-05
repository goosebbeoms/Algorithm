def promising(i, row):
    for idx in range(N):
        if idx == i:
            continue
        if (i - row) == (idx - used[idx]) or (i + row) == (idx + used[idx]):
            return False
    return True


def perm(row):
    global N, cnt

    if row == N:
        cnt += 1
        return

    for i in range(N):
        if used[i] == -99 and promising(i, row):
            used[i] = row
            perm(row+1)
            used[i] = -99


N = int(input())
cnt = 0
used = [-99] * N

perm(0)
print(cnt)