import sys

x = sys.stdin.read().splitlines()
x = [list(map(int, i.split())) for i in x]
n = x[0][0]
r = x[0][1]
c = x[0][2]