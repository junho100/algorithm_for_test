import sys

input = sys.stdin.readline

N = int(input())
edges = []

for i in range(N):
    x, y, z = map(int, input().split())
    edges.append((x, y, z, i))

parent = [i for i in range(N)]

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
cans = []
for i in range(3):
    edges.sort(key = lambda x : x[i])
    for j in range(1, N):
        cans.append((abs(edges[j][i] - edges[j-1][i]), edges[j][3], edges[j-1][3]))

cans.sort(key = lambda x : x[0])
result = 0
cnt = 0
for can in cans:
    cost, x, y = can

    if find_parent(x) != find_parent(y):
        union(x, y)
        result += cost
        cnt += 1

        if cnt == N-1:
            break

print(result)

