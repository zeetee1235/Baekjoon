import sys

x = sys.stdin.read().splitlines()
n = int(x.pop(0))
arr = list(map(int, x[0].split()))

dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)


print(max(dp))
