v1 = v2 = -1
while True:
    v1, v2 = map(int, input().split())
    if v1 == 0 and v2 == 0:     # 코드 종료 조건
        break

    if v2 % v1 == 0:
        print('factor')
    elif v1 % v2 == 0:
        print('multiple')
    else:
        print('neither')