import sys
sys.setrecursionlimit(99999)

def dfs(node, accumulated_weight):
    global max_dist, farthest_node

    if max_dist < accumulated_weight:
        max_dist = accumulated_weight
        farthest_node = node

    for nxt, w in graph[node]:
        if not visited[nxt]:
            visited[nxt] = True
            dfs(nxt, accumulated_weight + w)


N = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    p_node, c_node, weight = map(int, input().split())
    graph[p_node].append((c_node, weight))
    graph[c_node].append((p_node, weight))

max_dist = 0
farthest_node = 1
visited = [False] * (N+1)
visited[1] = True
dfs(1, 0)

max_dist = 0
visited = [False] * (N+1)
visited[farthest_node] = True
dfs(farthest_node, 0)

print(max_dist)