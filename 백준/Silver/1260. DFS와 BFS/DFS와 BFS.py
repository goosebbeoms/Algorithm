from collections import defaultdict, deque


def dfs(node):
    ans_dfs.append(node)
    visited_dfs[node] = True

    for n in graph[node]:
        if not visited_dfs[n]:
            dfs(n)


def bfs(node):
    q = deque()
    q.append(node)
    ans_bfs.append(node)
    visited_bfs[node] = True

    while q:
        now = q.popleft()

        for n in graph[now]:
            if not visited_bfs[n]:
                q.append(n)
                ans_bfs.append(n)
                visited_bfs[n] = True


# N: 정점의 개수, M: 간선의 개수, V: 탐색을 시작할 정점의 번호
N, M, V = map(int, input().split())
graph = defaultdict(list)

for _ in range(M):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

for key in graph.keys():
    graph[key].sort()

visited_dfs = [False] * (N+1)
ans_dfs = []
dfs(V)

visited_bfs = [False] * (N+1)
ans_bfs = []
bfs(V)

print(*ans_dfs)
print(*ans_bfs)