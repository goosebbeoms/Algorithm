N = int(input())
x = list(map(int, input().split()))
x_2 = sorted(list(set(x)))
cnt_dict = {x_2[i]: i for i in range(len(x_2))}
for i in x:
    print(cnt_dict[i], end=' ')
