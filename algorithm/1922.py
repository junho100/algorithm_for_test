import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
edges = []
for _ in range(M):
    a, b, c = map(int, input().split())

    if a == b:
        continue
    else:
        edges.append((c, a, b))

edges.sort()

parent = [i for i in range(N+1)]

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

result = 0

for edge in edges:
    cost, a, b = edge

    if find_parent(a) != find_parent(b):
        union(a, b)
        result += cost

print(result)