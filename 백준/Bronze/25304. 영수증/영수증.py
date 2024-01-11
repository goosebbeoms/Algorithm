X = int(input())  # 영수증 표기 총 금액
N = int(input())  # 영수증 표기 물건 종류 수
count = 0  # 검산 누적 금액
for n in range(N):
    a, b = map(int, input().split())
    count += a * b
if count == X:
    print('Yes')
else:
    print('No')