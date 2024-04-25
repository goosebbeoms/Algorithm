def student1(cnt):
    lst = []
    for i in range(cnt):
        lst.append((i % 5)+1)
    return lst


def student2(cnt):
    lst = []
    nums = [1, 3, 4, 5]
    for i in range(cnt):
        if i % 2:
            lst.append(nums[(i // 2) % 4])
        else:
            lst.append(2)
    return lst


def student3(cnt):
    lst = []
    nums = [3, 1, 2, 4, 5]
    for i in range(cnt):
        lst.append(nums[(i//2)%5])
    print(lst)
    return lst


def solution(answers):
    answer = []
    
    q_num = len(answers)
    st1 = student1(q_num)
    st2 = student2(q_num)
    st3 = student3(q_num)
    
    cnt = [0, 0, 0]
    for i in range(q_num):
        if st1[i] == answers[i]:
            cnt[0] += 1
        if st2[i] == answers[i]:
            cnt[1] += 1
        if st3[i] == answers[i]:
            cnt[2] += 1
    
    for i in range(1, 4):
        if cnt[i-1] == max(cnt):
            answer.append(i)
    
    return answer