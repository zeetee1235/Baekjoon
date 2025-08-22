import sys

sys.setrecursionlimit(10**6)
x = sys.stdin.read().splitlines()
n = int(x.pop(0))
x = [list(map(int, i.split())) for i in x]

graph = {}
for edge in x:
    a, b = edge
    if a not in graph:
        graph[a] = []
    if b not in graph:
        graph[b] = []
    graph[a].append(b)
    graph[b].append(a)

def dfs(graph, v, visited):
    global parents
    visited[v] = True
    for neighbor in graph[v]:
        if not visited[neighbor]:
            parents[neighbor] = v
            dfs(graph, neighbor, visited)

visited = [False] * (n + 1)
parents = [0] * (n + 1)
dfs(graph, 1, visited)

print("\n".join(map(str, parents[2:])))
