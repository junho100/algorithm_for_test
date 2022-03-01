import copy
from itertools import combinations_with_replacement
import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

graph = []

for _ in range(N):
    graph.append(list(map(int, input().rstrip().split())))

cctvs = []

for i in range(N):
    for j in range(M):
        if graph[i][j] in [1,2,3,4,5]:
            cctvs.append([i, j])
direc = [0, 1,2,3]
cans = list(combinations_with_replacement(direc, len(cctvs)))
result = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            result += 1

for can in cans:
    graph_d = copy.deepcopy(graph)

    def straight(x, y, d):
        if d == 0: # up
            for i in range(x-1, -1, -1):
                if graph_d[i][y] != 6:
                    graph_d[i][y] = -1
                else:
                    break
        elif d == 1: # right
            for i in range(y+1, M):
                if graph_d[x][i] != 6:
                    graph_d[x][i] = -1
                else:
                    break
        elif d == 2: # down
            for i in range(x+1, N):
                if graph_d[i][y] != 6:
                    graph_d[i][y] = -1
                else:
                    break
        elif d == 3: # left
            for i in range(y-1, -1, -1):
                if graph_d[x][i] != 6:
                    graph_d[x][i] = -1
                else:
                    break

    def check(x, y, d):
        if graph[x][y] == 1:
            straight(x, y, d)
        elif graph[x][y] == 2:
            if d == 0 or d == 2:
                straight(x, y, 0)
                straight(x, y, 2)
            elif d == 1 or d == 3:
                straight(x, y, 1)
                straight(x, y, 3)
        elif graph[x][y] == 3:
                if d == 0:
                    straight(x, y, 0)
                    straight(x, y, 1)
                elif d == 1:
                    straight(x, y, 1)
                    straight(x, y, 2)
                elif d == 2:
                    straight(x, y, 2)
                    straight(x, y, 3)
                elif d == 3:
                    straight(x, y, 3)
                    straight(x, y, 0)
        elif graph[x][y] == 4:
            for i in range(4):
                if i == d:
                    continue
                else:
                    straight(x, y, i)
        elif graph[x][y] == 5:
            for i in range(4):
                straight(x, y, i)
    for i in range(len(cctvs)):
        x, y = cctvs[i]

        check(x, y, can[i])
    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph_d[i][j] == 0:
                cnt += 1
    if result > cnt:
        result = cnt
print(result)