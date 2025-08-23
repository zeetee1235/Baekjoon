import sys

x = sys.stdin.read().splitlines()
x = [list(map(int, i.split())) for i in x]
N, K = x.pop(0)

dp = [0] * (K + 1)

for w, v in x:
    for j in range(K, w - 1, -1):
        dp[j] = max(dp[j], dp[j - w] + v)

print(dp[K])