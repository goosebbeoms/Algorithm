N = int(input())
lst = []

for i in range(N//3+2):
    for j in range(N//5+2):
        if i*3 + j*5 == N:
            lst.append(i+j)
if lst:
    print(min(lst))
else:
    print(-1)
