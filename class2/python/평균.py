import sys

x = sys.stdin.read().splitlines()
x = [list(map(int, i.split())) for i in x]
N = x[0][0]
arr = x[1]
M = max(arr)

for i in range(len(arr)):
    arr[i] = (arr[i] / M) * 100

average = sum(arr) / len(arr)
print(average)