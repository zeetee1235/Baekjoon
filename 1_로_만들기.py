x = int(input())


num = 0
while x != 1:
    if x % 3 == 0:
       x /= 3
    else:
        x -= 1

    num += 1

print(num)