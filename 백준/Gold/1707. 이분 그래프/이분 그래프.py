from collections import deque


def bfs():
    while q:
        node = q.popleft()
        for nxt in graph[node]:
            if not color[nxt]:  # 아직 방문 안 한 노드이면
                if color[node] == 1:    # node 빨간색 -> nxt 파란색
                    color[nxt] = 2
                elif color[node] == 2:  # node 파란색 -> nxt 빨간색
                    color[nxt] = 1
                q.append(nxt)
            else: # 이미 방문한 노드이면
                if color[node] == color[nxt]:   # 색깔이 같으면 이분 그래프 아님
                    return False

    return True

"""
    이분 그래프는 모든 인접한 정점끼리 서로 다른 색으로 칠해서, 모든 정점을 단 두 가지 색으로만 칠할 수 있는 그래프
    따라서 color 배열에 색을 반영하자.
    0: 아직 방문하지 않은 노드
    1: 빨간색
    2: 파란색
"""
K = int(input())    # 테스트 케이스
for _ in range(K):
    # 그래프 정점 개수: V, 간선 개수: E
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    color = [0] * (V+1)

    for _ in range(E):
        n1, n2 = map(int, input().split())
        graph[n1].append(n2)
        graph[n2].append(n1)

    answer = True
    for start in range(1, V+1):
        if not color[start]:
            q = deque([start])
            color[start] = 1
            if not bfs():
                answer = False
                break

    if answer:
        print("YES")
    else:
        print("NO")
