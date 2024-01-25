matrix = []

for _ in range(5):
    matrix.append(list(input()))

max_len = 0
for _ in matrix:
    if len(_) > max_len:
        max_len = len(_)

final_word = ''
for j in range(max_len):
    tmp_word = ''
    for i in range(5):
        try:
            tmp_word += matrix[i][j]
        except IndexError:
            continue
    final_word += tmp_word

print(final_word)