import sys

x = sys.stdin.read().splitlines()
n = int(x[0])
x.pop(0)

x = list(set(x))
x.sort(key=lambda word: word.lower())
x.sort(key=lambda word: len(word))

for i in range(len(x)):
    print(x[i])