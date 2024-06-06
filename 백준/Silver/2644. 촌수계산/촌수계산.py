from collections import defaultdict, deque

n = int(input())        # 전체 사람의 수
visited = [False] * (n + 1)
p1, p2 = map(int, input().split())      # 촌수를 구해야 하는 사람 p1, p2
m = int(input())        # 관계의 개수
book = defaultdict(list)

for _ in range(m):
    p, c = map(int, input().split())
    book[p].append(c)
    book[c].append(p)
book = dict(book)

q = deque([(p1, 0)])
visited[p1] = True

while q:
    pos, cnt = q.popleft()

    for i in book[pos]:
        if not visited[i]:
            if i == p2:
                print(cnt + 1)
                exit()
            else:
                visited[i] = True
                q.append((i, cnt + 1))
else:
    print(-1)
