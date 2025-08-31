

import sys
sys.setrecursionlimit(10**4)


def solve_n_queens(n):
    count = 0

    def backtrack(row, cols, diag1, diag2):
        nonlocal count
        if row == n:
            count += 1
            return
        available = ~(cols | diag1 | diag2) & ((1 << n) - 1)
        while available:
            bit = available & -available
            available -= bit
            backtrack(row + 1,
                      cols | bit,
                      (diag1 | bit) << 1,
                      (diag2 | bit) >> 1)

    backtrack(0, 0, 0, 0)
    return count

N = int(input())
print(solve_n_queens(N))


'''
import sys

sys.setrecursionlimit(10**5)
N = int(input())


count = 0
cols = set()
diag1 = set()
diag2 = set()

def backtrack(row):
    global count
    if row == N:
        count += 1
        return
    for col in range(N):
        if col in cols or (row - col) in diag1 or (row + col) in diag2:
            continue
        cols.add(col)
        diag1.add(row - col)
        diag2.add(row + col)

        backtrack(row + 1)

        cols.remove(col)
        diag1.remove(row - col)
        diag2.remove(row + col)

backtrack(0)
print(count)


---------------------------------------

count = 0
board = [[0] * N for _ in range(N)]

def is_safe(row, col):
    for i in range(row):
        if board[i][col] == 1:
            return False
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    i, j = row - 1, col + 1
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1
    return True

def backtrack(row):
    global count
    if row == N:
        count += 1
        return
    for col in range(N):
        if is_safe(row, col):
            board[row][col] = 1
            backtrack(row + 1)
            board[row][col] = 0

backtrack(0)
print(count)

--------------------------------------

def solve_n_queens(n):
    result = []
    board = [-1] * n

    def is_safe(row, col):
        for prev_row in range(row):
            if board[prev_row] == col or \
               abs(board[prev_row] - col) == abs(prev_row - row):
                return False
        return True

    def backtrack(row):
        if row == n:
            result.append(board[:])
            return
        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    backtrack(0)
    return result


n = int(input())
solutions = solve_n_queens(n)
print(len(solutions))
'''