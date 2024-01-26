N = int(input())

arr = [[0 for x in range(101)] for y in range(101)]

count = 0

for _ in range(N):
    tmp_coordinate = []
    x, y = map(int, input().split())
    
    for i in range(x, x+10):
        for j in range(y, y+10):
            arr[i][j] = 1

for i in range(101):
    for j in range(101):
        if arr[i][j] == 1:
            count += 1

print(count)