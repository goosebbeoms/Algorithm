from collections import deque

# N: 수빈 위치, K: 동생 위치
N, K = map(int, input().split())
visited = [0] * (10 ** 5 + 1)
q = deque([N])

while q:
    pos = q.popleft()
    if pos == K:
        print(visited[pos])
        break

    for nx in [pos-1, pos+1, pos*2]:
        if 0 <= nx <= 10**5 and not visited[nx]:
            visited[nx] = visited[pos] + 1
            q.append(nx)
