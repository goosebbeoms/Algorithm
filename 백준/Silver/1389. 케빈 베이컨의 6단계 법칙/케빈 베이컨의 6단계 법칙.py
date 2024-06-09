from collections import defaultdict, deque


def bfs():
    while queue:
        pos, cnt = queue.popleft()

        for i in book[pos]:
            if not visited[i]:
                visited[i] = cnt + 1
                queue.append((i, cnt + 1))


# N: 유저의 수, M: 친구 관계의 수
N, M = map(int, input().split())
# 관계도
book = defaultdict(list)
# 케빈 베이컨의 수
result = [0] * (N + 1)
result[0] = float('inf')

for _ in range(M):
    p1, p2 = map(int, input().split())
    book[p1].append(p2)
    book[p2].append(p1)

for p in range(1, N+1):
    queue = deque([(p, 0)])
    visited = [0] * (N + 1)

    bfs()
    result[p] = sum(visited)

print(result.index(min(result)))
