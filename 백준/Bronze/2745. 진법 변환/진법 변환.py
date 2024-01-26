N, B = input().split()

nums = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

lst = []
for t in N:
    idx = nums.index(t)
    lst.insert(0, idx)

lst2 = []
for i in range(len(lst)):
    lst2.append((int(B)**i) * lst[i])


print(sum(lst2))
