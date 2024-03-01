T = int(input())
for tc in range(1, T+1):
    arr = [input() for _ in range(5)]
    word = ''
    max_length = max(map(len, arr))

    for j in range(max_length):
        for i in range(5):
            try:
                word += arr[i][j]
            except IndexError:
                pass

    print(f'#{tc}', word)
