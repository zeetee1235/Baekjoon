x = input()
x = x.split()
x = list(map(int, x))
if x[0] < x[1]:
    print("<")
elif x[0] > x[1]:
    print(">")
elif x[0] == x[1]:
    print("==")   
