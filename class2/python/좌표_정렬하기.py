import sys

x = sys.stdin.read().splitlines()

n = int(x[0])
a = []
x.pop(0)

for i in range(n):
    a.append(x[i])
a = [list(map(int, a[i].split())) for i in range(n)]
    
a.sort(key=lambda coord: (coord[0], coord[1]))

for i in range(n):
    print(a[i][0], a[i][1])
        