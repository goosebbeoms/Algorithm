lights = [0] + list(input())
for i in range(len(lights)):
    if lights[i] == 'Y':
        lights[i] = True
    else:
        lights[i] = False

cnt = 0
for idx in range(len(lights)):
    if lights[idx]:
        cnt += 1
        for i in range(idx, len(lights)):
            if i % idx == 0:
                lights[i] = not lights[i]

print(cnt)