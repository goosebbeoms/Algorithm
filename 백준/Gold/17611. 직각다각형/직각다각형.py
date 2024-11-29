n = int(input())    # 단순직각사각형의 꼭지점 개수
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))
data.append(data[0])

num_dict_x = {}
num_dict_y = {}

pre_x, pre_y = data[0]
for i in range(1, len(data)):
    x, y = data[i]

    if x == pre_x:
        start = min(y, pre_y)
        end = max(y, pre_y)
        if start in num_dict_y.keys():
            num_dict_y[start] += 1
        else:
            num_dict_y[start] = 1

        if end in num_dict_y.keys():
            num_dict_y[end] -= 1
        else:
            num_dict_y[end] = -1

    if y == pre_y:
        start = min(x, pre_x)
        end = max(x, pre_x)
        if start in num_dict_x.keys():
            num_dict_x[start] += 1
        else:
            num_dict_x[start] = 1

        if end in num_dict_x.keys():
            num_dict_x[end] -= 1
        else:
            num_dict_x[end] = -1

    pre_x, pre_y = x, y

num_dict_x = sorted(num_dict_x.items(), key=(lambda t:t[0]))
num_dict_y = sorted(num_dict_y.items(), key=(lambda t:t[0]))

max_x = 0
temp_x = 0
for k, v in num_dict_x:
    temp_x += v
    max_x = max(max_x, temp_x)

max_y = 0
temp_y = 0
for k, v in num_dict_y:
    temp_y += v
    max_y = max(max_y, temp_y)

print(max(max_x, max_y))
