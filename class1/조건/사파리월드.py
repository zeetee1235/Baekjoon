x = input()
x = x.split()
x = list(map(int, x))
print(abs(x[0] - x[1]))