def alph_to_idx(char):
    return ord(char) - ord("A")


def recur(x, y, cnt):
    global R, C, answer

    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < C and 0 <= ny < R:
            alph_idx = alph_to_idx(arr[ny][nx])
            if visited[alph_idx]:
                continue

            visited[alph_idx] = True
            recur(nx, ny, cnt+1)
            visited[alph_idx] = False

    answer = max(answer, cnt)


R, C = map(int, input().split())
arr = [input() for _ in range(R)]
visited = [False] * (ord("Z") - ord("A") + 1)
answer = -1
visited[alph_to_idx(arr[0][0])] = True

recur(0, 0, 1)
print(answer)