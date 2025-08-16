import sys
from collections import deque

graph = sys.stdin.read().splitlines()
graph = [list(map(int, i.split())) for i in graph]
n, m = graph.pop(0)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dist = [[-1 for _ in range(m)] for _ in range(n)]

start_x = start_y = None
for y, row in enumerate(graph):
    if 2 in row:
        start_y = y
        start_x = row.index(2)
        break

def bfs(x, y):
    q = deque()
    q.append((x, y))
    dist[y][x] = 0

    while q:
        cx, cy = q.popleft()
        for k in range(4):
            nx, ny = cx + dx[k], cy + dy[k]
            if 0 <= nx < m and 0 <= ny < n:
                if graph[ny][nx] != 0 and dist[ny][nx] == -1:
                    dist[ny][nx] = dist[cy][cx] + 1
                    q.append((nx, ny))

bfs(start_x, start_y)

for y in range(n):
    for x in range(m):
        if graph[y][x] == 0:
            dist[y][x] = 0

for row in dist:
    print(' '.join(map(str, row)))
