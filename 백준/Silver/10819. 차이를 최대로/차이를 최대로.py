from itertools import permutations

N = int(input())
arr = list(map(int, input().split()))

perm = list(permutations(arr))
max_value = float('-inf')
for elem in perm:
    s = 0
    for i in range(len(elem)-1):
        s += abs(elem[i] - elem[i+1])
    if max_value < s:
        max_value = s

print(max_value)