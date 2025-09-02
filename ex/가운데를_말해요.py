import sys
import heapq

x = list(map(int, sys.stdin.read().splitlines()))
N = int(x.pop(0))
left, right = [], []

for i in range(N): 
    num = x[i]

    if not left or num <= -left[0]:
        heapq.heappush(left, -num)
    else:
        heapq.heappush(right, num)

    if len(left) > len(right) + 1:
        heapq.heappush(right, -heapq.heappop(left))
    elif len(right) > len(left):
        heapq.heappush(left, -heapq.heappop(right))

    print(-left[0])


