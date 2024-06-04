'''
from itertools import permutations

N = int(input())

perms = list(permutations(list(range(1, N+1)), N))
perms.sort()
for item in perms:
    print(*item)
'''


def perms(x):
    global N

    if x == N+1:
        result.append(temp[:])
        return

    for i in range(1, N+1):
        if not used[i]:
            used[i] = True
            temp.append(i)
            perms(x+1)
            used[i] = False
            temp.pop()


N = int(input())
used = [False] * (N + 1)
result = []
temp = []

perms(1)
result.sort()

for item in result:
    print(*item)