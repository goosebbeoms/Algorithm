T = int(input())

for _ in range(T):
    stack = []
    s = input()
    for c in s:
        if c == '(':
            stack.append(c)
        else:
            if stack:
                stack.pop()
            else:
                print('NO')
                break
    else:
        if stack:
            print('NO')
        else: print('YES')