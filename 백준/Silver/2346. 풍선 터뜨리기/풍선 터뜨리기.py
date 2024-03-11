from collections import deque

N = int(input())
arr = list(map(int, input().split()))
q = deque()
result = []

for i in range(len(arr)):
    q.append((i+1, arr[i]))

for i in range(N):
    idx, num = q.popleft()
    result.append(idx)
    if q:
        if num > 0:
            for j in range(abs(num)-1):
                q.append(q.popleft())
        else:
            for j in range(abs(num)):
                q.appendleft(q.pop())

print(*result)