def _union(A, B):
    A = _find(A)
    B = _find(B)

    if A == B:
        return

    if rank[A] < rank[B]:
        parent[A] = B
    elif rank[A] > rank[B]:
        parent[B] = A
    else:
        parent[A] = B
        rank[B] += 1


def _find(A):
    if parent[A] == A:
        return A
    else:
        parent[A] = _find(parent[A])
        return _find(parent[A])


N, M = map(int, input().split())
parent = [i for i in range(N+1)]
rank = [0 for _ in range(N+1)]

for _ in range(M):
    X, A, B = map(int, input().split())

    if X == 0:
        _union(A, B)
    else:
        if _find(A) == _find(B):
            print("YES")
        else:
            print("NO")