from collections import deque

N = int(input())
q = deque()
for num in range(1, N+1):
    q.append(num)
# 동작 시작
while len(q) >= 2:
    num1 = q.popleft()
    num2 = q.popleft()
    q.append(num2)
print(q[-1])