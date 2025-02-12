def dfs(n, cnt):
    global N, ans

    if n == N:
        ans = max(ans, cnt)
        return

    # 현재 개란이 깨진 경우 -> 다음 계란으로
    if arr[n][0] <= 0:
        dfs(n+1, cnt)
    else:
        flag = False
        for j in range(N):
            if n == j or arr[j][0] <= 0:
                continue

            # 계란 부딪히기
            arr[n][0], arr[j][0] = arr[n][0] - arr[j][1], arr[j][0] - arr[n][1]
            dfs(n+1, cnt+int(arr[n][0]<=0)+int(arr[j][0]<=0))
            arr[n][0], arr[j][0] = arr[n][0] + arr[j][1], arr[j][0] + arr[n][1]

            flag = True

        if not flag:
            dfs(n+1, cnt)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0
# 계란 index, 깨진 계란 개수
dfs(0, 0)
print(ans)