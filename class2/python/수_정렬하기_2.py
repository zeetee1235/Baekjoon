import sys

x = sys.stdin.read().splitlines()
n = int(x[0])
x.pop(0)
x = list(map(int, x[0:]))
x.sort(reverse=False)
for i in range(n):
    print(x[i])