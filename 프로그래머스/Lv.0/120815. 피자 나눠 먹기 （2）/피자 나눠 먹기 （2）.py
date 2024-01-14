def solution(n):
    dividend = n    # 피제수(나누어지는 수)
    divisor = 6    # 제수(나누는 수)
    while True:
        r = dividend % divisor    # 나머지
        if r == 0:
            break
        dividend = divisor
        divisor = r
    answer = n // divisor
    return answer