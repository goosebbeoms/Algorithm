N, M = map(int, input().split())
not_hear = dict()
for _ in range(N):
    name = input()
    not_hear[name] = 0

cnt = 0
names = []
for _ in range(M):
    name = input()
    try:
        not_hear[name] += 1
        cnt += 1
        names.append(name)
    except KeyError:
        continue
names.sort()
print(cnt)
for name in names:
    print(name)