from collections import deque

def bfs(sr, sc):
    q = deque()
    used = [[False] * 5 for _ in range(5)]

    q.append((sr, sc))
    used[sr][sc] = True
    cnt = 1

    while q:
        r, c = q.popleft()

        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < 5 and 0 <= nc < 5 and not used[nr][nc] and visited[nr][nc]:
                q.append((nr, nc))
                used[nr][nc] = True
                cnt += 1

    return cnt == 7


def check():
    for i in range(5):
        for j in range(5):
            if visited[i][j]:
                return bfs(i, j)


def dfs(no, cnt, scnt):
    global ans

    if cnt > 7:
        return

    if no == 25:
        if cnt == 7 and scnt >= 4:
            if check():
                ans += 1
        return

    # 해당 학생 포함하는 경우
    visited[no//5][no%5] = True
    dfs(no+1, cnt+1, scnt+int(arr[no//5][no%5]=='S'))
    # 포함하지 않는 경우
    visited[no//5][no%5] = False
    dfs(no+1, cnt, scnt)


arr = [list(input()) for _ in range(5)]
ans = 0
visited = [[False] * 5 for _ in range(5)]

# 학생 번호(0~24), 포함 학생 수, 다솜파 학생 수
dfs(0, 0, 0)
print(ans)