import sys

x = sys.stdin.read().splitlines()
y = x[0].split()
n = int(y[0])
m = int(y[1])
x.pop(0)
a = set()
b = set()
result = []

for i in range(n):
    a.add(x[i])

for j in range(m):
    b.add(x[j + n])

for k in a:
    if k in b:
        result.append(k)
        
result.sort()
print(len(result))
for i in result:
    print(i)
    
