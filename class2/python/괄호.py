import sys

data = []

for line in sys.stdin:
    try:
        data.append(line.strip()) 
    except:
        break

n = int(data[0])
data.pop(0)

def vps(s):
    num = 0
    for i in s:
        if num < 0:
            return False
        else:
            if i == "(":
                num += 1
            
            elif i == ")":
                num -= 1
        
    if num == 0:
        return True
    else:
        return False

for i in range(0, n):
    if vps(data[i]) == True:
        print("YES")
    else:
        print("NO")
        
