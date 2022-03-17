from itertools import combinations
import sys

input = sys.stdin.readline
N, M = map(int, input().rstrip().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().rstrip().split())))
INF = int(1e9)
houses = []
chickens = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            houses.append([i, j])
        elif graph[i][j] == 2:
            chickens.append([i,j])
chick_idx = [i for i in range(len(chickens))]

cans = list(combinations(chick_idx, M))
result = INF
for can in cans:
    distance = [INF]*(len(houses))

    for i in range(len(houses)):
        x, y = houses[i]
        for idx in can:
            distance[i] = min(distance[i], abs(x - chickens[idx][0]) + abs(y - chickens[idx][1]))
    result = min(result, sum(distance))
print(result)

