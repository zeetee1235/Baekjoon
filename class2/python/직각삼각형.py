import sys

x = sys.stdin.read().splitlines()

def triangle(x,y,z):

    if  x >= y and x >= z: #x가 가장 긴 변
        if x**2 == y**2 + z**2:
            return True
    
    if y >= x and y >= z: #y가 가장 긴 변
        if y**2 == x**2 + z**2:
            return True
        
    if z >= x and z >= y: #z가 가장 긴 변
        if z**2 == x**2 + y**2:
            return True
        
    else:
        return False

ans = []         
for i in range(0, len(x) - 1):
    a, b, c = map(int, x[i].split())
    if a == 0 and b == 0 and c == 0:
        break
    
    if triangle(a, b, c):
        ans += ['right']
    if not triangle(a, b, c):
        ans += ['wrong']
        
print('\n'.join(ans))
        
    