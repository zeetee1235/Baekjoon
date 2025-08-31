import sys

x = sys.stdin.read().splitlines()
n = int(x.pop(0))
m = int(x.pop(0))
INF = float('inf')
dist = [[INF] * (n + 1) for _ in range(n+1)]
x = [list(map(int, i.split())) for i in x]

for i in range(1, n+1):
    dist[i][i] = 0

for a, b, c in x:
    dist[a][b] = min(dist[a][b], c)

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if dist[i][j] == INF:
            print(0, end=' ')
        else:
            print(dist[i][j], end=' ')
    print()