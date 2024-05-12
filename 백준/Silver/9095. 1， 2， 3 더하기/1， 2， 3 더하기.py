T = int(input())
arr = [0] * 11
arr[1] = 1
arr[2] = 2
arr[3] = 4
arr[4] = 7

for i in range(5, len(arr)):
    arr[i] = arr[i-1] + arr[i-2] + arr[i-3]

for tc in range(T):
    print(arr[int(input())])