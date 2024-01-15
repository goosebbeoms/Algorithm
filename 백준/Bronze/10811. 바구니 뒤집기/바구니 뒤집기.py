N, M = map(int, input().split())  # N: 바구니 개수, M: 바구니 순서 변경 횟수
basket = [i+1 for i in range(N)]

for m in range(M):
    i, j = map(int, input().split())
    temp = basket[i-1:j]
    temp.reverse()
    basket[i-1:j] = temp

for i in basket:
    print(i, end=' ')