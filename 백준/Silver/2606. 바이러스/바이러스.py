from collections import defaultdict


def dfs(n):
    global cnt
    visited[n] = True

    for i in book[n]:
        if not visited[i]:
            cnt += 1
            if i in book.keys():
                dfs(i)


COM = int(input())      # 컴퓨터의 수
NET = int(input())      # 네트워크 간선 수
cnt = 0
visited = [False] * (COM + 1)

book = defaultdict(list)
for _ in range(NET):
    s, e = map(int, input().split())
    book[s].append(e)
    book[e].append(s)

dfs(1)
print(cnt)