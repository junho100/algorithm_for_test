import sys 
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []

for _ in range(M):
    a, b, c = map(int, input().split())
    graph.append((c, a, b))

graph.sort()

result = []

parent = [0]*(N+1)
for i in range(1, N+1):
    parent[i] = i

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    
    return parent[x]

def union(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(M):
    c, a, b = graph[i]

    if find_parent(a) != find_parent(b):
        union(a, b)
        result.append(c)
    else:
        continue

print(sum(result[:-1]))