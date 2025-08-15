import sys

x = sys.stdin.read().splitlines()
x = [list(map(int, i.split())) for i in x]
n, m = x.pop(0)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
dist = [[ -1 for _ in range(m)] for _ in range(n)]
target = 2
for i, row in enumerate(x):
    if target in row:
        j = row.index(target)
        start_node = (i,j)
        break

def dfs(graph, x, y):
    visited = []
    