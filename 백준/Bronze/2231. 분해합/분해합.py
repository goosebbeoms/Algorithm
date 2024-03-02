N = int(input())
for i in range(1, N+1):
    sub_sum = sum(map(int, str(i)))
    sum_v = i + sub_sum
    if sum_v == N:
        print(i)
        break
    if i == N:
        print(0)