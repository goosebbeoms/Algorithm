def solution(array, height):
    taller_then = []
    for i in array:
        if i > height:
            taller_then.append(i)
    answer = len(taller_then)
    return answer