# 백준 2635번 - 수 이어가기

num = int(input())  # 첫 번째 수
max_cnt = 0
max_lst = []

for i in range(num//2, num+1):
    cnt = 2
    temp_lst = [num, i]
    temp_num = temp_lst[-2] - temp_lst[-1]
    while temp_num >= 0:
        temp_lst.append(temp_num)
        cnt += 1
        temp_num = temp_lst[-2] - temp_lst[-1]
    if max_cnt < cnt:
        max_cnt = cnt
        max_lst = temp_lst[:]

print(max_cnt)
print(*max_lst)
