from collections import defaultdict

N = int(input())
graph = defaultdict(list)

for _ in range(N):
    root, l, r = input().split()
    graph[root].extend([l, r])

def rear(node):
    if node == '.':
        return

    print(node, end='')
    rear(graph[node][0])
    rear(graph[node][1])


def center(node):
    if node == '.':
        return

    center(graph[node][0])
    print(node, end='')
    center(graph[node][1])


def back(node):
    if node == '.':
        return

    back(graph[node][0])
    back(graph[node][1])
    print(node, end='')


rear('A')
print()
center('A')
print()
back('A')
print()