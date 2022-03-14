import sys
import math

input = sys.stdin.readline

N ,M = map(int, input().rstrip().split())
cors = [[]]

for _ in range(N):
    cors.append(list(map(int, input().rstrip().split())))

parent = [i for i in range(N+1)]

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

for _ in range(M):
    a, b = map(int, input().rstrip().split())
    
    if find_parent(a) != find_parent(b):
        union(a, b)

result = 0
edges = []
for i in range(1, N+1):
    for j in range(i, N+1):
        if find_parent(i) != find_parent(j):
            cost = math.sqrt(math.pow(cors[i][0]-cors[j][0], 2) + math.pow(cors[i][1]-cors[j][1], 2))
            edges.append((cost, i, j))

edges.sort()

for edge in edges:
    cost, a, b = edge

    if find_parent(a) != find_parent(b):
        result += cost
        union(a, b)
print(f"{result:.2f}")