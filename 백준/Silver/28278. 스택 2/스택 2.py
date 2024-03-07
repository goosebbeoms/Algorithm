import sys
input = sys.stdin.readline

def calc(txt):
    input_str = txt.split()
    if input_str[0] == '1':
        stack.append(int(input_str[1]))
    elif input_str[0] == '2':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif input_str[0] == '3':
        print(len(stack))
    elif input_str[0] == '4':
        if stack:
            print(0)
        else:
            print(1)
    elif input_str[0] == '5':
        if stack:
            print(stack[-1])
        else:
            print(-1)


N = int(input())
stack = []
for _ in range(N):
    calc(input())