import sys
import threading

def compute_height(n, parents):
    heights = [-1] * n
    
    def height(node):
        if heights[node] != -1:
            return heights[node]
        if parents[node] == -1:
            heights[node] = 1
        else:
            heights[node] = 1 + height(parents[node])
        return heights[node]

    max_height = 0
    for vertex in range(n):
        max_height = max(max_height, height(vertex))
    
    return max_height

def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))

sys.setrecursionlimit(10**7)  
threading.stack_size(2**27)   
threading.Thread(target=main).start()