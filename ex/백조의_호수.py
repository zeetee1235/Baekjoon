import sys
from collections import deque

grid = sys.stdin.read().splitlines()
R, C = map(int, grid.pop(0).split())
grid = [list(row) for row in grid[:R]]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
swan_visited = [[0 for _ in range(C)] for _ in range(R)]
water_visited = [[0 for _ in range(C)] for _ in range(R)]
swan_q = deque()
water_q = deque()
next_swan_q = deque()
next_water_q = deque()
day = 0

swans = []
for i in range(R):
    for j in range(C):
        if grid[i][j] != 'X':
            water_q.append((i, j))
            water_visited[i][j] = True
        if grid[i][j] == 'L':
            swans.append((i, j))

(sx, sy), (ex, ey) = swans
swan_q.append((sx, sy))
swan_visited[sx][sy] = True

day = 0
while True:
    while swan_q:
        x, y = swan_q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < R and 0 <= ny < C and not swan_visited[nx][ny]:
                swan_visited[nx][ny] = True
                if grid[nx][ny] == '.':
                    swan_q.append((nx, ny))
                elif grid[nx][ny] == 'X':
                    next_swan_q.append((nx, ny))
                elif (nx, ny) == (ex, ey):
                    print(day)
                    exit()

    while water_q:
        x, y = water_q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < R and 0 <= ny < C and not water_visited[nx][ny]:
                water_visited[nx][ny] = True
                if grid[nx][ny] == 'X':
                    grid[nx][ny] = '.'
                    next_water_q.append((nx, ny))
                else:
                    water_q.append((nx, ny))

    swan_q, next_swan_q = next_swan_q, deque()
    water_q, next_water_q = next_water_q, deque()
    day += 1
