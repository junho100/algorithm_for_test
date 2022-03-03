import math
import sys

input = sys.stdin.readline

N = int(input().rstrip())
stars = []

for _ in range(N):
    x, y = map(float, input().rstrip().split())
    stars.append([x, y])

edges = []

for i in range(N):
    for j in range(i+1, N):
        x_1, y_1 = stars[i]
        x_2, y_2 = stars[j]
        tmp = math.pow(x_2 - x_1, 2) + math.pow(y_2 - y_1,2)
        distance = math.sqrt(tmp)
        edges.append([distance, i, j])

parent = [i for i in range(N)]

def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(a, b):
    a = find_parent(a)
    b  =find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a]  =b

edges.sort()
result = 0
for edge in edges:
    cost, a, b = edge

    if find_parent(a) != find_parent(b):
        union(a, b)
        result += cost

result = round(result, 2)
print(result)