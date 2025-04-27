import sys

x = []

for line in sys.stdin:
    try:
        x.append(line.strip()) 
    except:
        break

n = int(x[0])
x.pop(0)

spot = [tuple(map(int, item.split())) for item in x]

def shoelace_area(coords):
    n = len(coords)
    area = 0
    for i in range(n):
        x1, y1 = coords[i]
        x2, y2 = coords[(i+1) % n]
        area += (x1 * y2 - y1 * x2)
    return abs(area) / 2

print(shoelace_area(spot))
