while True:
    num = int(input())
    if num == -1:
        break
    temp = []
    for i in range(1, num):
        if num % i == 0:
            temp.append(i)
    if num == sum(temp):
        print(f'{num} =', ' + '.join(list(map(str, temp))))
    else:
        print(f'{num} is NOT perfect.')