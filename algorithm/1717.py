import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000)

n, m = map(int, input().split())
parent = [0]*(n+1)
for i in range(n+1):
    parent[i] = i
def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    
    return parent[x]

def union(x, y):
    x = find_parent(x)
    y = find_parent(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y

for _ in range(m):
    op, a, b = map(int, input().split())

    if op == 0:
        union(a, b)
    elif op == 1:
        if find_parent(a) != find_parent(b):
            print("NO")
        else:
            print("YES")

