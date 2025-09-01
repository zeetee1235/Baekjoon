import sys

x = sys.stdin.read().splitlines()
TC = int(x.pop(0))
x = [list(map(int, i.split())) for i in x]

for _ in range(TC):
    N, M, W = x.pop(0)
    graph = []
    
    for i in range(M):
        S, E, T = x.pop(0)
        graph.append((S, E, T))
        graph.append((E, S, T))

    for i in range(W):
        S, E, T = x.pop(0)
        graph.append((S, E, -T))

    dist = [float('inf')] * (N + 1)
    dist[0] = 0

    for i in range(1, N + 1):
        graph.append((0, i, 0))

    for i in range(N + 1):
        for u, v, w in graph:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    has_cycle = False
    for u, v, w in graph:
        if dist[u] + w < dist[v]:
            has_cycle = True
            break

    if has_cycle:
        print('YES')
    else:
        print('NO')


