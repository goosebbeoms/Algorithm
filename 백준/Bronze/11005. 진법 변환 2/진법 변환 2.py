N, B = map(int, input().split())

nums = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

lst = []
number = N
while True:
    if number >= B:
        lst.insert(0, number % B)
        number = number // B
    else:
        lst.insert(0, number)
        break

converted_num = ''
for i in lst:
    converted_num += nums[i]

print(converted_num)