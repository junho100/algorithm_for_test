import sys

input = sys.stdin.readline

N ,M = map(int, input().rstrip().split())
d = list(map(int, input().rstrip().split()))
knows_num = d[0]
knows = d[1:]
parties = []
for _ in range(M):
    tmp = list(map(int, input().rstrip().split()))
    parties.append(tmp[1:])

parent = [i for i in range(N+1)]

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

for i in range(1, knows_num):
    union(knows[i], knows[i-1])
if len(knows) != 0:
    truth = knows[0]
else:
    print(len(parties))
    exit()
for party in parties:
    for i in range(1, len(party)):
        union(party[i], party[i-1])
result = 0
for party in parties:
    check = False
    for i in party:
        if find_parent(i) == find_parent(truth):
            check = True
            break
    if not check:
        result += 1

print(result)