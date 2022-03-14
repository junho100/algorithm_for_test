import sys

input = sys.stdin.readline

N ,M = map(int, input().rstrip().split())
schools = input().rstrip().split()

edges = []

for _ in range(M):
    a, b, c = map(int, input().rstrip().split())

    a -= 1
    b -= 1

    if schools[a] != schools[b]:
        edges.append((c, a, b))

parent = [i for i in range(N)]

edges.sort()

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

result = 0

for edge in edges:
    cost, a, b = edge

    if find_parent(a) != find_parent(b):
        union(a, b)
        result += cost

check = True
for i in range(1, N):
    if find_parent(i-1) != find_parent(i):
        check = False
        break

if check:
    print(result)
else:
    print(-1)