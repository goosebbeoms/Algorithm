from collections import deque
import sys
input = sys.stdin.readline

N = int(input())    # 자료구조의 개수
A = list(map(int, input().split()))     # i번 자료구조가 큐: Ai = 0, 스택: 1
B = list(map(int, input().split()))
M = int(input())    # 수열 C의 길이
C = list(map(int, input().split()))

q = deque()

for i in range(N):
    if A[i] == 0:
        q.appendleft(B[i])
else:
    if not q:
        print(*C)
        sys.exit()

for i in range(M):
    q.append(C[i])
    print(q.popleft(), end=' ')