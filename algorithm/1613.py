import sys

input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
INF = int(1e9)
distance = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    distance[i][i] = 0

for _ in range(k):
    a, b = map(int, input().rstrip().split())
    distance[a][b] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

s = int(input().rstrip())

for _ in range(s):
    a, b = map(int, input().rstrip().split())

    if distance[a][b] < INF:
        print(-1)
    elif distance[b][a] < INF:
        print(1)
    else:
        print(0)