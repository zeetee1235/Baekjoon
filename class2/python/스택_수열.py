import sys

x = []

for line in sys.stdin:
    try:
        x.append(line.strip())
    except:
        break

n = int(x.pop(0))
target = list(map(int, x))

stack = []
result = []
cur = 1
possible = True

for i in range(n):
    while cur <= target[i]:
        stack.append(cur)
        result.append("+")
        cur += 1

    if stack[-1] == target[i]:
        stack.pop()
        result.append("-")
    else:
        possible = False
        break
    
if  possible:
    print("\n".join(result))
else:
    print("NO")
    
