from collections import defaultdict, deque

# N: 정점의 개수, M: 간선의 개수
N, M = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

q = deque()
visited = [False] * (N+1)
cnt = 0

for s in range(1, N+1):
    if visited[s]:
        continue

    q.append(s)
    visited[s] = True
    cnt += 1
    while q:
        pos = q.popleft()
        for np in graph[pos]:
            if not visited[np]:
                q.append(np)
                visited[np] = True

print(cnt)