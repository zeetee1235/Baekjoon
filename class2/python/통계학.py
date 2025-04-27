import sys
from collections import Counter

x = []

for line in sys.stdin:
    try:
        numbers = list(map(int, line.split()))
        x.extend(numbers)
    except:
        break

num = x[0]
x.pop(0)
x.sort()

#산술평균
print(round(sum(x) / num))

#중앙값
print(x[num // 2])

# 최빈값
f = Counter(x)
max_f = max(f.values())
m = []
for key, value in f.items():
    if value == max_f:
        m.append(key) 
m.sort()
if len(m) > 1:
    print(m[1])
else:
    print(m[0])


#범위
print(max(x) - min(x))