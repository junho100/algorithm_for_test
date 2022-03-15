import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
graph = []

for _ in range(N):
    graph.append(list(input().rstrip()))

parent = [i for i in range(N*M)]

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


for i in range(N*M):
    x = i // M
    y = i % M
    nx = 0
    ny = 0
    if graph[x][y] == "U":
        nx = x -1
        ny = y
    elif graph[x][y] == "D":
        nx = x + 1
        ny = y
    elif graph[x][y] == "L":
        nx = x
        ny = y-1
    else:
        nx = x
        ny = y + 1
    ni = nx*M + ny
    union(i, ni)

visited = dict()
cnt = 0
for i in parent:
    p = find_parent(i)
    if p not in visited:
        visited[p] = True
        cnt += 1

print(cnt)