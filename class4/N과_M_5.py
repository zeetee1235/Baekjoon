import sys

x = sys.stdin.read().splitlines()
x = [list(map(int, i.split())) for i in x]
n, m = x[0]
arr = sorted(x[1])

def nested_loops(nt, current=[], used=set()):
    if len(current) == nt:
        print(*current)
        return
    for i in arr:
        if i not in used:
            used.add(i)
            nested_loops(nt, current + [i], used)
            used.remove(i)

nested_loops(m)