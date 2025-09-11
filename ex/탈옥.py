import sys
import heapq
import copy

x = sys.stdin.read().splitlines()
T = int(x[0])
x = x[1:]
INF = float('inf')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def find_prison(grid, h, w):
    prisons = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == '$':
                prisons.append((i, j))
    (sx, sy), (ex, ey) = prisons
    return (sx, sy), (ex, ey)


def record_cost(grid, h, w):
    cost_grid = [[0 for _ in range(w)] for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if grid[i][j] == '.' or grid[i][j] == '$':
                continue
            elif grid[i][j] == '#':
                cost_grid[i][j] = 1
            elif grid[i][j] == '*':
                cost_grid[i][j] = INF
    return cost_grid


def dijkstra(cost_grid, x, y, h, w):
    dists = [[INF for _ in range(w)] for _ in range(h)]
    dists[x][y] = 0
    q = [(0, x, y)]

    while q:
        current_dist, current_x, current_y = heapq.heappop(q)
        if current_dist > dists[current_x][current_y]:
            continue

        for d in range(4):
            nx, ny = current_x + dx[d], current_y + dy[d]
            if 0 <= nx < h and 0 <= ny < w:
                dist = current_dist + cost_grid[nx][ny]
                if dist < dists[nx][ny]:
                    dists[nx][ny] = dist
                    heapq.heappush(q, (dist, nx, ny))
                
    return dists


def find_outside(grid, h, w):
    outside = []
    for i in range(h):
        for j in range(w):
            if i == 0 or i == h-1 or j == 0 or j == w-1:
                if grid[i][j] != '*':
                    outside.append((i, j))
    return outside


def solve():
    global x
    H, W = map(int, x[0].split())
    x = x[1:]
    raw = [list(row) for row in x[:H]]
    x = x[H:]

    # pad grid with '.' to represent outside
    H2, W2 = H + 2, W + 2
    grid = [['.'] * W2 for _ in range(H2)]
    for i in range(H):
        for j in range(W):
            grid[i+1][j+1] = raw[i][j]

    # find prisoners in padded grid
    (p1x, p1y), (p2x, p2y) = find_prison(grid, H2, W2)

    cost_grid = record_cost(grid, H2, W2)

    # run dijkstra from outside (0,0) and both prisoners
    dist_out = dijkstra(cost_grid, 0, 0, H2, W2)
    dist1 = dijkstra(cost_grid, p1x, p1y, H2, W2)
    dist2 = dijkstra(cost_grid, p2x, p2y, H2, W2)

    ans = INF
    for i in range(H2):
        for j in range(W2):
            dsum = dist_out[i][j] + dist1[i][j] + dist2[i][j]
            if dsum >= INF:
                continue
            # if current cell is a door '#', opening counted three times -> subtract 2
            if grid[i][j] == '#':
                dsum -= 2
            ans = min(ans, dsum)

    print(ans)


for i in range(T):
    solve()
    


