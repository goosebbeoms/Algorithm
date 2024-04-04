from collections import defaultdict

book = defaultdict(int)
for i in range(1, 10001):
    i_lst = map(int, list(str(i)))
    book[i+sum(i_lst)] += 1

for i in range(1, 10001):
    if book[i] == 0:
        print(i)