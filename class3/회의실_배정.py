import sys

x = sys.stdin.read().splitlines()
x = [list(map(int, i.split())) for i in x]
n = int(x[0][0])
x.pop(0)

x.sort(key=lambda x: (x[1], x[0]))

count = 0
last_end_time = 0
    
for start, end in x:
    if start >= last_end_time:
        count += 1
        last_end_time = end
    
print(count)