import sys

x = sys.stdin.read().splitlines()

y = x[0].split()
k = int(y[0]) # 현재 랜선 개수
n = int(y[1]) # 필요한 랜선 개수
x.pop(0)

x = [int(i) for i in x] # 먼저 변환
right = max(x) # 변환 후 최대값
left = 1
    
def count_cables(cables, length):
    count = 0
    for cable in cables:
        count += cable // length
    return count

while left <= right:
    mid = (left + right) // 2
    cnt = count_cables(x, mid)
    if cnt >= n:
        left = mid + 1
    else:
        right = mid - 1

print(right)

