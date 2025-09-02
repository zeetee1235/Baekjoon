import sys
import heapq
from collections import defaultdict

arr = sys.stdin.read().splitlines()
arr = [list(map(int, i.split())) for i in arr]
n, m, x = arr.pop(0)

graph = defaultdict(list)
reverse_graph = defaultdict(list)
for a, b, c in arr:
    graph[a].append((b, c))
    reverse_graph[b].append((a, c))

def dijkstra(start, graph):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    q = [(0, start)]
    while q:
        d, cur = heapq.heappop(q)
        if dist[cur] < d:
            continue
        for nxt, cost in graph[cur]:
            nd = d + cost
            if nd < dist[nxt]:
                dist[nxt] = nd
                heapq.heappush(q, (nd, nxt))
    return dist

to_home = dijkstra(x, graph)

from_home = dijkstra(x, reverse_graph)

max_time = 0
for i in range(1, n + 1):
    total = from_home[i] + to_home[i]
    if total < float('inf'):
        max_time = max(max_time, total)

print(max_time)

