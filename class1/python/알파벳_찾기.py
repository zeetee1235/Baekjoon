s = input()
alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
for j in alphabet:
    print(s.find(j), end=' ')
