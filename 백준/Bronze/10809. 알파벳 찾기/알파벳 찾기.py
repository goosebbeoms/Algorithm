S = input()
position = [(-1) for i in range(26)]
for i in range(len(S)):
    idx = ord(S[i])-97
    if position[idx] == (-1):
        position[idx] = i
    else:
        continue
for i in position:
    print(i, end=' ')