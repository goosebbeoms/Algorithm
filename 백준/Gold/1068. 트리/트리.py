from collections import defaultdict


N = int(input())                        #트리 노드의 개수
arr = list(map(int, input().split()))
removed_node = int(input())             #삭제할 노드
nodes = defaultdict(list)

for i in range(N):
    nodes[arr[i]].append(i)

for key in nodes.keys():
    if removed_node in nodes[key]:
        nodes[key].remove(removed_node)
        break

cnt = 0
stack = [-1]

while stack:
    pos = stack.pop()

    if len(nodes[pos]) == 0:
        if pos == -1:
            break
        cnt += 1
    else:
        for i in nodes[pos]:
            stack.append(i)

print(cnt)