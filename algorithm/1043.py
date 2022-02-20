N, M = map(int, input().split())
parent = [i for i in range(N+1)]

d = list(map(int, input().split()))
true_num = d[0]
true_man = d[1:]

result = 0

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(x,y ):
    x = find_parent(x)
    y = find_parent(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y

for i in range(1, len(true_man)):
    union(true_man[0], i)

for _ in range(M):
    d = list(map(int, input().split()))
    par = d[1:]
    check = False
    for i in range(len(true_man)):
        if true_man[i] in par:
            check = True
            break
    if check:
        for i in par:
            if find_parent(i) != find_parent(true_man[0]):
                union(i, true_man[0])
    else:
        result += 1
        print(par)
        print("-"*10)

print(result)