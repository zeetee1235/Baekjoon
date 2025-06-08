import sys

sys.setrecursionlimit(10**6) #최대 재귀 깊이 설정
x = sys.stdin.read().splitlines()
num_vertices, num_edges = map(int, x[0].split())
edges_input = x[1:]
graph_list = [list(map(int, line.split())) for line in edges_input[:num_edges]]

def sort_array(matrix, col_index):
    return sorted(matrix, key=lambda row: row[col_index])
    
sorted_graph = sort_array(graph_list, 2) #가중치 기준으로 정렬

graph = {}
for i in range(len(sorted_graph)): #그래프 생성
    u, w, weight = sorted_graph[i]
    if u not in graph:
        graph[u] = []
    if w not in graph:
        graph[w] = []
    graph[u].append((w, weight))
    graph[w].append((u, weight))

def dfs(graph, start_node): #dfs 탐색
    need_visited, visited = list(), list()
    need_visited.append(start_node)
    
    while need_visited:
        node = need_visited.pop()
        
        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])
            
    return visited

def find_root(graph, start_node):
    visited = dfs(graph, start_node)
    return visited

def union_find(parent, x):
    
    if parent[x] != x:
        parent[x] = union_find(parent, parent[x])
        
    return parent[x]

def kruskal(v, edges):
    parent = [i for i in range(v + 1)]
    mst = []
    total_weight = 0
    
    for edge in edges:
        u, v, weight = edge
        root_u = union_find(parent, u)
        root_v = union_find(parent, v)
        
        if root_u != root_v:
            mst.append(edge)
            total_weight += weight
            parent[root_v] = root_u
            
    return mst, total_weight

mst, total_weight = kruskal(num_vertices, sorted_graph)
print(total_weight)


