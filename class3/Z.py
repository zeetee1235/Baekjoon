import sys
sys.setrecursionlimit(10**6)

x = sys.stdin.read().splitlines()
x = [list(map(int, i.split())) for i in x]
n = x[0][0]
r = x[0][1]
c = x[0][2]
count = 0

def count_z(size, r, c, x, y):
    global count
    half = size // 2
    if size == 1:  
        print(count)
        sys.exit(0)

    if r < y + half:
        if c < x + half:
            count_z(half, r, c, x, y)
        else:
            count += half * half
            count_z(half, r, c, x + half, y)
    else: 
        if c < x + half:
            count += 2 * half * half
            count_z(half, r, c, x, y + half)
        else:
            count += 3 * half * half
            count_z(half, r, c, x + half, y + half)

count_z(2**n, r, c, 0, 0)


