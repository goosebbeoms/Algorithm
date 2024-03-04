N = int(input())
words = []
for _ in range(N):
    words.append(input())
words.sort(key=lambda x: (len(x), x))
final = []
for word in words:
    if word not in final:
        final.append(word)
for word in final:
    print(word)