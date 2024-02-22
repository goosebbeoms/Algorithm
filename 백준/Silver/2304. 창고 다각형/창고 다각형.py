N = int(input())    # 기둥의 개수
pillars = []
for _ in range(N):
    pillars.append(list(map(int, input().split())))    # 각 기둥의 왼쪽 면의 위치 L, 높이 H
pillars.sort()

height_lst = [0] * (pillars[-1][0]+1)
for pillar in pillars:
    height_lst[pillar[0]] = pillar[1]
highest_idx = height_lst.index(max(height_lst))

s = 0
temp_max = 0
for i in height_lst[:highest_idx+1]:
    if temp_max < i:
        temp_max = i
    s += temp_max
temp_max = 0
for j in height_lst[len(height_lst)-1:highest_idx:-1]:
    if temp_max < j:
        temp_max = j
    s += temp_max
print(s)
