import sys
import heapq

x = sys.stdin.read().splitlines()
n = int(x[0])
x.pop(0)

x = [int(i) for i in x]
heap = []

for i in range(n):
    if x[i] == 0:
        if len(heap) == 0:
            print("0")
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, x[i])