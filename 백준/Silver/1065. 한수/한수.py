def calc(N):
    global cnt
    num_lst = list(map(int, list(str(num))))
    diff = num_lst[0]-num_lst[1]
    for i in range(1, len(num_lst)-1):
        if num_lst[i]-num_lst[i+1] != diff:
            return
    else:
        cnt += 1


cnt = 0
N = int(input())
for num in range(1, N+1):
    if num < 10:
        cnt += 1
    else:
        calc(N)

print(cnt)