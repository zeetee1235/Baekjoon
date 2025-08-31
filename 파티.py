import sys

arr = sys.stdin.read().splitlines()
arr = [list(map(int, i.split())) for i in arr]
n, m, x = arr.pop(0)

INF = float('inf')
dist = [[INF] * (n + 1) for _ in range(n+1)]

for i in range(1, n+1):
    dist[i][i] = 0

for a, b, c in arr:
    dist[a][b] = min(dist[a][b], c)

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

result = []
for i in range(1, n + 1):
    result.append(dist[i][x] + dist[x][i])

print(max(result))