switch_num = int(input())   # 스위치의 개수
switches = list(map(int, input().split()))   # on(1)/off(0) 상태
student_num = int(input())      # 학생 수
for _ in range(student_num):
    gen, num = map(int, input().split())
    if gen == 1:
        for i in range(num, switch_num+1):
            if i % num == 0:
                if switches[i-1] == 1:
                    switches[i-1] = 0
                else:
                    switches[i-1] = 1
    else:
        if switches[num-1] == 1:
            switches[num-1] = 0
        else:
            switches[num-1] = 1
        j = 1
        while num-j-1 >= 0 and num+j-1 < switch_num:
            if switches[num-1-j] == switches[num-1+j] == 1:
                switches[num-1-j] = 0
                switches[num-1+j] = 0
                j += 1
            elif switches[num-1-j] == switches[num-1+j] == 0:
                switches[num-1-j] = 1
                switches[num-1+j] = 1
                j += 1
            else:
                break

for i in range(len(switches)):
    if (i+1)%20==0:
        print(switches[i])
        continue
    print(switches[i], end=' ')