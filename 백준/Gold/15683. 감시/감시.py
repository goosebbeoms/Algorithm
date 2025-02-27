di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
cctv = [[], [1], [1, 3], [0, 1], [0, 1, 3], [0, 1, 2, 3]]

def calc(tlst):
    visited = [[0]*(M+2) for _ in range(N+2)]

    # 모든 CCTV에 대해서 처리(좌표, type, rotate)
    for i in range(CNT):
        si, sj = lst[i]
        rotate = tlst[i]
        type_num = arr[si][sj]

        # type에 따른 모든 방향을 뻗어가면서 visited에 1 표시
        for dr in cctv[type_num]:
            dr = (dr+rotate)%4
            ci, cj = si, sj
            while True:
                ci, cj = ci+di[dr], cj+dj[dr]
                if arr[ci][cj] == 6:
                    break
                visited[ci][cj] = 1

    # 사각지대 합산
    cnt = 0
    for i in range(1, N+1):
        for j in range(1, M+1):
            if not visited[i][j] and not arr[i][j]:
                cnt += 1

    return cnt


def dfs(n, tlst):
    global ans

    if n == CNT:    # 모든 CCTV의 방향 정하기 완료
        ans = min(ans, calc(tlst))
        return

    dfs(n+1, tlst+[0])  # 0도 회전
    dfs(n+1, tlst+[1])  # 90도 회전
    dfs(n+1, tlst+[2])  # 180도 회전
    dfs(n+1, tlst+[3])  # 270도 회전


N, M = map(int, input().split())
arr = [[6]*(M+2)] + [[6]+list(map(int, input().split()))+[6] for _ in range(N)] + [[6]*(M+2)]

# 1~5번 CCTV를 저장
lst = []
for i in range(1, N+1):
    for j in range(1, M+1):
        if 1 <= arr[i][j] <= 5:
            lst.append((i, j))

CNT = len(lst)
ans = N*M
dfs(0, [])
print(ans)