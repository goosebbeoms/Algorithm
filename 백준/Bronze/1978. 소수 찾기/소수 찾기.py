N = int(input())
arr = list(map(int, input().split()))

cnt = 0
for i in arr:
    if i == 1:
        continue

    if i == 2:
        cnt += 1
        continue

    temp = 2
    while temp <= i:
        if i % temp == 0:
            break
        temp += 1

    if temp == i:
        cnt += 1

print(cnt)