from collections import defaultdict, deque

N = int(input())
tree = defaultdict(list)
parent_node = [0] * (N+1)
parent_node[0] = -1
parent_node[1] = -1

for _ in range(N-1):
    p, c = map(int, input().split())
    tree[p].append(c)
    tree[c].append(p)

q = deque([1])
while q:
    node = q.pop()
    for child in tree[node]:
        if not parent_node[child]:
            q.append(child)
            parent_node[child] = node

for i in parent_node[2:]:
    print(i)