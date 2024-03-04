N = int(input())
cards = list(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))
cnt_dict = {i: 0 for i in nums}
for i in cards:
    if i in cnt_dict.keys():
        cnt_dict[i] = 1
print(*cnt_dict.values())