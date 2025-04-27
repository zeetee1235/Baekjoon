c = int(input())

for i in range(1, c + 1):
    x = input()
    x = x.split()
    x = list(map(int, x))
    print(x[0] + x[1])