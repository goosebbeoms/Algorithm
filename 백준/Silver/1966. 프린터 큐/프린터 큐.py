from collections import deque


def check():
    global doc
    for other in q:
        if arr[other] > arr[doc]:
            q.append(doc)
            return True
    return False


T = int(input())    # 테스트 케이스 수
for tc in range(T):
    # N: 문서의 개수, M: 순서 궁금한 문서의 현 위치
    N, M = map(int, input().split())
    # N개 문서의 중요도 arr
    arr = list(map(int, input().split()))
    q = deque(list(range(N)))

    cnt = 0

    while True:
        doc = q.popleft()

        if check():
            continue
        else:
            cnt += 1
            if doc == M:
                break

    print(cnt)