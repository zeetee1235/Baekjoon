import sys
from collections import deque

sys.setrecursionlimit(10**5)
x = sys.stdin.read().splitlines()
N = int(x[0])
x.pop(0)
x = [list(map(str, i.split())) for i in x]
graph = {}

for edge in x:
    a, b, c = edge
    graph[a] = [b, c]

result = []

def preorder(node):
    if node == ".":
        return
    result.append(node)
    preorder(graph[node][0])
    preorder(graph[node][1])

def inorder(node):
    if node == ".":
        return
    inorder(graph[node][0])
    result.append(node)
    inorder(graph[node][1])

def postorder(node):
    if node == ".":
        return
    postorder(graph[node][0])
    postorder(graph[node][1])
    result.append(node)

root = 'A'
preorder(root)
print("".join(result))
result = []
inorder(root)
print("".join(result))
result = []
postorder(root)
print("".join(result))

