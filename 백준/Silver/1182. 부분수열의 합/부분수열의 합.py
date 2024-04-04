def sub_set(x, start):
    global S, cnt, num
    if x == num:
        if sum(tmp_lst) == S:
            cnt += 1

    for i in range(start, len(lst)):
        tmp_lst.append(lst[i])
        sub_set(x+1, i+1)
        tmp_lst.pop()


N, S = map(int, input().split())
lst = list(map(int, input().split()))
tmp_lst = []
cnt = 0

for num in range(1, len(lst)+1):
    sub_set(0, 0)
print(cnt)