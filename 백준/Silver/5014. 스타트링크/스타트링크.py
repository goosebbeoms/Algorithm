from collections import deque


def bfs():
    global F, G, U, D

    while q:
        now, cnt = q.popleft()   # 현재 위치

        # 스타트링크 층 도착
        if now == G:
            return cnt

        # 위로 올라가는 경우
        if 1 <= now + U <= F and not visited[now+U]:
            visited[now+U] = True
            q.append((now + U, cnt + 1))

        # 아래로 내려가는 경우
        if 1 <= now - D <= F and not visited[now-D]:
            visited[now-D] = True
            q.append((now - D, cnt + 1))

    return -1


# F: 건물 층, S: 강호 위치, G: 목적지, U: 상승, D: 하강
F, S, G, U, D = map(int, input().split())
q = deque([(S, 0)])
visited = [False] * (F+1)
visited[S] = True
answer = bfs()

if answer == -1:
    print("use the stairs")
else:
    print(answer)