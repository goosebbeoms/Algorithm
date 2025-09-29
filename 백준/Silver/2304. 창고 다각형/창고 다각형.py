N = int(input())
graph = [0] * 10001
x_list = []
y_list = []

for _ in range(N):
    idx, hight = map(int, input().split())
    graph[idx] = hight
    x_list.append(idx)
    y_list.append(hight)

max_hight = max(y_list)
max_width = max(x_list)
prefix = [0] * (max_width + 2)
suffix = [0] * (max_width + 2)

max_point = []

# prefix
h = 0
for f in range(1, max_width + 3):
    if graph[f] == max_hight:
        max_point.append(f)
        break
    h = max(h, graph[f])
    prefix[f] = prefix[f-1] + h

h = 0
for b in range(max_width, 0, -1):
    if graph[b] == max_hight:
        max_point.append(b)
        break
    h = max(h, graph[b])
    suffix[b] = suffix[b+1] + h

answer = max(prefix) + max(suffix)
answer += (max_point[1] - max_point[0] + 1) * max_hight

print(answer)