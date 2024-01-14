# max(), min() 함수 사용 안 한 풀이
N = int(input())
lst = list(map(int, input().split()))
max_num = -10000000
min_num = 10000000
for i in range(N):
    if max_num < lst[i]:
        max_num = lst[i]
    if min_num > lst[i]:
        min_num = lst[i]
print(min_num, max_num)