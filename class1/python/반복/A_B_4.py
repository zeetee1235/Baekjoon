import sys

for line in sys.stdin:
    try:
        x = line.split()
        x = list(map(int, x))
        print(x[0] + x[1])
    except:
        break