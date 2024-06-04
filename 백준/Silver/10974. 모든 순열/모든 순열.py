from itertools import permutations

N = int(input())

perms = list(permutations(list(range(1, N+1)), N))
perms.sort()
for item in perms:
    print(*item)