def N_Queen(i, queens):
    global cnt
    if i == N:
        cnt += 1
        return

    for x in range(N):
        if x not in queens and not diagonal_check(i, x, queens):
            queens.append(x)
            N_Queen(i+1, queens)
            queens.pop()


def diagonal_check(i, x, queens):
    for k in range(len(queens)):
        if abs(i - k) == abs(x - queens[k]):
            return True
    return False


T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 보드 크기, 퀸의 개수
    cnt = 0     # 가능한 경우의 수
    queens = []
    N_Queen(0, queens)

    print(f'#{tc}', cnt)