N = int(input())  # 과목의 개수
scores = list(map(int, input().split()))
max_score = max(scores)
for i in range(len(scores)):
    scores[i] = scores[i] / max_score * 100
print(sum(scores)/len(scores))