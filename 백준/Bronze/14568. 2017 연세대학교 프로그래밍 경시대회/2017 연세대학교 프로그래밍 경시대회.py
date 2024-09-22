N = int(input())

# i: 택희, j: 영훈, k: 남규
cnt = 0
for i in range(1, N-1):
    if i % 2 == 1:
        continue

    for j in range(1, N-i-1):
        k = N - i - j
        if k - j < 2:
            continue

        cnt += 1

print(cnt)