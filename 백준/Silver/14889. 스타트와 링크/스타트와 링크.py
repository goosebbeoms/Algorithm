def bf(x, s):
    global N, p
    if x == p:
        for i in range(N):
            if not used[i]:
                st.append(i)
        s1 = 0
        s2 = 0
        for i in st[:p]:
            for j in st[:p]:
                if i != j:
                    s1 += S[i][j]
        for i in st[p:N]:
            for j in st[p:N]:
                if i != j:
                    s2 += S[i][j]
        result.append(abs(s1-s2))
        for i in range(p):
            st.pop()
        return

    for i in range(s, N):
        if not used[i]:
            st.append(i)
            used[i] = True
            bf(x+1, i+1)
            st.pop()
            used[i] = False



N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
p = N // 2      # 한 팀에 속하는 사람 수
used = [False] * N
st = []
result = []
bf(0, 0)
print(min(result))