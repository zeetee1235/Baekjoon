import sys

x = sys.stdin.read().splitlines()
y = list(map(int, x[0].split()))
n = int(y[0])
m = int(y[1])

num_list = list(map(int, x[1].split())) #수 리스트
x.pop(0)
x.pop(0)

prefix_sum = [0] * (n + 1)
for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i-1] + num_list[i-1]

queries = []
for line in x:
    queries.append(list(map(int, line.split())))
    

def add_numbers(i, j):
    return prefix_sum[j] - prefix_sum[i-1]        

result = []
for query in queries:
    add = add_numbers(query[0], query[1])
    result.append(add)

for res in result:
    print(res)
    
    