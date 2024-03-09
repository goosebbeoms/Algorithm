from collections import deque

N, K = map(int, input().split())
q = deque()
for num in range(1, N+1):
    q.append(num)
result = []
while q:
    for i in range(K):
        if q:
            if i != K-1:
                q.append(q.popleft())
            else:
                result.append(q.popleft())
print('<', end='')
for i in range(len(result)):
    print(result[i], end='')
    if i != len(result)-1:
        print(', ', end='')
print('>')
