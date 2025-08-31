import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)

x = sys.stdin.read().splitlines()
N = int(x.pop(0))
x = [list(map(int, i.split())) for i in x]
graph = defaultdict(list)
for edge in x:
    a, b, c = edge
    graph[a].append((b, c))
    graph[b].append((a, c))


def dfs(graph, node, dist, visited):
    max_dist = dist
    far_node = node
    visited[node] = True
    for neighbor, weight in graph[node]:
        if not visited[neighbor]:
            d , n = dfs(graph, neighbor, dist + weight, visited)
            if d > max_dist:
                max_dist = d
                far_node = n

    return max_dist, far_node

visited = [False] * (N + 1)
_ , far_node = dfs(graph, 1, 0, visited)

visited = [False] * (N + 1)
ans, _ = dfs(graph, far_node, 0, visited)

print(ans)

