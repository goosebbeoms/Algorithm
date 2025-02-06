from itertools import permutations

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

answer = set(permutations(nums, M))
for ans in answer:
    print(*ans)