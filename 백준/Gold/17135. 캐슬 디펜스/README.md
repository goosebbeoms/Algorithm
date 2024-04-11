# [Gold III] 캐슬 디펜스 - 17135 

[문제 링크](https://www.acmicpc.net/problem/17135) 

### 성능 요약

메모리: 116856 KB, 시간: 360 ms

### 분류

너비 우선 탐색, 브루트포스 알고리즘, 그래프 이론, 그래프 탐색, 구현, 시뮬레이션

### 제출 일자

2024년 4월 11일 17:09:13

### 문제 설명

<p>캐슬 디펜스는 성을 향해 몰려오는 적을 잡는 턴 방식의 게임이다. 게임이 진행되는 곳은 크기가 N×M인 격자판으로 나타낼 수 있다. 격자판은 1×1 크기의 칸으로 나누어져 있고, 각 칸에 포함된 적의 수는 최대 하나이다. 격자판의 N번행의 바로 아래(N+1번 행)의 모든 칸에는 성이 있다.</p>

<p>성을 적에게서 지키기 위해 궁수 3명을 배치하려고 한다. 궁수는 성이 있는 칸에 배치할 수 있고, 하나의 칸에는 최대 1명의 궁수만 있을 수 있다. 각각의 턴마다 궁수는 적 하나를 공격할 수 있고, 모든 궁수는 동시에 공격한다. 궁수가 공격하는 적은 거리가 D이하인 적 중에서 가장 가까운 적이고, 그러한 적이 여럿일 경우에는 가장 왼쪽에 있는 적을 공격한다. 같은 적이 여러 궁수에게 공격당할 수 있다. 공격받은 적은 게임에서 제외된다. 궁수의 공격이 끝나면, 적이 이동한다. 적은 아래로 한 칸 이동하며, 성이 있는 칸으로 이동한 경우에는 게임에서 제외된다. 모든 적이 격자판에서 제외되면 게임이 끝난다. </p>

<p>게임 설명에서 보다시피 궁수를 배치한 이후의 게임 진행은 정해져있다. 따라서, 이 게임은 궁수의 위치가 중요하다. 격자판의 상태가 주어졌을 때, 궁수의 공격으로 제거할 수 있는 적의 최대 수를 계산해보자.</p>

<p>격자판의 두 위치 (r<sub>1</sub>, c<sub>1</sub>), (r<sub>2</sub>, c<sub>2</sub>)의 거리는 |r<sub>1</sub>-r<sub>2</sub>| + |c<sub>1</sub>-c<sub>2</sub>|이다.</p>

### 입력 

 <p>첫째 줄에 격자판 행의 수 N, 열의 수 M, 궁수의 공격 거리 제한 D가 주어진다. 둘째 줄부터 N개의 줄에는 격자판의 상태가 주어진다. 0은 빈 칸, 1은 적이 있는 칸이다.</p>

### 출력 

 <p>첫째 줄에 궁수의 공격으로 제거할 수 있는 적의 최대 수를 출력한다.</p>


### 아래 코드 풀이 방식도 확인해보기!!!
```python
import sys
from itertools import combinations
gets = sys.stdin.readline

n, m, d = map(int, gets().split())

board = [list(map(lambda x: True if x == '1' else False, gets().split())) for i in range(n)]

ans = 0
max_ans = 0
for i in range(n):
    for j in range(m):
        if board[i][j]:
            max_ans += 1

def get_target_bfs(y, time):
    x = n - time - 1
    for tmp_dist in range(d):
        tmp_x, tmp_y = x, y-tmp_dist
        for i in range(tmp_dist):
            if tmp_x >= 0 and tmp_x < n and tmp_y >= 0 and tmp_y < m:
                if board[tmp_x][tmp_y]:
                    return tuple([tmp_x,tmp_y])
            tmp_x -= 1
            tmp_y += 1
        for i in range(tmp_dist):
            if tmp_x >= 0 and tmp_x < n and tmp_y >= 0 and tmp_y < m:
                if board[tmp_x][tmp_y]:
                    return tuple([tmp_x,tmp_y])
            tmp_x += 1
            tmp_y += 1
        if tmp_x >= 0 and tmp_x < n and tmp_y >= 0 and tmp_y < m:
            if board[tmp_x][tmp_y]:
                return tuple([tmp_x, tmp_y])

    return False


def simulate(archers):
    global ans
    tmp_ans = 0
    killed_set = set()

    for i in range(n):
        if tmp_ans + 3*(n-i) <= ans:
            break
        if tmp_ans >= max_ans:
            break

        tmp_killed_set = set()
        for y in archers:
            tmp_killed = get_target_bfs(y, i)
            if tmp_killed:
                tmp_killed_set.add(tmp_killed)
        for x, y in tmp_killed_set:
            board[x][y] = False
            tmp_ans += 1
        killed_set = killed_set.union(tmp_killed_set)
    if tmp_ans >= ans:
        ans = tmp_ans

    for x, y in killed_set:
        board[x][y] = True

    return

for archers in combinations(range(m), 3):
    simulate(archers)

print(ans)
```
