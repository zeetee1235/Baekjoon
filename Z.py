import sys
sys.setrecursionlimit(10**6)

x = sys.stdin.read().splitlines()
x = [list(map(int, i.split())) for i in x]
n = x[0][0]
r = x[0][1] + 1
c = x[0][2] + 1
count = 0

def count_z(size, r, c, x, y):
    global count
    half = size / 2
    if r <= y: # 3,4
        if c <= x: # 3
            count += ((half) ** 2) * 2
            count_z(half, r, c, x - (half / 2), y + (half / 2))
        else: # 4
            count += ((half) ** 2) * 3
            count_z(half, r, c, x + (half / 2), y + (half / 2))
    else: #1,2
        if c <= x: # 2
            count += ((half) ** 2) * 0
            count_z(half, r, c, x - (half / 2), y - (half / 2))
        else: # 1
            count += ((half) ** 2) * 1
            count_z(half, r, c, x + (half / 2), y - (half / 2))
    if half == 1:
        print(count - 1)
        sys.exit(0)

xy = (n - 1) ** 2
count_z(n ** 2, r, c, xy, xy)
            
    
    