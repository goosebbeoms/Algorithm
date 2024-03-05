N, M = map(int, input().split())
book = dict()
for i in range(1, N+1):
    name = input()
    book[str(i)] = name
    book[name] = i
for _ in range(M):
    print(book[input()])