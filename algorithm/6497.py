import sys

input = sys.stdin.readline

while True:
    M, N = map(int, input().rstrip().split())

    if M == 0 and N ==0:
        break

    parent = [i for i in range(M)]
    result = 0
    edges = []
    for _ in range(N):
        x, y, z = map(int, input().rstrip().split())
        result += z
        edges.append([z, x, y])
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
    
    for edge in edges:
        cost, x, y = edge

        if find_parent(x) != find_parent(y):
            union(x, y)
            result -= cost
    
    print(result)