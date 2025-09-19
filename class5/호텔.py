import sys

arr = sys.stdin.read().splitlines()
arr = [list(map(int, i.split())) for i in arr]
c, n = arr.pop(0)
INF = float('inf')
MAX = 2000
dp = [INF] * (MAX + 1)
dp[0] = 0

for cost, cus in arr:
    for i in range(cus, MAX + 1):
        dp[i] = min(dp[i], dp[i - cus] + cost)

print(min(dp[c:]))