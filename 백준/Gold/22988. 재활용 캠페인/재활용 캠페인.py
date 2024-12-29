N, X = map(int, input().split())
C = sorted(list(map(int, input().split())))

s = 0
e = N - 1

half = X / 2
cnt = 0
remain = 0

while s <= e:
    if C[e] == X:
        cnt += 1
        e -= 1
        continue

    if s == e:
        remain += 1
        break

    if C[s] + C[e] >= half:
        cnt += 1
        s += 1
        e -= 1
    else:
        s += 1
        remain += 1

print(cnt + remain//3)