import sys

x = sys.stdin.read().split()
A = int(x[0])
B = int(x[1])
C = int(x[2])

def inter(a, n, mod):
    result = 1
    while n > 0:
        if n & 1:
            result = (result * a) % mod
            n -= 1
        a = (a * a) % mod
        n //= 2
    return result

print(inter(A,B,C))