import sys

input = sys.stdin.readline

N = int(input().rstrip())
M = int(input().rstrip())
INF = int(1e9)
distance = [[INF]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().rstrip().split())
    distance[a][b] = 1

for i in range(1, N+1):
    distance[i][i] = 0

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

for i in range(1, N+1):
    cnt = 0

    for j in range(1, N+1):
        if i == j:
            continue
        if distance[i][j] >= INF and distance[j][i] >= INF:
            cnt += 1
    print(cnt)