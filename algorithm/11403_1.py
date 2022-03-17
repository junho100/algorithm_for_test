import sys

input = sys.stdin.readline

N = int(input().rstrip())

graph = []

for _ in range(N):
    graph.append(list(map(int, input().rstrip().split())))
INF = int(1e9)
distance = [[INF]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            distance[i][j] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

for i in range(N):
    for j in range(N):
        if distance[i][j] >= INF:
            print(0, end = " ")
        else:
            print(1, end = " ")
    print()