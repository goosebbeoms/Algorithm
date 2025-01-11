from collections import deque

N, K = map(int, input().split())
A = list(map(int, input().split()))
belt = deque(A)
position = deque([False] * N)

times = 0
zero_cnt = 0

while zero_cnt < K:
    times += 1

    # 1. 벨트와 로봇 회전
    belt.rotate(1)
    position.rotate(1)
    if position[N-1]:
        position[N-1] = False  # 회전 후 로봇 내리기

    # 2. 로봇 이동
    for i in range(N-2, -1, -1):
        if position[i] and not position[i+1] and belt[i+1] > 0:
            position[i] = False
            if i+1 != N-1:
                position[i+1] = True
            belt[i+1] -= 1
            if belt[i+1] == 0:
                zero_cnt += 1
    if position[N-1]:
        position[N-1] = False  # 이동 후 로봇 내리기

    # 3. 로봇 추가
    if belt[0] > 0 and not position[0]:
        position[0] = True
        belt[0] -= 1
        if belt[0] == 0:
            zero_cnt += 1

    # 4. 종료 조건 확인
    if zero_cnt >= K:
        break

print(times)