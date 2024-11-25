# 입력 받기
N, H = map(int, input().split())
cnt = [0] * (H + 2)  # 높이별로 누적 합을 저장할 배열

# 장애물 정보 처리
for i in range(N):
    num = int(input())
    if i % 2 == 0:
        # 석순 처리 (짝수 번째 장애물)
        cnt[1] += 1
        cnt[num + 1] -= 1
    else:
        # 종유석 처리 (홀수 번째 장애물)
        cnt[H - num + 1] += 1
        cnt[H + 1] -= 1

# 누적 합 계산을 통해 각 높이에서의 장애물 수를 구함
for i in range(1, H + 1):
    cnt[i] += cnt[i - 1]

# 높이 1부터 H까지의 값 중 최소값과 그 개수 찾기
min_v = min(cnt[1:H+1])
cnt_min = cnt[1:H+1].count(min_v)

# 결과 출력
print(min_v, cnt_min)
