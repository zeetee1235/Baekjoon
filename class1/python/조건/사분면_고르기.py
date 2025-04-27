x = int(input())
y = int(input())
xe = None
ye = None
if x > 0:
    xe = 1
else:
    xe = 0
if y > 0:
    ye = 1
else:
    ye = 0
if xe == 1 and ye == 1:
    print("1")
elif xe == 0 and ye == 1:
    print("2")
elif xe == 0 and ye == 0:
    print("3")
elif xe == 1 and ye == 0:
    print("4")