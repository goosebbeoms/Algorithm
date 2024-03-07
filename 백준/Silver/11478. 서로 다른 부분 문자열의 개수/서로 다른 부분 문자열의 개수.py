import collections
S = input()
book = collections.defaultdict(int)
for i in range(1, len(S)+1):
    for j in range(0, len(S)+1-i):
        book[S[j:j+i]] += 1
print(len(book.keys()))