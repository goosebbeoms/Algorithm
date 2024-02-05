A, B, V = map(int, input().split())     # A: 달팽이가 낮에 올라가는 거리, B: 밤에 내려가는 거리, V: 나무 막대 길이
day = (V-B-1) // (A-B) + 1
print(day)