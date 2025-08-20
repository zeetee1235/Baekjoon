import sys

x = sys.stdin.read().splitlines()
x = list(map(int,x[0].split()))
n = x[0]
m = x[1]
arr = []

if n == m:
    ex = []
    for i in range(1, n+1):
        ex.append(i)
    print(*ex)
    sys.exit(0)

def nested_loops(nt, current=[]):
    global arr, table
    if len(current) == nt:
        arr.append(current)
        return
    for i in range(1, n + 1):
        nested_loops(nt, current + [i])

nested_loops(m)
arr = [x for x in arr if len(x) == len(set(x))]
seen = set()
result = []
for item in arr:
    key = tuple(sorted(item))
    if key not in seen:
        seen.add(key)
        result.append(item)

for row in result:
    print(*row)