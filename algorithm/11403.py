N = int(input())
graph = []
INF = int(1e9)
for _ in range(N):
    d = list(map(int, input().split()))
    for i in range(len(d)):
        if d[i] == 0:
            d[i] = INF
    graph.append(d)

for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(N):
    for j in range(N):
        if graph[i][j] == INF:
            print(0, end = " ")
        else:
            print(1, end = " ")
    print()