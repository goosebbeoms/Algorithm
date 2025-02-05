def recur(idx, cnt):
    global N, M

    if cnt == M:
        print(*stack)
        return

    for i in range(idx, N):
        stack.append(nums[i])
        recur(i, cnt+1)
        stack.pop()


N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
stack = []

recur(0, 0)