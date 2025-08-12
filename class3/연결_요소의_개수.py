import sys

x = sys.stdin.read().splitlines()
x = [list(map(int, i.split())) for i in x]
n = x[0][0]
m = x[0][1]
x.pop(0)

graph = {i: [] for i in range(1, n+1)} 
for i in range(m):
    u, v = x[i][0], x[i][1]
    graph[u].append(v)
    graph[v].append(u)

def dfs(graph, start_node, visited):
    stack = [start_node]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            stack.extend(graph[node])

visited = set()
result = 0
for i in range(1, n+1):
    if i not in visited:
        dfs(graph, i, visited)
        result += 1
print(result)