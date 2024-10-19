N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
grade = [1] * N

for me in range(N):
    for other in range(N):
        if me == other: continue
        elif (arr[me][0] < arr[other][0]) and (arr[me][1] < arr[other][1]):
            grade[me] += 1

print(*grade)