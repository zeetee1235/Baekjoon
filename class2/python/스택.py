import sys

x = []

for line in sys.stdin:
    try:
        x.append(line.strip()) 
    except:
        break

excute_num = int(x[0])
x.pop(0)

queue = []

def split(data):
    parts = data.split()
    if len(parts) == 2:
        return parts[0], int(parts[1])
    else:
        return parts[0], None

# 명령어
def jundge(string, number):
    if string == "push":
        queue.insert(0, number)
    elif string == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
            queue.pop(0)
    elif string == "size":
        print(len(queue))
    elif string == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif string == "top":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])

for i in range(excute_num):
    command = x[i]
    string, number = split(command)
    jundge(string, number)
    
