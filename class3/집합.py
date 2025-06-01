import sys

s = 0
result = []
    
def case_n(cmd,x):
    global s
    if cmd == "add":
        s |= (1 << x)
    elif cmd == "remove":
        if s & (1 << x):
            s &= ~(1 << x)
    elif cmd == "check":
        if s & (1 << x):
            print(1)
        else:
            print(0)
    elif cmd == "toggle":
        s ^= (1 << x)
    elif cmd == "all":
        s = (1 << 21) - 1
    elif cmd == "empty":
        s = 0 

for line in sys.stdin:
    cmd = line.strip().split()
    if len(cmd) == 2:
        case_n(cmd[0], int(cmd[1]))
    else:
        case_n(cmd[0], 0)
