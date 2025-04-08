while True:
    x = input()
    x = x.split()
    x = list(map(int, x))
    if x[0] == 0 and x[1] == 0:
        break
    print(x[0] + x[1])