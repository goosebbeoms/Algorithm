T = int(input())

for t in range(T):
    C = int(input())  # 거스름돈

    coins = [0, 0, 0, 0]  # 쿼터(0.25), 다임(0.1), 니켈(0.05), 페니(0.01)
    while C > 0:
        if C >= 25:
            coins[0] += int(C//25)
            C -= 25 * coins[0]
        elif C >= 10:
            coins[1] += int(C // 10)
            C -= 10 * coins[1]
        elif C >= 5:
            coins[2] += int(C // 5)
            C -= 5 * coins[2]
        else:
            coins[3] += int(C // 1)
            C -= 1 * coins[3]

    for i in coins:
        print(i, end=" ")
    print()