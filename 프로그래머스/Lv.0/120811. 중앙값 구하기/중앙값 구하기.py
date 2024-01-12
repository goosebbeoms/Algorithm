def solution(array):
    array.sort()
    mid = (len(array)+1)//2
    answer = array[mid-1]
    return answer