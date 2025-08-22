import sys

x = sys.stdin.read().splitlines()
t = int(x[0])
N = int(x[1])
x.pop(0)
x.pop(0)
x = [list(map(int, i.split())) for i in x]

if N & 1:
    x[0].append(0)
    x[1].append(0)
    N += 1
    
arr = []
for i in range(1, N + 1, 2):
    table = [x[0][i - 1], x[1][i - 1], x[0][i], x[1][i], x[0][i - 1] + x[1][i], x[1][i - 1] + x[0][i]] #1, 2, 3, 4, 1 + 4, 2 + 3
    arr.append(table)
    
print(arr)