import sys

x = sys.stdin.read().splitlines()
t = int(x[0])
x.pop(0)
x = [int(i) for i in x]

max_n = max(x)
dp = [0] * (max_n + 1)
dp[0] = 1
for i in range(1, max_n + 1):
    if i - 1 >= 0:
        dp[i] += dp[i - 1]
    if i - 2 >= 0:
        dp[i] += dp[i - 2]
    if i - 3 >= 0:
        dp[i] += dp[i - 3]

for case in x:
    print(dp[case])