import sys

x = sys.stdin.read().splitlines()
n = int(x[0])
pre = list(map(int, x[1].split()))

coords = []
for i in range(n):
    coords.append([i, pre[i]])

sorted_unique = sorted(set(pre))
rank = {num: idx for idx, num in enumerate(sorted_unique)}

for i in range(n):
    coords[i][1] = rank[coords[i][1]]

print(' '.join(str(coords[i][1]) for i in range(n)))