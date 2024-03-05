import collections

N = int(input())
n_nums = list(map(int, input().split()))
M = int(input())
m_nums = list(map(int, input().split()))

book = collections.defaultdict(int)
for num in n_nums:
    book[num] += 1

for num in m_nums:
    print(book[num], end=' ')