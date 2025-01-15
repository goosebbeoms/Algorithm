from collections import deque


def bfs(N, K):
    # 최대 위치를 100,000으로 설정
    MAX = 100_001
    # 각 위치에 도달하는 최소 시간을 저장할 배열, 초기값은 무한대로 설정
    dist = [float('inf')] * MAX
    dist[N] = 0
    q = deque()
    q.append(N)

    while q:
        current = q.popleft()

        # 현재 위치가 K라면 최소 시간을 반환
        if current == K:
            return dist[current]

        # 순간이동 (cost 0)
        next_pos = current * 2
        if 0 <= next_pos < MAX and dist[next_pos] > dist[current]:
            dist[next_pos] = dist[current]
            q.appendleft(next_pos)  # 순간이동은 우선 처리

        # 앞으로 이동 (cost 1)
        next_pos = current + 1
        if 0 <= next_pos < MAX and dist[next_pos] > dist[current] + 1:
            dist[next_pos] = dist[current] + 1
            q.append(next_pos)

        # 뒤로 이동 (cost 1)
        next_pos = current - 1
        if 0 <= next_pos < MAX and dist[next_pos] > dist[current] + 1:
            dist[next_pos] = dist[current] + 1
            q.append(next_pos)

    return dist[K]


N, K = map(int, input().split())
print(bfs(N, K))
