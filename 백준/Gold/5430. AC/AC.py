from collections import deque
from typing import final


def R(arr):
    global reversed_flag

    reversed_flag = not reversed_flag


def D(arr):
    global error_checker, reversed_flag

    if len(arr) == 0:
        error_checker = True
    else:
        if reversed_flag:
            arr.pop()
        else:
            arr.popleft()


T = int(input())
for i in range(T):
    p = input()
    n = int(input())
    answer = deque(input()[1:-1].split(','))
    reversed_flag = False
    error_checker = False

    if n == 0:
        answer = deque([])

    for func in p:
        if func == "R":
            R(answer)
            if error_checker:
                break
        elif func == "D":
            D(answer)
            if error_checker:
                break

    if error_checker:
        print("error")
    else:
        if reversed_flag:
            answer.reverse()
        print(f"[{','.join(answer)}]")
