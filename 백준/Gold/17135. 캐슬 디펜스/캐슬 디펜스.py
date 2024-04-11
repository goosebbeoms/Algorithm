from collections import deque
import copy
import sys
input = sys.stdin.readline

def attack_one(r, c, arr):
    global D
    target = None
    min_distance = float('inf')
    for x in range(N):
        for y in range(M):
            if arr[x][y] == 1 and abs(r - x) + abs(c - y) <= D:
                distance = abs(r - x) + abs(c - y)
                if distance < min_distance or (distance == min_distance and y < target[1]):
                    target = (x, y)
                    min_distance = distance
    if target:
        return target
    return 0

# 궁수 공격 시작
def bfs(arr):
    global D, attack
    tmp = []

    for _ in range(N):
        targets = []
        for r, c in p:
            target = attack_one(r, c, arr)
            if target != 0:
                targets.append(target)
        for target in list(set(targets)):
            arr[target[0]][target[1]] = 0
            tmp.append(target)
        arr.pop() # 맨 아래 행 제거
        arr.appendleft([0]*M) # 맨 위에 빈 행 추가, 수정 필요
    return tmp

# 궁수 3명 배치(DFS)
def dfs(start, cnt):
    global N, M, attack

    if cnt == 3:
        arr = copy.deepcopy(default_arr)
        times = len(bfs(arr))
        if attack < times:
            attack = times
        return

    for i in range(start, M):
        p.append((N, i))
        dfs(i+1, cnt+1)
        p.pop()

# N: 행, M: 열, D: 궁수 공격 거리
N, M, D = map(int, input().split())
attack = 0
# 0: 빈 칸, 1: 적 위치
default_arr = deque()
for _ in range(N):
    default_arr.append(list(map(int, input().split())))

# 궁수 스택
p = []
dfs(0, 0)

print(attack)
