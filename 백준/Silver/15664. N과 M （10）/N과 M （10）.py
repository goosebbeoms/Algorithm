def dfs(cnt, idx, tlst):
    global N, M

    if cnt == M:
        print(*tlst)
        return

    prev = 0
    for i in range(idx, N):
        if not visited[i] and prev != nums[i]:
            visited[i] = True
            prev = nums[i]
            dfs(cnt+1, i, tlst+[nums[i]])
            visited[i] = False


N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
visited = [False] * N

dfs(0, 0,[])