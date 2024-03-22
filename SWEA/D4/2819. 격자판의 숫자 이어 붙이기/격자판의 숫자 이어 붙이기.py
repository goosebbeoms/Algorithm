from collections import defaultdict


def dfs(row, col):
    if len(num_st) == 7:
        num_str = ''.join(num_st)
        book[num_str] += 1
        return

    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr = row + dr
        nc = col + dc
        if 0<=nr<4 and 0<=nc<4:
            num_st.append(arr[nr][nc])
            dfs(nr, nc)
            num_st.pop()


T = int(input())
for tc in range(1, T+1):
    arr = [input().split() for _ in range(4)]
    book = defaultdict(int)
    num_st = []

    for row in range(4):
        for col in range(4):
            num_st.append(arr[row][col])
            dfs(row, col)
            num_st.pop()
    print(f'#{tc}', len(book.keys()))
