N = int(input())
book = dict()
for _ in range(N):
    name, check = input().split()
    if check == 'enter':
        book[name] = 1
    else:
        del book[name]
final = list(book.keys())
final.sort(reverse=True)
for i in final:
    print(i)