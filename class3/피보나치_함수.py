import sys

def fibonacci(n):
    if n == 0:
        return (1, 0)
    elif n == 1:
        return (0, 1)
    else:
        a, b = fibonacci(n - 1)
        return (b, a + b)
    
x = sys.stdin.read().splitlines()
t = int(x[0])
x.pop(0)
result = []

for i in range(t):
    n = int(x[i])
    cnt0, cnt1 = fibonacci(n)
    result.append(f"{cnt0} {cnt1}")
   
print('\n'.join(result))
 
