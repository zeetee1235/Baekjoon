import sys

x = []

for line in sys.stdin:
    try:
        x.append(line.strip()) 
    except:
        break
    
num = int(x[0])
x.pop(0)

for i in range(num):
    score = 0
    acc_score = 1 #더할 점수
    langth = len(x[i])
    
    for j in range(langth):
        
        if x[i][j] == "O":
            score += acc_score
            acc_score += 1
        else:
            acc_score = 1
    print(score)
            