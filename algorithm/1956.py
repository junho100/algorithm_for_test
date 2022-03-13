import sys

input = sys.stdin.readline

V, E = map(int, input().rstrip().split())
INF = int(1e9)
distance = [[INF]*(V+1) for _ in range(V+1)]
for _ in range(E):
    a, b, c = map(int, input().rstrip().split())
    distance[a][b] = c

for k in range(1, V+1):
    for i in range(1, V+1):
        for j in range(1, V+1):
            distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

result = INF

for i in range(1, V+1):
    result = min(result, distance[i][i])

if result >= INF:
    print(-1)
else:
    print(result)