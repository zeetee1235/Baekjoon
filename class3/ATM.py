import sys

x = sys.stdin.read().splitlines()
n = int(x[0])
x.pop(0)

p = x[0].split()
p = [int(i) for i in p]
p.sort()

result = 0
time = 0

for i in range(n):
    time += p[i]
    result += time

print(result)