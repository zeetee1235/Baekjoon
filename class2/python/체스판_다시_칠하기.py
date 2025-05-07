import sys

x = sys.stdin.read().splitlines()

nm = list(map(int,x[0].split()))
n = nm[0]
m = nm[1]
x.pop(0)
board = []

for i in range(n):
    board.append(list(x[i]))
    
last_n = n - 7 
last_m = m - 7
color_min = float("inf")

def check_color(b):
    b_color = 0
    w_color = 0
    
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0 and b[i][j] == "W":
                b_color += 1
            elif (i + j) % 2 == 1 and b[i][j] == "B":
                b_color += 1

    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0 and b[i][j] == "B":
                w_color += 1
            elif (i + j) % 2 == 1 and b[i][j] == "W":
                w_color += 1

    if b_color < w_color:
        color = b_color
    else:
        color = w_color
        
    return color

b_8x8 = []

for i in range(last_n):
    for j in range(last_m):
        b_8x8 = []
        for k in range(8):
            b_8x8.append(board[i + k][j:j + 8])
        color = check_color(b_8x8)
        if color < color_min:
            color_min = color
                    
print(color_min)

