# 크루스칼

# 1. 모든 링크를 한 번에 가져온다.
# 2. 링크를 연결하면서 같은 집합으로 만들어준다.
# 3. 만약에 이미 같은 집합이라면 연결하지 않는다.

def _union(A, B):
    A = _find(A)
    B = _find(B)

    if A == B:
        return

    if rank[A] < rank[B]:
        parents[A] = B
    elif rank[A] > rank[B]:
        parents[B] = A
    else:
        parents[A] = B
        rank[B] += 1


def _find(X):
    while X != parents[X]:
        X = parents[X]

    return X


V, E = map(int, input().split())
links = [list(map(int, input().split())) for _ in range(E)]
links.sort(key=lambda x: x[2])  # 가중치 기준으로 정렬

parents = [i for i in range(V+1)]
rank = [0 for _ in range(V+1)]
answer = 0

for node1, node2, weight in links:
    node1 = _find(node1)
    node2 = _find(node2)

    if node1 == node2:
        continue
    else:
        _union(node1, node2)
        answer += weight

print(answer)