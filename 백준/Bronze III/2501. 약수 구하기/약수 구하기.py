N, K = map(int, input().split())    # N: 계산 대상, K: 작은 수의 위치
temp_lst = []
for i in range(1, N+1):
    if N % i == 0:
        temp_lst.append(i)
try:
    print(temp_lst[K-1])
except IndexError:
    print(0)