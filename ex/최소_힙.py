#최소 힙 직접 구현
import sys

x = sys.stdin.read().splitlines()

n = int(x[0])
x.pop(0)

heap = []

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
    return arr

def insert(arr, value):
    arr.append(value)
    idx = len(arr) - 1
    
    while idx > 0:
        parent_idx = (idx - 1) // 2
        if arr[parent_idx] > arr[idx]:
            swap(arr, idx, parent_idx)
            idx = parent_idx
        else:
            break
    return arr
    
def delete(arr):
    if len(arr) == 0:
        return arr
    
    min_val = arr[0]
    print(min_val)
    
    if len(arr) == 1:
        arr.pop()
        return arr
    
    arr[0] = arr[-1]
    arr.pop()
    
    idx = 0
    while True:
        left_child = 2 * idx + 1
        right_child = 2 * idx + 2
        smallest = idx
        
        if left_child < len(arr) and arr[left_child] < arr[smallest]:
            smallest = left_child
        if right_child < len(arr) and arr[right_child] < arr[smallest]:
            smallest = right_child
            
        if smallest != idx:
            swap(arr, idx, smallest)
            idx = smallest
        else:
            break
    return arr

x = [int(i) for i in x]

for i in range(n):
    if x[i] == 0:
        if len(heap) == 0:
            print("0")
        else:
            delete(heap)
    else:
        insert(heap, x[i])
        

            
            