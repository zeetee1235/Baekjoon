import sys

x = sys.stdin.read().splitlines()
n = int(x[0])
x.pop(0)
members = [list(map(str, x[i].split())) for i in range(n)]
for i in range(n):
    members[i][0] = int(members[i][0])
members.sort(key=lambda coord: coord[0])

for i in range(n):
    print(members[i][0], members[i][1])


