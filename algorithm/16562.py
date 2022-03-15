import sys

input = sys.stdin.readline

N ,M, k = map(int, input().rstrip().split())
moneys = [0]
tmp = list(map(int, input().rstrip().split()))
moneys += tmp

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

for _ in range(M):
    a, b = map(int, input().rstrip().split())
    union(a, b)

tmp = 0
edges = []
for i in range(1, N+1):
    edges.append((moneys[i], 0, i))

edges.sort()

for edge in edges:
    cost , a, b = edge

    if find_parent(a) != find_parent(b):
        union(a, b)
        tmp += cost

if tmp > k:
    print("Oh no")
else:
    print(tmp)