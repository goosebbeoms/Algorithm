N, M = map(int, input().split())  # 행렬의 크기

matrix_1 = []
matrix_2 = []
added_matrix = []

for n in range(N):
    matrix_1.append(list(map(int, input().split())))

for n in range(N):
    matrix_2.append(list(map(int, input().split())))

for n in range(N):
    tmp_matrix = []
    for m in range(M):
        tmp_matrix.append(matrix_1[n][m] + matrix_2[n][m])
    added_matrix.append(tmp_matrix)

for i in range(len(added_matrix)):
    for j in range(len(added_matrix[i])):
        print(added_matrix[i][j], end=' ')
    print()