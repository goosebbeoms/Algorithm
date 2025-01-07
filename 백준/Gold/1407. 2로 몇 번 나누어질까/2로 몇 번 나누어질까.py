A, B = map(int, input().split())

A -= 1
temp_A = A

for i in range(1, 100):
    temp_A += (A//(2**i)) * (2**i - (2**(i-1)))

temp_B = B

for i in range(1, 100):
    temp_B += (B//(2**i)) * (2**i - (2**(i-1)))

print(temp_B - temp_A)