N = int(input())

for i in range(N):
    S = int(input())

    for i in range(2, 1_000_001):
        if S % i == 0:
            print("NO")
            break
    else:
        print("YES")