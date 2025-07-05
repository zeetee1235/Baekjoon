import sys

x = sys.stdin.read().splitlines()

a = int(x[0]) #컴퓨터 수
b = int(x[1]) #연결된 컴퓨터 쌍의 수
x.pop(0)
x.pop(0)

graph = {}
visited = []

x = [list(map(int, i.split())) for i in x]

for i in range(b):
    if x[i][0] not in graph:
        graph[x[i][0]] = []
    if x[i][1] not in graph:
        graph[x[i][1]] = []
    graph[x[i][0]].append(x[i][1])
    graph[x[i][1]].append(x[i][0])
    
def dfs(graph, start, visited):
    visited.append(start)
    for i in graph[start]:
        if i not in visited:
            dfs(graph, i, visited)

def union_find(graph, a, b):
    if a not in graph:
        graph[a] = []
    if b not in graph:
        graph[b] = []
    graph[a].append(b)
    graph[b].append(a)

union_find(graph, 1, 1)            
dfs(graph, 1, visited)
print(len(visited) - 1)
