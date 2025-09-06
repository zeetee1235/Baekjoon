import sys

matrix = sys.stdin.read().splitlines()
matrix = [list(map(int, i.split())) for i in matrix]
N, B = matrix.pop(0)
mod = 1000
table = [list(row) for row in matrix[:N]]


def pow_mat(mat, n):
    result = [[1 if i == j else 0 for j in range(N)] for i in range(N)]
    while n > 0:
        if n & 1:
            result = mult_mat(result, mat)
        mat = mult_mat(mat, mat)
        n //= 2
    return result


def mult_mat(X, Y):
    result = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += ((X[i][k] % mod) * (Y[k][j] % mod)) % mod
    for i in range(N):
        for j in range(N):
            result[i][j] %= mod
    return result


result = [[0] * N for _ in range(N)]
result = pow_mat(matrix, B)
for i in range(N):
    print(' '.join(map(str, result[i][:])))
