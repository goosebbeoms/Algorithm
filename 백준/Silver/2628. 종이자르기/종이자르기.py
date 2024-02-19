# 종이의 가로, 세로 길이 입력
col, row = map(int, input().split())

cuts_col = [0, col]
cuts_row = [0, row]

cut = int(input())      # 절단 횟수
for t in range(cut):
    d, num = map(int, input().split())      # d: 방향, num: 줄 번호
    if d == 0:  # 가로 방향
        cuts_row.append(num)
    else:       # 세로 방향
        cuts_col.append(num)

# 각 절단 위치를 정렬
cuts_col.sort()
cuts_row.sort()

# 각 절단 사이의 거리를 구해서 가장 큰 값을 찾음
max_width = max(cuts_col[i+1] - cuts_col[i] for i in range(len(cuts_col)-1))
max_height = max(cuts_row[i+1] - cuts_row[i] for i in range(len(cuts_row)-1))

# 가장 큰 가로 길이와 세로 길이를 곱해서 가장 큰 종이 조각의 넓이를 구함
print(max_width * max_height)