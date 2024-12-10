def recur(idx, price):
    global max_value

    if idx > N:
        return

    if idx == N:
        max_value = max(max_value, price)
        return

    recur(idx+interviews[idx][0], price+interviews[idx][1])
    recur(idx+1, price)


N = int(input())
interviews = [list(map(int, input().split())) for _ in range(N)]
max_value = -9999999999999999

recur(0, 0)
print(max_value)