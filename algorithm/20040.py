import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

parent = [i for i in range(n)]

def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(x, y):
    x = find_parent(x)
    y = find_parent(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y

for i in range(m):
    a, b = map(int, input().rstrip().split())

    if find_parent(a) != find_parent(b):
        union(a, b)
    else:
        print(i+1)
        break
else:
    print(0)