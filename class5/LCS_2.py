import sys

x = sys.stdin.read().splitlines()
x = [list(map(str, i.strip())) for i in x]
A = x[0]
B = x[1]

dp = [[0] * (len(x[1]) + 1) for _ in range(len(x[0]) + 1)]

for i in range(1, (len(A) + 1)):
    for j in range(1, (len(B) + 1)):
        if A[i - 1] == B[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j],dp[i][j - 1])

result = []
i, j = len(A), len(B)
while i > 0 and j > 0:
    if A[i-1] == B[j-1]:
        result.append(A[i-1])
        i -= 1
        j -= 1
    elif dp[i-1][j] > dp[i][j-1]:
        i -= 1
    else:
        j -= 1

print(max(dp[-1]))
print(''.join(reversed(result)))
