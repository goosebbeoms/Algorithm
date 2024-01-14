import sys
T = int(input())
for t in range(T):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    print(f'Case #{t+1}: {A} + {B} = {A+B}')