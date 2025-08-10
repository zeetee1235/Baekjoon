import sys

x = sys.stdin.read().splitlines()
n = int(x[0])
x.pop(0)
arr = [list(map(int, i.split())) for i in x]

white = 0
blue = 0

def count_color(x, y, size):
    global white, blue
    eq = True
    color = arr[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if arr[i][j] != color:
                eq = False
                break
        if not eq:
            break
    if eq:
        if color == 0:
            white += 1
        else:
            blue += 1
    else:
        half = size // 2
        count_color(x, y, half)
        count_color(x, y + half, half)
        count_color(x + half, y, half)
        count_color(x + half, y + half, half)
        
count_color(0,0,n)

print(f"{white}\n{blue}")