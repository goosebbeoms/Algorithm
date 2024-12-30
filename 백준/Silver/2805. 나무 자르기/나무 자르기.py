N, M = map(int, input().split())            # N: 나무의 수, M: 집으로 가져가려는 나무의 길이
trees = list(map(int, input().split()))     # 나무들(각 나무의 높이)
# 적어도 M미터의 나무를 가져가기 위해 설정할 수 있는 절단기의 최대 높이는?

h = max(trees)
l = 1


while l <= h:
    mid = (h + l) // 2
    cut = 0
    for tree in trees:
        if tree >= mid:
            cut += tree - mid

    if cut >= M:
        l = mid + 1
    elif cut < M:
        h = mid - 1

print(h)