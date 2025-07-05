import sys

x = sys.stdin.read().splitlines()

y = x[0].split()
k = int(y[0]) #현재 랜선 개수
n = int(y[1]) #필요한 랜선 개수
x.pop(0)

right = int(max(x))
left = 1

x = [int(i) for i in x]
    
def count_cables(cables, length):
    count = 0
    for cable in cables:
        count += cable // length
    return count

while True:
    if left > right:
        break
    mid = (left + right) // 2
    if count_cables(x, mid) >= n:
        left = mid + 1
    elif count_cables(x, mid) < n:
        right = mid - 1
    else:
        break
        
        
print(right)
    
    