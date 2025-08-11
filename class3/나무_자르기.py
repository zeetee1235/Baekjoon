import sys

x = sys.stdin.read().splitlines()
x = [list(map(int, i.split())) for i in x]
n = x[0][0]
m = x[0][1]
x.pop(0)
trees = x[0]

def count_trees(arr, mid):
    total = 0
    for tree in arr:
        if tree > mid:
            total += tree - mid
    return total

left = 0
right = max(trees)
result = 0
while left < right:
    mid = (left + right) // 2
    cnt = count_trees(trees, mid)
    if cnt >= m:
        result = mid
        left = mid + 1
    else:
        right = mid - 1
print(result)
