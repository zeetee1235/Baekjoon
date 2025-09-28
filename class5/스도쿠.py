import sys
import copy

grid = sys.stdin.read().splitlines()
grid = [list(map(int, i.strip())) for i in grid]

empties = []
for r in range(9):
    for c in range(9):
        if grid[r][c] == 0:
            empties.append((r, c))

def is_safe(grid, value, x, y):
    # 행, 열, 3x3 박스에 value가 있는지 체크
    for i in range(9):
        if grid[x][i] == value or grid[i][y] == value:
            return False
    box_x = (x // 3) * 3
    box_y = (y // 3) * 3
    for r in range(box_x, box_x + 3):
        for c in range(box_y, box_y + 3):
            if grid[r][c] == value:
                return False
    return True

def back_track(k=0):
    if k == len(empties):
        # 다 채웠으면 출력
        for row in grid:
            print(''.join(map(str, row)))
        sys.exit(0)  # 하나만 출력하고 끝내려면 필요
    x, y = empties[k]
    for num in range(1, 10):
        if is_safe(grid, num, x, y):
            grid[x][y] = num
            back_track(k + 1)
            grid[x][y] = 0  # 백트래킹

back_track()
