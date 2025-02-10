def condition_checker():
    ja = 0
    mo = 0
    for alph in password:
        if checker[alph]:
            mo += 1
        else:
            ja += 1

        if ja >= 2 and mo >= 1:
            return True

    return False


def dfs(depth, idx):
    global L, C

    if depth == L:
        if condition_checker():
            print(''.join(password))
        return

    for i in range(idx, C):
        password.append(arr[i])
        dfs(depth+1, i+1)
        password.pop()


L, C = map(int, input().split())
arr = sorted(input().split())
checker = dict()

for i in range(C):
    if arr[i] in ['a', 'e', 'i', 'o', 'u']:
        checker[arr[i]] = True
    else:
        checker[arr[i]] = False

password = []
dfs(0, 0)