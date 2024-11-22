H, W = map(int, input().split())
arr = list(map(int, input().split()))  # 각 열(W개의 열)의 블록 개수
hap = 0

for i in range(1, len(arr)-1):
    left_max = max(arr[:i])
    right_max = max(arr[i+1:])
    min_value = min(left_max, right_max)

    if min_value > arr[i]:
        hap += min_value - arr[i]

print(hap)
