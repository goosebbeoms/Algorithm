a, b, c, d, e, f = map(int, input().split())
# y값 구하기
y = (c*d - a*f) // (b*d - a*e)
# x값 구하기
if a != 0:
    x = (c - b*y) // a
else:
    x = (f - e*y) // d
print(x, y)