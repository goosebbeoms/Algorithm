N = int(input())  # 벌집 방 번호

hole = 1  # 벌집의 개수(번호)
cnt = 1
while N > hole:
    hole += 6 * cnt
    cnt += 1
print(cnt)