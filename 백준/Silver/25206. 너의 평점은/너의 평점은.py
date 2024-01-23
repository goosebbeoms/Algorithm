grade_dict = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0
    }

subj_name_list = []
subj_point_list = []
subj_grade_list = []
point_times_grade = []

for i in range(20):
    subject_name, subject_point, subject_grade = input().split()
    if subject_grade == 'P':
        continue
    subj_name_list.append(subject_name)
    subj_point_list.append(float(subject_point))
    subj_grade_list.append(subject_grade)

for idx in range(len(subj_grade_list)):
    subj_grade_list[idx] = float(grade_dict[subj_grade_list[idx]])
    point_times_grade.append(subj_point_list[idx] * subj_grade_list[idx])


# 전공 평점 계산
final = sum(point_times_grade) / sum(subj_point_list)
print(final)