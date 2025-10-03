import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
M = int(input())
dp = [[0] * N for _ in range(N)]

# 길이 1 구간
for i in range(N):
    dp[i][i] = 1

# 길이 2 구간
for i in range(N-1):
    if nums[i] == nums[i+1]:
        dp[i][i+1] = 1

# 길이 3 이상
for length in range(3, N+1):
    for i in range(N-length+1):
        j = i + length - 1
        if nums[i] == nums[j] and dp[i+1][j-1]:
            dp[i][j] = 1

result = []
for _ in range(M):
    s, e = map(int, input().split())
    result.append(str(dp[s-1][e-1]))

print('\n'.join(result))