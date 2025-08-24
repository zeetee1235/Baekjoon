import sys
from collections import deque

s = sys.stdin.readline()
lst = list(map(int, s.split()))
n = lst[0]
k = lst[1]

dq = deque([n])
MAX = 100000
dist = [-1] * (MAX + 1)
dist[n] = 0

if n == k:
    print(0)
    sys.exit(0)
if n > k:
    print(n - k)
    sys.exit(0)

while dq:
    x = dq.popleft()
    if x == k:
        print(dist[x])
        sys.exit(0)
    for i in (x - 1, x + 1, x * 2):
        if 0 <= i <= MAX and dist[i] == -1:
            if i == x * 2:
                dist[i] = dist[x]
                dq.appendleft(i)
            else:
                dist[i] = dist[x] + 1
                dq.append(i)

