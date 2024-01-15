nums = []
for i in range(10):
    nums.append(int(input()))

for i in range(len(nums)):
    nums[i] = nums[i] % 42

nums_set = set(nums)
print(len(nums_set))