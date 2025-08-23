import sys

x = sys.stdin.read().splitlines()
x = [list(map(str, i.strip())) for i in x]

dp = [[0] * (len(x[1]) + 1) for _ in range(len(x[0]) + 1)]

for i in range(1, (len(x[0]) + 1)):
    for j in range(1, (len(x[1]) + 1)):
        if x[0][i - 1] == x[1][j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j],dp[i][j - 1])

print(max(dp[-1]))