import sys

x = sys.stdin.read().splitlines()
n = int(x[0])
m = n // 5
a = -1

for i in range(m, -1, -1):
    p = i * 5
    if (n - p) % 3 == 0:
        a = i + (n - p) // 3
        break

print(a)