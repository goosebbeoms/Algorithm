N, M = map(int, input().split())  # N: 바구니 개수, 공 번호 / M: 공 교체 횟수
basket = [i for i in range(1, N+1)]

for m in range(M):
    i, j = map(int, input().split())
    temp = basket[i-1]
    basket[i-1] = basket[j-1]
    basket[j-1] = temp

for i in basket:
    print(i, end=' ')