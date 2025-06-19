import sys

x = sys.stdin.read().splitlines()

n = int(x[0])
x.pop(0)

metrix_list = []
for i in range(n):
    metrix_list.append(list(map(int, x[i].split())))
    
    
    
