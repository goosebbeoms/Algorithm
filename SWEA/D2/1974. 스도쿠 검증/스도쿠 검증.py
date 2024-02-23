def row_prove(arr):
    for lst in arr:
        temp_lst = []
        for num in lst:
            if num not in temp_lst:
                temp_lst.append(num)
            else:
                return False
    else:
        return True


def col_prove(arr):
    for idx in range(9):
        lst = []
        for i in range(9):
            lst.append(arr[i][idx])
        temp_lst = []
        for num in lst:
            if num not in temp_lst:
                temp_lst.append(num)
            else:
                return False
    else:
        return True


def square_prove(arr):
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            temp_lst = []
            for row in range(3):
                for col in range(3):
                    if arr[i+row][j+col] not in temp_lst:
                        temp_lst.append(arr[i+row][j+col])
                    else:
                        return False
    else:
        return True


T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]   # 스도구 퍼즐

    result = row_prove(arr) and col_prove(arr) and square_prove(arr)
    if result:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')