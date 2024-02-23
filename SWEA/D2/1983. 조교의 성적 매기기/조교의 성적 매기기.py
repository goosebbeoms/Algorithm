lst = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())    # N: 학생 수, K: 학점 조회 학생 번호
    grades = []     # 중간, 기말, 과제 점수
    for cnt in range(1, N+1):
        grades.append([cnt] + list(map(int, input().split())))
    temp = []
    for grade in grades:
        temp.append([grade[1]*0.35 + grade[2]*0.45 + grade[3]*0.2] + grade)

    temp.sort(key=lambda x:x[0], reverse=True)
    for idx in range(len(temp)):
        temp[idx].append(lst[idx//(N//10)])

    temp.sort(key=lambda x:x[1])
    print(f'#{tc}', temp[K-1][-1])