import sys

sys.setrecursionlimit(10**6)
x = sys.stdin.read().splitlines()
x = [list(map(int, i.split())) for i in x]
N = x[0][0]
M = x[0][1]
arr = x[1]
path = []
visited = [False] * (N + 1)
result = []

def backtrack(depth):
    global result
    if depth == M:
        result.append(path[:])
        return
    for i in range(N):
        if visited[i]:
            continue
        visited[i] = True
        path.append(arr[i])
        
        backtrack(depth + 1)
        
        path.pop()
        visited[i] = False

backtrack(0)
result = sorted(set(tuple(r) for r in result))
result = [list(r) for r in result]
for row in result:
    print(*row)


