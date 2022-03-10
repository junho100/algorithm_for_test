from collections import deque
import sys

input = sys.stdin.readline
M, N, H = map(int, input().rstrip().split())
graph = []

for _ in range(H):
    t = []
    for _ in range(N):
        t.append(list(map(int, input().rstrip().split())))
    graph.append(t)
visited = [[[False]*M for _ in range(N)] for _ in range(H)]
day = 0
q = deque()
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
result = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 1:
                visited[i][j][k] = True
                q.append((day, (i, j, k)))
while q:
    d, cor = q.popleft()
    z, x, y = cor

    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]

        if nx < 0 or ny < 0 or nz < 0 or nx >= N or ny >= M or nz >= H:
            continue
        if not visited[nz][nx][ny] and graph[nz][nx][ny] == 0:
            visited[nz][nx][ny] = True
            graph[nz][nx][ny] = 1
            q.append((d+1, (nz, nx, ny)))
            result = max(result, d+1)

for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 0:
                print(-1)
                exit()
else:
    print(result)