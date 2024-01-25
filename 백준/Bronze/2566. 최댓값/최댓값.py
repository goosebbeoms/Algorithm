matrix = []

for i in range(9):
    matrix.append(list(map(int, input().split())))

max_value = -1
idx = [0, 0]
for i in range(9):
    for j in range(9):
        if matrix[i][j] > max_value:
            max_value = matrix[i][j]
            idx[0] = i
            idx[1] = j

print(max_value)
print(idx[0]+1, idx[1]+1)