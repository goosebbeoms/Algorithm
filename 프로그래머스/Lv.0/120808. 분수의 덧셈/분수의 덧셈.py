import math

def solution(numer1, denom1, numer2, denom2):
    denom = denom1 * denom2
    numer = numer1*denom2 + numer2*denom1
    g = math.gcd(numer, denom)
    if g == 1:
        answer = [numer, denom]
    else:
        numer//=g
        denom//=g
        answer = [numer, denom]
    return answer