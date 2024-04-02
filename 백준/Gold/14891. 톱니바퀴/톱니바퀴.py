from collections import deque
import sys
input = sys.stdin.readline


def is_left_turn(num, left_v):
    if num < 0:
        return False
    elif book[num][2] != left_v:
        return True
    return False


def is_right_turn(num, right_v):
    if num > 3:
        return False
    elif book[num][6] != right_v:
        return True
    return False


def calc(num, d):
    if num < 0 or num > 3:
        return

    right_v, left_v = book[num][2], book[num][6]
    book[num].rotate(d)
    visited[num] = True

    if is_left_turn(num-1, left_v) and not visited[num-1]:
        calc(num-1, -d)
    if is_right_turn(num+1, right_v) and not visited[num+1]:
        calc(num+1, -d)
    return


book = {}
for i in range(4):
    book[i] = deque(list(map(int, list(input().strip()))))

K = int(input())    # 회전 횟수
for _ in range(K):
    num, d = map(int, input().split())
    visited = [False] * 4
    calc(num-1, d)

result = 0
for i in range(4):
    if book[i][0] == 1:
        result += 2**i

print(result)