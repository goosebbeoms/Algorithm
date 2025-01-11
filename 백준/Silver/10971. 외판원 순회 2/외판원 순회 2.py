def dfs(ST, W, depth=1):
    global answer, start, N

    if depth == N:
        for nxt, _w in graph[ST]:
            if nxt == start:
                answer = min(answer, W + _w)
                return

    for nxt, _w in graph[ST]:
        if visited[nxt]:
            continue

        visited[nxt] = True
        dfs(nxt, W + _w, depth+1)
        visited[nxt] = False


N = int(input())
graph = [[] for _ in range(N)]
answer = float('INF')

for i in range(N):
    lst = list(map(int, input().split()))
    for j in range(N):
        if i != j and lst[j]:
            graph[i].append([j, lst[j]])


for start in range(N):
    visited = [False] * N
    visited[start] = True
    dfs(start, 0)

print(answer)