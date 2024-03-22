def dfs(x, sub):
    global add, minus, multiply, divide, min_v, max_v

    if x == N-1:
        min_v = min(min_v, sub)
        max_v = max(max_v, sub)
        return

    if add > 0:
        add -= 1
        dfs(x+1, sub + operand[x+1])
        add += 1

    if minus > 0:
        minus -= 1
        dfs(x+1, sub - operand[x+1])
        minus += 1

    if multiply > 0:
        multiply -= 1
        dfs(x+1, sub * operand[x+1])
        multiply += 1

    if divide > 0:
        divide -= 1
        dfs(x+1, int(sub/operand[x+1]))
        divide += 1


N = int(input())    # 숫자의 개수
# operator
operand = list(map(int, input().split()))       # 피연산자
add, minus, multiply, divide = map(int, input().split())
min_v = int(1e10)
max_v = int(-1e10)
dfs(0, operand[0])
print(max_v)
print(min_v)