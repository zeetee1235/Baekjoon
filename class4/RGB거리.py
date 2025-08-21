import sys

x = sys.stdin.read().splitlines()
N = int(x[0])
x.pop(0)
x = [list(map(int, i.split())) for i in x]
x.insert(0 ,[0, 0, 0])
for i in range(1, N + 1):
    x[i][0] = min(x[i - 1][1], x[i - 1][2]) + x[i][0]
    x[i][1] = min(x[i - 1][0], x[i - 1][2]) + x[i][1]
    x[i][2] = min(x[i - 1][1], x[i - 1][0]) + x[i][2]
    
print(min(x[N]))