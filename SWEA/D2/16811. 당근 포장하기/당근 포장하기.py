T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 당근의 개수
    carrets = list(map(int, input().split()))  # N개의 당근 크기 배열

    counts = [0] * (max(carrets)+1)
    for i in carrets:
        counts[i] += 1

    diff_lst = []
    for l1 in range(1, len(counts)-2):
        for l2 in range(l1+1, len(counts)-1):
            temp_boxes = [0, 0, 0]      # 소, 중, 대 박스
            for i in counts[1:l1+1]:
                temp_boxes[0] += i
            for j in counts[l1+1:l2+1]:
                temp_boxes[1] += j
            for k in counts[l2+1:]:
                temp_boxes[2] += k
            if max(temp_boxes) > N//2:
                continue
            diff_lst.append(max(temp_boxes) - min(temp_boxes))

    if diff_lst:
        diff = min(diff_lst)
    else:
        diff = -1

    print(f'#{tc}', diff)