import sys

x = sys.stdin.read().splitlines()
N = int(x[0])
x.pop(0)
x = [list(map(int, i.split())) for i in x]
dp = [[-1 for _ in row] for row in x]
dp[0][0] = x[0][0]
for i in range(0, N -1):
    for j in range((len(x[i]))):
        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + x[i + 1][j])
        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + x[i + 1][j + 1])


print(max(dp[-1]))
