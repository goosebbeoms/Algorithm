N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
arr.sort()
arr.sort(key=lambda x: x[1])
for i in arr:
    print(*i)
