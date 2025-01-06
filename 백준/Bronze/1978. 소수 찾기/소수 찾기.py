N = int(input())
arr = list(map(int, input().split()))
answer = N

for num in arr:
    if num == 1:
        answer -= 1
        continue

    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            answer -= 1
            break

print(answer)