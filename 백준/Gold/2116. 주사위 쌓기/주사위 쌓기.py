import copy

def check(n):
    global idx1
    global idx2
    global num
    idx1 = n
    if idx1 == 0:
        idx2 = 5
    elif idx1 == 1:
        idx2 = 3
    elif idx1 == 2:
        idx2 = 4
    elif idx1 == 3:
        idx2 = 1
    elif idx1 == 4:
        idx2 = 2
    elif idx1 == 5:
        idx2 = 0
    temp = dice[num][idx2]
    dice_copy[num][idx1], dice_copy[num][idx2] = 0, 0      # 주사위 아래, 윗면 0으로
    if num < len(dice)-1:
        idx1 = dice[num+1].index(temp)



T = int(input())        # 주사위 개수
dice = []               # 주사위 눈금 순서
for _ in range(T):
    dice.append(list(map(int, input().split())))

sum_lst = []

for idx in range(len(dice[0])):
    dice_copy = copy.deepcopy(dice)
    idx1 = idx  # 주사위 아랫면
    idx2 = 0    # 주사위 윗면
    for num in range(len(dice)):
        check(idx1)

    temp_sum = 0
    for lst in dice_copy:
        temp_sum += max(lst)
    sum_lst.append(temp_sum)

print(max(sum_lst))