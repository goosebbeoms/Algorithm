N = int(input())

arr = [0] * 100

arr[0] = 1
arr[1] = 2
arr[2] = 3

for i in range(3, N):
    arr[i % 100] = arr[(i-1) % 100] + arr[(i-2) % 100]

print(arr[(N-1) % 100] % 10007)
