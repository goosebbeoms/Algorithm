T = int(input())  # 테스트 케이스 개수
final = []
for t in range(T):
    A, B = map(int, input().split())
    final.append(A + B)
for i in final:
    print(i)