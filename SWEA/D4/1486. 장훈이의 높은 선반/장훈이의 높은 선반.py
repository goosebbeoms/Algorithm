def partial(k, sub_sum):
    global N, result

    if sub_sum > result:
        return

    if k == N:
        for j in range(len(used)):
            if B <= sub_sum < result:
                result = sub_sum
        return

    for i in range(2):
        used[k] = i
        if used[k]:
            sub_sum += arr[k]
        partial(k+1, sub_sum)


T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    used = [-1 for _ in range(N)]
    result = sum(arr)
    partial(0, 0)
    print(f'#{tc}', result - B)