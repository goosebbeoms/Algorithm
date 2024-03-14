import collections


def bfs(r, c):
    q = collections.deque([(r, c)])
    arr[r][c] = 0
    temp = 0
    while q:
        row, col = q.popleft()
        temp += 1
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            new_r = row + dr
            new_c = col + dc
            if 0 <= new_r < N and 0 <= new_c < N and arr[new_r][new_c]:
                q.append((new_r, new_c))
                arr[new_r][new_c] = 0
    return temp


N = int(input())    # 정사각형
arr = [list(map(int, input())) for _ in range(N)]   # 지도 입력
cnt = 0     # 총 단지 수
homes = []  # 각 단지에 속하는 집의 수

for i in range(N):
    for j in range(N):
        if arr[i][j]:
            cnt += 1
            homes.append(bfs(i, j))
else:
    homes.sort()

# 결과 출력
print(cnt)
if cnt:
    for num in homes:
        print(num)