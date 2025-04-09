x = input()
x = x.split()
x = list(map(int, x))
n, k = x[0], x[1]

cir = list(range(1, n + 1))
removed = []

key = 0
while len(removed) < n:
    key = (key + k - 1) % len(cir)
    removed.append(cir[key])
    cir.pop(key)

print("<" + ", ".join(map(str, removed)) + ">")
