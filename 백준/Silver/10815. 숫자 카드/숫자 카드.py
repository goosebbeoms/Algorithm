N = int(input())
cards = sorted(list(map(int, input().split())))

M = int(input())
nums = list(map(int, input().split()))

answer = []

for num in nums:
    s = 0
    e = N-1
    flag = False

    while s <= e:
        mid = (s+e)//2

        if cards[mid] > num:
            e = mid-1
        elif cards[mid] < num:
            s = mid+1
        else:
            flag = True
            break

    if flag:
        answer.append(1)
    else:
        answer.append(0)

print(*answer)