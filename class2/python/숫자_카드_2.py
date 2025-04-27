import sys
from collections import Counter

x = []

for line in sys.stdin:
    try:
        x.append(line.strip()) 
    except:
        break

n = int(x[0])
m = int(x[2])


def split(data):
    parts = data.split()
    for i in range(len(parts)):
        if parts[i] == " ":
            parts.pop(i)
        else:
            pass
    return parts

num_cards = split(x[1])
target_num = split(x[3])

card_count = Counter(num_cards)
output= []
for num in target_num:
    output.append(str(card_count.get(num, 0)))
    
print(" ".join(output))
    