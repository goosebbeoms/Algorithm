def solution(name, yearning, photo):
    answer = []
    
    for lst in photo:
        tmp_yearning = 0
        for i in range(len(name)):
            if name[i] in lst:
                tmp_yearning += yearning[i]
        answer.append(tmp_yearning)
    
    return answer