s = input()
alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
for char in alphabet:
    print(s.find(char), end=' ')  
