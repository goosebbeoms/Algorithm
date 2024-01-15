N, M = map(int, input().split())    # N: 바구니 개수/공 번호, M: 공 넣는 횟수
basket = [0 for i in range(N+1)]    # basket[0]은 편의상 삽입

for t in range(M):
    i, j, k = map(int, input().split())    # i: 첫 바구니, j: 끝 바구니, k: k번 번호 적힌 공
    for i in range(i, j+1):
        if basket[i] != 0:
            basket[i] = 0
        basket[i] += k
        
for i in basket[1:]:
    print(i, end=' ')