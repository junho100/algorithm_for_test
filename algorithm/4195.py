import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    F = int(input())
    num = dict()
    parent = dict()
    
    def find_parent(x):
        if parent[x] != x:
            parent[x] = find_parent(parent[x])
        return parent[x]
    
    def union(x, y):
        x = find_parent(x)
        y = find_parent(y)
        s = num[x] + num[y]
        if x < y:
            parent[y] = x
        else:
            parent[x] = y
        
        num[y] = s
        num[x] = s
    
    for _ in range(F):
        a, b = input().split()
        if a not in parent:
            parent[a] = a
            num[a] = 1
        if b not in parent:
            parent[b] = b
            num[b] = 1
        
        if find_parent(a) != find_parent(b):
            union(a,b)
        
        print(num[parent[a]])