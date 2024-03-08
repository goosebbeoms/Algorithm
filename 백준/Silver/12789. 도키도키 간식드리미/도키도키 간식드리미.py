from collections import deque

N = int(input())
wait = deque(list(map(int, input().split())))

final_stack = []
temp_stack = []

while wait:
    p = wait[0]
    if temp_stack:
        if temp_stack[-1] < p:
            if final_stack and temp_stack[-1] > final_stack[-1]:
                final_stack.append(temp_stack.pop())
            elif final_stack and not(temp_stack[-1] > final_stack[-1]):
                print('Sad')
                break
            else:
                final_stack.append(temp_stack.pop())
        else:
            temp_stack.append(wait.popleft())
    else:
        temp_stack.append(wait.popleft())
else:
    if not (temp_stack and final_stack):
        print('Nice')    
    elif temp_stack[-1] > final_stack[-1]:
        print('Nice')
    else:
        print('Sad')