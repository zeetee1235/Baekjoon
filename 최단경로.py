import sys
import heapq

x = sys.stdin.read().splitlines()
x =[list(map(int,i.split())) for i in x]
V, E = x.pop(0)
K = int(x[0][0])
x.pop(0)

graph = {}
for edge in x:
    a, b, c = edge
    if a not in graph:
        graph[a] = []
    if b not in graph:
        graph[b] = []
    graph[a].append((b, c))


def dijkstra(graph, start):
    distances = {node: float('inf') for node in range(1, V+1)}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances


ans = dijkstra(graph, K)
for i in range(1, V+1):
    if str(ans[i]) == 'inf':
        print('INF')
    else:
        print(ans[i])