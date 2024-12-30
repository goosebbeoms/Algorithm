N = int(input())
text = input()

s = 0
e = 0
dist = 0
letters = [text[s]]

while s < len(text) and e < len(text):
    dist = max(dist, e-s+1)

    if len(letters) <= N:
        e += 1
        if e < len(text) and text[e] not in letters:
            letters.append(text[e])
    if len(letters) > N:
        s = s+1
        e = s
        letters = [text[s]]

print(dist)