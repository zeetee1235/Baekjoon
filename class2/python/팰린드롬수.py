import sys

x = sys.stdin.read().splitlines()

if x[-1] == '0':
    x.pop()

for num in x:
    if num == num[::-1]:
        print('yes')
    else:
        print('no')