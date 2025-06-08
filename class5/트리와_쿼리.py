import sys
sys.setrecursionlimit(10**6)

x = sys.stdin.read().splitlines()
y = x[0].split()
x.pop(0)
n = int(y[0])
r = int(y[1])
query_num = int(y[2])
query_list = [int(line) for line in x[-query_num:]]
x = x[:-query_num]


graph_list = [list(map(int, line.split())) for line in x[:n-1]]
graph = {}
for i in range(len(graph_list)): #그래프 생성
    u, v = graph_list[i]
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)
    
    
def dfs(graph, start_node): #dfs 탐색
    need_visited, visited = list(), list()
    need_visited.append(start_node)
    
    while need_visited:
        node = need_visited.pop()
        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])
    return visited


def find_parent(graph, start_node): #루트 노드 찾기
    visited = dfs(graph, start_node)
    return visited[0] if visited else None

"""
def sub_tree(graph, start_node): #서브트리 생성
    find_parent_node = find_parent(graph, start_node)
    if find_parent_node is None:
        return []
    sub_graph = {}
    visited = set()
    need_visited = [find_parent_node]
    while need_visited:
        node = need_visited.pop()
        if node not in visited:
            visited.add(node)
            if node not in sub_graph:
                sub_graph[node] = []
            for neighbor in graph[node]:
                if neighbor not in visited:
                    sub_graph[node].append(neighbor)
                    if neighbor not in sub_graph:
                        sub_graph[neighbor] = []
                    need_visited.append(neighbor)
    return sub_graph
"""

subtree_size = [0] * (n+1)
def compute_subtree(u, parent): # 서브트리 크기 계산
    subtree_size[u] = 1
    for v in graph[u]:
        if v == parent:
            continue
        compute_subtree(v, u)
        subtree_size[u] += subtree_size[v]

compute_subtree(r, 0)

def main(graph, query_list): #메인 함수
    result = []
    for start_node in query_list:
        result.append(subtree_size[start_node])
    return result

result = main(graph, query_list)
for i in range(len(result)):
    print(result[i])
    
    