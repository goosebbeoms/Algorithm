T = int(input())

for t in range(T):
    arr = list(map(int, input().split()))
    hap = 0
    for num in arr:
        if num % 2 == 1:
            hap += num
    print(f'#{t+1} {hap}')