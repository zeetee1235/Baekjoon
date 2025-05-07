import sys
x = sys.stdin.read().splitlines()
    
n = int(x[0])
a = set(list(map(int, x[1].split())))

m = int(x[2])
b = list(map(int, x[3].split()))

result = []


for i in range(m):
    if b[i] in a:
        result.append("1")
    else:
        result.append("0")
        
print("\n".join(result))
            