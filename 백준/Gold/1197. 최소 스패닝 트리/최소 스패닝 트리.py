import heapq

# 프림 알고리즘
V, E = map(int, input().split())  # V: 정점 개수, E: 간선 개수
graph = [[] for _ in range(V+1)]
visited = [0 for _ in range(V+1)]

for _ in range(E):
    A, B, C = map(int, input().split())
    graph[A].append([C, B])
    graph[B].append([C, A])

answer = 0
cnt = 0
# 다익스트라로 탐색
q = [[0, 1]]  # 1에서 출발
while q:
    if cnt == V:
        break

    weight, node = heapq.heappop(q)

    if not visited[node]:
        answer += weight
        cnt += 1
        visited[node] = 1
        for nxt in graph[node]:
            heapq.heappush(q, nxt)

print(answer)