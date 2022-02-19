import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

parent = [0]*N

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

for i in range(N):
    parent[i] = i

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if graph[i][j] == 1:
            if find_parent(i) == find_parent(j):
                continue
            else:
                union(i, j)

plan = list(map(int, input().split()))
check = True

for i in range(1, M):
    if find_parent(plan[i-1]-1) != find_parent(plan[i]-1):
        check = False

if check:
    print("YES")
else:
    print("NO")