import math
from collections import defaultdict

N = int(input())
nums = []
cnt = defaultdict(int)

for _ in range(N):
    nums.append(int(input()))

nums.sort()

# 산술 평균
print(int(round(sum(nums) / N, 0)))

# 중앙값
print(nums[int(math.ceil(len(nums)/2))-1])

# 최빈값
for num in nums:
    cnt[num] += 1
max_cnt = max(cnt.values())

temp = []
for k, v in cnt.items():
    if v == max_cnt:
        temp.append(k)

temp.sort()
if len(temp) > 1:
    print(temp[1])
else:
    print(temp[0])

# 범위
print(max(nums) - min(nums))