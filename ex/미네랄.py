import sys
from  collections import deque

x = sys.stdin.read().splitlines()
x = [list(map(str, i.split())) for i in x]
R = int(x[0][0])
C = int(x[0][1])
x.pop(0)
grid = [list(row[0]) for row in x[:R]]
N = int(x[-2][0])
sticks = list(map(int, x[-1]))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def throw_stick(h, a):
    global grid
    h = R - h
    if not a & 1:
        for i in range(C):
            if grid[h - 1][i] == 'x':
                grid[h - 1][i] = '.'
                return i
            else:
                continue
    else:
        for i in reversed(range(C)):
            if grid[h - 1][i] == 'x':
                grid[h - 1][i] = '.'
                return i
            else:
                continue



def bfs_find_cluster(grid):
    visited = [[False] * C for _ in range(R)]
    q = deque()

    for i in range(C):
        if grid[R - 1][i] == 'x':
            q.append((R - 1, i))
            visited[R - 1][i] = True
            
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny]:
                visited[nx][ny] = True
                if grid[nx][ny] == 'x':
                    q.append((nx, ny))

    cluster_ex = False
    clusters = []
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 'x' and not visited[i][j]:
                clusters.append((i, j))
                cluster_ex = True
    
    if not cluster_ex:
        return False
    else:
        return clusters

   
def down_cluster(grid, clusters):
    min_fall = R
    cluster_set = set(clusters)

    for x, y in clusters:
        fall = 0
        nx = x + 1
        while nx < R:
            if grid[nx][y] == 'x' and (nx, y) not in cluster_set:
                break
            if (nx, y) in cluster_set:
                nx += 1
                continue
            fall += 1
            nx += 1
        min_fall = min(min_fall, fall)

    for x, y in reversed(clusters):
        grid[x][y] = '.'
    for x, y in reversed(clusters):
        grid[x + min_fall][y] = 'x'


for i in range(len(sticks)):
    throw_stick((sticks[i] - 1), i)
    clusters = bfs_find_cluster(grid)
    if clusters != False:
        down_cluster(grid, clusters)

for i in range(R):
    print(''.join(grid[i]))