n,m = map(int,input().split())
arr_a = list(map(int,input().split()))
arr_b = list(map(int,input().split()))

arr = sorted(arr_a + arr_b)
print(*arr)