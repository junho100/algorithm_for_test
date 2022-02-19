import sys

input = sys.stdin.readline

N, M = map(int, input().split())
INF = int(1e9)
graph = [[INF]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())

    graph[a][b] = 1
    graph[b][a] = 1

for i in range(1, N+1):
    graph[i][i] = 0

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

result = [INF]
for i in range(1, N+1):
    s = 0
    for j in range(1, N+1):
        if i == j:
            continue
        else:
            s += graph[i][j]
    result.append(s)

m = min(result)

for i in range(1, N+1):
    if result[i] == m:
        print(i)
        break