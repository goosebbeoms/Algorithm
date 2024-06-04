N, M = map(int, input().split())

A = list(map(int, input().split()))
cnt = 0
left = 0
right = 1
hap = A[0]

while True:
    if hap == M:
        cnt += 1
        hap -= A[left]
        left += 1
    elif hap < M:
        if right < N:
            hap += A[right]
            right += 1
        else:
            break
    else:
        hap -= A[left]
        left += 1

print(cnt)