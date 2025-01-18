N = int(input())    # 전깃줄 개수
lines = []

# 전깃줄 입력 받기
for _ in range(N):
    A, B = map(int, input().split())
    lines.append((A, B))

lines.sort(key=lambda x: x[0])
b_line = list(map(lambda x: x[1], lines))

dp = [1] * N

# 최장 증가 수열 구하기
for i in range(1, N):
    for j in range(i):
        if b_line[i] > b_line[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(N-max(dp))