N, M = map(int, input().split())
ops = []
for _ in range(M):
    ops.append(list(map(int, input().split())))
parent = [0]*(N+1)
for i in range(N+1):
    parent[i] = i

def find_parent(x):
    if x != parent[x]:
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
    op, a, b = ops[i]

    if op == 0:
        union(a, b)
    elif op == 1:
        if find_parent(a) != find_parent(b):
            print("NO")
        else:
            print("YES")