import sys

input = sys.stdin.readline

N, M = map(int, input().split())

graph = []

for _ in range(M):
    a, b, c = map(int, input().split())

    graph.append((c, a, b))

A, B = map(int, input().split())

graph.sort(key = lambda x : -x[0])

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

for i in graph:
    cost, a, b = i

    if find_parent(a) != find_parent(b):
        union(a, b)
    
    if find_parent(A) == find_parent(B):
        print(cost)
        break