nums = []
for i in range(9):
    nums.append(int(input()))

max_num = max(nums)
max_index = nums.index(max_num)

print(max_num)
print(max_index + 1)