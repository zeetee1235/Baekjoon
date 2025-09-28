import sys

x = sys.stdin.read().splitlines()
x = [list(map(int, i.split())) for i in x]
N, S = x[0]
arr = x[1]
del x

best = N + 1
current_sum = 0
l = 0

for r in range(N):
    current_sum += arr[r]
    while current_sum >= S:
        best = min(best, r - l + 1)
        current_sum -= arr[l]
        l += 1

print(best if best <= N else 0)