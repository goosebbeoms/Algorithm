N = int(input())
arr = []
for _ in range(N):
    arr.append(input().split())
arr.sort(key=lambda x: int(x[0]))
for i in arr:
    print(*i)