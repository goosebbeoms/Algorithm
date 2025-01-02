import heapq

V, E = map(int, input().split())
K = int(input())

links = [[] for _ in range(V+1)]
visited = [0 for _ in range(V+1)]
dist = [1e9 for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    links[u].append([v, w])

q = []
heapq.heappush(q, [0, K])
dist[K] = 0

while q:
    _w, node = heapq.heappop(q)
    for nxt, weight in links[node]:
        # 1. 각 노드의 값을 업데이트
        # 2. 만약에 여러 노드가 있다면 min 비교
        # 3. 시작점으로부터 거리를 봐서 짧은 순서대로 탐색
        if dist[nxt] > dist[node] + weight:
            dist[nxt] = min(dist[nxt], dist[node] + weight)
            heapq.heappush(q, [dist[nxt], nxt])

for i in dist[1:]:
    if i == 1e9:
        print("INF")
    else:
        print(i)