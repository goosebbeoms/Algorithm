students = [0 for i in range(30)]
for i in range(28):
    submit_student = int(input())
    students[submit_student-1] = 1
for i in range(len(students)):
    if students[i] == 0:
        print(i+1)