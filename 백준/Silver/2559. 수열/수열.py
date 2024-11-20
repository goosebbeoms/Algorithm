N, K = map(int, input().split())    # N: 전체 날짜의 수, K: 합을 구하기 위한 날짜의 수
arr = list(map(int, input().split()))

prefix = [0 for _ in range(N+1)]

for i in range(N):
    prefix[i+1] = prefix[i] + arr[i]

answer = []
for j in range(K, N+1):
    answer.append(prefix[j] - prefix[j-K])

print(max(answer))