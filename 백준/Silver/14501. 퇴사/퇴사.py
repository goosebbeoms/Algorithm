import sys
input = sys.stdin.readline

def DFS(start):
    global result

    # 재귀 호출 종료 조건: start가 N 이상일 때
    if start >= N:
        sum_v = 0
        for j in idx_st:
            sum_v += P[j]
        if result < sum_v:
            result = sum_v
        return

    # 상담을 하는 경우
    if start + T[start] <= N:  # 상담을 할 수 있는 조건 확인
        idx_st.append(start)
        DFS(start + T[start])
        idx_st.pop()

    # 상담을 하지 않는 경우
    DFS(start + 1)


N = int(input())    # 업무일
T = []              # 상담 소요일
P = []              # 상담 비용
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

idx_st = []
result = 0
DFS(0)

print(result)
