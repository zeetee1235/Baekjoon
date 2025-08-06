import sys
from collections import deque
x = sys.stdin.read().splitlines()

t = int(x[0])
x.pop(0)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, x, y, m, n):
    queue = deque()
    queue.append((x, y))
    graph[y][x] = 0
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 1:
                graph[ny][nx] = 0
                queue.append((nx, ny))

def organic_farm(m, n, k, arr):
    graph = [[0] * m for _ in range(n)]
    count = 0
    for i in range(k):
        a, b = map(int, arr[i].split())
        graph[b][a] = 1
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(graph, j, i, m, n)
                count += 1
    return count   


idx = 0
for _ in range(t):
    m, n, k = map(int, x[idx].split())
    arr = x[idx + 1:idx + 1 + k]
    idx += k + 1
    print(organic_farm(m, n, k, arr))