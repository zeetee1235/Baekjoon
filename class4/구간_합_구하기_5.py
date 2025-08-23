import sys

x = sys.stdin.read().splitlines()
x = [list(map(int, i.split())) for i in x]
N ,M = x.pop(0)
arr = []
for i in range(N):
    arr.append(x.pop(0))
query = x
dp = [[0] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + arr[i-1][j-1]

for _ in range(M):
    x1, y1, x2, y2 = query[_]
    result = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]
    print(result)