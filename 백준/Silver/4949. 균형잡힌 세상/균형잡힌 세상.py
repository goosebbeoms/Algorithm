while True:
    s = input()
    stack = []
    if s == '.':
        break
    for c in s:
        if c not in ['(', '[', ')', ']']:
            continue
        elif c in ['(', '[']:
            stack.append(c)
        elif c in [')', ']']:
            if stack:
                if c == ')' and stack[-1] == '(':
                    stack.pop()
                elif c == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    print('no')
                    break
            else:
                print('no')
                break
    else:
        if stack:
            print('no')
        else:
            print('yes')
