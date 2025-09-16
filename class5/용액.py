import sys

x = sys.stdin.read().splitlines()
x = [list(map(int, i.split())) for i in x]
N = x[0][0]
arr = x[1]

l, r = 0, N - 1
best = 10**10
best_pair = (0, 0)
while l < r:
    s = arr[l] + arr[r]
    if abs(s) < best:
        best = abs(s)
        best_pair = (arr[l], arr[r])
        if best == 0:
            break
    if s < 0:
        l += 1
    else:
        r -= 1

print(best_pair[0], best_pair[1])
