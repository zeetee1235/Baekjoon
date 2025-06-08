import sys

sys.setrecursionlimit(10**6)
x = sys.stdin.read().splitlines()
y = x[0].split()
n = int(y[0])
m = int(y[1])
x.pop(0)

vertices_list = [list(map(int, line.split())) for line in x[:m]]

graph = {}

def dfs(graph, start_node):
    need_visited, visited = list(), list()
    need_visited.append(start_node)
    
    while need_visited:
        node = need_visited.pop()
        
        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])
            
    return visited

def union_find(parent, x):
    if parent[x] != x:
        parent[x] = union_find(parent, parent[x])
    return parent[x]

def find_root(graph, start_node):
    visited = dfs(graph, start_node)
    return visited

def main(vertices):
    parent = [i for i in range(n + 1)]
    result = 0
    for i in range(len(vertices)):
        u, v = vertices[i]
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)
        root_u = union_find(parent, u)
        root_v = union_find(parent, v)
        if root_u == root_v:
            result = i + 1
            break
        else:
            parent[root_v] = root_u
    print(result)
    

main(vertices_list)
