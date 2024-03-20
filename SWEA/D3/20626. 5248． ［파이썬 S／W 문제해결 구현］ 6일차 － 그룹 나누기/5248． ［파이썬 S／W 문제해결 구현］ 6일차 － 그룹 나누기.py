def find_set(idx):
    while idx != parents[idx]:
        idx = parents[idx]
    return idx


def link(idx1, idx2):
    if rank[idx1] < rank[idx2]:
        parents[idx1] = idx2
    else:
        parents[idx2] = idx1
        if rank[idx1] == rank[idx2]:
            rank[idx1] += 1


def union(data1, data2):
    idx1 = find_set(data1)
    idx2 = find_set(data2)
    link(idx1, idx2)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    parents = list(range(N+1))
    rank = [0] * (N+1)

    for i in range(0, len(arr), 2):
        union(arr[i], arr[i+1])

    result = set()
    for i in range(1, (N+1)):
        result.add(find_set(i))

    print(f'#{tc}', len(result))