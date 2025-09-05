import sys

x = sys.stdin.read().split()
N = int(x.pop(0))
K = int(x.pop(0))
mod = 1000000007

def inter(a, n):
    result = 1
    while n > 0:
        if n & 1:
            result = (result * a) % mod
            n -= 1
        a = (a * a) % mod
        n //= 2
    return result

fact = [1 for _ in range(N+1)]
for i in range(2, N+1):
    fact[i] = fact[i - 1] * i % mod

ans = (fact[N] % mod) * inter((fact[K] * fact[N - K]), mod -2) % mod
print(ans)