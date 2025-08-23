import sys

x = sys.stdin.read().splitlines()
x = [list(map(int, i.split())) for i in x]
N, M = x.pop(0)
arr = x.pop(0)
visited = [False] * (N+1)
path = []
result = []

def backtrack(depth):
    global result, path, visited
    if depth == 3:
        if sum(path) <= M:
            result.append(sum(path))
        return
    
    for i in range(N):
        if sum(path) > M:
            continue
        if visited[i]:
            continue
        visited[i] = True
        path.append(arr[i])
        
        backtrack(depth + 1)
        
        path.pop()
        visited[i] = False

backtrack(0)
print(max(result))
