import sys
T = int(sys.stdin.readline())
for t in range(T):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    print(f'Case #{t+1}: {A+B}')