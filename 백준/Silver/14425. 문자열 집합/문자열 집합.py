N, M = map(int, input().split())
S = {input(): 1 for _ in range(N)}
cnt = 0
for _ in range(M):
    try:
        cnt += S[input()]
    except:
        pass
print(cnt)