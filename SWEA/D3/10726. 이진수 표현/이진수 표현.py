T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    boolean = []
    for i in range(N):
        if M & (1 << i):
            boolean.append(True)
        else:
            boolean.append(False)
    if False in boolean:
        print(f'#{tc} OFF')
    else:
        print(f'#{tc} ON')