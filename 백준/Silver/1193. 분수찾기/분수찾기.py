X = int(input())
line = 1

while X > line:  # 라인이 입력 값보다 작은 경우에는 다음 라인으로 넘어가기 위해 변수 수치 변경
    X -= line
    line += 1

if line % 2 == 0:
    up = X
    down = line - X + 1
else:
    up = line - X + 1
    down = X

print(f'{up}/{down}')