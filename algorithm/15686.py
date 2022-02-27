from itertools import combinations
import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

graph = []

for _ in range(N):
    graph.append(list(map(int, input().rstrip().split())))

chicks = []
houses = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            houses.append((i, j))
        elif graph[i][j] == 2:
            chicks.append((i, j))

result = int(1e9)

for i in range(1, M+1):
    cans = list(combinations(chicks, i))
    for can in cans:
        tmp = 0
        for house in houses:
            t = int(1e9)
            for c in can:
                t = min(t, abs(c[0] - house[0]) + abs(c[1] - house[1]))
            tmp += t
        result = min(result, tmp)

print(result)