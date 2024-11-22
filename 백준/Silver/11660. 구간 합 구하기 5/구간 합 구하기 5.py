N, M = map(int, input().split())

arr = [[0] * (N+1)]
for _ in range(N):
    temp_arr = list(map(int, input().split()))
    temp = [0]
    for i in range(len(temp_arr)):
        temp.append(temp[i] + temp_arr[i])
    arr.append(temp)

points = []  # x1, y1, x2, y2
for _ in range(M):
    points.append(list(map(int, input().split())))

for x1, y1, x2, y2 in points:
    hap = 0
    for i in range(x2-x1+1):
        hap += arr[x1+i][y2] - arr[x1+i][y1-1]
    print(hap)

